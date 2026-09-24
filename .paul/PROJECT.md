# Codex-Velmora

Luxury physician-led Scottsdale demo spa. Core value: medical precision, hotel calm.

## Requirements
All requirements in the preserved source documents apply. Latest user instruction overrides destination to websites/Codex-Velmora. Build all routes, 13 treatments, forms, booking, quiz, stock assets, 3D, SEO and verification. No deployment.

## Delivered state — September 24, 2026

All four phases complete and unified. Full local demonstration built in websites/Codex-Velmora, with 53 rendered page routes, the custom 404, five APIs, original desktop 3D and mobile fallbacks. Final acceptance report: verification/ACCEPTANCE.md. Build is clean; mobile Lighthouse home 97/100/100/100 and treatment 98/100/100/100. No deployment or live messages. Review is the next action.

Validated requirements: complete research/design assets, all routes/content, request workflows, SEO, responsive/motion behavior, performance gates, visual review, credits and README. Original planning content below is preserved as source context, not a current task list.

## Source planning
# Velmora Aesthetics — Premium 3D Med Spa Website

> Ultra-premium, 3D-driven, fully functional multi-page website for a luxury medical spa, built from stock imagery and informed by a 10-site competitor teardown.

**Created:** 2026-09-24
**Type:** Client Website
**Client:** Velmora Aesthetics (demo brand, swappable via one config file)
**Build destination:** `websites/velmora-medspa/`
**Companion spec:** `projects/velmora-medspa/BUILD-SPEC.md` (sitemap, page-by-page sections, 3D, functionality, acceptance criteria)
**Skill Loadout:** playwright-cli, frontend-design, ui-ux-pro-max, copywriting, PAUL, geo (post-launch)
**Quality Gates:** competitor teardown complete, design system locked before pages, mobile + reduced-motion pass, Lighthouse targets, every form works end to end, no placeholder copy

---

## Business Context

- **Client:** Velmora Aesthetics, a physician-led luxury medical spa (aesthetics / wellness)
- **Location:** Scottsdale, Arizona (one of the densest, most competitive med spa markets in the US; forces a top-tier site)
- **What they do:** Injectables, skin rejuvenation, laser, body contouring, medical-grade facials, wellness (IV + medical weight loss)
- **Target audience:** Women 30 to 58, household income $150k+, time-poor, research-heavy, mobile-first; secondary: men 35 to 55 (Botox, hair, body)
- **Current presence:** None (net-new brand). Site must manufacture trust from zero.
- **Brand voice:** Quiet luxury. Calm, precise, clinical confidence without coldness. Short sentences. Never hype, never "transform your life", never guaranteed outcomes.
- **Brand direction:** Warm bone and sand neutrals, deep espresso ink, one champagne-gold accent, a soft sage secondary. Editorial serif display + clean geometric sans body. Final tokens are locked in the design-system phase with ui-ux-pro-max.
- **Existing assets:** None. All imagery is licensed stock (Unsplash / Pexels, recorded in `CREDITS.md`). Logo is a typographic wordmark built in SVG.

---

## Competitor Analysis

Done **inside the build** (Phase 1 of the PAUL prompt), not here. Build agent finds and tears down 10 top-performing med spa sites with playwright-cli, then picks the single best element from each.

Seed candidates (agent verifies each is live and still strong, replaces weak ones):

| Tier | Candidates |
|------|------------|
| National design leaders (6) | skinspirit.com, everbody.com, heydayskincare.com, alchemy43.com, ject.com, thethingswedo.com, idealimage.com, facefoundrie.com |
| Local Scottsdale rivals (4) | Found via web search: "best med spa Scottsdale", "Scottsdale botox", Google Maps top-rated with a real website |

**Positioning hypothesis to validate:** Scottsdale med spas look either like clinics (sterile, stock-blue, coupon-driven) or like beauty salons (pink, busy, promo pop-ups). Gap: a physician-led spa that looks like a luxury hotel and explains treatments with the clarity of a clinic. Differentiator: "Medical precision, hotel calm."

---

## Conversion Strategy

- **Primary CTA:** Book a consultation (free 20-min virtual or $50 in-person, credited to treatment)
- **Secondary CTAs:** Take the 60-second treatment match quiz, join the membership, buy a gift card, join the list (skin notes newsletter)

### Funnel
```
Ad / search / social
      │
      ▼
Home or Treatment page ──► Treatment Match quiz ──► recommended treatments ──┐
      │                                                                      │
      └────────────────────────► Book (4-step flow) ◄───────────────────────┘
                                      │
                                      ▼
                     Confirmation page + email (Resend) + .ics file
                                      │
                                      ▼
                     Pre-visit prep page (what to expect, intake)
```

### Objection Handling

| Objection | How We Address It |
|-----------|------------------|
| "Will I look fake / overdone?" | "Natural first" philosophy block, provider-led conservative-dosing promise, results gallery framed as subtle |
| "Is it safe? Who is actually injecting?" | Medical director + provider credentials on every treatment page, FDA-cleared device language, consult-first policy |
| "What does it cost?" | Transparent "from $X" pricing on every treatment, full pricing page, membership math, financing (Cherry / PatientFi) mention |
| "Does it hurt / downtime?" | Per-treatment spec strip: duration, discomfort, downtime, results onset, longevity |
| "I don't know what I need" | Treatment Match quiz + free virtual consult |

---

## Content Needs

### Existing Content
- [ ] Testimonials: need to write (realistic, clearly demo, first name + treatment, no fabricated review-platform badges)
- [ ] Case studies: before/after gallery uses stock with "Illustrative imagery" label, never presented as real patient results
- [ ] Service descriptions: need to write (8 to 10 treatments, clinically accurate, no outcome guarantees)
- [ ] Media assets: licensed stock, curated to one color grade

### Content to Create

| Section | Status | Notes |
|---------|--------|-------|
| Hero / headline | needs writing | 3 headline options, pick one; subline states physician-led + Scottsdale |
| About / team | needs writing | Medical director + 4 providers (fictional names, credentials plausible) |
| Treatments | needs writing | Structured data file drives index + detail pages |
| Pricing + membership | needs writing | 3 membership tiers |
| Testimonials | needs writing | 6 to 9, varied treatments |
| FAQ + Support | needs writing | 20+ Q&A grouped, searchable |
| Aftercare guides | needs writing | One per treatment category |
| Journal | needs writing | 3 seed articles |
| Legal | needs writing | Privacy, terms, medical disclaimer, cancellation policy, accessibility statement |

### Tone & Style Guide
Reading level grade 8 to 9. Clinical terms used once, then explained. No exclamation points. No em dashes. No "unlock", "elevate", "journey", "transform". Results always "may", "typically", "individual results vary".

---

## Tech Approach

- **Method:** Custom build (template sites can't do the 3D + booking flow at this quality)
- **Framework:** Astro 5 (matches every other site in `websites/`) + React islands only where interactive + Tailwind CSS
- **3D:** three.js via @react-three/fiber + @react-three/drei, lazy-loaded, one hero scene + one scroll-driven interlude, static poster fallback
- **Motion:** GSAP + ScrollTrigger, Lenis smooth scroll, respects `prefers-reduced-motion`
- **Forms / API:** Astro server endpoints (`@astrojs/node` adapter), zod validation, Resend for email (logs to console when key absent), honeypot + simple rate limit
- **Hosting:** Railway (existing workspace pattern); local `npm run build && npm run preview` must work first
- **Domain/DNS:** TBD, out of scope for the one-shot build
- **CMS needs:** Content lives in typed data files + Astro content collections (journal). No CMS.

---

## Timeline & Deliverables

Autonomous one-shot build. No client review between phases; the build agent self-reviews at each gate.

| Phase | Milestone | Deliverable | Gate |
|-------|-----------|-------------|------|
| 1 | Research | `research/` folder: 10 sites captured + `ELEMENTS.md` scorecard | 10 sites, every one with desktop + mobile screenshots and HTML |
| 2 | Design system | Tokens, type, components, 3D direction, stock image set | Style tile page renders |
| 3 | Build | All pages + functionality | Every route builds, every form submits |
| 4 | Verify + polish | Playwright visual pass, Lighthouse, fixes, README | Acceptance criteria in BUILD-SPEC.md all green |

### Client Review Checkpoints
Single review at end: Charles reviews the running local site and `research/ELEMENTS.md`.

---

## Skill Loadout & Quality Gates

### Skills Used During Build

| Skill | When It Fires | Purpose |
|-------|--------------|---------|
| playwright-cli | Phase 1 + Phase 4 | Capture competitor screenshots/HTML/assets; later self-verify own site |
| frontend-design | Phase 2 + 3 | Distinctive, non-generic production UI |
| ui-ux-pro-max | Phase 2 + 3 | Design system, palette, type pairing, component patterns, UX review |
| copywriting | Phase 3 | Conversion copy in the brand voice |
| PAUL | Whole build | Phase structure, STATE tracking |
| geo | Post-launch | Schema + AI search visibility |

### Quality Gates

| Gate | When | Pass Criteria |
|------|------|---------------|
| Research complete | End Phase 1 | 10 sites, scorecard with 1+ adopted element per site |
| Design lock | End Phase 2 | Tokens file + style tile, no ad-hoc colors after this |
| Functional | End Phase 3 | Booking, contact, support, quiz, newsletter, gift card request all submit and confirm |
| Performance | Phase 4 | Lighthouse mobile: Perf 85+, A11y 95+, SEO 100, Best Practices 95+ |
| Mobile | Phase 4 | 390px and 768px: no horizontal scroll, no overlap, tap targets 44px+ |
| Content | Phase 4 | `grep -ri "lorem\|TODO\|placeholder"` in src returns nothing |

---

## Design Decisions

1. **Demo brand "Velmora Aesthetics", Scottsdale**: fictional but specific. All brand data centralized in `src/config/site.ts` so a real client swaps name/phone/address/colors in one place.
2. **Astro over Next.js**: every site in `websites/` is Astro; static-first gives the performance budget room for the 3D.
3. **3D is concentrated, not everywhere**: one hero scene (liquid-glass serum form) + one scroll interlude. Everything else is refined 2D motion. Keeps mobile fast.
4. **Competitor research copies patterns, never assets**: captured images/HTML live in `research/` for reference only and are never shipped.
5. **Stock-only imagery with one color grade**: consistent warm grade so stock and 3D read as one world.
6. **Medical compliance posture**: no guaranteed outcomes, "illustrative imagery" labels on stock results, medical disclaimer, no PHI stored server-side beyond the booking email.

---

## Open Questions

1. Real client later? If yes, swap `site.ts`, replace stock providers with real team photos, and connect a real booking system (Boulevard / Zenoti / Vagaro embed) in place of the email-based booking flow.
2. Railway deploy in this pass or after review? Default: after review.

---

## Next Actions

- [ ] Run the prompt in `Prompt for site` in a fresh Claude Code session at the repo root
- [ ] Review `research/ELEMENTS.md` + running site
- [ ] Decide deploy

---

## References

- Build spec: `projects/velmora-medspa/BUILD-SPEC.md`
- Build prompt: `Prompt for site` (repo root)
- Workspace Astro patterns: `websites/charlie-automates/` (node adapter, Resend usage)

---

*Last updated: 2026-09-24*
