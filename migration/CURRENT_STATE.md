# Current State

## Approved checkpoint
- `main` has been rolled back to `af236e9` (`Set up Eleventy and add shared homepage navigation`).
- Backup of the pre-rollback state exists on:
  - branch `backup/pre-rollback-2026-04-19`
  - tag `pre-rollback-2026-04-19`

## Current task
- Batch 3 implementation completed locally and is being validated for review.

## Known issue being fixed
- Root-absolute internal paths like `/styles.css` and `/` broke the deployed site on GitHub Pages project subpaths. This was repaired before restarting Batch 2.

## Rules to follow
- Stop after each batch and wait for user approval.
- Keep summaries compact and durable.
- Validate against GitHub Pages-style subpath behavior before calling a batch safe.

## Validation checklist
- `npm run build`
- `python3 scripts/check_no_root_absolute_paths.py`
- Browser smoke test of homepage under a nested subpath
- Confirm homepage styling loads and no local links are broken

## Current built vs external status
- Built locally/new site:
  - homepage
  - the-club.html
  - membership.html
  - by-laws.html
  - useful-links.html
  - fleets.html
  - lido.html
  - el-toro.html
  - open.html
- Still external:
  - Racing
  - News & Archives
  - Photos

## Next planned step
- Finish live-site verification for Batch 3.
- Wait for user review and approval before any Batch 4 work.
