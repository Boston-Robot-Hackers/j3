# Current — j3

## Goal

Keep `j3/.claude` fully self-contained: copy `.claude/` into any project's
top-level folder, run `/bootstrap` inside Claude Code, and the project is
immediately functional with the full spec → feature → task → code → test
methodology — no submodule, no extra wiring, no manual reconciliation step.

## Status

Nothing in progress.

- `.claude/` has no external/submodule dependencies and no project-specific
  references.
- `/bootstrap` (`.claude/commands/bootstrap.md`) + `.claude/bootstrap.md`
  implement the copy-and-scaffold flow end to end.

## Ongoing upkeep

- Periodically re-verify `.claude/` stays self-contained as it evolves (no
  hardcoded project names/paths, no assumed external files).
- When a consuming project's `.claude/` drifts: re-copy `.claude/` wholesale
  from j3, then re-apply that project's own `settings.json` permissions and
  `autoMode` block — these are project-specific, not part of the kit.

## Considered and dropped

Turning `j3/.claude` into a git submodule, consumed by other projects instead
of copied and reconciled by hand, was explored and rejected in favor of the
copy-based model above.
