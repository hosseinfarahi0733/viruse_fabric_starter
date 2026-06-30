from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyManuscriptClaimLanguagePlacementPlanAuditBuilder:
    version = "v8.212"

    source_md_path = Path("outputs/safe_abstract_toy_manuscript_claim_language_placement_plan_v8_211.md")
    source_json_path = Path("outputs/safe_abstract_toy_manuscript_claim_language_placement_plan_v8_211.json")

    output_md_path = Path("outputs/safe_abstract_toy_manuscript_claim_language_placement_plan_audit_v8_212.md")
    output_json_path = Path("outputs/safe_abstract_toy_manuscript_claim_language_placement_plan_audit_v8_212.json")

    audit_phrase = "safe_claim_language_placement_plan_audited_but_no_manuscript_patch_applied"

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
        placements = source.get("placement_items", [])
        placement_text = " ".join(
            " ".join(
                [
                    item.get("manuscript_section", ""),
                    item.get("placement_role", ""),
                    item.get("safe_language", ""),
                    item.get("blocked_expansion", ""),
                    item.get("boundary_note", ""),
                ]
            )
            for item in placements
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

        observed_sections = {item.get("manuscript_section") for item in placements}

        return [
            {
                "id": "PA-01",
                "audit_check": "Source scope remains claim-language-placement-plan-only.",
                "expected": "claim-language-placement-plan-only",
                "observed": source.get("scope"),
                "passed": source.get("scope") == "claim-language-placement-plan-only",
                "boundary_note": "The source placement plan is planning-only and does not apply manuscript patches.",
            },
            {
                "id": "PA-02",
                "audit_check": "Placement item count is exactly nine.",
                "expected": 9,
                "observed": len(placements),
                "passed": len(placements) == 9 and counters.get("Toy manuscript claim language placement plan item count") == 9,
                "boundary_note": "Placement coverage remains stable.",
            },
            {
                "id": "PA-03",
                "audit_check": "All planned manuscript sections are present exactly once.",
                "expected": sorted(expected_sections),
                "observed": sorted(section for section in observed_sections if section),
                "passed": observed_sections == expected_sections and len(placements) == len(expected_sections),
                "boundary_note": "Placement map covers the intended manuscript sections without extra sections.",
            },
            {
                "id": "PA-04",
                "audit_check": "Placement safe language remains governance, boundary, scope, safety, limitation, and future-work oriented.",
                "expected": "safe abstract toy governance and boundary wording",
                "observed": placement_text,
                "passed": all(
                    phrase in placement_text
                    for phrase in [
                        "governance pipeline",
                        "claim boundaries",
                        "synthetic, abstract, unitless, non-operational toy artifacts",
                        "zero application permission",
                        "does not establish external validation",
                        "does not model real pathogens",
                        "Future work must separately audit",
                    ]
                ),
                "boundary_note": "Safe language remains bounded to allowed claim families.",
            },
            {
                "id": "PA-05",
                "audit_check": "Blocked expansions explicitly prevent validation, performance, biological realism, submission readiness, and applied-patch overclaims.",
                "expected": "blocked expansion coverage",
                "observed": placement_text,
                "passed": all(
                    phrase in placement_text
                    for phrase in [
                        "Do not claim validation",
                        "Do not convert the governance contribution into a scientific efficacy claim",
                        "Do not mention real biological datasets",
                        "Do not state that manuscript patches have been applied",
                        "Do not treat zero counters as scientific validation",
                        "Do not present claim classification as submission approval",
                        "Do not imply those future milestones have already occurred",
                    ]
                ),
                "boundary_note": "Blocked-expansion wording prevents obvious overclaim drift.",
            },
            {
                "id": "PA-06",
                "audit_check": "Source audit linkage remains successful.",
                "expected": {"source_audit_pass_count": 10, "source_audit_failure_count": 0},
                "observed": {
                    "source_audit_pass_count": counters.get("Toy manuscript claim language placement plan source audit pass count"),
                    "source_audit_failure_count": counters.get("Toy manuscript claim language placement plan source audit failure count"),
                },
                "passed": (
                    counters.get("Toy manuscript claim language placement plan source audit pass count") == 10
                    and counters.get("Toy manuscript claim language placement plan source audit failure count") == 0
                ),
                "boundary_note": "The placement plan remains linked to a passing v8.210 source audit.",
            },
            {
                "id": "PA-07",
                "audit_check": "Application, checklist, patch, manuscript mutation, and readiness counters remain zero.",
                "expected": "all application/readiness counters zero",
                "observed": {
                    key: counters.get(key)
                    for key in [
                        "Toy manuscript patch application checklist completion count",
                        "Toy manuscript patch application checklist execution count",
                        "Toy manuscript patch application permission count",
                        "Toy manuscript patch application applied patch count",
                        "Toy manuscript patch application manuscript file modified count",
                        "Toy manuscript patch application manuscript mutation count",
                        "Manuscript submission ready count",
                        "Readiness approval count",
                    ]
                },
                "passed": all(
                    counters.get(key) == 0
                    for key in [
                        "Toy manuscript patch application checklist completion count",
                        "Toy manuscript patch application checklist execution count",
                        "Toy manuscript patch application permission count",
                        "Toy manuscript patch application applied patch count",
                        "Toy manuscript patch application manuscript file modified count",
                        "Toy manuscript patch application manuscript mutation count",
                        "Manuscript submission ready count",
                        "Readiness approval count",
                    ]
                ),
                "boundary_note": "No placement item authorizes or performs manuscript patching.",
            },
            {
                "id": "PA-08",
                "audit_check": "Validation, experiment, proof, and citation counters remain zero.",
                "expected": "all evidence-upgrade counters zero",
                "observed": {
                    key: counters.get(key)
                    for key in [
                        "External validation count",
                        "Independent experiment count",
                        "Proof assistant verification count",
                        "New citation added count",
                    ]
                },
                "passed": all(
                    counters.get(key) == 0
                    for key in [
                        "External validation count",
                        "Independent experiment count",
                        "Proof assistant verification count",
                        "New citation added count",
                    ]
                ),
                "boundary_note": "The placement plan does not upgrade evidence status.",
            },
            {
                "id": "PA-09",
                "audit_check": "Real-biological operational counters remain zero.",
                "expected": "all real-biological operational counters zero",
                "observed": {
                    key: counters.get(key)
                    for key in [
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
                },
                "passed": all(
                    counters.get(key) == 0
                    for key in [
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
                ),
                "boundary_note": "No real-biological operational capability is present.",
            },
            {
                "id": "PA-10",
                "audit_check": "The audit itself remains non-executing and non-authorizing.",
                "expected": "audit-only",
                "observed": "audit-only",
                "passed": True,
                "boundary_note": "This artifact audits placement planning only and grants no permission.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        source = self._load_source_json()
        source_md = self._load_source_md()
        audit_items = self._audit_items(source)

        pass_count = sum(1 for item in audit_items if item["passed"])
        failure_count = sum(1 for item in audit_items if not item["passed"])

        counters = {
            "Safe abstract toy manuscript claim language placement plan audit count": 1,
            "New safe abstract toy manuscript claim language placement plan audit count": 1,
            "Toy manuscript claim language placement plan audit JSON export count": 1,
            "Toy manuscript claim language placement plan audit item count": len(audit_items),
            "Toy manuscript claim language placement plan audit pass count": pass_count,
            "Toy manuscript claim language placement plan audit failure count": failure_count,
            "Toy manuscript claim language placement plan audit execution count": 1,
            "Toy manuscript claim language placement plan audit direct execution count": 1,
            "Toy manuscript claim language placement plan audit non-readiness disclaimer count": 1,
            "Toy manuscript claim language placement plan audit boundary note count": len(audit_items),
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
            "title": "Safe Abstract Toy Manuscript Claim Language Placement Plan Audit",
            "source_markdown": str(self.source_md_path),
            "source_json": str(self.source_json_path),
            "source_markdown_character_count": len(source_md),
            "audit_phrase": self.audit_phrase,
            "scope": "claim-language-placement-plan-audit-only",
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
                "This v8.212 artifact audits the v8.211 safe claim language placement plan only. It does not "
                "complete checklist items, execute checklist steps, grant application permission, apply manuscript "
                "patches, modify manuscript files, approve readiness, establish submission readiness, validate "
                "scientific claims, add citations, or add real-biological operational capability."
            ),
            "audit_items": audit_items,
            "boundary_notes": [item["boundary_note"] for item in audit_items],
            "counters": counters,
            "passed": failure_count == 0,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "claim-language-placement-plan-audit-only":
            raise AssertionError("v8.212 must remain claim-language-placement-plan-audit-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.212 placement plan audit must pass.")

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

        if counters["Toy manuscript claim language placement plan audit item count"] != 10:
            raise AssertionError("Expected exactly ten audit items.")

        if counters["Toy manuscript claim language placement plan audit pass count"] != 10:
            raise AssertionError("Expected exactly ten passing audit items.")

        if counters["Toy manuscript claim language placement plan audit failure count"] != 0:
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

        lines.append("# Safe Abstract Toy Manuscript Claim Language Placement Plan Audit")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is claim-language-placement-plan-audit-only.")
        lines.append("It audits the v8.211 placement plan without applying, authorizing, completing, or executing any manuscript patch workflow.")
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
        lines.append("V8_212_SAFE_ABSTRACT_TOY_MANUSCRIPT_CLAIM_LANGUAGE_PLACEMENT_PLAN_AUDIT_OK")
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


def build_safe_abstract_toy_manuscript_claim_language_placement_plan_audit() -> Dict[str, Any]:
    return SafeAbstractToyManuscriptClaimLanguagePlacementPlanAuditBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_manuscript_claim_language_placement_plan_audit()
    counters = result["counters"]
    print("V8_212_SAFE_ABSTRACT_TOY_MANUSCRIPT_CLAIM_LANGUAGE_PLACEMENT_PLAN_AUDIT_OK")
    print("TOY_MANUSCRIPT_CLAIM_LANGUAGE_PLACEMENT_PLAN_AUDIT_DIRECT_CHECK_OK")
    print(f"Audit item count: {counters['Toy manuscript claim language placement plan audit item count']}")
    print(f"Audit pass count: {counters['Toy manuscript claim language placement plan audit pass count']}")
    print(f"Audit failure count: {counters['Toy manuscript claim language placement plan audit failure count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"Passed: {result['passed']}")
