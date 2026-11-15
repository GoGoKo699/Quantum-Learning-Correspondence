#!/usr/bin/env python3
"""Finite checks for the correspondence learning account.

Run from any directory. Only NumPy and Python's standard library are needed.
The default output is verification/results.json next to this script.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import sys

import numpy as np


I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PAULIS = (X, Y, Z)
TOLERANCE = 2e-11


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def tensor_power(matrix: np.ndarray, number: int) -> np.ndarray:
    result = np.ones((1, 1), dtype=complex)
    for _ in range(number):
        result = np.kron(result, matrix)
    return result


def state_from_correlations(correlations: np.ndarray) -> np.ndarray:
    """rho = (I + sum T_ab sigma_a tensor sigma_b)/4."""
    result = np.eye(4, dtype=complex)
    for a, left in enumerate(PAULIS):
        for b, right in enumerate(PAULIS):
            result += correlations[a, b] * np.kron(left, right)
    return result / 4


def shuffle_outputs(pair_state: np.ndarray, number: int) -> np.ndarray:
    """Direct dense construction, including all number! B permutations."""
    state = tensor_power(pair_state, number).reshape([2] * (4 * number))
    group = list(range(0, 2 * number, 2)) + list(range(1, 2 * number, 2))
    state = state.transpose(group + [axis + 2 * number for axis in group])
    result = np.zeros_like(state)
    for permutation in itertools.permutations(range(number)):
        order = list(range(number)) + [number + index for index in permutation]
        result += state.transpose(order + [axis + 2 * number for axis in order])
    return (result / math.factorial(number)).reshape(4**number, 4**number)


def cycle_coefficient(left: np.ndarray, right: np.ndarray, number: int) -> float:
    """Complete homogeneous coefficient from trace powers of diag(1,T S^T)."""
    product = left @ right.T
    power = np.eye(3)
    power_sums = [0.0]
    for _ in range(number):
        power = power @ product
        power_sums.append(1.0 + float(np.trace(power)))
    coefficients = [1.0]
    for degree in range(1, number + 1):
        coefficients.append(
            sum(power_sums[length] * coefficients[degree - length]
                for length in range(1, degree + 1)) / degree
        )
    return coefficients[number]


def check_cycle_identity() -> dict:
    # The generic sources have noncommuting correlation matrices. This checks
    # the operator contraction beyond simultaneously diagonal Werner examples.
    sources = {
        "generic_a": 0.07 * np.array([[1, 2, -1], [-2, 0.5, 1], [0.3, -1, 2]]),
        "generic_b": 0.08 * np.array([[0.5, -1, 2], [1, 1, -0.5], [-2, 0.2, 1]]),
        "werner_v1": np.eye(3) / 3,
    }
    states = {name: state_from_correlations(matrix) for name, matrix in sources.items()}
    minima = {}
    for name, state in states.items():
        minimum = float(np.linalg.eigvalsh(state).min())
        minima[name] = minimum
        require(minimum > -TOLERANCE, f"Nonphysical density in {name}")
        require(abs(np.trace(state) - 1) < TOLERANCE, f"Trace in {name}")
        tensor = state.reshape(2, 2, 2, 2)
        require(np.max(abs(np.trace(tensor, axis1=0, axis2=2) - I / 2)) < TOLERANCE,
                f"B marginal in {name}")
        require(np.max(abs(np.trace(tensor, axis1=1, axis2=3) - I / 2)) < TOLERANCE,
                f"A marginal in {name}")
    commutator = sources["generic_a"] @ sources["generic_b"] - sources["generic_b"] @ sources["generic_a"]
    require(np.linalg.norm(commutator) > 1e-3, "Generic correlation matrices accidentally commute")
    records = []
    for number in range(1, 5):
        shuffled = {name: shuffle_outputs(state, number) for name, state in states.items()}
        for left_name, right_name in [
            ("generic_a", "generic_b"),
            ("generic_a", "generic_a"),
            ("generic_b", "werner_v1"),
            ("werner_v1", "werner_v1"),
        ]:
            direct = float((4**number * np.trace(shuffled[left_name] @ shuffled[right_name])).real)
            predicted = cycle_coefficient(sources[left_name], sources[right_name], number)
            error = abs(direct - predicted)
            require(error < TOLERANCE, f"Cycle identity: N={number}, {left_name}, {right_name}")
            records.append({"N": number, "left": left_name, "right": right_name,
                            "dense_overlap": direct, "cycle_coefficient": predicted,
                            "absolute_error": error})
    return {"cases": records, "minimum_density_eigenvalues": minima,
            "correlation_commutator_frobenius_norm": float(np.linalg.norm(commutator)),
            "max_absolute_error": max(record["absolute_error"] for record in records)}


def quadratic(label: int, n: int) -> int:
    mask = (1 << n) - 1
    return ((label & mask) & (label >> n)).bit_count() % 2


def symplectic(left: int, right: int, n: int) -> int:
    mask = (1 << n) - 1
    return (((left & mask) & (right >> n)) ^ ((right & mask) & (left >> n))).bit_count() % 2


def pauli(label: int, n: int) -> np.ndarray:
    result = np.ones((1, 1), dtype=complex)
    for bit in reversed(range(n)):
        x, z = (label >> bit) & 1, (label >> (n + bit)) & 1
        factor = {(0, 0): I, (1, 0): X, (0, 1): Z, (1, 1): Y}[x, z]
        result = np.kron(result, factor)
    return result


def augmented_row(label: int, n: int) -> int:
    mask = (1 << n) - 1
    return (label >> n) | ((label & mask) << n) | (1 << (2 * n))


def echelon(rows: list[tuple[int, int]], width: int) -> tuple[int, int | None]:
    pivots: dict[int, tuple[int, int]] = {}
    for coefficient, rhs in rows:
        while coefficient:
            pivot = coefficient.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = (coefficient, rhs)
                break
            previous, previous_rhs = pivots[pivot]
            coefficient ^= previous
            rhs ^= previous_rhs
        else:
            require(rhs == 0, "Inconsistent noiseless demonstration")
    if len(pivots) < width:
        return len(pivots), None
    solution = 0
    for pivot in sorted(pivots):
        coefficient, rhs = pivots[pivot]
        bit = rhs ^ ((coefficient & solution).bit_count() % 2)
        solution |= bit << pivot
    return len(pivots), solution


def check_bell_and_fourier() -> dict:
    records = []
    for n in range(1, 5):
        dimension = 1 << n
        labels = range(dimension**2)
        support = [label for label in labels if quadratic(label, n) == 0]
        require(len(support) == dimension * (dimension + 1) // 2, "Quadratic support size")
        max_fourier_error = Fraction(0)
        for frequency in range(1, dimension**2):
            numerator = sum((-1)**symplectic(frequency, label, n) for label in support)
            observed = Fraction(numerator, len(support))
            expected = Fraction((-1)**quadratic(frequency, n), dimension + 1)
            max_fourier_error = max(max_fourier_error, abs(observed - expected))
        require(max_fourier_error == 0, "Exact support Fourier identity")
        # Check every support translation and every possible affine functional
        # without relying on the floating-point density calculation below.
        maximum_hyperplane_count = 0
        for hidden in labels:
            translated = [label ^ hidden for label in support]
            for frequency in range(1, dimension**2):
                ones = sum(symplectic(frequency, label, n) for label in translated)
                maximum_hyperplane_count = max(maximum_hyperplane_count, ones, len(support) - ones)
            for label in translated:
                require(quadratic(label ^ hidden, n) == 0, "Translated support")
                require(symplectic(label, hidden, n) ^ quadratic(hidden, n) == quadratic(label, n),
                        "Augmented decoding equation")
        hyperplane_mass = Fraction(maximum_hyperplane_count, len(support))
        require(hyperplane_mass == Fraction(dimension + 2, 2 * (dimension + 1)),
                "Affine hyperplane mass")

        bell_basis = np.column_stack([pauli(label, n).T.reshape(-1) / math.sqrt(dimension)
                                      for label in labels])
        require(np.max(abs(bell_basis.conj().T @ bell_basis - np.eye(dimension**2))) < TOLERANCE,
                "Bell basis normalization")
        swap = np.eye(dimension**2).reshape(dimension, dimension, dimension, dimension)
        swap = swap.transpose(1, 0, 2, 3).reshape(dimension**2, dimension**2)
        selected_hidden = sorted({0, 1, dimension + 1, dimension**2 - 1})
        max_bell_error = 0.0
        max_off_diagonal = 0.0
        for hidden in selected_hidden:
            operation = np.kron(np.eye(dimension), pauli(hidden, n))
            state = (np.eye(dimension**2) + operation @ swap @ operation.conj().T)
            state /= dimension * (dimension + 1)
            diagonalized = bell_basis.conj().T @ state @ bell_basis
            probabilities = np.diag(diagonalized).real
            expected = np.array([2 / (dimension * (dimension + 1))
                                 if quadratic(label ^ hidden, n) == 0 else 0 for label in labels])
            max_bell_error = max(max_bell_error, float(np.max(abs(probabilities - expected))))
            max_off_diagonal = max(max_off_diagonal, float(np.max(abs(diagonalized - np.diag(np.diag(diagonalized))))))
            require(abs(np.trace(state) - 1) < TOLERANCE, "Process probe normalization")
        require(max_bell_error < TOLERANCE and max_off_diagonal < TOLERANCE,
                "Physical Bell distribution")
        records.append({"n": n, "d": dimension, "support_size": len(support),
                        "exact_fourier_error": str(max_fourier_error),
                        "maximum_affine_hyperplane_mass": str(hyperplane_mass),
                        "physical_hidden_labels_checked": selected_hidden,
                        "max_bell_probability_error": max_bell_error,
                        "max_bell_off_diagonal": max_off_diagonal})
    return {"cases": records}


def canonical_span(basis: tuple[int, ...], vector: int) -> tuple[int, ...]:
    """Canonical reduced row basis over F_2, represented by small integers."""
    values = list(basis)
    for old in values:
        vector = min(vector, vector ^ old)
    if not vector:
        return basis
    values = [min(old, old ^ vector) for old in values]
    values.append(vector)
    return tuple(sorted(values, reverse=True))


def exact_rank_failure(n: int, number: int) -> Fraction:
    support = [label for label in range(1 << (2 * n)) if quadratic(label, n) == 0]
    rows = [augmented_row(label, n) for label in support]
    counts: dict[tuple[int, ...], int] = {(): 1}
    for _ in range(number):
        updated: dict[tuple[int, ...], int] = {}
        for basis, count in counts.items():
            for row in rows:
                new_basis = canonical_span(basis, row)
                updated[new_basis] = updated.get(new_basis, 0) + count
        counts = updated
    deficient = sum(count for basis, count in counts.items() if len(basis) < 2 * n + 1)
    return Fraction(deficient, len(support)**number)


def check_decoder(seed: int) -> dict:
    rng = np.random.default_rng(seed)
    exact = []
    for n, number in [(1, 3), (1, 8), (2, 5), (2, 12)]:
        failure = exact_rank_failure(n, number)
        d = 1 << n
        bound = min(Fraction(1), (2 * d * d - 2) * Fraction(d + 2, 2 * (d + 1))**number)
        require(failure <= bound, "Exact rank failure exceeds union bound")
        if n == 1:
            coupon_failure = 3 * Fraction(2, 3)**number - 3 * Fraction(1, 3)**number
            require(failure == coupon_failure, "Independent one-qubit coupon formula")
        exact.append({"n": n, "N": number, "rank_failure_exact": str(failure),
                      "rank_failure_decimal": float(failure), "union_upper_bound": float(bound)})
    simulations = []
    trials = 512
    target_delta = 0.05
    for n in range(1, 5):
        d = 1 << n
        p_max = (d + 2) / (2 * (d + 1))
        number = math.ceil(math.log((2 * d*d - 2) / target_delta) / -math.log(p_max))
        zero_support = np.array([label for label in range(d*d) if quadratic(label, n) == 0], dtype=np.int64)
        full_rank = 0
        wrong_full_rank_outputs = 0
        for _ in range(trials):
            hidden = int(rng.integers(d*d))
            examples = np.asarray(rng.choice(zero_support, size=number), dtype=np.int64) ^ hidden
            rank, solution = echelon([(augmented_row(int(label), n), quadratic(int(label), n))
                                      for label in examples], 2 * n + 1)
            if rank == 2 * n + 1:
                full_rank += 1
                expected = hidden | (quadratic(hidden, n) << (2 * n))
                wrong_full_rank_outputs += int(solution != expected)
        require(wrong_full_rank_outputs == 0, "Full-rank learner returned incorrect Pauli")
        simulations.append({"n": n, "d": d, "N": number, "trials": trials,
                            "full_rank_trials": full_rank,
                            "wrong_full_rank_outputs": wrong_full_rank_outputs,
                            "analytical_rank_failure_upper_bound": (2*d*d - 2) * p_max**number})
    return {"seed": seed, "exact_rank_cases": exact, "seeded_decoder_cases": simulations,
            "simulation_interpretation": "Observed trials illustrate the decoder; the analytical rank bound, not a passing simulation frequency, supplies its universal guarantee."}


def check_constants() -> dict:
    cases = []
    for n in range(1, 17):
        d = 1 << n
        p = d*d - 1
        t_squared = 1 / (d + 1)**2
        log_constant = -p * math.log1p(-t_squared)
        analytic_log_upper = (d*d - 1) / (d*d + 2*d)
        require(log_constant <= analytic_log_upper + 1e-14 < 1, "C_d < e bound")
        constant = math.exp(log_constant)
        cases.append({"n": n, "d": d, "C_d": constant,
                      "log_C_d_upper_bound": analytic_log_upper,
                      "guessing_upper_bound": math.sqrt(constant) / d,
                      "average_gate_fidelity_upper_bound": (math.sqrt(constant) + 1) / (d + 1)})
    return {"cases": cases}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    parser.add_argument("--seed", type=int, default=20261115)
    args = parser.parse_args()
    results = {
        "status": "passed",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "environment": {"python": platform.python_version(), "numpy": np.__version__, "platform": platform.platform()},
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "floating_point_tolerance": TOLERANCE,
        "cycle_identity": check_cycle_identity(),
        "bell_and_fourier": check_bell_and_fourier(),
        "paired_decoder": check_decoder(args.seed),
        "finite_constants": check_constants(),
        "scope": "Small dense quantum-state checks, exact finite binary-field enumeration, exact rational small-rank distributions, and seeded decoder demonstrations. These do not numerically certify the all-N theorem, exhaustive novelty, physical hardware, or optimal implementation complexity.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": results["status"], "output": str(args.output),
                      "max_cycle_error": results["cycle_identity"]["max_absolute_error"],
                      "bell_n_values": [case["n"] for case in results["bell_and_fourier"]["cases"]],
                      "seed": args.seed}))


if __name__ == "__main__":
    main()
