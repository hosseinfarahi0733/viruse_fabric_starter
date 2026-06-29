from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from viruse_fabric.safety.toy_fixture_catalog import get_fixture_catalog_payloads
from viruse_fabric.simulation.safe_abstract_toy_dynamics_kernel import (
    ToyKernelConfig,
    run_toy_kernel,
)


@dataclass(frozen=True)
class ToySensitivityConfig:
    config_id: str
    interpretation: str
    kernel_config: ToyKernelConfig


def build_sensitivity_configs() -> tuple[ToySensitivityConfig, ...]:
    return (
        ToySensitivityConfig(
            config_id="toy_sweep_baseline",
            interpretation="baseline toy synthetic abstract unitless non-operational configuration",
            kernel_config=ToyKernelConfig(),
        ),
        ToySensitivityConfig(
            config_id="toy_sweep_compatibility_weight_high",
            interpretation="higher abstract compatibility weight in toy non-operational configuration",
            kernel_config=ToyKernelConfig(
                compatibility_weight=0.50,
                transport_weight=0.20,
                capacity_weight=0.15,
                defense_weight=0.30,
                memory_weight=0.10,
            ),
        ),
        ToySensitivityConfig(
            config_id="toy_sweep_transport_weight_high",
            interpretation="higher abstract transport weight in toy non-operational configuration",
            kernel_config=ToyKernelConfig(
                compatibility_weight=0.30,
                transport_weight=0.45,
                capacity_weight=0.15,
                defense_weight=0.30,
                memory_weight=0.10,
            ),
        ),
        ToySensitivityConfig(
            config_id="toy_sweep_capacity_weight_high",
            interpretation="higher abstract capacity weight in toy non-operational configuration",
            kernel_config=ToyKernelConfig(
                compatibility_weight=0.30,
                transport_weight=0.20,
                capacity_weight=0.40,
                defense_weight=0.30,
                memory_weight=0.10,
            ),
        ),
        ToySensitivityConfig(
            config_id="toy_sweep_defense_weight_high",
            interpretation="higher abstract defense weight in toy non-operational configuration",
            kernel_config=ToyKernelConfig(
                compatibility_weight=0.35,
                transport_weight=0.25,
                capacity_weight=0.20,
                defense_weight=0.50,
                memory_weight=0.10,
            ),
        ),
    )


def build_sensitivity_records() -> list[dict[str, Any]]:
    fixtures = get_fixture_catalog_payloads()
    configs = build_sensitivity_configs()

    records: list[dict[str, Any]] = []
    run_index = 1

    for config in configs:
        for fixture in fixtures:
            result = run_toy_kernel(fixture, config=config.kernel_config)
            result_data = asdict(result)

            records.append(
                {
                    "sweep_run_id": f"toy_sensitivity_run_{run_index:03d}",
                    "sweep_kind": "toy_synthetic_abstract_unitless_non-operational",
                    "config_id": config.config_id,
                    "config_interpretation": config.interpretation,
                    "fixture_id": result_data["fixture_id"],
                    "step_count": result_data["step_count"],
                    "node_count": result_data["node_count"],
                    "edge_count": result_data["edge_count"],
                    "agent_count": result_data["agent_count"],
                    "final_activity_sum": result_data["final_activity_sum"],
                    "final_observation_score": result_data["final_observation_score"],
                    "targeted_looking_pattern_score": result_data[
                        "targeted_looking_pattern_score"
                    ],
                    "passed_safety_guard": result_data["passed_safety_guard"],
                    "compatibility_weight": config.kernel_config.compatibility_weight,
                    "transport_weight": config.kernel_config.transport_weight,
                    "capacity_weight": config.kernel_config.capacity_weight,
                    "defense_weight": config.kernel_config.defense_weight,
                    "memory_weight": config.kernel_config.memory_weight,
                    "activity_decay": config.kernel_config.activity_decay,
                }
            )
            run_index += 1

    return records


def summarize_sensitivity_records(records: list[dict[str, Any]]) -> dict[str, Any]:
    if not records:
        return {
            "toy_sensitivity_record_count": 0,
            "toy_sensitivity_config_count": 0,
            "toy_sensitivity_fixture_count": 0,
            "toy_sensitivity_all_safety_passed": False,
            "mean_final_observation_score": 0.0,
            "mean_targeted_looking_pattern_score": 0.0,
            "max_targeted_looking_pattern_score": 0.0,
            "min_targeted_looking_pattern_score": 0.0,
            "pattern_score_range": 0.0,
        }

    observation_scores = [
        float(record["final_observation_score"]) for record in records
    ]
    pattern_scores = [
        float(record["targeted_looking_pattern_score"]) for record in records
    ]
    config_ids = {str(record["config_id"]) for record in records}
    fixture_ids = {str(record["fixture_id"]) for record in records}

    max_pattern = max(pattern_scores)
    min_pattern = min(pattern_scores)

    return {
        "toy_sensitivity_record_count": len(records),
        "toy_sensitivity_config_count": len(config_ids),
        "toy_sensitivity_fixture_count": len(fixture_ids),
        "toy_sensitivity_all_safety_passed": all(
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
        "max_targeted_looking_pattern_score": round(max_pattern, 6),
        "min_targeted_looking_pattern_score": round(min_pattern, 6),
        "pattern_score_range": round(max_pattern - min_pattern, 6),
    }


def export_sensitivity_json(json_path: Path, records: list[dict[str, Any]]) -> None:
    payload = {
        "export_kind": "toy_synthetic_abstract_unitless_non-operational_sensitivity_sweep",
        "records": records,
        "metrics_summary": summarize_sensitivity_records(records),
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

    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def export_sensitivity_csv(csv_path: Path, records: list[dict[str, Any]]) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "sweep_run_id",
        "sweep_kind",
        "config_id",
        "fixture_id",
        "step_count",
        "node_count",
        "edge_count",
        "agent_count",
        "final_activity_sum",
        "final_observation_score",
        "targeted_looking_pattern_score",
        "passed_safety_guard",
        "compatibility_weight",
        "transport_weight",
        "capacity_weight",
        "defense_weight",
        "memory_weight",
        "activity_decay",
    ]

    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow({field: record[field] for field in fieldnames})


def write_sensitivity_exports(json_path: Path, csv_path: Path) -> dict[str, Any]:
    records = build_sensitivity_records()
    export_sensitivity_json(json_path, records)
    export_sensitivity_csv(csv_path, records)
    summary = summarize_sensitivity_records(records)

    return {
        "toy_sensitivity_export_record_count": len(records),
        "toy_sensitivity_json_export_path": str(json_path),
        "toy_sensitivity_csv_export_path": str(csv_path),
        "toy_sensitivity_json_export_exists": json_path.exists(),
        "toy_sensitivity_csv_export_exists": csv_path.exists(),
        **summary,
    }
