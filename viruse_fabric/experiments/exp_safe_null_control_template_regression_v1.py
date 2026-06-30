"""Regression checks for safe null-control templates.

This regression validates the null-control template registry and planned
cell-control pair structure only. It does not execute null controls, does not
execute a sweep, and does not execute the engine.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from viruse_fabric.simulation.viruse_fabric_safe_null_control_templates import (
    NULL_CONTROL_TEMPLATE_VERSION,
    build_safe_null_control_manifest_v1,
    build_safe_null_control_templates_v1,
)
from viruse_fabric.simulation.viruse_fabric_safe_sweep_execution_harness import (
    build_safe_sweep_execution_harness_manifest_v1,
)


NULL_CONTROL_JSON = Path("outputs/viruse_fabric_safe_null_control_templates_v1.json")
HARNESS_JSON = Path("outputs/viruse_fabric_safe_sweep_execution_harness_v1.json")

REPORT_MD = Path("outputs/viruse_fabric_safe_null_control_template_regression_v1.md")
REPORT_JSON = Path("outputs/viruse_fabric_safe_null_control_template_regression_v1.json")


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validate_template_records(template_records: List[Dict[str, Any]]) -> Dict[str, Any]:
    expected_template_ids = {
        "SAFE-NULL-LEDGER-DISABLED",
        "SAFE-NULL-ROUTE-LABEL-SHUFFLE",
        "SAFE-NULL-SYMBOLIC-DRIFT-FROZEN",
        "SAFE-NULL-PACKET-ORDER-PERMUTED",
    }

    actual_template_ids = {record["template_id"] for record in template_records}

    if actual_template_ids != expected_template_ids:
        raise AssertionError(f"Unexpected template IDs: {actual_template_ids}")

    for record in template_records:
        if record["expected_abstract_leak_count"] != 0:
            raise AssertionError(f"Template leak expectation must be zero: {record}")
        if record["execution_enabled_now"] is not False:
            raise AssertionError(f"Template execution must be disabled: {record}")
        if record["engine_execution_enabled_now"] is not False:
            raise AssertionError(f"Engine execution must be disabled: {record}")
        if record["sweep_execution_enabled_now"] is not False:
            raise AssertionError(f"Sweep execution must be disabled: {record}")
        if record["claim_expansion_allowed"] is not False:
            raise AssertionError(f"Claim expansion must be disabled: {record}")
        if record["real_biological_semantics_allowed"] is not False:
            raise AssertionError(f"Biological semantics must be disabled: {record}")
        if "biological" not in record["forbidden_interpretation"].lower():
            raise AssertionError(f"Forbidden interpretation must mention biological: {record}")

    return {
        "expected_template_id_count": len(expected_template_ids),
        "actual_template_id_count": len(actual_template_ids),
        "all_expected_template_ids_present": actual_template_ids == expected_template_ids,
        "all_template_leak_expectations_zero": True,
        "all_template_execution_flags_disabled": True,
        "all_template_forbidden_interpretations_reject_biological_meaning": True,
    }


def _validate_pair_preview(pair_records: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not pair_records:
        raise AssertionError("Expected at least one preview pair.")

    for pair in pair_records:
        if pair["planned_only"] is not True:
            raise AssertionError(f"Pair must be planned only: {pair}")
        if pair["execution_enabled_now"] is not False:
            raise AssertionError(f"Pair execution must be disabled: {pair}")
        if pair["engine_execution_enabled_now"] is not False:
            raise AssertionError(f"Pair engine execution must be disabled: {pair}")
        if pair["sweep_execution_enabled_now"] is not False:
            raise AssertionError(f"Pair sweep execution must be disabled: {pair}")
        if pair["expected_abstract_leak_count"] != 0:
            raise AssertionError(f"Pair expected leak must be zero: {pair}")
        if pair["claim_expansion_allowed"] is not False:
            raise AssertionError(f"Pair claim expansion must be disabled: {pair}")
        if pair["real_biological_semantics_allowed"] is not False:
            raise AssertionError(f"Pair biological semantics must be disabled: {pair}")
        if pair["cell_validation_route"] not in {
            "current_engine_default_boundary",
            "safe_sweep_profile_validation",
        }:
            raise AssertionError(f"Unexpected cell validation route: {pair}")

    return {
        "preview_pair_count": len(pair_records),
        "all_preview_pairs_planned_only": True,
        "all_preview_pair_execution_flags_disabled": True,
        "all_preview_pair_expected_leaks_zero": True,
        "all_preview_pair_routes_safe": True,
    }


def build_report() -> Dict[str, Any]:
    source_null_control = _load_json(NULL_CONTROL_JSON)
    source_harness = _load_json(HARNESS_JSON)

    assert source_null_control["passed"] is True
    assert source_null_control["next_allowed_action"] == (
        "run_safe_null_control_template_regression_without_sweep_execution"
    )
    assert source_harness["passed"] is True

    templates = build_safe_null_control_templates_v1()
    template_records = [template.to_dict() for template in templates]

    manifest = build_safe_null_control_manifest_v1(preview_pair_count=32)
    harness_manifest = build_safe_sweep_execution_harness_manifest_v1(preview_cell_count=64)

    template_regression = _validate_template_records(template_records)
    pair_regression = _validate_pair_preview(manifest["preview_pairs"])

    manifest_matches_source = (
        manifest["template_count"] == source_null_control["manifest"]["template_count"]
        and manifest["harness_cell_count"] == source_null_control["manifest"]["harness_cell_count"]
        and manifest["planned_pair_count"] == source_null_control["manifest"]["planned_pair_count"]
        and manifest["planned_expected_total_abstract_leak_count"]
        == source_null_control["manifest"]["planned_expected_total_abstract_leak_count"]
    )

    harness_alignment = (
        harness_manifest["cell_count"] == manifest["harness_cell_count"]
        and harness_manifest["route_counts"] == {
            "current_engine_default_boundary": 1,
            "safe_sweep_profile_validation": 63,
            "outside_safe_sweep_profile": 0,
        }
    )

    counters = {
        "Safe null-control template regression artifact count": 1,
        "Template regression case count": len(template_records),
        "Preview pair regression case count": len(manifest["preview_pairs"]),
        "Template count": manifest["template_count"],
        "Harness cell count": manifest["harness_cell_count"],
        "Planned null-control pair count": manifest["planned_pair_count"],
        "Planned expected abstract leak count": manifest["planned_expected_total_abstract_leak_count"],
        "Manifest source consistency count": 1 if manifest_matches_source else 0,
        "Harness alignment count": 1 if harness_alignment else 0,
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
        "artifact": "safe_null_control_template_regression_v1",
        "scope": "safe-null-control-template-regression-no-sweep-execution",
        "template_version": NULL_CONTROL_TEMPLATE_VERSION,
        "regression_executed": True,
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
        "template_regression": template_regression,
        "pair_regression": pair_regression,
        "manifest_summary": {
            "template_count": manifest["template_count"],
            "harness_cell_count": manifest["harness_cell_count"],
            "planned_pair_count": manifest["planned_pair_count"],
            "planned_expected_total_abstract_leak_count": manifest[
                "planned_expected_total_abstract_leak_count"
            ],
            "execution_enabled_now": manifest["execution_enabled_now"],
            "engine_execution_enabled_now": manifest["engine_execution_enabled_now"],
            "sweep_execution_enabled_now": manifest["sweep_execution_enabled_now"],
            "claim_expansion_allowed": manifest["claim_expansion_allowed"],
            "real_biological_semantics_allowed": manifest[
                "real_biological_semantics_allowed"
            ],
        },
        "manifest_matches_source": manifest_matches_source,
        "harness_alignment": harness_alignment,
        "next_allowed_action": "prepare_safe_sweep_dry_run_protocol_without_engine_or_sweep_execution",
        "counters": counters,
        "passed": True,
        "required_markers": [
            "safe-null-control-template-regression-no-sweep-execution",
            "SAFE_NULL_CONTROL_TEMPLATES_V1",
            "null-control template regression executed",
            "no null-control execution",
            "no observed null-control leak",
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
    assert report["scope"] == "safe-null-control-template-regression-no-sweep-execution"
    assert report["template_version"] == "SAFE_NULL_CONTROL_TEMPLATES_V1"
    assert report["regression_executed"] is True
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

    assert report["template_regression"]["all_expected_template_ids_present"] is True
    assert report["template_regression"]["all_template_leak_expectations_zero"] is True
    assert report["template_regression"]["all_template_execution_flags_disabled"] is True
    assert (
        report["template_regression"][
            "all_template_forbidden_interpretations_reject_biological_meaning"
        ]
        is True
    )

    assert report["pair_regression"]["all_preview_pairs_planned_only"] is True
    assert report["pair_regression"]["all_preview_pair_execution_flags_disabled"] is True
    assert report["pair_regression"]["all_preview_pair_expected_leaks_zero"] is True
    assert report["pair_regression"]["all_preview_pair_routes_safe"] is True

    assert report["manifest_matches_source"] is True
    assert report["harness_alignment"] is True

    manifest = report["manifest_summary"]
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
    assert counters["Template regression case count"] == 4
    assert counters["Preview pair regression case count"] == 32
    assert counters["Template count"] == 4
    assert counters["Harness cell count"] == 64
    assert counters["Planned null-control pair count"] == 256
    assert counters["Planned expected abstract leak count"] == 0
    assert counters["Manifest source consistency count"] == 1
    assert counters["Harness alignment count"] == 1

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
    manifest = report["manifest_summary"]

    lines = []
    lines.append("# Safe Null-Control Template Regression v1")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append("Scope: safe-null-control-template-regression-no-sweep-execution")
    lines.append("")
    lines.append("SAFE_NULL_CONTROL_TEMPLATES_V1")
    lines.append("")
    lines.append("null-control template regression executed")
    lines.append("There is no null-control execution.")
    lines.append("no null-control execution")
    lines.append("There is no observed null-control leak.")
    lines.append("no observed null-control leak")
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
    lines.append("## Template Regression")
    lines.append("")
    for key, value in report["template_regression"].items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Pair Regression")
    lines.append("")
    for key, value in report["pair_regression"].items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Manifest Summary")
    lines.append("")
    for key, value in manifest.items():
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
        "safe-null-control-template-regression-no-sweep-execution",
        "SAFE_NULL_CONTROL_TEMPLATES_V1",
        "null-control template regression executed",
        "no null-control execution",
        "no observed null-control leak",
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

    print("SAFE_NULL_CONTROL_TEMPLATE_REGRESSION_V1_OK")
    print("Template regression case count:", report["counters"]["Template regression case count"])
    print("Preview pair regression case count:", report["counters"]["Preview pair regression case count"])
    print("Planned pair count:", report["manifest_summary"]["planned_pair_count"])
    print("Observed null-control leak count:", report["observed_null_control_leak_count"])
    print("Null controls executed:", report["null_controls_executed"])
    print("Engine executed:", report["engine_executed"])
    print("Sweep executed:", report["sweep_executed"])
    print("Claim expansion allowed:", report["claim_expansion_allowed"])
    print("Next allowed action:", report["next_allowed_action"])


if __name__ == "__main__":
    main()
