const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { chromium } = require('playwright');
const output = process.argv[2];
if (!output) throw new Error('Pass a new output directory');
fs.mkdirSync(output, { recursive: false });
const sources = [
  ['GoGoKo699/Quantum-Learning-Readout', 'b4c5ffcc0745137db36ca1ff02d60934378c6ff8', 'learning/MILESTONES.md'],
  ['GoGoKo699/Quantum-Learning-Readout', 'b4c5ffcc0745137db36ca1ff02d60934378c6ff8', 'learning/TUTORIAL.md'],
  ['GoGoKo699/Quantum-Learning-Readout', 'b4c5ffcc0745137db36ca1ff02d60934378c6ff8', 'references/related_work.md'],
  ['GoGoKo699/Quantum-Learning-Correspondence', 'd6aeb84d4ed4d6c666703c6878ba7a0e627e4046', 'learning/MILESTONES.md'],
  ['GoGoKo699/Quantum-Learning-Correspondence', 'd6aeb84d4ed4d6c666703c6878ba7a0e627e4046', 'science/separate-list-readout.md']
];
(async () => {
  const browser = await chromium.launch({ headless: true });
  const report = { kind: 'supplemental_top_capture', captured_at: new Date().toISOString(), scope: 'Fresh top-of-page view only; supplements canonical complete MathML/source captures and is not a replacement for them.', pages: [] };
  try {
    for (const [repository, revision, pagePath] of sources) for (const width of [1440, 760]) {
      const context = await browser.newContext({ viewport: { width, height: 1800 } });
      const page = await context.newPage();
      const url = `https://github.com/${repository}/blob/${revision}/${pagePath}`;
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
      if (page.url() !== url) throw new Error('Unexpected navigation: ' + page.url());
      const article = page.locator('article').first();
      await article.locator('h1').first().waitFor({ state: 'visible', timeout: 30000 });
      await page.evaluate(async () => {
        await Promise.race([document.fonts.ready, new Promise((_, reject) => setTimeout(() => reject(new Error('font readiness timed out')), 15000))]);
        window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
        await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
      });
      await page.waitForTimeout(1000);
      const observations = await article.evaluate(el => ({ heading: el.querySelector('h1')?.textContent, introduction: el.innerText.slice(0, 1800), viewport: { width: innerWidth, height: innerHeight }, scrollY }));
      if (observations.scrollY !== 0 || observations.viewport.width !== width) throw new Error('Wrong supplemental viewport or scroll position');
      const file = `${repository.split('/')[1]}-${pagePath.replaceAll('/', '_')}-${width}.png`;
      await page.screenshot({ path: path.join(output, file), fullPage: false });
      const bytes = fs.readFileSync(path.join(output, file));
      report.pages.push({ repository, revision, path: pagePath, url, width, observed_at: new Date().toISOString(), observations, screenshot: { path: file, size: bytes.length, sha256: crypto.createHash('sha256').update(bytes).digest('hex') } });
      await context.close();
    }
    fs.writeFileSync(path.join(output, 'supplemental-report.json'), JSON.stringify(report, null, 2) + '\n');
  } finally { await browser.close(); }
})().catch(error => { console.error(error.stack); process.exitCode = 1; });
