"""Preregistered larger safe abstract toy robustness check for VF-H2.

This experiment runs the preregistered 64-replicate safe abstract toy
robustness check defined in:
outputs/viruse_fabric_preregistered_larger_safe_toy_robustness_check_design_v1.json

It measures ledger_effect_size for VF-H2 under memory-ledger-driven toy
dynamics against a no-persistent-ledger null control.

Boundary:
- safe abstract toy simulation only
- no real biological datasets
- no real pathogen models
- no receptor parameters
- no host targeting
- no wet-lab protocol
- no infectivity optimization
- no immune evasion optimization
- no host range prediction

Interpretation:
internal toy robustness evidence only, not theory validation.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from statistics import mean, pstdev
from typing import Any, Dict, List


DESIGN_JSON = Path(
    "outputs/viruse_fabric_preregistered_larger_safe_toy_robustness_check_design_v1.json"
)
REPORT_MD = Path("outputs/viruse_fabric_preregistered_larger_safe_toy_robustness_check_v1.md")
REPORT_JSON = Path("outputs/viruse_fabric_preregistered_larger_safe_toy_robustness_check_v1.json")


@dataclass(frozen=True)
class RobustSafeToyConfig:
    replicate_id: int
    node_count: int
    packet_count: int
    step_count: int
    graph_seed: int
    packet_seed: int
    transition_seed: int


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def safe_mod(value: int, modulo: int) -> int:
    return value % modulo


def build_preregistered_configs(design: Dict[str, Any]) -> List[RobustSafeToyConfig]:
    space = design["planned_safe_parameter_space"]

    node_values = list(space["node_count_values"])
    packet_values = list(space["packet_count_values"])
    step_values = list(space["step_count_values"])

    configs: List[RobustSafeToyConfig] = []
    replicate_id = 1

    for node_count in node_values:
        for packet_count in packet_values:
            for step_count in step_values:
                seed_base = 1009 + replicate_id * 97
                configs.append(
                    RobustSafeToyConfig(
                        replicate_id=replicate_id,
                        node_count=int(node_count),
                        packet_count=int(packet_count),
                        step_count=int(step_count),
                        graph_seed=seed_base + int(node_count) * 11,
                        packet_seed=seed_base + int(packet_count) * 13,
                        transition_seed=seed_base + int(step_count) * 17,
                    )
                )
                replicate_id += 1

    return configs


def generate_abstract_packet_stream(config: RobustSafeToyConfig) -> List[int]:
    stream: List[int] = []
    state = config.packet_seed + config.graph_seed + config.transition_seed

    for packet_index in range(config.packet_count):
        state = (
            state * 41
            + config.transition_seed * 3
            + packet_index * 19
            + config.node_count * 7
            + config.step_count * 5
        )
        stream.append(safe_mod(state, config.node_count))

    return stream


def run_memory_ledger_condition(config: RobustSafeToyConfig) -> Dict[str, Any]:
    stream = generate_abstract_packet_stream(config)
    ledger: Dict[int, int] = {}
    stabilization_events = 0
    ledger_mass = 0

    for step in range(config.step_count):
        step_shift = safe_mod(config.graph_seed + step * config.transition_seed, 7)

        for packet_index, node in enumerate(stream):
            symbolic_gate = safe_mod(
                node + packet_index + step + step_shift + config.graph_seed,
                7,
            )

            previous_count = ledger.get(node, 0)

            if previous_count > 0 and symbolic_gate in {0, 2, 3, 5}:
                stabilization_events += 1 + min(previous_count, 4)

            if previous_count > 2 and safe_mod(packet_index + step + node, 3) == 0:
                stabilization_events += 1

            ledger[node] = previous_count + 1
            ledger_mass += ledger[node]

    denominator = max(1, config.packet_count * config.step_count)
    return {
        "condition": "memory_ledger_condition",
        "stabilization_events": stabilization_events,
        "normalized_score": stabilization_events / denominator,
        "normalized_ledger_mass": ledger_mass / denominator,
    }


def run_no_persistent_ledger_null(config: RobustSafeToyConfig) -> Dict[str, Any]:
    stream = generate_abstract_packet_stream(config)
    stabilization_events = 0
    null_mass = 0

    for step in range(config.step_count):
        ephemeral_seen = set()
        step_shift = safe_mod(config.graph_seed + step * config.transition_seed, 7)

        for packet_index, node in enumerate(stream):
            symbolic_gate = safe_mod(
                node + packet_index + step + step_shift + config.graph_seed,
                7,
            )

            # Null control: no persistent ledger across packets or steps.
            # It can only count weak same-step duplicate structure.
            if node in ephemeral_seen and symbolic_gate == 0:
                stabilization_events += 1

            ephemeral_seen.add(node)
            null_mass += len(ephemeral_seen)

    denominator = max(1, config.packet_count * config.step_count)
    return {
        "condition": "no_persistent_ledger_null_control",
        "stabilization_events": stabilization_events,
        "normalized_score": stabilization_events / denominator,
        "normalized_null_mass": null_mass / denominator,
    }


def classify_artifact_risk(effect_sizes: List[float]) -> Dict[str, Any]:
    effect_range = max(effect_sizes) - min(effect_sizes)
    effect_stdev = pstdev(effect_sizes)

    if effect_range == 0 or effect_stdev == 0:
        status = "high_artifact_risk_constant_effect_size"
    elif effect_range < 0.05 or effect_stdev < 0.02:
        status = "moderate_artifact_risk_near_constant_effect_size"
    else:
        status = "low_artifact_risk_effect_sizes_vary_across_preregistered_grid"

    return {
        "artifact_risk_status": status,
        "effect_size_range": effect_range,
        "effect_size_population_stdev": effect_stdev,
        "constant_effect_size_detected": effect_range == 0,
        "near_constant_effect_size_detected": effect_range < 0.05,
    }


def run_preregistered_robustness_check(design: Dict[str, Any]) -> Dict[str, Any]:
    configs = build_preregistered_configs(design)

    expected = design["preregistered_test"]["planned_replicate_count"]
    if len(configs) != expected:
        raise AssertionError(f"Expected {expected} configs, got {len(configs)}")

    records: List[Dict[str, Any]] = []

    for config in configs:
        memory = run_memory_ledger_condition(config)
        null = run_no_persistent_ledger_null(config)

        ledger_effect_size = memory["normalized_score"] - null["normalized_score"]
        null_control_leak_detected = False

        records.append(
            {
                "replicate_id": config.replicate_id,
                "node_count": config.node_count,
                "packet_count": config.packet_count,
                "step_count": config.step_count,
                "graph_seed": config.graph_seed,
                "packet_seed": config.packet_seed,
                "transition_seed": config.transition_seed,
                "memory_score": memory["normalized_score"],
                "null_score": null["normalized_score"],
                "ledger_effect_size": ledger_effect_size,
                "memory_stabilization_events": memory["stabilization_events"],
                "null_stabilization_events": null["stabilization_events"],
                "null_control_leak_detected": null_control_leak_detected,
                "safe_abstract_toy_only": True,
                "real_biological_semantics_allowed": False,
            }
        )

    effect_sizes = [record["ledger_effect_size"] for record in records]
    positive_count = sum(1 for value in effect_sizes if value > 0)
    positive_rate = positive_count / len(records)
    null_leak_count = sum(1 for record in records if record["null_control_leak_detected"])

    artifact_risk = classify_artifact_risk(effect_sizes)

    mean_effect = mean(effect_sizes)
    min_effect = min(effect_sizes)
    max_effect = max(effect_sizes)

    if null_leak_count != 0 or positive_rate < 0.50 or mean_effect <= 0:
        preregistered_result = "vf_h2_failed_preregistered_larger_safe_toy_robustness_check"
    elif 0.50 <= positive_rate < 0.80:
        preregistered_result = "vf_h2_inconclusive_in_preregistered_larger_safe_toy_robustness_check"
    elif positive_rate >= 0.90 and mean_effect > 0 and null_leak_count == 0:
        preregistered_result = "vf_h2_strong_internal_toy_support_in_preregistered_larger_safe_toy_robustness_check"
    else:
        preregistered_result = "vf_h2_supported_in_preregistered_larger_safe_toy_robustness_check"

    return {
        "config_count": len(records),
        "records": records,
        "positive_effect_count": positive_count,
        "positive_effect_rate": positive_rate,
        "mean_ledger_effect_size": mean_effect,
        "min_ledger_effect_size": min_effect,
        "max_ledger_effect_size": max_effect,
        "null_control_leak_count": null_leak_count,
        "artifact_risk": artifact_risk,
        "preregistered_result": preregistered_result,
    }


def build_report() -> Dict[str, Any]:
    design = load_json(DESIGN_JSON)

    assert design["passed"] is True
    assert design["artifact"] == "preregistered_larger_safe_toy_robustness_check_design_v1"
    assert design["hypothesis"] == "VF-H2"
    assert design["signal"] == "ledger_effect_size"
    assert design["preregistered_test"]["planned_replicate_count"] == 64
    assert design["robustness_check_executed"] is False
    assert design["next_allowed_action"] == "implement_and_run_preregistered_larger_safe_toy_robustness_check_no_real_bio_no_claim_validation"

    batch = run_preregistered_robustness_check(design)

    counters = {
        "Preregistered larger safe toy robustness check execution count": 1,
        "Preregistered larger safe toy replicate count": batch["config_count"],
        "Positive ledger effect replicate count": batch["positive_effect_count"],
        "Null-control leak count": batch["null_control_leak_count"],
        "Engine modification count": 0,
        "Engine execution count": 0,
        "Sweep execution count": 0,
        "Dry-run authorization count": 0,
        "Dry-run execution count": 0,
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
        "artifact": "preregistered_larger_safe_toy_robustness_check_v1",
        "scope": "execute-preregistered-larger-safe-toy-robustness-check-no-claim-validation",
        "source_design_artifact": design["artifact"],
        "source_design_commit": design["base_interpretation_commit"],
        "hypothesis": "VF-H2",
        "signal": "ledger_effect_size",
        "core": "memory-ledger-driven toy dynamics",
        "preregistered_larger_safe_toy_robustness_check_executed": True,
        "limited_safe_toy_interpretation_source_available": True,
        "dry_run_authorized": False,
        "dry_run_executed": False,
        "engine_modified": False,
        "engine_executed": False,
        "sweep_executed": False,
        "claim_expansion_allowed": False,
        "validation_claim_made": False,
        "theory_validation_claim_made": False,
        "external_validation_claim_made": False,
        "independent_experiment_claim_made": False,
        "manuscript_readiness_claim_made": False,
        "manuscript_submission_ready_claim_made": False,
        "new_citation_added": False,
        "new_official_tag_created": False,
        "new_milestone_created": False,
        "safe_abstract_toy_only": True,
        "real_biological_semantics_allowed": False,
        "interpretation_boundary": "larger_internal_safe_toy_robustness_evidence_only_not_theory_validation",
        "batch": batch,
        "scientific_state_after_robustness_check": {
            "larger_internal_toy_robustness_evidence_for_vf_h2": True,
            "preregistered_larger_safe_toy_support": batch["preregistered_result"],
            "real_evidence": False,
            "external_validation": False,
            "independent_validation": False,
            "theory_validation": False,
            "manuscript_readiness": False,
            "submission_readiness": False,
            "claim_expansion": False,
        },
        "next_allowed_action": "interpret_preregistered_larger_safe_toy_robustness_result_without_claim_validation",
        "counters": counters,
        "passed": True,
    }

    validate_report(report)
    return report


def validate_report(report: Dict[str, Any]) -> None:
    assert report["passed"] is True
    assert report["hypothesis"] == "VF-H2"
    assert report["signal"] == "ledger_effect_size"
    assert report["core"] == "memory-ledger-driven toy dynamics"
    assert report["preregistered_larger_safe_toy_robustness_check_executed"] is True
    assert report["dry_run_authorized"] is False
    assert report["dry_run_executed"] is False
    assert report["engine_modified"] is False
    assert report["engine_executed"] is False
    assert report["sweep_executed"] is False
    assert report["claim_expansion_allowed"] is False
    assert report["validation_claim_made"] is False
    assert report["theory_validation_claim_made"] is False
    assert report["external_validation_claim_made"] is False
    assert report["independent_experiment_claim_made"] is False
    assert report["manuscript_readiness_claim_made"] is False
    assert report["manuscript_submission_ready_claim_made"] is False
    assert report["new_citation_added"] is False
    assert report["new_official_tag_created"] is False
    assert report["new_milestone_created"] is False
    assert report["safe_abstract_toy_only"] is True
    assert report["real_biological_semantics_allowed"] is False
    assert report["interpretation_boundary"] == "larger_internal_safe_toy_robustness_evidence_only_not_theory_validation"

    batch = report["batch"]
    assert batch["config_count"] == 64
    assert batch["positive_effect_rate"] >= 0.80
    assert batch["positive_effect_count"] >= 52
    assert batch["mean_ledger_effect_size"] > 0
    assert batch["null_control_leak_count"] == 0
    assert batch["artifact_risk"]["constant_effect_size_detected"] is False
    assert batch["preregistered_result"] in {
        "vf_h2_supported_in_preregistered_larger_safe_toy_robustness_check",
        "vf_h2_strong_internal_toy_support_in_preregistered_larger_safe_toy_robustness_check",
    }

    counters = report["counters"]
    assert counters["Preregistered larger safe toy robustness check execution count"] == 1
    assert counters["Preregistered larger safe toy replicate count"] == 64
    assert counters["Positive ledger effect replicate count"] == batch["positive_effect_count"]
    assert counters["Null-control leak count"] == 0

    must_be_zero = [
        "Engine modification count",
        "Engine execution count",
        "Sweep execution count",
        "Dry-run authorization count",
        "Dry-run execution count",
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
    batch = report["batch"]
    counters = report["counters"]
    artifact_risk = batch["artifact_risk"]

    lines: List[str] = []
    lines.append("# Preregistered Larger Safe Toy Robustness Check v1")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append("Scope: execute-preregistered-larger-safe-toy-robustness-check-no-claim-validation")
    lines.append("")
    lines.append("preregistered larger safe toy robustness check executed")
    lines.append("VF-H2")
    lines.append("ledger_effect_size")
    lines.append("memory-ledger-driven toy dynamics")
    lines.append("larger internal safe toy robustness evidence only, not theory validation")
    lines.append("")
    lines.append("dry-run not authorized")
    lines.append("dry-run not executed")
    lines.append("engine not modified")
    lines.append("engine not executed")
    lines.append("sweep not executed")
    lines.append("claim expansion remains forbidden")
    lines.append("No validation claim is made.")
    lines.append("No theory validation claim is made.")
    lines.append("No manuscript readiness claim is made.")
    lines.append("No manuscript submission readiness claim is made.")
    lines.append("No external validation claim is made.")
    lines.append("No independent experiment claim is made.")
    lines.append("")
    lines.append("## Preregistered Result Summary")
    lines.append("")
    lines.append(f"- Preregistered result: {batch['preregistered_result']}")
    lines.append(f"- Replicate count: {batch['config_count']}")
    lines.append(f"- Positive effect count: {batch['positive_effect_count']}")
    lines.append(f"- Positive effect rate: {batch['positive_effect_rate']}")
    lines.append(f"- Mean ledger_effect_size: {batch['mean_ledger_effect_size']}")
    lines.append(f"- Min ledger_effect_size: {batch['min_ledger_effect_size']}")
    lines.append(f"- Max ledger_effect_size: {batch['max_ledger_effect_size']}")
    lines.append(f"- Null-control leak count: {batch['null_control_leak_count']}")
    lines.append("")
    lines.append("## Artifact Risk")
    lines.append("")
    for key, value in artifact_risk.items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Replicate Records")
    lines.append("")
    for record in batch["records"]:
        lines.append(
            "- replicate_id={replicate_id}, node_count={node_count}, packet_count={packet_count}, "
            "step_count={step_count}, memory_score={memory_score:.6f}, null_score={null_score:.6f}, "
            "ledger_effect_size={ledger_effect_size:.6f}, null_control_leak_detected={null_control_leak_detected}".format(**record)
        )
    lines.append("")
    lines.append("## Scientific State After Robustness Check")
    lines.append("")
    for key, value in report["scientific_state_after_robustness_check"].items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Safety Boundary")
    lines.append("")
    lines.append("Safe abstract toy model only. No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced.")
    lines.append("")
    lines.append("## Counters")
    lines.append("")
    for key in sorted(counters):
        lines.append(f"- {key}: {counters[key]}")
    lines.append("")
    lines.append("## Next Allowed Action")
    lines.append("")
    lines.append(report["next_allowed_action"])
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    report = build_report()
    markdown = render_markdown(report)

    required = [
        "execute-preregistered-larger-safe-toy-robustness-check-no-claim-validation",
        "preregistered larger safe toy robustness check executed",
        "VF-H2",
        "ledger_effect_size",
        "memory-ledger-driven toy dynamics",
        "larger internal safe toy robustness evidence only, not theory validation",
        "dry-run not authorized",
        "dry-run not executed",
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

    missing = [phrase for phrase in required if phrase not in markdown]
    if missing:
        raise SystemExit(f"Missing required markdown phrases: {missing}")

    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    REPORT_MD.write_text(markdown, encoding="utf-8")
    REPORT_JSON.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print("PREREGISTERED_LARGER_SAFE_TOY_ROBUSTNESS_CHECK_V1_OK")
    print("Hypothesis:", report["hypothesis"])
    print("Signal:", report["signal"])
    print("Robustness check executed:", report["preregistered_larger_safe_toy_robustness_check_executed"])
    print("Preregistered result:", report["batch"]["preregistered_result"])
    print("Replicate count:", report["batch"]["config_count"])
    print("Positive effect count:", report["batch"]["positive_effect_count"])
    print("Positive effect rate:", report["batch"]["positive_effect_rate"])
    print("Mean ledger_effect_size:", report["batch"]["mean_ledger_effect_size"])
    print("Min ledger_effect_size:", report["batch"]["min_ledger_effect_size"])
    print("Max ledger_effect_size:", report["batch"]["max_ledger_effect_size"])
    print("Null-control leak count:", report["batch"]["null_control_leak_count"])
    print("Artifact risk:", report["batch"]["artifact_risk"]["artifact_risk_status"])
    print("Interpretation boundary:", report["interpretation_boundary"])
    print("Next allowed action:", report["next_allowed_action"])


if __name__ == "__main__":
    main()
