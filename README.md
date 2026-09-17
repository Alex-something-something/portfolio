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
- `public/portfolio-*.js` contains the existing launch, carousel, media, and schematic interactions.

## Adding pictures and videos

Open [public/Pictures/README.md](public/Pictures/README.md) for every required filename and folder. Copy a file into the matching location, keeping the filename exactly as shown. Empty media slots display the same path on the website.

Example:

```text
public/Pictures/Recovery/Assembly.png
```

## Updating portfolio content

The homepage content is in `content/index.html`. Each project or experience has a matching file in `content/`, such as `content/project_recovery.html` or `content/plummer.html`.

Internal links can continue to use the familiar HTML filenames inside these content files. The Next.js build converts them to clean routes such as `/project_recovery/`.

## Adding project cards

Add cards to a category container in `content/index.html`. Categories with three or fewer cards remain a grid. Categories with four or more cards use the portfolio carousel automatically.

Rotation begins after half the carousel is visible for three seconds, then advances every four seconds. Scrolling, swiping, clicking, using the keyboard, or pressing an arrow pauses rotation for ten seconds after the most recent interaction.

## Running the site locally

Open PowerShell in this folder:

```powershell
cd "C:\Users\aleto\OneDrive\Documents\Desktop\Gemini_Portfolio"
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

Start the local development site:

```powershell
yarn dev
```

Then open `http://localhost:3000`.

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
