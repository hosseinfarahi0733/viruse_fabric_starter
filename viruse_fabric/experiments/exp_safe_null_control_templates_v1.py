"""Report safe null-control template implementation.

This artifact implements null-control templates for future safe toy harness
use. It does not execute the engine, does not run a sweep, and does not observe
null-control outcomes.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from viruse_fabric.simulation.viruse_fabric_safe_null_control_templates import (
    NULL_CONTROL_TEMPLATE_VERSION,
    build_safe_null_control_manifest_v1,
)


HARNESS_JSON = Path("outputs/viruse_fabric_safe_sweep_execution_harness_v1.json")
PLAN_JSON = Path("outputs/viruse_fabric_safe_sweep_execution_plan_v1.json")

REPORT_MD = Path("outputs/viruse_fabric_safe_null_control_templates_v1.md")
REPORT_JSON = Path("outputs/viruse_fabric_safe_null_control_templates_v1.json")


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_report() -> Dict[str, Any]:
    harness = _load_json(HARNESS_JSON)
    plan = _load_json(PLAN_JSON)

    assert harness["passed"] is True
    assert harness["next_allowed_action"] == (
        "implement_null_control_templates_for_safe_harness_without_running_sweep"
    )
    assert plan["passed"] is True

    manifest = build_safe_null_control_manifest_v1(preview_pair_count=16)

    counters = {
        "Safe null-control template artifact count": 1,
        "Null-control template implementation count": 1,
        "Null-control template count": manifest["template_count"],
        "Harness cell count": manifest["harness_cell_count"],
        "Planned null-control pair count": manifest["planned_pair_count"],
        "Preview null-control pair count": manifest["preview_pair_count"],
        "Planned expected abstract leak count": manifest["planned_expected_total_abstract_leak_count"],
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
        "artifact": "safe_null_control_templates_v1",
        "scope": "safe-null-control-templates-no-sweep-execution",
        "template_version": NULL_CONTROL_TEMPLATE_VERSION,
        "null_control_templates_implemented": True,
        "null_control_manifest_created": True,
        "engine_modified": False,
        "engine_executed": False,
        "sweep_executed": False,
        "null_controls_executed": False,
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
            "harness": harness["artifact"],
            "plan": plan["artifact"],
        },
        "manifest": manifest,
        "next_allowed_action": "run_safe_null_control_template_regression_without_sweep_execution",
        "counters": counters,
        "passed": True,
        "required_markers": [
            "safe-null-control-templates-no-sweep-execution",
            "SAFE_NULL_CONTROL_TEMPLATES_V1",
            "null-control templates implemented",
            "planned null-control pairs",
            "no null-control execution",
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
    assert report["scope"] == "safe-null-control-templates-no-sweep-execution"
    assert report["template_version"] == "SAFE_NULL_CONTROL_TEMPLATES_V1"
    assert report["null_control_templates_implemented"] is True
    assert report["null_control_manifest_created"] is True
    assert report["engine_modified"] is False
    assert report["engine_executed"] is False
    assert report["sweep_executed"] is False
    assert report["null_controls_executed"] is False
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

    manifest = report["manifest"]
    assert manifest["template_count"] == 4
    assert manifest["harness_cell_count"] == 64
    assert manifest["planned_pair_count"] == 256
    assert manifest["planned_expected_total_abstract_leak_count"] == 0
    assert manifest["execution_enabled_now"] is False
    assert manifest["engine_execution_enabled_now"] is False
    assert manifest["sweep_execution_enabled_now"] is False
    assert manifest["claim_expansion_allowed"] is False
    assert manifest["real_biological_semantics_allowed"] is False

    counters = report["counters"]
    assert counters["Null-control template count"] == 4
    assert counters["Harness cell count"] == 64
    assert counters["Planned null-control pair count"] == 256
    assert counters["Planned expected abstract leak count"] == 0

    must_be_zero = [
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
    manifest = report["manifest"]

    lines = []
    lines.append("# Safe Null-Control Templates v1")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append("Scope: safe-null-control-templates-no-sweep-execution")
    lines.append("")
    lines.append("SAFE_NULL_CONTROL_TEMPLATES_V1")
    lines.append("")
    lines.append("null-control templates implemented")
    lines.append("planned null-control pairs")
    lines.append("There is no null-control execution.")
    lines.append("no null-control execution")
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
    lines.append("## Null-Control Manifest Summary")
    lines.append("")
    lines.append(f"- Template version: {manifest['template_version']}")
    lines.append(f"- Harness version: {manifest['harness_version']}")
    lines.append(f"- Harness cell count: {manifest['harness_cell_count']}")
    lines.append(f"- Template count: {manifest['template_count']}")
    lines.append(f"- Planned pair count: {manifest['planned_pair_count']}")
    lines.append(f"- Preview pair count: {manifest['preview_pair_count']}")
    lines.append(f"- Planned expected abstract leak count: {manifest['planned_expected_total_abstract_leak_count']}")
    lines.append(f"- Interpretation boundary: {manifest['interpretation_boundary']}")
    lines.append("")
    lines.append("## Templates")
    lines.append("")
    for template in manifest["templates"]:
        lines.append(f"- {template['template_id']}: {template['control_family']}")
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
        "safe-null-control-templates-no-sweep-execution",
        "SAFE_NULL_CONTROL_TEMPLATES_V1",
        "null-control templates implemented",
        "planned null-control pairs",
        "no null-control execution",
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

    print("SAFE_NULL_CONTROL_TEMPLATES_V1_OK")
    print("Template count:", report["manifest"]["template_count"])
    print("Harness cell count:", report["manifest"]["harness_cell_count"])
    print("Planned pair count:", report["manifest"]["planned_pair_count"])
    print("Planned expected abstract leak count:", report["manifest"]["planned_expected_total_abstract_leak_count"])
    print("Null controls executed:", report["null_controls_executed"])
    print("Engine executed:", report["engine_executed"])
    print("Sweep executed:", report["sweep_executed"])
    print("Claim expansion allowed:", report["claim_expansion_allowed"])
    print("Next allowed action:", report["next_allowed_action"])


if __name__ == "__main__":
    main()
