"""Prepare a safe sweep execution plan without executing a sweep.

This artifact plans a future safe abstract toy sweep only. It does not execute
the engine, does not execute a sweep, does not add biological semantics, and
does not expand claims.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


REGRESSION_JSON = Path("outputs/viruse_fabric_safe_engine_validation_regression_v1.json")
VALIDATION_ROUTE_JSON = Path("outputs/viruse_fabric_safe_engine_validation_safe_sweep_profile_v1.json")
BRIDGE_JSON = Path("outputs/viruse_fabric_safe_profile_engine_validation_bridge_v1.json")
SCAFFOLD_JSON = Path("outputs/viruse_fabric_safe_engine_redesign_sweep_profile_scaffold_v1.json")

REPORT_MD = Path("outputs/viruse_fabric_safe_sweep_execution_plan_v1.md")
REPORT_JSON = Path("outputs/viruse_fabric_safe_sweep_execution_plan_v1.json")


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _build_plan_steps() -> List[Dict[str, Any]]:
    return [
        {
            "step_id": "SAFE-SWEEP-PLAN-001",
            "title": "Preflight regression lock",
            "action": "Require safe engine validation regression to pass before any future sweep execution.",
            "allowed_now": True,
            "execution_now": False,
            "failure_response": "Stop before sweep harness execution.",
        },
        {
            "step_id": "SAFE-SWEEP-PLAN-002",
            "title": "Execution harness isolation",
            "action": "Implement a future harness that consumes SafeToySweepProfile cells without adding biological semantics.",
            "allowed_now": False,
            "execution_now": False,
            "failure_response": "Do not run sweep if harness modifies claim scope.",
        },
        {
            "step_id": "SAFE-SWEEP-PLAN-003",
            "title": "Null-control pairing",
            "action": "Pair every future safe sweep batch with null controls that must show zero leak.",
            "allowed_now": False,
            "execution_now": False,
            "failure_response": "Stop claim expansion if any null-control leak is nonzero.",
        },
        {
            "step_id": "SAFE-SWEEP-PLAN-004",
            "title": "Artifact-risk detection",
            "action": "Flag constant or mechanically identical signal deltas as artifact-risk before interpretation.",
            "allowed_now": False,
            "execution_now": False,
            "failure_response": "Stop interpretation if artifact-risk is moderate_to_high or worse.",
        },
        {
            "step_id": "SAFE-SWEEP-PLAN-005",
            "title": "No validation claim gate",
            "action": "Treat future sweep output as internal toy evidence only, not theory validation.",
            "allowed_now": False,
            "execution_now": False,
            "failure_response": "Block any manuscript readiness or validation language.",
        },
        {
            "step_id": "SAFE-SWEEP-PLAN-006",
            "title": "Post-run decision gate",
            "action": "After a future safe sweep, produce a decision gate before any next experiment.",
            "allowed_now": False,
            "execution_now": False,
            "failure_response": "Stop if safety counters or route counters deviate from plan.",
        },
    ]


def _build_stop_rules() -> List[Dict[str, Any]]:
    return [
        {
            "rule_id": "STOP-001",
            "condition": "Any real biological dataset, pathogen model, receptor parameter, host targeting, wet-lab protocol, infectivity optimization, immune evasion optimization, or host range prediction appears.",
            "decision": "stop_immediately",
        },
        {
            "rule_id": "STOP-002",
            "condition": "Any future null-control leak count is nonzero.",
            "decision": "stop_claim_expansion",
        },
        {
            "rule_id": "STOP-003",
            "condition": "Any future signal delta is constant across all valid cells without a mechanistic toy explanation.",
            "decision": "artifact_risk_review_required",
        },
        {
            "rule_id": "STOP-004",
            "condition": "Any future result is framed as theory validation, external validation, independent validation, readiness approval, or submission readiness.",
            "decision": "block_report",
        },
        {
            "rule_id": "STOP-005",
            "condition": "Any future sweep harness bypasses SafeToySweepProfile validation.",
            "decision": "reject_harness",
        },
    ]


def build_report() -> Dict[str, Any]:
    regression = _load_json(REGRESSION_JSON)
    validation_route = _load_json(VALIDATION_ROUTE_JSON)
    bridge = _load_json(BRIDGE_JSON)
    scaffold = _load_json(SCAFFOLD_JSON)

    assert regression["passed"] is True
    assert regression["next_allowed_action"] == "prepare_safe_engine_sweep_execution_plan_without_claim_expansion"
    assert validation_route["passed"] is True
    assert bridge["passed"] is True
    assert scaffold["passed"] is True

    regression_matrix = regression["validation_matrix_summary"]
    validation_matrix = validation_route["validation_matrix_summary"]
    bridge_summary = bridge["bridge_summary"]
    scaffold_summary = scaffold["profile_summary"]

    matrix_consistency = (
        regression_matrix["matrix_record_count"] == 64
        and validation_matrix["matrix_record_count"] == 64
        and bridge_summary["sweep_profile_cell_count"] == 64
        and scaffold_summary["total_grid_cell_count"] == 4 ** 7
        and regression_matrix["route_counts"]["current_engine_default_boundary"] == 1
        and regression_matrix["route_counts"]["safe_sweep_profile_validation"] == 63
        and regression_matrix["route_counts"]["outside_safe_sweep_profile"] == 0
    )

    plan_steps = _build_plan_steps()
    stop_rules = _build_stop_rules()

    counters = {
        "Safe sweep execution plan artifact count": 1,
        "Plan step count": len(plan_steps),
        "Stop rule count": len(stop_rules),
        "Preflight regression source count": 1,
        "Validation route source count": 1,
        "Bridge source count": 1,
        "Scaffold source count": 1,
        "Safe sweep profile total abstract grid cell count": scaffold_summary["total_grid_cell_count"],
        "Engine validation matrix record count": regression_matrix["matrix_record_count"],
        "Current engine default boundary route count": regression_matrix["route_counts"]["current_engine_default_boundary"],
        "Safe sweep profile validation route count": regression_matrix["route_counts"]["safe_sweep_profile_validation"],
        "Outside safe sweep profile route count": regression_matrix["route_counts"]["outside_safe_sweep_profile"],
        "Matrix consistency check count": 1 if matrix_consistency else 0,
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
        "artifact": "safe_sweep_execution_plan_v1",
        "scope": "safe-sweep-execution-plan-only-no-sweep-execution",
        "plan_created": True,
        "engine_modified": False,
        "engine_executed": False,
        "sweep_executed": False,
        "experiment_executed": False,
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
            "regression": regression["artifact"],
            "validation_route": validation_route["artifact"],
            "bridge": bridge["artifact"],
            "scaffold": scaffold["artifact"],
        },
        "matrix_consistency": matrix_consistency,
        "planned_future_scope": {
            "future_execution_may_use_engine": True,
            "execution_allowed_by_this_artifact": False,
            "safe_abstract_toy_only": True,
            "biological_semantics_allowed": False,
            "claim_expansion_allowed": False,
            "full_grid_execution_planned_cells": 64,
            "interpretation_boundary": "internal_toy_evidence_only",
        },
        "plan_steps": plan_steps,
        "stop_rules": stop_rules,
        "next_allowed_action": "implement_safe_sweep_execution_harness_on_separate_checked_commit_without_running_sweep",
        "counters": counters,
        "passed": True,
        "required_markers": [
            "safe-sweep-execution-plan-only-no-sweep-execution",
            "plan only",
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
    assert report["scope"] == "safe-sweep-execution-plan-only-no-sweep-execution"
    assert report["plan_created"] is True
    assert report["engine_modified"] is False
    assert report["engine_executed"] is False
    assert report["sweep_executed"] is False
    assert report["experiment_executed"] is False
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
    assert report["matrix_consistency"] is True

    assert len(report["plan_steps"]) == 6
    assert len(report["stop_rules"]) == 5

    future = report["planned_future_scope"]
    assert future["future_execution_may_use_engine"] is True
    assert future["execution_allowed_by_this_artifact"] is False
    assert future["safe_abstract_toy_only"] is True
    assert future["biological_semantics_allowed"] is False
    assert future["claim_expansion_allowed"] is False
    assert future["full_grid_execution_planned_cells"] == 64
    assert future["interpretation_boundary"] == "internal_toy_evidence_only"

    counters = report["counters"]
    assert counters["Plan step count"] == 6
    assert counters["Stop rule count"] == 5
    assert counters["Safe sweep profile total abstract grid cell count"] == 4 ** 7
    assert counters["Engine validation matrix record count"] == 64
    assert counters["Current engine default boundary route count"] == 1
    assert counters["Safe sweep profile validation route count"] == 63
    assert counters["Outside safe sweep profile route count"] == 0
    assert counters["Matrix consistency check count"] == 1

    must_be_zero = [
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
    future = report["planned_future_scope"]

    lines = []
    lines.append("# Safe Sweep Execution Plan v1")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append("Scope: safe-sweep-execution-plan-only-no-sweep-execution")
    lines.append("")
    lines.append("This artifact is plan only.")
    lines.append("plan only")
    lines.append("There is no sweep execution.")
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
    lines.append("## Planned Future Scope")
    lines.append("")
    for key, value in future.items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Plan Steps")
    lines.append("")
    for step in report["plan_steps"]:
        lines.append(f"### {step['step_id']} — {step['title']}")
        lines.append(f"- Action: {step['action']}")
        lines.append(f"- Allowed now: {step['allowed_now']}")
        lines.append(f"- Execution now: {step['execution_now']}")
        lines.append(f"- Failure response: {step['failure_response']}")
        lines.append("")
    lines.append("## Stop Rules")
    lines.append("")
    for rule in report["stop_rules"]:
        lines.append(f"- {rule['rule_id']}: if {rule['condition']} => {rule['decision']}")
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
        "safe-sweep-execution-plan-only-no-sweep-execution",
        "plan only",
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
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("SAFE_SWEEP_EXECUTION_PLAN_V1_OK")
    print("Plan step count:", len(report["plan_steps"]))
    print("Stop rule count:", len(report["stop_rules"]))
    print("Matrix consistency:", report["matrix_consistency"])
    print("Future planned cells:", report["planned_future_scope"]["full_grid_execution_planned_cells"])
    print("Engine modified:", report["engine_modified"])
    print("Engine executed:", report["engine_executed"])
    print("Sweep executed:", report["sweep_executed"])
    print("Claim expansion allowed:", report["claim_expansion_allowed"])
    print("Next allowed action:", report["next_allowed_action"])


if __name__ == "__main__":
    main()
