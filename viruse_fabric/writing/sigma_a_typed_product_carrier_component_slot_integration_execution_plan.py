from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class SigmaATypedProductCarrierComponentSlotIntegrationExecutionPlanReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class SigmaATypedProductCarrierComponentSlotIntegrationExecutionPlanBuilder:
    """Build v8.115 Sigma_A typed-product carrier component-slot integration execution plan.

    Boundary discipline:
    - This milestone plans component-slot integration execution.
    - It does not execute component-slot integration.
    - It does not execute full typed-product carrier refinement.
    - It does not execute carrier refinement.
    - It does not execute time-index refinement.
    - It does not execute Sigma_A refinement.
    - It does not create new Sigma_A draft clauses.
    - It does not execute definitions.
    - It does not complete Sigma_A.
    - It does not create theorem candidates.
    - It does not prove theorems.
    """

    title = "Sigma_A Typed-Product Carrier Component-Slot Integration Execution Plan v8.115"
    source_artifact = Path("outputs/sigma_a_typed_product_carrier_component_slot_refinement_boundary_audit_v8_114.md")
    output_path = Path("outputs/sigma_a_typed_product_carrier_component_slot_integration_execution_plan_v8_115.md")

    integration_plan_rows = [
        {
            "plan_id": "X-A-INT-PLAN-001",
            "slot": "B_A biological-state component",
            "planned_integration_role": "candidate first typed-product coordinate",
            "required_precondition": "Adm_A domain relation must remain separately unresolved",
            "blocked_overreach": "do not define Adm_A or complete Sigma_A",
        },
        {
            "plan_id": "X-A-INT-PLAN-002",
            "slot": "S_A spatial-context component",
            "planned_integration_role": "candidate second typed-product coordinate",
            "required_precondition": "C_reg and Pi_obs compatibility must remain separately unresolved",
            "blocked_overreach": "do not define C_reg or Pi_obs",
        },
        {
            "plan_id": "X-A-INT-PLAN-003",
            "slot": "Q_A constraint-status component",
            "planned_integration_role": "candidate third typed-product coordinate",
            "required_precondition": "C_reg membership semantics must remain separately unresolved",
            "blocked_overreach": "do not complete C_reg",
        },
        {
            "plan_id": "X-A-INT-PLAN-004",
            "slot": "O_A observer-visible component",
            "planned_integration_role": "candidate fourth typed-product coordinate",
            "required_precondition": "Pi_obs mapping relation must remain separately unresolved",
            "blocked_overreach": "do not define Pi_obs",
        },
        {
            "plan_id": "X-A-INT-PLAN-005",
            "slot": "K_A causal-mass support component",
            "planned_integration_role": "candidate fifth typed-product coordinate",
            "required_precondition": "M_c typing must remain separately unresolved",
            "blocked_overreach": "do not define M_c",
        },
        {
            "plan_id": "X-A-INT-PLAN-006",
            "slot": "Rdy_A transition-readiness component",
            "planned_integration_role": "candidate sixth typed-product coordinate",
            "required_precondition": "R_A typing must remain separately unresolved",
            "blocked_overreach": "do not define R_A",
        },
        {
            "plan_id": "X-A-INT-PLAN-007",
            "slot": "J_A trajectory-support component",
            "planned_integration_role": "candidate seventh typed-product coordinate",
            "required_precondition": "Traj_A construction must remain separately unresolved",
            "blocked_overreach": "do not define Traj_A",
        },
        {
            "plan_id": "X-A-INT-PLAN-008",
            "slot": "Ann_A audit-annotation component",
            "planned_integration_role": "candidate auxiliary audit coordinate",
            "required_precondition": "annotation must remain auxiliary unless later formalized",
            "blocked_overreach": "do not convert annotation into hidden mathematical structure",
        },
    ]

    integration_gate_rows = [
        "Each refined slot must enter the integration plan as a coordinate candidate only.",
        "No coordinate may define Adm_A, C_reg, Pi_obs, M_c, R_A, or Traj_A.",
        "Component-slot integration execution must remain a separate future milestone.",
        "Full typed-product carrier refinement must remain separate from component-slot integration.",
        "Time-index refinement must remain separate from component-slot integration.",
        "Sigma_A refinement must remain separate from integration planning.",
        "Definition execution and Sigma_A completion must remain separate milestones.",
        "Theorem planning, proof, validation, citations, and manuscript readiness must remain absent.",
    ]

    def run(self) -> SigmaATypedProductCarrierComponentSlotIntegrationExecutionPlanReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        warnings.extend([
            "This milestone plans component-slot integration execution only.",
            "Component-slot integration execution remains zero in v8.115.",
            "Full typed-product carrier refinement and Sigma_A refinement remain zero in v8.115.",
            "Sigma_A definition completion, theorem planning, theorem proof, proof assistant verification, validation, and readiness remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "sigma_a_typed_product_carrier_component_slot_integration_execution_plan_count": 1,
            "component_slot_integration_execution_plan_count": 1,
            "component_slot_integration_plan_row_count": len(self.integration_plan_rows),
            "component_slot_integration_gate_count": len(self.integration_gate_rows),
            "planned_integration_coordinate_count": len(self.integration_plan_rows),
            "planned_integration_precondition_count": len(self.integration_plan_rows),
            "planned_integration_blocked_overreach_count": len(self.integration_plan_rows),
            "carried_sigma_a_typed_product_carrier_component_slot_refinement_boundary_audit_count": carried.get("Sigma_A typed-product carrier component-slot refinement boundary audit count", 1),
            "carried_component_slot_refinement_boundary_audit_row_count": carried.get("Component-slot refinement boundary audit row count", 8),
            "carried_refined_component_slot_audited_count": carried.get("Refined component slot audited count", 8),
            "carried_local_boundary_preserved_count": carried.get("Local boundary preserved count", 8),
            "carried_open_dependency_preserved_count": carried.get("Open dependency preserved count", 8),
            "carried_integration_blocker_count": carried.get("Integration blocker count", 8),
            "carried_sigma_a_typed_product_carrier_component_slot_refinement_execution_count": carried.get("Carried Sigma_A typed-product carrier component-slot refinement execution count", 1),
            "carried_component_slot_refinement_execution_count": carried.get("Carried component-slot refinement execution count", 1),
            "carried_typed_product_component_slot_refined_count": carried.get("Carried typed-product component slot refined count", 8),
            "carried_selected_typed_product_carrier_count": carried.get("Carried selected typed-product carrier count", 1),
            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
            "component_slot_integration_execution_count": 0,
            "typed_product_carrier_refinement_execution_count": 0,
            "carrier_type_refinement_execution_count": 0,
            "carrier_refinement_execution_count": 0,
            "time_index_refinement_execution_count": 0,
            "sigma_a_refinement_execution_count": 0,
            "new_component_slot_refinement_execution_count": 0,
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
            errors.append("Overclaim detected in v8.115 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.115 report.")
        if counts["sigma_a_typed_product_carrier_component_slot_integration_execution_plan_count"] != 1:
            errors.append("v8.115 must produce exactly one integration execution plan.")
        if counts["component_slot_integration_execution_plan_count"] != 1:
            errors.append("v8.115 must set integration execution plan count to one.")
        if counts["component_slot_integration_plan_row_count"] != 8:
            errors.append("v8.115 must plan exactly eight component-slot integration rows.")
        if counts["component_slot_integration_gate_count"] != 8:
            errors.append("v8.115 must include exactly eight integration gates.")
        if counts["component_slot_integration_execution_count"] != 0:
            errors.append("v8.115 must not execute component-slot integration.")
        if counts["typed_product_carrier_refinement_execution_count"] != 0:
            errors.append("v8.115 must not execute full typed-product carrier refinement.")
        if counts["carrier_refinement_execution_count"] != 0:
            errors.append("v8.115 must not execute carrier refinement.")
        if counts["sigma_a_refinement_execution_count"] != 0:
            errors.append("v8.115 must not execute Sigma_A refinement.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.115 must not complete Sigma_A definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.115 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.115 must not prove a theorem.")

        zero_fields = [
            "component_slot_integration_execution_count",
            "typed_product_carrier_refinement_execution_count",
            "carrier_type_refinement_execution_count",
            "carrier_refinement_execution_count",
            "time_index_refinement_execution_count",
            "sigma_a_refinement_execution_count",
            "new_component_slot_refinement_execution_count",
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

        return SigmaATypedProductCarrierComponentSlotIntegrationExecutionPlanReport(
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
            "sigma_a_typed_product_carrier_component_slot_integration_execution_plan_count": "Sigma_A typed-product carrier component-slot integration execution plan count",
            "component_slot_integration_execution_plan_count": "Component-slot integration execution plan count",
            "component_slot_integration_plan_row_count": "Component-slot integration plan row count",
            "component_slot_integration_gate_count": "Component-slot integration gate count",
            "planned_integration_coordinate_count": "Planned integration coordinate count",
            "planned_integration_precondition_count": "Planned integration precondition count",
            "planned_integration_blocked_overreach_count": "Planned integration blocked-overreach count",
            "carried_sigma_a_typed_product_carrier_component_slot_refinement_boundary_audit_count": "Carried Sigma_A typed-product carrier component-slot refinement boundary audit count",
            "carried_component_slot_refinement_boundary_audit_row_count": "Carried component-slot refinement boundary audit row count",
            "carried_refined_component_slot_audited_count": "Carried refined component slot audited count",
            "carried_local_boundary_preserved_count": "Carried local boundary preserved count",
            "carried_open_dependency_preserved_count": "Carried open dependency preserved count",
            "carried_integration_blocker_count": "Carried integration blocker count",
            "carried_sigma_a_typed_product_carrier_component_slot_refinement_execution_count": "Carried Sigma_A typed-product carrier component-slot refinement execution count",
            "carried_component_slot_refinement_execution_count": "Carried component-slot refinement execution count",
            "carried_typed_product_component_slot_refined_count": "Carried typed-product component slot refined count",
            "carried_selected_typed_product_carrier_count": "Carried selected typed-product carrier count",
            "component_slot_integration_execution_count": "Component-slot integration execution count",
            "typed_product_carrier_refinement_execution_count": "Typed-product carrier refinement execution count",
            "time_index_refinement_execution_count": "Time-index refinement execution count",
            "new_component_slot_refinement_execution_count": "New component-slot refinement execution count",
            "new_carrier_type_selection_count": "New carrier type selection count",
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
            "Can Viruse Fabric plan component-slot integration execution after the v8.114 boundary audit "
            "while keeping component-slot integration execution, full typed-product carrier refinement, carrier refinement, "
            "time-index refinement, Sigma_A refinement, new draft execution, definition execution, Sigma_A definition completion, "
            "theorem candidate planning, theorem proof, proof assistant verification, external validation, manuscript readiness, "
            "readiness approval, and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Planning boundary")
        lines.append("- Milestone type: Sigma_A typed-product carrier component-slot integration execution plan only")
        lines.append("- Component-slot integration execution after this milestone: not executed")
        lines.append("- Full typed-product carrier refinement after this milestone: not executed")
        lines.append("- Carrier refinement execution after this milestone: not executed")
        lines.append("- Time-index refinement execution after this milestone: not executed")
        lines.append("- Sigma_A refinement execution after this milestone: not executed")
        lines.append("- Sigma_A definition completion after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("")
        lines.append("## Component-slot integration plan rows")
        lines.append("")
        lines.append("| Plan ID | Slot | Planned integration role | Required precondition | Blocked overreach |")
        lines.append("|---|---|---|---|---|")
        for row in self.integration_plan_rows:
            lines.append(
                f"| {row['plan_id']} | {row['slot']} | {row['planned_integration_role']} | "
                f"{row['required_precondition']} | {row['blocked_overreach']} |"
            )
        lines.append("")
        lines.append("## Integration execution gates")
        for index, gate in enumerate(self.integration_gate_rows, start=1):
            lines.append(f"{index}. {gate}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact plans Sigma_A typed-product carrier component-slot integration execution only. "
            "It does not execute component-slot integration, does not execute full typed-product carrier refinement, "
            "does not execute carrier-type refinement, does not execute full carrier refinement, does not execute time-index refinement, "
            "does not execute Sigma_A refinement, does not execute new component-slot refinement, does not perform a new carrier type selection, "
            "does not create new Sigma_A draft clauses, does not execute a new definition draft, does not execute definitions, "
            "does not complete Sigma_A, does not complete any formal definition, does not complete formalization, "
            "does not create theorem candidates, does not prove a theorem, does not run proof execution, "
            "does not provide proof assistant verification, does not prove the full framework, does not provide external validation, "
            "does not perform an independent experiment, does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "sigma_a_typed_product_carrier_component_slot_integration_execution_plan_count",
            "component_slot_integration_execution_plan_count",
            "component_slot_integration_plan_row_count",
            "component_slot_integration_gate_count",
            "planned_integration_coordinate_count",
            "planned_integration_precondition_count",
            "planned_integration_blocked_overreach_count",
            "carried_sigma_a_typed_product_carrier_component_slot_refinement_boundary_audit_count",
            "carried_component_slot_refinement_boundary_audit_row_count",
            "carried_refined_component_slot_audited_count",
            "carried_local_boundary_preserved_count",
            "carried_open_dependency_preserved_count",
            "carried_integration_blocker_count",
            "carried_sigma_a_typed_product_carrier_component_slot_refinement_execution_count",
            "carried_component_slot_refinement_execution_count",
            "carried_typed_product_component_slot_refined_count",
            "carried_selected_typed_product_carrier_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
            "component_slot_integration_execution_count",
            "typed_product_carrier_refinement_execution_count",
            "carrier_type_refinement_execution_count",
            "carrier_refinement_execution_count",
            "time_index_refinement_execution_count",
            "sigma_a_refinement_execution_count",
            "new_component_slot_refinement_execution_count",
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
            "The v8.115 artifact plans integration execution for eight refined typed-product component slots. "
            "This is planning only. It does not execute component-slot integration, does not execute full typed-product carrier refinement, "
            "does not execute Sigma_A refinement, does not create new draft clauses, does not execute definitions, "
            "does not complete Sigma_A, does not create theorem candidates, does not prove theorems, "
            "does not provide proof assistant verification, does not provide external validation, and does not approve manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Execute component-slot integration only after this plan is closed.",
            "Keep component-slot integration execution separate from full typed-product carrier refinement.",
            "Keep full carrier refinement separate from time-index refinement.",
            "Keep C_reg, Pi_obs, M_c, R_A, and Traj_A refinements separate.",
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
            "plan",
            "planning",
            "gate",
            "separate",
            "zero",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not execute component-slot integration",
            "does not execute full typed-product carrier refinement",
            "does not execute carrier-type refinement",
            "does not execute full carrier refinement",
            "does not execute time-index refinement",
            "does not execute Sigma_A refinement",
            "does not execute new component-slot refinement",
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
            "component slot integration execution count",
            "component-slot integration execution count",
            "typed product carrier refinement execution count",
            "typed-product carrier refinement execution count",
            "carrier type refinement execution count",
            "carrier refinement execution count",
            "time index refinement execution count",
            "time-index refinement execution count",
            "sigma_a refinement execution count",
            "sigma a refinement execution count",
            "new component-slot refinement execution count",
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
            "component-slot integration executed",
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
            "plan",
            "planned",
            "planning",
            "gate",
            "precondition",
            "blocked overreach",
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
    report = SigmaATypedProductCarrierComponentSlotIntegrationExecutionPlanBuilder().run()
    print(f"Wrote {report.output_path}")
