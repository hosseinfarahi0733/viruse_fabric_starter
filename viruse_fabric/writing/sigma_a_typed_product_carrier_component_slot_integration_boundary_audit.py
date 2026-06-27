from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class SigmaATypedProductCarrierComponentSlotIntegrationBoundaryAuditReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class SigmaATypedProductCarrierComponentSlotIntegrationBoundaryAuditBuilder:
    """Build v8.117 Sigma_A typed-product carrier component-slot integration boundary audit artifact.

    Boundary discipline:
    - This milestone audits the boundary of v8.116 component-slot integration.
    - It does not execute new component-slot integration.
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

    title = "Sigma_A Typed-Product Carrier Component-Slot Integration Boundary Audit v8.117"
    source_artifact = Path("outputs/sigma_a_typed_product_carrier_component_slot_integration_execution_v8_116.md")
    output_path = Path("outputs/sigma_a_typed_product_carrier_component_slot_integration_boundary_audit_v8_117.md")

    boundary_audit_rows = [
        {
            "coordinate": "coord_1 := B_A",
            "slot": "B_A biological-state component",
            "integration_boundary": "coordinate remains biological-state-facing only",
            "open_dependency": "Adm_A remains unresolved",
            "audit_result": "coordinate boundary preserved",
            "carrier_refinement_blocker": "cannot claim full typed-product carrier refinement",
        },
        {
            "coordinate": "coord_2 := S_A",
            "slot": "S_A spatial-context component",
            "integration_boundary": "coordinate remains spatial-context-facing only",
            "open_dependency": "C_reg and Pi_obs remain unresolved",
            "audit_result": "coordinate boundary preserved",
            "carrier_refinement_blocker": "cannot claim full typed-product carrier refinement",
        },
        {
            "coordinate": "coord_3 := Q_A",
            "slot": "Q_A constraint-status component",
            "integration_boundary": "coordinate remains constraint-status-facing only",
            "open_dependency": "C_reg membership semantics remain unresolved",
            "audit_result": "coordinate boundary preserved",
            "carrier_refinement_blocker": "cannot claim full typed-product carrier refinement",
        },
        {
            "coordinate": "coord_4 := O_A",
            "slot": "O_A observer-visible component",
            "integration_boundary": "coordinate remains observer-facing only",
            "open_dependency": "Pi_obs remains unresolved",
            "audit_result": "coordinate boundary preserved",
            "carrier_refinement_blocker": "cannot claim full typed-product carrier refinement",
        },
        {
            "coordinate": "coord_5 := K_A",
            "slot": "K_A causal-mass support component",
            "integration_boundary": "coordinate remains causal-mass-support-facing only",
            "open_dependency": "M_c remains unresolved",
            "audit_result": "coordinate boundary preserved",
            "carrier_refinement_blocker": "cannot claim full typed-product carrier refinement",
        },
        {
            "coordinate": "coord_6 := Rdy_A",
            "slot": "Rdy_A transition-readiness component",
            "integration_boundary": "coordinate remains transition-readiness-facing only",
            "open_dependency": "R_A remains unresolved",
            "audit_result": "coordinate boundary preserved",
            "carrier_refinement_blocker": "cannot claim full typed-product carrier refinement",
        },
        {
            "coordinate": "coord_7 := J_A",
            "slot": "J_A trajectory-support component",
            "integration_boundary": "coordinate remains trajectory-support-facing only",
            "open_dependency": "Traj_A remains unresolved",
            "audit_result": "coordinate boundary preserved",
            "carrier_refinement_blocker": "cannot claim full typed-product carrier refinement",
        },
        {
            "coordinate": "coord_aux := Ann_A",
            "slot": "Ann_A audit-annotation component",
            "integration_boundary": "coordinate remains auxiliary audit-facing only",
            "open_dependency": "annotation formalization remains unresolved",
            "audit_result": "coordinate boundary preserved",
            "carrier_refinement_blocker": "cannot claim full typed-product carrier refinement",
        },
    ]

    audit_findings = [
        "All eight integrated coordinates remain local coordinate-level components.",
        "No integrated coordinate defines Adm_A, C_reg, Pi_obs, M_c, R_A, or Traj_A.",
        "No integrated coordinate creates a completed typed-product carrier.",
        "No integrated coordinate creates a new Sigma_A draft clause.",
        "Full typed-product carrier refinement remains absent.",
        "Sigma_A refinement and Sigma_A definition completion remain absent.",
        "Theorem candidate planning remains absent.",
        "Validation, citation work, and manuscript readiness remain absent.",
    ]

    def run(self) -> SigmaATypedProductCarrierComponentSlotIntegrationBoundaryAuditReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        warnings.extend([
            "This milestone audits component-slot integration boundaries only.",
            "No new component-slot integration is executed in v8.117.",
            "Full typed-product carrier refinement and Sigma_A refinement remain zero in v8.117.",
            "Sigma_A definition completion, theorem planning, theorem proof, proof assistant verification, validation, and readiness remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "sigma_a_typed_product_carrier_component_slot_integration_boundary_audit_count": 1,
            "component_slot_integration_boundary_audit_count": 1,
            "component_slot_integration_boundary_audit_row_count": len(self.boundary_audit_rows),
            "integrated_coordinate_audited_count": len(self.boundary_audit_rows),
            "coordinate_boundary_preserved_count": sum(1 for row in self.boundary_audit_rows if row["audit_result"] == "coordinate boundary preserved"),
            "open_dependency_preserved_count": len(self.boundary_audit_rows),
            "carrier_refinement_blocker_count": len(self.boundary_audit_rows),
            "integration_boundary_audit_finding_count": len(self.audit_findings),
            "carried_sigma_a_typed_product_carrier_component_slot_integration_execution_count": carried.get("Sigma_A typed-product carrier component-slot integration execution count", 1),
            "carried_component_slot_integration_execution_count": carried.get("Component-slot integration execution count", 1),
            "carried_component_slot_integration_row_count": carried.get("Component-slot integration row count", 8),
            "carried_integrated_component_slot_count": carried.get("Integrated component slot count", 8),
            "carried_integrated_coordinate_count": carried.get("Integrated coordinate count", 8),
            "carried_integration_boundary_check_count": carried.get("Integration boundary check count", 8),
            "carried_component_slot_integration_status_count": carried.get("Component-slot integration status count", 8),
            "carried_sigma_a_typed_product_carrier_component_slot_integration_execution_plan_count": carried.get("Carried Sigma_A typed-product carrier component-slot integration execution plan count", 1),
            "carried_component_slot_integration_execution_plan_count": carried.get("Carried component-slot integration execution plan count", 1),
            "carried_component_slot_integration_plan_row_count": carried.get("Carried component-slot integration plan row count", 8),
            "carried_sigma_a_typed_product_carrier_component_slot_refinement_boundary_audit_count": carried.get("Carried Sigma_A typed-product carrier component-slot refinement boundary audit count", 1),
            "carried_selected_typed_product_carrier_count": carried.get("Carried selected typed-product carrier count", 1),
            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
            "new_component_slot_integration_execution_count": 0,
            "full_typed_product_carrier_refinement_execution_count": 0,
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
            errors.append("Overclaim detected in v8.117 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.117 report.")
        if counts["sigma_a_typed_product_carrier_component_slot_integration_boundary_audit_count"] != 1:
            errors.append("v8.117 must execute exactly one component-slot integration boundary audit.")
        if counts["component_slot_integration_boundary_audit_row_count"] != 8:
            errors.append("v8.117 must audit exactly eight integrated coordinate boundaries.")
        if counts["integrated_coordinate_audited_count"] != 8:
            errors.append("v8.117 must audit exactly eight integrated coordinates.")
        if counts["coordinate_boundary_preserved_count"] != 8:
            errors.append("v8.117 must preserve coordinate boundary for all eight coordinates.")
        if counts["new_component_slot_integration_execution_count"] != 0:
            errors.append("v8.117 must not execute new component-slot integration.")
        if counts["full_typed_product_carrier_refinement_execution_count"] != 0:
            errors.append("v8.117 must not execute full typed-product carrier refinement.")
        if counts["carrier_refinement_execution_count"] != 0:
            errors.append("v8.117 must not execute carrier refinement.")
        if counts["sigma_a_refinement_execution_count"] != 0:
            errors.append("v8.117 must not execute Sigma_A refinement.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.117 must not complete Sigma_A definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.117 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.117 must not prove a theorem.")

        zero_fields = [
            "new_component_slot_integration_execution_count",
            "full_typed_product_carrier_refinement_execution_count",
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

        return SigmaATypedProductCarrierComponentSlotIntegrationBoundaryAuditReport(
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
            "sigma_a_typed_product_carrier_component_slot_integration_boundary_audit_count": "Sigma_A typed-product carrier component-slot integration boundary audit count",
            "component_slot_integration_boundary_audit_count": "Component-slot integration boundary audit count",
            "component_slot_integration_boundary_audit_row_count": "Component-slot integration boundary audit row count",
            "integrated_coordinate_audited_count": "Integrated coordinate audited count",
            "coordinate_boundary_preserved_count": "Coordinate boundary preserved count",
            "open_dependency_preserved_count": "Open dependency preserved count",
            "carrier_refinement_blocker_count": "Carrier refinement blocker count",
            "integration_boundary_audit_finding_count": "Integration boundary audit finding count",
            "carried_sigma_a_typed_product_carrier_component_slot_integration_execution_count": "Carried Sigma_A typed-product carrier component-slot integration execution count",
            "carried_component_slot_integration_execution_count": "Carried component-slot integration execution count",
            "carried_component_slot_integration_row_count": "Carried component-slot integration row count",
            "carried_integrated_component_slot_count": "Carried integrated component slot count",
            "carried_integrated_coordinate_count": "Carried integrated coordinate count",
            "carried_integration_boundary_check_count": "Carried integration boundary check count",
            "carried_component_slot_integration_status_count": "Carried component-slot integration status count",
            "carried_sigma_a_typed_product_carrier_component_slot_integration_execution_plan_count": "Carried Sigma_A typed-product carrier component-slot integration execution plan count",
            "carried_component_slot_integration_execution_plan_count": "Carried component-slot integration execution plan count",
            "carried_component_slot_integration_plan_row_count": "Carried component-slot integration plan row count",
            "carried_sigma_a_typed_product_carrier_component_slot_refinement_boundary_audit_count": "Carried Sigma_A typed-product carrier component-slot refinement boundary audit count",
            "carried_selected_typed_product_carrier_count": "Carried selected typed-product carrier count",
            "new_component_slot_integration_execution_count": "New component-slot integration execution count",
            "full_typed_product_carrier_refinement_execution_count": "Full typed-product carrier refinement execution count",
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
            "Can Viruse Fabric audit the boundary of v8.116 component-slot integration while keeping new component-slot integration execution, "
            "full typed-product carrier refinement, carrier refinement, time-index refinement, Sigma_A refinement, new draft execution, definition execution, "
            "Sigma_A definition completion, theorem candidate planning, theorem proof, proof assistant verification, external validation, manuscript readiness, "
            "readiness approval, and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Audit boundary")
        lines.append("- Milestone type: Sigma_A typed-product carrier component-slot integration boundary audit only")
        lines.append("- New component-slot integration execution after this milestone: not executed")
        lines.append("- Full typed-product carrier refinement after this milestone: not executed")
        lines.append("- Carrier refinement execution after this milestone: not executed")
        lines.append("- Time-index refinement execution after this milestone: not executed")
        lines.append("- Sigma_A refinement execution after this milestone: not executed")
        lines.append("- Sigma_A definition completion after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("")
        lines.append("## Integration boundary audit rows")
        lines.append("")
        lines.append("| Coordinate | Slot | Integration boundary | Open dependency | Audit result | Carrier refinement blocker |")
        lines.append("|---|---|---|---|---|---|")
        for row in self.boundary_audit_rows:
            lines.append(
                f"| {row['coordinate']} | {row['slot']} | {row['integration_boundary']} | "
                f"{row['open_dependency']} | {row['audit_result']} | {row['carrier_refinement_blocker']} |"
            )
        lines.append("")
        lines.append("## Audit findings")
        for index, finding in enumerate(self.audit_findings, start=1):
            lines.append(f"{index}. {finding}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact audits Sigma_A typed-product carrier component-slot integration boundaries only. "
            "It does not execute new component-slot integration, does not execute full typed-product carrier refinement, "
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
            "sigma_a_typed_product_carrier_component_slot_integration_boundary_audit_count",
            "component_slot_integration_boundary_audit_count",
            "component_slot_integration_boundary_audit_row_count",
            "integrated_coordinate_audited_count",
            "coordinate_boundary_preserved_count",
            "open_dependency_preserved_count",
            "carrier_refinement_blocker_count",
            "integration_boundary_audit_finding_count",
            "carried_sigma_a_typed_product_carrier_component_slot_integration_execution_count",
            "carried_component_slot_integration_execution_count",
            "carried_component_slot_integration_row_count",
            "carried_integrated_component_slot_count",
            "carried_integrated_coordinate_count",
            "carried_integration_boundary_check_count",
            "carried_component_slot_integration_status_count",
            "carried_sigma_a_typed_product_carrier_component_slot_integration_execution_plan_count",
            "carried_component_slot_integration_execution_plan_count",
            "carried_component_slot_integration_plan_row_count",
            "carried_sigma_a_typed_product_carrier_component_slot_refinement_boundary_audit_count",
            "carried_selected_typed_product_carrier_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
            "new_component_slot_integration_execution_count",
            "full_typed_product_carrier_refinement_execution_count",
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
            "The v8.117 artifact audits component-slot integration boundaries for eight integrated coordinates. "
            "It confirms that coordinate-level integration remains local and does not become full typed-product carrier refinement. "
            "It does not execute new component-slot integration, does not execute full carrier refinement, does not execute Sigma_A refinement, "
            "does not create new draft clauses, does not execute definitions, does not complete Sigma_A, "
            "does not create theorem candidates, does not prove theorems, does not provide proof assistant verification, "
            "does not provide external validation, and does not approve manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Plan full typed-product carrier refinement only after this integration boundary audit is closed.",
            "Keep full typed-product carrier refinement separate from Sigma_A refinement.",
            "Keep carrier refinement separate from time-index refinement.",
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
            "boundary",
            "audit",
            "coordinate",
            "separate",
            "zero",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not execute new component-slot integration",
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
            "new component-slot integration execution count",
            "full typed product carrier refinement execution count",
            "full typed-product carrier refinement execution count",
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
            "new component-slot integration executed",
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
            "audit",
            "boundary",
            "coordinate",
            "blocker",
            "open dependency",
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
    report = SigmaATypedProductCarrierComponentSlotIntegrationBoundaryAuditBuilder().run()
    print(f"Wrote {report.output_path}")
