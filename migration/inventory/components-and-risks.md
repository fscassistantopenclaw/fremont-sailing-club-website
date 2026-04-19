# Repeated Templates, Components, and Risky Features

## Repeated templates / component patterns

These are the main repeated patterns visible in the current Weebly site.

### Global layout components
- Shared header/navigation across nearly every page
- Shared footer/search block across nearly every page
- Shared Weebly theme assets, fonts, and background styling
- Repeated page chrome for title, content container, and menu structure

### Content patterns
- **General info pages**: static prose pages such as The Club, Membership, Useful Links, Fleets
- **Fleet pages**: fleet-specific overview pages such as Lido and El Toro
- **Racing reference pages**: notice of race, sailing instructions, tactics, strategy, rules, race committee guidance
- **Results collections**: landing pages plus many day-by-day or overall result pages
- **Commodore's comments archives**: landing page, year pages, dated post pages, monthly post pages
- **Newsletter archives**: decade pages, year pages, and newsletter listings
- **Photo pages**: gallery pages and slideshow pages with many linked images
- **Historical archive pages**: decade and year pages with club history content

## Risky features for GitHub Pages

GitHub Pages is static hosting, so these items need special handling or replacement.

### 1. Weebly search
- Found on roughly the entire site as a form posting to `/apps/search`
- This will not work on a plain GitHub Pages site
- Recommendation: remove it at first launch, or replace later with a static-search approach only if truly needed

### 2. Weebly contact / comment form
- Found on at least:
  - `membership.html`
  - `lido.html`
  - `el-toro.html`
  - `open.html`
- Posts to `https://www.weebly.com/weebly/apps/formSubmit.php`
- This will not work on GitHub Pages
- Recommendation: replace with a mailto link, Google Form, or a separate trusted form backend

### 3. Weebly theme scripts and runtime dependencies
- Heavy references to `cdn2.editmysite.com` and `cdn11.editmysite.com`
- jQuery and Weebly runtime scripts are included on many pages
- These should not be carried into the rebuilt site unless a specific feature truly depends on them

### 4. Google-hosted content dependencies
- Many links/assets point to Google Drive and Google Forms
- These may be legitimate and can remain if they are intentional, but should be inventoried and confirmed

### 5. Analytics / external scripts
- Google Tag Manager is present
- Needs an explicit decision during rebuild: keep, simplify, or remove

### 6. Gallery/slideshow behavior
- Photo sections include gallery and slideshow pages with many images
- We need to confirm whether the rebuilt site should preserve the exact slideshow behavior or just preserve the image content cleanly

### 7. Duplicate or awkward legacy slugs
- The current site includes inconsistent URLs such as `2025.html`, `20251.html`, `20252.html`, and similar variants
- These may reflect Weebly-generated collisions or legacy edits
- Risk: cleanup could break old links unless redirects or preserved filenames are used

## External dependencies seen during Phase 1

Highest-volume external references found during crawl:
- `cdn2.editmysite.com`
- `cdn11.editmysite.com`
- `drive.google.com`
- `www.googletagmanager.com`

## Migration stance

For the rebuild, the safest default is:
- preserve content
- remove Weebly runtime dependence
- keep external documents only where they are intentional content sources
- replace dynamic forms/search with static-friendly alternatives
