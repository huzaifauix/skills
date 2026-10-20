# Agent Skills Collection

A collection of agent skills for Cursor AI agents, installable via the open `skills` CLI.

## What are Agent Skills?

Agent Skills are reusable instructions that enhance AI agents with specialized capabilities. Each skill provides structured guidance for completing specific tasks, from brand naming to code generation.

## Installation

### Install all skills

```bash
npx skills add huzaifauix/skills
```

### Install a specific skill

```bash
npx skills add huzaifauix/skills --skill brand-name-finder
```

## Available Skills

### `brand-name-finder`
Find available brand names with registered .com domains. Generates creative name combinations, checks domain availability via RDAP, and provides a shortlist of available names. Perfect for naming brands, channels, products, or sites where domain availability is critical.

**Use when:** Naming a brand, product, or service and the .com domain must be available.

### `scamper-it`
Run the SCAMPER creative-thinking method (Substitute, Combine, Adapt, Modify/Magnify/Minify, Put to other uses, Eliminate, Reverse/Rearrange) on content, writing, design, products, and processes, and **see the results as drafts**, not just idea lists. Every run works in three stages:

1. **Map:** split the request into areas (e.g. layout vs content), with their parts, limits, and the letters that apply.
2. **Drafts:** produce three variations (Close / Balanced / Bold), shown in the subject's own medium: rewritten copy, design artboards (or one side-by-side HTML file when there's no canvas), concept cards, or before → after flows.
3. **Close:** a "What changed" table, a recommendation, the riskiest assumption, and the cheapest test.

Modes: full session, **repurpose a template** (keep an infographic or post's layout and swap in a new topic, with a slot-by-slot fit check), focused lens on one letter, quick pass, and team workshop. Reference files hold trigger questions for each letter, size and length limits by domain, drafting formats, and fact-checked examples.

**Use when:** Brainstorming fresh angles, repurposing a template for a new topic, remixing something that already exists, or asking "what could we eliminate / reverse here?"

### `content-diy`
Build a content strategy with Nick Broekema's DIY Content Strategy framework: category → pillars → topics → post formats, where pillar + topic + format = one post. Runs a short onboarding, proposes audience-first pillars and topics, then picks the strongest topic × format pairings from 18 formats in four families (Teach, Story, Opinion, Proof) as post ideas with titles and hooks. Saves the profile, content map and an idea log in `content-strategy/` in your project, so later runs skip onboarding and never repeat ideas. Can also plan a content calendar, draft full posts per platform, and export ideas to CSV.

**Use when:** Asking "what should I post?", building content pillars or a posting plan, or coming back for more ideas or drafts.

## Manual Installation

You can also manually copy any `SKILL.md` file from the `skills/` directory into your Cursor skills folder:

```bash
# macOS/Linux
~/.cursor/skills/

# Windows
%USERPROFILE%\.cursor\skills\
```

## Contributing

Skills are organized in the `skills/` directory with the following structure:

```
skills/
  skill-name/
    SKILL.md
```

Each `SKILL.md` must include YAML frontmatter with `name` and `description` fields.

## About the Skills CLI

This repository is compatible with the [Vercel Labs Skills CLI](https://github.com/vercel-labs/skills), which provides an easy way to discover, install, and manage agent skills.
