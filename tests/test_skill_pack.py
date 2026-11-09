import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_FILES = sorted(ROOT.glob("*/SKILL.md"))
STAGE_SKILLS = {path.parent.name for path in SKILL_FILES} - {"dev-lead"}


class SkillPackTests(unittest.TestCase):
    def test_skill_front_matter_matches_folder(self):
        for skill_file in SKILL_FILES:
            with self.subTest(skill=skill_file.parent.name):
                lines = skill_file.read_text(encoding="utf-8").splitlines()
                self.assertGreaterEqual(len(lines), 4)
                self.assertEqual(lines[0], "---")
                self.assertEqual(lines[1], f"name: {skill_file.parent.name}")
                self.assertRegex(lines[2], r"^description: .+\S$")
                self.assertEqual(lines[3], "---")

    def test_router_and_readme_cover_every_stage_skill(self):
        router = (ROOT / "dev-lead" / "SKILL.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        for skill in sorted(STAGE_SKILLS):
            with self.subTest(skill=skill):
                pattern = rf"(?<![\w-]){re.escape(skill)}(?![\w-])"
                self.assertRegex(router, pattern, f"{skill} missing from router")
                self.assertRegex(readme, pattern, f"{skill} missing from README")

    def test_referenced_skill_markdown_files_exist(self):
        reference_pattern = re.compile(r"`references/([^`]+\.md)`")
        for skill_file in SKILL_FILES:
            text = skill_file.read_text(encoding="utf-8")
            for reference in reference_pattern.findall(text):
                with self.subTest(skill=skill_file.parent.name, reference=reference):
                    self.assertTrue((skill_file.parent / "references" / reference).is_file())


if __name__ == "__main__":
    unittest.main()
