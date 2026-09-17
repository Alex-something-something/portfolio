import fs from 'node:fs';
import path from 'node:path';

const contentDirectory = path.join(process.cwd(), 'content');

export const portfolioPages = {
  appt: 'appt.html',
  cossmo: 'cossmo.html',
  culturon: 'culturon.html',
  dbf: 'dbf.html',
  manufacturing: 'manufacturing.html',
  me360: 'me360.html',
  plummer: 'plummer.html',
  project_aerocover: 'project_aerocover.html',
  project_co2: 'project_co2.html',
  project_nozzle: 'project_nozzle.html',
  project_recovery: 'project_recovery.html',
  project_vacuum: 'project_vacuum.html',
  robot: 'robot.html'
};

function firstResumeFilename() {
  const resumeDirectory = path.join(process.cwd(), 'public', 'Resume');
  if (!fs.existsSync(resumeDirectory)) return 'Alexander_Tong_Resume.pdf';
  return fs.readdirSync(resumeDirectory).find((file) => file.toLowerCase().endsWith('.pdf'))
    ?? 'Alexander_Tong_Resume.pdf';
}

function routeForHtml(filename, isHome, hash = '') {
  const pageName = filename.replace(/\.html$/i, '');
  if (pageName === 'index') return isHome ? (hash || './') : `../${hash}`;
  return isHome ? `${pageName}/${hash}` : `../${pageName}/${hash}`;
}

function rewritePaths(markup, isHome) {
  const assetPrefix = isHome ? '' : '../';

  return markup
    .replace(/href="([^"#?]+\.html)(#[^"]*)?"/gi, (_, filename, hash = '') => {
      return `href="${routeForHtml(filename, isHome, hash)}"`;
    })
    .replace(/data-media="Pictures\//gi, `data-media="${assetPrefix}Pictures/`)
    .replace(/href="Alexander_Tong_Resume\.pdf"/gi, `href="${assetPrefix}Resume/${firstResumeFilename()}"`);
}

function addBottomReturn(markup) {
  const backLink = markup.match(/<a\b(?=[^>]*\bclass="[^"]*\bback-link\b[^"]*")[^>]*>[\s\S]*?<\/a>/i)?.[0];
  if (!backLink) return markup;

  const bottomReturn = `<div class="detail-return" aria-label="Return navigation">${backLink}</div>`;
  return markup.replace(/<footer\b/i, `${bottomReturn}\n<footer`);
}

export function readPortfolioPage(filename, isHome = false) {
  const source = fs.readFileSync(path.join(contentDirectory, filename), 'utf8');
  const title = source.match(/<title>([\s\S]*?)<\/title>/i)?.[1].trim()
    ?? 'Alexander Tong Engineering Portfolio';
  const styles = [...source.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/gi)]
    .map((match) => match[1])
    .join('\n');
  const body = source.match(/<body[^>]*>([\s\S]*?)<\/body>/i)?.[1] ?? '';
  const withoutScripts = body.replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, '');

  const rewrittenBody = rewritePaths(withoutScripts, isHome);

  return {
    title,
    styles,
    body: isHome ? rewrittenBody : addBottomReturn(rewrittenBody)
  };
}
