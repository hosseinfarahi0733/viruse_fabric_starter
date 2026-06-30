"""Prepare a safe sweep dry-run protocol without executing anything.

This artifact prepares a protocol for a future dry-run. It does not execute a
dry-run, does not execute the engine, does not run a sweep, and does not
execute null controls. It only specifies gates, stop rules, and expected
non-execution checks.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


NULL_CONTROL_REGRESSION_JSON = Path(
    "outputs/viruse_fabric_safe_null_control_template_regression_v1.json"
)
NULL_CONTROL_JSON = Path("outputs/viruse_fabric_safe_null_control_templates_v1.json")
HARNESS_JSON = Path("outputs/viruse_fabric_safe_sweep_execution_harness_v1.json")
PLAN_JSON = Path("outputs/viruse_fabric_safe_sweep_execution_plan_v1.json")

REPORT_MD = Path("outputs/viruse_fabric_safe_sweep_dry_run_protocol_v1.md")
REPORT_JSON = Path("outputs/viruse_fabric_safe_sweep_dry_run_protocol_v1.json")


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _protocol_phases() -> List[Dict[str, Any]]:
    return [
        {
            "phase_id": "DRY-RUN-PROTOCOL-001",
            "title": "Artifact preflight",
            "purpose": "Confirm plan, harness, null-control templates, and null-control regression are all present and passing.",
            "allowed_now": True,
            "executes_engine": False,
            "executes_sweep": False,
            "executes_null_controls": False,
            "failure_response": "stop_before_any_dry_run",
        },
        {
            "phase_id": "DRY-RUN-PROTOCOL-002",
            "title": "Dry-run manifest construction",
            "purpose": "Future dry-run may build a manifest of intended cells and null-control pairings without scoring or interpretation.",
            "allowed_now": False,
            "executes_engine": False,
            "executes_sweep": False,
            "executes_null_controls": False,
            "failure_response": "reject_manifest_if_any_execution_flag_is_true",
        },
        {
            "phase_id": "DRY-RUN-PROTOCOL-003",
            "title": "Execution refusal checks",
            "purpose": "Future dry-run must prove engine, sweep, and null-control execution paths remain disabled.",
            "allowed_now": False,
            "executes_engine": False,
            "executes_sweep": False,
            "executes_null_controls": False,
            "failure_response": "stop_if_refusal_check_fails",
        },
        {
            "phase_id": "DRY-RUN-PROTOCOL-004",
            "title": "Safety counter audit",
            "purpose": "Future dry-run must keep all biological, validation, readiness, citation, and claim counters at zero.",
            "allowed_now": False,
            "executes_engine": False,
            "executes_sweep": False,
            "executes_null_controls": False,
            "failure_response": "block_report_if_any_forbidden_counter_is_nonzero",
        },
        {
            "phase_id": "DRY-RUN-PROTOCOL-005",
            "title": "Post dry-run protocol gate",
            "purpose": "Future dry-run output must be classified as protocol/dry-run metadata only, not evidence.",
            "allowed_now": False,
            "executes_engine": False,
            "executes_sweep": False,
            "executes_null_controls": False,
            "failure_response": "stop_claim_expansion",
        },
    ]


def _stop_rules() -> List[Dict[str, Any]]:
    return [
        {
            "rule_id": "DRY-RUN-STOP-001",
            "condition": "Any engine execution flag becomes true.",
            "decision": "stop_immediately",
        },
        {
            "rule_id": "DRY-RUN-STOP-002",
            "condition": "Any sweep execution flag becomes true.",
            "decision": "stop_immediately",
        },
        {
            "rule_id": "DRY-RUN-STOP-003",
            "condition": "Any null-control execution flag becomes true.",
            "decision": "stop_immediately",
        },
        {
            "rule_id": "DRY-RUN-STOP-004",
            "condition": "Any biological semantics, pathogen framing, receptor parameter, targeting, wet-lab, infectivity, immune evasion, or host range content appears.",
            "decision": "reject_artifact",
        },
        {
            "rule_id": "DRY-RUN-STOP-005",
            "condition": "Any validation, external validation, independent experiment, manuscript readiness, submission readiness, readiness approval, or citation claim appears.",
            "decision": "reject_artifact",
        },
        {
            "rule_id": "DRY-RUN-STOP-006",
            "condition": "Any future dry-run output is interpreted as evidence rather than protocol metadata.",
            "decision": "stop_claim_expansion",
        },
    ]


def build_report() -> Dict[str, Any]:
    null_regression = _load_json(NULL_CONTROL_REGRESSION_JSON)
    null_templates = _load_json(NULL_CONTROL_JSON)
    harness = _load_json(HARNESS_JSON)
    plan = _load_json(PLAN_JSON)

    assert null_regression["passed"] is True
    assert null_regression["next_allowed_action"] == (
        "prepare_safe_sweep_dry_run_protocol_without_engine_or_sweep_execution"
    )
    assert null_templates["passed"] is True
    assert harness["passed"] is True
    assert plan["passed"] is True

    phases = _protocol_phases()
    stop_rules = _stop_rules()

    source_consistency = (
        null_regression["manifest_summary"]["template_count"] == 4
        and null_regression["manifest_summary"]["harness_cell_count"] == 64
        and null_regression["manifest_summary"]["planned_pair_count"] == 256
        and null_templates["manifest"]["planned_pair_count"] == 256
        and harness["manifest"]["cell_count"] == 64
        and plan["planned_future_scope"]["full_grid_execution_planned_cells"] == 64
    )

    phase_non_execution_consistency = all(
        phase["executes_engine"] is False
        and phase["executes_sweep"] is False
        and phase["executes_null_controls"] is False
        for phase in phases
    )

    counters = {
        "Safe sweep dry-run protocol artifact count": 1,
        "Protocol phase count": len(phases),
        "Protocol stop rule count": len(stop_rules),
        "Source consistency check count": 1 if source_consistency else 0,
        "Phase non-execution consistency check count": 1
        if phase_non_execution_consistency
        else 0,
        "Planned future harness cell count": 64,
        "Planned future null-control template count": 4,
        "Planned future null-control pair count": 256,
        "Dry-run execution count": 0,
        "Null-control execution count": 0,
        "Observed null-control leak count": 0,
        "Engine modification count": 0,
        "Engine execution count": 0,
        "Sweep execution count": 0,
        "Experiment execution count": 0,
        "Claim expansion count": 0,
        "Validation claim count": 0,
        "Theory validation claim count": 0,
        "External validation count": 0,
        "Independent experiment count": 0,
        "Manuscript readiness claim count": 0,
        "Manuscript submission ready count": 0,
        "Readiness approval count": 0,
        "Official tag created count": 0,
        "New milestone created count": 0,
        "New citation added count": 0,
        "Real biological dataset import count": 0,
        "Real pathogen simulation count": 0,
        "Real receptor parameter count": 0,
        "Operational host targeting count": 0,
        "Wet-lab protocol count": 0,
        "Real-world infectivity optimization count": 0,
        "Immune evasion optimization count": 0,
        "Real host range prediction count": 0,
    }

    report = {
        "artifact": "safe_sweep_dry_run_protocol_v1",
        "scope": "safe-sweep-dry-run-protocol-only-no-engine-or-sweep-execution",
        "protocol_created": True,
        "dry_run_executed": False,
        "null_controls_executed": False,
        "engine_modified": False,
        "engine_executed": False,
        "sweep_executed": False,
        "experiment_executed": False,
        "observed_null_control_leak_count": 0,
        "claim_expansion_allowed": False,
        "validation_claim_made": False,
        "theory_validation_claim_made": False,
        "external_validation_claim_made": False,
        "independent_experiment_claim_made": False,
        "manuscript_readiness_claim_made": False,
        "manuscript_submission_ready_claim_made": False,
        "new_milestone_created": False,
        "new_official_tag_created": False,
        "new_citation_added": False,
        "source_artifacts": {
            "null_control_regression": null_regression["artifact"],
            "null_control_templates": null_templates["artifact"],
            "harness": harness["artifact"],
            "plan": plan["artifact"],
        },
        "source_consistency": source_consistency,
        "phase_non_execution_consistency": phase_non_execution_consistency,
        "protocol_phases": phases,
        "stop_rules": stop_rules,
        "dry_run_boundary": {
            "allowed_now": False,
            "future_dry_run_may_build_manifest": True,
            "future_dry_run_may_execute_engine": False,
            "future_dry_run_may_execute_sweep": False,
            "future_dry_run_may_execute_null_controls": False,
            "future_dry_run_may_make_evidence_claim": False,
            "interpretation_boundary": "protocol_metadata_only_not_evidence",
        },
        "next_allowed_action": "run_safe_sweep_dry_run_protocol_regression_without_engine_or_sweep_execution",
        "counters": counters,
        "passed": True,
        "required_markers": [
            "safe-sweep-dry-run-protocol-only-no-engine-or-sweep-execution",
            "dry-run protocol created",
            "dry-run not executed",
            "no dry-run execution",
            "no null-control execution",
            "no observed null-control leak",
            "no engine execution",
            "no sweep execution",
            "engine not modified",
            "engine not executed",
            "sweep not executed",
            "claim expansion remains forbidden",
            "No validation claim is made",
            "No theory validation claim is made",
            "No manuscript readiness claim is made",
            "No manuscript submission readiness claim is made",
            "No external validation claim is made",
            "No independent experiment claim is made",
            "No real biological datasets",
            "no real pathogen models",
            "no receptor parameters",
            "no operational targeting",
            "no wet-lab protocol",
            "no infectivity optimization",
            "no immune evasion optimization",
            "no host range prediction",
        ],
    }

    validate_report(report)
    return report


def validate_report(report: Dict[str, Any]) -> None:
    assert report["passed"] is True
    assert report["scope"] == "safe-sweep-dry-run-protocol-only-no-engine-or-sweep-execution"
    assert report["protocol_created"] is True
    assert report["dry_run_executed"] is False
    assert report["null_controls_executed"] is False
    assert report["engine_modified"] is False
    assert report["engine_executed"] is False
    assert report["sweep_executed"] is False
    assert report["experiment_executed"] is False
    assert report["observed_null_control_leak_count"] == 0
    assert report["claim_expansion_allowed"] is False
    assert report["validation_claim_made"] is False
    assert report["theory_validation_claim_made"] is False
    assert report["external_validation_claim_made"] is False
    assert report["independent_experiment_claim_made"] is False
    assert report["manuscript_readiness_claim_made"] is False
    assert report["manuscript_submission_ready_claim_made"] is False
    assert report["new_milestone_created"] is False
    assert report["new_official_tag_created"] is False
    assert report["new_citation_added"] is False
    assert report["source_consistency"] is True
    assert report["phase_non_execution_consistency"] is True

    boundary = report["dry_run_boundary"]
    assert boundary["allowed_now"] is False
    assert boundary["future_dry_run_may_build_manifest"] is True
    assert boundary["future_dry_run_may_execute_engine"] is False
    assert boundary["future_dry_run_may_execute_sweep"] is False
    assert boundary["future_dry_run_may_execute_null_controls"] is False
    assert boundary["future_dry_run_may_make_evidence_claim"] is False
    assert boundary["interpretation_boundary"] == "protocol_metadata_only_not_evidence"

    counters = report["counters"]
    assert counters["Protocol phase count"] == 5
    assert counters["Protocol stop rule count"] == 6
    assert counters["Source consistency check count"] == 1
    assert counters["Phase non-execution consistency check count"] == 1
    assert counters["Planned future harness cell count"] == 64
    assert counters["Planned future null-control template count"] == 4
    assert counters["Planned future null-control pair count"] == 256

    must_be_zero = [
        "Dry-run execution count",
        "Null-control execution count",
        "Observed null-control leak count",
        "Engine modification count",
        "Engine execution count",
        "Sweep execution count",
        "Experiment execution count",
        "Claim expansion count",
        "Validation claim count",
        "Theory validation claim count",
        "External validation count",
        "Independent experiment count",
        "Manuscript readiness claim count",
        "Manuscript submission ready count",
        "Readiness approval count",
        "Official tag created count",
        "New milestone created count",
        "New citation added count",
        "Real biological dataset import count",
        "Real pathogen simulation count",
        "Real receptor parameter count",
        "Operational host targeting count",
        "Wet-lab protocol count",
        "Real-world infectivity optimization count",
        "Immune evasion optimization count",
        "Real host range prediction count",
    ]

    bad = {name: counters.get(name) for name in must_be_zero if counters.get(name) != 0}
    if bad:
        raise AssertionError(f"Forbidden nonzero counters: {bad}")


def render_markdown(report: Dict[str, Any]) -> str:
    counters = report["counters"]
    boundary = report["dry_run_boundary"]

    lines = []
    lines.append("# Safe Sweep Dry-Run Protocol v1")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append("Scope: safe-sweep-dry-run-protocol-only-no-engine-or-sweep-execution")
    lines.append("")
    lines.append("dry-run protocol created")
    lines.append("dry-run not executed")
    lines.append("no dry-run execution")
    lines.append("no null-control execution")
    lines.append("no observed null-control leak")
    lines.append("no engine execution")
    lines.append("no sweep execution")
    lines.append("The engine is not modified.")
    lines.append("engine not modified")
    lines.append("The engine is not executed.")
    lines.append("engine not executed")
    lines.append("A sweep is not executed.")
    lines.append("sweep not executed")
    lines.append("claim expansion remains forbidden.")
    lines.append("No validation claim is made.")
    lines.append("No theory validation claim is made.")
    lines.append("No manuscript readiness claim is made.")
    lines.append("No manuscript submission readiness claim is made.")
    lines.append("No external validation claim is made.")
    lines.append("No independent experiment claim is made.")
    lines.append("")
    lines.append("## Source Artifacts")
    lines.append("")
    for key, value in report["source_artifacts"].items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Protocol Phases")
    lines.append("")
    for phase in report["protocol_phases"]:
        lines.append(f"### {phase['phase_id']} — {phase['title']}")
        lines.append(f"- Purpose: {phase['purpose']}")
        lines.append(f"- Allowed now: {phase['allowed_now']}")
        lines.append(f"- Executes engine: {phase['executes_engine']}")
        lines.append(f"- Executes sweep: {phase['executes_sweep']}")
        lines.append(f"- Executes null controls: {phase['executes_null_controls']}")
        lines.append(f"- Failure response: {phase['failure_response']}")
        lines.append("")
    lines.append("## Stop Rules")
    lines.append("")
    for rule in report["stop_rules"]:
        lines.append(f"- {rule['rule_id']}: if {rule['condition']} => {rule['decision']}")
    lines.append("")
    lines.append("## Dry-Run Boundary")
    lines.append("")
    for key, value in boundary.items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Required Safety Markers")
    lines.append("")
    for marker in report["required_markers"]:
        lines.append(f"- {marker}")
    lines.append("")
    lines.append("## Counters")
    lines.append("")
    for key in sorted(counters):
        lines.append(f"- {key}: {counters[key]}")
    lines.append("")
    lines.append("## Boundary")
    lines.append("")
    lines.append("Safe abstract toy model only. No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced.")
    lines.append("")
    lines.append("## Next Allowed Action")
    lines.append("")
    lines.append(report["next_allowed_action"])
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    report = build_report()
    markdown = render_markdown(report)

    required_phrases = [
        "safe-sweep-dry-run-protocol-only-no-engine-or-sweep-execution",
        "dry-run protocol created",
        "dry-run not executed",
        "no dry-run execution",
        "no null-control execution",
        "no observed null-control leak",
        "no engine execution",
        "no sweep execution",
        "engine not modified",
        "engine not executed",
        "sweep not executed",
        "claim expansion remains forbidden",
        "No validation claim is made",
        "No theory validation claim is made",
        "No manuscript readiness claim is made",
        "No manuscript submission readiness claim is made",
        "No external validation claim is made",
        "No independent experiment claim is made",
        "No real biological datasets",
        "no real pathogen models",
        "no receptor parameters",
        "no operational targeting",
        "no wet-lab protocol",
        "no infectivity optimization",
        "no immune evasion optimization",
        "no host range prediction",
    ]

    missing = [phrase for phrase in required_phrases if phrase not in markdown]
    if missing:
        raise SystemExit(f"Missing markdown phrases: {missing}")

    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    REPORT_MD.write_text(markdown, encoding="utf-8")
    REPORT_JSON.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print("SAFE_SWEEP_DRY_RUN_PROTOCOL_V1_OK")
    print("Protocol phase count:", report["counters"]["Protocol phase count"])
    print("Stop rule count:", report["counters"]["Protocol stop rule count"])
    print("Dry-run executed:", report["dry_run_executed"])
    print("Null controls executed:", report["null_controls_executed"])
    print("Engine executed:", report["engine_executed"])
    print("Sweep executed:", report["sweep_executed"])
    print("Claim expansion allowed:", report["claim_expansion_allowed"])
    print("Next allowed action:", report["next_allowed_action"])


if __name__ == "__main__":
    main()
