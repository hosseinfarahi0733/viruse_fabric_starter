"""Report safe sweep profile validation route added to the engine module.

This script checks validation-route classification only. It does not execute the
engine and does not execute a sweep.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from viruse_fabric.simulation.viruse_fabric_minimal_safe_toy_simulation_engine import (
    SAFE_SWEEP_PROFILE_VALIDATION_ROUTE_VERSION,
    build_safe_sweep_profile_validation_matrix,
    classify_config_against_safe_sweep_profile,
    validate_config_against_safe_sweep_profile,
)


REPORT_MD = Path("outputs/viruse_fabric_safe_engine_validation_safe_sweep_profile_v1.md")
REPORT_JSON = Path("outputs/viruse_fabric_safe_engine_validation_safe_sweep_profile_v1.json")


def build_report() -> Dict[str, Any]:
    default_config = {
        "node_count": 16,
        "packet_count": 32,
        "step_count_limit": 3,
    }

    safe_sweep_config = {
        "node_count": 12,
        "packet_count": 24,
        "step_count_limit": 2,
    }

    outside_profile_config = {
        "node_count": 999,
        "packet_count": 32,
        "step_count_limit": 3,
    }

    default_result = validate_config_against_safe_sweep_profile(default_config)
    safe_sweep_result = validate_config_against_safe_sweep_profile(safe_sweep_config)
    outside_result = classify_config_against_safe_sweep_profile(outside_profile_config)

    matrix = build_safe_sweep_profile_validation_matrix()

    counters = {
        "Engine validation route extension count": 1,
        "Engine modification count": 1,
        "Engine execution count": 0,
        "Sweep execution count": 0,
        "Experiment execution count": 0,
        "Claim expansion count": 0,
        "Validation claim count": 0,
        "Manuscript readiness claim count": 0,
        "Official tag created count": 0,
        "New milestone created count": 0,
        "Current engine default boundary route count": matrix["route_counts"]["current_engine_default_boundary"],
        "Safe sweep profile validation route count": matrix["route_counts"]["safe_sweep_profile_validation"],
        "Outside safe sweep profile route count": matrix["route_counts"]["outside_safe_sweep_profile"],
        "Matrix record count": matrix["matrix_record_count"],
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
        "artifact": "safe_engine_validation_safe_sweep_profile_v1",
        "scope": "safe-sweep-profile-engine-validation-route-only",
        "route_version": SAFE_SWEEP_PROFILE_VALIDATION_ROUTE_VERSION,
        "engine_validation_route_modified": True,
        "engine_executed": False,
        "sweep_executed": False,
        "experiment_executed": False,
        "claim_expansion_allowed": False,
        "validation_claim_made": False,
        "manuscript_readiness_claim_made": False,
        "new_milestone_created": False,
        "new_official_tag_created": False,
        "default_result": default_result,
        "safe_sweep_result": safe_sweep_result,
        "outside_profile_result": outside_result,
        "validation_matrix_summary": {
            "scope": matrix["scope"],
            "engine_validated_field_count": matrix["engine_validated_field_count"],
            "matrix_record_count": matrix["matrix_record_count"],
            "route_counts": matrix["route_counts"],
        },
        "next_allowed_action": "run_safe_validation_regression_without_sweep_execution",
        "counters": counters,
        "passed": True,
        "required_markers": [
            "safe-sweep-profile-engine-validation-route-only",
            "SAFE_SWEEP_PROFILE_VALIDATION_ROUTE_V1",
            "current_engine_default_boundary",
            "safe_sweep_profile_validation",
            "outside_safe_sweep_profile",
            "engine validation route modified",
            "engine not executed",
            "sweep not executed",
            "claim expansion remains forbidden",
            "No validation claim is made",
            "No manuscript readiness claim is made",
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
    assert report["scope"] == "safe-sweep-profile-engine-validation-route-only"
    assert report["route_version"] == "SAFE_SWEEP_PROFILE_VALIDATION_ROUTE_V1"
    assert report["engine_validation_route_modified"] is True
    assert report["engine_executed"] is False
    assert report["sweep_executed"] is False
    assert report["experiment_executed"] is False
    assert report["claim_expansion_allowed"] is False
    assert report["validation_claim_made"] is False
    assert report["manuscript_readiness_claim_made"] is False
    assert report["new_milestone_created"] is False
    assert report["new_official_tag_created"] is False

    assert report["default_result"]["safe_sweep_profile_validation_passed"] is True
    assert report["default_result"]["validation_route"] == "current_engine_default_boundary"
    assert report["default_result"]["current_engine_default_compatible"] is True

    assert report["safe_sweep_result"]["safe_sweep_profile_validation_passed"] is True
    assert report["safe_sweep_result"]["validation_route"] == "safe_sweep_profile_validation"
    assert report["safe_sweep_result"]["current_engine_default_compatible"] is False

    assert report["outside_profile_result"]["safe_sweep_profile_validation_passed"] is False
    assert report["outside_profile_result"]["validation_route"] == "outside_safe_sweep_profile"

    matrix = report["validation_matrix_summary"]
    assert matrix["engine_validated_field_count"] == 3
    assert matrix["matrix_record_count"] == 64
    assert matrix["route_counts"] == {
        "current_engine_default_boundary": 1,
        "safe_sweep_profile_validation": 63,
        "outside_safe_sweep_profile": 0,
    }

    counters = report["counters"]
    must_be_zero = [
        "Engine execution count",
        "Sweep execution count",
        "Experiment execution count",
        "Claim expansion count",
        "Validation claim count",
        "Manuscript readiness claim count",
        "Official tag created count",
        "New milestone created count",
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
    matrix = report["validation_matrix_summary"]

    lines = []
    lines.append("# Safe Engine Validation for Safe Sweep Profile v1")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append("This artifact modifies the engine validation route.")
    lines.append("")
    lines.append("Scope: safe-sweep-profile-engine-validation-route-only")
    lines.append("")
    lines.append("SAFE_SWEEP_PROFILE_VALIDATION_ROUTE_V1")
    lines.append("")
    lines.append("engine validation route modified")
    lines.append("The engine is not executed.")
    lines.append("engine not executed")
    lines.append("A sweep is not executed.")
    lines.append("sweep not executed")
    lines.append("claim expansion remains forbidden.")
    lines.append("No validation claim is made.")
    lines.append("No manuscript readiness claim is made.")
    lines.append("")
    lines.append("## Route Results")
    lines.append("")
    lines.append(f"- Default config route: {report['default_result']['validation_route']}")
    lines.append(f"- Safe sweep config route: {report['safe_sweep_result']['validation_route']}")
    lines.append(f"- Outside profile config route: {report['outside_profile_result']['validation_route']}")
    lines.append("")
    lines.append("## Matrix Summary")
    lines.append("")
    lines.append(f"- Matrix scope: {matrix['scope']}")
    lines.append(f"- Engine validated field count: {matrix['engine_validated_field_count']}")
    lines.append(f"- Matrix record count: {matrix['matrix_record_count']}")
    lines.append(f"- current_engine_default_boundary: {matrix['route_counts']['current_engine_default_boundary']}")
    lines.append(f"- safe_sweep_profile_validation: {matrix['route_counts']['safe_sweep_profile_validation']}")
    lines.append(f"- outside_safe_sweep_profile: {matrix['route_counts']['outside_safe_sweep_profile']}")
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
        "safe-sweep-profile-engine-validation-route-only",
        "SAFE_SWEEP_PROFILE_VALIDATION_ROUTE_V1",
        "current_engine_default_boundary",
        "safe_sweep_profile_validation",
        "outside_safe_sweep_profile",
        "engine validation route modified",
        "engine not executed",
        "sweep not executed",
        "claim expansion remains forbidden",
        "No validation claim is made",
        "No manuscript readiness claim is made",
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

    print("SAFE_ENGINE_VALIDATION_SAFE_SWEEP_PROFILE_V1_OK")
    print("Default route:", report["default_result"]["validation_route"])
    print("Safe sweep route:", report["safe_sweep_result"]["validation_route"])
    print("Outside profile route:", report["outside_profile_result"]["validation_route"])
    print("Matrix record count:", report["validation_matrix_summary"]["matrix_record_count"])
    print("Engine executed:", report["engine_executed"])
    print("Sweep executed:", report["sweep_executed"])
    print("Claim expansion allowed:", report["claim_expansion_allowed"])
    print("Next allowed action:", report["next_allowed_action"])


if __name__ == "__main__":
    main()
