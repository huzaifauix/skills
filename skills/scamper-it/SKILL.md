---
name: scamper-it
description: Run the SCAMPER creative-thinking method (Substitute, Combine, Adapt, Modify/Magnify/Minify, Put to other uses, Eliminate, Reverse/Rearrange) to generate, improve, or rework ideas for content and marketing campaigns, writing (fiction, articles, copy, headlines), visual/UI/graphic design, products, and business processes. Use this whenever the user mentions SCAMPER (or "SCRAMPER"), asks to brainstorm variations or fresh angles, "remix", "repurpose", "make this less generic", rework an existing draft/design/campaign/process, find alternatives to something that already exists, or asks a single-lens question like "what could we eliminate here" or "what if we reversed this" — even if they never name the method. Also use it to plan or facilitate a SCAMPER workshop for a team.
---

# SCAMPER

SCAMPER is a checklist of seven operators you apply to something that **already exists** (a draft, a design, a campaign, a product, a process) to provoke new ideas. It descends from Alex Osborn's roughly 70 "idea-spurring questions" in *Applied Imagination* (1953). Bob Eberle packed them into the SCAMPER acronym in 1971, and Michael Michalko's *Thinkertoys* (1991) popularized it for business. ("SCRAMPER" is a common misspelling, not a different method.)

What it is good and bad at matters for how you run it. Studies consistently find SCAMPER increases the **number and range** of ideas. It is much less reliable at raising **originality**, because it anchors on the starting artifact. So the quality comes from three things the checklist alone does not give you:

1. Breaking the subject into attributes.
2. Pushing past the first obvious answer for each letter.
3. A real selection step at the end.

The workflow below is built around those three things.

## The operators (cheat sheet)

| Letter | Operator | Core questions | The mental move |
|---|---|---|---|
| **S** | Substitute | What could replace this part, material, person, channel, rule, time, tone? | Separate the *function* from the thing currently doing it |
| **C** | Combine | What could merge: features, purposes, audiences, formats, partners, steps? | Blend two normally separate frames |
| **A** | Adapt | What else is like this? Who solved a similar problem elsewhere: another industry, nature, history, games? | Analogy: borrow the *mechanism*, not the look |
| **M** | Modify / Magnify / Minify | Change an attribute (meaning, colour, shape, motion, tone). What if it were 10× bigger, more frequent, exaggerated? Or 1/10, condensed, split, understated? | Push attributes to extremes to see which ones matter |
| **P** | Put to other uses | Who else could use it, where, for what? What could the leftovers, waste, data or by-product become? | Ask "what else is this good for?" |
| **E** | Eliminate | What could be removed, simplified, skipped, and still work? What is the one thing it must do? | Subtraction. People neglect it and default to adding |
| **R** | Reverse / Rearrange | What's the opposite? Flip the order, roles, cause and effect, inside out. What if the last step came first? | Invert hidden assumptions and defaults |

The letters overlap (Eliminate vs Minify, Substitute vs Adapt, Reverse vs Rearrange). That is fine. They are prompts, not categories, so never spend effort deciding which letter an idea "belongs" to.

## Choose the mode

Read what the user actually wants and pick one mode. Don't run a full ceremony when they wanted three quick angles.

- **Full session** ("SCAMPER this", "brainstorm ideas for our launch"). Run all seven letters with the full workflow below.
- **Focused lens**. The user names one or more letters ("what can we eliminate from this onboarding?", "do the R on this plot"). Read `references/letters/<letter>.md` and go deep: more attributes, more ideas, more distant analogies, then select.
- **Quick pass** ("give me some fresh angles on this headline"). Give one to three strong ideas per letter, skip the scoring table, and finish with your top pick and why.
- **Apply and produce**. The user wants the changed artifact itself (rewrite this paragraph, rework this section, new campaign concepts ready to brief). Run SCAMPER briefly as your thinking scaffold, then **actually produce** two to four finished variants. Label each with the operator(s) behind it and recommend one. Show the original next to the variants when that helps comparison.
- **Facilitate** (the user will run SCAMPER with a team). Read `references/facilitation.md` and produce an agenda, timing, prompt cards per letter, and the selection method.

If it's unclear, default to a compact full session and offer to go deeper on any letter.

## Workflow (full session)

### 1. Frame the subject

Pin down:
- one concrete existing thing;
- the goal;
- the audience;
- the constraints, such as budget, brand, channel, deadline, word count.

Turn this into a one-line "How might we…?" and a success criterion.

If the user gave enough context, don't interrogate them. State your assumptions in a line and go. Ask only when the subject is genuinely ambiguous, because a vague subject produces vague ideas.

If there is no existing thing (a blue-sky request), apply SCAMPER to the nearest reference point and say so. That could be the category norm, a competitor's version, last year's version, or the default way it's usually done. If the request is really a different kind of problem, see "When SCAMPER is the wrong tool" below.

### 2. Break the subject into attributes

This is the single biggest quality lever. Letters applied to "the campaign" as a whole give generic answers like "try a new format". Letters applied to "the campaign's *spokesperson*" or "its *call to action*" give specific ones.

Pick 4–7 attributes that actually carry the subject. `references/domains.md` has ready attribute lists for content and marketing, writing, visual and UI design, and product, business and process work.

### 3. Diverge: run the letters

- **Apply each letter where it bites.** For each letter, work through the attributes where it does. You don't need to fill every cell of the letter × attribute grid. The point of the grid is to stop you thinking only at the whole-subject level.
- **Go deeper when the questions run dry.** Use the cheat-sheet questions. If they stop producing ideas, or you're in focused-lens mode, read the letter's file in `references/letters/`. Each one has 10–15 trigger questions plus prompts specific to each domain.
- **Push past the first answer.** Michalko's rule is to ask "How else? What else?" again. The first idea for a letter is usually the one everyone would have.
- **Include at least one bold idea per letter** and label it **(bold)**. It should be deliberately far out or uncomfortable. Bold ideas are often unusable as they stand, but they are where the original ones come from, and they can be scaled back during selection.
- **Give Eliminate and Reverse real effort.** People are biased toward adding things, so the subtractive and inverting letters tend to produce the most distinctive ideas.
- **Cover all three of M** (modify, magnify, minify), not only "modify".
- **For Adapt, reach to distant fields** (other industries, nature, history, games, sport, the military), not just close competitors. Borrowing from competitors gives me-too ideas.
- **Write each idea as a concrete, specific sentence** someone could picture or act on. "Serialize chapter one as a 7-day email course with a cliffhanger each morning" is good; "Experiment with new formats" is not.
- **Don't judge ideas while generating.** Criticism during divergence kills the bold ones. Save it for step 4.

### 4. Converge

Read `references/evaluation.md` for the tools. The default:
1. Shortlist about 6–10 ideas.
2. Score them on **New / Useful / Feasible** (1–5 each, the NUF test), or place them on impact versus effort.
3. **Look for combinations.** The best final idea is often a merger of two from different letters, for example a Substitute with an Eliminate.
4. Pick the top 3–5. Include at least one safe "now" idea and one bold bet, scaled back into something that can be tested.

### 5. Turn the picks into next steps

For each pick, give:
- a one-line concept;
- the operator(s) it came from;
- its **riskiest assumption**;
- the **cheapest way to test** that assumption: an A/B headline, a mock-up, a landing-page test, one pilot issue, a draft scene, a two-week process pilot.

Add an owner or a date if the user is working with a team.

## Output format (full session)

```markdown
## SCAMPER: <subject>
**Goal:** … · **Audience:** … · **Constraints:** …
**How might we** …?
**Attributes examined:** A, B, C, D, E

### S — Substitute
- **[Attribute]** Concrete idea, with a short note on why it might work if it isn't obvious.
- **[Attribute]** …
- **[Attribute] (bold)** …

### C — Combine
… (same for A, M, P, E, R. Under M, mark which ideas are Modify, Magnify or Minify.)

### Shortlist
| Idea | From | New | Useful | Feasible | Note |
|---|---|---|---|---|---|

### Recommended
1. **<Concept>** (S + E). Riskiest assumption: … · Cheapest test: …
2. …
```

Volume guide: about 3–6 ideas per letter for a full session (20–40 total), and 1–3 for a quick pass. If the user names a number, use their number. Keep the output scannable: short bullets, no padding, and no lecture about what SCAMPER is unless they asked.

When the subject is content, writing or design, end by offering to produce the chosen variant (draft the copy, write the scene, sketch the layout as HTML or a description), or just produce it if they asked for output rather than ideas.

## Accuracy when citing real-world examples

Users may put SCAMPER examples into client decks or articles. Use the verified examples listed in the letter files. Avoid these widely repeated myths:

- Columbus "proving the Earth was round".
- AWS starting from Amazon's "excess capacity". Amazon's CTO has denied this.
- Ray Kroc inventing fast-food self-service. It was the McDonald brothers' 1948 Speedee system.
- George Washington Carver's "300 peanut uses" as commercial products.
- The Gutenberg press as simply "wine press + coin punch".

Never make up statistics for illustrative stories.

## When SCAMPER is the wrong tool

Say so briefly, then offer the better tool or a combination. Don't refuse.

- **The problem itself is unclear.** Define it first (jobs-to-be-done, 5 Whys, a journey map), then run SCAMPER on the painful steps.
- **A hard technical trade-off** ("stronger but lighter", "faster but safer"). TRIZ is purpose-built for these.
- **A huge space of combinations** (many parameters, many options each). Use a morphological box. SCAMPER can generate the options in each column.
- **The team needs to decide, not generate.** Use Six Thinking Hats, Plus/Minus/Interesting (PMI), or a weighted decision matrix.
- **A blue-sky invention** with no anchor. Start with open brainwriting or random-stimulus techniques, then use SCAMPER to develop the ideas you get.

## Reference files

Load only what the task needs.

- `references/letters/`: one file per letter.
  - Files: `substitute.md`, `combine.md`, `adapt.md`, `modify-magnify-minify.md`, `put-to-other-uses.md`, `eliminate.md`, `reverse-rearrange.md`.
  - Each has the definition, the deep list of trigger questions, prompts for content/marketing, writing, design and business, pitfalls, and verified examples.
  - Read the file for any letter you're going deep on.
- `references/domains.md`: attribute checklists and setup tips for content and marketing, writing (fiction, non-fiction, copy), visual/UI/graphic design, and product, business and process work.
- `references/evaluation.md`: selection tools (NUF, impact/effort, the How-Now-Wow box, PMI, dot voting, weighted matrix), hybridizing ideas, and next-step templates.
- `references/facilitation.md`: running SCAMPER with a group (silent brainwriting first, timing, agenda), combining it with other methods, the evidence and its limits, history and variants.
