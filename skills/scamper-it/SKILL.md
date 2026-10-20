---
name: scamper-it
description: Run the SCAMPER creative-thinking method (Substitute, Combine, Adapt, Modify/Magnify/Minify, Put to other uses, Eliminate, Reverse/Rearrange) to generate and SHOW draft variations of content and marketing campaigns, writing (fiction, articles, copy, headlines, blurbs), visual/UI/graphic design (infographics, social posts, landing pages, covers), products, and business processes. It maps the request into areas first, then delivers real drafts (rewritten copy, design artboards, concept cards), not just idea lists. Use this whenever the user mentions SCAMPER (or "SCRAMPER"), asks to brainstorm variations or fresh angles, "remix", "repurpose" a template/infographic/post for a new topic, "make this less generic", rework an existing draft/design/campaign/process, find alternatives to something that already exists, or asks a single-lens question like "what could we eliminate here" or "what if we reversed this" — even if they never name the method. Also use it to plan or facilitate a SCAMPER workshop for a team.
---

# SCAMPER

SCAMPER is a checklist of seven operators applied to something that **already exists** (a draft, design, template, campaign, product or process) to provoke new versions of it. It comes from Alex Osborn's checklist of about 70 idea-spurring questions (*Applied Imagination*, 1953). Bob Eberle turned it into an acronym in 1971, and Michael Michalko's *Thinkertoys* (1991) popularized it. ("SCRAMPER" is a misspelling.)

SCAMPER reliably produces **more and wider** ideas, but not reliably more *original* ones, because it anchors on the starting thing. So in this skill, quality comes from four habits:

1. Map the request into areas and parts.
2. Push past the first obvious answer.
3. Show ideas as **drafts** people can judge with their eyes.
4. Select deliberately at the end.

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

### 1. Map: show it, then keep going

Split the request into **areas**, the separate things SCAMPER will work on. One request often holds more than one. "Repurpose this infographic for a new topic" is a **layout** area and a **content** area. A launch plan may be **offer**, **channel** and **message**. Common areas:

- layout / visual
- content / copy
- offer / CTA
- format / channel
- audience
- process / steps

For each area, list the **parts** that carry it, with their **limits**: slots, counts, character lengths, sizes. Then mark which letters bite where. `references/domains.md` has part lists and typical limits for each domain.

Show the map as a compact table at the top of your reply, plus one line of assumptions (audience, platform, size, what stays fixed). Then **continue without waiting for approval**. The user redirects afterwards if they need to. Ask a question first only if the subject itself is too ambiguous to map.

```markdown
**SCAMPER map**: <subject>
| Area | Parts (limits) | Letters |
|---|---|---|
| Content | cover headline (≤8 words), 6 slide titles (≤5 words), 1 tip per slide, CTA slide | S, C, M, E |
| Layout | 8-slide carousel, numbered steps, before/after split on slide 4 | A, R (only where the metaphor breaks) |
**Assumptions:** Instagram audience · 1080×1350 · keep the layout, change the content
```

### 2. Diverge per area (in your head or a scratch file)

Run the letters inside each area, part by part. The quality rules:

- **Apply each letter where it bites.** Work part by part, not on the whole subject. You don't need to fill every cell.
- **Push past the first answer.** Ask "How else? What else?". The first idea is the one everyone has.
- **Keep at least one bold idea per area.** Deliberately far out. It can be scaled back later.
- **Give Eliminate and Reverse real effort.** People are biased toward adding things.
- **Cover modify, magnify *and* minify.**
- **Adapt from distant fields** (other industries, nature, history, games, sport), not close competitors.
- **Write ideas concretely,** as a specific sentence someone could picture.
- **Respect limits.** Content must fit the slots the layout gives it (see the two-track rule below).
- **Don't judge yet.**

When the cheat sheet runs dry, or the user named specific letters, read `references/letters/<letter>.md`. Each file has 10–15 trigger questions and prompts per domain.

### 3. Compose three variations

Turn the raw ideas into **three coherent directions**. A direction combines moves across areas into one version someone would actually ship. It is never one variant per letter.

- **A: Close.** Faithful to the original, with the clearest wins applied.
- **B: Balanced.** The strongest mix of new and feasible. Usually your recommendation.
- **C: Bold.** Built on the most daring idea, scaled back until it is buildable.

Give each a short name, the letters behind it, and one line on why it works. Ideas that didn't make a variation go into a **Backlog** line: at most 8 one-liners, each tagged with its letter.

### 4. Render the drafts in the subject's own medium

The user needs to *see* the variations. Read `references/drafting.md` for the exact formats.

- **Copy and writing.** Show the original first, then the three variants as finished text, each with its name and letters.
- **Visual design** (infographics, posts, slides, landing sections, covers):
  - If a design canvas or artifact tool is available, put one artboard per variation on **one canvas**, with the original's structure as the reference.
  - If not, write **one HTML file** with the three variants side by side.
  - Draft at low-to-medium fidelity: real copy, real layout, real colours. Polish comes after the user picks.
- **Campaigns, ideas, products.** Write one concept card per variation: name, hook, a sample post or line, a visual note, and the first step.
- **Processes.** Show before → after: the steps as a flow, with removed and moved steps marked.

### 5. Close (this is part of the deliverable, and it is always written)

End your final message with this block. If a tool would end your turn (a wrap-up or next-step box, a question card), write the block first. Skipping it hides the reasoning, which is the point of the method.

```markdown
**What changed**
| Original part | Variation A / B / C | Letter |
|---|---|---|

**Recommendation:** B, because … · **Riskiest assumption:** … · **Cheapest test:** …
**Backlog:** (S) … · (E) … · (R) …
Pick one to develop, or combine (e.g. "B with C's headline").
```

Keep the "What changed" table to the parts that changed. Use one column per variation when they differ part by part, or one "New" column when one variation is the focus.

### 6. Develop (the next turn)

When the user picks a variation or a combination, polish it to final fidelity. Run a quick second SCAMPER pass on that variation alone (merge it with the best backlog idea, push its weakest part), and deliver the finished piece.

## Modes

Read the request and pick one.

| Mode | When | Shape |
|---|---|---|
| **Full session** | "SCAMPER this", "brainstorm our launch" | Map → 3 drafted variations → close. Add a NUF score row for A/B/C (New, Useful, Feasible, 1–5) in the close. |
| **Repurpose a template** | "Use this infographic / post / deck / page for topic X" | Read `references/repurpose.md`. Take an inventory of the slots, keep the layout by default, run the content track, fit-check, then show the drafts. |
| **Focused lens** | The user names letters ("what can we eliminate?") | Map limited to those letters, read their letter files, go deeper (more parts, more distant analogies), then draft. The three variations can be three strengths of the same letter. |
| **Quick pass** | "A few fresh angles on this headline" | Text only: 1–3 strong ideas per letter as concrete lines, then your top pick and why. No map, no drafts, no table. |
| **Facilitate** | The user will run SCAMPER with a team | Read `references/facilitation.md`. Agenda, timing, a prompt card per letter, the selection method. |

If it's unclear, default to a compact full session, and offer a focused lens on any area.

## The two-track rule: layout and content

When a subject has both a visual structure and the words that fill it:

- **The content track always runs.** Run SCAMPER on the message, and fit every new text to the limit of the slot it fills.
- **The layout track runs lightly by default.** Check each visual metaphor (ladder, pyramid, timeline, arrows, price tags) against the new topic. If the metaphor still means something, keep it and give it a new meaning (a salary slot becomes a word-count slot). If it doesn't, run SCAMPER on that piece only.
- **Run the full layout track when** the user asks to rework the design, or when no variation can work without it. Variation C is a good place for a layout move.
- **Prompt overrides:**
  - "keep the layout exactly": content only;
  - "rework the layout too": both tracks in full;
  - "content only, I'll design it": skip rendering and deliver the slot-by-slot copy.

## Brevity

- **No preamble about what SCAMPER is**, unless the user asked.
- **The map is a table, not prose.**
- **The drafts are the main body,** with rationale kept to one line each.
- **The backlog has at most 8 one-liners.**
- **Scoring rows appear only in full sessions.**
- **The user's numbers win.** If they ask for 5 variations or no drafts, do that.

## Accuracy when citing real-world examples

Use the verified examples in the letter files. Avoid these widely repeated myths:
- Columbus "proving the Earth round";
- AWS from "excess capacity" (Amazon's CTO denied it);
- Ray Kroc inventing self-service (it was the McDonald brothers' 1948 Speedee system);
- Carver's "300 peanut uses" as commercial products;
- Gutenberg as simply "wine press + coin punch".

Never invent statistics. Unknown facts and names become placeholders like [YOUR NAME].

## When SCAMPER is the wrong tool

Say so briefly, then offer the better tool or a combination.

- **The problem is unclear.** Define it first (jobs-to-be-done, 5 Whys, a journey map).
- **A hard technical trade-off.** Use TRIZ.
- **A huge space of combinations.** Use a morphological box, with SCAMPER filling its columns.
- **The team needs to decide, not generate.** Use Six Thinking Hats, PMI or a weighted matrix.
- **A blue-sky invention with no anchor.** Use brainwriting first, then SCAMPER the results.

## Reference files

Load only what the task needs.

- `references/drafting.md`: how to render drafts in each medium. Design canvas artboards, the HTML side-by-side fallback, copy comparison, concept cards, before/after flows, fidelity levels.
- `references/repurpose.md`: repurposing a template. Slot inventory, defaults and overrides, fit checklist, a worked mapping example.
- `references/domains.md`: part lists and typical limits for content and marketing, writing, visual/UI/graphic design, product, business and process work, and publishing.
- `references/letters/`: one file per letter (`substitute.md`, `combine.md`, `adapt.md`, `modify-magnify-minify.md`, `put-to-other-uses.md`, `eliminate.md`, `reverse-rearrange.md`). Each has trigger questions, domain prompts, pitfalls and verified examples.
- `references/evaluation.md`: selection tools (NUF, impact/effort, How–Now–Wow, PMI, dot voting, weighted matrix), hybridizing, next-step templates.
- `references/facilitation.md`: group sessions, timing, combining with other methods, the evidence and its limits, history and variants.
