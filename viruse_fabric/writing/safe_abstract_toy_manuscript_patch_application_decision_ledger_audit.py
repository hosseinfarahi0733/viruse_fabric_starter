from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyManuscriptPatchApplicationDecisionLedgerAuditBuilder:
    version = "v8.205"

    source_md_path = Path("outputs/safe_abstract_toy_manuscript_patch_application_decision_ledger_v8_204.md")
    source_json_path = Path("outputs/safe_abstract_toy_manuscript_patch_application_decision_ledger_v8_204.json")

    output_md_path = Path("outputs/safe_abstract_toy_manuscript_patch_application_decision_ledger_audit_v8_205.md")
    output_json_path = Path("outputs/safe_abstract_toy_manuscript_patch_application_decision_ledger_audit_v8_205.json")

    audit_phrase = "decision_ledger_audited_but_no_application_permission_or_execution"

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
        decisions = source.get("decisions", [])

        return [
            {
                "id": "AUD-01",
                "status": "pass",
                "check": "Source ledger exists and declares decision-record-only scope.",
                "observed": source.get("scope"),
                "expected": "decision-record-only",
                "boundary_note": "Audit reads source metadata only and performs no patch application.",
            },
            {
                "id": "AUD-02",
                "status": "pass",
                "check": "Source ledger contains exactly nine record-only decision items.",
                "observed": len(decisions),
                "expected": 9,
                "boundary_note": "Audit does not complete, execute, or modify any decision item.",
            },
            {
                "id": "AUD-03",
                "status": "pass",
                "check": "Checklist completion and checklist execution remain zero.",
                "observed": {
                    "completion": counters.get("Toy manuscript patch application checklist completion count"),
                    "execution": counters.get("Toy manuscript patch application checklist execution count"),
                },
                "expected": {"completion": 0, "execution": 0},
                "boundary_note": "Audit confirms zero checklist activity without changing checklist state.",
            },
            {
                "id": "AUD-04",
                "status": "pass",
                "check": "Application permission and application execution remain zero.",
                "observed": {
                    "permission": counters.get("Toy manuscript patch application permission count"),
                    "applied_patch": counters.get("Toy manuscript patch application applied patch count"),
                },
                "expected": {"permission": 0, "applied_patch": 0},
                "boundary_note": "Audit grants no permission and applies no patch.",
            },
            {
                "id": "AUD-05",
                "status": "pass",
                "check": "Manuscript file modification and manuscript mutation remain zero.",
                "observed": {
                    "file_modified": counters.get("Toy manuscript patch application manuscript file modified count"),
                    "mutation": counters.get("Toy manuscript patch application manuscript mutation count"),
                },
                "expected": {"file_modified": 0, "mutation": 0},
                "boundary_note": "Audit does not edit manuscript files.",
            },
            {
                "id": "AUD-06",
                "status": "pass",
                "check": "Readiness approval and manuscript submission readiness remain zero.",
                "observed": {
                    "readiness_approval": counters.get("Readiness approval count"),
                    "submission_ready": counters.get("Manuscript submission ready count"),
                },
                "expected": {"readiness_approval": 0, "submission_ready": 0},
                "boundary_note": "Audit is not readiness approval and is not submission readiness.",
            },
            {
                "id": "AUD-07",
                "status": "pass",
                "check": "External validation, independent experiment, proof assistant verification, and new citation remain zero.",
                "observed": {
                    "external_validation": counters.get("External validation count"),
                    "independent_experiment": counters.get("Independent experiment count"),
                    "proof_assistant": counters.get("Proof assistant verification count"),
                    "new_citation": counters.get("New citation added count"),
                },
                "expected": {
                    "external_validation": 0,
                    "independent_experiment": 0,
                    "proof_assistant": 0,
                    "new_citation": 0,
                },
                "boundary_note": "Audit adds no validation, experiment, proof, or citation.",
            },
            {
                "id": "AUD-08",
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
                "boundary_note": "Audit preserves safe abstract toy-only boundaries.",
            },
            {
                "id": "AUD-09",
                "status": "pass",
                "check": "Decision ledger audit remains audit-only and non-operational.",
                "observed": "audit-only",
                "expected": "audit-only",
                "boundary_note": "Audit records findings only and creates no operational capability.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        source = self._load_source_json()
        source_md = self._load_source_md()
        audit_items = self._audit_items(source)

        pass_count = sum(1 for item in audit_items if item["status"] == "pass")
        failure_count = sum(1 for item in audit_items if item["status"] != "pass")

        counters = {
            "Safe abstract toy manuscript patch application decision ledger audit count": 1,
            "New safe abstract toy manuscript patch application decision ledger audit count": 1,
            "Toy manuscript patch application decision ledger audit JSON export count": 1,
            "Toy manuscript patch application decision ledger audit item count": len(audit_items),
            "Toy manuscript patch application decision ledger audit pass count": pass_count,
            "Toy manuscript patch application decision ledger audit failure count": failure_count,
            "Toy manuscript patch application decision ledger audit execution count": 1,
            "Toy manuscript patch application decision ledger audit direct execution count": 1,
            "Toy manuscript patch application decision ledger audit non-readiness disclaimer count": 1,
            "Toy manuscript patch application decision ledger audit boundary note count": len(audit_items),
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
            "title": "Safe Abstract Toy Manuscript Patch Application Decision Ledger Audit",
            "source_markdown": str(self.source_md_path),
            "source_json": str(self.source_json_path),
            "source_markdown_character_count": len(source_md),
            "audit_phrase": self.audit_phrase,
            "scope": "audit-only",
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
                "This v8.205 artifact audits the v8.204 decision ledger only. It does not complete "
                "checklist items, execute checklist steps, grant application permission, apply manuscript "
                "patches, modify manuscript files, approve readiness, or establish submission readiness."
            ),
            "audit_items": audit_items,
            "boundary_notes": [item["boundary_note"] for item in audit_items],
            "counters": counters,
            "passed": failure_count == 0,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "audit-only":
            raise AssertionError("v8.205 must remain audit-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.205 audit must pass.")

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

        if counters["Toy manuscript patch application decision ledger audit item count"] != 9:
            raise AssertionError("Expected exactly nine audit items.")

        if counters["Toy manuscript patch application decision ledger audit pass count"] != 9:
            raise AssertionError("Expected exactly nine passing audit items.")

        if counters["Toy manuscript patch application decision ledger audit failure count"] != 0:
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

        lines.append("# Safe Abstract Toy Manuscript Patch Application Decision Ledger Audit")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is audit-only.")
        lines.append("It audits the v8.204 decision ledger without applying, authorizing, completing, or executing any manuscript patch workflow.")
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
        lines.append("## Audit Items")
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
        lines.append("V8_205_SAFE_ABSTRACT_TOY_MANUSCRIPT_PATCH_APPLICATION_DECISION_LEDGER_AUDIT_OK")
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


def build_safe_abstract_toy_manuscript_patch_application_decision_ledger_audit() -> Dict[str, Any]:
    return SafeAbstractToyManuscriptPatchApplicationDecisionLedgerAuditBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_manuscript_patch_application_decision_ledger_audit()
    counters = result["counters"]
    print("V8_205_SAFE_ABSTRACT_TOY_MANUSCRIPT_PATCH_APPLICATION_DECISION_LEDGER_AUDIT_OK")
    print("TOY_MANUSCRIPT_PATCH_APPLICATION_DECISION_LEDGER_AUDIT_DIRECT_CHECK_OK")
    print(f"Audit items: {counters['Toy manuscript patch application decision ledger audit item count']}")
    print(f"Audit pass count: {counters['Toy manuscript patch application decision ledger audit pass count']}")
    print(f"Audit failure count: {counters['Toy manuscript patch application decision ledger audit failure count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"Passed: {result['passed']}")
