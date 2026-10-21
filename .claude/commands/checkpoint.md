---
description: Run tests, update docs, commit and push
allowed-tools: Bash(git add *) Bash(git commit *) Bash(git push *) Bash(git diff *) Bash(git ls-files *) Bash(uv run pytest *) Bash(uv run ruff *) Read Edit Write Glob
---
Run a full checkpoint in this order:

- Run all tests: `uv run pytest`
- Run `uv run ruff check` and `uv run ruff format --check` on changed `.py` files
  only (staged, unstaged, and untracked — never the whole repo); fix any
  violations before continuing
- Update current.md's `## Open` section with your latest context; move any
  newly-completed items out to `process/02-doc/history.md` instead of appending to
  current.md
- Review changed code against judgment rules in @.claude/style_guide.md (design, error handling, naming semantics)
- Update any changed literate md files
- Create a commit (no need for a pull request)
- Push to github