from __future__ import annotations

import csv
import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from viruse_fabric.safety.toy_fixture_catalog import get_fixture_catalog_payloads
from viruse_fabric.simulation.safe_abstract_toy_dynamics_kernel import (
    run_toy_kernel_catalog,
    summarize_kernel_results,
)


def build_toy_run_records() -> list[dict[str, Any]]:
    fixtures = get_fixture_catalog_payloads()
    results = run_toy_kernel_catalog(fixtures)

    records: list[dict[str, Any]] = []
    for index, result in enumerate(results, start=1):
        row = asdict(result)
        row["run_id"] = f"toy_run_{index:03d}"
        row["run_kind"] = "toy_synthetic_abstract_unitless_non-operational"
        records.append(row)

    return records


def build_toy_run_metrics_summary(records: list[dict[str, Any]]) -> dict[str, Any]:
    if not records:
        return {
            "toy_run_record_count": 0,
            "toy_run_all_safety_passed": False,
            "mean_final_observation_score": 0.0,
            "mean_targeted_looking_pattern_score": 0.0,
            "max_targeted_looking_pattern_score": 0.0,
            "min_targeted_looking_pattern_score": 0.0,
        }

    observation_scores = [
        float(record["final_observation_score"]) for record in records
    ]
    pattern_scores = [
        float(record["targeted_looking_pattern_score"]) for record in records
    ]

    return {
        "toy_run_record_count": len(records),
        "toy_run_all_safety_passed": all(
            bool(record["passed_safety_guard"]) for record in records
        ),
        "mean_final_observation_score": round(
            sum(observation_scores) / len(observation_scores),
            6,
        ),
        "mean_targeted_looking_pattern_score": round(
            sum(pattern_scores) / len(pattern_scores),
            6,
        ),
        "max_targeted_looking_pattern_score": round(max(pattern_scores), 6),
        "min_targeted_looking_pattern_score": round(min(pattern_scores), 6),
    }


def export_toy_run_json(json_path: Path, records: list[dict[str, Any]]) -> None:
    payload = {
        "export_kind": "toy_synthetic_abstract_unitless_non-operational",
        "records": records,
        "metrics_summary": build_toy_run_metrics_summary(records),
        "boundary": {
            "real_biological_dataset_import_count": 0,
            "real_pathogen_simulation_count": 0,
            "real_receptor_parameter_count": 0,
            "operational_host_targeting_count": 0,
            "wet_lab_protocol_count": 0,
            "actionable_biosafety_risk_instruction_count": 0,
        },
    }

    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def export_toy_run_csv(csv_path: Path, records: list[dict[str, Any]]) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "run_id",
        "run_kind",
        "fixture_id",
        "step_count",
        "node_count",
        "edge_count",
        "agent_count",
        "final_activity_sum",
        "final_observation_score",
        "targeted_looking_pattern_score",
        "passed_safety_guard",
    ]

    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow({field: record[field] for field in fieldnames})


def write_toy_run_exports(json_path: Path, csv_path: Path) -> dict[str, Any]:
    records = build_toy_run_records()
    export_toy_run_json(json_path, records)
    export_toy_run_csv(csv_path, records)

    kernel_summary = summarize_kernel_results(run_toy_kernel_catalog(get_fixture_catalog_payloads()))
    metrics_summary = build_toy_run_metrics_summary(records)

    return {
        "toy_run_export_record_count": len(records),
        "toy_run_json_export_path": str(json_path),
        "toy_run_csv_export_path": str(csv_path),
        "toy_run_json_export_exists": json_path.exists(),
        "toy_run_csv_export_exists": csv_path.exists(),
        "toy_run_all_safety_passed": metrics_summary["toy_run_all_safety_passed"],
        "mean_final_observation_score": metrics_summary["mean_final_observation_score"],
        "mean_targeted_looking_pattern_score": metrics_summary[
            "mean_targeted_looking_pattern_score"
        ],
        "kernel_result_count": kernel_summary["toy_kernel_result_count"],
    }
