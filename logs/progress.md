# Progress Log

## 2026-04-19
- Created ongoing repo-local progress and action logs.
- Recorded new migration constraints: static-only for now, no search/forms/runtime scripts, no analytics, Google Drive/Forms links allowed, minimalist styling is acceptable, photo pages should stay visually organized.
- Began vertical-slice planning for the homepage, one standard content page, one photo-heavy page, and one downloadable-documents page.
- Wrote `migration/vertical-slice-plan.md` with candidate pages, source-material needs, target code structure, and approval questions.
- Received approval to start implementation, beginning with the homepage slice only. The homepage should keep the current section order closely, keep a similar visual emphasis to the original layout, and keep upcoming events as manually maintained content.
- Implemented a first static homepage slice using local copied assets from the live site, manual event content blocks, and simplified shared styling without any Weebly runtime dependencies.
- Received approval to continue with the rest of the site. Starting with a repo-local batching plan and a proposed menu structure before scaling implementation.
- Received approval for the simplified menu, installing Eleventy, and preserving legacy filenames for now. Beginning Batch 1: shared shell, homepage menu, and stable generated output after each commit.
- Completed the first pass of Batch 1: Eleventy is installed, the homepage now builds from shared source templates, the simplified menu is live, and the generated site was checked for obvious layout problems and dead local links.
- Repair batch completed after rollback: removed root-absolute internal paths from the shared homepage shell, added a subpath-safety validation script, and rechecked the homepage under a nested GitHub Pages-style subpath before resuming any content work.
- Restarted Batch 2 from the repaired base and migrated the public core club pages: The Club, Membership, By Laws, and Useful Links. Club and Useful Links now point to local pages, while other top-level sections remain external until their own batches are approved and migrated.
