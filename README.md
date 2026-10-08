# Alexander Tong Engineering Portfolio

A statically exported React and Next.js portfolio for GitHub Pages.

## Technology

- Next.js App Router
- React
- JavaScript and CSS
- Static export to `out/`
- GitHub Actions deployment

## Project structure

- `app/` contains the Next.js routes and shared stylesheet.
- `components/` contains the React page and interaction components.
- `content/` contains the portfolio page content preserved from the original HTML site.
- `lib/portfolio-content.js` maps that content to clean Next.js routes.
- `public/Pictures/` contains portfolio images, videos, and the exact-filename guide.
- `public/Resume/` is the resume folder. The build uses the first PDF found there.
- `public/Reports/Alexander_Tong_Technical_Portfolio.pdf` is the four-page technical portfolio, linked from the homepage contact section. This copy is tracked in Git and published with the website; replace it when updating the application portfolio.
- `public/portfolio-*.js` contains the existing launch, carousel, media, and schematic interactions.

## Adding pictures and videos

Open [public/Pictures/README.md](public/Pictures/README.md) for every required filename and folder. Copy a file into the matching location, keeping the filename exactly as shown. Missing media remains visible as an exact-filename placeholder and is replaced automatically after the matching file is added.

Example:

```text
public/Pictures/AIAA/Prototype-1-Assembled.webp
```

### Media layout safeguard

The shared media loader must leave a missing media slot, its caption, and its surrounding carousel or image block visible. Do not hide `.media-slot`, `.project-carousel`, or `.image-block` when a file fails to load. Hiding those elements can remove the Additional Projects section and compress project-page text into a narrow column.

## Updating portfolio content

The homepage content is in `content/index.html`. Each project or experience has a matching file in `content/`, such as `content/project_recovery.html` or `content/plummer.html`.

Internal links can continue to use the familiar HTML filenames inside these content files. The Next.js build converts them to clean routes such as `/project_recovery/`.

## Adding project cards

Add cards to a category container in `content/index.html`. Categories with three or fewer cards remain a grid. Categories with four or more cards use the portfolio carousel automatically.

Rotation begins after half the carousel is visible for three seconds, then advances every four seconds. Scrolling, swiping, clicking, using the keyboard, or pressing an arrow pauses rotation for ten seconds after the most recent interaction.

## Running the site locally

### For future sessions: start here

Open **PowerShell as Administrator**, paste this entire block, and press Enter:

```powershell
Set-Location -LiteralPath "C:\Users\aleto\OneDrive\Documents\Desktop\Gemini_Portfolio"
& "C:\Program Files\nodejs\corepack.cmd" yarn dev
```

Then open [http://localhost:3000](http://localhost:3000). Keep PowerShell open while viewing the portfolio. Press `Ctrl+C` in PowerShell when you want to stop the local website.

### First-time setup or troubleshooting

To open PowerShell as Administrator:

1. Open the Windows Start menu.
2. Search for `PowerShell`.
3. Right-click **Windows PowerShell** and select **Run as administrator**.

PowerShell normally opens in your user folder, which does not contain this project's `package.json`. Change into the portfolio folder before running any Yarn command:

```powershell
cd "C:\Users\aleto\OneDrive\Documents\Desktop\Gemini_Portfolio"
```

The prompt should now begin with:

```text
PS C:\Users\aleto\OneDrive\Documents\Desktop\Gemini_Portfolio>
```

Install [Node.js LTS](https://nodejs.org/en/download) first, then close and reopen PowerShell. Confirm that Node and npm are available:

```powershell
node --version
npm --version
```

If `corepack` is not recognized, install and enable it once:

```powershell
npm install --global corepack
corepack enable
```

Install the project dependencies:

```powershell
yarn install
```

Start the local development site from that folder:

```powershell
corepack yarn dev
```

If `corepack` is not found even after installing it, run:

```powershell
& "C:\Program Files\nodejs\corepack.cmd" yarn dev
```

Then open [http://localhost:3000](http://localhost:3000). Keep PowerShell open while viewing the site. Press `Ctrl+C` in PowerShell to stop the local server.

## Checking the production build

```powershell
yarn build
```

A successful build creates the static website in `out/`.

## Uploading changes to GitHub

The configured repository is [Alex-something-something/portfolio](https://github.com/Alex-something-something/portfolio), using the `main` branch.

Stage the portfolio changes:

```powershell
git add -A
```

The repository’s `.gitignore` already excludes local planning notes, the separate blueprint draft, generated build folders, and the old review screenshot.

Review, save, and upload the changes:

```powershell
git status
git commit -m "Update portfolio"
git push origin main
```

The workflow at `.github/workflows/deploy-pages.yml` builds and publishes the Next.js static export after each push to `main`. In the repository’s **Settings → Pages**, set the source to **GitHub Actions** the first time you deploy.

If a push is rejected because GitHub contains newer work, run:

```powershell
git pull --rebase origin main
git push origin main
```
