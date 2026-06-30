"""Generate safe profile-to-engine validation bridge report.

This validates a bridge between SafeToySweepProfile and the current engine
default boundary. It does not modify engine code and does not execute a sweep.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from viruse_fabric.simulation.viruse_fabric_safe_toy_sweep_profile_engine_validation_bridge import (
    build_validation_bridge_summary_v1,
)


REPORT_MD = Path("outputs/viruse_fabric_safe_profile_engine_validation_bridge_v1.md")
REPORT_JSON = Path("outputs/viruse_fabric_safe_profile_engine_validation_bridge_v1.json")


def build_report() -> Dict[str, Any]:
    summary = build_validation_bridge_summary_v1(preview_record_count=12)

    counters = {
        "Safe profile engine validation bridge artifact count": 1,
        "Profile-to-engine boundary bridge count": 1,
        "Engine modification count": 0,
        "Engine execution count": 0,
        "Sweep execution count": 0,
        "Experiment execution count": 0,
        "Claim expansion count": 0,
        "Validation claim count": 0,
        "Manuscript readiness claim count": 0,
        "Official tag created count": 0,
        "New milestone created count": 0,
        "Baseline-compatible current-engine cell count": summary["baseline_compatible_cell_count"],
        "Sweep-only future-validation cell count": summary["sweep_only_cell_count"],
        "Engine validated parameter count": summary["engine_validated_parameter_count"],
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
        "artifact": "safe_profile_engine_validation_bridge_v1",
        "scope": "safe-profile-to-current-engine-validation-boundary-bridge-only",
        "source_scaffold": "safe_engine_redesign_sweep_profile_scaffold_v1",
        "bridge_created": True,
        "engine_modified": False,
        "engine_executed": False,
        "sweep_executed": False,
        "experiment_executed": False,
        "claim_expansion_allowed": False,
        "validation_claim_made": False,
        "manuscript_readiness_claim_made": False,
        "new_milestone_created": False,
        "new_official_tag_created": False,
        "bridge_summary": summary,
        "next_allowed_action": summary["next_allowed_action"],
        "counters": counters,
        "passed": True,
        "required_markers": [
            "safe-profile-to-current-engine-validation-boundary-bridge-only",
            "profile-to-engine validation bridge",
            "current_engine_default_boundary",
            "future_safe_sweep_profile_validation_required",
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
    assert report["scope"] == "safe-profile-to-current-engine-validation-boundary-bridge-only"
    assert report["bridge_created"] is True
    assert report["engine_modified"] is False
    assert report["engine_executed"] is False
    assert report["sweep_executed"] is False
    assert report["experiment_executed"] is False
    assert report["claim_expansion_allowed"] is False
    assert report["validation_claim_made"] is False
    assert report["manuscript_readiness_claim_made"] is False
    assert report["new_milestone_created"] is False
    assert report["new_official_tag_created"] is False

    summary = report["bridge_summary"]
    assert summary["profile_parameter_count"] == 7
    assert summary["engine_validated_parameter_count"] == 3
    assert summary["baseline_compatible_cell_count"] == 1
    assert summary["sweep_profile_cell_count"] == 64
    assert summary["sweep_only_cell_count"] == 63
    assert summary["default_value_map"] == {
        "node_count": 16,
        "packet_count": 32,
        "step_count_limit": 3,
    }

    assert summary["engine_validated_parameter_values"] == {
        "node_count": [12, 16, 20, 24],
        "packet_count": [24, 32, 40, 48],
        "step_count_limit": [2, 3, 4, 5],
    }

    counters = report["counters"]
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
    summary = report["bridge_summary"]
    counters = report["counters"]

    lines = []
    lines.append("# Safe Profile Engine Validation Bridge v1")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append("This artifact creates a profile-to-engine validation bridge.")
    lines.append("")
    lines.append("Scope: safe-profile-to-current-engine-validation-boundary-bridge-only")
    lines.append("")
    lines.append("The bridge maps SafeToySweepProfile values to the current engine default boundary.")
    lines.append("It does not modify the engine.")
    lines.append("engine not modified")
    lines.append("It does not execute the engine.")
    lines.append("engine not executed")
    lines.append("It does not execute a sweep.")
    lines.append("sweep not executed")
    lines.append("claim expansion remains forbidden.")
    lines.append("No validation claim is made.")
    lines.append("No manuscript readiness claim is made.")
    lines.append("")
    lines.append("## Bridge Summary")
    lines.append("")
    lines.append(f"- Profile ID: {summary['profile_id']}")
    lines.append(f"- Profile scope: {summary['scope']}")
    lines.append(f"- Bridge scope: {summary['bridge_scope']}")
    lines.append(f"- Profile parameter count: {summary['profile_parameter_count']}")
    lines.append(f"- Engine validated parameter count: {summary['engine_validated_parameter_count']}")
    lines.append(f"- Baseline-compatible current-engine cell count: {summary['baseline_compatible_cell_count']}")
    lines.append(f"- Sweep profile cell count: {summary['sweep_profile_cell_count']}")
    lines.append(f"- Sweep-only future-validation cell count: {summary['sweep_only_cell_count']}")
    lines.append("")
    lines.append("## Current Engine Default Boundary")
    lines.append("")
    for key, value in summary["default_value_map"].items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Engine Validated Parameter Values")
    lines.append("")
    for key, values in summary["engine_validated_parameter_values"].items():
        lines.append(f"- {key}: {values}")
    lines.append("")
    lines.append("## Sweep-only Values by Parameter")
    lines.append("")
    for key, values in summary["sweep_only_values_by_parameter"].items():
        lines.append(f"- {key}: {values}")
    lines.append("")
    lines.append("## Preview Bridge Records")
    lines.append("")
    for record in summary["bridge_records_preview"]:
        lines.append(f"- {record['record_id']}: {record['engine_parameter_values']} => {record['validation_route']}")
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
        "profile-to-engine validation bridge",
        "safe-profile-to-current-engine-validation-boundary-bridge-only",
        "current_engine_default_boundary",
        "future_safe_sweep_profile_validation_required",
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

    print("SAFE_PROFILE_ENGINE_VALIDATION_BRIDGE_V1_OK")
    print("Baseline-compatible current-engine cell count:", report["bridge_summary"]["baseline_compatible_cell_count"])
    print("Sweep-only future-validation cell count:", report["bridge_summary"]["sweep_only_cell_count"])
    print("Engine modified:", report["engine_modified"])
    print("Engine executed:", report["engine_executed"])
    print("Sweep executed:", report["sweep_executed"])
    print("Claim expansion allowed:", report["claim_expansion_allowed"])
    print("Next allowed action:", report["next_allowed_action"])


if __name__ == "__main__":
    main()
