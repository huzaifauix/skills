---
name: content-write
description: >-
  Write social posts that sound like a real person, not AI. Takes a proven
  post the user brings (an outlier or an example they like), repurposes its
  angle and structure for the user's audience, writes the post in the saved
  voice, then runs a four-pass polish: AI-slop scan, reader pass, truth check
  and scan pass. Reads and writes the shared content-strategy/ folder used by
  content-diy. Use this whenever someone asks to write, draft or repurpose a
  LinkedIn post (or X, Instagram, newsletter post), turn a viral or outlier
  post into their own, write this week's posts, or edit, polish or "de-AI" a
  post: "this sounds like ChatGPT", "clean the AI
  slop", "check this post", "make it less generic". Use it even when they
  don't name a format or method. For content strategy, pillars or post ideas,
  use content-diy instead.
---

# Content write

Most AI-written posts fail the same way: they sound clever and say little. This skill writes posts that carry real information in plain words, starting from posts already proven to work.

**The core idea:** start from a proven post the user brings (an outlier that did far better than its creator's usual, or an example they like), take its angle, topic, structure and ending as the guide, and write a full post for the user's case in their own words. Never copy its words or its length.

## Project files

State lives in `content-strategy/` at the project root, shared with the `content-diy` skill:

| File | Used for | Owner |
|---|---|---|
| `profile.md` | Audience, voice, proof (real stories and results), preferences, cadence | content-diy |
| `map.md` | Category, pillars, topics, custom formats | content-diy |
| `ideas.md` | Idea log with IDs and statuses | shared |
| `drafts/` | One file per finished post | shared |

Read `references/project-files.md` before writing any of these files. It has the templates and update rules.

## Step 0: Load

Read `profile.md`, `map.md` and `ideas.md` if they exist, plus any proof or story file the project has (such as `stories.md`).

- **Found:** confirm in one line which brand and platform you're writing for, then carry on.
- **Not found, one-off post** ("write me a post about X"): ask in one message only for what you can't infer: who it's for, the platform, and any real story or result to use. Then write it. Mention once that `content-diy` can set up a saved profile so later posts need no questions.

## Pick the mode

Read the request:

- **Write mode:** a new post, from a post the user brings, an idea in `ideas.md`, or a topic. Run steps 1–5.
- **Polish mode:** the user gives an existing post to check, clean, edit or "de-AI". Their facts are the material; run steps 3 and 4 on their text.
  - "Find", "check" or "what's wrong": report the problems line by line, slop and writing rules both (a buried message, a weak hook), and stop.
  - "Clean", "fix" or "rewrite": report the problems, then rebuild the post. Removing slop is half the job: a post with the slop cut out and nothing put back reads flat. Find the strongest true material in it (usually a real moment or a hard number), lead with that, and make sure the core message lands in the first 3 lines. If they want to compare, keep the original and save the new version beside it.

## Step 1: Read the starting post

The user brings the starting post: an outlier they found, or an example they like the shape of. Read `references/starting-post.md` for what to take from it (angle, topic, structure, ending, visual) and what a good Proof example has.

If the user brings no post, write from their idea or topic, or from the idea in `ideas.md` they name, using its pillar, topic and format. Mention once that a proven post to start from usually makes a stronger one. Don't go looking for posts yourself.

When the user wants several posts (a week's worth), follow the mix in `profile.md` (for example 4 Teach, 2 Story, 1 Proof).

## Step 2: Match it to the map

Give every post, Proof posts included, a pillar, topic and format from `map.md` (formats are those in content-diy's `references/formats.md`, plus any custom ones in `map.md`). The starting post gives the angle and structure; the map makes sure the post belongs to this brand. If nothing in the map fits, say so, and suggest the closest topic or a new one, rather than forcing it.

Then write the post's **core message in one sentence** before drafting. If you can't, the post isn't ready.

**Let the real moments decide the length.** Before writing, count the beats you have: moments, steps, examples, facts. One point and one action makes a short post; several moments or a process makes a long one. Use every real beat and add none. The rules below cut hard, so without this count every post drifts short; a story with six real beats squeezed into five lines loses the reader as surely as padding does. The rough word counts in `references/writing-rules.md` are a guide, never a target.

## Step 3: Write

Read `references/writing-rules.md` and write the full post. Its main points:

- Hook on line 1, rehook on line 2 that opens a loop the post closes later.
- Plain words a stranger outside the user's field could follow. No jargon, including the user's own trade terms.
- Easy to scan, always: one idea per line, short lines, paragraphs of 1–2 lines with white space between. Then choose devices to fit the content (bullets, numbers, a timeline, label: value, → for cause and effect) and order each list by line length (long to short, short to long, square, or arrow >). Read `references/formatting.md`.
- Length follows the story. Every line adds something new.
- End on a real last line: an action, a point or the call to action.

**Truth comes first.** Any story, result, number, client or quote about the user must come from `profile.md`, a project proof file or the conversation. If it isn't there, write a bracketed placeholder (`[your result]`) and list it at the top of the draft. A post is published as fact under the user's name; an invented result can cost them a client's trust.

## Step 4: Polish in four passes

Read `references/anti-slop.md` and `references/formatting.md`, then check the post four times. Each pass catches what the others miss.

1. **Slop scan:** check every line against the banned patterns. Rewrite each hit, or turn it into a list. Never just delete it: deleting is what makes a cleaned post go flat.
2. **Reader pass:** read it top to bottom as the audience would. Does a stranger get the message from the first 3 lines? Is there a real moment or stake that makes them care, not just information? Would a stranger outside the user's field know every word, with trade terms like "cash crunch" or "P&L" said plainly? Does it flow? Does it feel finished, with no post stopping on a bare list? Is each line one simple idea, especially the last one?
3. **Truth check:** every claim about the user is backed by the files or the conversation. A line that sounds good but isn't quite true gets rewritten. Take the facts from the files, not their wording.
4. **Scan pass:** run `scripts/scan.py` on the post. Split every line it flags as too long or holding two sentences, and every paragraph over 2 lines, unless splitting would break the meaning. Check each list has a shape that fits what it does, and that the devices fit the content. A post that passes the other three checks but reads as a wall still fails here.

When writing several posts, also read them side by side: no trick (the same list shape, the same opening move, the same kind of ending, the same layout) appears twice in one batch, and the lengths are mixed rather than all short or all medium.

## Step 5: Save and show

1. Save each post to `content-strategy/drafts/<ID>-<short-slug>.md` using the layout in `references/project-files.md`.
2. Update `ideas.md`: set the idea's status to `drafted`, or add a new row (next ID, status `drafted`) if the post didn't come from a saved idea.
3. Show the post in the chat as it would be published, then one line each for the post it started from, its pillar / topic / format, and any placeholders left to fill.

If there's no `content-strategy/` folder and the user only wanted a one-off, show the post and don't create files.

## Reference files

- `references/starting-post.md`: what to take from the post the user brings, and what a good Proof example has. Read for step 1.
- `references/writing-rules.md`: hook, rehook, lists, endings, voice, and the shape of each content type. Read for step 3.
- `references/anti-slop.md`: the banned patterns with before → after fixes, and the reader pass and truth check. Read for step 4, and for every polish-mode request.
- `references/formatting.md`: what every post does to stay easy to scan, the devices that fit each kind of content, and the list shapes. Read for steps 3 and 4.
- `scripts/scan.py`: measures a post's line lengths, sentences per line and paragraph sizes, and names each list's shape. Run in the scan pass.
- `references/project-files.md`: the draft file layout, and how this skill updates `ideas.md`. Read before writing any project file.
