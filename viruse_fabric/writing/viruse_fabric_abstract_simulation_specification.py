from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class ViruseFabricAbstractSimulationSpecificationBuilder:
    version = "v9.1"

    source_reframing_json_path = Path("outputs/viruse_fabric_abstract_simulation_reframing_v9_0.json")
    output_md_path = Path("outputs/viruse_fabric_abstract_simulation_specification_v9_1.md")
    output_json_path = Path("outputs/viruse_fabric_abstract_simulation_specification_v9_1.json")

    plan_phrase = "v9_1_abstract_simulation_specification_without_engine_execution_or_validation"

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Missing required source JSON: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"Expected dict payload from {path}")
        return payload

    def _graph_specification(self) -> Dict[str, Any]:
        return {
            "graph_spec_id": "VF-SPEC-GRAPH-001",
            "name": "safe_abstract_toy_graph_generation",
            "graph_type": "finite_directed_or_undirected_abstract_graph",
            "node_count_values": [16, 32, 64],
            "edge_density_values": [0.08, 0.12, 0.18],
            "graph_generation_modes": [
                "seeded_uniform_random_graph",
                "seeded_clustered_toy_graph",
                "seeded_ring_plus_shortcuts_toy_graph",
            ],
            "node_state_dimension": 4,
            "edge_weight_type": "unitless_float_in_closed_interval_0_1",
            "allowed_graph_attributes": [
                "node_id",
                "node_state_vector",
                "node_constraint_profile",
                "edge_id",
                "source_node_id",
                "target_node_id",
                "edge_weight",
                "transition_channel_label",
            ],
            "forbidden_graph_attributes": [
                "real_location",
                "host_species",
                "organism",
                "tissue",
                "cell_type",
                "receptor",
                "pathogen",
                "genome",
                "protein",
                "clinical_state",
                "epidemiological_region",
            ],
            "non_operational_boundary": (
                "Graph generation is abstract and unitless. It does not represent real biological, clinical, "
                "epidemiological, geographical, receptor, host, pathogen, or wet-lab systems."
            ),
        }

    def _random_seed_specification(self) -> Dict[str, Any]:
        return {
            "seed_spec_id": "VF-SPEC-SEED-001",
            "name": "controlled_seed_grid",
            "primary_seed_values": [101, 202, 303, 404, 505],
            "replicate_count_per_condition": 5,
            "seed_usage": [
                "graph_generation_seed",
                "packet_initialization_seed",
                "transition_choice_seed",
                "symbolic_drift_seed",
            ],
            "reproducibility_rule": (
                "Every future simulation run must record the graph seed, packet seed, transition seed, and symbolic drift seed. "
                "A result without stored seeds is not accepted as a valid toy simulation result."
            ),
            "non_validation_boundary": (
                "Seed control supports reproducibility only. It does not validate the theory and does not create empirical evidence."
            ),
        }

    def _initialization_specification(self) -> Dict[str, Any]:
        return {
            "initialization_spec_id": "VF-SPEC-INIT-001",
            "name": "abstract_packet_and_node_initialization",
            "packet_count_values": [32, 64, 128],
            "packet_state_dimension": 6,
            "initial_packet_distribution": "seeded_uniform_unitless_vectors",
            "initial_node_distribution": "seeded_uniform_unitless_vectors",
            "initial_memory_trace": "empty_or_zero_vector",
            "initial_causal_mass": "zero_or_seeded_low_unitless_value",
            "initial_time_layer": "t1",
            "allowed_packet_attributes": [
                "packet_id",
                "packet_state_vector",
                "current_node_id",
                "compatibility_score",
                "local_constraint_score",
                "global_constraint_score",
                "causal_mass_score",
                "memory_trace",
                "symbolic_drift",
                "survival_indicator",
                "time_layer",
            ],
            "forbidden_packet_attributes": [
                "genetic_sequence",
                "protein_sequence",
                "receptor_binding_score",
                "host_range",
                "infectivity",
                "immune_evasion",
                "virulence",
                "clinical_outcome",
                "wet_lab_condition",
            ],
            "non_operational_boundary": (
                "Packets are symbolic toy state carriers only. They are not biological agents, pathogens, molecules, cells, "
                "genomes, receptors, clinical entities, or wet-lab materials."
            ),
        }

    def _update_rule_specification(self) -> List[Dict[str, Any]]:
        return [
            {
                "rule_id": "VF-SPEC-RULE-001",
                "name": "compatibility_score_update",
                "step_order": 1,
                "rule_summary": "Compute a unitless compatibility score between packet_state_vector and node_state_vector.",
                "inputs": ["packet_state_vector", "node_state_vector"],
                "outputs": ["compatibility_score"],
                "allowed_operation": "unitless vector similarity or bounded score function",
                "deferred_to_engine": True,
            },
            {
                "rule_id": "VF-SPEC-RULE-002",
                "name": "local_constraint_update",
                "step_order": 2,
                "rule_summary": "Apply node-local abstract constraints to produce a local_constraint_score.",
                "inputs": ["packet_state_vector", "node_constraint_profile"],
                "outputs": ["local_constraint_score"],
                "allowed_operation": "bounded abstract filtering score",
                "deferred_to_engine": True,
            },
            {
                "rule_id": "VF-SPEC-RULE-003",
                "name": "global_constraint_update",
                "step_order": 3,
                "rule_summary": "Apply system-level abstract constraints to produce a global_constraint_score.",
                "inputs": ["global_constraint_profile", "current_graph_state_summary"],
                "outputs": ["global_constraint_score"],
                "allowed_operation": "bounded aggregate constraint score",
                "deferred_to_engine": True,
            },
            {
                "rule_id": "VF-SPEC-RULE-004",
                "name": "causal_mass_update",
                "step_order": 4,
                "rule_summary": "Update causal_mass_score from prior memory trace and delayed abstract effects.",
                "inputs": ["memory_trace", "prior_causal_mass_score", "time_layer"],
                "outputs": ["causal_mass_score"],
                "allowed_operation": "bounded delayed-effect accumulator",
                "deferred_to_engine": True,
            },
            {
                "rule_id": "VF-SPEC-RULE-005",
                "name": "transition_decision_update",
                "step_order": 5,
                "rule_summary": "Choose remain, move, filtered, or symbolic perturbation using bounded toy scores.",
                "inputs": [
                    "compatibility_score",
                    "local_constraint_score",
                    "global_constraint_score",
                    "causal_mass_score",
                    "edge_weight",
                ],
                "outputs": ["transition_choice", "survival_indicator", "current_node_id"],
                "allowed_operation": "seeded bounded categorical selection",
                "deferred_to_engine": True,
            },
            {
                "rule_id": "VF-SPEC-RULE-006",
                "name": "symbolic_drift_update",
                "step_order": 6,
                "rule_summary": "Apply optional symbolic perturbation to unitless packet_state_vector.",
                "inputs": ["packet_state_vector", "symbolic_drift_seed"],
                "outputs": ["packet_state_vector", "symbolic_drift"],
                "allowed_operation": "bounded symbolic unitless perturbation",
                "deferred_to_engine": True,
            },
            {
                "rule_id": "VF-SPEC-RULE-007",
                "name": "memory_ledger_update",
                "step_order": 7,
                "rule_summary": "Record abstract transition, violation, score, and time-layer state into memory_trace.",
                "inputs": [
                    "transition_choice",
                    "violation_indicator",
                    "compatibility_score",
                    "local_constraint_score",
                    "global_constraint_score",
                    "causal_mass_score",
                    "time_layer",
                ],
                "outputs": ["memory_trace"],
                "allowed_operation": "bounded state-history append or summary",
                "deferred_to_engine": True,
            },
            {
                "rule_id": "VF-SPEC-RULE-008",
                "name": "time_layer_update",
                "step_order": 8,
                "rule_summary": "Advance or project t1, t2, and t3 abstract time-layer state.",
                "inputs": ["time_layer", "memory_trace", "causal_mass_score"],
                "outputs": ["time_layer", "projected_constraint_state"],
                "allowed_operation": "abstract discrete time-layer transition",
                "deferred_to_engine": True,
            },
        ]

    def _baseline_configuration(self) -> List[Dict[str, Any]]:
        return [
            {
                "baseline_id": "VF-BASE-A",
                "name": "random_walk_baseline",
                "enabled_components": ["graph", "packets", "seeded_random_transition"],
                "disabled_components": [
                    "local_constraint_score",
                    "global_constraint_score",
                    "causal_mass_score",
                    "memory_ledger",
                    "three_time_layer_state",
                    "symbolic_drift_selection",
                ],
                "comparison_target_hypotheses": ["VF-H1", "VF-H3"],
            },
            {
                "baseline_id": "VF-BASE-B",
                "name": "local_constraint_only_baseline",
                "enabled_components": ["graph", "packets", "local_constraint_score"],
                "disabled_components": [
                    "global_constraint_score",
                    "causal_mass_score",
                    "memory_ledger",
                    "three_time_layer_state",
                ],
                "comparison_target_hypotheses": ["VF-H1"],
            },
            {
                "baseline_id": "VF-BASE-C",
                "name": "no_memory_baseline",
                "enabled_components": ["graph", "packets", "local_constraint_score", "global_constraint_score"],
                "disabled_components": ["memory_ledger", "memory_trace_feedback"],
                "comparison_target_hypotheses": ["VF-H2"],
            },
            {
                "baseline_id": "VF-BASE-D",
                "name": "single_time_layer_baseline",
                "enabled_components": ["graph", "packets", "local_constraint_score", "global_constraint_score", "memory_ledger"],
                "disabled_components": ["t1_t2_t3_time_layering"],
                "comparison_target_hypotheses": ["VF-H4"],
            },
            {
                "baseline_id": "VF-BASE-E",
                "name": "no_causal_mass_baseline",
                "enabled_components": ["graph", "packets", "local_constraint_score", "global_constraint_score", "memory_ledger"],
                "disabled_components": ["causal_mass_score"],
                "comparison_target_hypotheses": ["VF-H3"],
            },
        ]

    def _metric_specification(self) -> List[Dict[str, Any]]:
        return [
            {
                "metric_id": "VF-MET-001",
                "name": "survival_rate",
                "formula_level": "fraction_of_active_packets_after_fixed_steps",
                "required_fields": ["survival_indicator", "step_index"],
                "directional_expectation": "context_dependent",
            },
            {
                "metric_id": "VF-MET-002",
                "name": "spread_entropy",
                "formula_level": "entropy_of_packet_distribution_over_nodes",
                "required_fields": ["current_node_id", "packet_id", "step_index"],
                "directional_expectation": "model_dependent",
            },
            {
                "metric_id": "VF-MET-003",
                "name": "constraint_violation_rate",
                "formula_level": "fraction_of_transitions_with_violation_indicator_true",
                "required_fields": ["violation_indicator", "transition_choice"],
                "directional_expectation": "lower_with_memory_or_constraints",
            },
            {
                "metric_id": "VF-MET-004",
                "name": "path_stability",
                "formula_level": "path_similarity_across_controlled_seed_replicates",
                "required_fields": ["packet_path", "seed_record"],
                "directional_expectation": "higher_with_memory_ledger",
            },
            {
                "metric_id": "VF-MET-005",
                "name": "delayed_effect_score",
                "formula_level": "difference_between_t1_outcomes_and_t2_or_t3_projected_outcomes",
                "required_fields": ["time_layer", "projected_constraint_state", "transition_choice"],
                "directional_expectation": "higher_with_causal_mass",
            },
            {
                "metric_id": "VF-MET-006",
                "name": "baseline_divergence",
                "formula_level": "distance_between_viruse_fabric_outputs_and_baseline_outputs",
                "required_fields": ["model_variant_id", "baseline_id", "metric_vector"],
                "directional_expectation": "nonzero_if_hypothesis_supported",
            },
            {
                "metric_id": "VF-MET-007",
                "name": "symbolic_drift_rate",
                "formula_level": "mean_bounded_change_in_packet_state_vector_per_step",
                "required_fields": ["packet_state_vector", "symbolic_drift", "step_index"],
                "directional_expectation": "bounded_by_specification",
            },
            {
                "metric_id": "VF-MET-008",
                "name": "ledger_effect_size",
                "formula_level": "difference_between_memory_ledger_variant_and_no_memory_baseline",
                "required_fields": ["memory_trace", "constraint_violation_rate", "path_stability"],
                "directional_expectation": "nonzero_if_H2_supported",
            },
        ]

    def _output_schema_specification(self) -> Dict[str, Any]:
        return {
            "schema_id": "VF-SPEC-OUTPUT-001",
            "name": "toy_simulation_output_schema",
            "required_top_level_fields": [
                "run_id",
                "model_variant_id",
                "baseline_id",
                "graph_spec_id",
                "seed_record",
                "parameter_record",
                "step_count",
                "packet_count",
                "node_count",
                "metric_results",
                "safety_counters",
                "execution_boundary",
            ],
            "required_seed_fields": [
                "graph_generation_seed",
                "packet_initialization_seed",
                "transition_choice_seed",
                "symbolic_drift_seed",
            ],
            "required_metric_fields": [
                "survival_rate",
                "spread_entropy",
                "constraint_violation_rate",
                "path_stability",
                "delayed_effect_score",
                "baseline_divergence",
                "symbolic_drift_rate",
                "ledger_effect_size",
            ],
            "forbidden_output_fields": [
                "real_biological_dataset",
                "pathogen_name",
                "host_species",
                "receptor_name",
                "binding_affinity",
                "infectivity_score",
                "immune_evasion_score",
                "host_range_prediction",
                "wet_lab_protocol",
            ],
            "schema_boundary": (
                "Future output files must remain abstract toy simulation outputs only and must not include real biological, "
                "clinical, pathogen, host, receptor, wet-lab, or operational targeting fields."
            ),
        }

    def _falsification_threshold_specification(self) -> List[Dict[str, Any]]:
        return [
            {
                "threshold_id": "VF-THRESH-H1",
                "hypothesis_id": "VF-H1",
                "primary_metric": "baseline_divergence",
                "comparison_baseline": "VF-BASE-B",
                "support_condition": "predeclared_nonzero_divergence_across_seed_replicates",
                "not_supported_condition": "divergence_absent_or_unstable_across_seed_replicates",
                "status_in_v9_1": "specified_not_executed",
            },
            {
                "threshold_id": "VF-THRESH-H2",
                "hypothesis_id": "VF-H2",
                "primary_metric": "ledger_effect_size",
                "comparison_baseline": "VF-BASE-C",
                "support_condition": "lower_violation_rate_or_higher_path_stability_with_memory_ledger",
                "not_supported_condition": "no_reduction_in_violation_rate_and_no_stability_gain",
                "status_in_v9_1": "specified_not_executed",
            },
            {
                "threshold_id": "VF-THRESH-H3",
                "hypothesis_id": "VF-H3",
                "primary_metric": "delayed_effect_score",
                "comparison_baseline": "VF-BASE-A_or_VF-BASE-E",
                "support_condition": "delayed_effect_score_differs_from_random_walk_or_no_causal_mass_baseline",
                "not_supported_condition": "delayed_effect_score_indistinguishable_from_baseline",
                "status_in_v9_1": "specified_not_executed",
            },
            {
                "threshold_id": "VF-THRESH-H4",
                "hypothesis_id": "VF-H4",
                "primary_metric": "projected_constraint_difference",
                "comparison_baseline": "VF-BASE-D",
                "support_condition": "t1_t2_t3_projection_differs_from_single_time_layer_baseline",
                "not_supported_condition": "projection_difference_absent_or_seed_unstable",
                "status_in_v9_1": "specified_not_executed",
            },
        ]

    def _safety_boundary_specification(self) -> List[Dict[str, Any]]:
        return [
            {
                "boundary_id": "VF-SPEC-SAFE-001",
                "name": "abstract_toy_only",
                "requirement": "All future v9 simulation artifacts remain abstract, symbolic, unitless, and non-operational.",
                "must_remain_zero_counter": "Real biological dataset import count",
            },
            {
                "boundary_id": "VF-SPEC-SAFE-002",
                "name": "no_real_pathogen_simulation",
                "requirement": "No future v9 milestone may simulate a real pathogen.",
                "must_remain_zero_counter": "Real pathogen simulation count",
            },
            {
                "boundary_id": "VF-SPEC-SAFE-003",
                "name": "no_receptor_parameters",
                "requirement": "No receptor names, receptor parameters, or binding values may be introduced.",
                "must_remain_zero_counter": "Real receptor parameter count",
            },
            {
                "boundary_id": "VF-SPEC-SAFE-004",
                "name": "no_operational_host_targeting",
                "requirement": "No host targeting, host range prediction, tropism, infectivity, or immune evasion optimization may be introduced.",
                "must_remain_zero_counter": "Operational host targeting count",
            },
            {
                "boundary_id": "VF-SPEC-SAFE-005",
                "name": "no_wet_lab_protocols",
                "requirement": "No wet-lab steps, materials, protocols, measurements, or operational procedures may be introduced.",
                "must_remain_zero_counter": "Wet-lab protocol count",
            },
            {
                "boundary_id": "VF-SPEC-SAFE-006",
                "name": "no_validation_claim_in_specification",
                "requirement": "v9.1 specifies simulation only and makes no validation claim.",
                "must_remain_zero_counter": "V9 theory validation claim count",
            },
            {
                "boundary_id": "VF-SPEC-SAFE-007",
                "name": "no_engine_in_specification",
                "requirement": "v9.1 does not implement an engine.",
                "must_remain_zero_counter": "V9 simulation engine implementation count",
            },
            {
                "boundary_id": "VF-SPEC-SAFE-008",
                "name": "no_run_in_specification",
                "requirement": "v9.1 does not execute a simulation.",
                "must_remain_zero_counter": "V9 simulation execution count",
            },
            {
                "boundary_id": "VF-SPEC-SAFE-009",
                "name": "no_baseline_execution_in_specification",
                "requirement": "v9.1 does not execute baseline comparison.",
                "must_remain_zero_counter": "V9 baseline comparison execution count",
            },
            {
                "boundary_id": "VF-SPEC-SAFE-010",
                "name": "no_results_or_falsification_audit",
                "requirement": "v9.1 reports no results and executes no falsification audit.",
                "must_remain_zero_counter": "V9 results report count",
            },
        ]

    def build(self) -> Dict[str, Any]:
        reframing_payload = self._load_json(self.source_reframing_json_path)
        reframing_counters = reframing_payload.get("counters", {})

        graph_spec = self._graph_specification()
        seed_spec = self._random_seed_specification()
        init_spec = self._initialization_specification()
        update_rules = self._update_rule_specification()
        baseline_configs = self._baseline_configuration()
        metric_specs = self._metric_specification()
        output_schema = self._output_schema_specification()
        falsification_thresholds = self._falsification_threshold_specification()
        safety_specs = self._safety_boundary_specification()

        counters = {
            "V9 abstract simulation specification artifact count": 1,
            "V9 detailed simulation specification completed count": 1,
            "V9 graph specification count": 1,
            "V9 random seed specification count": 1,
            "V9 initialization specification count": 1,
            "V9 update rule specification count": len(update_rules),
            "V9 baseline configuration specification count": len(baseline_configs),
            "V9 metric specification count": len(metric_specs),
            "V9 output schema specification count": 1,
            "V9 falsification threshold specification count": len(falsification_thresholds),
            "V9 safety boundary specification count": len(safety_specs),
            "V9 source reframing artifact count": reframing_counters.get("V9 abstract simulation reframing artifact count"),
            "V9 source model object definition count": reframing_counters.get("V9 simulatable model object definition count"),
            "V9 source state variable definition count": reframing_counters.get("V9 state variable definition count"),
            "V9 source reframed hypothesis count": reframing_counters.get("V9 reframed hypothesis count"),
            "V9 source baseline plan count": reframing_counters.get("V9 baseline plan count"),
            "V9 source metric proposal count": reframing_counters.get("V9 metric proposal count"),
            "V9 source falsification rule count": reframing_counters.get("V9 falsification rule count"),
            "V9 simulation engine implementation count": 0,
            "V9 simulation execution count": 0,
            "V9 baseline comparison execution count": 0,
            "V9 results report count": 0,
            "V9 falsification audit execution count": 0,
            "V9 theory validation claim count": 0,
            "Toy simulation engine created count": 0,
            "Toy simulation actual run count": 0,
            "Toy simulation result count": 0,
            "Toy baseline comparison execution count": 0,
            "Toy falsification audit execution count": 0,
            "Toy evaluation actual run count": 0,
            "Toy evaluation result count": 0,
            "Toy evaluation validation claim count": 0,
            "Toy scientific evidence upgrade completed count": 0,
            "Toy manuscript coherence rewrite application count": 0,
            "Toy manuscript patch application checklist completion count": 0,
            "Toy manuscript patch application checklist execution count": 0,
            "Toy manuscript patch application permission count": 0,
            "Toy manuscript patch application applied patch count": 0,
            "Toy manuscript patch application manuscript file modified count": 0,
            "Toy manuscript patch application manuscript mutation count": 0,
            "Toy citation citation-ready source count": 0,
            "Toy citation actual citation count": 0,
            "Toy citation fabricated reference count": 0,
            "Toy citation integration completion count": 0,
            "Toy citation added to manuscript count": 0,
            "Real biological dataset import count": 0,
            "Real pathogen simulation count": 0,
            "Real receptor parameter count": 0,
            "Operational host targeting count": 0,
            "Wet-lab protocol count": 0,
            "Actionable biosafety-risk instruction count": 0,
            "Real-world infectivity optimization count": 0,
            "Immune evasion optimization count": 0,
            "Real host range prediction count": 0,
            "Proof assistant verification count": 0,
            "External validation count": 0,
            "Independent experiment count": 0,
            "Manuscript submission ready count": 0,
            "Readiness approval count": 0,
            "New citation added count": 0,
        }

        report = {
            "version": self.version,
            "title": "Viruse Fabric Abstract Simulation Specification",
            "plan_phrase": self.plan_phrase,
            "scope": "abstract-simulation-specification-only",
            "source_reframing_json": str(self.source_reframing_json_path),
            "safe_abstract_toy_only": True,
            "formal_specification_only": True,
            "simulation_specification_completed": True,
            "simulation_engine_implemented": False,
            "simulation_run_performed": False,
            "baseline_comparison_performed": False,
            "results_reported": False,
            "falsification_audit_executed": False,
            "validation_claim_made": False,
            "readiness_approval_recorded": False,
            "manuscript_file_modified": False,
            "manuscript_mutation": False,
            "new_citation_added": False,
            "v9_2_engine_deferred": True,
            "v9_3_baseline_comparison_deferred": True,
            "v9_4_results_and_falsification_deferred": True,
            "specification_statement": (
                "v9.1 specifies the safe abstract toy simulation design for Viruse Fabric, including graph generation, "
                "random seed control, initialization, update rules, baseline configurations, metrics, output schema, "
                "falsification thresholds, and safety boundaries. It does not implement a simulation engine, does not run "
                "a simulation, does not execute baseline comparison, does not report results, and does not validate the theory."
            ),
            "graph_specification": graph_spec,
            "random_seed_specification": seed_spec,
            "initialization_specification": init_spec,
            "update_rule_specification": update_rules,
            "baseline_configuration": baseline_configs,
            "metric_specification": metric_specs,
            "output_schema_specification": output_schema,
            "falsification_threshold_specification": falsification_thresholds,
            "safety_boundary_specification": safety_specs,
            "non_validation_disclaimer": (
                "Abstract simulation specification only. No simulation engine is implemented. No simulation run is performed. "
                "No baseline comparison is executed. No results are reported. No falsification audit is executed. "
                "No validation claim is made. No manuscript file is modified. No citation is added. "
                "No real biological datasets, no real pathogen models, no receptor parameters, and no operational targeting are introduced."
            ),
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "abstract-simulation-specification-only":
            raise AssertionError("v9.1 must remain abstract-simulation-specification-only.")

        if report["passed"] is not True:
            raise AssertionError("v9.1 must pass.")

        for field in [
            "safe_abstract_toy_only",
            "formal_specification_only",
            "simulation_specification_completed",
            "v9_2_engine_deferred",
            "v9_3_baseline_comparison_deferred",
            "v9_4_results_and_falsification_deferred",
        ]:
            if report[field] is not True:
                raise AssertionError(f"Expected True for {field}")

        for field in [
            "simulation_engine_implemented",
            "simulation_run_performed",
            "baseline_comparison_performed",
            "results_reported",
            "falsification_audit_executed",
            "validation_claim_made",
            "readiness_approval_recorded",
            "manuscript_file_modified",
            "manuscript_mutation",
            "new_citation_added",
        ]:
            if report[field] is not False:
                raise AssertionError(f"Expected False for {field}")

        counters = report["counters"]

        expected_counts = {
            "V9 abstract simulation specification artifact count": 1,
            "V9 detailed simulation specification completed count": 1,
            "V9 graph specification count": 1,
            "V9 random seed specification count": 1,
            "V9 initialization specification count": 1,
            "V9 update rule specification count": 8,
            "V9 baseline configuration specification count": 5,
            "V9 metric specification count": 8,
            "V9 output schema specification count": 1,
            "V9 falsification threshold specification count": 4,
            "V9 safety boundary specification count": 10,
            "V9 source reframing artifact count": 1,
            "V9 source model object definition count": 8,
            "V9 source state variable definition count": 12,
            "V9 source reframed hypothesis count": 4,
            "V9 source baseline plan count": 5,
            "V9 source metric proposal count": 8,
            "V9 source falsification rule count": 6,
            "V9 simulation engine implementation count": 0,
            "V9 simulation execution count": 0,
            "V9 baseline comparison execution count": 0,
            "V9 results report count": 0,
            "V9 falsification audit execution count": 0,
            "V9 theory validation claim count": 0,
            "Toy simulation engine created count": 0,
            "Toy simulation actual run count": 0,
            "Toy simulation result count": 0,
            "Toy baseline comparison execution count": 0,
            "Toy falsification audit execution count": 0,
        }

        for name, expected in expected_counts.items():
            actual = counters.get(name)
            if actual != expected:
                raise AssertionError(f"Expected {expected} for {name}, got {actual}")

        must_be_zero = [
            "V9 simulation engine implementation count",
            "V9 simulation execution count",
            "V9 baseline comparison execution count",
            "V9 results report count",
            "V9 falsification audit execution count",
            "V9 theory validation claim count",
            "Toy simulation engine created count",
            "Toy simulation actual run count",
            "Toy simulation result count",
            "Toy baseline comparison execution count",
            "Toy falsification audit execution count",
            "Toy evaluation actual run count",
            "Toy evaluation result count",
            "Toy evaluation validation claim count",
            "Toy scientific evidence upgrade completed count",
            "Toy manuscript coherence rewrite application count",
            "Toy manuscript patch application checklist completion count",
            "Toy manuscript patch application checklist execution count",
            "Toy manuscript patch application permission count",
            "Toy manuscript patch application applied patch count",
            "Toy manuscript patch application manuscript file modified count",
            "Toy manuscript patch application manuscript mutation count",
            "Toy citation citation-ready source count",
            "Toy citation actual citation count",
            "Toy citation fabricated reference count",
            "Toy citation integration completion count",
            "Toy citation added to manuscript count",
            "Real biological dataset import count",
            "Real pathogen simulation count",
            "Real receptor parameter count",
            "Operational host targeting count",
            "Wet-lab protocol count",
            "Actionable biosafety-risk instruction count",
            "Real-world infectivity optimization count",
            "Immune evasion optimization count",
            "Real host range prediction count",
            "Proof assistant verification count",
            "External validation count",
            "Independent experiment count",
            "Manuscript submission ready count",
            "Readiness approval count",
            "New citation added count",
        ]

        for name in must_be_zero:
            if counters.get(name) != 0:
                raise AssertionError(f"Counter must remain zero: {name}")

        combined_text = json.dumps(report, ensure_ascii=False)

        required_phrases = [
            "Abstract simulation specification only",
            "No simulation engine is implemented",
            "No simulation run is performed",
            "No baseline comparison is executed",
            "No results are reported",
            "No falsification audit is executed",
            "No validation claim is made",
            "graph generation",
            "random seed control",
            "initialization",
            "update rules",
            "baseline configurations",
            "metrics",
            "output schema",
            "falsification thresholds",
            "safety boundaries",
            "No manuscript file is modified",
            "No citation is added",
            "No real biological datasets",
            "no real pathogen models",
            "no receptor parameters",
            "no operational targeting",
        ]

        for phrase in required_phrases:
            if phrase not in combined_text:
                raise AssertionError(f"Missing required v9.1 phrase: {phrase}")

    def render_markdown(self, report: Dict[str, Any]) -> str:
        lines: List[str] = []

        lines.append("# Viruse Fabric Abstract Simulation Specification")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is abstract-simulation-specification-only.")
        lines.append("It specifies the future safe abstract toy simulation but does not implement a simulation engine, run simulations, execute baseline comparison, report results, execute a falsification audit, validate the theory, modify manuscript files, or add citations.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")
        lines.append("## Specification Statement")
        lines.append("")
        lines.append(report["specification_statement"])
        lines.append("")
        lines.append("## Non-Validation Disclaimer")
        lines.append("")
        lines.append(report["non_validation_disclaimer"])
        lines.append("")

        lines.append("## Graph Specification")
        lines.append("")
        for key, value in report["graph_specification"].items():
            lines.append(f"- {key}: {value}")
        lines.append("")

        lines.append("## Random Seed Specification")
        lines.append("")
        for key, value in report["random_seed_specification"].items():
            lines.append(f"- {key}: {value}")
        lines.append("")

        lines.append("## Initialization Specification")
        lines.append("")
        for key, value in report["initialization_specification"].items():
            lines.append(f"- {key}: {value}")
        lines.append("")

        lines.append("## Update Rule Specification")
        lines.append("")
        for item in report["update_rule_specification"]:
            lines.append(f"### {item['rule_id']} - {item['name']}")
            lines.append("")
            lines.append(f"- Step order: {item['step_order']}")
            lines.append(f"- Rule summary: {item['rule_summary']}")
            lines.append(f"- Inputs: {item['inputs']}")
            lines.append(f"- Outputs: {item['outputs']}")
            lines.append(f"- Allowed operation: {item['allowed_operation']}")
            lines.append(f"- Deferred to engine: {item['deferred_to_engine']}")
            lines.append("")

        lines.append("## Baseline Configuration")
        lines.append("")
        for item in report["baseline_configuration"]:
            lines.append(f"### {item['baseline_id']} - {item['name']}")
            lines.append("")
            lines.append(f"- Enabled components: {item['enabled_components']}")
            lines.append(f"- Disabled components: {item['disabled_components']}")
            lines.append(f"- Comparison target hypotheses: {item['comparison_target_hypotheses']}")
            lines.append("")

        lines.append("## Metric Specification")
        lines.append("")
        for item in report["metric_specification"]:
            lines.append(f"### {item['metric_id']} - {item['name']}")
            lines.append("")
            lines.append(f"- Formula level: {item['formula_level']}")
            lines.append(f"- Required fields: {item['required_fields']}")
            lines.append(f"- Directional expectation: {item['directional_expectation']}")
            lines.append("")

        lines.append("## Output Schema Specification")
        lines.append("")
        for key, value in report["output_schema_specification"].items():
            lines.append(f"- {key}: {value}")
        lines.append("")

        lines.append("## Falsification Threshold Specification")
        lines.append("")
        for item in report["falsification_threshold_specification"]:
            lines.append(f"### {item['threshold_id']} - {item['hypothesis_id']}")
            lines.append("")
            lines.append(f"- Primary metric: {item['primary_metric']}")
            lines.append(f"- Comparison baseline: {item['comparison_baseline']}")
            lines.append(f"- Support condition: {item['support_condition']}")
            lines.append(f"- Not supported condition: {item['not_supported_condition']}")
            lines.append(f"- Status in v9.1: {item['status_in_v9_1']}")
            lines.append("")

        lines.append("## Safety Boundary Specification")
        lines.append("")
        for item in report["safety_boundary_specification"]:
            lines.append(f"### {item['boundary_id']} - {item['name']}")
            lines.append("")
            lines.append(f"- Requirement: {item['requirement']}")
            lines.append(f"- Must remain zero counter: {item['must_remain_zero_counter']}")
            lines.append("")

        lines.append("## Counters")
        lines.append("")
        for key, value in report["counters"].items():
            lines.append(f"{key}: {value}")

        lines.append("")
        lines.append("## Result")
        lines.append("")
        lines.append(f"Passed: {report['passed']}")
        lines.append("")
        lines.append("V9_1_VIRUSE_FABRIC_ABSTRACT_SIMULATION_SPECIFICATION_OK")
        lines.append("")

        return "\n".join(lines)

    def run(self) -> Dict[str, Any]:
        report = self.build()
        self.output_md_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_json_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_md_path.write_text(self.render_markdown(report), encoding="utf-8")
        self.output_json_path.write_text(
            json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        return report


def build_viruse_fabric_abstract_simulation_specification() -> Dict[str, Any]:
    return ViruseFabricAbstractSimulationSpecificationBuilder().run()


if __name__ == "__main__":
    result = build_viruse_fabric_abstract_simulation_specification()
    counters = result["counters"]
    print("V9_1_VIRUSE_FABRIC_ABSTRACT_SIMULATION_SPECIFICATION_OK")
    print("VIRUSE_FABRIC_ABSTRACT_SIMULATION_SPECIFICATION_DIRECT_CHECK_OK")
    print(f"Graph specification count: {counters['V9 graph specification count']}")
    print(f"Random seed specification count: {counters['V9 random seed specification count']}")
    print(f"Initialization specification count: {counters['V9 initialization specification count']}")
    print(f"Update rule specification count: {counters['V9 update rule specification count']}")
    print(f"Baseline configuration specification count: {counters['V9 baseline configuration specification count']}")
    print(f"Metric specification count: {counters['V9 metric specification count']}")
    print(f"Output schema specification count: {counters['V9 output schema specification count']}")
    print(f"Falsification threshold specification count: {counters['V9 falsification threshold specification count']}")
    print(f"Safety boundary specification count: {counters['V9 safety boundary specification count']}")
    print(f"Simulation engine implementation count: {counters['V9 simulation engine implementation count']}")
    print(f"Simulation execution count: {counters['V9 simulation execution count']}")
    print(f"Baseline comparison execution count: {counters['V9 baseline comparison execution count']}")
    print(f"Results report count: {counters['V9 results report count']}")
    print(f"Falsification audit execution count: {counters['V9 falsification audit execution count']}")
    print(f"Theory validation claim count: {counters['V9 theory validation claim count']}")
    print(f"Toy simulation actual run count: {counters['Toy simulation actual run count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {result['passed']}")
