from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Mapping, Sequence, Tuple


FORBIDDEN_INPUT_FIELDS = frozenset(
    {
        "real_biological_dataset",
        "pathogen_name",
        "host_species",
        "organism",
        "tissue",
        "cell_type",
        "receptor",
        "receptor_name",
        "binding_affinity",
        "genetic_sequence",
        "protein_sequence",
        "infectivity",
        "infectivity_score",
        "immune_evasion",
        "immune_evasion_score",
        "virulence",
        "host_range",
        "host_range_prediction",
        "wet_lab_protocol",
        "clinical_outcome",
        "epidemiological_region",
    }
)


@dataclass(frozen=True)
class ToyEngineConfig:
    """Configuration for the safe abstract toy engine.

    This is abstract, symbolic, unitless, and non-operational.
    It is not a biological, clinical, epidemiological, wet-lab, host, receptor, pathogen,
    infectivity, immune-evasion, or host-range model.
    """

    graph_spec_id: str
    seed_spec_id: str
    initialization_spec_id: str
    node_count: int
    packet_count: int
    step_count_limit: int
    graph_seed: int
    packet_seed: int
    transition_seed: int
    symbolic_drift_seed: int


@dataclass(frozen=True)
class ToyNode:
    node_id: int
    node_state_vector: Tuple[float, ...]
    node_constraint_profile: Tuple[float, ...]


@dataclass(frozen=True)
class ToyEdge:
    edge_id: int
    source_node_id: int
    target_node_id: int
    edge_weight: float
    transition_channel_label: str


@dataclass(frozen=True)
class ToyPacket:
    packet_id: int
    packet_state_vector: Tuple[float, ...]
    current_node_id: int
    compatibility_score: float
    local_constraint_score: float
    global_constraint_score: float
    causal_mass_score: float
    memory_trace: Tuple[str, ...]
    symbolic_drift: float
    survival_indicator: bool
    time_layer: str


@dataclass(frozen=True)
class ToyGraph:
    graph_spec_id: str
    nodes: Tuple[ToyNode, ...]
    edges: Tuple[ToyEdge, ...]


@dataclass(frozen=True)
class ToyEngineManifest:
    engine_name: str
    engine_version: str
    implementation_scope: str
    safety_boundary: str
    implemented_components: Tuple[str, ...]
    explicitly_not_performed: Tuple[str, ...]
    forbidden_input_fields: Tuple[str, ...]


class SafeAbstractToySimulationEngine:
    """Minimal safe abstract toy engine.

    v9.2 implements the engine contract and deterministic toy methods only.
    v9.2 does not execute a simulation run, does not compare baselines, does not report
    results, does not execute a falsification audit, and does not validate the theory.

    Any future execution must remain safe abstract toy-only.
    """

    engine_name = "SafeAbstractToySimulationEngine"
    engine_version = "v9.2"
    implementation_scope = "minimal-safe-toy-engine-implementation-only"

    implemented_components = (
        "safety_field_guard",
        "toy_config_validation",
        "toy_graph_builder_method",
        "toy_packet_initializer_method",
        "toy_score_update_methods",
        "toy_transition_step_method",
        "toy_metric_snapshot_method",
        "toy_output_schema_guard",
    )

    explicitly_not_performed = (
        "no_simulation_run_performed_in_v9_2",
        "no_baseline_comparison_executed_in_v9_2",
        "no_results_reported_in_v9_2",
        "no_falsification_audit_executed_in_v9_2",
        "no_validation_claim_made_in_v9_2",
        "no_manuscript_file_modified_in_v9_2",
        "no_citation_added_in_v9_2",
    )

    forbidden_input_fields = FORBIDDEN_INPUT_FIELDS

    def manifest(self) -> ToyEngineManifest:
        return ToyEngineManifest(
            engine_name=self.engine_name,
            engine_version=self.engine_version,
            implementation_scope=self.implementation_scope,
            safety_boundary=(
                "safe abstract toy model only; no real biological datasets, no real pathogen models, "
                "no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity "
                "optimization, no immune evasion optimization, and no host range prediction"
            ),
            implemented_components=self.implemented_components,
            explicitly_not_performed=self.explicitly_not_performed,
            forbidden_input_fields=tuple(sorted(self.forbidden_input_fields)),
        )

    def validate_no_forbidden_fields(self, payload: Mapping[str, object]) -> None:
        forbidden = sorted(set(payload.keys()) & set(self.forbidden_input_fields))
        if forbidden:
            raise ValueError(f"Forbidden non-toy fields detected: {forbidden}")

    def validate_config(self, config: ToyEngineConfig) -> None:
        if config.graph_spec_id != "VF-SPEC-GRAPH-001":
            raise ValueError("Unexpected graph_spec_id for v9.2 toy engine.")
        if config.seed_spec_id != "VF-SPEC-SEED-001":
            raise ValueError("Unexpected seed_spec_id for v9.2 toy engine.")
        if config.initialization_spec_id != "VF-SPEC-INIT-001":
            raise ValueError("Unexpected initialization_spec_id for v9.2 toy engine.")
        if config.node_count not in {16, 32, 64}:
            raise ValueError("node_count must use the v9.1 specified toy values.")
        if config.packet_count not in {32, 64, 128}:
            raise ValueError("packet_count must use the v9.1 specified toy values.")
        if config.step_count_limit <= 0:
            raise ValueError("step_count_limit must be positive.")
        for seed_name in [
            "graph_seed",
            "packet_seed",
            "transition_seed",
            "symbolic_drift_seed",
        ]:
            seed_value = getattr(config, seed_name)
            if not isinstance(seed_value, int):
                raise ValueError(f"{seed_name} must be an integer.")

    def build_toy_graph(self, config: ToyEngineConfig) -> ToyGraph:
        """Build a deterministic unitless toy graph.

        This method is implemented in v9.2 but not executed by the v9.2 milestone tests
        as a simulation run. Future milestones may call it under the safe toy boundary.
        """

        self.validate_config(config)

        nodes: List[ToyNode] = []
        for node_id in range(config.node_count):
            base = ((node_id + config.graph_seed) % 97) / 96.0
            nodes.append(
                ToyNode(
                    node_id=node_id,
                    node_state_vector=(
                        round(base, 6),
                        round((base * 0.5 + 0.1) % 1.0, 6),
                        round((base * 0.25 + 0.2) % 1.0, 6),
                        round((base * 0.125 + 0.3) % 1.0, 6),
                    ),
                    node_constraint_profile=(
                        round((base + 0.11) % 1.0, 6),
                        round((base + 0.23) % 1.0, 6),
                        round((base + 0.37) % 1.0, 6),
                        round((base + 0.41) % 1.0, 6),
                    ),
                )
            )

        edges: List[ToyEdge] = []
        edge_id = 0
        for source_node_id in range(config.node_count):
            for offset in (1, 3):
                target_node_id = (source_node_id + offset) % config.node_count
                weight = ((source_node_id + target_node_id + config.graph_seed) % 31) / 30.0
                edges.append(
                    ToyEdge(
                        edge_id=edge_id,
                        source_node_id=source_node_id,
                        target_node_id=target_node_id,
                        edge_weight=round(weight, 6),
                        transition_channel_label=f"toy_channel_{offset}",
                    )
                )
                edge_id += 1

        return ToyGraph(
            graph_spec_id=config.graph_spec_id,
            nodes=tuple(nodes),
            edges=tuple(edges),
        )

    def initialize_toy_packets(self, config: ToyEngineConfig) -> Tuple[ToyPacket, ...]:
        """Initialize deterministic unitless toy packets.

        Packets are symbolic toy state carriers only. They are not biological agents.
        """

        self.validate_config(config)

        packets: List[ToyPacket] = []
        for packet_id in range(config.packet_count):
            base = ((packet_id + config.packet_seed) % 89) / 88.0
            packets.append(
                ToyPacket(
                    packet_id=packet_id,
                    packet_state_vector=(
                        round(base, 6),
                        round((base * 0.5 + 0.07) % 1.0, 6),
                        round((base * 0.25 + 0.13) % 1.0, 6),
                        round((base * 0.125 + 0.19) % 1.0, 6),
                        round((base * 0.0625 + 0.29) % 1.0, 6),
                        round((base * 0.03125 + 0.31) % 1.0, 6),
                    ),
                    current_node_id=packet_id % config.node_count,
                    compatibility_score=0.0,
                    local_constraint_score=0.0,
                    global_constraint_score=0.0,
                    causal_mass_score=0.0,
                    memory_trace=tuple(),
                    symbolic_drift=0.0,
                    survival_indicator=True,
                    time_layer="t1",
                )
            )

        return tuple(packets)

    def compatibility_score(self, packet: ToyPacket, node: ToyNode) -> float:
        packet_values = packet.packet_state_vector[: len(node.node_state_vector)]
        distance = sum(abs(a - b) for a, b in zip(packet_values, node.node_state_vector))
        score = 1.0 - min(1.0, distance / max(1, len(node.node_state_vector)))
        return round(score, 6)

    def local_constraint_score(self, packet: ToyPacket, node: ToyNode) -> float:
        packet_values = packet.packet_state_vector[: len(node.node_constraint_profile)]
        distance = sum(abs(a - b) for a, b in zip(packet_values, node.node_constraint_profile))
        score = 1.0 - min(1.0, distance / max(1, len(node.node_constraint_profile)))
        return round(score, 6)

    def global_constraint_score(self, packets: Sequence[ToyPacket]) -> float:
        if not packets:
            return 0.0
        active_fraction = sum(1 for packet in packets if packet.survival_indicator) / len(packets)
        return round(active_fraction, 6)

    def causal_mass_score(self, packet: ToyPacket) -> float:
        memory_factor = min(1.0, len(packet.memory_trace) / 10.0)
        time_factor = {"t1": 0.1, "t2": 0.2, "t3": 0.3}.get(packet.time_layer, 0.1)
        return round(min(1.0, packet.causal_mass_score + memory_factor + time_factor), 6)

    def one_step_transition(
        self,
        config: ToyEngineConfig,
        graph: ToyGraph,
        packets: Sequence[ToyPacket],
        packet: ToyPacket,
    ) -> ToyPacket:
        """Compute one abstract toy transition.

        This method is implemented but not called by v9.2 as a simulation execution.
        """

        self.validate_config(config)

        node_lookup: Dict[int, ToyNode] = {node.node_id: node for node in graph.nodes}
        current_node = node_lookup[packet.current_node_id]

        compatibility = self.compatibility_score(packet, current_node)
        local_constraint = self.local_constraint_score(packet, current_node)
        global_constraint = self.global_constraint_score(packets)
        causal_mass = self.causal_mass_score(packet)

        outgoing = [edge for edge in graph.edges if edge.source_node_id == packet.current_node_id]
        if outgoing:
            edge_index = (packet.packet_id + config.transition_seed + len(packet.memory_trace)) % len(outgoing)
            selected_edge = outgoing[edge_index]
            next_node_id = selected_edge.target_node_id
        else:
            next_node_id = packet.current_node_id

        violation_indicator = local_constraint < 0.2 or global_constraint < 0.2
        survival_indicator = packet.survival_indicator and not violation_indicator
        symbolic_drift = ((packet.packet_id + config.symbolic_drift_seed) % 17) / 100.0

        if packet.time_layer == "t1":
            next_time_layer = "t2"
        elif packet.time_layer == "t2":
            next_time_layer = "t3"
        else:
            next_time_layer = "t3"

        memory_entry = (
            f"toy_transition:{packet.current_node_id}->{next_node_id}:"
            f"lc={local_constraint}:gc={global_constraint}:cm={causal_mass}:v={violation_indicator}"
        )

        return ToyPacket(
            packet_id=packet.packet_id,
            packet_state_vector=tuple(
                round(min(1.0, max(0.0, value + symbolic_drift)), 6)
                for value in packet.packet_state_vector
            ),
            current_node_id=next_node_id,
            compatibility_score=compatibility,
            local_constraint_score=local_constraint,
            global_constraint_score=global_constraint,
            causal_mass_score=causal_mass,
            memory_trace=packet.memory_trace + (memory_entry,),
            symbolic_drift=round(symbolic_drift, 6),
            survival_indicator=survival_indicator,
            time_layer=next_time_layer,
        )

    def metric_snapshot(self, packets: Sequence[ToyPacket]) -> Dict[str, float]:
        """Return a bounded toy metric snapshot.

        This is a method definition only in v9.2. v9.2 does not report simulation results.
        """

        if not packets:
            return {
                "survival_rate": 0.0,
                "constraint_violation_rate": 0.0,
                "symbolic_drift_rate": 0.0,
                "ledger_effect_size": 0.0,
            }

        survival_rate = sum(1 for packet in packets if packet.survival_indicator) / len(packets)
        violation_rate = sum(
            1
            for packet in packets
            if packet.memory_trace and "v=True" in packet.memory_trace[-1]
        ) / len(packets)
        drift_rate = sum(packet.symbolic_drift for packet in packets) / len(packets)
        ledger_effect_size = sum(len(packet.memory_trace) for packet in packets) / len(packets)

        return {
            "survival_rate": round(survival_rate, 6),
            "constraint_violation_rate": round(violation_rate, 6),
            "symbolic_drift_rate": round(drift_rate, 6),
            "ledger_effect_size": round(ledger_effect_size, 6),
        }


def build_engine_manifest_without_running() -> ToyEngineManifest:
    """Create an engine manifest without executing a simulation run."""

    return SafeAbstractToySimulationEngine().manifest()
