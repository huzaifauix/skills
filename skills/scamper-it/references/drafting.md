# Rendering drafts

The variations have to be *seen*, not described. A reader judges a headline by reading it and a layout by looking at it. A bullet that says "try a bolder hierarchy" can't be judged at all. Pick the format below that matches the subject's medium. If a request mixes media (a post plus its caption), render each part in its own format, inside the same variation.

## Contents
- Copy and writing
- Visual design: canvas
- Visual design: HTML fallback
- Concept cards (campaigns, ideas, products)
- Before → after (processes)
- Fidelity levels
- The final check

---

## Format drafts (reformat preset)

When the three drafts are three formats of the same message, draft each one in its own structure, as finished copy:

```markdown
**A · LinkedIn carousel (8 slides)**
1. Hook: …  2. … 8. Save-worthy summary + CTA
**B · X thread (6 posts)**
1/ … (must stand alone) … 6/ CTA
**C · 45-second video script**
0–2s hook (on-screen: …) · 2–15s … · close + CTA
```

For visual formats on a canvas, render the cover and two key slides, not every slide.

## Copy and writing

Show the original once, then each variation as **finished text**, ready to paste, at the length the slot needs.

```markdown
**Original** (podcast episode description)
> In this episode we chat with our guest about productivity tips and tools…

**A · Specific and clean** (S + E)
> [Guest] stopped using to-do lists. In this episode: what replaced them, and the one habit that stuck.
*Why:* swaps "productivity tips" for one concrete story and cuts the filler.

**B · Open on the quote** (C + R) ← recommended
> "I deleted my to-do app and got more done." [Guest] on the [20-minute] rule that…
*Why:* the guest's voice does the selling in the first line.

**C · The bold one** (R + Minify)
> Don't listen to this if you love your to-do list.
*Why:* a reversal hook in eight words. Use it only if the brand's tone allows it.
```

- **Short pieces** (headlines, subject lines, CTAs, captions): give 3 variations per slot. A compact table works well (Slot | A | B | C).
- **Long pieces** (an article intro, a scene): draft the changed section only and mark where it joins the original.
- **Placeholders:** put every invented specific in [brackets] (names, numbers, ages, durations, quotes, plot facts) and say so once. An unbracketed invented detail reads as fact.
- **Dates:** a placeholder date has to agree with the user's timeline, worked out from today's date ("next month" means next month). Otherwise use [DATE].

## Visual design: canvas

Use this when a design canvas or artifact tool is available, such as a Design artifact type in Claude.

- **One canvas, one artboard per variation**, named `A-<short-name>.dc.html`, `B-…`, `C-…`. Lay them out in a row, 80 px apart. Give each artboard a frame title like "A · Close (S + E)" so the letters show on the canvas.
- **The reference.** Describe the source in one line of your reply. Don't embed a third-party source image in the drafts. It carries the original creator's name and branding into a file the user may share, and the drafts must stand on their own.
- **The same frame size as the source.** If there is no source, use the platform's standard size (see `domains.md`).
- **The same structure across A/B/C** unless the variation *is* a layout move. That way the differences are easy to see.
- **Build order:** A, then B, then C. Publish after each artboard, so the user sees progress.
- **Your reply** holds the map, a one-line note per artboard, and the close. Rationale never goes inside an artboard.

## Visual design: HTML fallback

Use this when there is no canvas tool (Cursor, Codex, plain CLI agents).

- **Write one self-contained file,** `scamper-variations.html`, in the working directory, or wherever the user keeps drafts.
- **Its layout:**
  - a header row with the subject and the map;
  - a **comparison strip:** one column per variation (`grid-template-columns: repeat(3, minmax(0, 1fr))`, stacking under 900 px), each with a label bar ("B · Balanced · C + A + R") above a scaled thumbnail at the real aspect ratio;
  - below it, **each variation at full size** (or at least 60% scale), one after another, with the same label. The strip is too small to read text in, so the full-size versions are what the user actually reviews.
- **Don't embed the source image.** Describe it in the header instead (see the canvas rules above).
- **If you can render the file** (a headless browser), check for text overflow and overlapping elements (badges over titles, clipped headlines) before handing it over.
- **Tech rules:**
  - inline CSS only;
  - fonts from Google Fonts or system fonts;
  - no external images unless the user supplied them (use labelled grey placeholder boxes instead);
  - text contrast of at least 4.5:1.
- **Tell the user the file path** and how to open it.
- **If the user wants an image export,** offer to build the chosen variation at full size as its own file.

## Concept cards (campaigns, ideas, products)

```markdown
### B · "Stamp Swap" (C + R)
**Hook:** Regulars give their 10th coffee to a friend instead of collecting it.
**Sample:** Card line: "Your 10th coffee is on you. Give it to someone."
**Visual:** Two-part stamp card with a tear-off "gift" half in the café's colours
**First step:** Print 200 swap cards and run it for one month at one location
```

Keep it to four lines per card. If a card needs more, the idea isn't concrete enough yet.

## Screens and flows (UI)

When the subject is a screen or a user flow (a checkout, onboarding, sign-up, app screen), show the before → after flow **and** render the key screen of each draft as a phone-sized mockup (390 wide), on the canvas or in the HTML file. Mark removed elements and moved steps visibly. A flow described only in text can't be judged by eye.

## Video, Reel and Story frames

Every rendered frame carries its real on-screen text and layout: the hook line, captions, stickers and the CTA. Don't leave large empty boxes or grey "footage" placeholders. If footage is unknown, show a simple described shot ("[close-up: hands closing a book]") inside a small labelled area, and give the frame's text the space.

## Before → after (processes)

```markdown
**Before:** Offer signed → IT ticket → Laptop shipped → Day 1 orientation → Week 2 first project
**B · Ready before day one** (E + R)
**After:** Offer signed → Laptop and accounts ready before day 1 → Day 1 small first project → Orientation videos during week 1
Removed: IT ticket · Moved: first project → day 1, orientation → async · Added: pre-start setup
```

## Fidelity levels

| Level | Use for | What it includes |
|---|---|---|
| **Low** | Quick comparison of directions | Real headline and key copy, the layout blocks, rough colours; secondary copy may be placeholder lines |
| **Medium** (default for A/B/C) | Choosing a direction | All real copy fitted to its slots, real layout and colours, simple icons; no fine detail |
| **Final** (after the pick) | The deliverable | Everything polished: spacing, contrast checks, exact sizes, export-ready |

Three medium drafts beat one final draft plus two descriptions. At this stage the user is choosing a direction, not proofreading.

## The final check

Run this after the user picks, before you call the piece final:

- [ ] **Fit:** every text inside its slot or limit; nothing clipped.
- [ ] **Overlaps:** no badge, label or arrow over text. Render it to check if you can (a headless browser, or a canvas screenshot when the tool allows verifying).
- [ ] **Contrast and size:** text at least 4.5:1, nothing under 12 px at the published size.
- [ ] **Placeholders:** all invented facts bracketed; dates consistent with the user's timeline.
- [ ] **Source traces:** no creator name, handle, logo or watermark from any reference.
- [ ] **Originality:** mixes 2+ sources; not too close to any single reference.

Then say which of these you actually verified. If the environment told you not to verify (some design canvases do), write "Not visually checked; ask me to render and fix" instead of claiming it is clean.
