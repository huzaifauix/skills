---
name: scamper-it
description: Run SCAMPER (Substitute, Combine, Adapt, Modify/Magnify/Minify, Put to other uses, Eliminate, Reverse/Rearrange) to generate and SHOW draft variations of content and marketing, writing (copy, headlines, blurbs, articles, fiction), visual design (infographics, social posts, carousels, landing pages, covers), products and processes. It first reads the intent of the request (goal, what to keep vs change, how much effort), asks only if blocked, then delivers three real drafts (copy, artboards, concept cards), not just idea lists. Use this whenever the user mentions SCAMPER (or "SCRAMPER"), wants variations or fresh angles, wants to "remix", "repurpose" or "reformat" something (a template, infographic, post, blog) for a new topic, format or audience, designs something "like this reference", wants to make something less generic, reworks an existing draft, design, campaign or process, or asks "what could we eliminate / reverse here", even if they never name the method. Also for planning a SCAMPER workshop.
---

# SCAMPER

SCAMPER is a checklist of seven operators applied to something that **already exists** (a draft, design, template, campaign, product or process) to provoke new versions of it. It comes from Alex Osborn's checklist of about 70 idea-spurring questions (*Applied Imagination*, 1953). Bob Eberle turned it into an acronym in 1971, and Michael Michalko's *Thinkertoys* (1991) popularized it. ("SCRAMPER" is a misspelling.)

SCAMPER reliably produces **more and wider** ideas, but not reliably more *original* ones, because it anchors on the starting thing. So in this skill, quality comes from five habits:

1. Read what the user actually wants changed, and what must stay.
2. Map the subject into areas and parts.
3. Push past the first obvious answer.
4. Show ideas as **drafts** people can judge with their eyes.
5. Select deliberately at the end.

## The operators (cheat sheet)

| Letter | Operator | Core questions | The mental move |
|---|---|---|---|
| **S** | Substitute | What could replace this part, material, person, channel, rule, time, tone? | Separate the *function* from the thing currently doing it |
| **C** | Combine | What could merge: features, purposes, audiences, formats, partners, steps? | Blend two normally separate frames |
| **A** | Adapt | What else is like this? Who solved it elsewhere: another industry, nature, history, games? | Analogy: borrow the *mechanism*, not the look |
| **M** | Modify / Magnify / Minify | Change an attribute (meaning, colour, shape, tone). 10× bigger, more frequent, exaggerated? 1/10, condensed, split, understated? | Push attributes to extremes to see which matter |
| **P** | Put to other uses | Who else could use it, where, for what? What could leftovers, data or by-products become? | Ask "what else is this good for?" |
| **E** | Eliminate | What could be removed, simplified or skipped and still work? What is the one thing it must do? | Subtraction. People neglect it and default to adding |
| **R** | Reverse / Rearrange | What's the opposite? Flip the order, roles, cause and effect. What if the last step came first? | Invert hidden assumptions and defaults |

The letters overlap (Eliminate vs Minify, Substitute vs Adapt, Reverse vs Rearrange). That's fine. They are prompts, not categories, so never spend effort deciding which letter an idea belongs to.

## How every run works

Every run except a quick pass follows six steps. Steps 1, 4 and 5 are visible to the user. Steps 2 and 3 are mostly your own thinking.

### 1. Assess and map: show it, then keep going

**First, read the intent** (see `references/assess.md`). SCAMPER only works well when it transforms the right thing, so before any letters, decide:

- **Goal:** the job underneath the request, in a phrase. "An infographic about sleep" is really "help tired parents fix bad nights".
- **Keep / Change:** which dimensions stay fixed and which SCAMPER may touch: message, format, layout, audience, purpose, channel, length, style. Read them from the wording. Anything not mentioned stays **Keep**.
- **Effort:**
  - **light:** a quick pass, text only;
  - **standard:** the full run with drafts.
  "A few angles", "quick" and one-liners are light. Everything else is standard.

**Ask only if blocked.** If something critical is missing and can't be reasonably assumed (no clear subject, conflicting goals, no idea what "good" means), ask 1–3 questions in one batch, multiple choice where possible, each with a recommended default. Then stop. Everything else becomes a stated assumption.

**Then map the subject.** Split it into **areas**: layout/visual, content/copy, offer/CTA, format/channel, audience, process/steps. For each area, list the **parts** that carry it, with their **limits**: slots, counts, character lengths, sizes. Then mark which letters bite where. Only areas marked Change get letters. `references/domains.md` has part lists and typical limits.

Show the Assess line and the map at the top of the reply, then **continue without waiting**:

```markdown
**Read as:** template reuse · **Goal:** help tired parents fix bad nights · **Keep:** layout, style · **Change:** topic · **Effort:** standard · *Say "change layout" or "quick" to adjust.*
| Area | Parts (limits) | Letters |
|---|---|---|
| Content | cover headline (≤8 words), 6 slide titles (≤5 words), 1 tip per slide, CTA slide | S, C, M, E |
| Layout | 8-slide carousel, numbered steps, before/after split on slide 4 | — (kept) |
```

"Read as" uses one of seven fixed labels: full session · template reuse · reformat · from a reference · focused lens · quick pass · custom.

### 2. Diverge per area (in your head or a scratch file)

Run the letters inside each area marked Change, part by part. The quality rules:

- **Apply each letter where it bites.** Work part by part, not on the whole subject. You don't need to fill every cell.
- **Push past the first answer.** Ask "How else? What else?". The first idea is the one everyone has.
- **Keep at least one bold idea per area.** Deliberately far out. It can be scaled back later.
- **Give Eliminate and Reverse real effort.** People are biased toward adding things.
- **Cover modify, magnify *and* minify,** and name which one wherever an M idea appears ("M · Minify").
- **Adapt from distant fields** (other industries, nature, history, games, sport), not close competitors.
- **Write ideas concretely,** as a specific sentence someone could picture.
- **Respect limits.** Content must fit the slots the layout gives it (see the two-track rule below).
- **Don't judge yet.**

When the cheat sheet runs dry, or the user named specific letters, read `references/letters/<letter>.md`. Each file has 10–15 trigger questions and prompts per domain.

### 3. Compose three variations

Turn the raw ideas into **three coherent directions**. A direction combines moves across areas into one version someone would actually ship. It is never one variant per letter.

- **A: Close.** Faithful to the original, with the clearest wins applied.
- **B: Balanced.** The strongest mix of new and feasible. Usually your recommendation.
- **C: Bold.** Built on the most daring idea, scaled back until it is buildable. C should be clearly further from the original than B, not B plus one tweak. Bold is not exempt: C still fits every slot limit (a quoted line used as a headline counts too; if it's too long, put it in the subhead) and drops every phrase the user asked to drop.

**If layout is marked Change**, at least two of the three drafts need a genuinely different structure: a different spatial arrangement and reading order, not a new metaphor over the same arrangement. Name the structure in each draft's one-line note.

If the user explicitly asked for SCAMPER, show a compact **Ideas by letter** block before the drafts: one line per letter, with the strongest idea for each.

Give each draft a short name, the letters behind it, and one line on why it works. Ideas that didn't make a draft go into a **Backlog** line: at most 5 one-liners, each tagged with its letter.

### 4. Render the drafts in the subject's own medium

The user needs to *see* the variations. Read `references/drafting.md` for the exact formats.

- **Copy and writing.** Show the original first, then the three variants as finished text, each with its name and letters.
- **Visual design** (infographics, posts, slides, landing sections, covers):
  - If a design canvas or artifact tool is available, put one artboard per variation on **one canvas**.
  - If not, write **one HTML file** with the three variants side by side.
  - Draft at low-to-medium fidelity: real copy, real layout, real colours. Polish comes after the user picks.
- **Screens and flows** (checkout, onboarding, app screens). Show before → after, plus a phone-sized mockup of each draft's key screen.
- **Campaigns, ideas, products.** Write one concept card per variation: name, hook, a sample post or line, a visual note, and the first step.
- **Processes.** Show before → after: the steps as a flow, with removed and moved steps marked.

### 5. Close (part of the deliverable; every run except a quick pass)

End your final message with this block. If a tool would end your turn (a wrap-up or next-step box, a question card), write the block first. Skipping it hides the reasoning, which is the point of the method.

```markdown
**What changed**
| Original part | A | B | C | Letters |
|---|---|---|---|---|

**Recommendation:** B, because … · **Riskiest assumption:** … · **Cheapest test:** …
**Backlog:** (S) … · (E) … · (R) …
**Checked:** what you actually verified, e.g. "rendered, no overlaps", or "not visually checked"
Pick one to develop, or combine (e.g. "B with C's headline").
```

- **The close is the end of the message.** Nothing comes after the pick prompt.
- **Keep the table to the parts that changed.**
- **The riskiest assumption and cheapest test belong to the recommended draft.** If the recommendation is a sequence ("A now, B next"), give them for the main pick.
- **"Checked" only claims what you really verified.** Before writing "all invented details bracketed" or "no clichés reused", search the drafts for them.
- **Don't offer other formats here.** Wait until the user has settled.

### 6. Develop (the next turn)

When the user picks a variation or a combination, polish it to final fidelity. Run a quick second SCAMPER pass on that variation alone (merge it with the best backlog idea, push its weakest part), and deliver the finished piece. If they redirect instead ("more layout options"), run steps 2–5 again in that direction.

**Once the user has settled** (they've picked, and the final piece is delivered or approved), offer other formats **once**, in one line, only when the piece could live elsewhere:

> Want this adapted to another format too, for example a carousel, a thread or a short video script?

Never offer this in the draft round. Never produce other formats unasked.

## Modes

Read the request and pick one.

| Mode | When | Shape |
|---|---|---|
| **Full session** | "SCAMPER this", "brainstorm our launch" | Assess and map → 3 drafted variations → close. Add a NUF score row for A/B/C (New, Useful, Feasible, 1–5) in the close. |
| **Repurpose** | "Use this infographic / post / deck for topic X", "turn this post into…", "design X like this reference" | Read `references/repurpose.md`. The wording decides which kind:<br>• **template reuse:** keep the layout, change the content;<br>• **reformat:** keep the message, change the format. Deliver **one** target format, the one named or the best fit stated in the Assess line, as three takes in that format;<br>• **from a reference:** keep the idea, change the layout (2 of 3 drafts get a new structure). |
| **Focused lens** | The user names letters ("what can we eliminate?") | Map limited to those letters, read their letter files, go deeper (more parts, more distant analogies), then draft. The three variations can be three strengths of the same letter. |
| **Quick pass** | "A few fresh angles on this headline" | 5–6 concrete options from the letters that bite best, one top pick with a one-line reason. No map, no drafts, no table. Under 300 words. |
| **Facilitate** | The user will run SCAMPER with a team | Read `references/facilitation.md`. Agenda, timing, a prompt card per letter, the selection method. |

If it's unclear, default to a compact full session, and offer a focused lens on any area.

## The two-track rule: layout and content

When a subject has both a visual structure and the words that fill it:

- **The content track always runs.** Run SCAMPER on the message, and fit every new text to the limit of the slot it fills.
- **The layout track follows Keep / Change.** If layout is kept, check each visual metaphor (ladder, pyramid, timeline, arrows) against the new topic. Keep it with a new meaning when it still works, and change only the piece that breaks. If layout is marked Change (a reference, or "rework the design"), run the full layout track.
- **Prompt overrides:**
  - "keep the layout exactly": content only;
  - "rework the layout too": both tracks in full;
  - "content only, I'll design it": skip rendering and deliver the slot-by-slot copy.

## Brevity

- **No preamble about what SCAMPER is**, unless the user asked.
- **The Assess line is one line; the map is a table, not prose.**
- **The drafts are the main body,** with rationale kept to one line each. Everything else totals about 350 words.
- **The backlog has at most 5 one-liners.**
- **Scoring rows appear only in full sessions.**
- **The user's numbers win.** If they ask for 5 variations or no drafts, do that.

## Accuracy when citing real-world examples

Use the verified examples in the letter files. Avoid these widely repeated myths:
- Columbus "proving the Earth round";
- AWS from "excess capacity" (Amazon's CTO denied it);
- Ray Kroc inventing self-service (it was the McDonald brothers' 1948 Speedee system);
- Carver's "300 peanut uses" as commercial products;
- Gutenberg as simply "wine press + coin punch".

Never invent statistics. Unknown facts and names become placeholders like [YOUR NAME]. Nothing from a source creator (name, handle, logo, signature claim) carries into the drafts.

## When SCAMPER is the wrong tool

Say so briefly, then offer the better tool or a combination.

- **The problem is unclear.** Define it first (jobs-to-be-done, 5 Whys, a journey map).
- **A hard technical trade-off.** Use TRIZ.
- **A huge space of combinations.** Use a morphological box, with SCAMPER filling its columns.
- **The team needs to decide, not generate.** Use Six Thinking Hats, PMI or a weighted matrix.
- **A blue-sky invention with no anchor.** Use brainwriting first, then SCAMPER the results.

## Reference files

Load only what the task needs.

- `references/assess.md`: reading intent. Clarity check, when to ask, Keep/Change dimensions, phrasing cues, effort, the Assess line.
- `references/repurpose.md`: template reuse, reformat and from a reference. Slot inventory, fit checklist, a worked example.
- `references/drafting.md`: how to render drafts in each medium. Design canvas artboards, the HTML side-by-side fallback, copy comparison, screens, concept cards, before/after flows, fidelity levels.
- `references/domains.md`: part lists and typical limits for content and marketing, writing, visual/UI/graphic design, product, business and process work, publishing, and reformat targets.
- `references/letters/`: one file per letter (`substitute.md`, `combine.md`, `adapt.md`, `modify-magnify-minify.md`, `put-to-other-uses.md`, `eliminate.md`, `reverse-rearrange.md`). Each has trigger questions, domain prompts, pitfalls and verified examples.
- `references/evaluation.md`: selection tools (NUF, impact/effort, How–Now–Wow, PMI, dot voting, weighted matrix), hybridizing, next-step templates.
- `references/facilitation.md`: group sessions, timing, combining with other methods, the evidence and its limits, history and variants.
