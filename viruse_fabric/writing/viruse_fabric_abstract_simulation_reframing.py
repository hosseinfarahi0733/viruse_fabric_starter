from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class ViruseFabricAbstractSimulationReframingBuilder:
    version = "v9.0"

    source_acceptance_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_batch_1_source_acceptance_decision_register_v8_228.json"
    )

    output_md_path = Path("outputs/viruse_fabric_abstract_simulation_reframing_v9_0.md")
    output_json_path = Path("outputs/viruse_fabric_abstract_simulation_reframing_v9_0.json")

    plan_phrase = "v9_0_abstract_simulation_reframing_without_simulation_execution"

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Missing required source JSON: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"Expected dict payload from {path}")
        return payload

    def _model_objects(self) -> List[Dict[str, str]]:
        return [
            {
                "object_id": "VF-OBJ-001",
                "name": "abstract_environment_graph",
                "definition": "A finite directed or undirected toy graph whose nodes represent abstract environments and whose edges represent abstract transition channels.",
                "non_operational_boundary": "No real location, host, organism, receptor, pathogen, tissue, or biological substrate is represented.",
            },
            {
                "object_id": "VF-OBJ-002",
                "name": "pattern_packet",
                "definition": "A symbolic toy agent carrying abstract state variables such as compatibility, cost, memory trace, and constraint score.",
                "non_operational_boundary": "The packet is not a biological agent, pathogen, molecule, cell, genome, protein, receptor, or wet-lab object.",
            },
            {
                "object_id": "VF-OBJ-003",
                "name": "local_constraint_field",
                "definition": "A unitless rule layer applied at individual nodes to determine whether a pattern packet remains, moves, degrades, or is filtered.",
                "non_operational_boundary": "The field is mathematical only and contains no real biological parameters.",
            },
            {
                "object_id": "VF-OBJ-004",
                "name": "global_constraint_field",
                "definition": "A unitless rule layer that applies cross-node pressure or system-level restrictions over the toy graph.",
                "non_operational_boundary": "The field does not model real-world biosafety, infectivity, tropism, or host range.",
            },
            {
                "object_id": "VF-OBJ-005",
                "name": "causal_mass",
                "definition": "A unitless aggregate influence score intended to represent delayed or distributed abstract causal pressure.",
                "non_operational_boundary": "Causal mass is not a physical, biological, clinical, or epidemiological measurement.",
            },
            {
                "object_id": "VF-OBJ-006",
                "name": "memory_ledger",
                "definition": "A state history layer that stores prior abstract decisions, violations, transitions, and delayed effects.",
                "non_operational_boundary": "The ledger stores toy simulation state only and does not store real biological or personal data.",
            },
            {
                "object_id": "VF-OBJ-007",
                "name": "three_time_layer_state",
                "definition": "A tri-temporal representation using t1, t2, and t3 to separate current state, delayed effect, and projected constraint state.",
                "non_operational_boundary": "The time layers are abstract simulation indices, not real clinical or biological timelines.",
            },
            {
                "object_id": "VF-OBJ-008",
                "name": "symbolic_mutation_operator",
                "definition": "A purely symbolic perturbation operator that changes unitless toy attributes of a pattern packet.",
                "non_operational_boundary": "This operator is not genetic, biological, molecular, phenotypic, immune, host-range, or infectivity optimization.",
            },
        ]

    def _state_variables(self) -> List[Dict[str, str]]:
        return [
            {
                "variable_id": "VF-VAR-001",
                "name": "node_state",
                "type": "categorical_or_vector",
                "definition": "Toy environment state attached to each graph node.",
                "unit": "unitless",
            },
            {
                "variable_id": "VF-VAR-002",
                "name": "packet_state",
                "type": "vector",
                "definition": "Toy symbolic attributes carried by each pattern packet.",
                "unit": "unitless",
            },
            {
                "variable_id": "VF-VAR-003",
                "name": "local_constraint_score",
                "type": "float",
                "definition": "Node-level abstract filtering score.",
                "unit": "unitless",
            },
            {
                "variable_id": "VF-VAR-004",
                "name": "global_constraint_score",
                "type": "float",
                "definition": "System-level abstract filtering score.",
                "unit": "unitless",
            },
            {
                "variable_id": "VF-VAR-005",
                "name": "compatibility_score",
                "type": "float",
                "definition": "Toy match score between packet state and node state.",
                "unit": "unitless",
            },
            {
                "variable_id": "VF-VAR-006",
                "name": "causal_mass_score",
                "type": "float",
                "definition": "Aggregate delayed influence score.",
                "unit": "unitless",
            },
            {
                "variable_id": "VF-VAR-007",
                "name": "memory_trace",
                "type": "vector_or_record",
                "definition": "Prior transition and constraint history retained for path dependence.",
                "unit": "unitless",
            },
            {
                "variable_id": "VF-VAR-008",
                "name": "symbolic_drift",
                "type": "float",
                "definition": "Magnitude of symbolic toy-state perturbation over time.",
                "unit": "unitless",
            },
            {
                "variable_id": "VF-VAR-009",
                "name": "survival_indicator",
                "type": "boolean",
                "definition": "Whether a packet remains active in the toy system.",
                "unit": "unitless",
            },
            {
                "variable_id": "VF-VAR-010",
                "name": "transition_choice",
                "type": "categorical",
                "definition": "Toy action selected at a step: remain, move, filtered, or symbolic perturbation.",
                "unit": "unitless",
            },
            {
                "variable_id": "VF-VAR-011",
                "name": "violation_indicator",
                "type": "boolean",
                "definition": "Whether a packet violates a declared abstract constraint.",
                "unit": "unitless",
            },
            {
                "variable_id": "VF-VAR-012",
                "name": "time_layer",
                "type": "categorical",
                "definition": "One of t1, t2, or t3 abstract simulation layers.",
                "unit": "unitless",
            },
        ]

    def _reframed_hypotheses(self) -> List[Dict[str, str]]:
        return [
            {
                "hypothesis_id": "VF-H1",
                "name": "multi_layer_constraint_path_shift",
                "hypothesis": "In an abstract graph, combining local and global constraints changes packet transition paths compared with a local-only baseline.",
                "falsification_condition": "If transition distributions are not detectably different from local-only baseline under predeclared toy metrics, H1 is not supported.",
            },
            {
                "hypothesis_id": "VF-H2",
                "name": "memory_ledger_stability_effect",
                "hypothesis": "A memory-ledger layer reduces repeated constraint violations and increases path stability compared with a no-memory baseline.",
                "falsification_condition": "If violation rates and stability metrics do not improve over the no-memory baseline, H2 is not supported.",
            },
            {
                "hypothesis_id": "VF-H3",
                "name": "causal_mass_delayed_effect",
                "hypothesis": "A causal-mass term produces delayed transition effects that are absent in a memory-free random-walk baseline.",
                "falsification_condition": "If delayed-effect metrics are indistinguishable from the random-walk baseline, H3 is not supported.",
            },
            {
                "hypothesis_id": "VF-H4",
                "name": "three_time_layer_predictive_difference",
                "hypothesis": "A three-time-layer state representation produces different projected constraint outcomes than a single-time-layer state representation.",
                "falsification_condition": "If projected constraint outcomes do not differ from a single-time-layer baseline, H4 is not supported.",
            },
        ]

    def _baseline_plan(self) -> List[Dict[str, str]]:
        return [
            {
                "baseline_id": "VF-BASE-A",
                "name": "random_walk_baseline",
                "definition": "Packets move randomly over the abstract graph without local constraint, global constraint, memory ledger, causal mass, or three-time layering.",
            },
            {
                "baseline_id": "VF-BASE-B",
                "name": "local_constraint_only_baseline",
                "definition": "Packets are filtered only by node-local abstract constraints without global constraint, memory ledger, or causal mass.",
            },
            {
                "baseline_id": "VF-BASE-C",
                "name": "no_memory_baseline",
                "definition": "Packets use local and global constraints but do not retain prior transition or violation history.",
            },
            {
                "baseline_id": "VF-BASE-D",
                "name": "single_time_layer_baseline",
                "definition": "Packets use one abstract time layer instead of the t1, t2, t3 representation.",
            },
            {
                "baseline_id": "VF-BASE-E",
                "name": "no_causal_mass_baseline",
                "definition": "Packets use constraints and memory but exclude delayed causal-mass scoring.",
            },
        ]

    def _metric_proposals(self) -> List[Dict[str, str]]:
        return [
            {
                "metric_id": "VF-MET-001",
                "name": "survival_rate",
                "definition": "Fraction of toy pattern packets remaining active after a fixed number of abstract steps.",
            },
            {
                "metric_id": "VF-MET-002",
                "name": "spread_entropy",
                "definition": "Diversity of packet positions over the abstract graph.",
            },
            {
                "metric_id": "VF-MET-003",
                "name": "constraint_violation_rate",
                "definition": "Fraction of transitions that violate declared abstract constraints.",
            },
            {
                "metric_id": "VF-MET-004",
                "name": "path_stability",
                "definition": "Degree to which packet paths remain consistent under controlled random seeds.",
            },
            {
                "metric_id": "VF-MET-005",
                "name": "delayed_effect_score",
                "definition": "Difference between immediate transition outcomes and later t2 or t3 outcomes.",
            },
            {
                "metric_id": "VF-MET-006",
                "name": "baseline_divergence",
                "definition": "Distance between Viruse Fabric model outputs and baseline outputs under predeclared toy metrics.",
            },
            {
                "metric_id": "VF-MET-007",
                "name": "symbolic_drift_rate",
                "definition": "Rate of unitless symbolic packet-state perturbation over toy steps.",
            },
            {
                "metric_id": "VF-MET-008",
                "name": "ledger_effect_size",
                "definition": "Difference between memory-ledger and no-memory model outputs.",
            },
        ]

    def _falsification_rules(self) -> List[Dict[str, str]]:
        return [
            {
                "rule_id": "VF-FALS-001",
                "name": "baseline_non_difference_rule",
                "rule": "If Viruse Fabric outputs do not differ from all relevant baselines under predeclared metrics, the corresponding hypothesis is not supported.",
            },
            {
                "rule_id": "VF-FALS-002",
                "name": "ledger_no_effect_rule",
                "rule": "If memory-ledger variants do not reduce violations or change stability compared with no-memory baselines, the ledger-stability claim is not supported.",
            },
            {
                "rule_id": "VF-FALS-003",
                "name": "causal_mass_no_delay_rule",
                "rule": "If causal-mass variants do not generate delayed-effect differences, the causal-mass delayed-effect claim is not supported.",
            },
            {
                "rule_id": "VF-FALS-004",
                "name": "three_time_no_projection_rule",
                "rule": "If t1/t2/t3 variants do not differ from single-time variants, the three-time-layer claim is not supported.",
            },
            {
                "rule_id": "VF-FALS-005",
                "name": "seed_instability_rule",
                "rule": "If observed effects collapse across controlled random seeds, the result is treated as unstable and not validated.",
            },
            {
                "rule_id": "VF-FALS-006",
                "name": "no_validation_without_execution_rule",
                "rule": "No theory validation is claimed until v9.2 engine execution, v9.3 baseline comparison, and v9.4 falsification audit are completed.",
            },
        ]

    def _safety_boundaries(self) -> List[Dict[str, str]]:
        return [
            {
                "boundary_id": "VF-SAFE-001",
                "boundary": "Safe abstract toy only.",
                "counter_requirement": "Real biological dataset import count remains zero.",
            },
            {
                "boundary_id": "VF-SAFE-002",
                "boundary": "No real pathogen simulation.",
                "counter_requirement": "Real pathogen simulation count remains zero.",
            },
            {
                "boundary_id": "VF-SAFE-003",
                "boundary": "No receptor parameters.",
                "counter_requirement": "Real receptor parameter count remains zero.",
            },
            {
                "boundary_id": "VF-SAFE-004",
                "boundary": "No operational host targeting.",
                "counter_requirement": "Operational host targeting count remains zero.",
            },
            {
                "boundary_id": "VF-SAFE-005",
                "boundary": "No wet-lab protocols.",
                "counter_requirement": "Wet-lab protocol count remains zero.",
            },
            {
                "boundary_id": "VF-SAFE-006",
                "boundary": "No actionable biosafety-risk instructions.",
                "counter_requirement": "Actionable biosafety-risk instruction count remains zero.",
            },
            {
                "boundary_id": "VF-SAFE-007",
                "boundary": "No real-world infectivity optimization.",
                "counter_requirement": "Real-world infectivity optimization count remains zero.",
            },
            {
                "boundary_id": "VF-SAFE-008",
                "boundary": "No immune evasion optimization.",
                "counter_requirement": "Immune evasion optimization count remains zero.",
            },
            {
                "boundary_id": "VF-SAFE-009",
                "boundary": "No real host range prediction.",
                "counter_requirement": "Real host range prediction count remains zero.",
            },
            {
                "boundary_id": "VF-SAFE-010",
                "boundary": "No validation, readiness, citation integration, or manuscript mutation in v9.0.",
                "counter_requirement": "Validation, readiness, citation, and manuscript mutation counters remain zero.",
            },
        ]

    def _roadmap(self) -> List[Dict[str, str]]:
        return [
            {
                "milestone": "v9.0",
                "name": "Viruse Fabric Abstract Simulation Reframing",
                "status": "current_reframing_only",
                "purpose": "Define theory as a formal, simulatable, falsifiable abstract toy model.",
            },
            {
                "milestone": "v9.1",
                "name": "Abstract Simulation Specification",
                "status": "planned",
                "purpose": "Specify exact graph generation, update rules, metrics, seeds, and output schema.",
            },
            {
                "milestone": "v9.2",
                "name": "Minimal Safe Toy Simulation Engine",
                "status": "planned",
                "purpose": "Implement the first non-operational abstract toy simulation engine.",
            },
            {
                "milestone": "v9.3",
                "name": "Baseline Comparison",
                "status": "planned",
                "purpose": "Compare Viruse Fabric variants against predeclared baselines.",
            },
            {
                "milestone": "v9.4",
                "name": "Results and Falsification Audit",
                "status": "planned",
                "purpose": "Report results and explicitly identify supported, unsupported, or inconclusive hypotheses.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        acceptance_payload = self._load_json(self.source_acceptance_json_path)
        acceptance_counters = acceptance_payload.get("counters", {})

        model_objects = self._model_objects()
        state_variables = self._state_variables()
        hypotheses = self._reframed_hypotheses()
        baselines = self._baseline_plan()
        metrics = self._metric_proposals()
        falsification_rules = self._falsification_rules()
        safety_boundaries = self._safety_boundaries()
        roadmap = self._roadmap()

        counters = {
            "V9 abstract simulation reframing artifact count": 1,
            "V9 theory reframing record count": 1,
            "V9 simulatable model object definition count": len(model_objects),
            "V9 state variable definition count": len(state_variables),
            "V9 reframed hypothesis count": len(hypotheses),
            "V9 baseline plan count": len(baselines),
            "V9 metric proposal count": len(metrics),
            "V9 falsification rule count": len(falsification_rules),
            "V9 safety boundary count": len(safety_boundaries),
            "V9 roadmap milestone count": len(roadmap),
            "V9 abstract simulation reframing completed count": 1,
            "V9 detailed simulation specification completed count": 0,
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
            "Toy citation batch 1 accepted source count": acceptance_counters.get("Toy citation batch 1 accepted source count"),
            "Toy citation batch 1 accepted methodological source pool count": acceptance_counters.get("Toy citation batch 1 accepted methodological source pool count"),
            "Toy citation batch 1 accepted not citation-ready source count": acceptance_counters.get("Toy citation batch 1 accepted not citation-ready source count"),
            "Toy citation batch 1 citation-ready source count": acceptance_counters.get("Toy citation batch 1 citation-ready source count"),
            "Toy citation batch 1 actual citation count": acceptance_counters.get("Toy citation batch 1 actual citation count"),
            "Toy citation batch 1 citation integration completion count": acceptance_counters.get("Toy citation batch 1 citation integration completion count"),
            "Toy citation batch 1 manuscript mutation count": acceptance_counters.get("Toy citation batch 1 manuscript mutation count"),
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
            "title": "Viruse Fabric Abstract Simulation Reframing",
            "plan_phrase": self.plan_phrase,
            "scope": "abstract-simulation-reframing-only",
            "source_acceptance_json": str(self.source_acceptance_json_path),
            "safe_abstract_toy_only": True,
            "formal_reframing_only": True,
            "simulatable_theory_reframed": True,
            "falsifiable_hypotheses_declared": True,
            "simulation_specification_deferred_to_v9_1": True,
            "simulation_engine_created": False,
            "simulation_run_performed": False,
            "baseline_comparison_performed": False,
            "results_reported": False,
            "falsification_audit_executed": False,
            "validation_claim_made": False,
            "readiness_approval_recorded": False,
            "manuscript_file_modified": False,
            "manuscript_mutation": False,
            "new_citation_added": False,
            "v8_line_frozen": True,
            "post_v8_pivot_to_simulation_backed_theory": True,
            "theory_reframing_statement": (
                "Viruse Fabric is reframed as a safe abstract toy model over graph-based symbolic pattern packets, "
                "local and global constraints, causal-mass scoring, memory-ledger path dependence, and t1/t2/t3 time-layered state. "
                "This v9.0 milestone defines a formal, simulatable, and falsifiable theory frame without creating a simulation engine "
                "and without executing any simulation."
            ),
            "model_objects": model_objects,
            "state_variables": state_variables,
            "reframed_hypotheses": hypotheses,
            "baseline_plan": baselines,
            "metric_proposals": metrics,
            "falsification_rules": falsification_rules,
            "safety_boundaries": safety_boundaries,
            "roadmap": roadmap,
            "non_validation_disclaimer": (
                "Abstract simulation reframing only. No simulation engine is created. No simulation run is performed. "
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
        if report["scope"] != "abstract-simulation-reframing-only":
            raise AssertionError("v9.0 must remain abstract-simulation-reframing-only.")

        if report["passed"] is not True:
            raise AssertionError("v9.0 must pass.")

        for field in [
            "safe_abstract_toy_only",
            "formal_reframing_only",
            "simulatable_theory_reframed",
            "falsifiable_hypotheses_declared",
            "simulation_specification_deferred_to_v9_1",
            "v8_line_frozen",
            "post_v8_pivot_to_simulation_backed_theory",
        ]:
            if report[field] is not True:
                raise AssertionError(f"Expected True for {field}")

        for field in [
            "simulation_engine_created",
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
            "V9 abstract simulation reframing artifact count": 1,
            "V9 theory reframing record count": 1,
            "V9 simulatable model object definition count": 8,
            "V9 state variable definition count": 12,
            "V9 reframed hypothesis count": 4,
            "V9 baseline plan count": 5,
            "V9 metric proposal count": 8,
            "V9 falsification rule count": 6,
            "V9 safety boundary count": 10,
            "V9 roadmap milestone count": 5,
            "V9 abstract simulation reframing completed count": 1,
            "V9 detailed simulation specification completed count": 0,
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
            "Toy citation batch 1 accepted source count": 7,
            "Toy citation batch 1 accepted methodological source pool count": 7,
            "Toy citation batch 1 accepted not citation-ready source count": 7,
            "Toy citation batch 1 citation-ready source count": 0,
            "Toy citation batch 1 actual citation count": 0,
            "Toy citation batch 1 citation integration completion count": 0,
            "Toy citation batch 1 manuscript mutation count": 0,
        }

        for name, expected in expected_counts.items():
            actual = counters.get(name)
            if actual != expected:
                raise AssertionError(f"Expected {expected} for {name}, got {actual}")

        must_be_zero = [
            "V9 detailed simulation specification completed count",
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
            "Abstract simulation reframing only",
            "No simulation engine is created",
            "No simulation run is performed",
            "No baseline comparison is executed",
            "No results are reported",
            "No falsification audit is executed",
            "No validation claim is made",
            "Viruse Fabric is reframed as a safe abstract toy model",
            "formal, simulatable, and falsifiable theory frame",
            "safe abstract toy model over graph-based symbolic pattern packets",
            "local and global constraints",
            "causal-mass scoring",
            "memory-ledger path dependence",
            "t1/t2/t3 time-layered state",
            "No manuscript file is modified",
            "No citation is added",
            "No real biological datasets",
            "no real pathogen models",
            "no receptor parameters",
            "no operational targeting",
        ]

        for phrase in required_phrases:
            if phrase not in combined_text:
                raise AssertionError(f"Missing required v9.0 phrase: {phrase}")

    def render_markdown(self, report: Dict[str, Any]) -> str:
        lines: List[str] = []

        lines.append("# Viruse Fabric Abstract Simulation Reframing")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is abstract-simulation-reframing-only.")
        lines.append("It reframes Viruse Fabric as a formal, simulatable, falsifiable safe abstract toy theory without creating a simulation engine, running simulations, executing baseline comparison, reporting results, validating the theory, modifying manuscript files, or adding citations.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")
        lines.append("## Theory Reframing Statement")
        lines.append("")
        lines.append(report["theory_reframing_statement"])
        lines.append("")
        lines.append("## Non-Validation Disclaimer")
        lines.append("")
        lines.append(report["non_validation_disclaimer"])
        lines.append("")

        lines.append("## Model Objects")
        lines.append("")
        for item in report["model_objects"]:
            lines.append(f"### {item['object_id']} - {item['name']}")
            lines.append("")
            lines.append(f"- Definition: {item['definition']}")
            lines.append(f"- Non-operational boundary: {item['non_operational_boundary']}")
            lines.append("")

        lines.append("## State Variables")
        lines.append("")
        for item in report["state_variables"]:
            lines.append(f"### {item['variable_id']} - {item['name']}")
            lines.append("")
            lines.append(f"- Type: {item['type']}")
            lines.append(f"- Definition: {item['definition']}")
            lines.append(f"- Unit: {item['unit']}")
            lines.append("")

        lines.append("## Reframed Hypotheses")
        lines.append("")
        for item in report["reframed_hypotheses"]:
            lines.append(f"### {item['hypothesis_id']} - {item['name']}")
            lines.append("")
            lines.append(f"- Hypothesis: {item['hypothesis']}")
            lines.append(f"- Falsification condition: {item['falsification_condition']}")
            lines.append("")

        lines.append("## Baseline Plan")
        lines.append("")
        for item in report["baseline_plan"]:
            lines.append(f"### {item['baseline_id']} - {item['name']}")
            lines.append("")
            lines.append(f"- Definition: {item['definition']}")
            lines.append("")

        lines.append("## Metric Proposals")
        lines.append("")
        for item in report["metric_proposals"]:
            lines.append(f"### {item['metric_id']} - {item['name']}")
            lines.append("")
            lines.append(f"- Definition: {item['definition']}")
            lines.append("")

        lines.append("## Falsification Rules")
        lines.append("")
        for item in report["falsification_rules"]:
            lines.append(f"### {item['rule_id']} - {item['name']}")
            lines.append("")
            lines.append(f"- Rule: {item['rule']}")
            lines.append("")

        lines.append("## Safety Boundaries")
        lines.append("")
        for item in report["safety_boundaries"]:
            lines.append(f"### {item['boundary_id']}")
            lines.append("")
            lines.append(f"- Boundary: {item['boundary']}")
            lines.append(f"- Counter requirement: {item['counter_requirement']}")
            lines.append("")

        lines.append("## Post-v8 Roadmap")
        lines.append("")
        for item in report["roadmap"]:
            lines.append(f"### {item['milestone']} - {item['name']}")
            lines.append("")
            lines.append(f"- Status: {item['status']}")
            lines.append(f"- Purpose: {item['purpose']}")
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
        lines.append("V9_0_VIRUSE_FABRIC_ABSTRACT_SIMULATION_REFRAMING_OK")
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


def build_viruse_fabric_abstract_simulation_reframing() -> Dict[str, Any]:
    return ViruseFabricAbstractSimulationReframingBuilder().run()


if __name__ == "__main__":
    result = build_viruse_fabric_abstract_simulation_reframing()
    counters = result["counters"]
    print("V9_0_VIRUSE_FABRIC_ABSTRACT_SIMULATION_REFRAMING_OK")
    print("VIRUSE_FABRIC_ABSTRACT_SIMULATION_REFRAMING_DIRECT_CHECK_OK")
    print(f"Model object definition count: {counters['V9 simulatable model object definition count']}")
    print(f"State variable definition count: {counters['V9 state variable definition count']}")
    print(f"Reframed hypothesis count: {counters['V9 reframed hypothesis count']}")
    print(f"Baseline plan count: {counters['V9 baseline plan count']}")
    print(f"Metric proposal count: {counters['V9 metric proposal count']}")
    print(f"Falsification rule count: {counters['V9 falsification rule count']}")
    print(f"Safety boundary count: {counters['V9 safety boundary count']}")
    print(f"Roadmap milestone count: {counters['V9 roadmap milestone count']}")
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
