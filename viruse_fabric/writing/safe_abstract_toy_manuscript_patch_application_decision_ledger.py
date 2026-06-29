from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyManuscriptPatchApplicationDecisionLedgerBuilder:
    version = "v8.204"

    source_md_path = Path("outputs/safe_abstract_toy_manuscript_patch_application_checklist_audit_v8_203.md")
    source_json_path = Path("outputs/safe_abstract_toy_manuscript_patch_application_checklist_audit_v8_203.json")

    output_md_path = Path("outputs/safe_abstract_toy_manuscript_patch_application_decision_ledger_v8_204.md")
    output_json_path = Path("outputs/safe_abstract_toy_manuscript_patch_application_decision_ledger_v8_204.json")

    decision_phrase = "decision_ledger_recorded_but_no_application_permission_or_execution"

    def _load_source_json(self) -> Dict[str, Any]:
        if not self.source_json_path.exists():
            raise FileNotFoundError(f"Missing required source JSON: {self.source_json_path}")

        with self.source_json_path.open("r", encoding="utf-8") as f:
            payload = json.load(f)

        if not isinstance(payload, dict):
            raise ValueError("Source JSON must be an object/dict.")

        return payload

    def _require_source_markdown(self) -> str:
        if not self.source_md_path.exists():
            raise FileNotFoundError(f"Missing required source markdown: {self.source_md_path}")

        return self.source_md_path.read_text(encoding="utf-8")

    def _decision_items(self) -> List[Dict[str, Any]]:
        return [
            {
                "id": "DL-01",
                "status": "accepted_record_only",
                "decision": "Record v8.203 checklist-audit lineage as the only direct source for this ledger.",
                "permission_granted": False,
                "execution_allowed": False,
                "manuscript_mutation_allowed": False,
                "boundary_note": "Lineage recording is metadata-only and does not apply any patch.",
            },
            {
                "id": "DL-02",
                "status": "accepted_record_only",
                "decision": "Preserve zero checklist completion from the audited v8.203 source state.",
                "permission_granted": False,
                "execution_allowed": False,
                "manuscript_mutation_allowed": False,
                "boundary_note": "No checklist item is completed by this ledger.",
            },
            {
                "id": "DL-03",
                "status": "accepted_record_only",
                "decision": "Preserve zero checklist execution from the audited v8.203 source state.",
                "permission_granted": False,
                "execution_allowed": False,
                "manuscript_mutation_allowed": False,
                "boundary_note": "No checklist step is executed by this ledger.",
            },
            {
                "id": "DL-04",
                "status": "accepted_record_only",
                "decision": "Preserve zero manuscript patch application permission.",
                "permission_granted": False,
                "execution_allowed": False,
                "manuscript_mutation_allowed": False,
                "boundary_note": "This ledger records decisions but grants no application permission.",
            },
            {
                "id": "DL-05",
                "status": "accepted_record_only",
                "decision": "Preserve zero applied manuscript patches.",
                "permission_granted": False,
                "execution_allowed": False,
                "manuscript_mutation_allowed": False,
                "boundary_note": "No manuscript patch is applied, staged, simulated as applied, or authorized.",
            },
            {
                "id": "DL-06",
                "status": "accepted_record_only",
                "decision": "Preserve zero manuscript file modifications and zero manuscript mutation.",
                "permission_granted": False,
                "execution_allowed": False,
                "manuscript_mutation_allowed": False,
                "boundary_note": "The ledger does not edit any manuscript file.",
            },
            {
                "id": "DL-07",
                "status": "accepted_record_only",
                "decision": "Preserve zero readiness approval and zero manuscript submission readiness.",
                "permission_granted": False,
                "execution_allowed": False,
                "manuscript_mutation_allowed": False,
                "boundary_note": "Decision recording is not approval and is not submission readiness.",
            },
            {
                "id": "DL-08",
                "status": "accepted_record_only",
                "decision": "Preserve zero external validation, zero independent experiment, zero proof assistant verification, and zero new citation.",
                "permission_granted": False,
                "execution_allowed": False,
                "manuscript_mutation_allowed": False,
                "boundary_note": "This ledger adds no validation, experiment, proof, or citation.",
            },
            {
                "id": "DL-09",
                "status": "accepted_record_only",
                "decision": "Preserve safe abstract toy-only boundaries and zero real-biological operational capability.",
                "permission_granted": False,
                "execution_allowed": False,
                "manuscript_mutation_allowed": False,
                "boundary_note": "All content remains synthetic, abstract, unitless, non-operational, and toy-only.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        source_json = self._load_source_json()
        source_md = self._require_source_markdown()
        decisions = self._decision_items()

        accepted_count = sum(1 for item in decisions if item["status"] == "accepted_record_only")
        rejected_count = sum(1 for item in decisions if item["status"].startswith("rejected"))

        boundary_notes = [item["boundary_note"] for item in decisions]

        counters = {
            "Safe abstract toy manuscript patch application decision ledger count": 1,
            "New safe abstract toy manuscript patch application decision ledger count": 1,
            "Toy manuscript patch application decision ledger JSON export count": 1,
            "Toy manuscript patch application decision ledger item count": len(decisions),
            "Toy manuscript patch application decision ledger accepted decision count": accepted_count,
            "Toy manuscript patch application decision ledger rejected decision count": rejected_count,
            "Toy manuscript patch application decision ledger execution count": 1,
            "Toy manuscript patch application checklist completion count": 0,
            "Toy manuscript patch application checklist execution count": 0,
            "Toy manuscript patch application permission count": 0,
            "Toy manuscript patch application applied patch count": 0,
            "Toy manuscript patch application manuscript file modified count": 0,
            "Toy manuscript patch application manuscript mutation count": 0,
            "Toy manuscript patch application decision ledger non-readiness disclaimer count": 1,
            "Toy manuscript patch application decision ledger boundary note count": len(boundary_notes),
            "Toy manuscript patch application decision ledger direct execution count": 1,
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
            "title": "Safe Abstract Toy Manuscript Patch Application Decision Ledger",
            "source_markdown": str(self.source_md_path),
            "source_json": str(self.source_json_path),
            "source_json_top_level_keys": sorted(source_json.keys()),
            "source_markdown_character_count": len(source_md),
            "decision_phrase": self.decision_phrase,
            "scope": "decision-record-only",
            "safe_abstract_toy_only": True,
            "synthetic_only": True,
            "abstract_graphs_only": True,
            "unitless_parameters_only": True,
            "non_operational_only": True,
            "manuscript_file_modified": False,
            "manuscript_mutation": False,
            "application_permission_granted": False,
            "application_execution_performed": False,
            "checklist_completion_performed": False,
            "checklist_execution_performed": False,
            "applied_patch_count": 0,
            "non_readiness_disclaimer": (
                "This v8.204 ledger records audited decisions only. It does not complete checklist "
                "items, execute checklist steps, grant application permission, apply manuscript patches, "
                "modify manuscript files, approve readiness, or establish manuscript submission readiness."
            ),
            "decisions": decisions,
            "boundary_notes": boundary_notes,
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "decision-record-only":
            raise AssertionError("v8.204 must remain decision-record-only.")

        zero_fields = [
            "manuscript_file_modified",
            "manuscript_mutation",
            "application_permission_granted",
            "application_execution_performed",
            "checklist_completion_performed",
            "checklist_execution_performed",
        ]

        for field in zero_fields:
            if report[field] is not False:
                raise AssertionError(f"Expected False for {field}")

        if report["applied_patch_count"] != 0:
            raise AssertionError("Applied patch count must remain zero.")

        counters = report["counters"]

        required_zero_counters = [
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

        for key in required_zero_counters:
            if counters.get(key) != 0:
                raise AssertionError(f"Counter must remain zero: {key}")

        if counters["Toy manuscript patch application decision ledger item count"] != 9:
            raise AssertionError("Expected exactly 9 decision ledger items.")

        if counters["Toy manuscript patch application decision ledger accepted decision count"] != 9:
            raise AssertionError("Expected exactly 9 accepted record-only decisions.")

        if counters["Toy manuscript patch application decision ledger rejected decision count"] != 0:
            raise AssertionError("Expected zero rejected decisions.")

        if counters["Toy manuscript patch application decision ledger boundary note count"] != 9:
            raise AssertionError("Expected exactly 9 boundary notes.")

    def render_markdown(self, report: Dict[str, Any]) -> str:
        lines: List[str] = []

        lines.append("# Safe Abstract Toy Manuscript Patch Application Decision Ledger")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is decision-record-only.")
        lines.append("It records audited decisions from the v8.203 checklist audit lineage.")
        lines.append("It does not apply, authorize, complete, or execute any manuscript patch workflow.")
        lines.append("")
        lines.append(f"Decision phrase: `{report['decision_phrase']}`")
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
        lines.append("## Decision Ledger Items")
        lines.append("")

        for item in report["decisions"]:
            lines.append(f"### {item['id']}")
            lines.append("")
            lines.append(f"- Status: `{item['status']}`")
            lines.append(f"- Decision: {item['decision']}")
            lines.append(f"- Permission granted: `{item['permission_granted']}`")
            lines.append(f"- Execution allowed: `{item['execution_allowed']}`")
            lines.append(f"- Manuscript mutation allowed: `{item['manuscript_mutation_allowed']}`")
            lines.append(f"- Boundary note: {item['boundary_note']}")
            lines.append("")

        lines.append("## Boundary Notes")
        lines.append("")

        for index, note in enumerate(report["boundary_notes"], start=1):
            lines.append(f"{index}. {note}")

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
        lines.append("V8_204_SAFE_ABSTRACT_TOY_MANUSCRIPT_PATCH_APPLICATION_DECISION_LEDGER_OK")
        lines.append("")

        return "\n".join(lines)

    def run(self) -> Dict[str, Any]:
        report = self.build()

        self.output_md_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_json_path.parent.mkdir(parents=True, exist_ok=True)

        markdown = self.render_markdown(report)

        self.output_md_path.write_text(markdown, encoding="utf-8")
        self.output_json_path.write_text(
            json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

        return report


def build_safe_abstract_toy_manuscript_patch_application_decision_ledger() -> Dict[str, Any]:
    return SafeAbstractToyManuscriptPatchApplicationDecisionLedgerBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_manuscript_patch_application_decision_ledger()
    print("V8_204_SAFE_ABSTRACT_TOY_MANUSCRIPT_PATCH_APPLICATION_DECISION_LEDGER_OK")
    print(f"Decision ledger items: {result['counters']['Toy manuscript patch application decision ledger item count']}")
    print(f"Accepted decisions: {result['counters']['Toy manuscript patch application decision ledger accepted decision count']}")
    print(f"Rejected decisions: {result['counters']['Toy manuscript patch application decision ledger rejected decision count']}")
    print(f"Application permission count: {result['counters']['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {result['counters']['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript file modified count: {result['counters']['Toy manuscript patch application manuscript file modified count']}")
    print(f"Manuscript mutation count: {result['counters']['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {result['counters']['Manuscript submission ready count']}")
    print(f"Readiness approval count: {result['counters']['Readiness approval count']}")
    print(f"Passed: {result['passed']}")
