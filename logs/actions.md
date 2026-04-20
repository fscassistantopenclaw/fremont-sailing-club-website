# Action Log

## 2026-04-19 - vertical-slice planning setup
- Tool activity summary:
  - Created `logs/progress.md`
  - Created `logs/actions.md`
  - Preparing a repo-local vertical-slice migration proposal based on the user's new constraints
- Output summary:
  - Logging framework added for future major steps
  - `migration/vertical-slice-plan.md` added with the proposed homepage, standard page, photo page, and document page slices
  - No new dependencies installed
  - No implementation work started

## 2026-04-19 - homepage slice kickoff
- Tool activity summary:
  - Recorded the user's homepage approvals in the repo logs
  - Starting homepage-only implementation work
- Output summary:
  - Will keep current section order closely
  - Will aim for similar emphasis/visual focus without copying Weebly runtime behavior
  - Upcoming events will stay manual for v1

## 2026-04-19 - homepage slice implementation
- Tool activity summary:
  - Fetched and inspected the current homepage source and assets
  - Captured a visual screenshot reference of the live homepage
  - Downloaded the homepage logo, header banner, background image, and sailing action photo into local repo assets
  - Replaced the placeholder `index.html` and `styles.css` with a first static homepage slice
  - Captured a local screenshot for layout verification
- Output summary:
  - Homepage now follows the original section order more closely
  - Upcoming events are manual static content
  - No Weebly runtime scripts or analytics were added
  - First slice uses local image assets and plain HTML/CSS only

## 2026-04-19 - sitewide migration planning kickoff
- Tool activity summary:
  - Recorded the user's approval to continue with the rest of the migration
  - Starting with sitewide batching and menu-structure planning before deeper implementation
- Output summary:
  - Goal is to migrate the rest of the site in small, reviewable commits
  - Need to lock down menu structure and page-group batching first
  - Will surface any major architecture/tooling decision for approval before proceeding

## 2026-04-19 - Batch 1 kickoff
- Tool activity summary:
  - Recorded approval for simplified menu, Eleventy installation, and preserving legacy filenames
  - Starting Batch 1 implementation
- Output summary:
  - Batch 1 will add shared structure and homepage navigation
  - The generated site should stay usable after each commit
  - Menu links will avoid dead ends while section migrations are still in progress

## 2026-04-19 - Batch 1 implementation
- Tool activity summary:
  - Installed `@11ty/eleventy` after approval
  - Added `.eleventy.js`, `package.json`, `package-lock.json`, and `src/` source structure
  - Added shared site data and a shared base layout
  - Rebuilt the homepage through Eleventy with the simplified top navigation
  - Ran a local Eleventy build
  - Ran a local browser screenshot check
  - Ran a local-link check for generated homepage links
- Output summary:
  - Homepage now builds from shared source templates
  - Simplified menu is integrated without dead local links
  - Batch 1 stays in a usable state and remains easy to rollback

## 2026-04-19 - repair batch after rollback
- Tool activity summary:
  - Rolled `main` back to `af236e9` after preserving the later state on a backup branch and tag
  - Replaced root-absolute homepage shell paths with deployment-safe relative paths
  - Added `scripts/check_no_root_absolute_paths.py` and `npm run validate:subpath`
  - Added `migration/CURRENT_STATE.md` as a compact handoff/status file
  - Rebuilt the site and validated the homepage under a nested GitHub Pages-style subpath using a local browser smoke test
- Output summary:
  - Shared homepage shell no longer depends on domain-root paths
  - A repeatable subpath-safety validation step now exists in the repo
  - Homepage styling and images loaded correctly in the subpath smoke test
  - No further migration work was resumed in this batch
