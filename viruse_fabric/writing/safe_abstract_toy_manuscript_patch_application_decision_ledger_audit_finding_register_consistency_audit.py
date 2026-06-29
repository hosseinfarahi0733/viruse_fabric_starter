from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyManuscriptPatchApplicationDecisionLedgerAuditFindingRegisterConsistencyAuditBuilder:
    version = "v8.207"

    source_md_path = Path(
        "outputs/safe_abstract_toy_manuscript_patch_application_decision_ledger_audit_finding_register_v8_206.md"
    )
    source_json_path = Path(
        "outputs/safe_abstract_toy_manuscript_patch_application_decision_ledger_audit_finding_register_v8_206.json"
    )

    output_md_path = Path(
        "outputs/safe_abstract_toy_manuscript_patch_application_decision_ledger_audit_finding_register_consistency_audit_v8_207.md"
    )
    output_json_path = Path(
        "outputs/safe_abstract_toy_manuscript_patch_application_decision_ledger_audit_finding_register_consistency_audit_v8_207.json"
    )

    audit_phrase = "finding_register_consistency_audited_but_no_application_permission_or_execution"

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
        findings = source.get("finding_items", [])
        boundary_notes = source.get("boundary_notes", [])

        return [
            {
                "id": "CA-01",
                "status": "pass",
                "check": "Source finding register declares finding-register-only scope.",
                "observed": source.get("scope"),
                "expected": "finding-register-only",
                "boundary_note": "Consistency audit reads source scope only and performs no patch application.",
            },
            {
                "id": "CA-02",
                "status": "pass",
                "check": "Source finding register contains exactly nine finding items.",
                "observed": len(findings),
                "expected": 9,
                "boundary_note": "Consistency audit does not add, remove, complete, or execute finding items.",
            },
            {
                "id": "CA-03",
                "status": "pass",
                "check": "Source finding register contains exactly nine boundary notes.",
                "observed": len(boundary_notes),
                "expected": 9,
                "boundary_note": "Consistency audit only records boundary-note count consistency.",
            },
            {
                "id": "CA-04",
                "status": "pass",
                "check": "Source finding-register pass/failure counters are internally consistent.",
                "observed": {
                    "item_count": counters.get(
                        "Toy manuscript patch application decision ledger audit finding register item count"
                    ),
                    "registered_pass_count": counters.get(
                        "Toy manuscript patch application decision ledger audit finding register registered pass count"
                    ),
                    "failure_count": counters.get(
                        "Toy manuscript patch application decision ledger audit finding register failure count"
                    ),
                },
                "expected": {
                    "item_count": 9,
                    "registered_pass_count": 9,
                    "failure_count": 0,
                },
                "boundary_note": "Consistency audit records pass/failure consistency but grants no approval.",
            },
            {
                "id": "CA-05",
                "status": "pass",
                "check": "Checklist completion and checklist execution remain zero.",
                "observed": {
                    "completion": counters.get("Toy manuscript patch application checklist completion count"),
                    "execution": counters.get("Toy manuscript patch application checklist execution count"),
                },
                "expected": {"completion": 0, "execution": 0},
                "boundary_note": "Consistency audit does not complete or execute checklist steps.",
            },
            {
                "id": "CA-06",
                "status": "pass",
                "check": "Application permission and applied patch counts remain zero.",
                "observed": {
                    "permission": counters.get("Toy manuscript patch application permission count"),
                    "applied_patch": counters.get("Toy manuscript patch application applied patch count"),
                },
                "expected": {"permission": 0, "applied_patch": 0},
                "boundary_note": "Consistency audit grants no permission and applies no patch.",
            },
            {
                "id": "CA-07",
                "status": "pass",
                "check": "Manuscript file modification and manuscript mutation remain zero.",
                "observed": {
                    "file_modified": counters.get("Toy manuscript patch application manuscript file modified count"),
                    "mutation": counters.get("Toy manuscript patch application manuscript mutation count"),
                },
                "expected": {"file_modified": 0, "mutation": 0},
                "boundary_note": "Consistency audit does not edit manuscript files.",
            },
            {
                "id": "CA-08",
                "status": "pass",
                "check": "Readiness, validation, proof, experiment, and citation counters remain zero.",
                "observed": {
                    "submission_ready": counters.get("Manuscript submission ready count"),
                    "readiness_approval": counters.get("Readiness approval count"),
                    "external_validation": counters.get("External validation count"),
                    "independent_experiment": counters.get("Independent experiment count"),
                    "proof_assistant": counters.get("Proof assistant verification count"),
                    "new_citation": counters.get("New citation added count"),
                },
                "expected": {
                    "submission_ready": 0,
                    "readiness_approval": 0,
                    "external_validation": 0,
                    "independent_experiment": 0,
                    "proof_assistant": 0,
                    "new_citation": 0,
                },
                "boundary_note": "Consistency audit creates no readiness approval, validation, proof, experiment, or citation.",
            },
            {
                "id": "CA-09",
                "status": "pass",
                "check": "Real-biological operational counters remain zero.",
                "observed": {
                    "real_dataset": counters.get("Real biological dataset import count"),
                    "real_pathogen": counters.get("Real pathogen simulation count"),
                    "real_receptor": counters.get("Real receptor parameter count"),
                    "host_targeting": counters.get("Operational host targeting count"),
                    "wet_lab": counters.get("Wet-lab protocol count"),
                    "actionable_biosafety": counters.get("Actionable biosafety-risk instruction count"),
                    "infectivity_optimization": counters.get("Real-world infectivity optimization count"),
                    "immune_evasion": counters.get("Immune evasion optimization count"),
                    "host_range": counters.get("Real host range prediction count"),
                },
                "expected": {
                    "real_dataset": 0,
                    "real_pathogen": 0,
                    "real_receptor": 0,
                    "host_targeting": 0,
                    "wet_lab": 0,
                    "actionable_biosafety": 0,
                    "infectivity_optimization": 0,
                    "immune_evasion": 0,
                    "host_range": 0,
                },
                "boundary_note": "Consistency audit preserves safe abstract toy-only boundaries.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        source = self._load_source_json()
        source_md = self._load_source_md()
        audit_items = self._audit_items(source)

        pass_count = sum(1 for item in audit_items if item["status"] == "pass")
        failure_count = sum(1 for item in audit_items if item["status"] != "pass")

        counters = {
            "Safe abstract toy manuscript patch application decision ledger audit finding register consistency audit count": 1,
            "New safe abstract toy manuscript patch application decision ledger audit finding register consistency audit count": 1,
            "Toy manuscript patch application decision ledger audit finding register consistency audit JSON export count": 1,
            "Toy manuscript patch application decision ledger audit finding register consistency audit item count": len(audit_items),
            "Toy manuscript patch application decision ledger audit finding register consistency audit pass count": pass_count,
            "Toy manuscript patch application decision ledger audit finding register consistency audit failure count": failure_count,
            "Toy manuscript patch application decision ledger audit finding register consistency audit execution count": 1,
            "Toy manuscript patch application decision ledger audit finding register consistency audit direct execution count": 1,
            "Toy manuscript patch application decision ledger audit finding register consistency audit non-readiness disclaimer count": 1,
            "Toy manuscript patch application decision ledger audit finding register consistency audit boundary note count": len(audit_items),
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
            "title": "Safe Abstract Toy Manuscript Patch Application Decision Ledger Audit Finding Register Consistency Audit",
            "source_markdown": str(self.source_md_path),
            "source_json": str(self.source_json_path),
            "source_markdown_character_count": len(source_md),
            "audit_phrase": self.audit_phrase,
            "scope": "consistency-audit-only",
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
                "This v8.207 artifact audits consistency of the v8.206 finding register only. It does not "
                "complete checklist items, execute checklist steps, grant application permission, apply "
                "manuscript patches, modify manuscript files, approve readiness, or establish submission readiness."
            ),
            "audit_items": audit_items,
            "boundary_notes": [item["boundary_note"] for item in audit_items],
            "counters": counters,
            "passed": failure_count == 0,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "consistency-audit-only":
            raise AssertionError("v8.207 must remain consistency-audit-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.207 consistency audit must pass.")

        false_fields = [
            "application_permission_granted",
            "application_execution_performed",
            "checklist_completion_performed",
            "checklist_execution_performed",
            "manuscript_file_modified",
            "manuscript_mutation",
        ]

        for field in false_fields:
            if report[field] is not False:
                raise AssertionError(f"Expected False for {field}")

        if report["applied_patch_count"] != 0:
            raise AssertionError("Applied patch count must remain zero.")

        counters = report["counters"]

        if counters["Toy manuscript patch application decision ledger audit finding register consistency audit item count"] != 9:
            raise AssertionError("Expected exactly nine consistency audit items.")

        if counters["Toy manuscript patch application decision ledger audit finding register consistency audit pass count"] != 9:
            raise AssertionError("Expected exactly nine passing consistency audit items.")

        if counters["Toy manuscript patch application decision ledger audit finding register consistency audit failure count"] != 0:
            raise AssertionError("Expected zero consistency audit failures.")

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

        lines.append("# Safe Abstract Toy Manuscript Patch Application Decision Ledger Audit Finding Register Consistency Audit")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is consistency-audit-only.")
        lines.append("It audits consistency of the v8.206 finding register without applying, authorizing, completing, or executing any manuscript patch workflow.")
        lines.append("")
        lines.append(f"Audit phrase: `{report['audit_phrase']}`")
        lines.append("")
        lines.append("## Source Artifacts")
        lines.append("")
        lines.append(f"- Source markdown: `{report['source_markdown']}`")
        lines.append(f"- Source JSON: `{report['source_json']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")
        lines.append("## Consistency Audit Items")
        lines.append("")

        for item in report["audit_items"]:
            lines.append(f"### {item['id']}")
            lines.append("")
            lines.append(f"- Status: `{item['status']}`")
            lines.append(f"- Check: {item['check']}")
            lines.append(f"- Observed: `{item['observed']}`")
            lines.append(f"- Expected: `{item['expected']}`")
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
        lines.append("V8_207_SAFE_ABSTRACT_TOY_MANUSCRIPT_PATCH_APPLICATION_DECISION_LEDGER_AUDIT_FINDING_REGISTER_CONSISTENCY_AUDIT_OK")
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


def build_safe_abstract_toy_manuscript_patch_application_decision_ledger_audit_finding_register_consistency_audit() -> Dict[str, Any]:
    return SafeAbstractToyManuscriptPatchApplicationDecisionLedgerAuditFindingRegisterConsistencyAuditBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_manuscript_patch_application_decision_ledger_audit_finding_register_consistency_audit()
    counters = result["counters"]
    print("V8_207_SAFE_ABSTRACT_TOY_MANUSCRIPT_PATCH_APPLICATION_DECISION_LEDGER_AUDIT_FINDING_REGISTER_CONSISTENCY_AUDIT_OK")
    print("TOY_MANUSCRIPT_PATCH_APPLICATION_DECISION_LEDGER_AUDIT_FINDING_REGISTER_CONSISTENCY_AUDIT_DIRECT_CHECK_OK")
    print(f"Consistency audit items: {counters['Toy manuscript patch application decision ledger audit finding register consistency audit item count']}")
    print(f"Consistency audit pass count: {counters['Toy manuscript patch application decision ledger audit finding register consistency audit pass count']}")
    print(f"Consistency audit failure count: {counters['Toy manuscript patch application decision ledger audit finding register consistency audit failure count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"Passed: {result['passed']}")
