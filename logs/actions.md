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

## 2026-04-19 - Batch 2 implementation
- Tool activity summary:
  - Fetched and reviewed source content for The Club, Membership, By Laws, Useful Links, and the legacy Officers & Fleet Captains page
  - Detected that `officers--fleet-captains.html` is password-protected on the old site
  - Added a shared standard content-page layout
  - Migrated the core club pages into Eleventy source templates
  - Copied the by-laws PDF into the repo as a local public asset
  - Rebuilt the site and corrected Eleventy output to preserve legacy filenames exactly
  - Verified generated local links and spot-checked page layouts with local browser screenshots
- Output summary:
  - Core club pages now exist locally with stable legacy filenames
  - Club and Useful Links menu entries now point to local pages
  - Password-protected legacy content was not copied into the public repo
  - Batch 2 remains in a usable, rollback-safe state

## 2026-04-19 - Batch 3 implementation
- Tool activity summary:
  - Fetched and reviewed source content for Fleets, Lido, El Toro, and Open Fleet
  - Added Eleventy templates for the fleets overview and the three fleet pages
  - Switched the main Fleets navigation item from the live site to the local page
  - Rebuilt the site, rechecked generated local links, and spot-checked fleet page layouts in a browser
- Output summary:
  - Fleets content now exists locally with stable legacy filenames
  - Main navigation now points to the local Fleets page without introducing dead links
  - Batch 3 remains in a usable, rollback-safe state

## 2026-04-19 - Batch 4 implementation
- Tool activity summary:
  - Fetched and reviewed source content for Racing, Results, 2026 Notice of Race, and 2026 Sailing Instructions
  - Identified and copied the current Notice of Race and Sailing Instructions PDFs into the repo as local public assets
  - Added Eleventy templates for the Racing overview, Results page, and both current-season document pages
  - Switched the main Racing navigation item from the live site to the local page
  - Rebuilt the site, rechecked generated local links, and spot-checked racing page layouts in a browser
- Output summary:
  - Racing overview and current-season core docs now exist locally with stable legacy filenames
  - Main navigation now points to the local Racing page without introducing dead links
  - Deeper race archives remain available through clearly-labeled legacy links until migrated
  - Batch 4 remains in a usable, rollback-safe state

## 2026-04-19 - Batch 5 implementation
- Tool activity summary:
  - Fetched and reviewed source content for Commodore's Comments, Windjammer Newsletter, and the related archive/navigation links
  - Added Eleventy templates for Commodore's Comments and Windjammer Newsletter
  - Updated club internal Windjammer links to point to the local site
  - Switched the main News & Archives navigation item from the live site to the local page
  - Rebuilt the site, rechecked generated local links, and spot-checked page layouts in a browser
- Output summary:
  - News & Archives basics now exist locally and are reachable from the main navigation
  - Windjammer links inside the site now stay local where available
  - Archive-heavy historical content remains clearly linked from the legacy site until migrated
  - Batch 5 remains in a usable, rollback-safe state
