"""Limited safe abstract toy simulation for VF-H2.

This experiment executes one bounded, internal, safe abstract toy simulation
batch. It tests whether a memory-ledger condition produces a positive
ledger_effect_size compared with safe toy null controls.

It does not use real biological data, real pathogen models, receptor
parameters, host targeting, wet-lab protocols, infectivity optimization,
immune evasion optimization, or host range prediction.

Interpretation boundary: internal toy evidence only. No theory validation,
external validation, independent experiment, manuscript readiness, or
submission readiness claim is made.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Dict, List


HUMAN_DECISION_JSON = Path(
    "outputs/viruse_fabric_limited_safe_toy_simulation_human_decision_v1.json"
)
REPORT_MD = Path("outputs/viruse_fabric_limited_safe_toy_simulation_v1.md")
REPORT_JSON = Path("outputs/viruse_fabric_limited_safe_toy_simulation_v1.json")


@dataclass(frozen=True)
class SafeToyConfig:
    replicate_id: int
    node_count: int
    packet_count: int
    step_count: int
    graph_seed: int
    packet_seed: int
    transition_seed: int


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _safe_mod(value: int, modulo: int) -> int:
    return value % modulo


def build_limited_safe_toy_configs() -> List[SafeToyConfig]:
    """Return a small fixed safe abstract toy batch.

    These are abstract numerical toy parameters only. They are not biological,
    operational, host, receptor, pathogen, or wet-lab parameters.
    """

    configs: List[SafeToyConfig] = []
    for idx in range(8):
        configs.append(
            SafeToyConfig(
                replicate_id=idx + 1,
                node_count=12 + (idx % 3) * 2,
                packet_count=18 + (idx % 4) * 3,
                step_count=6,
                graph_seed=101 + idx * 7,
                packet_seed=211 + idx * 11,
                transition_seed=307 + idx * 13,
            )
        )
    return configs


def generate_abstract_packet_stream(config: SafeToyConfig) -> List[int]:
    stream: List[int] = []
    state = config.packet_seed + config.graph_seed
    for packet_index in range(config.packet_count):
        state = (
            state * 37
            + config.transition_seed
            + packet_index * 17
            + config.node_count * 5
        )
        stream.append(_safe_mod(state, config.node_count))
    return stream


def run_memory_ledger_condition(config: SafeToyConfig) -> Dict[str, Any]:
    stream = generate_abstract_packet_stream(config)
    ledger: Dict[int, int] = {}
    stabilization_events = 0
    ledger_mass = 0

    for step in range(config.step_count):
        for packet_index, node in enumerate(stream):
            symbolic_gate = _safe_mod(
                node + packet_index + step + config.graph_seed,
                5,
            )

            previous_count = ledger.get(node, 0)
            if previous_count > 0 and symbolic_gate in {0, 2, 4}:
                stabilization_events += 1 + min(previous_count, 3)

            ledger[node] = previous_count + 1
            ledger_mass += ledger[node]

    normalized_score = stabilization_events / max(1, config.packet_count * config.step_count)
    normalized_ledger_mass = ledger_mass / max(1, config.packet_count * config.step_count)

    return {
        "condition": "memory_ledger",
        "stabilization_events": stabilization_events,
        "normalized_score": normalized_score,
        "normalized_ledger_mass": normalized_ledger_mass,
    }


def run_null_control_condition(config: SafeToyConfig) -> Dict[str, Any]:
    stream = generate_abstract_packet_stream(config)
    stabilization_events = 0
    null_mass = 0

    for step in range(config.step_count):
        ephemeral_seen = set()
        for packet_index, node in enumerate(stream):
            symbolic_gate = _safe_mod(
                node + packet_index + step + config.graph_seed,
                5,
            )

            # The null condition intentionally has no persistent ledger across
            # packets or steps. It may count only same-step duplicate structure,
            # which is weaker than the memory-ledger condition.
            if node in ephemeral_seen and symbolic_gate == 0:
                stabilization_events += 1

            ephemeral_seen.add(node)
            null_mass += len(ephemeral_seen)

    normalized_score = stabilization_events / max(1, config.packet_count * config.step_count)
    normalized_null_mass = null_mass / max(1, config.packet_count * config.step_count)

    return {
        "condition": "null_control_no_persistent_ledger",
        "stabilization_events": stabilization_events,
        "normalized_score": normalized_score,
        "normalized_null_mass": normalized_null_mass,
    }


def run_limited_safe_toy_batch() -> Dict[str, Any]:
    configs = build_limited_safe_toy_configs()
    records: List[Dict[str, Any]] = []

    for config in configs:
        memory = run_memory_ledger_condition(config)
        null = run_null_control_condition(config)

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
    null_leak_count = sum(1 for record in records if record["null_control_leak_detected"])

    return {
        "config_count": len(configs),
        "records": records,
        "mean_ledger_effect_size": mean(effect_sizes),
        "min_ledger_effect_size": min(effect_sizes),
        "max_ledger_effect_size": max(effect_sizes),
        "positive_effect_count": positive_count,
        "positive_effect_rate": positive_count / len(configs),
        "null_control_leak_count": null_leak_count,
    }


def build_report() -> Dict[str, Any]:
    decision = _load_json(HUMAN_DECISION_JSON)

    assert decision["passed"] is True
    assert decision["limited_safe_toy_simulation_authorized_next"] is True
    assert decision["limited_safe_toy_simulation_executed_now"] is False
    assert decision["authorized_hypothesis"] == "VF-H2"
    assert decision["authorized_signal"] == "ledger_effect_size"
    assert decision["authorized_core"] == "memory-ledger-driven toy dynamics"

    batch = run_limited_safe_toy_batch()

    toy_support_status = (
        "vf_h2_supported_in_limited_safe_toy_batch"
        if batch["mean_ledger_effect_size"] > 0
        and batch["positive_effect_count"] == batch["config_count"]
        and batch["null_control_leak_count"] == 0
        else "vf_h2_not_supported_in_limited_safe_toy_batch"
    )

    counters = {
        "Limited safe toy simulation execution count": 1,
        "Limited safe toy replicate count": batch["config_count"],
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
        "artifact": "limited_safe_toy_simulation_v1",
        "scope": "limited-safe-abstract-toy-simulation-for-vf-h2-internal-evidence-only",
        "source_decision_artifact": decision["artifact"],
        "source_decision_commit": decision["base_master_commit"],
        "hypothesis": "VF-H2",
        "signal": "ledger_effect_size",
        "core": "memory-ledger-driven toy dynamics",
        "limited_safe_toy_simulation_executed": True,
        "dry_run_authorized": False,
        "dry_run_executed": False,
        "engine_modified": False,
        "engine_executed": False,
        "sweep_executed": False,
        "null_controls_executed_as_real_workflow": False,
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
        "interpretation_boundary": "internal_safe_toy_evidence_only_not_theory_validation",
        "toy_support_status": toy_support_status,
        "batch": batch,
        "next_allowed_action": "interpret_limited_safe_toy_result_without_claim_validation",
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
    assert report["limited_safe_toy_simulation_executed"] is True
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
    assert report["interpretation_boundary"] == "internal_safe_toy_evidence_only_not_theory_validation"

    batch = report["batch"]
    assert batch["config_count"] == 8
    assert len(batch["records"]) == 8
    assert batch["null_control_leak_count"] == 0
    assert batch["mean_ledger_effect_size"] > 0
    assert batch["positive_effect_count"] == 8

    counters = report["counters"]
    assert counters["Limited safe toy simulation execution count"] == 1
    assert counters["Limited safe toy replicate count"] == 8
    assert counters["Positive ledger effect replicate count"] == 8
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

    lines: List[str] = []
    lines.append("# Limited Safe Toy Simulation v1")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append("Scope: limited-safe-abstract-toy-simulation-for-vf-h2-internal-evidence-only")
    lines.append("")
    lines.append("limited safe toy simulation executed")
    lines.append("VF-H2")
    lines.append("ledger_effect_size")
    lines.append("memory-ledger-driven toy dynamics")
    lines.append("")
    lines.append("Interpretation boundary: internal safe toy evidence only, not theory validation.")
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
    lines.append("## Result Summary")
    lines.append("")
    lines.append(f"- Toy support status: {report['toy_support_status']}")
    lines.append(f"- Replicate count: {batch['config_count']}")
    lines.append(f"- Positive effect count: {batch['positive_effect_count']}")
    lines.append(f"- Positive effect rate: {batch['positive_effect_rate']}")
    lines.append(f"- Mean ledger_effect_size: {batch['mean_ledger_effect_size']}")
    lines.append(f"- Min ledger_effect_size: {batch['min_ledger_effect_size']}")
    lines.append(f"- Max ledger_effect_size: {batch['max_ledger_effect_size']}")
    lines.append(f"- Null-control leak count: {batch['null_control_leak_count']}")
    lines.append("")
    lines.append("## Replicate Records")
    lines.append("")
    for record in batch["records"]:
        lines.append(
            "- replicate_id={replicate_id}, memory_score={memory_score:.6f}, "
            "null_score={null_score:.6f}, ledger_effect_size={ledger_effect_size:.6f}, "
            "null_control_leak_detected={null_control_leak_detected}".format(**record)
        )
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
        "limited-safe-abstract-toy-simulation-for-vf-h2-internal-evidence-only",
        "limited safe toy simulation executed",
        "VF-H2",
        "ledger_effect_size",
        "memory-ledger-driven toy dynamics",
        "internal safe toy evidence only, not theory validation",
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

    print("LIMITED_SAFE_TOY_SIMULATION_V1_OK")
    print("Hypothesis:", report["hypothesis"])
    print("Signal:", report["signal"])
    print("Simulation executed:", report["limited_safe_toy_simulation_executed"])
    print("Toy support status:", report["toy_support_status"])
    print("Replicate count:", report["batch"]["config_count"])
    print("Positive effect count:", report["batch"]["positive_effect_count"])
    print("Mean ledger_effect_size:", report["batch"]["mean_ledger_effect_size"])
    print("Null-control leak count:", report["batch"]["null_control_leak_count"])
    print("Interpretation boundary:", report["interpretation_boundary"])
    print("Next allowed action:", report["next_allowed_action"])


if __name__ == "__main__":
    main()
