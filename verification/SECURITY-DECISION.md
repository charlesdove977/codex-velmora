# Security exception to original Astro 5 version

The original prompt permits stack changes with a logged reason. npm audit on 2026-09-24 reported an Astro critical AVIF optimization advisory plus high-severity SSRF/XSS advisories, with no patched Astro 5 release indicated. Upgrade Astro and its official adapters to supported patched versions while retaining Astro, Tailwind 3, React islands and the requested architecture. Update Sharp and Lighthouse as well. This is a security maintenance exception, not a change to product scope.

Primary evidence: https://github.com/advisories/GHSA-26w7-cxv4-gfx2 (patched Astro 7.2.8, Sharp 0.35.4). Upgrade reference: https://docs.astro.build/en/guides/upgrade-to/v7/ . Original audit preserved in dependency-audit.json. Final audit and build must be recorded after migration.
