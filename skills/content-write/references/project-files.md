# Project files

This skill shares `content-strategy/` with content-diy. content-diy owns `profile.md` and `map.md` and their templates (its `references/project-files.md`); this skill only reads them, except to add a standing writing instruction to **Preferences** in `profile.md` when the user gives one ("never use emoji", "always British English").

General rules, same as content-diy:

- **Edit in place.** Change the line or row; leave the rest. The user's hand edits win.
- **Dates are absolute** (`2026-10-27`).
- **Real versus assumed.** Anything inferred and not confirmed is marked `(assumed)`.

## ideas.md

Same table and rules as content-diy (IDs `I-001`…, never reused; statuses `idea`, `picked`, `scheduled`, `drafted`, `posted`, `dropped`). This skill:

- sets an idea's status to `drafted` when its post is saved;
- adds a new row with the next ID and status `drafted` when a post didn't come from a saved idea. Its Title is the post's working title and its Hook is the post's first line.

If `ideas.md` doesn't exist yet, create it with content-diy's header row.

## drafts/

One file per post: `content-strategy/drafts/<ID>-<short-slug>.md`, the same layout content-diy uses, plus the source and visual lines.

```markdown
# <Working title>
**ID:** I-012 · **Platform:** LinkedIn · **Pillar:** … · **Topic:** … · **Format:** …
**From:** <the post the user brought: creator, "first words of the post" (likes, if given), or "example: …", or "user's idea">
**Visual:** <the one visual for this post>
**Fill in before posting:** [placeholder 1], [placeholder 2]

---

<post text exactly as it will be published>
```

Leave out **Fill in before posting** when there are no placeholders. When the user asks for a before/after comparison, keep the original file and save the new version beside it (for example `I-012-free-tools-clean.md`), rather than overwriting.
