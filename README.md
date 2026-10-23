# Codex-Velmora

A complete luxury medical-spa concept site: Astro, Tailwind, React islands, an original Three.js glass scene, 13 treatment guides, booking requests, a six-question quiz, searchable support, journal and practice pages.

**Want websites like this built and making you money?** Join [CC Strategic AI +](https://www.skool.com/cc-strategic-ai-plus/about): my 27-day Claude Code mastery program with a 1-click install setup file, and you work with us to land your first AI client in 90 days, or your money back.

Full build breakdown: [Claude Code vs Codex: build a website from one prompt](https://charlieautomates.com/blog/build-website-with-claude-code-one-prompt/)

## Run locally

Use Node 22.12+ and npm. From this folder:

```sh
npm ci
npm run dev
```

Development: http://127.0.0.1:4321. To review the production build:

```sh
npm run build
npm run preview -- --port 4322
```

Production preview: http://127.0.0.1:4322. Astro 7 runs preview in the background; `npx astro preview status`, `npx astro preview logs`, and `npx astro preview stop` manage it. Rebuild and restart preview after source changes. For a foreground standalone server use `HOST=127.0.0.1 PORT=4322 npm start` after building.

## Configuration

Copy `.env.example` to `.env` for development. Leave email configuration empty to use the local demonstration: validated requests are logged, references and tentative calendars are generated, and no email is sent. Use only synthetic data in demo forms.

| Variable | Purpose |
|---|---|
| `RESEND_API_KEY` | Enables real email delivery when set |
| `SPA_INBOX_EMAIL` | Destination for booking, support, contact and gift-card requests |
| `RESEND_FROM_EMAIL` | Sender on a verified Resend domain |
| `RESEND_AUDIENCE_ID` | Optional newsletter audience; without it the practice receives a notification |
| `HOST` | Standalone bind address, `0.0.0.0` on Railway |
| `PORT` | Standalone listening port; use the host-provided value |

Supply secrets at runtime in the hosting environment. Never put credentials into `PUBLIC_` variables or version control. `npm start` reads process environment variables; it does not automatically load `.env`.

## Swap the brand

Edit `src/config/site.ts`: name, short name, URL, email, phone/link, address, coordinates, opening hours, timezone labels/offset, social links, colors, consultation terms and demo notice. These values drive shared navigation/footer, schema, canonical URLs, sitemap, crawl documents, map and booking hours. Rebuild afterward. The current booking calendar uses Arizona’s fixed UTC−07:00 offset from `site.utcOffset`. A daylight-saving timezone also needs date-aware offset conversion in `src/lib/booking.ts`.

Editorial copy and clinical offerings are separate: treatments/prices in `src/data/treatments.ts`, providers in `src/data/team.ts`, memberships in `src/data/memberships.ts`, help in `src/data/help.ts`, articles in `src/content/journal/`. Review place-specific prose, fictional credentials and sample policies when adapting to a real practice. Replace portraits, proof and the OG image with client-approved assets. Keep illustrative-result labels until genuine consented results exist. Fonts/spacing live in `src/styles/tokens.css` and `tailwind.config.mjs`.

## What the flows do

Booking is a four-step **request**, not a live reservation: next 30 days, practice hours, validation, refresh persistence, reference, confirmation page and tentative `.ics`. Contact, support, gift-card and newsletter routes accept JSON. Gift cards are inquiries; no payment or gift balance is created. Quiz results are non-diagnostic discussion starters.

All five endpoints use Zod, a honeypot, same-origin checks, a request-size cap and a shared five-per-minute IP limit. Rate limits are in-memory and per server process. A scaled production practice should use a shared rate-limit store and its actual scheduling system. Request details are not written to a database or application files; demo logging can be retained by the process host. Avoid private health details in these forms.

Resend sends practice notifications and a booking acknowledgment with calendar attachment. The local test suite mocks the Resend transport, including failures; real inbox delivery is intentionally untested. If the practice notification succeeds but the acknowledgment fails, the request remains received and the failure is logged against its reference.

## Railway deployment instructions

No deployment was performed. When ready, use a Node service rooted at `websites/Codex-Velmora` (or this folder in a dedicated repository). Install with `npm ci`, build with `npm run build`, and start with `npm start`. Set `HOST=0.0.0.0`, use Railway's supplied `PORT`, and add the email variables as service secrets. Set the public URL in `site.ts` before rebuilding; configure the domain and use `/` as a healthcheck. No database or volume is needed for this request-based demonstration.

See [Railway's Astro deployment guide](https://docs.railway.com/guides/astro) and [Astro's Railway guide](https://docs.astro.build/en/guides/deploy/railway/). This project already uses the standalone Node adapter; do not replace it with static-only hosting because `/api/*` needs a server.

## Evidence and design decisions

- [Acceptance report](verification/ACCEPTANCE.md): pass/fail evidence and limitations.
- [Research adaptations](research/ELEMENTS.md): ten sites and the original pattern adapted from each.
- [Credits](CREDITS.md): all photography and the local CC0 studio HDRI.
- [Design system](design-system.md), live at `/styleguide` (noindex).
- [Security version decision](verification/SECURITY-DECISION.md): Astro 7 and matching adapters replace the requested Astro 5 because of audit findings. Tailwind 3 remains via PostCSS.
- `verification/pages/`: all full-page desktop/mobile captures. `verification/review/`: visual review sheets.
- `verification/lighthouse-*-final.report.html`: mobile performance reports.
- `.paul/`: preserved specification, plans, summaries and completion state.

3D is dynamically imported and pauses offscreen. Desktop uses the live scene; small screens, reduced-motion and unavailable WebGL use the original AVIF poster. Four Method steps remain readable without motion. The mobile performance choice is deliberate, with the desktop scene and full scroll sequence retained.

## Repeat verification

Microsoft `playwright-cli` is used for browser checks. Start preview with email disabled, then:

```sh
playwright-cli -s=velmora-qa open http://127.0.0.1:4322
playwright-cli -s=velmora-qa run-code --filename=scripts/booking-check.js
playwright-cli -s=velmora-qa run-code --filename=scripts/interaction-check.js
playwright-cli -s=velmora-qa run-code --filename=scripts/forms-check.js
playwright-cli -s=velmora-qa run-code --filename=scripts/page-audit.js
node scripts/api-negative-check.mjs
node scripts/email-check.mjs
python3 scripts/artifact-check.py
```

Allow a minute between submission batches when running against the same preview server; production rate limiting deliberately applies to tests too. The negative and mocked-email tests launch their own isolated local servers. Screenshot scripts currently save to this workspace's absolute build path; update that path if moving the project. `research/` is reference-only and never imported into application assets.

More free Claude Code tools: [charlieautomates.com](https://charlieautomates.com/free-resources/) · Go deeper inside [CC Strategic AI +](https://www.skool.com/cc-strategic-ai-plus/about)
