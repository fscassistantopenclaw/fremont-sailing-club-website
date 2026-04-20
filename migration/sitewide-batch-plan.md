# Sitewide Migration Batch Plan

Date: 2026-04-19
Status: planning only

## Guiding approach

- Keep commits small and reviewable
- Reuse the same static-first, no-runtime principles used on the homepage
- Preserve content and legacy filenames where practical
- Simplify navigation where needed, but not content
- Pause for approval when a major architectural or design decision appears

## Proposed migration batches

### Batch 1, shared shell and homepage menu integration
- Add a sitewide menu structure to the homepage
- Build reusable header/footer/navigation patterns for the rest of the site
- Keep this commit focused on shared structure only

### Batch 2, core club information pages
Candidate pages:
- `the-club.html`
- `membership.html`
- `by-laws.html`
- `useful-links.html`
- `officers--fleet-captains.html`

Why this batch:
- high-value reader-facing pages
- mostly standard content pages
- validates the standard content-page pattern

### Batch 3, fleets section
Candidate pages:
- `fleets.html`
- `lido.html`
- `el-toro.html`
- `open.html`

Why this batch:
- logically grouped
- similar page type
- includes simple outbound references but no runtime features we need to keep

### Batch 4, racing overview and core documents
Candidate pages:
- `racing.html` / `racing1.html` as needed after source review
- `2026-notice-of-race.html`
- `2026-sailing-instructions.html`
- `results.html`
- `2023-calendar-562573-358418.html`

Why this batch:
- gives the site a usable racing hub early
- surfaces document-link handling and structured navigation

### Batch 5, recent racing results
Candidate pages:
- recent result pages for 2026 and 2025 first
- related overall pages

Why this batch:
- recent content matters most to members
- can be migrated in a compact, recent-first chunk

### Batch 6, Commodore's Comments
Candidate pages:
- `commodores-comments.html`
- 2026 and 2025 comment pages first
- then older archives in later chunks

Why this batch:
- strong reader value
- same content pattern repeated many times

### Batch 7, Windjammer newsletters and archive landing pages
Candidate pages:
- `windjammer-newsletter.html`
- decade landing pages
- then year pages in grouped chunks

Why this batch:
- archive-heavy section that benefits from clearer structure
- likely easier to maintain with a shared archive template

### Batch 8, photos
Candidate pages:
- `photos.html`
- `2024-photo-gallery.html`
- other gallery/slideshow pages in grouped commits

Why this batch:
- lets us settle on one clean photo pattern and apply it consistently

### Batch 9+, deep archives and long tail
Candidate pages:
- decade history pages
- year archive pages
- older results, newsletters, and historical content not already covered

Why this batch:
- lower urgency than member-facing current information
- can be migrated in calm, decade-by-decade or section-by-section chunks

## Commit style

Each commit should ideally do one of these things:
- add or refine shared structure
- migrate one page family
- migrate one archive cluster
- clean up links or assets for one clearly scoped section

That keeps review practical and rollback easy.

## Major architecture question still open

Migrating the rest of the site cleanly with shared menus, archive landing pages, and many content pages is much easier if I install **Eleventy** and move from ad hoc flat HTML files to a tiny static-site workflow.

I have not installed it yet.

If approved, the benefit would be:
- shared nav/footer/includes across the whole site
- easier small commits
- cleaner archive pages
- less duplicated HTML

If not approved, I can keep going with plain hand-authored static HTML, but the migration will be slower and the maintenance burden will be higher.
