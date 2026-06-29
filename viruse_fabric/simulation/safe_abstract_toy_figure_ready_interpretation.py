from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


def load_ranking_analysis(source_json: Path) -> dict[str, Any]:
    payload = json.loads(source_json.read_text(encoding="utf-8"))
    if payload.get("analysis_kind") != "toy_synthetic_abstract_unitless_non-operational_sensitivity_ranking":
        raise ValueError("Unexpected ranking analysis kind.")
    return payload


def build_figure_ready_rows(source_json: Path) -> list[dict[str, Any]]:
    analysis = load_ranking_analysis(source_json)
    rows = sorted(
        analysis["config_rows"],
        key=lambda row: int(row["pattern_score_rank_desc"]),
    )

    output_rows: list[dict[str, Any]] = []
    top_config = analysis["top_pattern_score_config_id"]
    bottom_config = analysis["bottom_pattern_score_config_id"]
    baseline_config = analysis["baseline_config_id"]

    for row in rows:
        config_id = str(row["config_id"])
        figure_role = "middle"
        if config_id == top_config:
            figure_role = "top"
        elif config_id == bottom_config:
            figure_role = "bottom"
        elif config_id == baseline_config:
            figure_role = "baseline"

        output_rows.append(
            {
                "figure_row_id": f"figure_row_{int(row['pattern_score_rank_desc']):02d}",
                "figure_kind": "toy_synthetic_abstract_unitless_non-operational_ranking",
                "rank": int(row["pattern_score_rank_desc"]),
                "figure_role": figure_role,
                "config_id": config_id,
                "record_count": int(row["record_count"]),
                "fixture_count": int(row["fixture_count"]),
                "mean_final_observation_score": float(row["mean_final_observation_score"]),
                "delta_mean_final_observation_score_vs_baseline": float(
                    row["delta_mean_final_observation_score_vs_baseline"]
                ),
                "mean_targeted_looking_pattern_score": float(
                    row["mean_targeted_looking_pattern_score"]
                ),
                "delta_mean_targeted_looking_pattern_score_vs_baseline": float(
                    row["delta_mean_targeted_looking_pattern_score_vs_baseline"]
                ),
                "pattern_score_range": float(row["pattern_score_range"]),
                "all_safety_passed": bool(row["all_safety_passed"]),
            }
        )

    return output_rows


def build_controlled_interpretation(source_json: Path) -> dict[str, Any]:
    analysis = load_ranking_analysis(source_json)
    rows = build_figure_ready_rows(source_json)

    top_row = next(row for row in rows if row["figure_role"] == "top")
    bottom_row = next(row for row in rows if row["figure_role"] == "bottom")
    baseline_candidates = [row for row in rows if row["config_id"] == analysis["baseline_config_id"]]
    baseline_row = baseline_candidates[0]

    interpretation_lines = [
        "The toy ranking summarizes synthetic, abstract, unitless, non-operational sensitivity outputs.",
        f"The top toy configuration by mean targeted-looking pattern score is {top_row['config_id']}.",
        f"The bottom toy configuration by mean targeted-looking pattern score is {bottom_row['config_id']}.",
        f"The baseline toy configuration is {baseline_row['config_id']} and has zero baseline delta by construction.",
        "The result is a toy interpretation only and is not a biological, empirical, external-validation, or manuscript-readiness claim.",
    ]

    return {
        "interpretation_kind": "toy_synthetic_abstract_unitless_non-operational_figure_ready_interpretation",
        "source_record_count": int(analysis["source_record_count"]),
        "config_summary_count": int(analysis["config_summary_count"]),
        "figure_ready_row_count": len(rows),
        "top_config_id": top_row["config_id"],
        "bottom_config_id": bottom_row["config_id"],
        "baseline_config_id": baseline_row["config_id"],
        "top_mean_targeted_looking_pattern_score": top_row["mean_targeted_looking_pattern_score"],
        "bottom_mean_targeted_looking_pattern_score": bottom_row["mean_targeted_looking_pattern_score"],
        "baseline_mean_targeted_looking_pattern_score": baseline_row["mean_targeted_looking_pattern_score"],
        "all_figure_rows_safety_passed": all(row["all_safety_passed"] for row in rows),
        "interpretation_lines": interpretation_lines,
        "figure_ready_rows": rows,
        "boundary": {
            "real_biological_dataset_import_count": 0,
            "real_pathogen_simulation_count": 0,
            "real_receptor_parameter_count": 0,
            "operational_host_targeting_count": 0,
            "wet_lab_protocol_count": 0,
            "actionable_biosafety_risk_instruction_count": 0,
            "external_validation_count": 0,
            "independent_experiment_count": 0,
            "manuscript_submission_ready_count": 0,
            "new_citation_added_count": 0,
        },
    }


def export_figure_ready_json(output_path: Path, package: dict[str, Any]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(package, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def export_figure_ready_csv(output_path: Path, rows: list[dict[str, Any]]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "figure_row_id",
        "figure_kind",
        "rank",
        "figure_role",
        "config_id",
        "record_count",
        "fixture_count",
        "mean_final_observation_score",
        "delta_mean_final_observation_score_vs_baseline",
        "mean_targeted_looking_pattern_score",
        "delta_mean_targeted_looking_pattern_score_vs_baseline",
        "pattern_score_range",
        "all_safety_passed",
    ]

    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row[field] for field in fieldnames})


def write_figure_ready_exports(source_json: Path, output_json: Path, output_csv: Path) -> dict[str, Any]:
    package = build_controlled_interpretation(source_json)
    rows = package["figure_ready_rows"]
    export_figure_ready_json(output_json, package)
    export_figure_ready_csv(output_csv, rows)

    return {
        "figure_ready_source_record_count": package["source_record_count"],
        "figure_ready_config_summary_count": package["config_summary_count"],
        "figure_ready_row_count": package["figure_ready_row_count"],
        "figure_ready_json_exists": output_json.exists(),
        "figure_ready_csv_exists": output_csv.exists(),
        "top_config_id": package["top_config_id"],
        "bottom_config_id": package["bottom_config_id"],
        "baseline_config_id": package["baseline_config_id"],
        "all_figure_rows_safety_passed": package["all_figure_rows_safety_passed"],
    }
