---
name: brand-name-finder
description: >-
  Find brand names whose .com is actually unregistered. Builds modifier and
  niche word lists, mixes naming styles (compounds, blends, invented words,
  metaphors), bulk-checks .com/.co/.io/.ai and YouTube handles with a bundled
  script, flags existing brands, and returns a ranked shortlist. Use this
  whenever someone wants to name or rename a business, startup, product, app,
  YouTube channel, podcast, newsletter, agency, or website, asks for "name
  ideas", "domain ideas" or "what should I call it", or asks whether a name or
  domain is available, even if they never mention .com.
---
# Brand name finder

Goal: a shortlist of short, sayable, distinctive names whose .com is actually unregistered, with the main conflicts already flagged.

Names that sound good are cheap; names that are free are rare. So the whole process is built around generating many varied candidates and checking them in bulk *before* recommending anything. Never present a name as available unless the script has checked it this session or in the cache.

## Tools in this skill

- `scripts/names.py combine` builds modifier+core pairs from two word-list files, filtered by length, with awkward joins removed and already-checked names skipped.
- `scripts/names.py check` checks availability through registry RDAP (404 = free, 200 = taken) for `.com` plus optional `.co,.io,.ai,.net,.app,.dev,.xyz`, and YouTube handles with `--youtube`. It sanity-checks with a nonsense name, retries on rate limits, and caches results in a JSON file so later rounds skip names it has already seen.
- `references/naming-styles.md` covers naming styles beyond plain pairs, plus quality filters. Read it before generating candidates (step 4).

Run `python3 <skill-dir>/scripts/names.py --help` for full options. Keep all working files (word lists, `name-checks.json`) in one folder for this naming project, so every round reuses the same cache.

## 1. Brief

If the user arrives with a favourite name that's taken, start there: check its close variants (see "Follow-up rounds") in the first batch, and put any free ones in the shortlist next to the new names. They already like that name, so a free variant is often the best answer.

Get, or infer from the conversation, what's being named, the audience, the feel (premium, playful, technical, calm…), the niche, the max length (default 9 letters before `.com`), words or sounds to avoid, names already tried or shortlisted, and which extras matter (other domain endings, YouTube, other socials). Ask only for what you can't reasonably infer, in one short message. If the user already gave enough, state your assumptions and move on.

## 2. Modifier list

Write a broad modifier list grouped by the signal each word sends, picking the groups that fit the brief. Typical groups: trust/honesty, expertise/testing, clarity/simplicity, speed/energy, value/money, choice/decision, premium/craft, personality/host, tech flavour, size/pace, place/direction, and nature/objects (for mascot-style names). Aim for roughly 60–120 words in total, short words first.

## 3. Core / seed words for the niche

Write the niche's vocabulary, grouped by sub-topic. For hosting, for example: core hosting, domains/DNS, speed, infrastructure, security, platforms, plans/pricing, reliability, and place metaphors. Include adjacent-world metaphor words (harbour, forge, nest, orbit…) because they produce more distinctive names than literal ones.

**Pause here.** Show both lists compactly (groups on one line each) and ask the user to mark favourites, cut anything they dislike, or add words. Their picks steer everything after this. If the user said to skip the pause, or you are running unattended, pick the strongest ~30 modifiers and ~20 cores yourself, say which you picked, and continue.

## 4. Generate candidates in several styles

Save the chosen words to `mods.txt` and `cores.txt`, then:

```bash
python3 <skill-dir>/scripts/names.py combine --mods mods.txt --cores cores.txt --max-len 9 --seen name-checks.json > pairs.txt
```

The script output is raw material. Don't check all of it blindly; hand-pick the pairs that pass the quality filters in `references/naming-styles.md`. Then add names in other styles from that file (blends, unexpected pairings, invented words, alliteration, suffixes) so that at least four styles are represented. A good batch is 80–200 candidates. Generic `adjective+noun` names should be under half of the batch.

## 5. Check availability before suggesting anything

```bash
python3 <skill-dir>/scripts/names.py check --file candidates.txt --tlds com --cache name-checks.json
```

- Check `.com` for the whole batch first. Then re-run on the `.com`-free names with the extras the user cares about, for example `--tlds com,co,io,ai --youtube`. This keeps the slow, rate-limited checks to a small set.
- If the sanity-check warning appears, that column is unreliable: wait and re-run, and don't report results from it.
- If fewer than ~10 names come back free, generate another batch, leaning on the styles and words that produced free names, and check again. Don't pad the shortlist with taken names.

## 6. Conflict check on finalists

For the top ~10 free names, web-search each one, in quotes, with the niche. Flag existing companies, apps, YouTube channels or products with the same or a confusingly similar name, especially in the same niche. A free `.com` doesn't mean the name is unused.

Instagram, TikTok and X block automated handle checks, so the script can't verify them. Give the user profile links to check by hand (`instagram.com/NAME`, `tiktok.com/@NAME`, `x.com/NAME`) rather than guessing.

For trademarks, give the search links (USPTO: `tmsearch.uspto.gov`; EU: `euipo.europa.eu/eSearch`; UK: `trademarks.ipo.gov.uk`), note any obvious same-class hits you found while searching, and say a real clearance needs a professional.

## 7. Report

Use this structure:

```
## Top pick: Name.com
One or two sentences on why it fits the brief.

## Shortlist (all .com unregistered as of <date>)
| # | Name | Letters | Style | Why it works | Also free | Conflicts |
|---|------|---------|-------|--------------|-----------|-----------|
(10–15 rows, ranked; "Also free" lists the other endings and YouTube that came back free; "Conflicts" is "none found" or a short note)

## Notes
- "Unregistered" means the registry has no record; a registrar may still price it as premium or hold it reserved, so confirm at checkout.
- Manual checks still to do: Instagram / TikTok / X links, and a trademark search for the finalists.
- <n> names checked this round (<n> free); all saved in name-checks.json for the next round.
```

Then offer a next round: a fresh batch in the styles the user liked, more extras for finalists, or variations on a favourite.

## Follow-up rounds

Reuse the same folder and `name-checks.json` so nothing gets re-checked. When the user likes a name whose .com is taken, try close variants: plural or singular, a prefix (get, try, use, hey), a suffix (hq, app, labs, studio), a swapped word order, or a synonym for one half. Present these as variants of the name they liked.
