"""Safe regression tests for the safe sweep profile validation route.

This regression artifact checks validation classification only. It does not
execute the engine, does not execute a sweep, and does not expand claims.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

from viruse_fabric.simulation.viruse_fabric_minimal_safe_toy_simulation_engine import (
    SAFE_SWEEP_PROFILE_VALIDATION_ROUTE_VERSION,
    build_safe_sweep_profile_validation_matrix,
    classify_config_against_safe_sweep_profile,
    validate_config_against_safe_sweep_profile,
)
from viruse_fabric.simulation.viruse_fabric_safe_toy_sweep_profile import (
    build_safe_toy_sweep_profile_v1,
)
from viruse_fabric.simulation.viruse_fabric_safe_toy_sweep_profile_engine_validation_bridge import (
    build_validation_bridge_summary_v1,
)


REPORT_MD = Path("outputs/viruse_fabric_safe_engine_validation_regression_v1.md")
REPORT_JSON = Path("outputs/viruse_fabric_safe_engine_validation_regression_v1.json")


@dataclass(frozen=True)
class ObjectConfig:
    node_count: int
    packet_count: int
    step_count_limit: int


def _expect_route(config: Any, expected_route: str, expected_passed: bool) -> Dict[str, Any]:
    result = classify_config_against_safe_sweep_profile(config)

    if result["validation_route"] != expected_route:
        raise AssertionError(
            f"Expected route {expected_route}, got {result['validation_route']} for {config}"
        )

    if result["safe_sweep_profile_validation_passed"] is not expected_passed:
        raise AssertionError(
            "Unexpected safe_sweep_profile_validation_passed value "
            f"for {config}: {result['safe_sweep_profile_validation_passed']}"
        )

    if result["claim_expansion_allowed"] is not False:
        raise AssertionError("claim_expansion_allowed must remain False.")

    if result["real_biological_semantics_allowed"] is not False:
        raise AssertionError("real_biological_semantics_allowed must remain False.")

    if result["engine_execution_allowed_by_this_check"] is not False:
        raise AssertionError("engine_execution_allowed_by_this_check must remain False.")

    if result["sweep_execution_allowed_by_this_check"] is not False:
        raise AssertionError("sweep_execution_allowed_by_this_check must remain False.")

    return result


def build_report() -> Dict[str, Any]:
    profile = build_safe_toy_sweep_profile_v1()
    profile.validate()

    route_test_records: List[Dict[str, Any]] = []

    route_cases = [
        (
            "default_mapping",
            {"node_count": 16, "packet_count": 32, "step_count_limit": 3},
            "current_engine_default_boundary",
            True,
        ),
        (
            "safe_sweep_mapping",
            {"node_count": 12, "packet_count": 24, "step_count_limit": 2},
            "safe_sweep_profile_validation",
            True,
        ),
        (
            "mixed_safe_sweep_mapping",
            {"node_count": 24, "packet_count": 48, "step_count_limit": 5},
            "safe_sweep_profile_validation",
            True,
        ),
        (
            "default_object",
            ObjectConfig(node_count=16, packet_count=32, step_count_limit=3),
            "current_engine_default_boundary",
            True,
        ),
        (
            "safe_sweep_object",
            ObjectConfig(node_count=20, packet_count=40, step_count_limit=4),
            "safe_sweep_profile_validation",
            True,
        ),
        (
            "outside_profile_mapping",
            {"node_count": 999, "packet_count": 32, "step_count_limit": 3},
            "outside_safe_sweep_profile",
            False,
        ),
        (
            "outside_profile_object",
            ObjectConfig(node_count=16, packet_count=999, step_count_limit=3),
            "outside_safe_sweep_profile",
            False,
        ),
    ]

    for case_id, config, expected_route, expected_passed in route_cases:
        result = _expect_route(config, expected_route, expected_passed)
        route_test_records.append(
            {
                "case_id": case_id,
                "expected_route": expected_route,
                "actual_route": result["validation_route"],
                "expected_passed": expected_passed,
                "actual_passed": result["safe_sweep_profile_validation_passed"],
                "current_engine_default_compatible": result["current_engine_default_compatible"],
                "claim_expansion_allowed": result["claim_expansion_allowed"],
                "engine_execution_allowed_by_this_check": result["engine_execution_allowed_by_this_check"],
                "sweep_execution_allowed_by_this_check": result["sweep_execution_allowed_by_this_check"],
            }
        )

    outside_profile_raise_check_passed = False
    try:
        validate_config_against_safe_sweep_profile(
            {"node_count": 999, "packet_count": 32, "step_count_limit": 3}
        )
    except ValueError:
        outside_profile_raise_check_passed = True

    missing_field_check_passed = False
    try:
        classify_config_against_safe_sweep_profile(
            {"node_count": 16, "packet_count": 32}
        )
    except ValueError:
        missing_field_check_passed = True

    matrix = build_safe_sweep_profile_validation_matrix(profile)
    bridge = build_validation_bridge_summary_v1(preview_record_count=12)

    route_counts = matrix["route_counts"]
    bridge_counts_match_matrix = (
        bridge["baseline_compatible_cell_count"] == route_counts["current_engine_default_boundary"]
        and bridge["sweep_only_cell_count"] == route_counts["safe_sweep_profile_validation"]
        and bridge["sweep_profile_cell_count"] == matrix["matrix_record_count"]
    )

    counters = {
        "Safe engine validation regression artifact count": 1,
        "Regression route case count": len(route_test_records),
        "Default route regression count": sum(
            1 for record in route_test_records if record["actual_route"] == "current_engine_default_boundary"
        ),
        "Safe sweep route regression count": sum(
            1 for record in route_test_records if record["actual_route"] == "safe_sweep_profile_validation"
        ),
        "Outside profile route regression count": sum(
            1 for record in route_test_records if record["actual_route"] == "outside_safe_sweep_profile"
        ),
        "Outside profile raise check count": 1 if outside_profile_raise_check_passed else 0,
        "Missing field raise check count": 1 if missing_field_check_passed else 0,
        "Matrix record count": matrix["matrix_record_count"],
        "Current engine default boundary matrix count": route_counts["current_engine_default_boundary"],
        "Safe sweep profile validation matrix count": route_counts["safe_sweep_profile_validation"],
        "Outside safe sweep profile matrix count": route_counts["outside_safe_sweep_profile"],
        "Bridge matrix consistency count": 1 if bridge_counts_match_matrix else 0,
        "Engine modification count": 0,
        "Engine execution count": 0,
        "Sweep execution count": 0,
        "Experiment execution count": 0,
        "Claim expansion count": 0,
        "Validation claim count": 0,
        "Manuscript readiness claim count": 0,
        "Official tag created count": 0,
        "New milestone created count": 0,
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
        "artifact": "safe_engine_validation_regression_v1",
        "scope": "safe-engine-validation-regression-without-sweep-execution",
        "route_version": SAFE_SWEEP_PROFILE_VALIDATION_ROUTE_VERSION,
        "regression_executed": True,
        "engine_modified": False,
        "engine_executed": False,
        "sweep_executed": False,
        "experiment_executed": False,
        "claim_expansion_allowed": False,
        "validation_claim_made": False,
        "manuscript_readiness_claim_made": False,
        "new_milestone_created": False,
        "new_official_tag_created": False,
        "route_test_records": route_test_records,
        "outside_profile_raise_check_passed": outside_profile_raise_check_passed,
        "missing_field_check_passed": missing_field_check_passed,
        "validation_matrix_summary": {
            "scope": matrix["scope"],
            "engine_validated_field_count": matrix["engine_validated_field_count"],
            "matrix_record_count": matrix["matrix_record_count"],
            "route_counts": route_counts,
        },
        "bridge_counts_match_matrix": bridge_counts_match_matrix,
        "next_allowed_action": "prepare_safe_engine_sweep_execution_plan_without_claim_expansion",
        "counters": counters,
        "passed": True,
        "required_markers": [
            "safe-engine-validation-regression-without-sweep-execution",
            "SAFE_SWEEP_PROFILE_VALIDATION_ROUTE_V1",
            "current_engine_default_boundary",
            "safe_sweep_profile_validation",
            "outside_safe_sweep_profile",
            "regression executed",
            "engine not modified",
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
    assert report["scope"] == "safe-engine-validation-regression-without-sweep-execution"
    assert report["route_version"] == "SAFE_SWEEP_PROFILE_VALIDATION_ROUTE_V1"
    assert report["regression_executed"] is True
    assert report["engine_modified"] is False
    assert report["engine_executed"] is False
    assert report["sweep_executed"] is False
    assert report["experiment_executed"] is False
    assert report["claim_expansion_allowed"] is False
    assert report["validation_claim_made"] is False
    assert report["manuscript_readiness_claim_made"] is False
    assert report["new_milestone_created"] is False
    assert report["new_official_tag_created"] is False

    assert len(report["route_test_records"]) == 7
    assert report["outside_profile_raise_check_passed"] is True
    assert report["missing_field_check_passed"] is True
    assert report["bridge_counts_match_matrix"] is True

    matrix = report["validation_matrix_summary"]
    assert matrix["engine_validated_field_count"] == 3
    assert matrix["matrix_record_count"] == 64
    assert matrix["route_counts"] == {
        "current_engine_default_boundary": 1,
        "safe_sweep_profile_validation": 63,
        "outside_safe_sweep_profile": 0,
    }

    counters = report["counters"]
    assert counters["Regression route case count"] == 7
    assert counters["Default route regression count"] == 2
    assert counters["Safe sweep route regression count"] == 3
    assert counters["Outside profile route regression count"] == 2
    assert counters["Outside profile raise check count"] == 1
    assert counters["Missing field raise check count"] == 1
    assert counters["Bridge matrix consistency count"] == 1

    must_be_zero = [
        "Engine modification count",
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
    lines.append("# Safe Engine Validation Regression v1")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append("Scope: safe-engine-validation-regression-without-sweep-execution")
    lines.append("")
    lines.append("SAFE_SWEEP_PROFILE_VALIDATION_ROUTE_V1")
    lines.append("")
    lines.append("regression executed")
    lines.append("The engine is not modified.")
    lines.append("engine not modified")
    lines.append("The engine is not executed.")
    lines.append("engine not executed")
    lines.append("A sweep is not executed.")
    lines.append("sweep not executed")
    lines.append("claim expansion remains forbidden.")
    lines.append("No validation claim is made.")
    lines.append("No manuscript readiness claim is made.")
    lines.append("")
    lines.append("## Route Test Records")
    lines.append("")
    for record in report["route_test_records"]:
        lines.append(
            f"- {record['case_id']}: expected={record['expected_route']}, actual={record['actual_route']}, passed={record['actual_passed']}"
        )
    lines.append("")
    lines.append("## Error Checks")
    lines.append("")
    lines.append(f"- Outside profile raise check passed: {report['outside_profile_raise_check_passed']}")
    lines.append(f"- Missing field check passed: {report['missing_field_check_passed']}")
    lines.append(f"- Bridge counts match matrix: {report['bridge_counts_match_matrix']}")
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
        "safe-engine-validation-regression-without-sweep-execution",
        "SAFE_SWEEP_PROFILE_VALIDATION_ROUTE_V1",
        "current_engine_default_boundary",
        "safe_sweep_profile_validation",
        "outside_safe_sweep_profile",
        "regression executed",
        "engine not modified",
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

    print("SAFE_ENGINE_VALIDATION_REGRESSION_V1_OK")
    print("Route case count:", len(report["route_test_records"]))
    print("Matrix record count:", report["validation_matrix_summary"]["matrix_record_count"])
    print("Default route count:", report["validation_matrix_summary"]["route_counts"]["current_engine_default_boundary"])
    print("Safe sweep route count:", report["validation_matrix_summary"]["route_counts"]["safe_sweep_profile_validation"])
    print("Outside profile route count:", report["validation_matrix_summary"]["route_counts"]["outside_safe_sweep_profile"])
    print("Engine modified:", report["engine_modified"])
    print("Engine executed:", report["engine_executed"])
    print("Sweep executed:", report["sweep_executed"])
    print("Claim expansion allowed:", report["claim_expansion_allowed"])
    print("Next allowed action:", report["next_allowed_action"])


if __name__ == "__main__":
    main()
