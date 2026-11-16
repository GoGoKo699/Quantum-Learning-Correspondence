#!/usr/bin/env python3
"""Finite normalization checks for the anonymous-batch Fourier proof.

Uses NumPy and the standard library only. No receiver is synthesized here.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform

import numpy as np

I2 = np.eye(2, dtype=complex)
P = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.diag([1, -1]).astype(complex),
)
TOL = 3e-10
V = 0.5
T_SCALE = V / (2 + V)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def exp_pauli(vector: np.ndarray) -> np.ndarray:
    length = float(np.linalg.norm(vector))
    if length == 0:
        return I2.copy()
    hermitian = sum((value * matrix for value, matrix in zip(vector, P)), np.zeros((2, 2), dtype=complex))
    return math.cos(length) * I2 + 1j * math.sin(length) / length * hermitian


def tensor_power(matrix: np.ndarray, number: int) -> np.ndarray:
    answer = np.ones((1, 1), dtype=complex)
    for _ in range(number):
        answer = np.kron(answer, matrix)
    return answer


def rho_from_t(correlations: np.ndarray) -> np.ndarray:
    answer = np.eye(4, dtype=complex)
    for a in range(3):
        for b in range(3):
            answer += correlations[a, b] * np.kron(P[a], P[b])
    return answer / 4


def anonymous_dense(pair: np.ndarray, number: int) -> np.ndarray:
    state = tensor_power(pair, number).reshape([2] * (4 * number))
    group = list(range(0, 2 * number, 2)) + list(range(1, 2 * number, 2))
    state = state.transpose(group + [axis + 2 * number for axis in group])
    answer = np.zeros_like(state)
    for permutation in itertools.permutations(range(number)):
        order = list(range(number)) + [number + index for index in permutation]
        answer += state.transpose(order + [axis + 2 * number for axis in order])
    return (answer / math.factorial(number)).reshape(4**number, 4**number)


def dictionary() -> np.ndarray:
    e = np.eye(3)
    bases = [np.concatenate([e[a], e[a]]) for a in range(3)]
    bases += [np.concatenate([e[a], e[(a + 1) % 3]]) for a in range(3)]
    bases += [np.concatenate([(e[0] + e[1]) / math.sqrt(2), (e[1] + e[2]) / math.sqrt(2)])]
    return np.asarray([np.zeros(6)] + [sign * vector for vector in bases for sign in (1, -1)])


FREQUENCIES = dictionary()


def fourier_dense(frequency: np.ndarray, number: int) -> np.ndarray:
    left = tensor_power(exp_pauli(frequency[:3] / math.sqrt(number)), number)
    right = tensor_power(exp_pauli(frequency[3:] / math.sqrt(number)), number)
    return np.kron(left, right)


def characteristic_finite(pair: np.ndarray, frequency: np.ndarray, number: int) -> complex:
    local = np.kron(exp_pauli(frequency[:3] / math.sqrt(number)),
                    exp_pauli(frequency[3:] / math.sqrt(number)))
    return complex(np.trace(pair @ local)) ** number


def gram_finite(number: int) -> np.ndarray:
    local_a = [exp_pauli(f[:3] / math.sqrt(number)) for f in FREQUENCIES]
    local_b = [exp_pauli(f[3:] / math.sqrt(number)) for f in FREQUENCIES]
    return np.asarray([[(np.trace(a.conj().T @ aa) / 2 * np.trace(b.conj().T @ bb) / 2) ** number
                        for aa, bb in zip(local_a, local_b)]
                       for a, b in zip(local_a, local_b)])


def gram_gaussian() -> np.ndarray:
    differences = FREQUENCIES[:, None, :] - FREQUENCIES[None, :, :]
    return np.exp(-np.sum(differences**2, axis=2) / 2)


def char_gaussian(correlations: np.ndarray) -> np.ndarray:
    return np.asarray([math.exp(-(float(f @ f) + 2 * float(f[:3] @ correlations @ f[3:])) / 2)
                       for f in FREQUENCIES])


def self_kernel(number: int) -> float:
    return math.fsum(math.comb(k + 2, 2) * T_SCALE ** (2 * k) for k in range(number + 1))


def correlations_of(unitary: np.ndarray) -> np.ndarray:
    return T_SCALE * np.asarray([[np.trace(P[b] @ unitary @ P[a] @ unitary.conj().T).real / 2
                                  for b in range(3)] for a in range(3)])


def max_local_commutator(number: int) -> float:
    vectors = np.unique(np.vstack([FREQUENCIES[:, :3], FREQUENCIES[:, 3:]]), axis=0)
    local = [exp_pauli(x / math.sqrt(number)) for x in vectors]
    maximum = 0.0
    for u, v in itertools.combinations(local, 2):
        inner = complex(np.trace(v.conj().T @ u.conj().T @ v @ u) / 2)
        squared = max(0.0, 2 - 2 * (inner**number).real)
        maximum = max(maximum, math.sqrt(squared))
    return maximum


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('fourier_saturation_results.json'),
                        help='JSON result path (default: beside this script)')
    args = parser.parse_args()
    unitaries = {
        'identity': I2,
        'rotation_x_0.41': exp_pauli(np.array([0.41, 0, 0])),
        'rotation_z_0.63': exp_pauli(np.array([0, 0, 0.63])),
    }
    commutator = np.linalg.norm(unitaries['rotation_x_0.41'] @ unitaries['rotation_z_0.63']
                                - unitaries['rotation_z_0.63'] @ unitaries['rotation_x_0.41'])
    require(commutator > 0.1, 'Hypothesis unitaries must not commute')
    g = gram_gaussian()
    eigenvalues = np.linalg.eigvalsh(g)
    condition = float(eigenvalues.max() / eigenvalues.min())
    require(eigenvalues.min() > 1e-6 and condition < 1e6, 'Unstable fixed dictionary')
    dense_records = []
    residual_records = []
    n_values = (1, 2, 3, 4, 8, 16, 64, 256, 1024, 4096, 16384)
    grams = {n: gram_finite(n) for n in n_values}
    maximum_gram_error = 0.0
    for n in (1, 2, 3):
        operators = [fourier_dense(f, n) for f in FREQUENCIES]
        direct_g = np.asarray([[np.trace(a.conj().T @ b) / (4**n) for b in operators] for a in operators])
        maximum_gram_error = max(maximum_gram_error, float(np.max(abs(direct_g - grams[n]))))
    require(maximum_gram_error < TOL, 'Finite Fourier Gram identity')
    swap = np.asarray([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
    limiting_kernel = (1 - T_SCALE**2) ** -3
    for label, unitary in unitaries.items():
        correlations = correlations_of(unitary)
        pair = rho_from_t(correlations)
        target_operation = np.kron(I2, unitary)
        swap_pair = (np.eye(4) + V * target_operation @ swap @ target_operation.conj().T) / (2 * (2 + V))
        require(np.max(abs(pair - swap_pair)) < TOL, 'Source orientation / normalization')
        require(np.linalg.eigvalsh(pair).min() > 0, 'Full-rank pair source')
        b_gaussian = char_gaussian(correlations)
        coefficients = np.linalg.solve(g, b_gaussian)
        limiting_residual = float(limiting_kernel - 2 * np.vdot(coefficients, b_gaussian).real
                                  + np.vdot(coefficients, g @ coefficients).real)
        require(limiting_residual > 0, 'Dictionary must have nontrivial approximation residual')
        per_n = []
        for n in n_values:
            b = np.asarray([characteristic_finite(pair, -f, n) for f in FREQUENCIES])
            finite_residual = float(self_kernel(n) - 2 * np.vdot(coefficients, b).real
                                    + np.vdot(coefficients, grams[n] @ coefficients).real)
            require(finite_residual > -TOL, 'Squared L2 residual cannot be negative')
            per_n.append({'N': n, 'finite_fourier_L2_residual_squared': finite_residual,
                          'Gaussian_L2_residual_squared': limiting_residual,
                          'absolute_limit_difference': abs(finite_residual - limiting_residual),
                          'kernel': self_kernel(n)})
            if n <= 3:
                omega = anonymous_dense(pair, n)
                operators = [fourier_dense(f, n) for f in FREQUENCIES]
                expectations = np.asarray([np.trace(omega @ operator.conj().T) for operator in operators])
                expectation_error = float(np.max(abs(expectations - b)))
                direct_kernel = float((4**n * np.trace(omega @ omega)).real)
                q = sum((coefficient * operator for coefficient, operator in zip(coefficients, operators)),
                        np.zeros_like(omega))
                difference = 4**n * omega - q
                direct_residual = float((np.trace(difference.conj().T @ difference) / (4**n)).real)
                residual_error = abs(direct_residual - finite_residual)
                kernel_error = abs(direct_kernel - self_kernel(n))
                require(max(expectation_error, residual_error, kernel_error) < TOL,
                        'Direct dense saturation identity')
                dense_records.append({'unitary': label, 'N': n,
                                      'max_characteristic_identity_error': expectation_error,
                                      'kernel_identity_error': kernel_error,
                                      'direct_L2_residual_identity_error': residual_error})
        require(per_n[-1]['absolute_limit_difference'] < 5e-4, 'Large-N Gaussian residual agreement')
        require(per_n[-1]['absolute_limit_difference'] < per_n[0]['absolute_limit_difference'] / 100,
                'Residual limit discrepancy must shrink substantially')
        residual_records.append({'unitary': label, 'correlations': correlations.tolist(),
                                 'Gaussian_projection_coefficients': coefficients.tolist(), 'cases': per_n})
    commutators = [{'N': n, 'max_exact_tensor_formula_normalized_HS_commutator': max_local_commutator(n)}
                   for n in n_values]
    require(commutators[-1]['max_exact_tensor_formula_normalized_HS_commutator'] < 0.03,
            'Local Fourier family finite commutator diagnostic')
    result = {
        'status': 'passed', 'generated_at_utc': datetime.now(timezone.utc).isoformat(),
        'baseline_source_pins': {'Readout': 'ce61966034a9b72ba1c846a354f8034f5e1a9285',
                        'Correspondence': '00d19bd0f60c6cd34ce4b77bb3268e52120efead'},
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'source_pin_scope': 'Historical source revisions supplying the original pair model and collision kernel; these are not current integration-revision or hosted-rendering receipts.',
        'environment': {'python': platform.python_version(), 'numpy': np.__version__},
        'dimension': 2, 'visibility': V, 'correlation_singular_value': T_SCALE,
        'floating_tolerance': TOL, 'noncommuting_hypotheses_commutator_frobenius': float(commutator),
        'dictionary': FREQUENCIES.tolist(), 'Gaussian_Gram_condition_number': condition,
        'Gaussian_Gram_minimum_eigenvalue': float(eigenvalues.min()),
        'max_dense_Gram_identity_error': maximum_gram_error,
        'dense_cases': dense_records, 'finite_residuals': residual_records,
        'local_commutator_diagnostic': commutators,
        'scope': 'Deterministic d=2 v=1/2 checks. Direct anonymous density matrices for N=1,2,3 and three noncommuting unitary hypotheses verify Fourier expectations, Gram normalization, collision self-kernel and full L2 residual identity. Fixed-dictionary residuals are evaluated through N=16384 with exact finite kernel/characteristic/Gram formulas and compared with their Gaussian limits.',
        'limitations': 'No commuting approximants or Glebsky receiver are numerically constructed. These finite checks support identities and normalization only. They do not prove operational sufficiency, all-parameter uniformity, entropy continuity, asymptotic rates, Fisher-information convergence, efficient measurement implementation, or novelty.'
    }
    output = args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'output': str(output), 'dense_cases': len(dense_records),
                      'max_dense_Gram_identity_error': maximum_gram_error,
                      'max_final_residual_limit_difference': max(x['cases'][-1]['absolute_limit_difference'] for x in residual_records),
                      'Gaussian_Gram_condition_number': condition}))


if __name__ == '__main__':
    main()
