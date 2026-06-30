"""Report safe dry-run manifest builder implementation.

The builder produces metadata only. It does not execute a dry-run, engine,
sweep, or null controls.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from viruse_fabric.simulation.viruse_fabric_safe_dry_run_manifest_builder import (
    SAFE_DRY_RUN_MANIFEST_BUILDER_VERSION,
    build_safe_dry_run_manifest_v1,
)


DRY_RUN_PROTOCOL_REGRESSION_JSON = Path(
    "outputs/viruse_fabric_safe_sweep_dry_run_protocol_regression_v1.json"
)
DRY_RUN_PROTOCOL_JSON = Path("outputs/viruse_fabric_safe_sweep_dry_run_protocol_v1.json")
NULL_CONTROL_REGRESSION_JSON = Path(
    "outputs/viruse_fabric_safe_null_control_template_regression_v1.json"
)
NULL_CONTROL_JSON = Path("outputs/viruse_fabric_safe_null_control_templates_v1.json")
HARNESS_JSON = Path("outputs/viruse_fabric_safe_sweep_execution_harness_v1.json")

REPORT_MD = Path("outputs/viruse_fabric_safe_dry_run_manifest_builder_v1.md")
REPORT_JSON = Path("outputs/viruse_fabric_safe_dry_run_manifest_builder_v1.json")


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_report() -> Dict[str, Any]:
    dry_regression = _load_json(DRY_RUN_PROTOCOL_REGRESSION_JSON)
    dry_protocol = _load_json(DRY_RUN_PROTOCOL_JSON)
    null_regression = _load_json(NULL_CONTROL_REGRESSION_JSON)
    null_templates = _load_json(NULL_CONTROL_JSON)
    harness = _load_json(HARNESS_JSON)

    assert dry_regression["passed"] is True
    assert dry_regression["next_allowed_action"] == (
        "implement_safe_dry_run_manifest_builder_without_engine_or_sweep_execution"
    )
    assert dry_protocol["passed"] is True
    assert null_regression["passed"] is True
    assert null_templates["passed"] is True
    assert harness["passed"] is True

    manifest = build_safe_dry_run_manifest_v1(preview_cell_count=12, preview_pair_count=16)

    source_alignment = (
        manifest["cell_count"] == harness["manifest"]["cell_count"]
        and manifest["planned_null_control_pair_count"]
        == null_templates["manifest"]["planned_pair_count"]
        and manifest["template_count"] == null_templates["manifest"]["template_count"]
        and dry_protocol["dry_run_boundary"]["future_dry_run_may_build_manifest"] is True
        and dry_regression["boundary_regression"]["future_manifest_building_allowed"] is True
    )

    counters = {
        "Safe dry-run manifest builder artifact count": 1,
        "Manifest builder implementation count": 1,
        "Manifest metadata build count": 1,
        "Dry-run manifest cell count": manifest["cell_count"],
        "Dry-run manifest template count": manifest["template_count"],
        "Dry-run manifest planned null-control pair count": manifest[
            "planned_null_control_pair_count"
        ],
        "Dry-run manifest planned expected abstract leak count": manifest[
            "planned_expected_total_abstract_leak_count"
        ],
        "Dry-run manifest preview cell count": manifest["preview_cell_count"],
        "Dry-run manifest preview pair count": manifest["preview_pair_count"],
        "Source alignment count": 1 if source_alignment else 0,
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
        "artifact": "safe_dry_run_manifest_builder_v1",
        "scope": "safe-dry-run-manifest-builder-no-engine-or-sweep-execution",
        "builder_version": SAFE_DRY_RUN_MANIFEST_BUILDER_VERSION,
        "manifest_builder_implemented": True,
        "manifest_metadata_built": True,
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
            "dry_run_protocol_regression": dry_regression["artifact"],
            "dry_run_protocol": dry_protocol["artifact"],
            "null_control_regression": null_regression["artifact"],
            "null_control_templates": null_templates["artifact"],
            "harness": harness["artifact"],
        },
        "source_alignment": source_alignment,
        "manifest": manifest,
        "next_allowed_action": "run_safe_dry_run_manifest_builder_regression_without_engine_or_sweep_execution",
        "counters": counters,
        "passed": True,
        "required_markers": [
            "safe-dry-run-manifest-builder-no-engine-or-sweep-execution",
            "SAFE_DRY_RUN_MANIFEST_BUILDER_V1",
            "dry-run manifest builder implemented",
            "dry-run manifest metadata built",
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
    assert report["scope"] == "safe-dry-run-manifest-builder-no-engine-or-sweep-execution"
    assert report["builder_version"] == "SAFE_DRY_RUN_MANIFEST_BUILDER_V1"
    assert report["manifest_builder_implemented"] is True
    assert report["manifest_metadata_built"] is True
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

    manifest = report["manifest"]
    assert manifest["cell_count"] == 64
    assert manifest["template_count"] == 4
    assert manifest["planned_null_control_pair_count"] == 256
    assert manifest["planned_expected_total_abstract_leak_count"] == 0
    assert manifest["route_counts"] == {
        "current_engine_default_boundary": 1,
        "safe_sweep_profile_validation": 63,
        "outside_safe_sweep_profile": 0,
    }
    assert manifest["dry_run_execution_enabled"] is False
    assert manifest["engine_execution_enabled"] is False
    assert manifest["sweep_execution_enabled"] is False
    assert manifest["null_control_execution_enabled"] is False
    assert manifest["claim_expansion_allowed"] is False
    assert manifest["real_biological_semantics_allowed"] is False
    assert manifest["safe_abstract_toy_only"] is True
    assert manifest["interpretation_boundary"] == "dry_run_manifest_metadata_only_not_evidence"

    counters = report["counters"]
    assert counters["Manifest builder implementation count"] == 1
    assert counters["Manifest metadata build count"] == 1
    assert counters["Dry-run manifest cell count"] == 64
    assert counters["Dry-run manifest template count"] == 4
    assert counters["Dry-run manifest planned null-control pair count"] == 256
    assert counters["Dry-run manifest planned expected abstract leak count"] == 0
    assert counters["Source alignment count"] == 1

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
    manifest = report["manifest"]

    lines = []
    lines.append("# Safe Dry-Run Manifest Builder v1")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append("Scope: safe-dry-run-manifest-builder-no-engine-or-sweep-execution")
    lines.append("")
    lines.append("SAFE_DRY_RUN_MANIFEST_BUILDER_V1")
    lines.append("dry-run manifest builder implemented")
    lines.append("dry-run manifest metadata built")
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
    lines.append("## Manifest Summary")
    lines.append("")
    lines.append(f"- Builder version: {manifest['builder_version']}")
    lines.append(f"- Cell count: {manifest['cell_count']}")
    lines.append(f"- Template count: {manifest['template_count']}")
    lines.append(f"- Planned null-control pair count: {manifest['planned_null_control_pair_count']}")
    lines.append(f"- Planned expected total abstract leak count: {manifest['planned_expected_total_abstract_leak_count']}")
    lines.append(f"- current_engine_default_boundary: {manifest['route_counts']['current_engine_default_boundary']}")
    lines.append(f"- safe_sweep_profile_validation: {manifest['route_counts']['safe_sweep_profile_validation']}")
    lines.append(f"- outside_safe_sweep_profile: {manifest['route_counts']['outside_safe_sweep_profile']}")
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
        "safe-dry-run-manifest-builder-no-engine-or-sweep-execution",
        "SAFE_DRY_RUN_MANIFEST_BUILDER_V1",
        "dry-run manifest builder implemented",
        "dry-run manifest metadata built",
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

    print("SAFE_DRY_RUN_MANIFEST_BUILDER_V1_OK")
    print("Manifest cell count:", report["manifest"]["cell_count"])
    print("Manifest template count:", report["manifest"]["template_count"])
    print("Manifest planned pair count:", report["manifest"]["planned_null_control_pair_count"])
    print("Dry-run executed:", report["dry_run_executed"])
    print("Null controls executed:", report["null_controls_executed"])
    print("Engine executed:", report["engine_executed"])
    print("Sweep executed:", report["sweep_executed"])
    print("Claim expansion allowed:", report["claim_expansion_allowed"])
    print("Next allowed action:", report["next_allowed_action"])


if __name__ == "__main__":
    main()
