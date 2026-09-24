# Velmora acceptance report

Verified September 24, 2026 against `.paul/BUILD-SPEC.md` and the original `Prompt for site`. Build location follows the user's override: `websites/Codex-Velmora`. Local preview: http://127.0.0.1:4322. No deployment or real email delivery performed.

## Original section 6 checklist

| Requirement | Result | Evidence |
|---|---|---|
| Ten research folders, all artifacts, SITES and ten adopted elements | PASS | `artifact-check.json`; `../research/SITES.md`; `../research/ELEMENTS.md`; ten folders with rendered HTML, computed styles, network captures, desktop/mobile/nav/hero/inner-page images and seven reference images each |
| Build exits zero, no TypeScript errors | PASS | `final-build.log`: zero errors, warnings and hints; completed production build |
| Every sitemap route returns 200; designed unknown-route 404 | PASS | `metadata-check.txt`: all 51 sitemap routes; `page-audit-final.txt`: 55 paths including styleguide, confirmation and two expected 404 paths |
| Booking at 1440 and 390, reference and calendar download | PASS | `booking-check.txt`; `booking-review-{1440,390}.png`; `booking-confirmed-{1440,390}.png`; `booking-{1440,390}.ics` |
| All four forms, valid submissions and inline errors | PASS | `forms-check.txt` (390); `forms-desktop-check.txt` (1440); `form-*.png` |
| Quiz recommendations and prefilled booking link | PASS | `interaction-check.txt`: six questions, three matches, neuromodulator preselection |
| Live desktop 3D, reduced-motion poster | PASS | `motion-check.txt`; `hero-live.png`; `method-{8,36,65,94}.png`; `reduced-final.png`; `final-ui-check.txt` also verifies no-WebGL fallback |
| Mobile Lighthouse thresholds on home and treatment | PASS | `lighthouse-home-final.report.{html,json}`: 97/100/100/100; `lighthouse-treatment-final.report.{html,json}`: 98/100/100/100 |
| No overflow at 390, 768, 1440; menu and sticky bar | PASS | `page-audit-final.txt`; `interaction-check.txt`; `motion-check.txt`; `final-ui-check.txt` adds 375 and 1024 on shared layouts |
| Every page captured at 1440 and 390 and visually reviewed | PASS | `pages/`: 110 full-page captures; `review/sheet-01.jpg` through `sheet-22.jpg`; `VISUAL-REVIEW.md`; map correction in `contact-map-final.png` |
| No unfinished-copy matches in src | PASS | `artifact-check.json`: no case-insensitive matches for lorem, todo, placeholder or tbd |
| Every stock image credited; no competitor assets ship | PASS | `../CREDITS.md`; `artifact-check.json`: eleven stock families, six responsive variants each, no research/public or research/src identical files; source import review confirms research isolation |
| No browser application errors on pages | PASS | `page-audit-final.txt` and `motion-check.txt`; only expected browser HTTP 404 messages on intentional missing-page tests |
| README: local commands, env, brand swap, Railway | PASS | `../README.md`; `../.env.example`; deployment instructions only |

Score order: Performance / Accessibility / Best Practices / SEO. Lighthouse numbers are local mobile lab results, not a guarantee for every device or hosting environment.

## Full-spec qualification beyond the checklist

- **Data and routes:** `data-check.json` confirms 13 full treatment records with six FAQs each, valid concern/provider/related-care/aftercare relationships, six concerns, five providers, six aftercare categories, 26 FAQs, eight policies and three journal articles. Treatment templates contain risk discussion, preparation/during/after timelines, five clinical specs, starting price, provider links, illustrative comparison, FAQs and booking CTA.
- **Home:** all thirteen specified sections are present, in the required order. Original copy and the research adaptations appear throughout. Membership comparison, financing context, fictional provider profiles and testimonials, legal pages and custom 404 are present.
- **Design:** self-hosted Cormorant/Manrope, shared palette/type/spacing tokens, responsive AVIF/WebP imagery, consistent grade and original glass artwork. Component gallery includes variants, tabs, native modal, validation fields, carousel, accordion and comparison slider. Original AA contrast proof is `contrast.json`; both Lighthouse accessibility scores are 100.
- **Motion:** dynamic shared scene chunk is approximately 234 KB gzip (see exact bytes in `artifact-check.json`); includes Three/Fiber/transmission material. React/site/scheduler shared runtime is separate. DPR is capped at 1.75, rendering pauses offscreen, local studio HDRI is credited. Desktop hero line reveals, image clipping, magnetic CTA and Lenis run only when motion is allowed. Method scroll snapshots verify four distinct copy states with a live canvas. Mobile shows all four steps as ordinary content.
- **Interactions:** `interaction-check.txt` verifies treatment filters and empty state, results filtering, keyboard comparison slider, fuzzy FAQ search, quiz, menu Escape and restored focus. `final-ui-check.txt` verifies policy search, keyboard tabs, optional map loading and poster fallback without WebGL.
- **APIs:** `api-negative.json` verifies all five endpoints reject invalid payloads and honeypots, sixth request is rate-limited, cross-origin and oversized requests are rejected. Astro rejects cross-origin plain-text media at its CSRF boundary (403). `email-check.json` verifies the configured Resend code path with a blocked-network mock: all notifications, support topic, newsletter audience, client booking receipt with tentative calendar, and generic 503 on delivery failure. `api-valid.json` records console-only success for all five endpoints; current booking/forms checks independently verify that behavior.
- **SEO/GEO:** `metadata-check.txt` checks every sitemap page's metadata, canonical, OG, single h1, image alt text and nonempty links. Sitewide MedicalBusiness/LocalBusiness, all treatment MedicalProcedure/FAQPage/BreadcrumbList schemas, physician profile and article schema are present. Sitemap omits styleguide and confirmation. Crawl documents derive brand and URL from `site.ts` and `llms.txt` includes booking. Original OG artwork is local.
- **Brand:** shared identity, contact details, hours, social URLs, palette, location labels and fixed timezone offset derive from `site.ts`. Editorial prose and service/provider offerings are separately editable data. Original image locations remain factual descriptions of the photographs. See README for adapting clinical content or a daylight-saving timezone.
- **Assets/research:** seventy reference-only competitor images stay isolated from eleven licensed stock sources used by the application. Favicon and OG art are original; the studio HDRI is CC0. Research captures measure observable design patterns, not unverifiable commercial conversion performance.

## Decisions and practical limits

1. Astro 7 and matching adapters replaced requested Astro 5 due to security advisories. The original architecture remains; `SECURITY-DECISION.md` records the exception. `dependency-audit-final.json` reports zero known vulnerabilities.
2. Desktop retains full live 3D. Mobile deliberately uses the original rendered poster and ordinary Method steps to meet the performance target; hero hydration uses a desktop media condition rather than loading 3D on mobile.
3. Every identity, clinical credential, testimonial and price is explicitly fictional. Comparison sliders use the same stock image with two color treatments; they never claim clinical results. A real client must supply approved proof, provider credentials, policies and actual photos.
4. Booking reserves no slot; gift cards collect no payment. Both behave as the request workflows specified. Calendars are tentative. Production scheduling and payments require the real practice's systems.
5. Email integration is transport-mocked and local demo delivery is tested. Real Resend credentials/inbox delivery are intentionally outside this local, no-message verification. A successful practice notification is retained even if the acknowledgment email fails, with the failure logged against its reference.
6. Rate limits are in-memory, five per minute per IP across all endpoints. A multi-instance deployment needs a shared store. Forms ask visitors to keep private medical information for clinical channels; demo server output may be retained by the process host.
7. The third-party embedded map rendered blank in this environment. Contact now provides a styled address/location panel and working external map link, with an optional interactive embed and fallback instructions.
8. No deployment, remote publishing, or workspace-wide git staging was performed. PAUL auto-commit is disabled in project configuration. Final review is the user's next action.
