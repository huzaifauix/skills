# Project files

Everything lives in `content-strategy/` at the project root (or `content-strategy/<brand-slug>/` per brand). These files are the skill's memory: write them so a later run, or the user editing by hand, can pick up without this conversation.

General rules:

- **Edit in place.** Update the existing line or row; leave the rest of the file as it is. The user may have edited it by hand, and their edits win.
- **Dates are absolute** (`2026-10-20`), never "today" or "next week".
- **Real versus assumed.** Anything you inferred and the user hasn't confirmed is marked `(assumed)`. Remove the mark when they confirm it.

## profile.md

```markdown
# Content profile
_Last confirmed: YYYY-MM-DD_

## Business
- **What we do:**
- **Offer (what people pay for):**

## Audience
- **Who:**
- **Biggest struggles:**
- **Outcome they want:**

## Category
<one line>

## Point of view
- <belief that sets us apart from others in the space>

## Proof we can draw on
<!-- Real stories, client results, mistakes, milestones. Only what the user has supplied. -->
-

## Channels
- **Platforms:**
- **Cadence:**

## Voice
- **Tone:**
- **Avoid:**

## Preferences
<!-- Standing instructions from the user, e.g. "skip Testimonial", "hooks under 12 words", "no emojis". -->
-
```

When the user gives a standing instruction during any run ("never use Red flags", "keep it British English"), add it to **Preferences** so later runs follow it. Update `Last confirmed` whenever the user confirms or corrects the profile.

## map.md

```markdown
# Content map
**Category:** <category>

## Pillar 1: <name>
_<one-line purpose: what this pillar does for the audience>_
- <topic>
- <topic>

## Pillar 2: <name>
...

## Custom formats
<!-- Formats the user added beyond the standard 18, each with a one-line "needs". -->
```

Topics the user adds by hand count the same as generated ones. When the user removes a topic or pillar, leave its ideas in `ideas.md` untouched; only new generation skips it.

## ideas.md

```markdown
# Ideas

| ID | Status | Pillar | Topic | Format | Title | Hook | Added |
|---|---|---|---|---|---|---|---|
| I-001 | idea | Confidence | Imposter feelings | Failure story | The meeting where I froze | "I had 12 slides ready. I said nothing for 40 seconds." | 2026-10-20 |
```

- **IDs** run `I-001`, `I-002`… across the whole file and are never reused, even after an idea is dropped.
- **Status** is one of `idea`, `picked`, `scheduled`, `drafted`, `posted`, `dropped`.
- **Append** new ideas at the bottom. Escape any `|` inside a title or hook as `\|` so the table stays intact.
- **Duplicate check** before adding: the same Topic + Format pair, or a title saying the same thing, counts as a repeat. A repeated pair is allowed only when the user asks for a fresh angle on it; then make the new title clearly different.
- **Coverage**: to find under-used topics and formats, count rows per Topic and per Format, ignoring `dropped`.

## calendar.md

```markdown
# Content calendar
_Cadence: <from profile> · Generated: YYYY-MM-DD_

| Date | Day | Platform | ID | Pillar | Format | Title |
|---|---|---|---|---|---|---|
```

How to schedule:

1. Take the cadence and platforms from `profile.md`. If the user names a period ("next month", "the next 4 weeks"), cover exactly that; the default is 4 weeks starting next Monday.
2. Draw from ideas with status `idea` or `picked`, putting `picked` ones first. Generate more ideas (step 4 in `SKILL.md`) if there aren't enough.
3. Rotate pillars so the same pillar doesn't run twice in a row, and spread format families so each week mixes them, with at least one Story or Opinion post.
4. Put Proof posts (Testimonial, Objection response) near any launch or offer date the user mentions.
5. Set each scheduled idea's status to `scheduled` in `ideas.md`.

If `calendar.md` already exists, add the new period below the existing rows rather than replacing them.
