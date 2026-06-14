# j3

Portable Claude Code methodology kit. Drop `.claude/` into any project and Claude gets a structured, disciplined development process: spec → features → tasks → code → tests.

**Core rule:** no code without a task, no task without a feature, no feature without a spec.

## Requirements

- [Claude Code](https://claude.ai/code) CLI

## Quickstart

```bash
git clone https://github.com/pitosalas/j3.git
cp -r j3/.claude/ myproject/.claude/
```

Open your project in Claude Code and say: **"bootstrap this project"**

Claude scaffolds the folder structure, generates starter files, and blocks you from writing code until a spec and feature exist.

## What's in `.claude/`

| File | Purpose |
|---|---|
| `bootstrap.md` | Scaffold instructions — run once on a new project |
| `how_to_be.md` | Working principles Claude follows every session (auto-loaded via `@`) |
| `process.md` | Workflow rules: spec → feature → task → code → test |
| `codereview.md` | Python coding standards, style rules, review checklist (v3.1) |
| `literate.md` | Generates literate-program Markdown walkthroughs of source files |
| `commands/start.md` | `/start` — orients Claude at session start |
| `commands/checkpoint.md` | `/checkpoint` — runs tests, updates docs, commits, pushes |
| `templates/` | Starter files: LICENSE, README, .gitignore, feature/task/issue templates |

## Project structure created by bootstrap

```
CLAUDE.md                  ← auto-loads how_to_be, process, codereview every session
LICENSE
README.md
.gitignore
01-literate/               ← generated literate-program docs
02-doc/
  spec.md                  ← describe what your app does here
  current.md               ← session handoff: what's in progress
  notes.md                 ← architecture decisions, research, gotchas
03-features/
  notdone/                 ← FNN-slug.md mini-specs
  done/
  deferred/
04-tasks/
  notdone/                 ← TFNN-slug.md task files (NN matches feature)
  done/
  deferred/
05-issues/                 ← bugs not yet converted to features
```

## Workflow

1. Fill `02-doc/spec.md` — describe the app
2. Create feature file `03-features/notdone/F01-slug.md`
3. Create task file `04-tasks/notdone/TF01-slug.md` (NN matches feature)
4. Write code, write tests task by task
5. `/checkpoint` — review, commit, push
6. When all tasks done → move task file to `done/`, move feature file to `done/`

## Naming conventions

- Features: `FNN-slug.md` (e.g. `F01-add-auth.md`)
- Tasks: `TFNN-slug.md` where `NN` matches the feature (e.g. `TF01-add-auth.md`)

## Slash commands

| Command | What it does |
|---|---|
| `/start` | Reads current status, open features, open tasks — orients Claude at session start |
| `/checkpoint` | Runs tests, regenerates literate docs, commits, pushes |

## Propagating updates to child projects

Projects that copy `.claude/` from j3 will drift over time. When j3 changes, sync key files:

```bash
cp j3/.claude/codereview.md myproject/.claude/codereview.md
cp j3/.claude/process.md myproject/.claude/process.md
cp j3/.claude/how_to_be.md myproject/.claude/how_to_be.md
cp j3/.claude/templates/feature-template.md myproject/.claude/templates/feature-template.md
cp j3/.claude/templates/task_template.md myproject/.claude/templates/task_template.md
```

## License

MIT — see [LICENSE](LICENSE)
