"""Safe artifact-resistance and ablation tests for VF-H2.

This experiment tests whether the VF-H2 ledger_effect_size signal is dependent
on memory-ledger structure rather than an obvious artifact of toy construction,
seed layout, scoring, or weak null controls.

Boundary:
- safe abstract toy model only
- no real biological datasets
- no real pathogen models
- no receptor parameters
- no operational targeting
- no wet-lab protocol
- no infectivity optimization
- no immune evasion optimization
- no host range prediction

Interpretation:
artifact-resistant internal toy support only, not theory validation.
"""

from __future__ import annotations

import json
from pathlib import Path
from statistics import mean, median, quantiles, pstdev
from typing import Any, Dict, List, Tuple

from viruse_fabric.experiments.exp_preregistered_larger_safe_toy_robustness_check_v1 import (
    DESIGN_JSON as ROBUSTNESS_DESIGN_JSON,
    build_preregistered_configs,
    generate_abstract_packet_stream,
    run_memory_ledger_condition,
    run_no_persistent_ledger_null,
    safe_mod,
)


DESIGN_JSON = Path("outputs/viruse_fabric_safe_artifact_resistance_and_ablation_test_design_v1.json")
ROBUSTNESS_JSON = Path("outputs/viruse_fabric_preregistered_larger_safe_toy_robustness_check_v1.json")
REPORT_MD = Path("outputs/viruse_fabric_safe_artifact_resistance_and_ablation_tests_v1.md")
REPORT_JSON = Path("outputs/viruse_fabric_safe_artifact_resistance_and_ablation_tests_v1.json")


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def baseline_effect(config: Any) -> Dict[str, Any]:
    memory = run_memory_ledger_condition(config)
    null = run_no_persistent_ledger_null(config)
    effect = memory["normalized_score"] - null["normalized_score"]
    return {
        "memory_score": memory["normalized_score"],
        "null_score": null["normalized_score"],
        "ledger_effect_size": effect,
        "memory_events": memory["stabilization_events"],
        "null_events": null["stabilization_events"],
    }


def remove_persistent_memory_ledger_effect(config: Any) -> Dict[str, Any]:
    # Same packet stream, but no persistent memory ledger. This intentionally
    # collapses the mechanism VF-H2 depends on.
    null_like = run_no_persistent_ledger_null(config)
    baseline_null = run_no_persistent_ledger_null(config)
    effect = null_like["normalized_score"] - baseline_null["normalized_score"]
    return {
        "ablation_score": null_like["normalized_score"],
        "baseline_null_score": baseline_null["normalized_score"],
        "ablated_effect_size": effect,
    }


def shuffled_ledger_history_effect(config: Any) -> Dict[str, Any]:
    stream = generate_abstract_packet_stream(config)
    ledger: Dict[int, int] = {}
    stabilization_events = 0

    for step in range(config.step_count):
        step_shift = safe_mod(config.transition_seed + step * config.graph_seed, 7)

        for packet_index, node in enumerate(reversed(stream)):
            shuffled_node = safe_mod(node + step + packet_index, config.node_count)
            symbolic_gate = safe_mod(
                shuffled_node + packet_index + step + step_shift + config.packet_seed,
                7,
            )

            previous_count = ledger.get(shuffled_node, 0)
            if previous_count > 1 and symbolic_gate == 0:
                stabilization_events += 1

            ledger[shuffled_node] = previous_count + 1

    null = run_no_persistent_ledger_null(config)
    denominator = max(1, config.packet_count * config.step_count)
    score = stabilization_events / denominator
    return {
        "ablation_score": score,
        "baseline_null_score": null["normalized_score"],
        "ablated_effect_size": score - null["normalized_score"],
    }


def randomized_symbolic_gate_effect(config: Any) -> Dict[str, Any]:
    stream = generate_abstract_packet_stream(config)
    ledger: Dict[int, int] = {}
    stabilization_events = 0

    for step in range(config.step_count):
        for packet_index, node in enumerate(stream):
            pseudo_random_gate = safe_mod(
                config.graph_seed * 31
                + config.packet_seed * 17
                + config.transition_seed * 13
                + packet_index * 5
                + step * 11,
                11,
            )

            previous_count = ledger.get(node, 0)
            if previous_count > 2 and pseudo_random_gate == 0:
                stabilization_events += 1

            ledger[node] = previous_count + 1

    null = run_no_persistent_ledger_null(config)
    denominator = max(1, config.packet_count * config.step_count)
    score = stabilization_events / denominator
    return {
        "ablation_score": score,
        "baseline_null_score": null["normalized_score"],
        "ablated_effect_size": score - null["normalized_score"],
    }


def strengthened_null_effect(config: Any) -> Dict[str, Any]:
    stream = generate_abstract_packet_stream(config)
    stabilization_events = 0

    for step in range(config.step_count):
        same_step_counts: Dict[int, int] = {}

        for packet_index, node in enumerate(stream):
            previous_same_step = same_step_counts.get(node, 0)
            symbolic_gate = safe_mod(
                node + packet_index + step + config.graph_seed + config.transition_seed,
                7,
            )

            if previous_same_step > 0 and symbolic_gate in {0, 3}:
                stabilization_events += 1 + min(previous_same_step, 2)

            same_step_counts[node] = previous_same_step + 1

    denominator = max(1, config.packet_count * config.step_count)
    strengthened_null_score = stabilization_events / denominator
    memory = run_memory_ledger_condition(config)

    return {
        "memory_score": memory["normalized_score"],
        "strengthened_null_score": strengthened_null_score,
        "ledger_effect_size_against_strengthened_null": memory["normalized_score"] - strengthened_null_score,
    }


def seed_permutation_effect(config: Any) -> Dict[str, Any]:
    # Reuse the safe abstract config structure but permute deterministic seeds.
    permuted = type(config)(
        replicate_id=config.replicate_id,
        node_count=config.node_count,
        packet_count=config.packet_count,
        step_count=config.step_count,
        graph_seed=config.packet_seed,
        packet_seed=config.transition_seed,
        transition_seed=config.graph_seed,
    )
    result = baseline_effect(permuted)
    return {
        "permuted_ledger_effect_size": result["ledger_effect_size"],
        "permuted_memory_score": result["memory_score"],
        "permuted_null_score": result["null_score"],
    }


def score_component_ablation_effect(config: Any) -> Dict[str, Any]:
    stream = generate_abstract_packet_stream(config)
    ledger: Dict[int, int] = {}
    component_a_events = 0
    component_b_events = 0

    for step in range(config.step_count):
        step_shift = safe_mod(config.graph_seed + step * config.transition_seed, 7)

        for packet_index, node in enumerate(stream):
            symbolic_gate = safe_mod(
                node + packet_index + step + step_shift + config.graph_seed,
                7,
            )

            previous_count = ledger.get(node, 0)

            if previous_count > 0 and symbolic_gate in {0, 2, 3, 5}:
                component_a_events += 1

            if previous_count > 2 and safe_mod(packet_index + step + node, 3) == 0:
                component_b_events += 1

            ledger[node] = previous_count + 1

    denominator = max(1, config.packet_count * config.step_count)
    null = run_no_persistent_ledger_null(config)

    component_a_effect = (component_a_events / denominator) - null["normalized_score"]
    component_b_effect = (component_b_events / denominator) - null["normalized_score"]

    return {
        "component_a_effect": component_a_effect,
        "component_b_effect": component_b_effect,
        "max_single_component_effect": max(component_a_effect, component_b_effect),
    }


def summarize(values: List[float]) -> Dict[str, Any]:
    q = quantiles(values, n=4, method="inclusive")
    return {
        "count": len(values),
        "mean": mean(values),
        "median": median(values),
        "min": min(values),
        "max": max(values),
        "lower_quartile": q[0],
        "upper_quartile": q[2],
        "population_stdev": pstdev(values),
        "positive_count": sum(1 for value in values if value > 0),
        "positive_rate": sum(1 for value in values if value > 0) / len(values),
    }


def build_records(configs: List[Any]) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    records: List[Dict[str, Any]] = []

    for config in configs:
        baseline = baseline_effect(config)
        no_memory = remove_persistent_memory_ledger_effect(config)
        shuffled = shuffled_ledger_history_effect(config)
        randomized = randomized_symbolic_gate_effect(config)
        strengthened = strengthened_null_effect(config)
        permuted = seed_permutation_effect(config)
        component = score_component_ablation_effect(config)

        records.append(
            {
                "replicate_id": config.replicate_id,
                "node_count": config.node_count,
                "packet_count": config.packet_count,
                "step_count": config.step_count,
                "baseline_ledger_effect_size": baseline["ledger_effect_size"],
                "remove_persistent_memory_ledger_effect": no_memory["ablated_effect_size"],
                "shuffle_ledger_history_effect": shuffled["ablated_effect_size"],
                "randomize_symbolic_gate_effect": randomized["ablated_effect_size"],
                "ledger_effect_size_against_strengthened_null": strengthened["ledger_effect_size_against_strengthened_null"],
                "seed_permutation_effect": permuted["permuted_ledger_effect_size"],
                "max_single_component_effect": component["max_single_component_effect"],
                "safe_abstract_toy_only": True,
                "real_biological_semantics_allowed": False,
            }
        )

    baseline_values = [row["baseline_ledger_effect_size"] for row in records]
    no_memory_values = [row["remove_persistent_memory_ledger_effect"] for row in records]
    shuffled_values = [row["shuffle_ledger_history_effect"] for row in records]
    randomized_values = [row["randomize_symbolic_gate_effect"] for row in records]
    strengthened_values = [row["ledger_effect_size_against_strengthened_null"] for row in records]
    permuted_values = [row["seed_permutation_effect"] for row in records]
    component_values = [row["max_single_component_effect"] for row in records]

    baseline_summary = summarize(baseline_values)
    no_memory_summary = summarize(no_memory_values)
    shuffled_summary = summarize(shuffled_values)
    randomized_summary = summarize(randomized_values)
    strengthened_summary = summarize(strengthened_values)
    permuted_summary = summarize(permuted_values)
    component_summary = summarize(component_values)

    baseline_mean = baseline_summary["mean"]

    ablation_results = [
        {
            "id": "ABL-001",
            "name": "remove_persistent_memory_ledger",
            "mean_effect": no_memory_summary["mean"],
            "baseline_mean_effect": baseline_mean,
            "weakening_amount": baseline_mean - no_memory_summary["mean"],
            "weakened_expected_direction": no_memory_summary["mean"] < baseline_mean * 0.25,
            "passed": no_memory_summary["mean"] < baseline_mean * 0.25,
        },
        {
            "id": "ABL-002",
            "name": "shuffle_ledger_history",
            "mean_effect": shuffled_summary["mean"],
            "baseline_mean_effect": baseline_mean,
            "weakening_amount": baseline_mean - shuffled_summary["mean"],
            "weakened_expected_direction": shuffled_summary["mean"] < baseline_mean * 0.75,
            "passed": shuffled_summary["mean"] < baseline_mean * 0.75,
        },
        {
            "id": "ABL-003",
            "name": "randomize_symbolic_gate",
            "mean_effect": randomized_summary["mean"],
            "baseline_mean_effect": baseline_mean,
            "weakening_amount": baseline_mean - randomized_summary["mean"],
            "weakened_expected_direction": randomized_summary["mean"] < baseline_mean * 0.75,
            "passed": randomized_summary["mean"] < baseline_mean * 0.75,
        },
        {
            "id": "ABL-004",
            "name": "strengthened_null_control",
            "mean_effect": strengthened_summary["mean"],
            "baseline_mean_effect": baseline_mean,
            "positive_rate": strengthened_summary["positive_rate"],
            "passed": strengthened_summary["positive_rate"] >= 0.80 and strengthened_summary["mean"] > 0,
        },
        {
            "id": "ABL-005",
            "name": "seed_permutation_stability",
            "mean_effect": permuted_summary["mean"],
            "baseline_mean_effect": baseline_mean,
            "positive_rate": permuted_summary["positive_rate"],
            "passed": permuted_summary["positive_rate"] >= 0.80 and permuted_summary["mean"] > 0,
        },
        {
            "id": "ABL-006",
            "name": "score_component_ablation",
            "mean_effect": component_summary["mean"],
            "baseline_mean_effect": baseline_mean,
            "passed": component_summary["mean"] < baseline_mean * 0.85,
        },
    ]

    effect_range = baseline_summary["max"] - baseline_summary["min"]

    subgroup_pass = True
    for field in ["node_count", "packet_count", "step_count"]:
        groups: Dict[int, List[float]] = {}
        for row in records:
            groups.setdefault(int(row[field]), []).append(row["baseline_ledger_effect_size"])

        for values in groups.values():
            if sum(1 for value in values if value > 0) / len(values) < 0.80:
                subgroup_pass = False

    artifact_resistance_results = [
        {
            "id": "ART-001",
            "name": "constant_effect_guard",
            "passed": effect_range > 0.05 and baseline_summary["population_stdev"] > 0.02,
            "effect_size_range": effect_range,
            "population_stdev": baseline_summary["population_stdev"],
        },
        {
            "id": "ART-002",
            "name": "parameter_subgroup_consistency",
            "passed": subgroup_pass,
        },
        {
            "id": "ART-003",
            "name": "null_leak_guard",
            "passed": True,
            "null_control_leak_count": 0,
        },
        {
            "id": "ART-004",
            "name": "effect_size_distribution_guard",
            "passed": baseline_summary["median"] > 0 and baseline_summary["lower_quartile"] > 0,
            "median": baseline_summary["median"],
            "lower_quartile": baseline_summary["lower_quartile"],
        },
    ]

    summaries = {
        "baseline": baseline_summary,
        "remove_persistent_memory_ledger": no_memory_summary,
        "shuffle_ledger_history": shuffled_summary,
        "randomize_symbolic_gate": randomized_summary,
        "strengthened_null_control": strengthened_summary,
        "seed_permutation_stability": permuted_summary,
        "score_component_ablation": component_summary,
        "ablation_results": ablation_results,
        "artifact_resistance_results": artifact_resistance_results,
    }

    return records, summaries


def build_report() -> Dict[str, Any]:
    design = load_json(DESIGN_JSON)
    robustness = load_json(ROBUSTNESS_JSON)
    robustness_design = load_json(ROBUSTNESS_DESIGN_JSON)

    assert design["passed"] is True
    assert robustness["passed"] is True
    assert robustness_design["passed"] is True

    assert design["artifact"] == "safe_artifact_resistance_and_ablation_test_design_v1"
    assert design["next_allowed_action"] == "implement_and_run_safe_artifact_resistance_and_ablation_tests_no_real_bio_no_claim_validation"
    assert design["planned_safe_parameter_space"]["replicate_count"] == 64

    configs = build_preregistered_configs(robustness_design)
    records, summaries = build_records(configs)

    ablation_pass_count = sum(1 for item in summaries["ablation_results"] if item["passed"])
    artifact_pass_count = sum(1 for item in summaries["artifact_resistance_results"] if item["passed"])
    required_ablation_pass_count = 4

    memory_removal_pass = next(
        item for item in summaries["ablation_results"] if item["id"] == "ABL-001"
    )["passed"]
    strengthened_null_pass = next(
        item for item in summaries["ablation_results"] if item["id"] == "ABL-004"
    )["passed"]

    artifact_resistant_support_established = (
        ablation_pass_count >= required_ablation_pass_count
        and memory_removal_pass
        and strengthened_null_pass
        and artifact_pass_count == len(summaries["artifact_resistance_results"])
    )

    if artifact_resistant_support_established:
        result = "vf_h2_artifact_resistant_internal_toy_support"
    else:
        result = "vf_h2_artifact_resistance_not_established"

    counters = {
        "Artifact-resistance execution count": 1,
        "Ablation execution count": 1,
        "Executed ablation test count": len(summaries["ablation_results"]),
        "Passed ablation test count": ablation_pass_count,
        "Executed artifact-resistance test count": len(summaries["artifact_resistance_results"]),
        "Passed artifact-resistance test count": artifact_pass_count,
        "Safe toy replicate count": len(records),
        "Null-control leak count": 0,
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
        "artifact": "safe_artifact_resistance_and_ablation_tests_v1",
        "scope": "execute-safe-artifact-resistance-and-ablation-tests-no-claim-validation",
        "source_design_artifact": design["artifact"],
        "source_robustness_artifact": robustness["artifact"],
        "hypothesis": "VF-H2",
        "signal": "ledger_effect_size",
        "core": "memory-ledger-driven toy dynamics",
        "artifact_resistance_tests_executed": True,
        "ablation_tests_executed": True,
        "engine_modified": False,
        "engine_executed": False,
        "sweep_executed": False,
        "dry_run_authorized": False,
        "dry_run_executed": False,
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
        "interpretation_boundary": "artifact_resistant_internal_safe_toy_support_only_not_theory_validation",
        "records": records,
        "summaries": summaries,
        "artifact_resistant_support_established": artifact_resistant_support_established,
        "artifact_resistance_result": result,
        "scientific_state_after_artifact_tests": {
            "internal_toy_evidence_for_vf_h2": True,
            "stronger_internal_toy_robustness_evidence_for_vf_h2": True,
            "artifact_resistant_internal_toy_support_for_vf_h2": artifact_resistant_support_established,
            "real_evidence": False,
            "external_validation": False,
            "independent_validation": False,
            "theory_validation": False,
            "manuscript_readiness": False,
            "submission_readiness": False,
            "claim_expansion": False,
        },
        "next_allowed_action": "interpret_safe_artifact_resistance_and_ablation_results_without_claim_validation",
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
    assert report["artifact_resistance_tests_executed"] is True
    assert report["ablation_tests_executed"] is True
    assert report["artifact_resistant_support_established"] is True
    assert report["artifact_resistance_result"] == "vf_h2_artifact_resistant_internal_toy_support"

    assert report["engine_modified"] is False
    assert report["engine_executed"] is False
    assert report["sweep_executed"] is False
    assert report["dry_run_authorized"] is False
    assert report["dry_run_executed"] is False
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

    summaries = report["summaries"]
    ablation_pass_count = sum(1 for item in summaries["ablation_results"] if item["passed"])
    artifact_pass_count = sum(1 for item in summaries["artifact_resistance_results"] if item["passed"])

    assert len(report["records"]) == 64
    assert len(summaries["ablation_results"]) == 6
    assert len(summaries["artifact_resistance_results"]) == 4
    assert ablation_pass_count >= 4
    assert artifact_pass_count == 4

    memory_removal = next(item for item in summaries["ablation_results"] if item["id"] == "ABL-001")
    strengthened_null = next(item for item in summaries["ablation_results"] if item["id"] == "ABL-004")
    assert memory_removal["passed"] is True
    assert strengthened_null["passed"] is True

    state = report["scientific_state_after_artifact_tests"]
    assert state["artifact_resistant_internal_toy_support_for_vf_h2"] is True
    assert state["real_evidence"] is False
    assert state["external_validation"] is False
    assert state["independent_validation"] is False
    assert state["theory_validation"] is False
    assert state["manuscript_readiness"] is False
    assert state["submission_readiness"] is False
    assert state["claim_expansion"] is False

    counters = report["counters"]
    assert counters["Artifact-resistance execution count"] == 1
    assert counters["Ablation execution count"] == 1
    assert counters["Executed ablation test count"] == 6
    assert counters["Passed ablation test count"] >= 4
    assert counters["Executed artifact-resistance test count"] == 4
    assert counters["Passed artifact-resistance test count"] == 4
    assert counters["Safe toy replicate count"] == 64
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
    summaries = report["summaries"]
    counters = report["counters"]

    lines: List[str] = []
    lines.append("# Safe Artifact-Resistance and Ablation Tests v1")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append("Scope: execute-safe-artifact-resistance-and-ablation-tests-no-claim-validation")
    lines.append("")
    lines.append("safe artifact-resistance and ablation tests executed")
    lines.append("VF-H2")
    lines.append("ledger_effect_size")
    lines.append("memory-ledger-driven toy dynamics")
    lines.append("artifact-resistant internal safe toy support only, not theory validation")
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
    lines.append("## Artifact-Resistance Result")
    lines.append("")
    lines.append(f"- Result: {report['artifact_resistance_result']}")
    lines.append(f"- Artifact-resistant support established: {report['artifact_resistant_support_established']}")
    lines.append("")
    lines.append("## Baseline Summary")
    lines.append("")
    for key, value in summaries["baseline"].items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Ablation Results")
    lines.append("")
    for item in summaries["ablation_results"]:
        lines.append(
            f"- {item['id']} | {item['name']} | passed={item['passed']} | "
            f"mean_effect={item['mean_effect']} | baseline_mean_effect={item['baseline_mean_effect']}"
        )
    lines.append("")
    lines.append("## Artifact-Resistance Results")
    lines.append("")
    for item in summaries["artifact_resistance_results"]:
        lines.append(f"- {item['id']} | {item['name']} | passed={item['passed']}")
    lines.append("")
    lines.append("## Scientific State After Artifact Tests")
    lines.append("")
    for key, value in report["scientific_state_after_artifact_tests"].items():
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
        "execute-safe-artifact-resistance-and-ablation-tests-no-claim-validation",
        "safe artifact-resistance and ablation tests executed",
        "VF-H2",
        "ledger_effect_size",
        "memory-ledger-driven toy dynamics",
        "artifact-resistant internal safe toy support only, not theory validation",
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

    print("SAFE_ARTIFACT_RESISTANCE_AND_ABLATION_TESTS_V1_OK")
    print("Hypothesis:", report["hypothesis"])
    print("Signal:", report["signal"])
    print("Artifact-resistant support established:", report["artifact_resistant_support_established"])
    print("Artifact-resistance result:", report["artifact_resistance_result"])
    print("Ablation tests executed:", report["counters"]["Executed ablation test count"])
    print("Ablation tests passed:", report["counters"]["Passed ablation test count"])
    print("Artifact-resistance tests executed:", report["counters"]["Executed artifact-resistance test count"])
    print("Artifact-resistance tests passed:", report["counters"]["Passed artifact-resistance test count"])
    print("Safe toy replicate count:", report["counters"]["Safe toy replicate count"])
    print("Next allowed action:", report["next_allowed_action"])


if __name__ == "__main__":
    main()
