import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import skill_map  # noqa: E402  (tools/skill_map.py)
import style_catalog as sc  # noqa: E402  (tools/style_catalog.py)

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


class ProjectMemoryTests(unittest.TestCase):
    MEMORY_REF = ROOT / "dev-lead" / "references" / "project-memory.md"

    def test_router_points_to_memory_reference(self):
        router = (ROOT / "dev-lead" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("`references/project-memory.md`", router)
        self.assertIn("PROJECT_MEMORY.md", router)

    def test_memory_template_has_required_sections(self):
        text = self.MEMORY_REF.read_text(encoding="utf-8")
        for heading in (
            "## Snapshot",
            "## Now",
            "## Verified status",
            "## Working agreements",
            "## Guardrails",
            "## Where things are",
            "## Gotchas",
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, text)

    def test_entry_file_template_covers_both_tools(self):
        text = self.MEMORY_REF.read_text(encoding="utf-8")
        self.assertIn("AGENTS.md", text)
        self.assertIn("CLAUDE.md", text)
        entry = text.split("## 8. Template: AGENTS.md and CLAUDE.md", 1)[1]
        self.assertIn("PROJECT_MEMORY.md", entry)

    def test_memory_rules_keep_safety_limits(self):
        text = self.MEMORY_REF.read_text(encoding="utf-8")
        self.assertIn("## 4. What never goes in", text)
        self.assertIn("Secrets", text)
        self.assertIn("never replace dev-lead's risk rules", text)

    def test_stage_skills_do_not_link_into_other_skill_folders(self):
        # Each skill folder must stay standalone, so memory details live only in dev-lead.
        cross_link = re.compile(r"`(?:\.\./|dev-lead/references/)[^`]*`")
        for skill_file in SKILL_FILES:
            if skill_file.parent.name == "dev-lead":
                continue
            with self.subTest(skill=skill_file.parent.name):
                text = skill_file.read_text(encoding="utf-8")
                self.assertIsNone(cross_link.search(text))


class SkillConnectionTests(unittest.TestCase):
    def setUp(self):
        self.names = {d.name for d in skill_map.skill_dirs()}
        self.stage_names = self.names - {"dev-lead"}
        self.connections = skill_map.load_all()

    def test_every_skill_has_needs_produces_and_next(self):
        for name, fields in self.connections.items():
            for field in skill_map.FIELDS:
                with self.subTest(skill=name, field=field):
                    self.assertTrue(fields.get(field), f"{name}: missing '{field}' in Connections")

    def test_skill_names_in_connections_exist(self):
        for name, fields in self.connections.items():
            for field in ("Needs", "Next"):
                for mentioned in skill_map.skill_names_in(fields.get(field, "")):
                    with self.subTest(skill=name, field=field, mentioned=mentioned):
                        self.assertIn(mentioned, self.names)
            if name != "dev-lead":
                with self.subTest(skill=name, check="no self-reference in Next"):
                    self.assertNotIn(name, skill_map.skill_names_in(fields.get("Next", "")))

    def test_needed_files_name_a_skill_that_produces_them(self):
        pattern = re.compile(r"`([^`]+\.md)`")
        for name, fields in self.connections.items():
            needs = fields.get("Needs", "")
            for match in pattern.finditer(needs):
                artifact = match.group(1)
                with self.subTest(skill=name, artifact=artifact):
                    tail = needs[match.end():]
                    producer = re.match(r" \(from `([a-z]+(?:-[a-z]+)+)`", tail)
                    self.assertIsNotNone(producer, f"{name}: Needs {artifact} without '(from `skill`...)'")
                    self.assertIn(producer.group(1), self.names)
                    self.assertIn(
                        artifact,
                        skill_map.artifacts_in(self.connections[producer.group(1)].get("Produces", "")),
                        f"{producer.group(1)} does not list {artifact} under Produces",
                    )

    def test_no_dead_ends_and_every_stage_is_reachable(self):
        edges = {n: set(skill_map.skill_names_in(f.get("Next", ""))) for n, f in self.connections.items()}
        for name in self.stage_names:
            with self.subTest(skill=name, check="has a next step"):
                self.assertTrue(edges[name], f"{name} has no Next skill (dead end)")
        reached, queue = {"plan-project"}, ["plan-project"]
        while queue:
            for nxt in edges.get(queue.pop(), ()):
                if nxt not in reached:
                    reached.add(nxt)
                    queue.append(nxt)
        unreachable = self.stage_names - reached
        self.assertEqual(unreachable, set(), f"not reachable from plan-project via Next: {sorted(unreachable)}")

    def test_generated_skill_map_is_current(self):
        current = skill_map.MAP_FILE.read_text(encoding="utf-8")
        self.assertEqual(
            current, skill_map.build_map(),
            "skill-map.md is stale; run: python tools/skill_map.py --write",
        )

    def test_router_explains_how_to_use_connections(self):
        router = (ROOT / "dev-lead" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("## How the stages connect", router)
        self.assertIn("`references/skill-map.md`", router)

    def test_descriptions_fit_the_length_limit(self):
        for skill_file in SKILL_FILES:
            text = skill_file.read_text(encoding="utf-8")
            description = re.search(r"^description: (.+)$", text, re.M).group(1)
            with self.subTest(skill=skill_file.parent.name):
                self.assertLessEqual(len(description), 1024)


class StyleCatalogTests(unittest.TestCase):
    def setUp(self):
        self.files = sc.style_files()
        self.names = {p.stem for p in self.files}
        self.styles = {p.stem: sc.parse_style(p) for p in self.files}

    def test_catalog_is_not_empty_and_index_exists(self):
        self.assertGreaterEqual(len(self.files), 10)
        self.assertTrue(sc.INDEX_FILE.exists())

    def test_index_links_every_style_exactly_once(self):
        links = [Path(link).stem for link in sc.index_links()]
        self.assertEqual(sorted(links), sorted(self.names))

    def test_index_table_rows_are_complete(self):
        text = sc.INDEX_FILE.read_text(encoding="utf-8")
        rows = [line for line in text.splitlines() if line.startswith("| [")]
        self.assertEqual(len(rows), len(self.names))
        for row in rows:
            cells = [c.strip() for c in row.strip("|").split("|")]
            with self.subTest(row=cells[0]):
                self.assertEqual(len(cells), 6)
                self.assertTrue(all(cells))
                self.assertIn(cells[4], {"low", "medium", "high"})
                self.assertIn(cells[5], {"low", "medium"})

    def test_style_names_in_index_pickers_and_pairings_are_real(self):
        hyphenated = re.compile(r"\b[a-z]+(?:-[a-z]+)+\b")
        text = sc.INDEX_FILE.read_text(encoding="utf-8")
        picker = text.split("## Pick by situation", 1)[1].split("\n## ", 1)[0]
        for line in picker.splitlines():
            if line.startswith("|") and not line.startswith("|--") and "Situation" not in line:
                for cell in line.strip("|").split("|")[1:]:
                    for token in hyphenated.findall(cell):
                        with self.subTest(picker_cell=token):
                            self.assertIn(token, self.names)
        for name, style in self.styles.items():
            for token in hyphenated.findall(style["sections"].get("Pairs with", "")):
                with self.subTest(style=name, pairs=token):
                    self.assertIn(token, self.names)

    def test_style_files_have_every_section_in_order(self):
        for name, style in self.styles.items():
            with self.subTest(style=name):
                headings = list(style["sections"])
                self.assertEqual(headings, list(sc.REQUIRED_SECTIONS))

    def test_tokens_are_complete_and_colors_are_hex(self):
        for name, style in self.styles.items():
            tokens = style["tokens"]
            for token in sc.COLOR_TOKENS + sc.OTHER_TOKENS:
                with self.subTest(style=name, token=token):
                    self.assertIn(token, tokens)
            for token in sc.COLOR_TOKENS:
                with self.subTest(style=name, token=token, check="hex"):
                    self.assertRegex(tokens.get(token, ""), sc.HEX)

    def test_palettes_meet_contrast_limits(self):
        for name, style in self.styles.items():
            t = style["tokens"]
            if any(token not in t for token in sc.COLOR_TOKENS):
                continue  # test_tokens_are_complete_and_colors_are_hex reports the missing token
            checks = [
                ("--text on --bg", t["--text"], t["--bg"], 4.5),
                ("--text on --surface", t["--text"], t["--surface"], 4.5),
                ("--muted on --bg", t["--muted"], t["--bg"], 4.5),
                ("--muted on --surface", t["--muted"], t["--surface"], 4.5),
                ("--on-primary on --primary", t["--on-primary"], t["--primary"], 4.5),
                ("--focus on --bg", t["--focus"], t["--bg"], 3.0),
                ("--focus on --surface", t["--focus"], t["--surface"], 3.0),
            ]
            for label, fg, bg, needed in checks:
                with self.subTest(style=name, pair=label):
                    self.assertGreaterEqual(sc.contrast(fg, bg), needed, f"{name}: {label}")

    def test_starter_css_is_complete_and_token_only(self):
        for name, style in self.styles.items():
            css = style["starter_css"]
            with self.subTest(style=name):
                self.assertTrue(css.strip(), "empty starter CSS")
                for selector in (".card", ".button", ".input", ":focus-visible"):
                    self.assertIn(selector, css)
                self.assertEqual(css.count("{"), css.count("}"), "unbalanced braces")
                self.assertIsNone(re.search(r"#[0-9A-Fa-f]{3,8}\b", css), "raw hex color in starter CSS")
                self.assertIsNone(re.search(r"outline:\s*(none|0)\b", css), "focus outline removed")
                used = set(re.findall(r"var\((--[\w-]+)\)", css))
                self.assertEqual(used - set(style["tokens"]), set(), "uses undeclared tokens")

    def test_every_accessibility_trap_has_a_fix(self):
        for name, style in self.styles.items():
            with self.subTest(style=name):
                self.assertGreaterEqual(len(style["traps"]), 3)
                for trap in style["traps"]:
                    self.assertIn(" Fix: ", trap)
                    self.assertTrue(trap.rstrip().endswith("."))

    def test_glassmorphism_keeps_its_fallbacks(self):
        css = self.styles["glassmorphism"]["starter_css"]
        self.assertIn("@supports not", css)
        self.assertIn("-webkit-backdrop-filter", css)
        self.assertIn("prefers-reduced-transparency", css)

    def test_design_ui_points_to_the_catalog(self):
        text = (ROOT / "design-ui" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("`references/styles/index.md`", text)

    def test_gallery_shows_every_style(self):
        page = sc.build_gallery()
        for style in self.styles.values():
            with self.subTest(style=style["name"]):
                self.assertIn(style["title"].replace("&", "&amp;"), page)
        self.assertEqual(page.count("<iframe"), len(self.styles))


class ConceptGuideTests(unittest.TestCase):
    CONCEPT = ROOT / "design-ui" / "references" / "concept.md"
    HEADINGS = [
        "When to use it",
        "The six steps",
        "Guardrails: usability beats theme",
        "The DESIGN.md concept template",
        "Worked examples",
    ]
    FIELDS = ("Idea", "Feeling", "Metaphor", "Style", "Signature parts", "Stays plain", "Avoid")

    def setUp(self):
        self.text = self.CONCEPT.read_text(encoding="utf-8")
        self.sections = {re.sub(r"^\d+\.\s*", "", k): v for k, v in sc.sections(self.text).items()}
        self.style_names = {p.stem for p in sc.style_files()}

    def examples(self):
        parts = re.split(r"^### (.+)$", self.sections.get("Worked examples", ""), flags=re.M)
        return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}

    def test_design_ui_points_to_the_concept_guide(self):
        text = (ROOT / "design-ui" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("`references/concept.md`", text)

    def test_guide_has_its_sections_in_order(self):
        headings = [h for h in self.sections if h != "Contents"]
        self.assertEqual(headings, self.HEADINGS)

    def test_six_steps_and_guardrails_are_present(self):
        steps = re.findall(r"^\d\. \*\*", self.sections.get("The six steps", ""), flags=re.M)
        self.assertEqual(len(steps), 6)
        guardrails = [l for l in self.sections.get("Guardrails: usability beats theme", "").splitlines() if l.startswith("- ")]
        self.assertGreaterEqual(len(guardrails), 6)

    def test_template_covers_the_concept_and_the_plain_parts(self):
        template = self.sections.get("The DESIGN.md concept template", "")
        for heading in ("## Concept", "## Style", "## Tokens", "## Signature parts", "## Stays plain", "## Avoid"):
            with self.subTest(heading=heading):
                self.assertIn(heading, template)

    def test_worked_examples_are_complete(self):
        examples = self.examples()
        self.assertGreaterEqual(len(examples), 3)
        for name, body in examples.items():
            for field in self.FIELDS:
                with self.subTest(example=name, field=field):
                    self.assertIn(f"**{field}:**", body)
            with self.subTest(example=name, check="style exists in the catalog"):
                style = re.search(r"\*\*Style:\*\* ([a-z]+(?:-[a-z]+)*)", body)
                self.assertIsNotNone(style)
                self.assertIn(style.group(1), self.style_names)

    def test_worked_example_palettes_meet_contrast_limits(self):
        for name, body in self.examples().items():
            tokens = sc.parse_tokens(sc.css_block(body))
            for token in sc.COLOR_TOKENS:
                with self.subTest(example=name, token=token):
                    self.assertRegex(tokens.get(token, ""), sc.HEX)
            if any(token not in tokens for token in sc.COLOR_TOKENS):
                continue
            checks = [
                ("--text on --bg", tokens["--text"], tokens["--bg"], 4.5),
                ("--text on --surface", tokens["--text"], tokens["--surface"], 4.5),
                ("--muted on --bg", tokens["--muted"], tokens["--bg"], 4.5),
                ("--muted on --surface", tokens["--muted"], tokens["--surface"], 4.5),
                ("--on-primary on --primary", tokens["--on-primary"], tokens["--primary"], 4.5),
                ("--focus on --bg", tokens["--focus"], tokens["--bg"], 3.0),
                ("--focus on --surface", tokens["--focus"], tokens["--surface"], 3.0),
            ]
            for label, fg, bg, needed in checks:
                with self.subTest(example=name, pair=label):
                    self.assertGreaterEqual(sc.contrast(fg, bg), needed)

    def test_router_has_the_small_idea_path(self):
        router = (ROOT / "dev-lead" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("## Small idea, working result", router)
        path = router.split("## Small idea, working result", 1)[1].split("\n## ", 1)[0]
        for needed in ("PLAN.md", "design-ui", "DESIGN.md", "test-feature", "rule 4"):
            with self.subTest(needed=needed):
                self.assertIn(needed, path)
        self.assertIn("small-idea path", router)

    def test_build_feature_builds_from_design_tokens(self):
        text = (ROOT / "build-feature" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("DESIGN.md", text)
        self.assertIn("CSS variables", text)


if __name__ == "__main__":
    unittest.main()
