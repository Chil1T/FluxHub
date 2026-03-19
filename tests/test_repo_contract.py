from __future__ import annotations

import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = [
    ".gitignore",
    "README.md",
    "AGENTS.md",
    ".codex/config.toml",
    "docs/README.md",
    "docs/product/vision.md",
    "docs/collaboration/codex-workflow.md",
    "docs/runbooks/repo-modernization-baseline.md",
    "docs/runbooks/github-remote-preflight.md",
    "docs/specs/README.md",
    "docs/plans/README.md",
    ".agents/skills/winui-sticky-notes-entry/SKILL.md",
    ".agents/skills/playground-repo-maintenance/SKILL.md",
    ".github/workflows/repo-hygiene.yml",
]
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


class RepoContractTests(unittest.TestCase):
    def test_required_paths_exist(self) -> None:
        missing = [path for path in REQUIRED_PATHS if not (REPO_ROOT / path).exists()]
        self.assertEqual([], missing, f"Missing required repository paths: {missing}")

    def test_root_agents_mentions_docs_and_validation(self) -> None:
        content = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("docs/README.md", content)
        self.assertIn("python -m unittest discover -s tests -p \"test_*.py\" -v", content)

    def test_gitignore_covers_common_local_artifacts(self) -> None:
        content = (REPO_ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn("__pycache__/", content)
        self.assertIn(".vscode/", content)
        self.assertIn("bin/", content)
        self.assertIn("obj/", content)

    def test_repo_local_skills_have_basic_metadata(self) -> None:
        skill_paths = [
            REPO_ROOT / ".agents/skills/winui-sticky-notes-entry/SKILL.md",
            REPO_ROOT / ".agents/skills/playground-repo-maintenance/SKILL.md",
        ]
        for path in skill_paths:
            content = path.read_text(encoding="utf-8")
            self.assertIn("name:", content, f"{path} is missing a skill name")
            self.assertIn("description:", content, f"{path} is missing a skill description")

    def test_markdown_links_resolve(self) -> None:
        failures: list[str] = []

        for markdown_path in REPO_ROOT.rglob("*.md"):
            text = markdown_path.read_text(encoding="utf-8")
            for raw_target in MARKDOWN_LINK_RE.findall(text):
                if self._should_skip_target(raw_target):
                    continue

                target = raw_target.split("#", 1)[0]
                candidate = (markdown_path.parent / target).resolve()
                if not candidate.exists():
                    rel_source = markdown_path.relative_to(REPO_ROOT)
                    failures.append(f"{rel_source} -> {raw_target}")

        self.assertEqual([], failures, f"Broken markdown links: {failures}")

    @staticmethod
    def _should_skip_target(target: str) -> bool:
        return (
            target.startswith("http://")
            or target.startswith("https://")
            or target.startswith("mailto:")
            or target.startswith("#")
        )


if __name__ == "__main__":
    unittest.main()
