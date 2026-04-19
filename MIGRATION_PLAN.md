# Fremont Sailing Club Website Migration Plan

Status: Phase 0 and Phase 1 complete. Paused before rebuild work.

## Goals

- Move the Fremont Sailing Club website from Weebly to a code-based repo on GitHub
- Preserve site content and URL structure as much as practical
- Keep the final site simple, readable, and easy to update
- Keep a reproducible migration trail in this repo

## Working rules for this migration

- Work only in this dedicated repository
- Proceed in clear phases
- Pause for approval before major phase transitions
- Ask for input whenever source content is ambiguous or a design/content choice is needed
- Do not install new dependencies without approval first

## Phase outline

### Phase 0, setup and planning
- Create migration plan and log
- Propose repository structure
- Explain tools and skills before installing anything new

### Phase 1, crawl and inventory
- Crawl the live site
- Produce page inventory, asset inventory, navigation map, component/template list, risky feature list, and architecture recommendation

### Phase 2, approved source capture
- After approval, create a clean local source snapshot for migration work
- Confirm what should be preserved exactly and what can be simplified

### Phase 3, foundation build
- Set up the chosen static site structure
- Rebuild shared layout, navigation, footer, and content patterns first

### Phase 4, content migration
- Move pages section by section
- Preserve URLs where possible
- Track unresolved content issues in the migration log

### Phase 5, verification and cutover prep
- Link check
- asset check
- content spot checks
- GitHub Pages deploy verification

## Proposed repository structure

This is the proposed structure for the migration and rebuild work. I created only the migration folders needed for Phase 0/1 so far.

```text
/
  MIGRATION_PLAN.md
  MIGRATION_LOG.md
  README.md
  migration/
    inventory/              # crawl outputs, inventories, analysis
    logs/                   # dated migration notes
    notes/                  # decisions, open questions, content issues
  scripts/                  # reproducible crawl/build helper scripts
  src/                      # proposed final site source (after approval)
    assets/
    pages/
    includes/
    layouts/
    data/
  public/                   # optional static passthrough files if needed
```

## Tools and skills planned

### Already used in Phase 0/1, no new installs
- **`web_fetch`**: quick inspection of the live site, homepage, robots.txt, sitemap.xml, and representative pages
- **Python standard library crawler (`scripts/crawl_inventory.py`)**: reproducible inventory without adding third-party dependencies
- **Git + repo files**: keep the migration traceable and versioned

### Skill likely useful during migration
- **`playwright-npx` skill**: useful if we need browser automation for pages where static fetching misses gallery behavior, embedded content behavior, or navigation edge cases
  - Why: it is a focused, trusted skill already available in the workspace
  - Current status: skill instructions reviewed, but no new Playwright project dependency was installed for this repo during Phase 0/1

### Proposed future installs, approval required before any of these
- **Eleventy (`@11ty/eleventy`)**: my recommended target framework for the rebuilt site
  - Why: simple, readable, low-magic static site generator, good for shared templates and many content pages
- **Playwright package in this repo**: only if we need deeper scripted capture of galleries or JS-driven behavior that static crawling misses
  - Why: useful for verification and edge-case capture, but not required yet

## Current recommendation

The simplest maintainable target is:
- a static GitHub Pages site
- Eleventy for templates/includes and page generation
- plain HTML, CSS, and very light vanilla JavaScript only where needed
- no client-side framework
- minimal build complexity

That keeps the site understandable while avoiding 100 manually duplicated HTML files.

## Pause point

Do not start rebuilding pages yet.

Next major transition would be **Phase 2, approved source capture and architecture setup**.
That needs your approval first.
