from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyManuscriptAssemblyPreviewPackageBuilder:
    version = "v8.215"

    draft_source_json_path = Path("outputs/safe_abstract_toy_manuscript_section_draft_package_v8_213.json")
    audit_source_json_path = Path("outputs/safe_abstract_toy_manuscript_section_draft_package_audit_v8_214.json")

    output_md_path = Path("outputs/safe_abstract_toy_manuscript_assembly_preview_package_v8_215.md")
    output_json_path = Path("outputs/safe_abstract_toy_manuscript_assembly_preview_package_v8_215.json")

    package_phrase = "safe_manuscript_assembly_preview_packaged_but_no_manuscript_file_modified"

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Missing JSON source: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"Expected dict JSON payload from {path}")
        return payload

    def _draft_map(self, draft_source: Dict[str, Any]) -> Dict[str, Dict[str, str]]:
        drafts = draft_source.get("section_draft_items", [])
        if not isinstance(drafts, list):
            raise ValueError("section_draft_items must be a list.")
        return {item["manuscript_section"]: item for item in drafts}

    def _assembled_sections(self, draft_source: Dict[str, Any]) -> List[Dict[str, str]]:
        drafts = self._draft_map(draft_source)

        ordered_sections = [
            "Abstract",
            "Introduction",
            "Method Scope",
            "Pipeline Overview",
            "Safety Controls",
            "Claim Governance",
            "Limitations",
            "Safety Exclusions",
            "Future Work",
        ]

        sections: List[Dict[str, str]] = []

        for index, section_name in enumerate(ordered_sections, start=1):
            item = drafts[section_name]
            sections.append(
                {
                    "id": f"AS-{index:02d}",
                    "manuscript_section": section_name,
                    "section_heading": section_name,
                    "assembled_text": item["draft_text"],
                    "usage_boundary": item["usage_boundary"],
                    "blocked_expansion": item["blocked_expansion"],
                }
            )

        return sections

    def _preview_title(self) -> str:
        return "A Safety-Bounded Governance Pipeline for Safe Abstract Toy Manuscript Claim Control"

    def _keywords(self) -> List[str]:
        return [
            "safe abstract toy systems",
            "claim governance",
            "manuscript patch control",
            "safety-bounded artifacts",
            "non-operational evaluation planning",
            "anti-overclaim workflow",
        ]

    def build(self) -> Dict[str, Any]:
        draft_source = self._load_json(self.draft_source_json_path)
        audit_source = self._load_json(self.audit_source_json_path)

        draft_counters = draft_source.get("counters", {})
        audit_counters = audit_source.get("counters", {})

        assembled_sections = self._assembled_sections(draft_source)

        assembled_text = "\n\n".join(
            f"## {section['section_heading']}\n\n{section['assembled_text']}"
            for section in assembled_sections
        )

        counters = {
            "Safe abstract toy manuscript assembly preview package count": 1,
            "New safe abstract toy manuscript assembly preview package count": 1,
            "Toy manuscript assembly preview package JSON export count": 1,
            "Toy manuscript assembly preview section count": len(assembled_sections),
            "Toy manuscript assembly preview source draft item count": draft_counters.get("Toy manuscript section draft package item count"),
            "Toy manuscript assembly preview source audit item count": audit_counters.get("Toy manuscript section draft package audit item count"),
            "Toy manuscript assembly preview source audit pass count": audit_counters.get("Toy manuscript section draft package audit pass count"),
            "Toy manuscript assembly preview source audit failure count": audit_counters.get("Toy manuscript section draft package audit failure count"),
            "Toy manuscript assembly preview execution count": 1,
            "Toy manuscript assembly preview direct execution count": 1,
            "Toy manuscript assembly preview non-readiness disclaimer count": 1,
            "Toy manuscript assembly preview boundary note count": len(assembled_sections),
            "Toy manuscript patch application checklist completion count": 0,
            "Toy manuscript patch application checklist execution count": 0,
            "Toy manuscript patch application permission count": 0,
            "Toy manuscript patch application applied patch count": 0,
            "Toy manuscript patch application manuscript file modified count": 0,
            "Toy manuscript patch application manuscript mutation count": 0,
            "Real biological dataset import count": 0,
            "Real pathogen simulation count": 0,
            "Real receptor parameter count": 0,
            "Operational host targeting count": 0,
            "Wet-lab protocol count": 0,
            "Actionable biosafety-risk instruction count": 0,
            "Real-world infectivity optimization count": 0,
            "Immune evasion optimization count": 0,
            "Real host range prediction count": 0,
            "Proof assistant verification count": 0,
            "External validation count": 0,
            "Independent experiment count": 0,
            "Manuscript submission ready count": 0,
            "Readiness approval count": 0,
            "New citation added count": 0,
        }

        report = {
            "version": self.version,
            "title": "Safe Abstract Toy Manuscript Assembly Preview Package",
            "preview_title": self._preview_title(),
            "keywords": self._keywords(),
            "draft_source_json": str(self.draft_source_json_path),
            "audit_source_json": str(self.audit_source_json_path),
            "package_phrase": self.package_phrase,
            "scope": "manuscript-assembly-preview-package-only",
            "safe_abstract_toy_only": True,
            "synthetic_only": True,
            "abstract_graphs_only": True,
            "unitless_parameters_only": True,
            "non_operational_only": True,
            "application_permission_granted": False,
            "application_execution_performed": False,
            "checklist_completion_performed": False,
            "checklist_execution_performed": False,
            "manuscript_file_modified": False,
            "manuscript_mutation": False,
            "applied_patch_count": 0,
            "non_readiness_disclaimer": (
                "This v8.215 artifact assembles a safe manuscript preview only. It does not complete checklist "
                "items, execute checklist steps, grant application permission, apply manuscript patches, modify "
                "manuscript files, approve readiness, establish submission readiness, validate scientific claims, "
                "add citations, or add real-biological operational capability."
            ),
            "assembled_sections": assembled_sections,
            "assembled_text": assembled_text,
            "boundary_notes": [section["usage_boundary"] for section in assembled_sections],
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "manuscript-assembly-preview-package-only":
            raise AssertionError("v8.215 must remain manuscript-assembly-preview-package-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.215 assembly preview package must pass.")

        for field in [
            "application_permission_granted",
            "application_execution_performed",
            "checklist_completion_performed",
            "checklist_execution_performed",
            "manuscript_file_modified",
            "manuscript_mutation",
        ]:
            if report[field] is not False:
                raise AssertionError(f"Expected False for {field}")

        if report["applied_patch_count"] != 0:
            raise AssertionError("Applied patch count must remain zero.")

        counters = report["counters"]

        if counters["Toy manuscript assembly preview section count"] != 9:
            raise AssertionError("Expected exactly nine assembled preview sections.")

        if counters["Toy manuscript assembly preview source draft item count"] != 9:
            raise AssertionError("Expected source draft item count of nine.")

        if counters["Toy manuscript assembly preview source audit item count"] != 11:
            raise AssertionError("Expected source audit item count of eleven.")

        if counters["Toy manuscript assembly preview source audit pass count"] != 11:
            raise AssertionError("Expected source audit pass count of eleven.")

        if counters["Toy manuscript assembly preview source audit failure count"] != 0:
            raise AssertionError("Expected source audit failure count of zero.")

        required_phrases = [
            "internally audited, safety-bounded, safe abstract toy-only governance pipeline",
            "does not import real biological datasets",
            "does not model real pathogens",
            "zero applied patches",
            "does not establish external validation",
            "Future work may only introduce stronger claims",
        ]

        for phrase in required_phrases:
            if phrase not in report["assembled_text"]:
                raise AssertionError(f"Missing required assembled phrase: {phrase}")

        must_be_zero = [
            "Toy manuscript patch application checklist completion count",
            "Toy manuscript patch application checklist execution count",
            "Toy manuscript patch application permission count",
            "Toy manuscript patch application applied patch count",
            "Toy manuscript patch application manuscript file modified count",
            "Toy manuscript patch application manuscript mutation count",
            "Real biological dataset import count",
            "Real pathogen simulation count",
            "Real receptor parameter count",
            "Operational host targeting count",
            "Wet-lab protocol count",
            "Actionable biosafety-risk instruction count",
            "Real-world infectivity optimization count",
            "Immune evasion optimization count",
            "Real host range prediction count",
            "Proof assistant verification count",
            "External validation count",
            "Independent experiment count",
            "Manuscript submission ready count",
            "Readiness approval count",
            "New citation added count",
        ]

        for name in must_be_zero:
            if counters.get(name) != 0:
                raise AssertionError(f"Counter must remain zero: {name}")

    def render_markdown(self, report: Dict[str, Any]) -> str:
        lines: List[str] = []

        lines.append("# Safe Abstract Toy Manuscript Assembly Preview Package")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is manuscript-assembly-preview-package-only.")
        lines.append("It assembles a readable manuscript preview from audited safe section drafts without applying, authorizing, completing, or executing any manuscript patch workflow.")
        lines.append("")
        lines.append(f"Package phrase: `{report['package_phrase']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")
        lines.append("## Preview Title")
        lines.append("")
        lines.append(report["preview_title"])
        lines.append("")
        lines.append("## Keywords")
        lines.append("")
        for keyword in report["keywords"]:
            lines.append(f"- {keyword}")
        lines.append("")
        lines.append("## Assembled Manuscript Preview")
        lines.append("")
        lines.append(report["assembled_text"])
        lines.append("")
        lines.append("## Section Boundaries")
        lines.append("")
        for section in report["assembled_sections"]:
            lines.append(f"### {section['id']} — {section['manuscript_section']}")
            lines.append("")
            lines.append(f"- Usage boundary: {section['usage_boundary']}")
            lines.append(f"- Blocked expansion: {section['blocked_expansion']}")
            lines.append("")
        lines.append("## Counters")
        lines.append("")
        for key, value in report["counters"].items():
            lines.append(f"{key}: {value}")
        lines.append("")
        lines.append("## Result")
        lines.append("")
        lines.append(f"Passed: {report['passed']}")
        lines.append("")
        lines.append("V8_215_SAFE_ABSTRACT_TOY_MANUSCRIPT_ASSEMBLY_PREVIEW_PACKAGE_OK")
        lines.append("")

        return "\n".join(lines)

    def run(self) -> Dict[str, Any]:
        report = self.build()
        self.output_md_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_json_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_md_path.write_text(self.render_markdown(report), encoding="utf-8")
        self.output_json_path.write_text(
            json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        return report


def build_safe_abstract_toy_manuscript_assembly_preview_package() -> Dict[str, Any]:
    return SafeAbstractToyManuscriptAssemblyPreviewPackageBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_manuscript_assembly_preview_package()
    counters = result["counters"]
    print("V8_215_SAFE_ABSTRACT_TOY_MANUSCRIPT_ASSEMBLY_PREVIEW_PACKAGE_OK")
    print("TOY_MANUSCRIPT_ASSEMBLY_PREVIEW_PACKAGE_DIRECT_CHECK_OK")
    print(f"Assembly preview section count: {counters['Toy manuscript assembly preview section count']}")
    print(f"Source draft item count: {counters['Toy manuscript assembly preview source draft item count']}")
    print(f"Source audit item count: {counters['Toy manuscript assembly preview source audit item count']}")
    print(f"Source audit pass count: {counters['Toy manuscript assembly preview source audit pass count']}")
    print(f"Source audit failure count: {counters['Toy manuscript assembly preview source audit failure count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"Passed: {result['passed']}")
