# j3

A portable Claude Code methodology kit. Copy the `.claude/` directory into any project to give Claude a structured, disciplined development process: spec → features → tasks → code → tests.

j3 enforces the rule that no code is written without a task, no task without a feature, and no feature without a spec. It also bundles opinionated coding standards, a literate-programming workflow, and slash commands for common operations.

## Why

Claude Code is powerful but undisciplined by default. j3 gives it a repeatable process:

- Every piece of work is traceable from spec → feature → task → code
- Features are never closed without passing tests
- Bugs get regression tests automatically
- Projects are scaffolded consistently and open-source-ready from day one

## Requirements

- [Claude Code](https://claude.ai/code) CLI

## Quickstart

```bash
# 1. Clone this repo
git clone https://github.com/pitosalas/j3.git

# 2. Copy .claude/ into your new (empty) project directory
cp -r j3/.claude/ myproject/.claude/

# 3. Open your project in Claude Code and say:
#    "bootstrap this project"
```

Claude will scaffold the full folder structure, generate starter files, and prompt you to fill in the spec before any features or code are defined.

## What's inside `.claude/`

| File | Purpose |
|---|---|
| `CLAUDE.md` | Entry point — routes Claude to the right instructions on every session start |
| `bootstrap.md` | Scaffold instructions: creates numbered folder structure, templates, LICENSE, README, .gitignore |
| `process.md` | Workflow rules: spec → feature → task → code → test discipline |
| `coding.md` | Python coding standards (style, structure, quality) |
| `literate.md` | Prompt for generating literate-program Markdown walkthroughs |
| `commands/newsesh.md` | `/newsesh` slash command — orients Claude at the start of a session |
| `commands/checkpoint.md` | `/checkpoint` slash command — runs tests, generates docs, commits, pushes |
| `templates/` | Starter files: LICENSE, README, .gitignore, CLAUDE.md, feature, task, issue templates |

## Project structure created by bootstrap

```
CLAUDE.md                  ← project entry point for Claude
LICENSE
README.md
.gitignore
01-literate/               ← generated literate-program docs
02-doc/
  spec.md                  ← describe what your app does here
  current.md               ← session handoff and current status
  notes.md                 ← architecture decisions, research, gotchas
03-features/
  notdone/                 ← features not yet implemented
  done/                    ← completed features
  deferred/                ← features parked for later
  template.md
04-tasks/
  notdone/                 ← tasks not yet done
  done/                    ← completed tasks
  deferred/
  template.md
05-issues/                 ← bugs and issues not yet converted to features
  template.md
```

## The workflow

1. Write a spec in `02-doc/spec.md`
2. Ask Claude to define a feature — it creates a file in `03-features/notdone/`
3. Ask Claude to break the feature into tasks — it creates a task file in `04-tasks/notdone/`
4. Claude writes code only after tasks are defined
5. Every feature requires a testing task; feature is only closed when tests pass
6. Bugs get a regression test before being marked fixed

## Slash commands

| Command | What it does |
|---|---|
| `/newsesh` | Reorients Claude: reads current status and process rules |
| `/checkpoint` | Runs tests, regenerates literate docs, commits, pushes |

## License

MIT — see [LICENSE](LICENSE)
