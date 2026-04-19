# Recommended Target Architecture

## Recommendation

Use **Eleventy** as a very small static site generator, with:
- plain HTML templates
- shared includes/layouts
- plain CSS
- very light vanilla JavaScript only when necessary
- GitHub Pages deployment via GitHub Actions

## Why this is the simplest maintainable option

The current site has 173 indexed pages and a large repeated navigation structure. Rebuilding that as completely hand-maintained flat HTML would preserve simplicity at first, but it would create a lot of duplicate markup and make future updates painful.

Eleventy is a good middle ground:
- much simpler than a SPA or framework-heavy stack
- good for content-heavy static sites
- easy to read in generated output and source templates
- good support for shared navigation, archive templates, and reusable partials
- easy to keep URLs stable

## Proposed shape

- `src/layouts/` for page shells
- `src/includes/` for header, footer, navigation, cards, and archive lists
- `src/pages/` for migrated page content and archive pages
- `src/data/` for shared nav and structured club metadata
- `src/assets/` for local CSS, images, and optional light JS

## What not to do

To stay readable and low-risk, I do **not** recommend:
- React/Vue/Next/Nuxt style app frameworks
- client-side rendering for core content
- importing Weebly runtime scripts into the new site
- a complex CSS pipeline unless the club explicitly wants one later

## GitHub Pages fit

GitHub Pages can host the built static output cleanly. Because Eleventy needs a build step, the clean deployment path is:
- source in this repo
- GitHub Actions builds the site
- Pages serves the static output

## Open questions for Phase 2+

- Should the rebuilt site preserve the exact current menu structure, or is light cleanup allowed where duplicate legacy links exist?
- Should the photo sections remain separate gallery and slideshow pages, or can they be simplified while preserving content?
- Should analytics stay?
- What should replace Weebly forms and search?

## Approval needed before setup

I have not installed Eleventy or any new dependency yet.
If you approve Phase 2 later, I will first explain the exact install step before doing it.
