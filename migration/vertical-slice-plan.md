# Vertical-Slice Migration Proposal

Date: 2026-04-19
Status: Proposal only, not approved for implementation

## Confirmed constraints from the user

- Focus on static content for the first version
- Do not implement search, comments, contact forms, email handlers, or other runtime scripts
- Do not carry over Weebly runtime/theme dependencies
- Minimalist styling is acceptable, content fidelity matters more than copying the original visual style
- Google Drive and Google Forms links are acceptable if access works
- No analytics for now
- Photo pages should remain visually organized, slideshow or another clean gallery pattern is acceptable

## Proposed vertical slices

### Slice 1, homepage
**Goal**
- Prove the new shared site shell, navigation, typography, homepage content blocks, and event/news layout

**Likely source material needed**
- `index.html`
- homepage hero/background image(s)
- homepage logo/banner assets if any
- links to current calendar, membership page, Commodore's Comments, and featured event links

**Target code structure**
- shared base layout
- shared site header/navigation
- homepage template
- shared footer
- local CSS for typography, spacing, cards, and responsive layout

**Approval choices needed**
- How closely should the new homepage preserve the current section order?
- Should the homepage stay text-forward and simple, or should it include a stronger visual hero section?
- Should upcoming events remain manually edited content for now, or should we simplify to a few static featured links?

### Slice 2, one standard content page
**Candidate page**
- `the-club.html`

**Why this page**
- It is representative, content-first, and free of special runtime behavior

**Likely source material needed**
- page HTML content from `the-club.html`
- any inline images used on that page
- links referenced from the content, such as Membership and Windjammer Newsletter

**Target code structure**
- shared base layout
- reusable standard content-page template
- content body with headings, paragraphs, and linked cards or callouts where useful

**Approval choices needed**
- Do you want these standard pages migrated with very light editorial cleanup, or as close to the current wording/structure as possible?
- Is it okay to convert some raw link lists into clearer callout blocks if content stays the same?

### Slice 3, one photo-heavy page
**Candidate page**
- `2024-photo-gallery.html`

**Why this page**
- It tests image handling, gallery presentation, and photo-page styling without forcing the entire site migration first

**Likely source material needed**
- page content and title
- all images referenced by that gallery page
- any captions or grouping metadata that can be extracted cleanly

**Target code structure**
- shared base layout
- reusable gallery/slideshow page template
- image collection data for the page
- local CSS and optional minimal vanilla JS only if needed for a clean slideshow or lightbox behavior

**Approval choices needed**
- Preferred presentation for v1:
  - simple slideshow
  - clean thumbnail gallery with click-to-expand
  - hybrid gallery plus lightbox
- Should captions be preserved exactly where available, or only when clearly present in source content?

### Slice 4, one page with downloadable documents
**Candidate page**
- `membership.html`

**Why this page**
- It includes downloadable and outbound document links and also exposes the form/runtime problem clearly

**Likely source material needed**
- page HTML content
- Google Drive printable-form link
- Google Form online-form link
- any surrounding explanatory text

**Target code structure**
- shared base layout
- standard content-page template
- document/action link list or card group for downloads and external forms
- no rebuilt onsite form for v1

**Approval choices needed**
- Is it acceptable for v1 to replace the old embedded/contact form section with a short note plus external Google Form link only?
- Do you want download links shown as plain buttons/cards, or as a simpler text list?

## Shared code we would create across all slices

If approved, these slices would establish the reusable foundation:
- base layout
- global navigation
- footer
- global CSS
- standard content-page template
- gallery/photo template
- small shared component set for cards, buttons, callouts, and file links

## Proposed implementation order

1. Homepage
2. Standard content page (`the-club.html`)
3. Photo-heavy page (`2024-photo-gallery.html`)
4. Downloadable-documents page (`membership.html`)

## Why this order

- It builds the shared shell first
- Then proves clean migration of ordinary prose content
- Then proves images/gallery handling
- Then proves document-link handling while explicitly skipping forms for v1

## Not starting yet

No implementation should begin until the user approves:
- the slice order
- the candidate pages
- the gallery presentation choice
- the treatment of the membership/contact form area
