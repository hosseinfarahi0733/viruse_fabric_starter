from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyManuscriptClaimLanguagePackageAuditBuilder:
    version = "v8.210"

    source_md_path = Path("outputs/safe_abstract_toy_manuscript_claim_language_package_v8_209.md")
    source_json_path = Path("outputs/safe_abstract_toy_manuscript_claim_language_package_v8_209.json")

    output_md_path = Path("outputs/safe_abstract_toy_manuscript_claim_language_package_audit_v8_210.md")
    output_json_path = Path("outputs/safe_abstract_toy_manuscript_claim_language_package_audit_v8_210.json")

    audit_phrase = "safe_claim_language_audited_but_no_readiness_or_real_bio_claims"

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
        safe_items = source.get("safe_language_items", [])
        blocked_items = source.get("blocked_language_items", [])
        safe_text = " ".join(item.get("language", "") for item in safe_items)
        blocked_text = " ".join(item.get("blocked_language", "") for item in blocked_items)

        return [
            {
                "id": "LA-01",
                "audit_check": "Source scope remains claim-language-package-only.",
                "expected": "claim-language-package-only",
                "observed": source.get("scope"),
                "passed": source.get("scope") == "claim-language-package-only",
                "boundary_note": "The source package is wording-only and does not apply manuscript patches.",
            },
            {
                "id": "LA-02",
                "audit_check": "Source safe language item count is exactly eight.",
                "expected": 8,
                "observed": len(safe_items),
                "passed": len(safe_items) == 8 and counters.get("Toy manuscript claim language package safe language item count") == 8,
                "boundary_note": "Safe language package size is stable.",
            },
            {
                "id": "LA-03",
                "audit_check": "Source blocked language item count is exactly nine.",
                "expected": 9,
                "observed": len(blocked_items),
                "passed": len(blocked_items) == 9 and counters.get("Toy manuscript claim language package blocked language item count") == 9,
                "boundary_note": "Blocked language coverage is stable.",
            },
            {
                "id": "LA-04",
                "audit_check": "Allowed contribution language remains governance-only.",
                "expected": "governance pipeline and claim boundaries, not validation or readiness",
                "observed": safe_text,
                "passed": (
                    "governance pipeline" in safe_text
                    and "claim boundaries" in safe_text
                    and "submission readiness" in safe_text
                    and "does not establish external validation" in safe_text
                ),
                "boundary_note": "Contribution wording stays limited to governance and boundaries.",
            },
            {
                "id": "LA-05",
                "audit_check": "Safety scope language excludes real-biological operation.",
                "expected": "synthetic, abstract, unitless, non-operational toy artifacts only",
                "observed": safe_text,
                "passed": (
                    "synthetic" in safe_text
                    and "abstract" in safe_text
                    and "unitless" in safe_text
                    and "non-operational" in safe_text
                    and "does not model real pathogens" in safe_text
                ),
                "boundary_note": "Real-biological operational claims remain explicitly excluded.",
            },
            {
                "id": "LA-06",
                "audit_check": "Blocked language includes submission readiness, validation, experiment, proof, citation, patch, and real-bio exclusions.",
                "expected": "all major prohibited families covered",
                "observed": blocked_text,
                "passed": all(
                    phrase in blocked_text
                    for phrase in [
                        "ready for submission",
                        "externally validated",
                        "independently experimentally verified",
                        "formally proved",
                        "new citation-supported claims",
                        "patches have been applied",
                        "real pathogens or real receptors",
                        "predicts host range",
                        "optimizes infectivity or immune evasion",
                    ]
                ),
                "boundary_note": "Blocked wording covers the current major overclaim families.",
            },
            {
                "id": "LA-07",
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
                "boundary_note": "No patch application or readiness claim is introduced.",
            },
            {
                "id": "LA-08",
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
                "boundary_note": "No external validation, independent experiment, proof, or citation upgrade is claimed.",
            },
            {
                "id": "LA-09",
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
                "id": "LA-10",
                "audit_check": "The audit itself remains non-executing and non-authorizing.",
                "expected": "audit-only",
                "observed": "audit-only",
                "passed": True,
                "boundary_note": "This artifact audits language only and grants no permission.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        source = self._load_source_json()
        source_md = self._load_source_md()
        audit_items = self._audit_items(source)

        pass_count = sum(1 for item in audit_items if item["passed"])
        failure_count = sum(1 for item in audit_items if not item["passed"])

        counters = {
            "Safe abstract toy manuscript claim language package audit count": 1,
            "New safe abstract toy manuscript claim language package audit count": 1,
            "Toy manuscript claim language package audit JSON export count": 1,
            "Toy manuscript claim language package audit item count": len(audit_items),
            "Toy manuscript claim language package audit pass count": pass_count,
            "Toy manuscript claim language package audit failure count": failure_count,
            "Toy manuscript claim language package audit execution count": 1,
            "Toy manuscript claim language package audit direct execution count": 1,
            "Toy manuscript claim language package audit non-readiness disclaimer count": 1,
            "Toy manuscript claim language package audit boundary note count": len(audit_items),
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
            "title": "Safe Abstract Toy Manuscript Claim Language Package Audit",
            "source_markdown": str(self.source_md_path),
            "source_json": str(self.source_json_path),
            "source_markdown_character_count": len(source_md),
            "audit_phrase": self.audit_phrase,
            "scope": "claim-language-package-audit-only",
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
                "This v8.210 artifact audits the v8.209 safe claim language package only. It does not complete "
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
        if report["scope"] != "claim-language-package-audit-only":
            raise AssertionError("v8.210 must remain claim-language-package-audit-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.210 claim language package audit must pass.")

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

        if counters["Toy manuscript claim language package audit item count"] != 10:
            raise AssertionError("Expected exactly ten audit items.")

        if counters["Toy manuscript claim language package audit pass count"] != 10:
            raise AssertionError("Expected exactly ten passing audit items.")

        if counters["Toy manuscript claim language package audit failure count"] != 0:
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

        lines.append("# Safe Abstract Toy Manuscript Claim Language Package Audit")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is claim-language-package-audit-only.")
        lines.append("It audits the v8.209 safe claim language package without applying, authorizing, completing, or executing any manuscript patch workflow.")
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
        lines.append("V8_210_SAFE_ABSTRACT_TOY_MANUSCRIPT_CLAIM_LANGUAGE_PACKAGE_AUDIT_OK")
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


def build_safe_abstract_toy_manuscript_claim_language_package_audit() -> Dict[str, Any]:
    return SafeAbstractToyManuscriptClaimLanguagePackageAuditBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_manuscript_claim_language_package_audit()
    counters = result["counters"]
    print("V8_210_SAFE_ABSTRACT_TOY_MANUSCRIPT_CLAIM_LANGUAGE_PACKAGE_AUDIT_OK")
    print("TOY_MANUSCRIPT_CLAIM_LANGUAGE_PACKAGE_AUDIT_DIRECT_CHECK_OK")
    print(f"Audit item count: {counters['Toy manuscript claim language package audit item count']}")
    print(f"Audit pass count: {counters['Toy manuscript claim language package audit pass count']}")
    print(f"Audit failure count: {counters['Toy manuscript claim language package audit failure count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"Passed: {result['passed']}")
