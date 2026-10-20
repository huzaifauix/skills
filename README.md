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
Run the SCAMPER creative-thinking method (Substitute, Combine, Adapt, Modify/Magnify/Minify, Put to other uses, Eliminate, Reverse/Rearrange) and **see the results as drafts**, not just idea lists. Every run works in three stages:

1. **Assess and map:** reads the intent first (the real goal, what to **keep vs change**, light or standard effort), asks only if something critical is missing, then maps the parts SCAMPER may touch, with their limits.
2. **Drafts:** three variations (Close / Balanced / Bold) in the subject's own medium: rewritten copy, design artboards (or one side-by-side HTML file), screen mockups, concept cards, or before → after flows.
3. **Close:** a "What changed" table, a recommendation, the riskiest assumption, the cheapest test, and what was actually checked.

Repurpose requests are read from the wording: **template reuse** (keep the layout, new topic), **reformat** (keep the message, one new format, with other formats offered only after you've settled), or **from a reference** (keep the idea, new layouts). Quick asks get a short text pass.

**Use when:** Brainstorming fresh angles, repurposing or reformatting content, designing something "like this reference", or asking "what could we eliminate / reverse here?"

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
