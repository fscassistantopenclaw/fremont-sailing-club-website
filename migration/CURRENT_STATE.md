# Current State

## Approved checkpoint
- `main` has been rolled back to `af236e9` (`Set up Eleventy and add shared homepage navigation`).
- Backup of the pre-rollback state exists on:
  - branch `backup/pre-rollback-2026-04-19`
  - tag `pre-rollback-2026-04-19`

## Current task
- Repair the homepage/shared-shell foundation before restarting Batch 2.

## Known issue being fixed
- Root-absolute internal paths like `/styles.css` and `/` broke the deployed site on GitHub Pages project subpaths.

## Rules to follow
- Stop after each batch and wait for user approval.
- Keep summaries compact and durable.
- Validate against GitHub Pages-style subpath behavior before calling a batch safe.

## Validation checklist
- `npm run build`
- `python3 scripts/check_no_root_absolute_paths.py`
- Browser smoke test of homepage under a nested subpath
- Confirm homepage styling loads and no local links are broken

## Next planned step after this repair batch
- Wait for user review.
- Only then restart Batch 2.
