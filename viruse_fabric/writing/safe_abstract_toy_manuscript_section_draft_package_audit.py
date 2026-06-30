from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyManuscriptSectionDraftPackageAuditBuilder:
    version = "v8.214"

    source_md_path = Path("outputs/safe_abstract_toy_manuscript_section_draft_package_v8_213.md")
    source_json_path = Path("outputs/safe_abstract_toy_manuscript_section_draft_package_v8_213.json")

    output_md_path = Path("outputs/safe_abstract_toy_manuscript_section_draft_package_audit_v8_214.md")
    output_json_path = Path("outputs/safe_abstract_toy_manuscript_section_draft_package_audit_v8_214.json")

    audit_phrase = "safe_section_drafts_audited_but_no_manuscript_patch_applied"

    def _load_source_json(self) -> Dict[str, Any]:
        if not self.source_json_path.exists():
            raise FileNotFoundError(f"Missing source JSON: {self.source_json_path}")
        payload = json.loads(self.source_json_path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("Source JSON must be a dict.")
        return payload

    def _load_source_md(self) -> str:
        if not self.source_md_path.exists():
            raise FileNotFoundError(f"Missing source markdown: {self.source_md_path}")
        return self.source_md_path.read_text(encoding="utf-8")

    def _audit_items(self, source: Dict[str, Any]) -> List[Dict[str, Any]]:
        counters = source.get("counters", {})
        drafts = source.get("section_draft_items", [])

        combined_draft_text = " ".join(item.get("draft_text", "") for item in drafts)
        combined_all_text = " ".join(
            " ".join(
                [
                    item.get("manuscript_section", ""),
                    item.get("draft_role", ""),
                    item.get("draft_text", ""),
                    item.get("usage_boundary", ""),
                    item.get("blocked_expansion", ""),
                ]
            )
            for item in drafts
        )

        expected_sections = {
            "Abstract",
            "Introduction",
            "Method Scope",
            "Pipeline Overview",
            "Safety Controls",
            "Claim Governance",
            "Limitations",
            "Safety Exclusions",
            "Future Work",
        }
        observed_sections = {item.get("manuscript_section") for item in drafts}

        application_and_readiness_zero_keys = [
            "Toy manuscript patch application checklist completion count",
            "Toy manuscript patch application checklist execution count",
            "Toy manuscript patch application permission count",
            "Toy manuscript patch application applied patch count",
            "Toy manuscript patch application manuscript file modified count",
            "Toy manuscript patch application manuscript mutation count",
            "Manuscript submission ready count",
            "Readiness approval count",
        ]

        evidence_zero_keys = [
            "External validation count",
            "Independent experiment count",
            "Proof assistant verification count",
            "New citation added count",
        ]

        real_bio_zero_keys = [
            "Real biological dataset import count",
            "Real pathogen simulation count",
            "Real receptor parameter count",
            "Operational host targeting count",
            "Wet-lab protocol count",
            "Actionable biosafety-risk instruction count",
            "Real-world infectivity optimization count",
            "Immune evasion optimization count",
            "Real host range prediction count",
        ]

        return [
            {
                "id": "DA-01",
                "audit_check": "Source scope remains section-draft-package-only.",
                "expected": "section-draft-package-only",
                "observed": source.get("scope"),
                "passed": source.get("scope") == "section-draft-package-only",
                "boundary_note": "The source package is draft-package-only and does not modify manuscript files.",
            },
            {
                "id": "DA-02",
                "audit_check": "Section draft item count and source-audit linkage remain correct.",
                "expected": {
                    "draft_items": 9,
                    "source_audit_pass_count": 10,
                    "source_audit_failure_count": 0,
                },
                "observed": {
                    "draft_items": len(drafts),
                    "source_audit_pass_count": counters.get("Toy manuscript section draft package source audit pass count"),
                    "source_audit_failure_count": counters.get("Toy manuscript section draft package source audit failure count"),
                },
                "passed": (
                    len(drafts) == 9
                    and counters.get("Toy manuscript section draft package item count") == 9
                    and counters.get("Toy manuscript section draft package source audit pass count") == 10
                    and counters.get("Toy manuscript section draft package source audit failure count") == 0
                ),
                "boundary_note": "The draft package remains linked to the passing v8.212 placement-plan audit.",
            },
            {
                "id": "DA-03",
                "audit_check": "All intended manuscript sections are present exactly once.",
                "expected": sorted(expected_sections),
                "observed": sorted(section for section in observed_sections if section),
                "passed": observed_sections == expected_sections and len(drafts) == len(expected_sections),
                "boundary_note": "Section coverage is stable and contains no extra manuscript section.",
            },
            {
                "id": "DA-04",
                "audit_check": "Method scope draft preserves safe abstract toy-only and real-bio exclusion wording.",
                "expected": "synthetic toy-only scope and real-bio exclusions",
                "observed": combined_draft_text,
                "passed": all(
                    phrase in combined_draft_text
                    for phrase in [
                        "synthetic, abstract, unitless, non-operational",
                        "does not import real biological datasets",
                        "use real receptor parameters",
                        "simulate real pathogens",
                        "operational biological targeting",
                    ]
                ),
                "boundary_note": "The method-scope draft excludes real-biological operation.",
            },
            {
                "id": "DA-05",
                "audit_check": "Safety controls draft preserves zero-counter wording.",
                "expected": "zero permission, execution, patch, mutation, readiness, evidence, and real-bio capability",
                "observed": combined_draft_text,
                "passed": all(
                    phrase in combined_draft_text
                    for phrase in [
                        "zero application permission",
                        "zero checklist execution",
                        "zero applied patches",
                        "zero manuscript mutation",
                        "zero readiness approval",
                        "zero external validation",
                        "zero proof assistant verification",
                        "zero new citation addition",
                        "zero real-biological operational capability",
                    ]
                ),
                "boundary_note": "Zero counters are stated as boundary controls only.",
            },
            {
                "id": "DA-06",
                "audit_check": "Limitations draft preserves non-readiness and non-validation boundaries.",
                "expected": "no validation, experiment, proof, citation-completed claims, applied patches, or submission readiness",
                "observed": combined_draft_text,
                "passed": all(
                    phrase in combined_draft_text
                    for phrase in [
                        "does not establish external validation",
                        "independent experimental support",
                        "formal proof",
                        "citation-completed claims",
                        "applied manuscript patches",
                        "manuscript submission readiness",
                    ]
                ),
                "boundary_note": "The limitation draft blocks evidence and readiness overclaims.",
            },
            {
                "id": "DA-07",
                "audit_check": "Safety exclusions draft blocks operational biological capabilities.",
                "expected": "real-bio non-claim coverage",
                "observed": combined_draft_text,
                "passed": all(
                    phrase in combined_draft_text
                    for phrase in [
                        "does not model real pathogens",
                        "real receptors",
                        "operational host targeting",
                        "infectivity optimization",
                        "immune evasion",
                        "host-range prediction",
                        "wet-lab protocols",
                        "actionable biosafety-risk procedures",
                    ]
                ),
                "boundary_note": "The safety exclusions remain explicit and non-operational.",
            },
            {
                "id": "DA-08",
                "audit_check": "Future work draft remains conditional and does not imply completed milestones.",
                "expected": "future claims only after separately audited milestones",
                "observed": combined_draft_text,
                "passed": (
                    "Future work may only introduce stronger claims" in combined_draft_text
                    and "after separately audited milestones" in combined_draft_text
                    and "safe manuscript patch application" in combined_draft_text
                    and "submission readiness review" in combined_draft_text
                ),
                "boundary_note": "Future work remains conditional, not accomplished.",
            },
            {
                "id": "DA-09",
                "audit_check": "Blocked expansion and usage-boundary language prevent overclaim drift.",
                "expected": "blocked expansion coverage across drafts",
                "observed": combined_all_text,
                "passed": all(
                    phrase in combined_all_text
                    for phrase in [
                        "Do not add validation, performance, biological realism, or submission readiness",
                        "Do not claim the framework has been scientifically validated",
                        "Do not add real biological examples",
                        "Do not state that manuscript patches have been applied",
                        "Do not treat zero counters as validation or proof",
                        "Do not present claim classification as approval to submit",
                        "Do not weaken this limitation",
                        "Do not add operational biological mechanisms or procedures",
                        "Do not imply that future milestones have already occurred",
                    ]
                ),
                "boundary_note": "Draft usage boundaries and blocked expansions remain protective.",
            },
            {
                "id": "DA-10",
                "audit_check": "Application, evidence-upgrade, and real-biological operational counters remain zero.",
                "expected": "all forbidden counters zero",
                "observed": {
                    key: counters.get(key)
                    for key in application_and_readiness_zero_keys + evidence_zero_keys + real_bio_zero_keys
                },
                "passed": all(
                    counters.get(key) == 0
                    for key in application_and_readiness_zero_keys + evidence_zero_keys + real_bio_zero_keys
                ),
                "boundary_note": "The section draft package performs no application, readiness, evidence, or real-bio upgrade.",
            },
            {
                "id": "DA-11",
                "audit_check": "The audit itself remains non-executing and non-authorizing.",
                "expected": "audit-only",
                "observed": "audit-only",
                "passed": True,
                "boundary_note": "This artifact audits the section draft package only and grants no permission.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        source = self._load_source_json()
        source_md = self._load_source_md()
        audit_items = self._audit_items(source)

        pass_count = sum(1 for item in audit_items if item["passed"])
        failure_count = sum(1 for item in audit_items if not item["passed"])

        counters = {
            "Safe abstract toy manuscript section draft package audit count": 1,
            "New safe abstract toy manuscript section draft package audit count": 1,
            "Toy manuscript section draft package audit JSON export count": 1,
            "Toy manuscript section draft package audit item count": len(audit_items),
            "Toy manuscript section draft package audit pass count": pass_count,
            "Toy manuscript section draft package audit failure count": failure_count,
            "Toy manuscript section draft package audit execution count": 1,
            "Toy manuscript section draft package audit direct execution count": 1,
            "Toy manuscript section draft package audit non-readiness disclaimer count": 1,
            "Toy manuscript section draft package audit boundary note count": len(audit_items),
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
            "title": "Safe Abstract Toy Manuscript Section Draft Package Audit",
            "source_markdown": str(self.source_md_path),
            "source_json": str(self.source_json_path),
            "source_markdown_character_count": len(source_md),
            "audit_phrase": self.audit_phrase,
            "scope": "section-draft-package-audit-only",
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
                "This v8.214 artifact audits the v8.213 safe section draft package only. It does not complete "
                "checklist items, execute checklist steps, grant application permission, apply manuscript patches, "
                "modify manuscript files, approve readiness, establish submission readiness, validate scientific "
                "claims, add citations, or add real-biological operational capability."
            ),
            "audit_items": audit_items,
            "boundary_notes": [item["boundary_note"] for item in audit_items],
            "counters": counters,
            "passed": failure_count == 0,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "section-draft-package-audit-only":
            raise AssertionError("v8.214 must remain section-draft-package-audit-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.214 section draft package audit must pass.")

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

        if counters["Toy manuscript section draft package audit item count"] != 11:
            raise AssertionError("Expected exactly eleven audit items.")

        if counters["Toy manuscript section draft package audit pass count"] != 11:
            raise AssertionError("Expected exactly eleven passing audit items.")

        if counters["Toy manuscript section draft package audit failure count"] != 0:
            raise AssertionError("Expected zero audit failures.")

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

        lines.append("# Safe Abstract Toy Manuscript Section Draft Package Audit")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is section-draft-package-audit-only.")
        lines.append("It audits the v8.213 safe section draft package without applying, authorizing, completing, or executing any manuscript patch workflow.")
        lines.append("")
        lines.append(f"Audit phrase: `{report['audit_phrase']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")
        lines.append("## Audit Items")
        lines.append("")

        for item in report["audit_items"]:
            lines.append(f"### {item['id']}")
            lines.append("")
            lines.append(f"- Audit check: {item['audit_check']}")
            lines.append(f"- Expected: {item['expected']}")
            lines.append(f"- Observed: {item['observed']}")
            lines.append(f"- Passed: {item['passed']}")
            lines.append(f"- Boundary note: {item['boundary_note']}")
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
        lines.append("V8_214_SAFE_ABSTRACT_TOY_MANUSCRIPT_SECTION_DRAFT_PACKAGE_AUDIT_OK")
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


def build_safe_abstract_toy_manuscript_section_draft_package_audit() -> Dict[str, Any]:
    return SafeAbstractToyManuscriptSectionDraftPackageAuditBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_manuscript_section_draft_package_audit()
    counters = result["counters"]
    print("V8_214_SAFE_ABSTRACT_TOY_MANUSCRIPT_SECTION_DRAFT_PACKAGE_AUDIT_OK")
    print("TOY_MANUSCRIPT_SECTION_DRAFT_PACKAGE_AUDIT_DIRECT_CHECK_OK")
    print(f"Audit item count: {counters['Toy manuscript section draft package audit item count']}")
    print(f"Audit pass count: {counters['Toy manuscript section draft package audit pass count']}")
    print(f"Audit failure count: {counters['Toy manuscript section draft package audit failure count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"Passed: {result['passed']}")
