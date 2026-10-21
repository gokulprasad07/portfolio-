# Gokul Prasad M, Portfolio
Vanilla HTML, CSS and JavaScript. No build step, no dependencies.

## Run locally
Open the folder in VS Code, install the **Live Server** extension, right-click `index.html` and choose *Open with Live Server*. Test responsive layouts with browser DevTools (Ctrl+Shift+M).

## Edit your content (all in `js/projects.js`)
- `PROFILE`: email, GitHub, LinkedIn, resume path. Empty values show as "not added yet" and never as dead links.
- `SKILLS`, `PROJECTS`, `CREATIVE`.
- Experience and education text lives in `index.html`; yellow `[placeholders]` mark what you must fill in (company dates, internship organization, grades).

## Add a project
Copy an entry in `PROJECTS`, give it a unique `id`, and put files under `projects/<name>/`. Fill `links` with real relative paths or URLs, e.g. `"Notebook": "projects/tourist-analytics/analysis.ipynb"`, `"Source Code": "https://github.com/you/repo"`. Keys: Source Code, Live Demo, Documentation, Dataset, Notebook, Report. Only label something Live Demo if it is actually hosted.

## Add creative work
Put images in `assets/images/` (use ~800px thumbnails, link the full file as `src`) and add `{ title, category, type: "image", src, thumb, description }` to `CREATIVE`. Use `type: "video"` for mp4. Don't publish confidential client work.

## Deploy
- **GitHub Pages:** push to a repo, Settings > Pages > deploy from `main` / root.
- **Netlify:** drag the folder onto app.netlify.com/drop.
Use relative paths only (`assets/...`). Paths like `C:\Users\...` break on other devices. Python notebooks or backends need separate hosting (Colab, Render, Hugging Face Spaces); link to them as Live Demo.

## Contact form
None included, because a frontend-only form cannot send mail. Add Formspree or Netlify Forms if wanted.
