#!/usr/bin/env python3
# test_bootstrap.py — tests that verify j3 bootstrap produces correct project structure
# Author: Pito Salas and Claude Code
# Open Source Under MIT license

import shutil
import tempfile
from pathlib import Path

import pytest


J3_DIR = Path(__file__).parent.parent / ".claude"

EXPECTED_FILES = [
    "CLAUDE.md",
    "LICENSE",
    "README.md",
    ".gitignore",
    "process/spec.md",
    "process/features/template.md",
    "process/tasks/template.md",
]

EXPECTED_DIRS = [
    "process/features/notdone",
    "process/features/done",
    "process/tasks/notdone",
    "process/tasks/done",
]


@pytest.fixture()
def bootstrapped_project():
    tmp = Path(tempfile.mkdtemp())
    shutil.copytree(J3_DIR, tmp / ".claude")
    _scaffold(tmp)
    yield tmp
    shutil.rmtree(tmp)


def _scaffold(root: Path):
    for d in EXPECTED_DIRS:
        (root / d).mkdir(parents=True, exist_ok=True)

    templates = J3_DIR / "templates"
    (root / "CLAUDE.md").write_text(
        (templates / "CLAUDE.md.template").read_text()
    )
    (root / "process/spec.md").write_text(
        "# Spec for <APP NAME>\n* <Describe what the app does>\n"
    )
    (root / "process/features/template.md").write_text(
        (J3_DIR / "templates" / "feature-template.md").read_text()
    )
    (root / "process/tasks/template.md").write_text(
        (J3_DIR / "templates" / "task_template.md").read_text()
    )
    (root / "LICENSE").write_text(
        (templates / "LICENSE.template").read_text()
    )
    (root / "README.md").write_text(
        (templates / "README.md.template").read_text()
    )
    (root / ".gitignore").write_text(
        (templates / ".gitignore.template").read_text()
    )


def test_j3_dir_is_present(bootstrapped_project):
    assert (bootstrapped_project / ".claude").is_dir()


def test_j3_required_files_exist(bootstrapped_project):
    for name in ["method.md", "coding.md", "bootstrap.md"]:
        assert (bootstrapped_project / ".claude" / name).exists(), f"Missing .claude/{name}"
    assert (bootstrapped_project / ".claude" / "templates" / "CLAUDE.md.template").exists()


def test_expected_dirs_created(bootstrapped_project):
    for d in EXPECTED_DIRS:
        assert (bootstrapped_project / d).is_dir(), f"Missing dir: {d}"


def test_expected_files_created(bootstrapped_project):
    for f in EXPECTED_FILES:
        assert (bootstrapped_project / f).is_file(), f"Missing file: {f}"


def test_claude_md_contains_app_placeholder(bootstrapped_project):
    content = (bootstrapped_project / "CLAUDE.md").read_text()
    assert "<APP NAME>" in content


def test_spec_md_contains_app_placeholder(bootstrapped_project):
    content = (bootstrapped_project / "process/spec.md").read_text()
    assert "<APP NAME>" in content


def test_license_is_mit(bootstrapped_project):
    content = (bootstrapped_project / "LICENSE").read_text()
    assert "MIT License" in content
    assert "<YEAR>" in content
    assert "<AUTHOR NAME>" in content


def test_readme_contains_app_placeholder(bootstrapped_project):
    content = (bootstrapped_project / "README.md").read_text()
    assert "<APP NAME>" in content


def test_gitignore_covers_venv(bootstrapped_project):
    content = (bootstrapped_project / ".gitignore").read_text()
    assert ".venv/" in content
