# Migration Log

## 2026-04-19

### Phase 0
- Created `MIGRATION_PLAN.md`
- Created migration working folders under `migration/` and `scripts/`
- Decided to avoid new installs during Phase 0/1
- Documented proposed future tool usage and install approvals needed before Phase 2+

### Phase 1
- Read `robots.txt` and `sitemap.xml`
- Crawled the live site with a repo-local Python inventory script using only the standard library
- Produced:
  - `migration/inventory/site-inventory.json`
  - `migration/inventory/site-inventory-summary.md`
  - `migration/inventory/page-inventory.csv`
  - `migration/inventory/asset-inventory.csv`
  - `migration/inventory/navigation-map.md`
  - `migration/inventory/components-and-risks.md`
  - `migration/inventory/architecture-recommendation.md`

### Key findings
- Sitemap currently exposes 173 HTML pages
- Inventory found 837 referenced assets
- The site uses a Weebly-generated global navigation repeated across nearly all pages
- The live site still depends heavily on Weebly and Google-hosted external resources
- A built-in Weebly search form appears on nearly every page
- A custom contact form appears on membership-related pages and cannot be carried over to plain GitHub Pages without replacement

### Status
- Phase 0 complete
- Phase 1 complete
- Paused before Phase 2 and before any new dependency installation
