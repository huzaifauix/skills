---
name: content-diy
description: >-
  Build a content strategy from category → pillars → topics → post formats,
  then turn it into specific post ideas (title + hook), a content calendar, or
  full drafts. Saves the brand profile, pillar/topic map and an idea log in the
  project, so later runs skip onboarding and never repeat ideas. Use this
  whenever someone asks for a content strategy, content pillars, post ideas,
  "what should I post", a content calendar or posting plan, LinkedIn /
  Instagram / X / newsletter / blog topics, or says they're running out of
  content ideas, for any business, creator or niche. Also use it when they come
  back for "more ideas", ideas for one pillar or format, or drafts of ideas
  from an earlier run.
---

# Content DIY

Based on Nick Broekema's "DIY Content Strategy" framework. Credit him whenever you name or explain the method.

**Pillar + topic + format = one post.** Every topic can be told in every format, so a small map produces hundreds of ideas: 3 pillars × 14 topics × 18 formats = 756.

The multiplication is cheap; the value is elsewhere:

1. **Specific pillars and topics**, drawn from what this audience actually struggles with, not a generic list for the industry.
2. **Strong pairings.** Many topic × format combinations are weak. Keep only the ones where the format has something real to say about the topic.
3. **Memory across runs.** The project files below mean onboarding happens once and ideas never repeat.

## Project files

All state lives in `content-strategy/` at the root of the user's project:

| File | Holds | Written |
|---|---|---|
| `profile.md` | Onboarding answers: business, audience, point of view, proof, channels, voice, preferences | First run; updated when anything changes |
| `map.md` | Category, pillars, topics, custom formats | First run; updated when the user edits the map |
| `ideas.md` | Every idea generated, with ID and status | Appended every run |
| `calendar.md` | Ideas scheduled to dates | When asked for a calendar |
| `drafts/` | Full posts, one file per idea | When asked for drafts |

Templates and update rules are in `references/project-files.md`. Read it before writing any of these files.

If the user runs content for several brands in one project, use `content-strategy/<brand-slug>/` per brand and ask which brand when it's unclear.

## Step 0: Load or onboard

Look for `content-strategy/profile.md`.

- **Found:** read `profile.md`, `map.md` and `ideas.md`. Confirm in one line, e.g. *"Using your saved profile: Northside Bookkeeping, restaurant owners, LinkedIn 3×/week. Still accurate?"* Then go straight to the user's request, without waiting for a reply unless they've said something that contradicts the profile. If they correct something, update `profile.md` and carry on. Skip to "Returning runs".
- **Not found:** run onboarding, then steps 1–4.

### Onboarding

First gather what you can without asking: the conversation, and brand material in the project (README, about page, brand or positioning docs, website copy). Then ask only for what's missing, in **one message**, numbered so the user can answer quickly:

1. **What you do and sell.** The business and the offer people pay for.
2. **Who it's for.** The ideal audience, their biggest struggles, and the outcome they want.
3. **Your point of view.** What you believe that others in your space get wrong, or what you're known for.
4. **Proof you can draw on.** Real stories, client results, mistakes, milestones. These feed the story and proof formats.
5. **Where and how often.** Platforms and posting cadence.
6. **Voice.** How you sound, plus any topics or words to avoid.

If the user says "just go", fill gaps with clearly stated assumptions, save them in `profile.md` marked `(assumed)`, and proceed. Write `profile.md` as soon as you have the answers.

## Step 1: Category

One line naming the space the user wants to be known for, phrased the way their audience would search or say it (*Restaurant bookkeeping*, not *Financial services*). It should be narrow enough that a stranger knows who it's for.

## Step 2: Pillars

Propose 3 pillars (4 at most). Each pillar is a recurring theme the audience cares about, and between them they cover the whole category. Read `references/pillars-and-topics.md` for the tests a good pillar passes and the worked example from the framework.

Show the pillars with a one-line purpose each, and ask the user to confirm or adjust before generating topics. This is the one checkpoint in the first run, because everything after it depends on the pillars.

## Step 3: Topics

Generate 10–15 topics per pillar, each a short noun phrase (*Late supplier invoices*, not *How to deal with suppliers who invoice late*). `references/pillars-and-topics.md` lists sources for topics and the quality bar. Write `map.md` with the category, pillars and topics, then show the map compactly and move on. The user can edit it any time.

## Step 4: Ideas

Read `references/formats.md`: the 18 formats grouped into four families (Teach, Story, Opinion, Proof), with what each needs to work and the pairings to avoid.

Generate candidate pairings, then keep the strongest. Default output is **24 ideas**, or the number the user asks for. The set is done when it:

- covers every pillar roughly evenly;
- uses all four format families, with no single format more than 3 times;
- pairs each topic with a format that fits it, judged by the format's "needs" line in `references/formats.md`;
- follows every rule under **Preferences** and **Avoid** in `profile.md`;
- has no idea whose topic + format pair, or near-identical title, already appears in `ideas.md`.

Each idea gets:

- **ID** (`I-001`, continuing from the last ID in `ideas.md`)
- **Pillar · Topic · Format**
- **Title**: specific and concrete, in the user's voice
- **Hook**: the opening line or two, written to stop the scroll

**Story and Proof ideas depend on the user's real experience.** Write the hook around a placeholder such as `[your client's result]` or `[the moment you nearly quit]` unless the profile records the real story. Invented testimonials, client results or statistics would be published as fact under the user's name, so they always stay placeholders until the user supplies them.

Present the ideas as a table grouped by pillar, append them to `ideas.md` with status `idea`, and close with one line offering the next moves: more ideas, a calendar, or drafts of the ones they like.

## Returning runs

Interpret the request against the saved files:

- **"More ideas"**, optionally narrowed to a pillar, topic or format: run step 4 on that slice. Favour topics and formats that `ideas.md` shows are under-used.
- **Calendar or posting plan**: read the calendar section of `references/project-files.md`, schedule ideas by the cadence in `profile.md`, and write `calendar.md`.
- **Drafts**: read `references/drafting.md`, write each picked idea in full to `drafts/`, and set its status to `drafted`.
- **Status updates** ("I posted I-004", "drop I-009"): update `ideas.md`.
- **Edits to the map or profile** ("add a pillar on hiring", "we've moved to Instagram"): update the file, then show what changed.
- **Export** ("give me a spreadsheet"): write `content-strategy/ideas.csv` from `ideas.md`. Use the xlsx skill if they ask for Excel specifically.

When the request is open-ended ("let's do content"), offer these options in one line rather than guessing.

## Reference files

- `references/project-files.md`: templates for `profile.md`, `map.md`, `ideas.md` and `calendar.md`, ID and status rules, and the calendar method. Read before writing any project file.
- `references/pillars-and-topics.md`: tests for good pillars, sources for topics, the quality bar, and the worked example from the framework. Read for steps 2–3 and for map edits.
- `references/formats.md`: the 18 formats by family, what each needs, title and hook patterns, and weak pairings. Read for step 4.
- `references/drafting.md`: turning an idea into a finished post, with platform shapes for LinkedIn, X, Instagram, newsletters and blogs. Read only when writing drafts.
