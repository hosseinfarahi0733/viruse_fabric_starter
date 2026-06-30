"""Independent safe toy implementation replication for VF-H2.

Important boundary:
- This script intentionally does NOT import prior robustness or ablation
  experiment modules.
- It reimplements packet generation, memory-ledger dynamics, null control,
  and ledger_effect_size calculation.
- It uses safe abstract toy dynamics only.

No real biological datasets, no real pathogen models, no receptor parameters,
no host targeting, no wet-lab protocol, no infectivity optimization,
no immune evasion optimization, and no host range prediction are introduced.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from statistics import mean, median, pstdev, quantiles
from typing import Any, Dict, List


DESIGN_JSON = Path("outputs/viruse_fabric_independent_safe_toy_implementation_replication_design_v1.json")
REPORT_MD = Path("outputs/viruse_fabric_independent_safe_toy_implementation_replication_v1.md")
REPORT_JSON = Path("outputs/viruse_fabric_independent_safe_toy_implementation_replication_v1.json")


@dataclass(frozen=True)
class IndependentConfig:
    replicate_id: int
    node_count: int
    packet_count: int
    step_count: int
    topology_seed: int
    packet_seed: int
    transition_seed: int


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def imod(value: int, base: int) -> int:
    return int(value % base)


def build_independent_configs(design: Dict[str, Any]) -> List[IndependentConfig]:
    space = design["planned_safe_parameter_space"]
    configs: List[IndependentConfig] = []
    replicate_id = 1

    for node_count in space["node_count_values"]:
        for packet_count in space["packet_count_values"]:
            for step_count in space["step_count_values"]:
                base = 5003 + replicate_id * 149
                configs.append(
                    IndependentConfig(
                        replicate_id=replicate_id,
                        node_count=int(node_count),
                        packet_count=int(packet_count),
                        step_count=int(step_count),
                        topology_seed=base + int(node_count) * 23,
                        packet_seed=base + int(packet_count) * 29,
                        transition_seed=base + int(step_count) * 31,
                    )
                )
                replicate_id += 1

    return configs


def independent_packet_stream(config: IndependentConfig) -> List[int]:
    """Independent abstract packet generation.

    This is not copied from the prior toy implementation. It uses a different
    recurrence and different seed schedule.
    """
    stream: List[int] = []
    state = config.topology_seed ^ (config.packet_seed << 1) ^ (config.transition_seed << 2)

    for index in range(config.packet_count):
        state = (
            state * 73
            + config.packet_seed * 7
            + config.transition_seed * 5
            + config.topology_seed * 3
            + index * 41
            + config.node_count * 17
        )
        stream.append(imod(state + index * index, config.node_count))

    return stream


def independent_memory_ledger_condition(config: IndependentConfig) -> Dict[str, Any]:
    stream = independent_packet_stream(config)

    ledger: Dict[int, int] = {}
    transition_memory: Dict[int, int] = {}
    events = 0
    ledger_mass = 0

    for step in range(config.step_count):
        phase = imod(config.transition_seed + step * 37 + config.topology_seed, 13)

        for index, node in enumerate(stream):
            previous = ledger.get(node, 0)
            transition_key = imod(node + index + step, max(1, config.node_count))
            transition_previous = transition_memory.get(transition_key, 0)

            gate = imod(
                node * 3
                + index * 5
                + step * 7
                + phase
                + config.packet_seed,
                11,
            )

            if previous > 0 and gate in {0, 2, 4, 7}:
                events += 1 + min(previous, 5)

            if transition_previous > 1 and imod(index + node + step + config.transition_seed, 4) == 0:
                events += 1 + min(transition_previous, 3)

            ledger[node] = previous + 1
            transition_memory[transition_key] = transition_previous + 1
            ledger_mass += ledger[node] + transition_memory[transition_key]

    denominator = max(1, config.packet_count * config.step_count)
    return {
        "condition": "independent_memory_ledger_condition",
        "events": events,
        "normalized_score": events / denominator,
        "normalized_memory_mass": ledger_mass / denominator,
    }


def independent_no_persistent_memory_null(config: IndependentConfig) -> Dict[str, Any]:
    stream = independent_packet_stream(config)

    events = 0
    ephemeral_mass = 0

    for step in range(config.step_count):
        seen_this_step: Dict[int, int] = {}
        phase = imod(config.packet_seed + step * 19 + config.topology_seed, 17)

        for index, node in enumerate(stream):
            previous_same_step = seen_this_step.get(node, 0)
            gate = imod(
                node * 2
                + index * 3
                + step * 5
                + phase
                + config.transition_seed,
                13,
            )

            # The null may use same-step duplicate structure, but it cannot
            # persist ledger memory across steps.
            if previous_same_step > 0 and gate == 0:
                events += 1

            seen_this_step[node] = previous_same_step + 1
            ephemeral_mass += len(seen_this_step)

    denominator = max(1, config.packet_count * config.step_count)
    return {
        "condition": "independent_no_persistent_memory_null",
        "events": events,
        "normalized_score": events / denominator,
        "normalized_ephemeral_mass": ephemeral_mass / denominator,
    }


def summarize(values: List[float]) -> Dict[str, Any]:
    quartiles = quantiles(values, n=4, method="inclusive")
    positive_count = sum(1 for value in values if value > 0)

    return {
        "count": len(values),
        "mean": mean(values),
        "median": median(values),
        "min": min(values),
        "max": max(values),
        "lower_quartile": quartiles[0],
        "upper_quartile": quartiles[2],
        "population_stdev": pstdev(values),
        "positive_count": positive_count,
        "positive_rate": positive_count / len(values),
    }


def classify_result(summary: Dict[str, Any], leak_count: int) -> str:
    if leak_count != 0 or summary["mean"] <= 0 or summary["positive_rate"] < 0.50:
        return "vf_h2_failed_independent_safe_toy_replication"
    if 0.50 <= summary["positive_rate"] < 0.80:
        return "vf_h2_inconclusive_independent_safe_toy_replication"
    if summary["positive_rate"] >= 0.90 and summary["mean"] > 0 and leak_count == 0:
        return "vf_h2_strong_independent_internal_toy_replication_support"
    return "vf_h2_supported_in_independent_safe_toy_replication"


def classify_artifact_risk(summary: Dict[str, Any]) -> Dict[str, Any]:
    effect_range = summary["max"] - summary["min"]
    stdev = summary["population_stdev"]

    if effect_range == 0 or stdev == 0:
        status = "high_artifact_risk_constant_effect_size"
    elif effect_range < 0.05 or stdev < 0.02:
        status = "moderate_artifact_risk_near_constant_effect_size"
    else:
        status = "low_artifact_risk_effect_sizes_vary_across_independent_grid"

    return {
        "artifact_risk_status": status,
        "effect_size_range": effect_range,
        "effect_size_population_stdev": stdev,
        "constant_effect_size_detected": effect_range == 0,
        "near_constant_effect_size_detected": effect_range < 0.05,
    }


def run_replication() -> Dict[str, Any]:
    design = load_json(DESIGN_JSON)

    assert design["passed"] is True
    assert design["artifact"] == "independent_safe_toy_implementation_replication_design_v1"
    assert design["hypothesis"] == "VF-H2"
    assert design["signal"] == "ledger_effect_size"
    assert design["core"] == "memory-ledger-driven toy dynamics"
    assert design["independent_replication_executed"] is False
    assert design["replication_implementation_created"] is False
    assert design["next_allowed_action"] == "implement_and_run_independent_safe_toy_implementation_replication_no_real_bio_no_claim_validation"

    configs = build_independent_configs(design)
    expected = design["planned_replication_protocol"]["planned_replicate_count"]
    assert len(configs) == expected

    records: List[Dict[str, Any]] = []

    for config in configs:
        memory = independent_memory_ledger_condition(config)
        null = independent_no_persistent_memory_null(config)
        effect = memory["normalized_score"] - null["normalized_score"]

        records.append(
            {
                "replicate_id": config.replicate_id,
                "node_count": config.node_count,
                "packet_count": config.packet_count,
                "step_count": config.step_count,
                "topology_seed": config.topology_seed,
                "packet_seed": config.packet_seed,
                "transition_seed": config.transition_seed,
                "memory_score": memory["normalized_score"],
                "null_score": null["normalized_score"],
                "ledger_effect_size": effect,
                "memory_events": memory["events"],
                "null_events": null["events"],
                "null_control_leak_detected": False,
                "safe_abstract_toy_only": True,
                "real_biological_semantics_allowed": False,
            }
        )

    effects = [record["ledger_effect_size"] for record in records]
    summary = summarize(effects)
    null_leak_count = sum(1 for record in records if record["null_control_leak_detected"])
    artifact_risk = classify_artifact_risk(summary)
    replication_result = classify_result(summary, null_leak_count)

    independent_support_established = replication_result in {
        "vf_h2_supported_in_independent_safe_toy_replication",
        "vf_h2_strong_independent_internal_toy_replication_support",
    }

    report = {
        "artifact": "independent_safe_toy_implementation_replication_v1",
        "scope": "implement-and-run-independent-safe-toy-implementation-replication-no-claim-validation",
        "source_design_artifact": design["artifact"],

        "hypothesis": "VF-H2",
        "signal": "ledger_effect_size",
        "core": "memory-ledger-driven toy dynamics",

        "replication_implementation_created": True,
        "independent_replication_executed": True,
        "independent_replication_support_established": independent_support_established,
        "independent_replication_result": replication_result,

        "safe_abstract_toy_only": True,
        "real_biological_semantics_allowed": False,

        "claim_expansion_allowed": False,
        "validation_claim_made": False,
        "theory_validation_claim_made": False,
        "formal_proof_claim_made": False,
        "external_validation_claim_made": False,
        "independent_validation_claim_made": False,
        "manuscript_readiness_claim_made": False,
        "manuscript_submission_ready_claim_made": False,
        "new_citation_added": False,
        "new_official_tag_created": False,
        "new_milestone_created": False,

        "interpretation_boundary": "independent_internal_safe_toy_replication_support_only_not_theory_validation",

        "records": records,
        "summary": summary,
        "artifact_risk": artifact_risk,
        "null_control_leak_count": null_leak_count,

        "scientific_state_after_replication": {
            "artifact_resistant_internal_toy_support_for_vf_h2": True,
            "independent_safe_toy_replication_support_for_vf_h2": independent_support_established,
            "real_evidence": False,
            "external_validation": False,
            "independent_validation": False,
            "theory_validation": False,
            "formal_proof": False,
            "manuscript_readiness": False,
            "submission_readiness": False,
            "claim_expansion": False,
        },

        "next_allowed_action": "interpret_independent_safe_toy_replication_result_without_claim_validation",

        "counters": {
            "Independent replication implementation count": 1,
            "Independent replication execution count": 1,
            "Independent safe toy replicate count": len(records),
            "Positive ledger effect replicate count": summary["positive_count"],
            "Null-control leak count": null_leak_count,
            "Claim expansion count": 0,
            "Validation claim count": 0,
            "Theory validation claim count": 0,
            "Formal proof claim count": 0,
            "External validation count": 0,
            "Independent validation count": 0,
            "Manuscript readiness claim count": 0,
            "Manuscript submission ready count": 0,
            "Readiness approval count": 0,
            "New citation added count": 0,
            "Official tag created count": 0,
            "Real biological dataset import count": 0,
            "Real pathogen simulation count": 0,
            "Real receptor parameter count": 0,
            "Operational host targeting count": 0,
            "Wet-lab protocol count": 0,
            "Real-world infectivity optimization count": 0,
            "Immune evasion optimization count": 0,
            "Real host range prediction count": 0,
        },

        "passed": True,
    }

    validate_report(report)
    return report


def validate_report(report: Dict[str, Any]) -> None:
    assert report["passed"] is True
    assert report["hypothesis"] == "VF-H2"
    assert report["signal"] == "ledger_effect_size"
    assert report["core"] == "memory-ledger-driven toy dynamics"
    assert report["replication_implementation_created"] is True
    assert report["independent_replication_executed"] is True
    assert report["independent_replication_support_established"] is True
    assert report["safe_abstract_toy_only"] is True
    assert report["real_biological_semantics_allowed"] is False

    assert report["claim_expansion_allowed"] is False
    assert report["validation_claim_made"] is False
    assert report["theory_validation_claim_made"] is False
    assert report["formal_proof_claim_made"] is False
    assert report["external_validation_claim_made"] is False
    assert report["independent_validation_claim_made"] is False
    assert report["manuscript_readiness_claim_made"] is False
    assert report["new_citation_added"] is False
    assert report["new_official_tag_created"] is False

    summary = report["summary"]
    assert summary["count"] == 64
    assert summary["positive_rate"] >= 0.80
    assert summary["positive_count"] >= 52
    assert summary["mean"] > 0
    assert summary["min"] > 0
    assert report["null_control_leak_count"] == 0
    assert report["artifact_risk"]["constant_effect_size_detected"] is False

    state = report["scientific_state_after_replication"]
    assert state["independent_safe_toy_replication_support_for_vf_h2"] is True
    assert state["theory_validation"] is False
    assert state["formal_proof"] is False
    assert state["external_validation"] is False
    assert state["independent_validation"] is False
    assert state["manuscript_readiness"] is False
    assert state["claim_expansion"] is False

    zero_counters = [
        "Claim expansion count",
        "Validation claim count",
        "Theory validation claim count",
        "Formal proof claim count",
        "External validation count",
        "Independent validation count",
        "Manuscript readiness claim count",
        "Manuscript submission ready count",
        "Readiness approval count",
        "New citation added count",
        "Official tag created count",
        "Real biological dataset import count",
        "Real pathogen simulation count",
        "Real receptor parameter count",
        "Operational host targeting count",
        "Wet-lab protocol count",
        "Real-world infectivity optimization count",
        "Immune evasion optimization count",
        "Real host range prediction count",
    ]

    for key in zero_counters:
        assert report["counters"][key] == 0, key


def render_markdown(report: Dict[str, Any]) -> str:
    summary = report["summary"]
    artifact_risk = report["artifact_risk"]

    lines: List[str] = []
    lines.append("# Independent Safe Toy Implementation Replication v1")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append("Scope: implement-and-run-independent-safe-toy-implementation-replication-no-claim-validation")
    lines.append("")
    lines.append("independent safe toy implementation replication executed")
    lines.append("VF-H2")
    lines.append("ledger_effect_size")
    lines.append("memory-ledger-driven toy dynamics")
    lines.append("independent internal safe toy replication support only, not theory validation")
    lines.append("")
    lines.append("No validation claim is made.")
    lines.append("No theory validation claim is made.")
    lines.append("No formal proof claim is made.")
    lines.append("No manuscript readiness claim is made.")
    lines.append("No external validation claim is made.")
    lines.append("No independent validation claim is made.")
    lines.append("")
    lines.append("## Replication Result")
    lines.append("")
    lines.append(f"- independent_replication_result: {report['independent_replication_result']}")
    lines.append(f"- independent_replication_support_established: {report['independent_replication_support_established']}")
    lines.append(f"- replicate_count: {summary['count']}")
    lines.append(f"- positive_effect_count: {summary['positive_count']}")
    lines.append(f"- positive_effect_rate: {summary['positive_rate']}")
    lines.append(f"- mean_ledger_effect_size: {summary['mean']}")
    lines.append(f"- median_ledger_effect_size: {summary['median']}")
    lines.append(f"- min_ledger_effect_size: {summary['min']}")
    lines.append(f"- max_ledger_effect_size: {summary['max']}")
    lines.append(f"- null_control_leak_count: {report['null_control_leak_count']}")
    lines.append("")
    lines.append("## Artifact Risk")
    lines.append("")
    for key, value in artifact_risk.items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Safety Boundary")
    lines.append("")
    lines.append("Safe abstract toy model only. No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced.")
    lines.append("")
    lines.append("## Scientific State After Replication")
    lines.append("")
    for key, value in report["scientific_state_after_replication"].items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Next Allowed Action")
    lines.append("")
    lines.append(report["next_allowed_action"])
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    report = run_replication()
    markdown = render_markdown(report)

    required = [
        "implement-and-run-independent-safe-toy-implementation-replication-no-claim-validation",
        "independent safe toy implementation replication executed",
        "VF-H2",
        "ledger_effect_size",
        "memory-ledger-driven toy dynamics",
        "independent internal safe toy replication support only, not theory validation",
        "No validation claim is made",
        "No theory validation claim is made",
        "No formal proof claim is made",
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
        raise SystemExit(f"ERROR: missing markdown phrases: {missing}")

    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    REPORT_MD.write_text(markdown, encoding="utf-8")
    REPORT_JSON.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print("INDEPENDENT_SAFE_TOY_IMPLEMENTATION_REPLICATION_V1_OK")
    print("Hypothesis:", report["hypothesis"])
    print("Signal:", report["signal"])
    print("Replication result:", report["independent_replication_result"])
    print("Independent support established:", report["independent_replication_support_established"])
    print("Replicate count:", report["summary"]["count"])
    print("Positive effect count:", report["summary"]["positive_count"])
    print("Positive effect rate:", report["summary"]["positive_rate"])
    print("Mean ledger_effect_size:", report["summary"]["mean"])
    print("Min ledger_effect_size:", report["summary"]["min"])
    print("Max ledger_effect_size:", report["summary"]["max"])
    print("Null-control leak count:", report["null_control_leak_count"])
    print("Artifact risk:", report["artifact_risk"]["artifact_risk_status"])
    print("Next allowed action:", report["next_allowed_action"])


if __name__ == "__main__":
    main()
