# Current — j3

## Goal

Make `j3/.claude` a git submodule, consumed by passim (and other projects)
instead of manually copied and reconciled by hand each time.

## Constraint

Everything physically inside `.claude/` must stay byte-identical to `j3`'s
tracked state — a submodule is a full nested repo pinned to one commit; the
parent repo has no way to track a modified version of anything inside it.

## Status of the pieces

- **Already submodule-ready**: `process.md`, `literate.md`, `bootstrap.md`,
  `templates/`, `agents/`, `hooks/` — pristine matches with passim's copies
  today.
- **Needs trivial cleanup**: `commands/checkpoint.md` and `start.md` — passim's
  copies carry a `description:` frontmatter line these don't. Backport it here
  (or drop it in passim) so the two are identical again.
- **Needs a real split**: `style_guide.md` — passim has real additions (Before
  Every Commit, Absolute Rules — Salesforce) mixed into the generic base. For
  submodule purity these must move to a file *outside* `.claude/` in passim
  (e.g. `02-doc/style_guide.local.md`), referenced via `CLAUDE.md`'s
  `@`-import alongside `.claude/style_guide.md`.

## settings.json — decided: Option 3

Three options were considered for handling `settings.json`'s project-specific
content (permissions entries, `autoMode.environment` facts) once `.claude/`
becomes a submodule:

1. Use `.claude/settings.local.json` as an escape hatch — Claude Code merges
   it with `settings.json` regardless of git, but since it's *inside* the
   submodule, the parent repo can't track it. Content stops being
   version-controlled; a fresh clone loses it.
2. A tracked symlink inside `.claude/` pointing outside the submodule to a
   file the parent repo owns — keeps everything version-controlled and the
   submodule pristine, but adds real machinery (every consuming project has
   to create the external target; depends on unverified symlink support in
   Claude Code's settings loader).
3. **Chosen**: leave `settings.json` out of the submodule-sync story
   entirely. Keep reconciling its small, stable project-specific portion
   (currently ~15 lines in passim: a handful of `permissions` entries plus
   the `autoMode` block) by hand after each submodule bump — same manual
   process used all along, just scoped down to one file instead of ten.

**Why**: the tooling cost of options 1 and 2 is out of proportion to how
small and stable the project-specific part of `settings.json` actually is.

## Next steps (not yet done)

- Actually convert `passim/.claude` to a `git submodule` pointing at `j3`.
- Split `style_guide.md` in passim per above.
- Resolve the `description:` frontmatter divergence in
  `commands/checkpoint.md` and `start.md`.
- Re-apply passim's `settings.json` project-specific lines after the
  submodule conversion (per Option 3).
