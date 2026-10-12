---
name: brand-name-finder
description: >-
  use this when naming a brand, channel, product, or site and the .com must be
  available: builds modifier + niche core-word lists, combines them, checks .com
  availability, and shortlists free names
---
# Brand name finder

Goal: a shortlist of short, sayable names whose .com is actually unregistered.

## 1. Brief
Get (or infer) what it is, audience, feel (premium/playful/technical), niche, max length (default ≤9 letters before .com), words to avoid, and names already shortlisted.

## 2. Modifier list
Comprehensive, grouped by signal: testing/hands-on, honesty/trust, comparison, clarity, choosing well, money/value, buying/decisions, personality/host, tech flavor, tone/energy, size/pace, place/direction, nature/objects (mascot). Show to user; let them mark favorites.

## 3. Core / seed words for the niche
Comprehensive niche vocabulary, grouped (e.g. for hosting: core hosting, domains/DNS, speed, infrastructure, security, platforms, plans/pricing, reliability, place metaphors). Show to user; let them mark favorites.

## 4. Combine
Generate modifier+core and core+modifier pairs (plus core+object mascot pairs), filter to the length cap, drop awkward double letters and hard-to-spell results, dedupe against names already checked.

## 5. Check .com availability (before suggesting anything)
RDAP per name: `curl -s -o /dev/null -w '%{http_code}' https://rdap.verisign.com/com/v1/domain/NAME.com` — 404 = unregistered, 200 = taken. Sanity-check with a nonsense domain first. Throttle gently. Save results to a file so later rounds skip them. Optional: .co/.io for strong taken names.

## 6. Conflict check
Web-search the top finalists for existing brands, YouTube channels, and competitors in the same niche; flag overlaps.

## 7. Report
10–15 available names, ranked, each with letter count, one-line reason, and conflict flag; a top pick; note that 404 means likely free (could be premium/reserved). Offer YouTube-handle and trademark checks for finalists.

## Notes
- Short invented words and obvious one-word .coms are almost always taken; two-word pairs are where availability lives.
- Run fresh batches on request, skipping everything already checked.
