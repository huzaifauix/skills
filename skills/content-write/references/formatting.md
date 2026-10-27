# Formatting

A post is read on a phone, by someone scrolling. If it looks like a wall, it's skipped before the first line is read. Formatting has two layers: what every post does, and what is chosen to fit what the post says.

## Always: every post

- **One idea per line.** If a line has "and" joining two thoughts, it's usually two lines.
- **Short lines.** Aim for under about 80 characters, which is 2 rows on a phone. A line longer than that is a paragraph pretending to be a line.
- **Paragraphs of 1–2 short lines**, with a blank line between paragraphs.
- **The key line stands alone.** The line that turns the post (the result, the lesson, the moment it went wrong) gets its own paragraph.
- **The hook and rehook are each one line**, so both land before "…see more".

Split a long line at its natural break, and keep both halves:

> By April the café had closed, and every number that could have stopped me was sitting in my receipts box.

becomes

> By April, the café had closed.
>
> Every number that could have stopped me was in my receipts box.

## Fit to the writing

Choose a device only when the content has that shape. Forcing a list onto a story, or a story onto a list, makes the post harder to read, not easier.

| Content | Device | Example |
|---|---|---|
| Items in any order | **Bullets** | What came back: / - Design: clean / - Colours: wrong |
| Steps in order | **Numbers** | 1. List who has to say yes / 2. … |
| Facts side by side | **Label: value** | Food cost: under 30% |
| Change over time | **Timeline** | Week 1: chasing names. / Week 2: chasing meals. |
| A cause and its effect | **→ arrow** | Names asked at booking → no chasing in week 4 |
| A sequence of moments in a story | **Short dated lines** | February: the supplier stopped delivering. / March: I borrowed £6,000. |
| One sharp point | **A line on its own** | It closed after a cash crunch. |

Label: value is for real facts only. A label used for rhythm ("Memory: asleep") is slop (`anti-slop.md`).

## List shapes

When a post has a list, order its lines by length, so the right edge makes a shape. The shape guides the eye and makes the list feel designed, not dumped. Pick the shape by what the list should do:

**Long to short:** builds to a punch. The last, shortest item lands hardest.

```
- Tables booked and paid online in one step
- Guests added by whoever booked
- Reports in one click
```

**Short to long:** opens up. Ends on the item with the most detail.

```
- Names
- Dietary needs
- Final numbers for the venue, a week early
```

**Square:** every line about the same length. Equal weight, for steps or options of the same kind.

```
- Ask for names at booking
- Let bookers add guests
- Keep one list for all
```

**Arrow (>):** lines grow toward the middle, then shrink, so the edge points right. For a longer list (5 or more items) that needs rhythm.

```
- Coffee
- Emails in the inbox
- Versions of the guest list spreadsheet
- Venue asking for numbers
- Sleep
```

If the items have a fixed order (steps, a timeline), keep their order and let the shape go: the order is information. Reword items to fit a shape only when the meaning stays the same.

## Vary it

Posts that all use the same device look templated, even when each one is fine alone. Across a week's posts, mix the devices and the list shapes: one post with numbered steps, another with a timeline, another with no list at all.

## Check it

Run `scripts/scan.py` on the post text (a file, or `-` for stdin). It prints each line's length and flags lines over 80 characters and paragraphs over 2 lines, and names the shape of each list. It measures; you judge. A flagged line in a quote or a list item that can't split may be fine.
