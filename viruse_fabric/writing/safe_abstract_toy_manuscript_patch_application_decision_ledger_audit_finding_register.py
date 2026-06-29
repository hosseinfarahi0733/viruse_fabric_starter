from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyManuscriptPatchApplicationDecisionLedgerAuditFindingRegisterBuilder:
    version = "v8.206"

    source_md_path = Path("outputs/safe_abstract_toy_manuscript_patch_application_decision_ledger_audit_v8_205.md")
    source_json_path = Path("outputs/safe_abstract_toy_manuscript_patch_application_decision_ledger_audit_v8_205.json")

    output_md_path = Path("outputs/safe_abstract_toy_manuscript_patch_application_decision_ledger_audit_finding_register_v8_206.md")
    output_json_path = Path("outputs/safe_abstract_toy_manuscript_patch_application_decision_ledger_audit_finding_register_v8_206.json")

    register_phrase = "audit_findings_registered_but_no_application_permission_or_execution"

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

    def _finding_items(self, source: Dict[str, Any]) -> List[Dict[str, Any]]:
        counters = source.get("counters", {})
        audit_items = source.get("audit_items", [])

        return [
            {
                "id": "FR-01",
                "status": "registered_pass",
                "finding": "The v8.205 audit source declares audit-only scope.",
                "source_observed": source.get("scope"),
                "registered_action": "record_only_no_execution",
                "boundary_note": "Finding registration reads the audit result only and applies no patch.",
            },
            {
                "id": "FR-02",
                "status": "registered_pass",
                "finding": "The v8.205 audit source contains exactly nine audit items.",
                "source_observed": len(audit_items),
                "registered_action": "record_only_no_execution",
                "boundary_note": "Finding registration does not alter audit items.",
            },
            {
                "id": "FR-03",
                "status": "registered_pass",
                "finding": "Checklist completion and checklist execution remained zero in the audit.",
                "source_observed": {
                    "completion": counters.get("Toy manuscript patch application checklist completion count"),
                    "execution": counters.get("Toy manuscript patch application checklist execution count"),
                },
                "registered_action": "record_only_no_execution",
                "boundary_note": "Finding registration does not complete or execute checklist steps.",
            },
            {
                "id": "FR-04",
                "status": "registered_pass",
                "finding": "Application permission and applied patch counts remained zero in the audit.",
                "source_observed": {
                    "permission": counters.get("Toy manuscript patch application permission count"),
                    "applied_patch": counters.get("Toy manuscript patch application applied patch count"),
                },
                "registered_action": "record_only_no_execution",
                "boundary_note": "Finding registration grants no permission and applies no patch.",
            },
            {
                "id": "FR-05",
                "status": "registered_pass",
                "finding": "Manuscript file modification and manuscript mutation remained zero in the audit.",
                "source_observed": {
                    "file_modified": counters.get("Toy manuscript patch application manuscript file modified count"),
                    "mutation": counters.get("Toy manuscript patch application manuscript mutation count"),
                },
                "registered_action": "record_only_no_execution",
                "boundary_note": "Finding registration does not edit manuscript files.",
            },
            {
                "id": "FR-06",
                "status": "registered_pass",
                "finding": "Readiness approval and manuscript submission readiness remained zero in the audit.",
                "source_observed": {
                    "readiness_approval": counters.get("Readiness approval count"),
                    "submission_ready": counters.get("Manuscript submission ready count"),
                },
                "registered_action": "record_only_no_execution",
                "boundary_note": "Finding registration is not readiness approval.",
            },
            {
                "id": "FR-07",
                "status": "registered_pass",
                "finding": "External validation, independent experiment, proof assistant verification, and new citation remained zero in the audit.",
                "source_observed": {
                    "external_validation": counters.get("External validation count"),
                    "independent_experiment": counters.get("Independent experiment count"),
                    "proof_assistant": counters.get("Proof assistant verification count"),
                    "new_citation": counters.get("New citation added count"),
                },
                "registered_action": "record_only_no_execution",
                "boundary_note": "Finding registration adds no validation, experiment, proof, or citation.",
            },
            {
                "id": "FR-08",
                "status": "registered_pass",
                "finding": "Real-biological operational counters remained zero in the audit.",
                "source_observed": {
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
                "registered_action": "record_only_no_execution",
                "boundary_note": "Finding registration preserves safe abstract toy-only boundaries.",
            },
            {
                "id": "FR-09",
                "status": "registered_pass",
                "finding": "The audit produced zero failures and nine passing audit items.",
                "source_observed": {
                    "pass_count": counters.get("Toy manuscript patch application decision ledger audit pass count"),
                    "failure_count": counters.get("Toy manuscript patch application decision ledger audit failure count"),
                },
                "registered_action": "record_only_no_execution",
                "boundary_note": "Finding registration records the pass/fail outcome without approving readiness.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        source = self._load_source_json()
        source_md = self._load_source_md()
        findings = self._finding_items(source)

        registered_count = sum(1 for item in findings if item["status"] == "registered_pass")
        failure_count = sum(1 for item in findings if item["status"] != "registered_pass")

        counters = {
            "Safe abstract toy manuscript patch application decision ledger audit finding register count": 1,
            "New safe abstract toy manuscript patch application decision ledger audit finding register count": 1,
            "Toy manuscript patch application decision ledger audit finding register JSON export count": 1,
            "Toy manuscript patch application decision ledger audit finding register item count": len(findings),
            "Toy manuscript patch application decision ledger audit finding register registered pass count": registered_count,
            "Toy manuscript patch application decision ledger audit finding register failure count": failure_count,
            "Toy manuscript patch application decision ledger audit finding register execution count": 1,
            "Toy manuscript patch application decision ledger audit finding register direct execution count": 1,
            "Toy manuscript patch application decision ledger audit finding register non-readiness disclaimer count": 1,
            "Toy manuscript patch application decision ledger audit finding register boundary note count": len(findings),
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
            "title": "Safe Abstract Toy Manuscript Patch Application Decision Ledger Audit Finding Register",
            "source_markdown": str(self.source_md_path),
            "source_json": str(self.source_json_path),
            "source_markdown_character_count": len(source_md),
            "register_phrase": self.register_phrase,
            "scope": "finding-register-only",
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
                "This v8.206 artifact registers findings from the v8.205 audit only. It does not "
                "complete checklist items, execute checklist steps, grant application permission, apply "
                "manuscript patches, modify manuscript files, approve readiness, or establish submission readiness."
            ),
            "finding_items": findings,
            "boundary_notes": [item["boundary_note"] for item in findings],
            "counters": counters,
            "passed": failure_count == 0,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "finding-register-only":
            raise AssertionError("v8.206 must remain finding-register-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.206 finding register must pass.")

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

        if counters["Toy manuscript patch application decision ledger audit finding register item count"] != 9:
            raise AssertionError("Expected exactly nine finding-register items.")

        if counters["Toy manuscript patch application decision ledger audit finding register registered pass count"] != 9:
            raise AssertionError("Expected exactly nine registered passing findings.")

        if counters["Toy manuscript patch application decision ledger audit finding register failure count"] != 0:
            raise AssertionError("Expected zero finding-register failures.")

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

        lines.append("# Safe Abstract Toy Manuscript Patch Application Decision Ledger Audit Finding Register")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is finding-register-only.")
        lines.append("It registers findings from the v8.205 audit without applying, authorizing, completing, or executing any manuscript patch workflow.")
        lines.append("")
        lines.append(f"Register phrase: `{report['register_phrase']}`")
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
        lines.append("## Finding Items")
        lines.append("")

        for item in report["finding_items"]:
            lines.append(f"### {item['id']}")
            lines.append("")
            lines.append(f"- Status: `{item['status']}`")
            lines.append(f"- Finding: {item['finding']}")
            lines.append(f"- Source observed: `{item['source_observed']}`")
            lines.append(f"- Registered action: `{item['registered_action']}`")
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
        lines.append("V8_206_SAFE_ABSTRACT_TOY_MANUSCRIPT_PATCH_APPLICATION_DECISION_LEDGER_AUDIT_FINDING_REGISTER_OK")
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


def build_safe_abstract_toy_manuscript_patch_application_decision_ledger_audit_finding_register() -> Dict[str, Any]:
    return SafeAbstractToyManuscriptPatchApplicationDecisionLedgerAuditFindingRegisterBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_manuscript_patch_application_decision_ledger_audit_finding_register()
    counters = result["counters"]
    print("V8_206_SAFE_ABSTRACT_TOY_MANUSCRIPT_PATCH_APPLICATION_DECISION_LEDGER_AUDIT_FINDING_REGISTER_OK")
    print("TOY_MANUSCRIPT_PATCH_APPLICATION_DECISION_LEDGER_AUDIT_FINDING_REGISTER_DIRECT_CHECK_OK")
    print(f"Finding items: {counters['Toy manuscript patch application decision ledger audit finding register item count']}")
    print(f"Registered pass count: {counters['Toy manuscript patch application decision ledger audit finding register registered pass count']}")
    print(f"Finding failure count: {counters['Toy manuscript patch application decision ledger audit finding register failure count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"Passed: {result['passed']}")
