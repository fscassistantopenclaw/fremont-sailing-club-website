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
- Completed Batch 2 for the core club section: migrated The Club, Membership, By Laws, and Useful Links into the shared static layout, and added a careful placeholder for the password-protected Officers & Fleet Captains page instead of exposing protected content.
- Completed Batch 3 for fleets: migrated the Fleets overview plus Lido, El Toro, and Open Fleet pages into the shared layout, swapped the main Fleets menu link to the local site, and rechecked local navigation after the batch.
- Completed Batch 4 for racing basics: migrated the Racing overview, Results page, and current 2026 Notice of Race and Sailing Instructions pages, copied the current PDFs into the repo, and switched the main Racing menu link to the local site.
- Completed Batch 5 for news basics: migrated Commodore's Comments and Windjammer landing pages, updated internal Windjammer links, and switched the main News & Archives menu link to the local site.
