# Roadmap

Parked ideas for the skills in this repo. Tick an item when it ships and note the commit.

## Content system

A set of small skills that share the `content-strategy/` folder, rather than one big skill or a separate tool. Each idea in `ideas.md` carries a status that the skills move along: `idea → drafted → edited → designed → scheduled → posted → measured`.

**Flow:** brand foundation → idea bank + story bank → strategy → writing → editing → design → repurposing/formatting → scheduling → engagement → performance tracking, which feeds back into strategy.

**Setup:** one project folder per brand, opened in Claude Code, holds `content-strategy/`. Skills are installed once and triggered by plain requests. A weekly `content-week` run chains the stages, so a normal week is about 1–1.5 hours of reviewing instead of creating from scratch.

**Build order:** shared file contract, writing, design, `content-week` and the Monday schedule, performance tracking.

- [x] **Strategy and ideas.** `content-diy`.
- [ ] **Shared file contract.** Document the files in `content-strategy/` and the idea statuses, so every content skill reads and writes the same state.
- [ ] **`content-week` skill.** One command that runs the week: read the inbox → pick this week's ideas → write → edit → design → add to the calendar. Then "approve and schedule" sends approved posts to the scheduler, and "log results" records performance. Calls the other skills, so they never need to be run one by one.
- [ ] **Monday schedule.** A scheduled task runs `content-week` every Monday at 7am, so drafts and designs are ready for review when the week starts.
- [ ] **Brand foundation.** Voice and audience already live in `profile.md`. Add `brand.md` for colours, fonts and layout templates, used by the writing and design skills.
- [ ] **Idea bank.** An inbox (`content-strategy/inbox.md`) for saved posts, audience questions, comments and notes, which `content-diy` turns into ideas. Capture from the phone into an Apple Notes note ("Content inbox"), pulled into `inbox.md` on each weekly run. Includes "Audience language" under content-diy.
- [ ] **Story and proof bank.** Real wins, results and mistakes for Story and Proof posts. See "Story bank" under content-diy.
- [x] **Writing.** `content-write`. New skill. Drafts posts in the saved voice for each platform, starting from `content-diy/references/drafting.md`. Handles "write me a post about X" without a strategy.
- [x] **Editing.** Lives inside `content-write` as its polish mode. A review pass on hook, voice, facts and call to action, with an optional approval step for clients or a team. Could live inside the writing skill.
- [ ] **Design.** New skill. Turns a draft into a carousel or graphic (HTML → PNG, or Figma) using `brand.md`.
- [ ] **Repurposing and formatting.** One step: adapt one piece for several platforms, with platform specs as references. See "Repurposing" under content-diy.
- [ ] **Scheduling and publishing.** Don't build. Keep `calendar.md`, export a CSV for bulk upload, or connect a scheduler's MCP (Buffer, Typefully).
- [ ] **Engagement.** Mostly a habit. At most, drafting replies to comments and DMs.
- [ ] **Performance tracking.** See "Results tracking" under content-diy.

Only if needed: research and SEO (blogs, YouTube), an asset library (photos, logos, templates), video and audio production.

## content-diy

- [ ] **Story bank.** A short interview (client wins, mistakes, why you started, turning points) saved to `content-strategy/stories.md`. Story and Proof ideas and drafts then use real material instead of `[placeholders]`.
- [ ] **Results tracking.** Log how posted ideas performed (reactions, comments, saves, leads) in `ideas.md`, and lean new batches toward the pillars, formats and hook styles that work for this audience.
- [ ] **Repurposing.** Turn one idea or draft into versions for several platforms: LinkedIn post, Instagram carousel, X thread, newsletter section.
- [ ] **Audience language.** Mine pasted comments, DMs, sales-call notes, reviews or FAQs for topics and hooks in the audience's own words.
- [ ] **Goal mode.** Set a goal (awareness, leads, launch on a date) and shift the format-family mix and sequence to match, e.g. more Proof and Objection response before a launch.
- [ ] **Audit past posts.** Classify existing posts into the map's pillars and formats, then show gaps and over-used areas.
- [ ] **Visual strategy map.** Generate an HTML page of the map in the style of the original infographic, for sharing with a team or client.
- [ ] **Hook variants.** Offer 3 alternative hooks per idea in different styles (question, number, bold claim) for picking or A/B testing.

## brand-name-finder

_No parked ideas yet._

## scamper-it

_No parked ideas yet._
