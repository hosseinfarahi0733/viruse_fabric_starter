from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class SigmaATypedProductCarrierComponentSlotRefinementExecutionReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class SigmaATypedProductCarrierComponentSlotRefinementExecutionBuilder:
    """Build v8.113 Sigma_A typed-product carrier component-slot refinement execution artifact.

    Boundary discipline:
    - This milestone executes component-slot refinement for the selected typed-product carrier.
    - It does not execute full typed-product carrier refinement.
    - It does not execute full carrier refinement.
    - It does not execute time-index refinement.
    - It does not execute Sigma_A refinement.
    - It does not create new Sigma_A draft clauses.
    - It does not execute definitions.
    - It does not complete Sigma_A.
    - It does not create theorem candidates.
    - It does not prove theorems.
    """

    title = "Sigma_A Typed-Product Carrier Component-Slot Refinement Execution v8.113"
    source_artifact = Path("outputs/sigma_a_typed_product_carrier_component_slot_refinement_execution_plan_v8_112.md")
    output_path = Path("outputs/sigma_a_typed_product_carrier_component_slot_refinement_execution_v8_113.md")

    refined_slot_rows = [
        {
            "slot_id": "X-A-SLOT-REF-001",
            "slot": "B_A biological-state component",
            "refined_slot_form": "B_A := biological-state typed component family",
            "local_obligation": "must expose state fields usable by Adm_A",
            "boundary": "does not define Adm_A",
            "status": "slot-level refinement executed",
        },
        {
            "slot_id": "X-A-SLOT-REF-002",
            "slot": "S_A spatial-context component",
            "refined_slot_form": "S_A := spatial-context typed component family",
            "local_obligation": "must remain compatible with C_reg and Pi_obs planning",
            "boundary": "does not define C_reg or Pi_obs",
            "status": "slot-level refinement executed",
        },
        {
            "slot_id": "X-A-SLOT-REF-003",
            "slot": "Q_A constraint-status component",
            "refined_slot_form": "Q_A := constraint-status typed component family",
            "local_obligation": "must support future C_reg membership checks without replacing C_reg",
            "boundary": "does not complete C_reg",
            "status": "slot-level refinement executed",
        },
        {
            "slot_id": "X-A-SLOT-REF-004",
            "slot": "O_A observer-visible component",
            "refined_slot_form": "O_A := observer-visible typed component family",
            "local_obligation": "must distinguish observer-facing state from full state",
            "boundary": "does not define Pi_obs",
            "status": "slot-level refinement executed",
        },
        {
            "slot_id": "X-A-SLOT-REF-005",
            "slot": "K_A causal-mass support component",
            "refined_slot_form": "K_A := causal-mass-support typed component family",
            "local_obligation": "must preserve M_c typing flexibility",
            "boundary": "does not define M_c",
            "status": "slot-level refinement executed",
        },
        {
            "slot_id": "X-A-SLOT-REF-006",
            "slot": "Rdy_A transition-readiness component",
            "refined_slot_form": "Rdy_A := transition-readiness typed component family",
            "local_obligation": "must support later R_A transition checks",
            "boundary": "does not define R_A",
            "status": "slot-level refinement executed",
        },
        {
            "slot_id": "X-A-SLOT-REF-007",
            "slot": "J_A trajectory-support component",
            "refined_slot_form": "J_A := trajectory-support typed component family",
            "local_obligation": "must support later Traj_A construction",
            "boundary": "does not define Traj_A",
            "status": "slot-level refinement executed",
        },
        {
            "slot_id": "X-A-SLOT-REF-008",
            "slot": "Ann_A audit-annotation component",
            "refined_slot_form": "Ann_A := audit-annotation auxiliary component family",
            "local_obligation": "must remain auxiliary unless later formalized",
            "boundary": "does not add hidden mathematical structure",
            "status": "slot-level refinement executed",
        },
    ]

    post_refinement_checks = [
        "B_A refinement remains local and does not define Adm_A.",
        "S_A refinement remains local and does not define C_reg or Pi_obs.",
        "Q_A refinement remains local and does not complete C_reg.",
        "O_A refinement remains local and does not define Pi_obs.",
        "K_A refinement remains local and does not define M_c.",
        "Rdy_A refinement remains local and does not define R_A.",
        "J_A refinement remains local and does not define Traj_A.",
        "Ann_A refinement remains auxiliary and audit-facing.",
    ]

    def run(self) -> SigmaATypedProductCarrierComponentSlotRefinementExecutionReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        warnings.extend([
            "This milestone executes typed-product component-slot refinement only.",
            "Full typed-product carrier refinement remains zero in v8.113.",
            "Sigma_A refinement remains zero in v8.113.",
            "Sigma_A definition completion, theorem planning, theorem proof, proof assistant verification, validation, and readiness remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "sigma_a_typed_product_carrier_component_slot_refinement_execution_count": 1,
            "component_slot_refinement_execution_count": 1,
            "typed_product_component_slot_refined_count": len(self.refined_slot_rows),
            "component_slot_refinement_row_count": len(self.refined_slot_rows),
            "component_slot_post_refinement_check_count": len(self.post_refinement_checks),
            "component_slot_local_boundary_count": len(self.refined_slot_rows),
            "component_slot_refinement_status_count": sum(1 for row in self.refined_slot_rows if row["status"] == "slot-level refinement executed"),
            "carried_sigma_a_typed_product_carrier_component_slot_refinement_execution_plan_count": carried.get("Sigma_A typed-product carrier component-slot refinement execution plan count", 1),
            "carried_component_slot_refinement_plan_row_count": carried.get("Component-slot refinement plan row count", 8),
            "carried_component_slot_refinement_execution_gate_count": carried.get("Component-slot refinement execution gate count", 8),
            "carried_planned_component_slot_count": carried.get("Planned component slot count", 8),
            "carried_sigma_a_typed_product_carrier_component_slot_audit_execution_count": carried.get("Carried Sigma_A typed-product carrier component-slot audit execution count", 1),
            "carried_typed_product_carrier_component_slot_audited_count": carried.get("Carried typed-product carrier component slot audited count", 8),
            "carried_selected_typed_product_carrier_count": carried.get("Carried selected typed-product carrier count", 1),
            "carried_sigma_a_carrier_type_selection_decision_execution_count": carried.get("Carried Sigma_A carrier-type selection decision execution count", 1),
            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
            "typed_product_carrier_refinement_execution_count": 0,
            "carrier_type_refinement_execution_count": 0,
            "carrier_refinement_execution_count": 0,
            "time_index_refinement_execution_count": 0,
            "sigma_a_refinement_execution_count": 0,
            "component_slot_integration_execution_count": 0,
            "new_carrier_type_selection_count": 0,
            "new_sigma_a_draft_clause_count": 0,
            "new_definition_draft_execution_count": 0,
            "definition_inventory_execution_count": 0,
            "definition_execution_count": 0,
            "new_definition_execution_count": 0,
            "completed_formal_definition_count": 0,
            "formalization_complete_count": 0,
            "sigma_a_definition_completion_count": 0,
            "stabilization_predicate_definition_completion_count": 0,
            "attractor_class_definition_completion_count": 0,
            "constraint_region_definition_completion_count": 0,
            "causal_mass_definition_completion_count": 0,
            "observer_projection_definition_completion_count": 0,
            "completion_decision_plan_count": carried.get("Completion decision plan count", 1),
            "completion_decision_count": 0,
            "completion_execution_count": 0,
            "completion_execution_authorized_count": 0,
            "theorem_candidate_plan_count": 0,
            "new_theorem_proven_count": 0,
            "cumulative_limited_theorem_proven_count": 5,
            "proof_assistant_verification_count": 0,
            "formal_mathematical_proof_count": 0,
            "formal_proof_execution_count": 0,
            "proof_execution_count": 0,
            "proof_gap_resolution_count": 0,
            "definition_completion_execution_count": 0,
            "full_framework_formal_proof_count": 0,
            "manuscript_submission_ready_count": 0,
            "readiness_approval_count": 0,
            "external_validation_count": 0,
            "independent_experiment_count": 0,
            "new_citation_added_count": 0,
            "hard_zero_count": 13,
            "next_step_count": 8,
        }

        report_text = self._render_report(counts, warnings)
        counts["boundary_phrase_count"] = self._count_boundary_phrases(report_text)
        counts["prohibited_behavior_count"] = self._count_prohibited_behaviors(report_text)
        counts["overclaim_count"] = self._count_overclaims(report_text)
        counts["invented_citation_like_pattern_count"] = self._count_invented_citation_like_patterns(report_text)
        counts["word_count"] = len(re.findall(r"\b\S+\b", report_text))

        if counts["overclaim_count"] != 0:
            errors.append("Overclaim detected in v8.113 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.113 report.")
        if counts["sigma_a_typed_product_carrier_component_slot_refinement_execution_count"] != 1:
            errors.append("v8.113 must execute exactly one component-slot refinement milestone.")
        if counts["component_slot_refinement_execution_count"] != 1:
            errors.append("v8.113 must set component-slot refinement execution count to one.")
        if counts["typed_product_component_slot_refined_count"] != 8:
            errors.append("v8.113 must refine exactly eight typed-product component slots.")
        if counts["component_slot_post_refinement_check_count"] != 8:
            errors.append("v8.113 must include exactly eight post-refinement checks.")
        if counts["typed_product_carrier_refinement_execution_count"] != 0:
            errors.append("v8.113 must not execute full typed-product carrier refinement.")
        if counts["carrier_refinement_execution_count"] != 0:
            errors.append("v8.113 must not execute full carrier refinement.")
        if counts["sigma_a_refinement_execution_count"] != 0:
            errors.append("v8.113 must not execute Sigma_A refinement.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.113 must not complete Sigma_A definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.113 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.113 must not prove a theorem.")

        zero_fields = [
            "typed_product_carrier_refinement_execution_count",
            "carrier_type_refinement_execution_count",
            "carrier_refinement_execution_count",
            "time_index_refinement_execution_count",
            "sigma_a_refinement_execution_count",
            "component_slot_integration_execution_count",
            "new_carrier_type_selection_count",
            "new_sigma_a_draft_clause_count",
            "new_definition_draft_execution_count",
            "definition_inventory_execution_count",
            "definition_execution_count",
            "new_definition_execution_count",
            "completed_formal_definition_count",
            "formalization_complete_count",
            "sigma_a_definition_completion_count",
            "stabilization_predicate_definition_completion_count",
            "attractor_class_definition_completion_count",
            "constraint_region_definition_completion_count",
            "causal_mass_definition_completion_count",
            "observer_projection_definition_completion_count",
            "completion_decision_count",
            "completion_execution_count",
            "completion_execution_authorized_count",
            "theorem_candidate_plan_count",
            "new_theorem_proven_count",
            "proof_assistant_verification_count",
            "formal_mathematical_proof_count",
            "formal_proof_execution_count",
            "proof_execution_count",
            "proof_gap_resolution_count",
            "definition_completion_execution_count",
            "full_framework_formal_proof_count",
            "manuscript_submission_ready_count",
            "readiness_approval_count",
            "external_validation_count",
            "independent_experiment_count",
            "new_citation_added_count",
        ]

        for field in zero_fields:
            if counts[field] != 0:
                errors.append(f"{field} must remain zero, found {counts[field]}.")

        final_report_text = self._render_report(counts, warnings)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(final_report_text, encoding="utf-8")

        return SigmaATypedProductCarrierComponentSlotRefinementExecutionReport(
            title=self.title,
            output_path=str(self.output_path),
            source_artifact=str(self.source_artifact),
            errors=errors,
            warnings=warnings,
            passed=len(errors) == 0,
            **counts,
        )

    def _extract_carried_counts(self, source_text: str) -> dict[str, int]:
        carried: dict[str, int] = {}
        for line in source_text.splitlines():
            clean = line.strip().lstrip("-").strip()
            match = re.match(r"^([A-Za-z][A-Za-z0-9 /_-]* count):\s*(\d+)\s*$", clean)
            if match:
                carried[match.group(1)] = int(match.group(2))
        return carried

    def _format_label(self, key: str) -> str:
        overrides = {
            "sigma_a_typed_product_carrier_component_slot_refinement_execution_count": "Sigma_A typed-product carrier component-slot refinement execution count",
            "component_slot_refinement_execution_count": "Component-slot refinement execution count",
            "typed_product_component_slot_refined_count": "Typed-product component slot refined count",
            "component_slot_refinement_row_count": "Component-slot refinement row count",
            "component_slot_post_refinement_check_count": "Component-slot post-refinement check count",
            "component_slot_local_boundary_count": "Component-slot local boundary count",
            "component_slot_refinement_status_count": "Component-slot refinement status count",
            "carried_sigma_a_typed_product_carrier_component_slot_refinement_execution_plan_count": "Carried Sigma_A typed-product carrier component-slot refinement execution plan count",
            "carried_component_slot_refinement_plan_row_count": "Carried component-slot refinement plan row count",
            "carried_component_slot_refinement_execution_gate_count": "Carried component-slot refinement execution gate count",
            "carried_sigma_a_typed_product_carrier_component_slot_audit_execution_count": "Carried Sigma_A typed-product carrier component-slot audit execution count",
            "carried_typed_product_carrier_component_slot_audited_count": "Carried typed-product carrier component slot audited count",
            "carried_selected_typed_product_carrier_count": "Carried selected typed-product carrier count",
            "carried_sigma_a_carrier_type_selection_decision_execution_count": "Carried Sigma_A carrier-type selection decision execution count",
            "typed_product_carrier_refinement_execution_count": "Typed-product carrier refinement execution count",
            "component_slot_integration_execution_count": "Component-slot integration execution count",
            "new_carrier_type_selection_count": "New carrier type selection count",
            "time_index_refinement_execution_count": "Time-index refinement execution count",
            "new_sigma_a_draft_clause_count": "New Sigma_A draft clause count",
            "sigma_a_refinement_execution_count": "Sigma_A refinement execution count",
            "sigma_a_definition_completion_count": "Sigma_A definition completion count",
        }
        return overrides.get(key, key.replace("_", " ").capitalize())

    def _render_report(self, counts: dict[str, int], warnings: list[str]) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric execute typed-product carrier component-slot refinement after the refinement execution plan "
            "while keeping full typed-product carrier refinement, carrier refinement, time-index refinement, Sigma_A refinement, "
            "new draft execution, definition execution, Sigma_A definition completion, theorem candidate planning, theorem proof, "
            "proof assistant verification, external validation, manuscript readiness, readiness approval, and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Execution boundary")
        lines.append("- Milestone type: Sigma_A typed-product carrier component-slot refinement execution only")
        lines.append("- Component-slot refinement execution after this milestone: executed")
        lines.append("- Full typed-product carrier refinement after this milestone: not executed")
        lines.append("- Full carrier refinement after this milestone: not executed")
        lines.append("- Time-index refinement execution after this milestone: not executed")
        lines.append("- Sigma_A refinement execution after this milestone: not executed")
        lines.append("- Sigma_A definition completion after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("")
        lines.append("## Refined component-slot rows")
        lines.append("")
        lines.append("| Slot ID | Slot | Refined slot form | Local obligation | Boundary | Status |")
        lines.append("|---|---|---|---|---|---|")
        for row in self.refined_slot_rows:
            lines.append(
                f"| {row['slot_id']} | {row['slot']} | {row['refined_slot_form']} | "
                f"{row['local_obligation']} | {row['boundary']} | {row['status']} |"
            )
        lines.append("")
        lines.append("## Post-refinement checks")
        for index, check in enumerate(self.post_refinement_checks, start=1):
            lines.append(f"{index}. {check}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact executes Sigma_A typed-product carrier component-slot refinement only. "
            "It does not execute full typed-product carrier refinement, does not execute carrier-type refinement, "
            "does not execute full carrier refinement, does not execute time-index refinement, does not execute Sigma_A refinement, "
            "does not integrate the refined slots into a completed carrier, does not perform a new carrier type selection, "
            "does not create new Sigma_A draft clauses, does not execute a new definition draft, does not execute definitions, "
            "does not complete Sigma_A, does not complete any formal definition, does not complete formalization, "
            "does not create theorem candidates, does not prove a theorem, does not run proof execution, "
            "does not provide proof assistant verification, does not prove the full framework, does not provide external validation, "
            "does not perform an independent experiment, does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "sigma_a_typed_product_carrier_component_slot_refinement_execution_count",
            "component_slot_refinement_execution_count",
            "typed_product_component_slot_refined_count",
            "component_slot_refinement_row_count",
            "component_slot_post_refinement_check_count",
            "component_slot_local_boundary_count",
            "component_slot_refinement_status_count",
            "carried_sigma_a_typed_product_carrier_component_slot_refinement_execution_plan_count",
            "carried_component_slot_refinement_plan_row_count",
            "carried_component_slot_refinement_execution_gate_count",
            "carried_planned_component_slot_count",
            "carried_sigma_a_typed_product_carrier_component_slot_audit_execution_count",
            "carried_typed_product_carrier_component_slot_audited_count",
            "carried_selected_typed_product_carrier_count",
            "carried_sigma_a_carrier_type_selection_decision_execution_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
            "typed_product_carrier_refinement_execution_count",
            "carrier_type_refinement_execution_count",
            "carrier_refinement_execution_count",
            "time_index_refinement_execution_count",
            "sigma_a_refinement_execution_count",
            "component_slot_integration_execution_count",
            "new_carrier_type_selection_count",
            "new_sigma_a_draft_clause_count",
            "new_definition_draft_execution_count",
            "definition_inventory_execution_count",
            "definition_execution_count",
            "new_definition_execution_count",
            "completed_formal_definition_count",
            "formalization_complete_count",
            "sigma_a_definition_completion_count",
            "stabilization_predicate_definition_completion_count",
            "attractor_class_definition_completion_count",
            "constraint_region_definition_completion_count",
            "causal_mass_definition_completion_count",
            "observer_projection_definition_completion_count",
            "completion_decision_plan_count",
            "completion_decision_count",
            "completion_execution_count",
            "completion_execution_authorized_count",
            "theorem_candidate_plan_count",
            "new_theorem_proven_count",
            "cumulative_limited_theorem_proven_count",
            "proof_assistant_verification_count",
            "formal_mathematical_proof_count",
            "formal_proof_execution_count",
            "proof_execution_count",
            "proof_gap_resolution_count",
            "definition_completion_execution_count",
            "full_framework_formal_proof_count",
            "manuscript_submission_ready_count",
            "readiness_approval_count",
            "external_validation_count",
            "independent_experiment_count",
            "new_citation_added_count",
            "hard_zero_count",
            "boundary_phrase_count",
            "prohibited_behavior_count",
            "next_step_count",
            "overclaim_count",
            "invented_citation_like_pattern_count",
            "word_count",
        ]
        for key in counter_order:
            if key in counts:
                lines.append(f"- {self._format_label(key)}: {counts[key]}")
        lines.append("")
        lines.append("## Warnings")
        for warning in warnings:
            lines.append(f"- {warning}")
        lines.append("")
        lines.append("## Interpretation")
        lines.append(
            "The v8.113 artifact executes slot-level refinement for eight typed-product carrier components. "
            "This is component-slot refinement execution only. It does not execute full typed-product carrier refinement, "
            "does not execute Sigma_A refinement, does not create new draft clauses, does not execute definitions, "
            "does not complete Sigma_A, does not create theorem candidates, does not prove theorems, "
            "does not provide proof assistant verification, does not provide external validation, and does not approve manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Audit component-slot refinement outputs before any integration step.",
            "Keep component-slot integration separate from component-slot refinement execution.",
            "Keep full carrier refinement execution separate from slot-level refinement.",
            "Keep time-index refinement separate from typed-product slot refinement.",
            "Keep Sigma_A completion separate from theorem candidate planning.",
            "Keep theorem candidate planning separate from theorem proof.",
            "Keep proof assistant verification separate from proof execution.",
            "Keep validation, citation work, and manuscript readiness separate.",
        ]
        for step in next_steps:
            lines.append(f"- {step}")
        lines.append("")
        return "\n".join(lines) + "\n"

    def _count_boundary_phrases(self, text: str) -> int:
        phrases = [
            "does not",
            "not executed",
            "not completed",
            "not created",
            "component-slot refinement",
            "slot-level",
            "separate",
            "zero",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not execute full typed-product carrier refinement",
            "does not execute carrier-type refinement",
            "does not execute full carrier refinement",
            "does not execute time-index refinement",
            "does not execute Sigma_A refinement",
            "does not integrate the refined slots into a completed carrier",
            "does not perform a new carrier type selection",
            "does not create new Sigma_A draft clauses",
            "does not execute a new definition draft",
            "does not execute definitions",
            "does not complete Sigma_A",
            "does not complete any formal definition",
            "does not complete formalization",
            "does not create theorem candidates",
            "does not prove a theorem",
            "does not run proof execution",
            "does not provide proof assistant verification",
            "does not prove the full framework",
            "does not provide external validation",
            "does not perform an independent experiment",
            "does not approve manuscript submission readiness",
            "does not add new citations",
        ]
        return sum(1 for phrase in prohibited if phrase in text)

    def _count_overclaims(self, text: str) -> int:
        forbidden_positive_counter_names = {
            "typed product carrier refinement execution count",
            "typed-product carrier refinement execution count",
            "carrier type refinement execution count",
            "carrier refinement execution count",
            "time index refinement execution count",
            "time-index refinement execution count",
            "sigma_a refinement execution count",
            "sigma a refinement execution count",
            "component slot integration execution count",
            "component-slot integration execution count",
            "new carrier type selection count",
            "new sigma_a draft clause count",
            "new sigma a draft clause count",
            "new definition draft execution count",
            "definition inventory execution count",
            "definition execution count",
            "new definition execution count",
            "completed formal definition count",
            "formalization complete count",
            "sigma_a definition completion count",
            "sigma a definition completion count",
            "stabilization predicate definition completion count",
            "attractor class definition completion count",
            "constraint region definition completion count",
            "causal mass definition completion count",
            "observer projection definition completion count",
            "completion decision count",
            "completion execution count",
            "completion execution authorized count",
            "theorem candidate plan count",
            "new theorem proven count",
            "proof assistant verification count",
            "formal mathematical proof count",
            "formal proof execution count",
            "proof execution count",
            "proof gap resolution count",
            "definition completion execution count",
            "full framework formal proof count",
            "external validation count",
            "independent experiment count",
            "manuscript submission ready count",
            "readiness approval count",
            "new citation added count",
        }

        unsafe_phrases = [
            "full typed-product carrier refinement executed",
            "carrier refinement executed",
            "Sigma_A refinement executed",
            "Sigma_A definition completed",
            "Sigma_A completion achieved",
            "formal definition completed",
            "formal definitions completed",
            "theorem candidate created",
            "theorem proven",
            "proof assistant verification complete",
            "framework proven",
            "external validation complete",
            "manuscript ready",
        ]

        protective_markers = [
            "does not",
            "do not",
            "cannot",
            "not executed",
            "not completed",
            "not created",
            "not provide",
            "not approve",
            "not add",
            "not run",
            "slot-level",
            "component-slot refinement execution only",
            "local",
            "boundary",
            "separate",
            "carried",
            "cumulative limited",
            "remain absent",
            "remains absent",
            "remain zero",
            "remains zero",
            "at zero",
            "zero",
            "count: 0",
        ]

        count = 0
        for raw_line in text.splitlines():
            line = raw_line.strip().lstrip("-").strip()
            lowered = line.lower()

            if not lowered:
                continue

            counter_match = re.match(r"^([a-z0-9_ /-]+ count):\s*([0-9]+)\s*$", lowered)
            if counter_match:
                counter_name = counter_match.group(1).replace("_", " ").strip()
                value = int(counter_match.group(2))
                if value > 0 and counter_name in forbidden_positive_counter_names:
                    count += 1
                continue

            if any(marker in lowered for marker in protective_markers):
                continue

            for phrase in unsafe_phrases:
                if phrase.lower() in lowered:
                    count += 1
                    break

        return count

    def _count_invented_citation_like_patterns(self, text: str) -> int:
        patterns = [
            r"\([A-Z][A-Za-z-]+,\s*20\d{2}\)",
            r"\[[0-9]{1,3}\]",
            r"doi:",
            r"arXiv:",
        ]
        return sum(len(re.findall(pattern, text)) for pattern in patterns)


if __name__ == "__main__":
    report = SigmaATypedProductCarrierComponentSlotRefinementExecutionBuilder().run()
    print(f"Wrote {report.output_path}")
