# Bootstrap Scaffold

When bootstrapping a new project, assume that you are inside the directory of the target. Check the `.claude/` folder is there and correct. Then create the following files and folders exactly as specified below.

## Folder structure to create

```
LICENSE
README.md
.gitignore
CLAUDE.md
01-literate/
02-doc/
  spec.md
  current.md
  notes.md
03-features/
  notdone/
  done/
  deferred/
  template.md
04-tasks/
  notdone/
  done/
  deferred/
  template.md
05-issues/
  template.md
```

### LICENSE
Copy from `.claude/templates/LICENSE.template` and replace `<YEAR>` and `<AUTHOR NAME>`.

### README.md
Copy from `.claude/templates/README.md.template` and replace `<APP NAME>` and other placeholders.

### .gitignore
Copy from `.claude/templates/.gitignore.template` as-is.

### CLAUDE.md
Create at the project root with this content (fill in the app name):
```
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Read and follow all rules in the `.claude/` folder:
- `.claude/process.md` — development workflow and feature/task tracking rules
- `.claude/coding.md` — coding standards, style rules, and review checklist
- `02-doc/current.md` — latest status
- `02-doc/notes.md` — semi-permanent project notes

We are developing a repo called <APP NAME>. Features are in `03-features/`, tasks in `04-tasks/`, issues in `05-issues/`, spec in `02-doc/spec.md`.
```

### 03-features/template.md
Copy from `.claude/templates/feature-template.md`.

### 04-tasks/template.md
Copy from `.claude/templates/task_template.md`.

### 05-issues/template.md
Copy from `.claude/templates/issue_template.md`.

### 02-doc/spec.md, 02-doc/current.md, 02-doc/notes.md
Create as empty files with a `# Title` heading placeholder.

## After scaffolding

Prompt the user to:
1. Fill in `02-doc/spec.md` with the app description
2. Initialize `02-doc/current.md` with current session status
3. Replace `<APP NAME>` in `CLAUDE.md`, `README.md`, and `LICENSE` with the actual app name, author, and year
4. Define the first feature before writing any code
