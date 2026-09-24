# Velmora Aesthetics — Build Spec

Companion to `projects/velmora-medspa/PLANNING.md`. PLANNING says **why**, this file says **what exactly to build** and **how it's judged done**.

Build root: `/Users/user/Desktop/Development-Charlie-2/Charlieautomates/websites/velmora-medspa/`

---

## 1. Research Protocol (Phase 1)

### 1.1 Find the 10
- 6 national design leaders + 4 Scottsdale rivals. Start from the seed list in PLANNING.md, verify with web search ("best med spa website design", "awwwards med spa", "best med spa Scottsdale").
- Drop any site that is dead, template-generic, or popup-spammed. Replace until you have 10 strong ones.
- Log picks + why in `research/SITES.md`.

### 1.2 Capture each site with playwright-cli
Per site, folder `research/sites/{NN}-{slug}/`:

| Artifact | How |
|----------|-----|
| `desktop-full.png` | `resize 1440 900` → `goto` → scroll to bottom (trigger lazy load) → `screenshot` full page |
| `mobile-full.png` | `resize 390 844` → reload → same |
| `hero-desktop.png`, `nav-open-mobile.png` | element/viewport screenshots |
| `page.html` | `eval "document.documentElement.outerHTML"` with `--raw` |
| `styles.json` | `eval` pulling computed font-family, font-size, color, background, letter-spacing for h1, h2, body, nav links, primary button |
| `network.txt` | `network` output; note three.js / Spline / GSAP / Lenis / video usage |
| `images/` | download 5 to 10 representative images (reference only, never shipped) |
| `notes.md` | hero pattern, nav pattern, booking CTA placement, proof style, pricing display, motion, what's weak |

Also capture 1 inner page per site (a treatment page or booking page).

### 1.3 Scorecard
`research/ELEMENTS.md`: one row per site, at least one adopted element each.

| # | Site | Best element | Why it works | How Velmora adapts it (not copies) |
|---|------|--------------|--------------|-------------------------------------|

Then a **Positioning** paragraph: what all 10 do, what none do, and how Velmora wins.

Hard rule: adapt layout, interaction, and information patterns only. Never reuse competitor copy, images, logos, or code verbatim.

---

## 2. Design System (Phase 2)

Run `/frontend-design` and `/ui-ux-pro-max` before writing any page.

- **Tokens** in `src/styles/tokens.css` (CSS custom properties) mirrored in `tailwind.config`:
  - Neutrals: bone (~#F5F0E8), sand (~#E7DDCF), stone (~#BFB3A3), espresso ink (~#221B17)
  - Accent: champagne gold (~#B8946A), used sparingly (CTAs, hairlines, numerals)
  - Secondary: muted sage (~#8E9A86)
  - Final hex values are chosen by ui-ux-pro-max, with a WCAG AA check on every text/background pair
- **Type:** editorial serif display (e.g., Fraunces or Cormorant) + geometric sans body (e.g., Manrope or General Sans), fluid `clamp()` scale, self-hosted via `@fontsource`
- **Grid:** 12-col, generous whitespace, 1440 max content width, 16px mobile gutter
- **Components:** Button (primary / ghost / link), Nav (transparent-over-hero → solid on scroll, full-screen mobile menu), Footer, TreatmentCard, SpecStrip (duration / discomfort / downtime / onset / longevity), PriceTable, MembershipCard, TestimonialCarousel, BeforeAfterSlider, Accordion, Tabs, Form fields with inline validation, Toast, Modal, Badge, Breadcrumbs, StickyMobileBookBar
- **Motion language:** slow easing (expo/cubic out, 600 to 1200ms), text line reveals, image clip-path reveals, magnetic CTA, Lenis smooth scroll. All disabled or reduced under `prefers-reduced-motion`.
- **Style tile:** `/styleguide` route (noindex) showing every token + component. Must render before Phase 3 starts.

### 2.1 Stock imagery
- Source from Unsplash / Pexels (free commercial license). Themes: serene treatment rooms, textures (marble, linen, water, glass), hands + skincare, diverse faces with natural skin, Scottsdale desert light.
- Download to `public/images/`, convert to AVIF + WebP at 3 widths, apply one consistent warm grade (sharp or ffmpeg).
- Record every image: file, source URL, author, license, in `CREDITS.md`.
- Before/after imagery is labeled "Illustrative imagery. Not actual patient results."

### 2.2 3D direction
- **Hero scene** (`src/components/three/HeroScene.tsx`): a liquid-glass serum droplet / organic blob using `MeshTransmissionMaterial`, soft studio HDRI, caustic-like highlights in champagne tones, subtle noise-driven vertex motion, mouse/gyro parallax, slow scroll-linked rotation and dissolve as the hero exits.
- **Scroll interlude** (Home "The Velmora Method"): 3 to 4 step scroll-scrubbed sequence where one 3D form morphs between states (e.g., droplet → layered skin-like strata → smooth sphere), pinned with ScrollTrigger, step copy fades alongside.
- **Performance rules:** `client:visible` islands, dynamic import, `dpr={[1, 1.75]}`, pause render when off-screen, total 3D JS under ~250KB gzipped, a static AVIF poster rendered first and swapped when the canvas is ready, poster-only on `prefers-reduced-motion` or no WebGL.
- Optional micro-3D: small tilt/parallax on treatment cards (CSS 3D transforms, not WebGL).

---

## 3. Sitemap + Pages (Phase 3)

```
/                          Home
/treatments                Treatments index (filter by concern + category)
/treatments/[slug]         Treatment detail (8 to 10, data-driven)
/concerns/[slug]           Concern pages (lines & wrinkles, volume loss, pigmentation, acne & texture, body, hair) → map to treatments
/results                   Results gallery (before/after sliders, filterable)
/pricing                   Full price list + financing
/membership                3 tiers + comparison + FAQ
/about                     Story, philosophy, medical director, team
/team/[slug]               Provider bios (5)
/quiz                      Treatment Match quiz (6 questions → recommendations)
/book                      4-step booking flow
/book/confirmed            Confirmation + .ics + prep info
/support                   Help center hub: search, categories, top questions, contact form
/support/aftercare/[slug]  Aftercare guides per category
/support/policies          Cancellation, deposits, refunds, age requirement
/faq                       Full FAQ (grouped, searchable, FAQPage schema)
/contact                   Map, hours, phone, form
/gift-cards                Amounts + request form
/journal                   Journal index (content collection)
/journal/[slug]            3 seed articles
/privacy  /terms  /medical-disclaimer  /accessibility
/styleguide                noindex, design system tile
/404
```

### 3.1 Home (section order, adapt using ELEMENTS.md winners)
1. Hero: 3D scene, headline, subline (physician-led, Scottsdale), primary "Book a consultation" + secondary "Find your treatment"
2. Trust strip: medical director credential, years, treatments performed, rating (demo), FDA-cleared devices
3. Signature treatments: 6 cards, hover reveal, "from $" price
4. Shop by concern: interactive concern selector
5. The Velmora Method: 3D scroll interlude, 4 steps (Consult → Plan → Treat → Maintain)
6. Results preview: 2 before/after sliders + link
7. Membership teaser with savings math
8. Meet the medical director: portrait + quote
9. Testimonials carousel
10. The space: editorial image grid of the spa
11. Journal preview (3)
12. Final CTA band + quiz link
13. Footer: hours, address, map link, socials, newsletter, legal, disclaimer

### 3.2 Treatment detail template
Hero (image + name + one-line benefit + price from + Book) → SpecStrip → What it treats → How it works → What to expect (before / during / after timeline) → Results (illustrative) → Pairs well with → Provider(s) who perform it → Pricing detail → FAQ (5+) → Aftercare link → Sticky Book CTA. JSON-LD: `MedicalProcedure` + `FAQPage` + `BreadcrumbList`.

Treatments data (`src/data/treatments.ts`): Botox/Dysport (neuromodulators), Dermal fillers, Lip enhancement, Sculptra/biostimulators, Microneedling with RF (Morpheus8-style), IPL photofacial, Laser resurfacing, HydraFacial, Chemical peels, Laser hair removal, Body contouring, IV therapy, Medical weight loss (GLP-1). Keep 10 to 13, each with the full field set.

### 3.3 Support page
Search input (client-side fuzzy search over FAQ + aftercare + policies), category tiles (Booking & changes, Before your visit, Aftercare, Billing & membership, Policies), top 8 questions accordion, "Still need help?" contact form (name, email, phone, topic select, message) → `/api/support`, response-time promise, phone + hours.

### 3.4 Booking flow (`/book`, React island)
1. Choose treatment(s) or "Not sure, book a consult" (preselect via `?treatment=slug`)
2. Choose provider (or "First available") + date (next 30 days, closed Sundays) + time slot (generated from hours in `site.ts`)
3. Details: name, email, phone, first visit?, notes, SMS consent checkbox, policy acknowledgment
4. Review + confirm → POST `/api/book` → `/book/confirmed`

Progress indicator, back/next, state preserved in URL/sessionStorage, full keyboard support, inline zod errors.

---

## 4. Functionality (Phase 3)

| Feature | Endpoint | Behavior |
|---------|----------|----------|
| Booking request | `POST /api/book` | zod validate → email to spa inbox + confirmation to client via Resend → returns ref ID; generates `.ics` |
| Contact | `POST /api/contact` | validate → Resend |
| Support | `POST /api/support` | validate → Resend, topic in subject |
| Gift card request | `POST /api/gift-card` | validate → Resend |
| Newsletter | `POST /api/newsletter` | validate email → Resend audience or log |
| Quiz | client-side | scoring map in `src/data/quiz.ts` → results link to treatments + prefilled `/book` |

All endpoints: honeypot field, in-memory IP rate limit (5/min), no PHI persisted to disk, generic error messages, `RESEND_API_KEY` + `SPA_INBOX_EMAIL` from env; without a key, log payload to console and still return success so local demo works. `.env.example` documents vars.

---

## 5. SEO / GEO

- Per-page title + meta description, OG image (generated or designed), canonical, `@astrojs/sitemap`, `robots.txt`
- JSON-LD: `MedicalBusiness` + `LocalBusiness` (address, geo, hours) sitewide, `MedicalProcedure`, `FAQPage`, `Physician` on team pages, `Article` on journal
- `llms.txt` summarizing services, location, booking URL
- Semantic HTML, one h1 per page, descriptive alt text on every image

---

## 6. Acceptance Criteria (Phase 4, all must pass)

- [x] `research/` holds 10 site folders with all artifacts, `SITES.md`, `ELEMENTS.md` with 10+ adopted elements
- [x] `npm run build` exits 0, zero TypeScript errors
- [x] Every route in the sitemap returns 200 in `npm run preview`; unknown route shows the designed 404
- [x] Booking flow completes end to end in playwright-cli at 1440 and 390; confirmation page shows ref ID; `.ics` downloads
- [x] Contact, support, gift card, newsletter forms submit and show success; invalid input shows inline errors
- [x] Quiz produces recommendations and deep-links into `/book?treatment=`
- [x] Hero 3D renders on desktop; poster fallback shows with reduced motion emulated
- [x] Lighthouse mobile on `/` and one treatment page: Perf 85+, A11y 95+, Best Practices 95+, SEO 100
- [x] No horizontal scroll at 390 / 768 / 1440; mobile menu and sticky book bar work
- [x] Screenshots of every page at 1440 and 390 saved to `verification/` and reviewed; visual bugs fixed
- [x] `grep -riE "lorem|todo|placeholder|tbd" src` returns nothing
- [x] `CREDITS.md` lists every stock image; no competitor asset in `public/`
- [x] Browser console has zero errors on every page
- [x] `README.md`: run, env vars, how to swap brand via `site.ts`, deploy to Railway


Verification closed September 24, 2026. Requirement-by-requirement proof, scores, decisions and deployment boundaries: `../verification/ACCEPTANCE.md`.
