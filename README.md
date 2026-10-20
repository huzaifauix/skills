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
Run the SCAMPER creative-thinking method (Substitute, Combine, Adapt, Modify/Magnify/Minify, Put to other uses, Eliminate, Reverse/Rearrange) on content, writing, design, products, and processes. Breaks the subject into attributes, generates labelled ideas per letter (including bold ones), scores a shortlist on New/Useful/Feasible, and turns the picks into cheap tests. Supports full sessions, single-letter deep dives, quick passes, producing finished variants (e.g. rewritten copy), and planning team workshops. Per-letter reference files hold trigger questions, domain prompts, pitfalls, and fact-checked examples.

**Use when:** Brainstorming fresh angles, remixing or repurposing something that already exists, or asking "what could we eliminate / reverse here?"

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
