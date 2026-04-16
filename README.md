# j3

A portable Claude Code methodology kit. Drop the `.claude/` directory into any project to give Claude a structured, disciplined development process: spec → features → tasks → code → tests.

j3 enforces the rule that no code is written without a task, no task without a feature, and no feature without a spec. It also bundles opinionated coding standards, a literate-programming workflow, and slash commands for common operations.

## Why

Claude Code is powerful but undisciplined by default. j3 gives it a repeatable process:

- Every piece of work is traceable from spec → feature → task → code
- Features are never closed without passing tests
- Bugs get regression tests automatically
- Projects are scaffolded consistently and open-source-ready from day one

## Requirements

- [Claude Code](https://claude.ai/code) CLI
- Python 3.11+ and [uv](https://github.com/astral-sh/uv) (for the target project)

## Quickstart

```bash
# 1. Clone this repo or download the .claude/ directory
git clone https://github.com/pitosalas/j3.git

# 2. Copy .claude/ into your new project
cp -r j3/.claude/ myproject/.claude/

# 3. Open your project in Claude Code and say:
#    "bootstrap this project with j3"
```

Claude will scaffold the `process/` folder structure, generate starter files, and prompt you to fill in the spec.

## What's inside `.claude/`

| File | Purpose |
|---|---|
| `CLAUDE.md` | Entry point — routes Claude to the right instructions on every session start |
| `bootstrap.md` | Scaffold instructions: creates `process/`, templates, LICENSE, README, .gitignore |
| `method.md` | Workflow rules: spec → feature → task → code → test discipline |
| `coding.md` | Python coding standards (style, structure, ROS2 support) |
| `literate.md` | Prompt for generating literate-program Markdown walkthroughs |
| `commands/newsesh.md` | `/newsesh` slash command — orients Claude at the start of a session |
| `commands/checkpoint.md` | `/checkpoint` slash command — runs tests, generates docs, commits, pushes |
| `templates/` | Starter files: LICENSE, README, .gitignore, CLAUDE.md, feature, task templates |

## Project structure created by bootstrap

```
process/
  spec.md               ← describe what your app does here
  features/
    notdone/            ← features not yet implemented
    done/               ← completed features
    deferred/           ← features parked for later
  tasks/
    notdone/            ← tasks not yet done
    done/               ← completed tasks
    deferred/
  bugs/
    found/              ← discovered bugs
    fixed/              ← fixed bugs with regression tests
LICENSE
README.md
.gitignore
CLAUDE.md
```

## The workflow

1. Write a spec in `process/spec.md`
2. Ask Claude to define a feature — it creates a file in `features/notdone/`
3. Ask Claude to break the feature into tasks — it creates a task file in `tasks/notdone/`
4. Claude writes code only after tasks are defined
5. Every feature requires a testing task; feature is only closed when tests pass
6. Bugs get a regression test before being marked fixed

## Slash commands

| Command | What it does |
|---|---|
| `/newsesh` | Reorients Claude: reads current state and method |
| `/checkpoint` | Runs tests, regenerates literate docs, commits, pushes |

## Development (this repo)

```bash
uv sync
uv run pytest
```

## Contributing

Issues and PRs welcome. The methodology is intentionally opinionated — if you want to fork and adapt the rules in `method.md` or `coding.md` for your own style, that's exactly what j3 is designed for.

## License

MIT — see [LICENSE](LICENSE)
