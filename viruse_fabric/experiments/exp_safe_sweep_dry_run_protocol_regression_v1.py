"""Regression checks for the safe sweep dry-run protocol.

This regression validates the dry-run protocol artifact only. It does not
execute a dry-run, does not execute the engine, does not execute a sweep, and
does not execute null controls.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


DRY_RUN_PROTOCOL_JSON = Path("outputs/viruse_fabric_safe_sweep_dry_run_protocol_v1.json")
NULL_CONTROL_REGRESSION_JSON = Path(
    "outputs/viruse_fabric_safe_null_control_template_regression_v1.json"
)
NULL_CONTROL_JSON = Path("outputs/viruse_fabric_safe_null_control_templates_v1.json")
HARNESS_JSON = Path("outputs/viruse_fabric_safe_sweep_execution_harness_v1.json")
PLAN_JSON = Path("outputs/viruse_fabric_safe_sweep_execution_plan_v1.json")

REPORT_MD = Path("outputs/viruse_fabric_safe_sweep_dry_run_protocol_regression_v1.md")
REPORT_JSON = Path("outputs/viruse_fabric_safe_sweep_dry_run_protocol_regression_v1.json")


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validate_protocol_phases(phases: List[Dict[str, Any]]) -> Dict[str, Any]:
    expected_phase_ids = {
        "DRY-RUN-PROTOCOL-001",
        "DRY-RUN-PROTOCOL-002",
        "DRY-RUN-PROTOCOL-003",
        "DRY-RUN-PROTOCOL-004",
        "DRY-RUN-PROTOCOL-005",
    }

    actual_phase_ids = {phase["phase_id"] for phase in phases}

    if actual_phase_ids != expected_phase_ids:
        raise AssertionError(f"Unexpected protocol phase ids: {actual_phase_ids}")

    allowed_now_count = 0

    for phase in phases:
        if phase["executes_engine"] is not False:
            raise AssertionError(f"Phase executes engine: {phase}")
        if phase["executes_sweep"] is not False:
            raise AssertionError(f"Phase executes sweep: {phase}")
        if phase["executes_null_controls"] is not False:
            raise AssertionError(f"Phase executes null controls: {phase}")
        if phase["allowed_now"] is True:
            allowed_now_count += 1
        if not phase["failure_response"]:
            raise AssertionError(f"Phase must define failure_response: {phase}")

    if allowed_now_count != 1:
        raise AssertionError(f"Expected exactly one allowed-now preflight phase, got {allowed_now_count}")

    return {
        "expected_phase_id_count": len(expected_phase_ids),
        "actual_phase_id_count": len(actual_phase_ids),
        "all_expected_phase_ids_present": actual_phase_ids == expected_phase_ids,
        "all_phases_disable_engine_execution": True,
        "all_phases_disable_sweep_execution": True,
        "all_phases_disable_null_control_execution": True,
        "allowed_now_phase_count": allowed_now_count,
    }


def _validate_stop_rules(stop_rules: List[Dict[str, Any]]) -> Dict[str, Any]:
    expected_rule_ids = {
        "DRY-RUN-STOP-001",
        "DRY-RUN-STOP-002",
        "DRY-RUN-STOP-003",
        "DRY-RUN-STOP-004",
        "DRY-RUN-STOP-005",
        "DRY-RUN-STOP-006",
    }

    actual_rule_ids = {rule["rule_id"] for rule in stop_rules}

    if actual_rule_ids != expected_rule_ids:
        raise AssertionError(f"Unexpected stop rule ids: {actual_rule_ids}")

    combined_text = " ".join(
        f"{rule['condition']} {rule['decision']}" for rule in stop_rules
    ).lower()

    required_terms = [
        "engine",
        "sweep",
        "null-control",
        "biological",
        "validation",
        "readiness",
        "evidence",
    ]

    missing_terms = [term for term in required_terms if term not in combined_text]
    if missing_terms:
        raise AssertionError(f"Stop rules missing required terms: {missing_terms}")

    return {
        "expected_stop_rule_count": len(expected_rule_ids),
        "actual_stop_rule_count": len(actual_rule_ids),
        "all_expected_stop_rules_present": actual_rule_ids == expected_rule_ids,
        "stop_rules_cover_engine_sweep_null_bio_validation_readiness_evidence": True,
    }


def build_report() -> Dict[str, Any]:
    protocol = _load_json(DRY_RUN_PROTOCOL_JSON)
    null_regression = _load_json(NULL_CONTROL_REGRESSION_JSON)
    null_templates = _load_json(NULL_CONTROL_JSON)
    harness = _load_json(HARNESS_JSON)
    plan = _load_json(PLAN_JSON)

    assert protocol["passed"] is True
    assert protocol["next_allowed_action"] == (
        "run_safe_sweep_dry_run_protocol_regression_without_engine_or_sweep_execution"
    )
    assert null_regression["passed"] is True
    assert null_templates["passed"] is True
    assert harness["passed"] is True
    assert plan["passed"] is True

    phase_regression = _validate_protocol_phases(protocol["protocol_phases"])
    stop_rule_regression = _validate_stop_rules(protocol["stop_rules"])

    boundary = protocol["dry_run_boundary"]
    boundary_regression = {
        "allowed_now_false": boundary["allowed_now"] is False,
        "future_manifest_building_allowed": boundary["future_dry_run_may_build_manifest"] is True,
        "future_engine_execution_forbidden": boundary["future_dry_run_may_execute_engine"] is False,
        "future_sweep_execution_forbidden": boundary["future_dry_run_may_execute_sweep"] is False,
        "future_null_control_execution_forbidden": boundary["future_dry_run_may_execute_null_controls"] is False,
        "future_evidence_claim_forbidden": boundary["future_dry_run_may_make_evidence_claim"] is False,
        "interpretation_boundary_is_metadata_only": boundary["interpretation_boundary"]
        == "protocol_metadata_only_not_evidence",
    }

    source_alignment = (
        protocol["source_consistency"] is True
        and protocol["phase_non_execution_consistency"] is True
        and null_regression["manifest_summary"]["planned_pair_count"] == 256
        and null_templates["manifest"]["planned_pair_count"] == 256
        and harness["manifest"]["cell_count"] == 64
        and plan["planned_future_scope"]["full_grid_execution_planned_cells"] == 64
    )

    counters = {
        "Safe sweep dry-run protocol regression artifact count": 1,
        "Protocol phase regression case count": len(protocol["protocol_phases"]),
        "Protocol stop-rule regression case count": len(protocol["stop_rules"]),
        "Boundary regression case count": len(boundary_regression),
        "Source alignment count": 1 if source_alignment else 0,
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
        "artifact": "safe_sweep_dry_run_protocol_regression_v1",
        "scope": "safe-sweep-dry-run-protocol-regression-no-engine-or-sweep-execution",
        "regression_executed": True,
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
            "dry_run_protocol": protocol["artifact"],
            "null_control_regression": null_regression["artifact"],
            "null_control_templates": null_templates["artifact"],
            "harness": harness["artifact"],
            "plan": plan["artifact"],
        },
        "phase_regression": phase_regression,
        "stop_rule_regression": stop_rule_regression,
        "boundary_regression": boundary_regression,
        "source_alignment": source_alignment,
        "next_allowed_action": "implement_safe_dry_run_manifest_builder_without_engine_or_sweep_execution",
        "counters": counters,
        "passed": True,
        "required_markers": [
            "safe-sweep-dry-run-protocol-regression-no-engine-or-sweep-execution",
            "dry-run protocol regression executed",
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
    assert report["scope"] == "safe-sweep-dry-run-protocol-regression-no-engine-or-sweep-execution"
    assert report["regression_executed"] is True
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
    assert report["source_alignment"] is True

    assert report["phase_regression"]["all_expected_phase_ids_present"] is True
    assert report["phase_regression"]["all_phases_disable_engine_execution"] is True
    assert report["phase_regression"]["all_phases_disable_sweep_execution"] is True
    assert report["phase_regression"]["all_phases_disable_null_control_execution"] is True
    assert report["phase_regression"]["allowed_now_phase_count"] == 1

    assert report["stop_rule_regression"]["all_expected_stop_rules_present"] is True
    assert (
        report["stop_rule_regression"][
            "stop_rules_cover_engine_sweep_null_bio_validation_readiness_evidence"
        ]
        is True
    )

    for key, value in report["boundary_regression"].items():
        assert value is True, key

    counters = report["counters"]
    assert counters["Protocol phase regression case count"] == 5
    assert counters["Protocol stop-rule regression case count"] == 6
    assert counters["Boundary regression case count"] == 7
    assert counters["Source alignment count"] == 1
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

    lines = []
    lines.append("# Safe Sweep Dry-Run Protocol Regression v1")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append("Scope: safe-sweep-dry-run-protocol-regression-no-engine-or-sweep-execution")
    lines.append("")
    lines.append("dry-run protocol regression executed")
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
    lines.append("## Phase Regression")
    lines.append("")
    for key, value in report["phase_regression"].items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Stop Rule Regression")
    lines.append("")
    for key, value in report["stop_rule_regression"].items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Boundary Regression")
    lines.append("")
    for key, value in report["boundary_regression"].items():
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
        "safe-sweep-dry-run-protocol-regression-no-engine-or-sweep-execution",
        "dry-run protocol regression executed",
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

    print("SAFE_SWEEP_DRY_RUN_PROTOCOL_REGRESSION_V1_OK")
    print("Protocol phase regression case count:", report["counters"]["Protocol phase regression case count"])
    print("Protocol stop-rule regression case count:", report["counters"]["Protocol stop-rule regression case count"])
    print("Dry-run executed:", report["dry_run_executed"])
    print("Null controls executed:", report["null_controls_executed"])
    print("Engine executed:", report["engine_executed"])
    print("Sweep executed:", report["sweep_executed"])
    print("Claim expansion allowed:", report["claim_expansion_allowed"])
    print("Next allowed action:", report["next_allowed_action"])


if __name__ == "__main__":
    main()
