# GitHub Pages Deployment Guide

## Current Status

✅ MkDocs is installed and working
✅ Documentation site has been built successfully to `site/` directory
✅ GitHub Actions workflow is configured for automatic deployment

## How to Deploy

### Option 1: Using GitHub Actions (Recommended)

The repository now includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) that will automatically:
1. Build the documentation when you push to the `main` branch
2. Deploy it to GitHub Pages

**Steps:**
1. Ensure git is installed on your local machine
2. Push your changes to GitHub:
   ```bash
   git add .
   git commit -m "Build and deploy documentation"
   git push origin main
   ```
3. The GitHub Actions workflow will automatically build and deploy

### Option 2: Manual Deployment

If you want to deploy manually:

1. **Install Git** (if not already installed):
   - Download from https://git-scm.com/download/win
   - Follow the installation wizard

2. **After Git is installed**, run:
   ```bash
   mkdocs gh-deploy
   ```

### Option 3: Manual Push to gh-pages Branch

1. Build the site:
   ```bash
   python -m mkdocs build
   ```

2. Commit the built `site/` folder to the `gh-pages` branch:
   ```bash
   git add site/
   git commit -m "Deploy documentation"
   git push origin main
   ```

3. Then set GitHub Pages to use the `gh-pages` branch from repository settings

## GitHub Pages Configuration

Make sure your repository settings have GitHub Pages enabled:
1. Go to: Settings → Pages
2. Select source as "Deploy from a branch"
3. Select branch: `gh-pages` (will be created by GitHub Actions)
4. Click Save

## Testing Locally

To test the site locally before deploying:

```bash
python -m mkdocs serve
```

Then open: http://127.0.0.1:8000

## Site URL

Your documentation will be available at:
- https://malmostad.github.io/Verksamhetssystem-RFI/

## Troubleshooting

- **mkdocs command not found**: Use `python -m mkdocs` instead
- **Git not found**: Install Git from https://git-scm.com/download/win
- **GitHub Actions failing**: Check the workflow logs in Settings → Actions
