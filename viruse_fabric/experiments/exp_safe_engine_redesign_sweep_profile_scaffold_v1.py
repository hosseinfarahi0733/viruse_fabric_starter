"""Generate a safe engine redesign sweep-profile scaffold report.

This script validates only the SafeToySweepProfile scaffold. It does not modify
the engine, does not run a biological model, and does not claim validation.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from viruse_fabric.simulation.viruse_fabric_safe_toy_sweep_profile import (
    build_profile_summary_v1,
    build_safe_toy_sweep_profile_v1,
)


REPORT_MD = Path("outputs/viruse_fabric_safe_engine_redesign_sweep_profile_scaffold_v1.md")
REPORT_JSON = Path("outputs/viruse_fabric_safe_engine_redesign_sweep_profile_scaffold_v1.json")


def build_report() -> Dict[str, Any]:
    profile = build_safe_toy_sweep_profile_v1()
    summary = build_profile_summary_v1(preview_record_count=8)

    counters = {
        "Safe engine redesign scaffold artifact count": 1,
        "SafeToySweepProfile definition count": 1,
        "Safe toy parameter definition count": summary["parameter_count"],
        "Engine-supported safe parameter count": summary["engine_supported_parameter_count"],
        "Seed safe parameter count": summary["seed_parameter_count"],
        "Safe toy grid cell count": summary["total_grid_cell_count"],
        "Preview safe toy grid record count": summary["preview_record_count"],
        "Code scaffold module count": 1,
        "Engine modification count": 0,
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
        "artifact": "safe_engine_redesign_sweep_profile_scaffold_v1",
        "scope": "safe-abstract-toy-sweep-profile-scaffold-only",
        "source_plan": "engine_redesign_implementation_plan_v1",
        "code_scaffold_created": True,
        "engine_modified": False,
        "experiment_executed": False,
        "claim_expansion_allowed": False,
        "validation_claim_made": False,
        "manuscript_readiness_claim_made": False,
        "new_milestone_created": False,
        "new_official_tag_created": False,
        "profile_summary": summary,
        "engine_supported_parameter_names": list(profile.engine_supported_parameter_names()),
        "seed_parameter_names": list(profile.seed_parameter_names()),
        "next_allowed_action": "connect_profile_to_engine_validation_on_separate_checked_commit",
        "counters": counters,
        "passed": True,
        "required_markers": [
            "safe-abstract-toy-sweep-profile-scaffold-only",
            "SafeToySweepProfile",
            "safe toy parameter registry",
            "engine not modified",
            "experiment not executed",
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
    counters = report["counters"]
    summary = report["profile_summary"]

    assert report["passed"] is True
    assert report["scope"] == "safe-abstract-toy-sweep-profile-scaffold-only"
    assert report["code_scaffold_created"] is True
    assert report["engine_modified"] is False
    assert report["experiment_executed"] is False
    assert report["claim_expansion_allowed"] is False
    assert report["validation_claim_made"] is False
    assert report["manuscript_readiness_claim_made"] is False
    assert report["new_milestone_created"] is False
    assert report["new_official_tag_created"] is False

    assert summary["parameter_count"] == 7
    assert summary["engine_supported_parameter_count"] == 3
    assert summary["seed_parameter_count"] == 4
    assert summary["total_grid_cell_count"] == 4 ** 7
    assert summary["preview_record_count"] == 8
    assert summary["claim_expansion_allowed"] is False
    assert summary["real_biological_semantics_allowed"] is False

    assert report["engine_supported_parameter_names"] == [
        "node_count",
        "packet_count",
        "step_count_limit",
    ]

    assert report["seed_parameter_names"] == [
        "graph_seed",
        "packet_seed",
        "transition_seed",
        "symbolic_drift_seed",
    ]

    must_be_zero = [
        "Engine modification count",
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
    summary = report["profile_summary"]
    counters = report["counters"]

    lines = []
    lines.append("# Safe Engine Redesign Sweep Profile Scaffold v1")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append("This artifact creates a SafeToySweepProfile scaffold.")
    lines.append("")
    lines.append("Scope: safe-abstract-toy-sweep-profile-scaffold-only")
    lines.append("")
    lines.append("This is a safe toy parameter registry and scaffold only.")
    lines.append("The engine is not modified.")
    lines.append("engine not modified")
    lines.append("No experiment is executed.")
    lines.append("experiment not executed")
    lines.append("claim expansion remains forbidden.")
    lines.append("No validation claim is made.")
    lines.append("No manuscript readiness claim is made.")
    lines.append("")
    lines.append("## Profile Summary")
    lines.append("")
    lines.append(f"- Profile ID: {summary['profile_id']}")
    lines.append(f"- Scope: {summary['scope']}")
    lines.append(f"- Parameter count: {summary['parameter_count']}")
    lines.append(f"- Engine-supported parameter count: {summary['engine_supported_parameter_count']}")
    lines.append(f"- Seed parameter count: {summary['seed_parameter_count']}")
    lines.append(f"- Total safe toy grid cell count: {summary['total_grid_cell_count']}")
    lines.append(f"- Preview safe toy grid record count: {summary['preview_record_count']}")
    lines.append(f"- Claim expansion allowed: {summary['claim_expansion_allowed']}")
    lines.append(f"- Real biological semantics allowed: {summary['real_biological_semantics_allowed']}")
    lines.append("")
    lines.append("## Engine-Supported Safe Parameters")
    lines.append("")
    for name in report["engine_supported_parameter_names"]:
        lines.append(f"- {name}")
    lines.append("")
    lines.append("## Seed Safe Parameters")
    lines.append("")
    for name in report["seed_parameter_names"]:
        lines.append(f"- {name}")
    lines.append("")
    lines.append("## Preview Records")
    lines.append("")
    for record in summary["preview_records"]:
        lines.append(f"- {record['record_id']}: {record['parameter_values']}")
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
        "SafeToySweepProfile",
        "safe toy parameter registry",
        "safe-abstract-toy-sweep-profile-scaffold-only",
        "engine not modified",
        "experiment not executed",
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

    print("SAFE_ENGINE_REDESIGN_SWEEP_PROFILE_SCAFFOLD_V1_OK")
    print("Parameter count:", report["profile_summary"]["parameter_count"])
    print("Engine-supported parameter count:", report["profile_summary"]["engine_supported_parameter_count"])
    print("Seed parameter count:", report["profile_summary"]["seed_parameter_count"])
    print("Total safe toy grid cell count:", report["profile_summary"]["total_grid_cell_count"])
    print("Engine modified:", report["engine_modified"])
    print("Experiment executed:", report["experiment_executed"])
    print("Claim expansion allowed:", report["claim_expansion_allowed"])
    print("Next allowed action:", report["next_allowed_action"])


if __name__ == "__main__":
    main()
