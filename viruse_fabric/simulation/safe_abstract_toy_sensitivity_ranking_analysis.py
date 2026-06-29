from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


BASELINE_CONFIG_ID = "toy_sweep_baseline"


def load_sensitivity_payload(json_path: Path) -> dict[str, Any]:
    payload = json.loads(json_path.read_text(encoding="utf-8"))
    if payload.get("export_kind") != "toy_synthetic_abstract_unitless_non-operational_sensitivity_sweep":
        raise ValueError("Unexpected toy sensitivity export kind.")
    return payload


def load_sensitivity_records(json_path: Path) -> list[dict[str, Any]]:
    payload = load_sensitivity_payload(json_path)
    records = payload.get("records", [])
    if not isinstance(records, list):
        raise ValueError("Toy sensitivity records must be a list.")
    return records


def summarize_by_config(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        groups[str(record["config_id"])].append(record)

    rows: list[dict[str, Any]] = []
    for config_id, group in sorted(groups.items()):
        observation_scores = [float(row["final_observation_score"]) for row in group]
        pattern_scores = [float(row["targeted_looking_pattern_score"]) for row in group]

        rows.append(
            {
                "config_id": config_id,
                "fixture_count": len({str(row["fixture_id"]) for row in group}),
                "record_count": len(group),
                "all_safety_passed": all(bool(row["passed_safety_guard"]) for row in group),
                "mean_final_observation_score": round(sum(observation_scores) / len(observation_scores), 6),
                "mean_targeted_looking_pattern_score": round(sum(pattern_scores) / len(pattern_scores), 6),
                "max_targeted_looking_pattern_score": round(max(pattern_scores), 6),
                "min_targeted_looking_pattern_score": round(min(pattern_scores), 6),
                "pattern_score_range": round(max(pattern_scores) - min(pattern_scores), 6),
            }
        )

    return rows


def add_baseline_deltas(config_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    baseline_rows = [row for row in config_rows if row["config_id"] == BASELINE_CONFIG_ID]
    if len(baseline_rows) != 1:
        raise ValueError("Expected exactly one baseline config row.")

    baseline = baseline_rows[0]
    baseline_observation = float(baseline["mean_final_observation_score"])
    baseline_pattern = float(baseline["mean_targeted_looking_pattern_score"])

    output: list[dict[str, Any]] = []
    for row in config_rows:
        enriched = dict(row)
        enriched["delta_mean_final_observation_score_vs_baseline"] = round(
            float(row["mean_final_observation_score"]) - baseline_observation,
            6,
        )
        enriched["delta_mean_targeted_looking_pattern_score_vs_baseline"] = round(
            float(row["mean_targeted_looking_pattern_score"]) - baseline_pattern,
            6,
        )
        output.append(enriched)

    ranked = sorted(
        output,
        key=lambda row: float(row["mean_targeted_looking_pattern_score"]),
        reverse=True,
    )

    for rank, row in enumerate(ranked, start=1):
        row["pattern_score_rank_desc"] = rank

    return sorted(ranked, key=lambda row: row["config_id"])


def build_ranking_analysis(json_path: Path) -> dict[str, Any]:
    payload = load_sensitivity_payload(json_path)
    records = payload["records"]

    config_rows = summarize_by_config(records)
    ranked_rows = add_baseline_deltas(config_rows)

    sorted_by_rank = sorted(ranked_rows, key=lambda row: int(row["pattern_score_rank_desc"]))
    top_config = sorted_by_rank[0]
    bottom_config = sorted_by_rank[-1]

    return {
        "analysis_kind": "toy_synthetic_abstract_unitless_non-operational_sensitivity_ranking",
        "source_record_count": len(records),
        "config_summary_count": len(ranked_rows),
        "baseline_config_id": BASELINE_CONFIG_ID,
        "top_pattern_score_config_id": top_config["config_id"],
        "bottom_pattern_score_config_id": bottom_config["config_id"],
        "top_mean_targeted_looking_pattern_score": top_config["mean_targeted_looking_pattern_score"],
        "bottom_mean_targeted_looking_pattern_score": bottom_config["mean_targeted_looking_pattern_score"],
        "config_rows": ranked_rows,
        "boundary": {
            "real_biological_dataset_import_count": 0,
            "real_pathogen_simulation_count": 0,
            "real_receptor_parameter_count": 0,
            "operational_host_targeting_count": 0,
            "wet_lab_protocol_count": 0,
            "actionable_biosafety_risk_instruction_count": 0,
            "external_validation_count": 0,
            "manuscript_submission_ready_count": 0,
            "new_citation_added_count": 0,
        },
    }


def export_ranking_json(output_path: Path, analysis: dict[str, Any]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(analysis, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def export_ranking_csv(output_path: Path, analysis: dict[str, Any]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "config_id",
        "pattern_score_rank_desc",
        "fixture_count",
        "record_count",
        "all_safety_passed",
        "mean_final_observation_score",
        "mean_targeted_looking_pattern_score",
        "max_targeted_looking_pattern_score",
        "min_targeted_looking_pattern_score",
        "pattern_score_range",
        "delta_mean_final_observation_score_vs_baseline",
        "delta_mean_targeted_looking_pattern_score_vs_baseline",
    ]

    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in sorted(analysis["config_rows"], key=lambda item: int(item["pattern_score_rank_desc"])):
            writer.writerow({field: row[field] for field in fieldnames})


def write_ranking_exports(source_json_path: Path, output_json_path: Path, output_csv_path: Path) -> dict[str, Any]:
    analysis = build_ranking_analysis(source_json_path)
    export_ranking_json(output_json_path, analysis)
    export_ranking_csv(output_csv_path, analysis)
    return {
        "ranking_analysis_record_count": analysis["source_record_count"],
        "ranking_analysis_config_count": analysis["config_summary_count"],
        "ranking_json_exists": output_json_path.exists(),
        "ranking_csv_exists": output_csv_path.exists(),
        "top_pattern_score_config_id": analysis["top_pattern_score_config_id"],
        "bottom_pattern_score_config_id": analysis["bottom_pattern_score_config_id"],
        "all_config_rows_safety_passed": all(row["all_safety_passed"] for row in analysis["config_rows"]),
    }
