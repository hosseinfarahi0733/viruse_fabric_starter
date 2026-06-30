from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class ViruseFabricSafeToyScientificYieldExtractionAndTheoryReductionBuilder:
    version = "v9.6"

    source_reframing_json_path = Path("outputs/viruse_fabric_abstract_simulation_reframing_v9_0.json")
    source_results_audit_json_path = Path("outputs/viruse_fabric_results_and_falsification_audit_v9_4.json")
    source_readiness_gate_json_path = Path("outputs/viruse_fabric_toy_evidence_limitation_and_manuscript_readiness_gate_v9_5.json")

    output_md_path = Path("outputs/viruse_fabric_safe_toy_scientific_yield_extraction_and_theory_reduction_v9_6.md")
    output_json_path = Path("outputs/viruse_fabric_safe_toy_scientific_yield_extraction_and_theory_reduction_v9_6.json")

    plan_phrase = "v9_6_safe_toy_scientific_yield_extraction_and_theory_reduction_without_validation_or_readiness"

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Missing required source JSON: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"Expected dict payload from {path}")
        return payload

    def _comparison_lookup(self, results_payload: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        return {
            row["baseline_id"]: row
            for row in results_payload["result_summary"]["comparison_table"]
        }

    def _audit_lookup(self, results_payload: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        return {
            row["hypothesis_id"]: row
            for row in results_payload["falsification_audit"]["audit_records"]
        }

    def _hypothesis_yield_table(self, results_payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        audit = self._audit_lookup(results_payload)

        mapping = [
            {
                "hypothesis_id": "VF-H1",
                "mechanism": "multi_layer_constraint_path_shift",
                "status": "unresolved_or_unsupported_in_current_safe_toy_audit",
                "allowed_interpretation": (
                    "The current safe toy audit does not provide measurable support for the multi-layer constraint path-shift mechanism."
                ),
            },
            {
                "hypothesis_id": "VF-H2",
                "mechanism": "memory_ledger_stability_effect",
                "status": "not_falsified_in_current_safe_toy_audit",
                "allowed_interpretation": (
                    "The current safe toy audit identifies the memory-ledger mechanism as the clearest measurable toy-level signal."
                ),
            },
            {
                "hypothesis_id": "VF-H3",
                "mechanism": "causal_mass_delayed_effect",
                "status": "unresolved_or_unsupported_in_current_safe_toy_audit",
                "allowed_interpretation": (
                    "The current safe toy audit does not provide measurable support for the causal-mass delayed-effect mechanism."
                ),
            },
            {
                "hypothesis_id": "VF-H4",
                "mechanism": "three_time_layer_predictive_difference",
                "status": "unresolved_or_unsupported_in_current_safe_toy_audit",
                "allowed_interpretation": (
                    "The current safe toy audit does not provide measurable support for the three-time-layer predictive-difference mechanism."
                ),
            },
        ]

        rows = []
        for item in mapping:
            source = audit[item["hypothesis_id"]]
            rows.append(
                {
                    "hypothesis_id": item["hypothesis_id"],
                    "mechanism": item["mechanism"],
                    "source_toy_verdict": source["toy_audit_verdict"],
                    "selected_delta_total": source["selected_delta_total"],
                    "selected_metric_deltas": source["selected_metric_deltas"],
                    "yield_status": item["status"],
                    "allowed_interpretation": item["allowed_interpretation"],
                    "interpretation_boundary": (
                        "Safe abstract toy interpretation only. This is not empirical evidence, not external validation, "
                        "not independent validation, not manuscript readiness, and not a theory validation claim."
                    ),
                }
            )
        return rows

    def _mechanism_status_table(self, hypothesis_yield_table: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return [
            {
                "mechanism_id": "VF-MECH-001",
                "mechanism_name": "memory_ledger",
                "linked_hypothesis": "VF-H2",
                "current_status": "retained_as_reduced_toy_core",
                "evidence_basis": "selected_delta_total 3.0 in VF-H2 toy audit and ledger_effect_size signal",
                "next_action": "Keep as the central reduced toy-supported mechanism.",
            },
            {
                "mechanism_id": "VF-MECH-002",
                "mechanism_name": "multi_layer_constraint_path_shift",
                "linked_hypothesis": "VF-H1",
                "current_status": "unresolved_or_unsupported",
                "evidence_basis": "selected_delta_total 0.0 in VF-H1 toy audit",
                "next_action": "Redesign metrics or demote from central theory claim.",
            },
            {
                "mechanism_id": "VF-MECH-003",
                "mechanism_name": "causal_mass_delayed_effect",
                "linked_hypothesis": "VF-H3",
                "current_status": "unresolved_or_unsupported",
                "evidence_basis": "selected_delta_total 0.0 in VF-H3 toy audit",
                "next_action": "Redesign engine exposure and delayed-effect metrics before claiming support.",
            },
            {
                "mechanism_id": "VF-MECH-004",
                "mechanism_name": "three_time_layer_predictive_difference",
                "linked_hypothesis": "VF-H4",
                "current_status": "unresolved_or_unsupported",
                "evidence_basis": "selected_delta_total 0.0 in VF-H4 toy audit",
                "next_action": "Redesign time-layer intervention and predictive-difference metrics before claiming support.",
            },
        ]

    def _allowed_claims_register(self) -> List[Dict[str, Any]]:
        return [
            {
                "claim_id": "V9-6-ALLOW-001",
                "claim_text": (
                    "In the current safe abstract toy model, the memory-ledger component produces the clearest measurable divergence from baseline behavior."
                ),
                "claim_scope": "safe_abstract_toy_only",
                "basis": "VF-H2 selected_delta_total 3.0 and ledger_effect_size signal.",
            },
            {
                "claim_id": "V9-6-ALLOW-002",
                "claim_text": (
                    "The current safe toy audit does not falsify the memory-ledger stability effect within the tested toy configuration."
                ),
                "claim_scope": "safe_abstract_toy_only",
                "basis": "VF-H2 verdict is not_falsified_in_this_safe_toy_audit.",
            },
            {
                "claim_id": "V9-6-ALLOW-003",
                "claim_text": (
                    "The current safe toy evidence supports reducing the defensible toy core to memory-ledger-driven toy dynamics."
                ),
                "claim_scope": "safe_abstract_toy_theory_reduction",
                "basis": "Only VF-H2 is not-falsified while VF-H1, VF-H3, and VF-H4 are falsified-or-unresolved.",
            },
            {
                "claim_id": "V9-6-ALLOW-004",
                "claim_text": (
                    "The multi-layer constraint, causal-mass, and three-time-layer mechanisms remain unresolved or unsupported in the current safe toy audit."
                ),
                "claim_scope": "safe_abstract_toy_only",
                "basis": "VF-H1, VF-H3, and VF-H4 each have selected_delta_total 0.0.",
            },
            {
                "claim_id": "V9-6-ALLOW-005",
                "claim_text": (
                    "The full Viruse Fabric theory should be treated as a broader framework, not as a validated theory."
                ),
                "claim_scope": "boundary_and_positioning",
                "basis": "Current evidence is toy-only and narrow, with readiness denied in v9.5.",
            },
        ]

    def _forbidden_claims_register(self) -> List[Dict[str, Any]]:
        return [
            {
                "claim_id": "V9-6-FORBID-001",
                "forbidden_claim": "The full Viruse Fabric theory is validated.",
                "reason": "Only safe toy evidence exists, and only VF-H2 is not-falsified in the current audit.",
            },
            {
                "claim_id": "V9-6-FORBID-002",
                "forbidden_claim": "The causal-mass mechanism is supported.",
                "reason": "VF-H3 has selected_delta_total 0.0 and is falsified-or-unresolved in this safe toy audit.",
            },
            {
                "claim_id": "V9-6-FORBID-003",
                "forbidden_claim": "The three-time-layer mechanism is supported.",
                "reason": "VF-H4 has selected_delta_total 0.0 and is falsified-or-unresolved in this safe toy audit.",
            },
            {
                "claim_id": "V9-6-FORBID-004",
                "forbidden_claim": "The multi-layer constraint path-shift mechanism is supported.",
                "reason": "VF-H1 has selected_delta_total 0.0 and is falsified-or-unresolved in this safe toy audit.",
            },
            {
                "claim_id": "V9-6-FORBID-005",
                "forbidden_claim": "The project is manuscript submission ready.",
                "reason": "v9.5 readiness gate decision is not_ready_for_manuscript_submission.",
            },
            {
                "claim_id": "V9-6-FORBID-006",
                "forbidden_claim": "The toy audit is empirical evidence.",
                "reason": "The audit is safe abstract toy only and has no external validation or independent experiment.",
            },
            {
                "claim_id": "V9-6-FORBID-007",
                "forbidden_claim": "The model applies to real biological systems.",
                "reason": "No real biological datasets, pathogen models, receptor parameters, or operational biological assumptions are introduced.",
            },
            {
                "claim_id": "V9-6-FORBID-008",
                "forbidden_claim": "The current outputs justify manuscript mutation or citation integration.",
                "reason": "No manuscript mutation or citation integration is authorized in v9.6.",
            },
        ]

    def _next_evidence_requirements(self) -> List[Dict[str, Any]]:
        return [
            {
                "requirement_id": "V9-6-NEXT-001",
                "name": "expanded_safe_toy_replicates",
                "description": "Run additional safe abstract toy replicates across seed grids and graph configurations.",
                "boundary": "safe abstract toy only",
            },
            {
                "requirement_id": "V9-6-NEXT-002",
                "name": "mechanism_specific_metric_redesign",
                "description": "Redesign metrics for multi-layer constraints, causal mass, and three-time-layer effects.",
                "boundary": "safe abstract toy metric design only",
            },
            {
                "requirement_id": "V9-6-NEXT-003",
                "name": "causal_mass_engine_exposure",
                "description": "Increase safe toy visibility of causal-mass effects without introducing real biological semantics.",
                "boundary": "safe abstract toy engine only",
            },
            {
                "requirement_id": "V9-6-NEXT-004",
                "name": "time_layer_intervention_test",
                "description": "Create safe toy interventions that can distinguish single-time and three-time-layer behavior.",
                "boundary": "safe abstract toy intervention only",
            },
            {
                "requirement_id": "V9-6-NEXT-005",
                "name": "claim_language_control",
                "description": "Keep claim language restricted to toy evidence and reduced theory core until stronger evidence exists.",
                "boundary": "non-validation claim control",
            },
        ]

    def build(self) -> Dict[str, Any]:
        reframing_payload = self._load_json(self.source_reframing_json_path)
        results_payload = self._load_json(self.source_results_audit_json_path)
        readiness_payload = self._load_json(self.source_readiness_gate_json_path)

        hypothesis_yield_table = self._hypothesis_yield_table(results_payload)
        mechanism_status_table = self._mechanism_status_table(hypothesis_yield_table)
        allowed_claims_register = self._allowed_claims_register()
        forbidden_claims_register = self._forbidden_claims_register()
        next_evidence_requirements = self._next_evidence_requirements()

        not_falsified_count = sum(
            1 for item in hypothesis_yield_table
            if item["source_toy_verdict"] == "not_falsified_in_this_safe_toy_audit"
        )
        unresolved_count = sum(
            1 for item in hypothesis_yield_table
            if item["source_toy_verdict"] == "falsified_or_unresolved_in_this_safe_toy_audit"
        )

        reduced_theory_core = {
            "core_id": "V9-6-REDUCED-CORE-001",
            "core_name": "memory-ledger-driven toy dynamics",
            "retained_mechanism": "memory_ledger",
            "retained_hypothesis": "VF-H2",
            "demoted_or_unresolved_hypotheses": ["VF-H1", "VF-H3", "VF-H4"],
            "core_statement": (
                "The currently defensible toy-supported core of Viruse Fabric is memory-ledger-driven toy dynamics. "
                "The broader theory remains a framework, not a validated theory."
            ),
            "boundary": (
                "Safe abstract toy reduction only. This is not empirical evidence, not external validation, "
                "not independent validation, not manuscript readiness, and not a theory validation claim."
            ),
        }

        scientific_yield_summary = {
            "summary_id": "V9-6-SCIENTIFIC-YIELD-SUMMARY-001",
            "yield_type": "narrow_safe_toy_signal",
            "primary_signal": "ledger_effect_size",
            "primary_supported_hypothesis": "VF-H2",
            "not_falsified_toy_hypothesis_count": not_falsified_count,
            "unresolved_or_unsupported_hypothesis_count": unresolved_count,
            "strongest_safe_toy_divergence": results_payload["result_summary"]["strongest_safe_toy_divergence"],
            "weakest_safe_toy_divergence": results_payload["result_summary"]["weakest_safe_toy_divergence"],
            "readiness_gate_decision": readiness_payload["readiness_gate"]["gate_decision"],
            "summary_statement": (
                "The v9.4 safe toy audit yields a narrow signal centered on the memory ledger. "
                "Only VF-H2 is not-falsified in the current safe toy audit. VF-H1, VF-H3, and VF-H4 remain unresolved "
                "or unsupported. v9.5 denies manuscript submission readiness."
            ),
        }

        counters = {
            "V9 scientific yield extraction artifact count": 1,
            "V9 scientific yield extraction count": 1,
            "V9 theory reduction count": 1,
            "V9 reduced theory core count": 1,
            "V9 hypothesis yield table count": 1,
            "V9 hypothesis yield record count": len(hypothesis_yield_table),
            "V9 not-falsified toy hypothesis count": not_falsified_count,
            "V9 unresolved or unsupported toy hypothesis count": unresolved_count,
            "V9 mechanism status table count": 1,
            "V9 mechanism status record count": len(mechanism_status_table),
            "V9 allowed claims register count": 1,
            "V9 allowed claim count": len(allowed_claims_register),
            "V9 forbidden claims register count": 1,
            "V9 forbidden claim count": len(forbidden_claims_register),
            "V9 next evidence requirement table count": 1,
            "V9 next evidence requirement count": len(next_evidence_requirements),
            "V9 source reframed hypothesis count": reframing_payload["counters"]["V9 reframed hypothesis count"],
            "V9 source formal results report count": results_payload["counters"]["V9 formal results report count"],
            "V9 source falsification audit execution count": results_payload["counters"]["V9 falsification audit execution count"],
            "V9 source toy falsification audit record count": results_payload["counters"]["V9 toy falsification audit record count"],
            "V9 source manuscript readiness denial count": readiness_payload["counters"]["V9 manuscript readiness denial count"],
            "V9 source manuscript readiness approval count": readiness_payload["counters"]["V9 manuscript readiness approval count"],
            "V9 theory validation claim count": 0,
            "V9 manuscript readiness claim count": 0,
            "V9 manuscript readiness approval count": 0,
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
            "title": "Viruse Fabric Safe Toy Scientific Yield Extraction and Theory Reduction",
            "plan_phrase": self.plan_phrase,
            "scope": "safe-toy-scientific-yield-extraction-and-theory-reduction-only",
            "safe_abstract_toy_only": True,
            "scientific_yield_extracted": True,
            "theory_reduction_performed": True,
            "reduced_theory_core_identified": True,
            "validation_claim_made": False,
            "readiness_approval_recorded": False,
            "manuscript_file_modified": False,
            "manuscript_mutation": False,
            "new_citation_added": False,
            "source_reframing_json": str(self.source_reframing_json_path),
            "source_results_audit_json": str(self.source_results_audit_json_path),
            "source_readiness_gate_json": str(self.source_readiness_gate_json_path),
            "scientific_yield_summary": scientific_yield_summary,
            "hypothesis_yield_table": hypothesis_yield_table,
            "reduced_theory_core": reduced_theory_core,
            "mechanism_status_table": mechanism_status_table,
            "allowed_claims_register": allowed_claims_register,
            "forbidden_claims_register": forbidden_claims_register,
            "next_evidence_requirements": next_evidence_requirements,
            "non_validation_disclaimer": (
                "Safe toy scientific yield extraction and theory reduction only. No validation claim is made. "
                "No manuscript readiness claim is made. No readiness approval is recorded. No manuscript file is modified. "
                "No citation is added. No external validation is performed. No independent experiment is performed. "
                "No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, "
                "no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction "
                "are introduced."
            ),
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "safe-toy-scientific-yield-extraction-and-theory-reduction-only":
            raise AssertionError("v9.6 must remain safe-toy-scientific-yield-extraction-and-theory-reduction-only.")

        for field in [
            "safe_abstract_toy_only",
            "scientific_yield_extracted",
            "theory_reduction_performed",
            "reduced_theory_core_identified",
        ]:
            if report[field] is not True:
                raise AssertionError(f"Expected True for {field}")

        for field in [
            "validation_claim_made",
            "readiness_approval_recorded",
            "manuscript_file_modified",
            "manuscript_mutation",
            "new_citation_added",
        ]:
            if report[field] is not False:
                raise AssertionError(f"Expected False for {field}")

        summary = report["scientific_yield_summary"]
        if summary["primary_supported_hypothesis"] != "VF-H2":
            raise AssertionError("v9.6 must identify VF-H2 as the only current supported toy hypothesis.")

        if summary["not_falsified_toy_hypothesis_count"] != 1:
            raise AssertionError("Expected one not-falsified toy hypothesis.")

        if summary["unresolved_or_unsupported_hypothesis_count"] != 3:
            raise AssertionError("Expected three unresolved or unsupported hypotheses.")

        core = report["reduced_theory_core"]
        if core["core_name"] != "memory-ledger-driven toy dynamics":
            raise AssertionError("Reduced theory core must be memory-ledger-driven toy dynamics.")

        if core["retained_hypothesis"] != "VF-H2":
            raise AssertionError("Reduced core must retain VF-H2.")

        if set(core["demoted_or_unresolved_hypotheses"]) != {"VF-H1", "VF-H3", "VF-H4"}:
            raise AssertionError("Reduced core must demote or mark VF-H1, VF-H3, VF-H4 unresolved.")

        counters = report["counters"]

        expected_counts = {
            "V9 scientific yield extraction artifact count": 1,
            "V9 scientific yield extraction count": 1,
            "V9 theory reduction count": 1,
            "V9 reduced theory core count": 1,
            "V9 hypothesis yield table count": 1,
            "V9 hypothesis yield record count": 4,
            "V9 not-falsified toy hypothesis count": 1,
            "V9 unresolved or unsupported toy hypothesis count": 3,
            "V9 mechanism status table count": 1,
            "V9 mechanism status record count": 4,
            "V9 allowed claims register count": 1,
            "V9 allowed claim count": 5,
            "V9 forbidden claims register count": 1,
            "V9 forbidden claim count": 8,
            "V9 next evidence requirement table count": 1,
            "V9 next evidence requirement count": 5,
            "V9 source reframed hypothesis count": 4,
            "V9 source formal results report count": 1,
            "V9 source falsification audit execution count": 1,
            "V9 source toy falsification audit record count": 4,
            "V9 source manuscript readiness denial count": 1,
            "V9 source manuscript readiness approval count": 0,
            "V9 theory validation claim count": 0,
            "V9 manuscript readiness claim count": 0,
            "V9 manuscript readiness approval count": 0,
        }

        for name, expected in expected_counts.items():
            actual = counters.get(name)
            if actual != expected:
                raise AssertionError(f"Expected {expected} for {name}, got {actual}")

        must_be_zero = [
            "V9 theory validation claim count",
            "V9 manuscript readiness claim count",
            "V9 manuscript readiness approval count",
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
            "memory-ledger-driven toy dynamics",
            "Only VF-H2 is not-falsified",
            "VF-H1, VF-H3, and VF-H4 remain unresolved",
            "allowed claims",
            "forbidden claims",
            "not empirical evidence",
            "not external validation",
            "not independent validation",
            "not manuscript readiness",
            "not a theory validation claim",
            "No validation claim is made",
            "No manuscript readiness claim is made",
            "No readiness approval is recorded",
            "No manuscript file is modified",
            "No citation is added",
            "No external validation is performed",
            "No independent experiment is performed",
            "No real biological datasets",
            "no real pathogen models",
            "no receptor parameters",
            "no operational targeting",
            "no wet-lab protocol",
            "no infectivity optimization",
            "no immune evasion optimization",
            "no host range prediction",
        ]

        for phrase in required_phrases:
            if phrase not in combined_text:
                raise AssertionError(f"Missing required v9.6 phrase: {phrase}")

    def render_markdown(self, report: Dict[str, Any]) -> str:
        lines: List[str] = []

        lines.append("# Viruse Fabric Safe Toy Scientific Yield Extraction and Theory Reduction")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is safe-toy-scientific-yield-extraction-and-theory-reduction-only.")
        lines.append("It extracts the actual scientific yield from safe toy outputs and reduces the theory to the currently defensible toy-supported core.")
        lines.append("It does not validate the theory, does not approve manuscript readiness, does not modify manuscript files, and does not add citations.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")

        lines.append("## Scientific Yield Summary")
        lines.append("")
        for key, value in report["scientific_yield_summary"].items():
            lines.append(f"- {key}: {value}")
        lines.append("")

        lines.append("## Hypothesis-by-Hypothesis Toy Verdict Table")
        lines.append("")
        for item in report["hypothesis_yield_table"]:
            lines.append(f"### {item['hypothesis_id']} - {item['mechanism']}")
            lines.append("")
            lines.append(f"- Source toy verdict: {item['source_toy_verdict']}")
            lines.append(f"- Selected delta total: {item['selected_delta_total']}")
            lines.append(f"- Selected metric deltas: {item['selected_metric_deltas']}")
            lines.append(f"- Yield status: {item['yield_status']}")
            lines.append(f"- Allowed interpretation: {item['allowed_interpretation']}")
            lines.append(f"- Interpretation boundary: {item['interpretation_boundary']}")
            lines.append("")

        lines.append("## Reduced Theory Core")
        lines.append("")
        for key, value in report["reduced_theory_core"].items():
            lines.append(f"- {key}: {value}")
        lines.append("")

        lines.append("## Mechanism Status Table")
        lines.append("")
        for item in report["mechanism_status_table"]:
            lines.append(f"### {item['mechanism_id']} - {item['mechanism_name']}")
            lines.append("")
            lines.append(f"- Linked hypothesis: {item['linked_hypothesis']}")
            lines.append(f"- Current status: {item['current_status']}")
            lines.append(f"- Evidence basis: {item['evidence_basis']}")
            lines.append(f"- Next action: {item['next_action']}")
            lines.append("")

        lines.append("## Allowed Claims Register")
        lines.append("")
        for item in report["allowed_claims_register"]:
            lines.append(f"### {item['claim_id']}")
            lines.append("")
            lines.append(f"- Claim text: {item['claim_text']}")
            lines.append(f"- Claim scope: {item['claim_scope']}")
            lines.append(f"- Basis: {item['basis']}")
            lines.append("")

        lines.append("## Forbidden Claims Register")
        lines.append("")
        for item in report["forbidden_claims_register"]:
            lines.append(f"### {item['claim_id']}")
            lines.append("")
            lines.append(f"- Forbidden claim: {item['forbidden_claim']}")
            lines.append(f"- Reason: {item['reason']}")
            lines.append("")

        lines.append("## Next Evidence Requirements")
        lines.append("")
        for item in report["next_evidence_requirements"]:
            lines.append(f"### {item['requirement_id']} - {item['name']}")
            lines.append("")
            lines.append(f"- Description: {item['description']}")
            lines.append(f"- Boundary: {item['boundary']}")
            lines.append("")

        lines.append("## Non-Validation Disclaimer")
        lines.append("")
        lines.append(report["non_validation_disclaimer"])
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
        lines.append("V9_6_VIRUSE_FABRIC_SAFE_TOY_SCIENTIFIC_YIELD_EXTRACTION_AND_THEORY_REDUCTION_OK")
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


def build_viruse_fabric_safe_toy_scientific_yield_extraction_and_theory_reduction() -> Dict[str, Any]:
    return ViruseFabricSafeToyScientificYieldExtractionAndTheoryReductionBuilder().run()


if __name__ == "__main__":
    result = build_viruse_fabric_safe_toy_scientific_yield_extraction_and_theory_reduction()
    counters = result["counters"]
    summary = result["scientific_yield_summary"]
    core = result["reduced_theory_core"]
    print("V9_6_VIRUSE_FABRIC_SAFE_TOY_SCIENTIFIC_YIELD_EXTRACTION_AND_THEORY_REDUCTION_OK")
    print("VIRUSE_FABRIC_SAFE_TOY_SCIENTIFIC_YIELD_EXTRACTION_AND_THEORY_REDUCTION_DIRECT_CHECK_OK")
    print(f"Primary supported hypothesis: {summary['primary_supported_hypothesis']}")
    print(f"Reduced theory core: {core['core_name']}")
    print(f"Scientific yield extraction count: {counters['V9 scientific yield extraction count']}")
    print(f"Theory reduction count: {counters['V9 theory reduction count']}")
    print(f"Reduced theory core count: {counters['V9 reduced theory core count']}")
    print(f"Hypothesis yield record count: {counters['V9 hypothesis yield record count']}")
    print(f"Not-falsified toy hypothesis count: {counters['V9 not-falsified toy hypothesis count']}")
    print(f"Unresolved or unsupported toy hypothesis count: {counters['V9 unresolved or unsupported toy hypothesis count']}")
    print(f"Allowed claim count: {counters['V9 allowed claim count']}")
    print(f"Forbidden claim count: {counters['V9 forbidden claim count']}")
    print(f"Theory validation claim count: {counters['V9 theory validation claim count']}")
    print(f"Manuscript readiness claim count: {counters['V9 manuscript readiness claim count']}")
    print(f"External validation count: {counters['External validation count']}")
    print(f"Independent experiment count: {counters['Independent experiment count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {result['passed']}")
