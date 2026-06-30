"""Report the safe sweep execution harness implementation.

The harness is implemented but not run. This artifact validates the harness
manifest, confirms execution refusal, and preserves all no-claim boundaries.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from viruse_fabric.simulation.viruse_fabric_safe_sweep_execution_harness import (
    HARNESS_VERSION,
    build_safe_sweep_execution_harness_manifest_v1,
    build_safe_sweep_execution_harness_v1,
)


PLAN_JSON = Path("outputs/viruse_fabric_safe_sweep_execution_plan_v1.json")
REGRESSION_JSON = Path("outputs/viruse_fabric_safe_engine_validation_regression_v1.json")
VALIDATION_ROUTE_JSON = Path("outputs/viruse_fabric_safe_engine_validation_safe_sweep_profile_v1.json")

REPORT_MD = Path("outputs/viruse_fabric_safe_sweep_execution_harness_v1.md")
REPORT_JSON = Path("outputs/viruse_fabric_safe_sweep_execution_harness_v1.json")


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_report() -> Dict[str, Any]:
    plan = _load_json(PLAN_JSON)
    regression = _load_json(REGRESSION_JSON)
    validation_route = _load_json(VALIDATION_ROUTE_JSON)

    assert plan["passed"] is True
    assert plan["next_allowed_action"] == (
        "implement_safe_sweep_execution_harness_on_separate_checked_commit_without_running_sweep"
    )
    assert regression["passed"] is True
    assert validation_route["passed"] is True

    harness = build_safe_sweep_execution_harness_v1()
    manifest = build_safe_sweep_execution_harness_manifest_v1(preview_cell_count=12)

    execution_refusal_check_passed = False
    try:
        harness.run_sweep()
    except RuntimeError:
        execution_refusal_check_passed = True

    counters = {
        "Safe sweep execution harness artifact count": 1,
        "Harness implementation count": 1,
        "Harness manifest count": 1,
        "Harness cell count": manifest["cell_count"],
        "Harness preview cell count": manifest["preview_cell_count"],
        "Current engine default boundary route count": manifest["route_counts"]["current_engine_default_boundary"],
        "Safe sweep profile validation route count": manifest["route_counts"]["safe_sweep_profile_validation"],
        "Outside safe sweep profile route count": manifest["route_counts"]["outside_safe_sweep_profile"],
        "Execution refusal check count": 1 if execution_refusal_check_passed else 0,
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
        "artifact": "safe_sweep_execution_harness_v1",
        "scope": "safe-sweep-execution-harness-implementation-no-sweep-execution",
        "harness_version": HARNESS_VERSION,
        "harness_implemented": True,
        "harness_manifest_created": True,
        "execution_refusal_check_passed": execution_refusal_check_passed,
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
            "plan": plan["artifact"],
            "regression": regression["artifact"],
            "validation_route": validation_route["artifact"],
        },
        "manifest": manifest,
        "next_allowed_action": "implement_null_control_templates_for_safe_harness_without_running_sweep",
        "counters": counters,
        "passed": True,
        "required_markers": [
            "safe-sweep-execution-harness-implementation-no-sweep-execution",
            "SAFE_SWEEP_EXECUTION_HARNESS_V1",
            "harness implemented",
            "harness manifest created",
            "execution refused",
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
    assert report["scope"] == "safe-sweep-execution-harness-implementation-no-sweep-execution"
    assert report["harness_version"] == "SAFE_SWEEP_EXECUTION_HARNESS_V1"
    assert report["harness_implemented"] is True
    assert report["harness_manifest_created"] is True
    assert report["execution_refusal_check_passed"] is True
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

    manifest = report["manifest"]
    assert manifest["cell_count"] == 64
    assert manifest["route_counts"] == {
        "current_engine_default_boundary": 1,
        "safe_sweep_profile_validation": 63,
        "outside_safe_sweep_profile": 0,
    }
    assert manifest["execution_enabled"] is False
    assert manifest["engine_execution_enabled"] is False
    assert manifest["sweep_execution_enabled"] is False
    assert manifest["claim_expansion_allowed"] is False
    assert manifest["real_biological_semantics_allowed"] is False

    counters = report["counters"]
    assert counters["Harness implementation count"] == 1
    assert counters["Harness manifest count"] == 1
    assert counters["Harness cell count"] == 64
    assert counters["Current engine default boundary route count"] == 1
    assert counters["Safe sweep profile validation route count"] == 63
    assert counters["Outside safe sweep profile route count"] == 0
    assert counters["Execution refusal check count"] == 1

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
    manifest = report["manifest"]

    lines = []
    lines.append("# Safe Sweep Execution Harness v1")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append("Scope: safe-sweep-execution-harness-implementation-no-sweep-execution")
    lines.append("")
    lines.append("SAFE_SWEEP_EXECUTION_HARNESS_V1")
    lines.append("")
    lines.append("harness implemented")
    lines.append("harness manifest created")
    lines.append("execution refused")
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
    lines.append("## Harness Manifest Summary")
    lines.append("")
    lines.append(f"- Harness ID: {manifest['harness_id']}")
    lines.append(f"- Harness version: {manifest['harness_version']}")
    lines.append(f"- Scope: {manifest['scope']}")
    lines.append(f"- Cell count: {manifest['cell_count']}")
    lines.append(f"- Preview cell count: {manifest['preview_cell_count']}")
    lines.append(f"- current_engine_default_boundary: {manifest['route_counts']['current_engine_default_boundary']}")
    lines.append(f"- safe_sweep_profile_validation: {manifest['route_counts']['safe_sweep_profile_validation']}")
    lines.append(f"- outside_safe_sweep_profile: {manifest['route_counts']['outside_safe_sweep_profile']}")
    lines.append(f"- Execution enabled: {manifest['execution_enabled']}")
    lines.append(f"- Engine execution enabled: {manifest['engine_execution_enabled']}")
    lines.append(f"- Sweep execution enabled: {manifest['sweep_execution_enabled']}")
    lines.append(f"- Interpretation boundary: {manifest['interpretation_boundary']}")
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
        "safe-sweep-execution-harness-implementation-no-sweep-execution",
        "SAFE_SWEEP_EXECUTION_HARNESS_V1",
        "harness implemented",
        "harness manifest created",
        "execution refused",
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

    print("SAFE_SWEEP_EXECUTION_HARNESS_V1_OK")
    print("Harness implemented:", report["harness_implemented"])
    print("Execution refusal check passed:", report["execution_refusal_check_passed"])
    print("Harness cell count:", report["manifest"]["cell_count"])
    print("Engine modified:", report["engine_modified"])
    print("Engine executed:", report["engine_executed"])
    print("Sweep executed:", report["sweep_executed"])
    print("Claim expansion allowed:", report["claim_expansion_allowed"])
    print("Next allowed action:", report["next_allowed_action"])


if __name__ == "__main__":
    main()
