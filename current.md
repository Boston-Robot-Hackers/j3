# Current — j3

## Status

<<<<<<< HEAD
Keep `j3/.claude` fully self-contained: copy `.claude/` into any project's
top-level folder, run `/bootstrap` inside Claude Code, and the project is
immediately functional with the full spec → feature → task → code → test
methodology — no submodule, no extra wiring, no manual reconciliation step.

## Status

- `.claude/` has no external/submodule dependencies today — confirmed no
  `submodule` or project-specific (e.g. `passim`) references exist anywhere
  inside it.
- `/bootstrap` (`.claude/commands/bootstrap.md`) + `.claude/bootstrap.md` already
  implement the copy-and-scaffold flow end to end: create the folder structure,
  populate starter files from `.claude/templates/`, then prompt the user to fill
  in `spec.md`, `current.md`, `notes.md`, placeholders, and `settings.json`'s
  `autoMode.environment` block.
- Previous plan (git submodule conversion for `.claude/`) is abandoned — dropped
  in favor of the simpler copy-based distribution model this file now describes.

## Next steps

- Periodically re-verify `.claude/` stays self-contained as it evolves (no
  hardcoded project names/paths, no assumed external files).
- If any consuming project's `.claude/` drifts from j3's and needs an update,
  the process is: re-copy `.claude/` wholesale from j3, then manually re-apply
  that project's own `settings.json` permissions/`autoMode` block (these are
  project-specific and not part of the generic kit).
=======
Nothing in progress.

## Considered and dropped

Turning `j3/.claude` into a git submodule, consumed by other projects instead
of copied and reconciled by hand, was explored and rejected.

No further action planned here.
>>>>>>> f8ba6a59326580877fae7b0145f2db3cab7929b2
