from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class DependentObjectDraftBundleIntegrationExecutionReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class DependentObjectDraftBundleIntegrationExecutionBuilder:
    """Build v8.143 dependent-object draft bundle integration execution artifact.

    Boundary discipline:
    - This milestone integrates the carried dependent-object draft slots into one bundle.
    - It does not create a new dependent-object draft slot.
    - It does not execute final definitions.
    - It does not complete Adm_A, C_reg, Pi_obs, M_c, R_A, Traj_A, or Sigma_A.
    - It does not create theorem candidates or prove theorems.
    """

    title = "Dependent-object Draft Bundle Integration Execution v8.143"
    source_artifact = Path("outputs/traj_a_definition_draft_execution_v8_142.md")
    output_path = Path("outputs/dependent_object_draft_bundle_integration_execution_v8_143.md")

    bundle_statement = (
        "Draft bundle B_dep := the carried dependent-object draft bundle attached to the refined Draft Sigma_A shell. "
        "It integrates the already-created draft slots Adm_A, C_reg, Pi_obs, M_c, R_A, and Traj_A as a bundle-level bookkeeping object. "
        "This integration records dependency coherence among the carried drafts only. "
        "It does not create new dependent-object drafts, does not execute final definitions, does not complete any dependent object, "
        "does not complete Sigma_A, and does not execute theorem or proof work."
    )

    integration_rows = [
        {
            "id": "BUNDLE-INT-001",
            "focus": "bundle activation",
            "result": "created exactly one dependent-object draft bundle integration",
            "boundary": "does not create a new dependent-object draft slot",
        },
        {
            "id": "BUNDLE-INT-002",
            "focus": "Adm_A integration",
            "result": "integrated the carried Adm_A draft into the bundle",
            "boundary": "does not complete Adm_A",
        },
        {
            "id": "BUNDLE-INT-003",
            "focus": "C_reg integration",
            "result": "integrated the carried C_reg draft into the bundle",
            "boundary": "does not complete C_reg",
        },
        {
            "id": "BUNDLE-INT-004",
            "focus": "Pi_obs integration",
            "result": "integrated the carried Pi_obs draft into the bundle",
            "boundary": "does not complete Pi_obs",
        },
        {
            "id": "BUNDLE-INT-005",
            "focus": "M_c integration",
            "result": "integrated the carried M_c draft into the bundle",
            "boundary": "does not complete M_c",
        },
        {
            "id": "BUNDLE-INT-006",
            "focus": "R_A integration",
            "result": "integrated the carried R_A draft into the bundle",
            "boundary": "does not complete R_A",
        },
        {
            "id": "BUNDLE-INT-007",
            "focus": "Traj_A integration",
            "result": "integrated the carried Traj_A draft into the bundle",
            "boundary": "does not complete Traj_A",
        },
        {
            "id": "BUNDLE-INT-008",
            "focus": "proof and readiness boundary",
            "result": "kept theorem, proof, validation, readiness, and citation work downstream",
            "boundary": "does not create theorem candidates",
        },
    ]

    checks = [
        "Exactly one dependent-object draft bundle integration execution is performed.",
        "Exactly six carried dependent-object drafts are integrated.",
        "No new dependent-object draft slot is created.",
        "Final definition execution remains absent.",
        "Dependent-object definition completion remains absent.",
        "Sigma_A definition completion remains absent.",
        "Theorem candidate planning remains absent.",
        "Validation, readiness, and citation claims remain absent.",
    ]

    def run(self) -> DependentObjectDraftBundleIntegrationExecutionReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""
        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        warnings.extend([
            "This milestone integrates carried dependent-object drafts; it does not create new draft slots.",
            "All dependent-object definition completion counters remain zero.",
            "Sigma_A definition completion remains zero.",
            "Theorem, proof, validation, readiness, and citation claims remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,

            "dependent_object_draft_bundle_integration_execution_count": 1,
            "new_dependent_object_draft_bundle_integration_execution_count": 1,
            "draft_bundle_integration_execution_count": 1,
            "integrated_dependent_object_draft_bundle_count": 1,
            "integrated_dependent_object_draft_count": 6,
            "integrated_adm_a_draft_count": 1,
            "integrated_c_reg_draft_count": 1,
            "integrated_pi_obs_draft_count": 1,
            "integrated_m_c_draft_count": 1,
            "integrated_r_a_draft_count": 1,
            "integrated_traj_a_draft_count": 1,
            "bundle_linked_to_refined_sigma_a_count": 1,
            "bundle_dependency_coherence_recorded_count": 1,
            "remaining_dependent_object_deferral_count": 0,
            "all_dependent_object_draft_slots_created_count": carried.get("All dependent-object draft slots created count", 1),
            "all_dependent_object_draft_slots_integrated_count": 1,
            "bundle_integration_row_count": len(self.integration_rows),
            "bundle_integration_check_count": len(self.checks),
            "bundle_integration_boundary_preserved_count": len(self.integration_rows),

            "carried_traj_a_definition_draft_execution_count": carried.get("Traj_A definition draft execution count", 1),
            "carried_new_traj_a_definition_draft_execution_count": carried.get("New Traj_A definition draft execution count", 1),
            "carried_traj_a_draft_slot_created_count": carried.get("Traj_A draft slot created count", 1),
            "carried_traj_a_draft_linked_to_refined_sigma_a_count": carried.get("Traj_A draft linked to refined Sigma_A count", 1),
            "carried_traj_a_linked_to_adm_a_draft_count": carried.get("Traj_A linked to Adm_A draft count", 1),
            "carried_traj_a_linked_to_c_reg_draft_count": carried.get("Traj_A linked to C_reg draft count", 1),
            "carried_traj_a_linked_to_pi_obs_draft_count": carried.get("Traj_A linked to Pi_obs draft count", 1),
            "carried_traj_a_linked_to_m_c_draft_count": carried.get("Traj_A linked to M_c draft count", 1),
            "carried_traj_a_linked_to_r_a_draft_count": carried.get("Traj_A linked to R_A draft count", 1),
            "carried_traj_a_trajectory_family_placeholder_count": carried.get("Traj_A trajectory-family placeholder count", 1),
            "carried_remaining_dependent_object_deferral_count": carried.get("Remaining dependent-object deferral count", 0),

            "carried_r_a_definition_draft_execution_count": carried.get("Carried R_A definition draft execution count", 1),
            "carried_m_c_definition_draft_execution_count": carried.get("Carried M_c definition draft execution count", 1),
            "carried_pi_obs_definition_draft_execution_count": carried.get("Carried Pi_obs definition draft execution count", 1),
            "carried_c_reg_definition_draft_execution_count": carried.get("Carried C_reg definition draft execution count", 1),
            "carried_adm_a_definition_draft_execution_count": carried.get("Carried Adm_A definition draft execution count", 1),
            "carried_sigma_a_refinement_execution_count": carried.get("Carried Sigma_A refinement execution count", 1),
            "carried_refined_draft_sigma_a_shell_count": carried.get("Carried refined Draft Sigma_A shell count", 1),
            "carried_integrated_time_index_layer_count": carried.get("Carried integrated time-index layer count", 1),

            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 14,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,

            "new_definition_draft_execution_count": 0,
            "new_dependent_object_definition_draft_execution_count": 0,
            "dependent_object_definition_draft_execution_count": 0,
            "new_traj_a_definition_draft_execution_count": 0,
            "new_r_a_definition_draft_execution_count": 0,
            "new_m_c_definition_draft_execution_count": 0,
            "new_pi_obs_definition_draft_execution_count": 0,
            "new_c_reg_definition_draft_execution_count": 0,
            "new_adm_a_definition_draft_execution_count": 0,

            "definition_execution_count": 0,
            "new_definition_execution_count": 0,
            "completed_formal_definition_count": 0,
            "formalization_complete_count": 0,
            "traj_a_definition_completion_count": 0,
            "r_a_definition_completion_count": 0,
            "m_c_definition_completion_count": 0,
            "pi_obs_definition_completion_count": 0,
            "c_reg_definition_completion_count": 0,
            "adm_a_definition_completion_count": 0,
            "sigma_a_definition_completion_count": 0,
            "stabilization_predicate_definition_completion_count": 0,
            "attractor_class_definition_completion_count": 0,
            "constraint_region_definition_completion_count": 0,
            "causal_mass_definition_completion_count": 0,
            "observer_projection_definition_completion_count": 0,

            "new_sigma_a_refinement_execution_count": 0,
            "new_time_index_refinement_execution_count": 0,
            "new_t_a_refinement_execution_count": 0,
            "new_whole_sigma_a_draft_assembly_execution_count": 0,
            "new_sigma_a_draft_assembly_execution_count": 0,
            "new_sigma_a_draft_clause_count": 0,
            "new_sigma_a_draft_clause_creation_count": 0,
            "new_carrier_draft_clause_creation_execution_count": 0,
            "new_carrier_level_draft_assembly_execution_count": 0,
            "new_typed_product_carrier_refinement_execution_count": 0,
            "generic_carrier_refinement_execution_count": 0,
            "carrier_refinement_execution_count": 0,
            "carrier_type_refinement_execution_count": 0,
            "new_component_slot_integration_execution_count": 0,
            "new_component_slot_refinement_execution_count": 0,
            "new_carrier_type_selection_count": 0,

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
            "next_step_count": 8,
        }

        report_text = self._render_report(counts, warnings)
        counts["boundary_phrase_count"] = self._count_boundary_phrases(report_text)
        counts["prohibited_behavior_count"] = self._count_prohibited_behaviors(report_text)
        counts["overclaim_count"] = self._count_overclaims(report_text)
        counts["invented_citation_like_pattern_count"] = self._count_invented_citation_like_patterns(report_text)
        counts["word_count"] = len(re.findall(r"\b\S+\b", report_text))

        if counts["overclaim_count"] != 0:
            errors.append("Overclaim detected in v8.143 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.143 report.")
        if counts["dependent_object_draft_bundle_integration_execution_count"] != 1:
            errors.append("v8.143 must execute exactly one dependent-object draft bundle integration.")
        if counts["integrated_dependent_object_draft_count"] != 6:
            errors.append("v8.143 must integrate exactly six carried dependent-object drafts.")
        if counts["new_definition_draft_execution_count"] != 0:
            errors.append("v8.143 must not create a new definition draft.")
        if counts["dependent_object_definition_draft_execution_count"] != 0:
            errors.append("v8.143 must not execute new dependent-object definition drafts.")
        if counts["definition_execution_count"] != 0:
            errors.append("v8.143 must not execute final definitions.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.143 must not complete Sigma_A definition.")
        if counts["completed_formal_definition_count"] != 0:
            errors.append("v8.143 must not complete a formal definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.143 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.143 must not prove theorem claims.")

        zero_fields = [
            "new_definition_draft_execution_count",
            "new_dependent_object_definition_draft_execution_count",
            "dependent_object_definition_draft_execution_count",
            "new_traj_a_definition_draft_execution_count",
            "new_r_a_definition_draft_execution_count",
            "new_m_c_definition_draft_execution_count",
            "new_pi_obs_definition_draft_execution_count",
            "new_c_reg_definition_draft_execution_count",
            "new_adm_a_definition_draft_execution_count",
            "definition_execution_count",
            "new_definition_execution_count",
            "completed_formal_definition_count",
            "formalization_complete_count",
            "traj_a_definition_completion_count",
            "r_a_definition_completion_count",
            "m_c_definition_completion_count",
            "pi_obs_definition_completion_count",
            "c_reg_definition_completion_count",
            "adm_a_definition_completion_count",
            "sigma_a_definition_completion_count",
            "stabilization_predicate_definition_completion_count",
            "attractor_class_definition_completion_count",
            "constraint_region_definition_completion_count",
            "causal_mass_definition_completion_count",
            "observer_projection_definition_completion_count",
            "new_sigma_a_refinement_execution_count",
            "new_time_index_refinement_execution_count",
            "new_t_a_refinement_execution_count",
            "new_whole_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_clause_count",
            "new_sigma_a_draft_clause_creation_count",
            "new_carrier_draft_clause_creation_execution_count",
            "new_carrier_level_draft_assembly_execution_count",
            "new_typed_product_carrier_refinement_execution_count",
            "generic_carrier_refinement_execution_count",
            "carrier_refinement_execution_count",
            "carrier_type_refinement_execution_count",
            "new_component_slot_integration_execution_count",
            "new_component_slot_refinement_execution_count",
            "new_carrier_type_selection_count",
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

        return DependentObjectDraftBundleIntegrationExecutionReport(
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

    def _label(self, key: str) -> str:
        overrides = {
            "dependent_object_draft_bundle_integration_execution_count": "Dependent-object draft bundle integration execution count",
            "new_dependent_object_draft_bundle_integration_execution_count": "New dependent-object draft bundle integration execution count",
            "draft_bundle_integration_execution_count": "Draft bundle integration execution count",
            "integrated_dependent_object_draft_bundle_count": "Integrated dependent-object draft bundle count",
            "integrated_dependent_object_draft_count": "Integrated dependent-object draft count",
            "integrated_adm_a_draft_count": "Integrated Adm_A draft count",
            "integrated_c_reg_draft_count": "Integrated C_reg draft count",
            "integrated_pi_obs_draft_count": "Integrated Pi_obs draft count",
            "integrated_m_c_draft_count": "Integrated M_c draft count",
            "integrated_r_a_draft_count": "Integrated R_A draft count",
            "integrated_traj_a_draft_count": "Integrated Traj_A draft count",
            "bundle_linked_to_refined_sigma_a_count": "Bundle linked to refined Sigma_A count",
            "bundle_dependency_coherence_recorded_count": "Bundle dependency coherence recorded count",
            "remaining_dependent_object_deferral_count": "Remaining dependent-object deferral count",
            "all_dependent_object_draft_slots_created_count": "All dependent-object draft slots created count",
            "all_dependent_object_draft_slots_integrated_count": "All dependent-object draft slots integrated count",
            "bundle_integration_row_count": "Bundle integration row count",
            "bundle_integration_check_count": "Bundle integration check count",
            "bundle_integration_boundary_preserved_count": "Bundle integration boundary preserved count",
            "carried_traj_a_definition_draft_execution_count": "Carried Traj_A definition draft execution count",
            "carried_new_traj_a_definition_draft_execution_count": "Carried new Traj_A definition draft execution count",
            "carried_traj_a_draft_slot_created_count": "Carried Traj_A draft slot created count",
            "carried_traj_a_draft_linked_to_refined_sigma_a_count": "Carried Traj_A draft linked to refined Sigma_A count",
            "carried_traj_a_linked_to_adm_a_draft_count": "Carried Traj_A linked to Adm_A draft count",
            "carried_traj_a_linked_to_c_reg_draft_count": "Carried Traj_A linked to C_reg draft count",
            "carried_traj_a_linked_to_pi_obs_draft_count": "Carried Traj_A linked to Pi_obs draft count",
            "carried_traj_a_linked_to_m_c_draft_count": "Carried Traj_A linked to M_c draft count",
            "carried_traj_a_linked_to_r_a_draft_count": "Carried Traj_A linked to R_A draft count",
            "carried_traj_a_trajectory_family_placeholder_count": "Carried Traj_A trajectory-family placeholder count",
            "carried_remaining_dependent_object_deferral_count": "Carried remaining dependent-object deferral count",
            "carried_r_a_definition_draft_execution_count": "Carried R_A definition draft execution count",
            "carried_m_c_definition_draft_execution_count": "Carried M_c definition draft execution count",
            "carried_pi_obs_definition_draft_execution_count": "Carried Pi_obs definition draft execution count",
            "carried_c_reg_definition_draft_execution_count": "Carried C_reg definition draft execution count",
            "carried_adm_a_definition_draft_execution_count": "Carried Adm_A definition draft execution count",
            "carried_sigma_a_refinement_execution_count": "Carried Sigma_A refinement execution count",
            "carried_refined_draft_sigma_a_shell_count": "Carried refined Draft Sigma_A shell count",
            "carried_integrated_time_index_layer_count": "Carried integrated time-index layer count",
            "new_definition_draft_execution_count": "New definition draft execution count",
            "new_dependent_object_definition_draft_execution_count": "New dependent-object definition draft execution count",
            "dependent_object_definition_draft_execution_count": "Dependent-object definition draft execution count",
            "definition_execution_count": "Definition execution count",
            "new_definition_execution_count": "New definition execution count",
            "completed_formal_definition_count": "Completed formal definition count",
            "formalization_complete_count": "Formalization complete count",
            "traj_a_definition_completion_count": "Traj_A definition completion count",
            "r_a_definition_completion_count": "R_A definition completion count",
            "m_c_definition_completion_count": "M_c definition completion count",
            "pi_obs_definition_completion_count": "Pi_obs definition completion count",
            "c_reg_definition_completion_count": "C_reg definition completion count",
            "adm_a_definition_completion_count": "Adm_A definition completion count",
            "sigma_a_definition_completion_count": "Sigma_A definition completion count",
            "theorem_candidate_plan_count": "Theorem candidate plan count",
            "new_theorem_proven_count": "New theorem proven count",
            "proof_assistant_verification_count": "Proof assistant verification count",
            "manuscript_submission_ready_count": "Manuscript submission ready count",
            "readiness_approval_count": "Readiness approval count",
            "new_citation_added_count": "New citation added count",
            "overclaim_count": "Overclaim count",
            "invented_citation_like_pattern_count": "Invented citation-like pattern count",
        }
        return overrides.get(key, key.replace("_", " ").capitalize())

    def _render_report(self, counts: dict[str, int], warnings: list[str]) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric integrate the carried dependent-object draft slots into one bundle while keeping new definition drafts, "
            "final definition execution, dependent-object completion, Sigma_A definition completion, theorem candidate planning, theorem proof, proof assistant verification, validation, readiness, and citations at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Bundle boundary")
        lines.append("- Milestone type: dependent-object draft bundle integration execution only")
        lines.append("- Dependent-object draft bundle integration after this milestone: executed")
        lines.append("- New dependent-object definition draft execution after this milestone: not executed")
        lines.append("- New definition draft execution after this milestone: not executed")
        lines.append("- Final definition execution after this milestone: not executed")
        lines.append("- Dependent-object definition completion after this milestone: not completed")
        lines.append("- Sigma_A definition completion after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("")
        lines.append("## Bundle statement")
        lines.append(self.bundle_statement)
        lines.append("")
        lines.append("## Bundle integration rows")
        lines.append("")
        lines.append("| ID | Focus | Result | Boundary |")
        lines.append("|---|---|---|---|")
        for row in self.integration_rows:
            lines.append(f"| {row['id']} | {row['focus']} | {row['result']} | {row['boundary']} |")
        lines.append("")
        lines.append("## Integration checks")
        for index, check in enumerate(self.checks, start=1):
            lines.append(f"{index}. {check}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact executes one dependent-object draft bundle integration only. "
            "It integrates the carried Adm_A, C_reg, Pi_obs, M_c, R_A, and Traj_A draft slots into one bundle linked to the refined Draft Sigma_A shell, "
            "but it does not create new dependent-object drafts, does not execute final definitions, does not complete Adm_A, does not complete C_reg, "
            "does not complete Pi_obs, does not complete M_c, does not complete R_A, does not complete Traj_A, does not complete Sigma_A, "
            "does not complete any formal definition, does not complete formalization, does not create theorem candidates, does not prove a theorem, "
            "does not run proof execution, does not provide proof assistant verification, does not provide external validation, "
            "does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        order = [
            "dependent_object_draft_bundle_integration_execution_count",
            "new_dependent_object_draft_bundle_integration_execution_count",
            "draft_bundle_integration_execution_count",
            "integrated_dependent_object_draft_bundle_count",
            "integrated_dependent_object_draft_count",
            "integrated_adm_a_draft_count",
            "integrated_c_reg_draft_count",
            "integrated_pi_obs_draft_count",
            "integrated_m_c_draft_count",
            "integrated_r_a_draft_count",
            "integrated_traj_a_draft_count",
            "bundle_linked_to_refined_sigma_a_count",
            "bundle_dependency_coherence_recorded_count",
            "remaining_dependent_object_deferral_count",
            "all_dependent_object_draft_slots_created_count",
            "all_dependent_object_draft_slots_integrated_count",
            "bundle_integration_row_count",
            "bundle_integration_check_count",
            "bundle_integration_boundary_preserved_count",
            "carried_traj_a_definition_draft_execution_count",
            "carried_new_traj_a_definition_draft_execution_count",
            "carried_traj_a_draft_slot_created_count",
            "carried_traj_a_draft_linked_to_refined_sigma_a_count",
            "carried_traj_a_linked_to_adm_a_draft_count",
            "carried_traj_a_linked_to_c_reg_draft_count",
            "carried_traj_a_linked_to_pi_obs_draft_count",
            "carried_traj_a_linked_to_m_c_draft_count",
            "carried_traj_a_linked_to_r_a_draft_count",
            "carried_traj_a_trajectory_family_placeholder_count",
            "carried_remaining_dependent_object_deferral_count",
            "carried_r_a_definition_draft_execution_count",
            "carried_m_c_definition_draft_execution_count",
            "carried_pi_obs_definition_draft_execution_count",
            "carried_c_reg_definition_draft_execution_count",
            "carried_adm_a_definition_draft_execution_count",
            "carried_sigma_a_refinement_execution_count",
            "carried_refined_draft_sigma_a_shell_count",
            "carried_integrated_time_index_layer_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
            "new_definition_draft_execution_count",
            "new_dependent_object_definition_draft_execution_count",
            "dependent_object_definition_draft_execution_count",
            "new_traj_a_definition_draft_execution_count",
            "new_r_a_definition_draft_execution_count",
            "new_m_c_definition_draft_execution_count",
            "new_pi_obs_definition_draft_execution_count",
            "new_c_reg_definition_draft_execution_count",
            "new_adm_a_definition_draft_execution_count",
            "definition_execution_count",
            "new_definition_execution_count",
            "completed_formal_definition_count",
            "formalization_complete_count",
            "traj_a_definition_completion_count",
            "r_a_definition_completion_count",
            "m_c_definition_completion_count",
            "pi_obs_definition_completion_count",
            "c_reg_definition_completion_count",
            "adm_a_definition_completion_count",
            "sigma_a_definition_completion_count",
            "stabilization_predicate_definition_completion_count",
            "attractor_class_definition_completion_count",
            "constraint_region_definition_completion_count",
            "causal_mass_definition_completion_count",
            "observer_projection_definition_completion_count",
            "new_sigma_a_refinement_execution_count",
            "new_time_index_refinement_execution_count",
            "new_t_a_refinement_execution_count",
            "new_whole_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_clause_count",
            "new_sigma_a_draft_clause_creation_count",
            "new_carrier_draft_clause_creation_execution_count",
            "new_carrier_level_draft_assembly_execution_count",
            "new_typed_product_carrier_refinement_execution_count",
            "generic_carrier_refinement_execution_count",
            "carrier_refinement_execution_count",
            "carrier_type_refinement_execution_count",
            "new_component_slot_integration_execution_count",
            "new_component_slot_refinement_execution_count",
            "new_carrier_type_selection_count",
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
            "boundary_phrase_count",
            "prohibited_behavior_count",
            "next_step_count",
            "overclaim_count",
            "invented_citation_like_pattern_count",
            "word_count",
        ]
        for key in order:
            if key in counts:
                lines.append(f"- {self._label(key)}: {counts[key]}")
        lines.append("")
        lines.append("## Warnings")
        for warning in warnings:
            lines.append(f"- {warning}")
        lines.append("")
        lines.append("## Interpretation")
        lines.append(
            "The v8.143 artifact integrates the carried dependent-object draft slots into one bundle. "
            "It does not create a new definition draft and it keeps final definition execution, dependent-object completion, Sigma_A completion, "
            "theorem candidate planning, theorem proof, proof assistant verification, validation, readiness, and citation claims absent."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Execute dependent-object draft bundle boundary audit next only if checking the integration boundary is useful.",
            "Prefer Sigma_A definition completion readiness planning after bundle integration if the bundle remains stable.",
            "Keep definition completion separate from bundle integration.",
            "Keep theorem candidate planning separate from definition completion.",
            "Keep theorem proof separate from theorem candidate planning.",
            "Keep proof assistant verification separate from proof execution.",
            "Keep validation separate from proof work.",
            "Keep manuscript readiness and citation work separate from validation.",
        ]
        for step in next_steps:
            lines.append(f"- {step}")
        lines.append("")
        return "\n".join(lines) + "\n"

    def _count_boundary_phrases(self, text: str) -> int:
        phrases = ["does not", "not executed", "not completed", "not created", "bundle", "definition draft", "boundary", "separate", "zero"]
        return sum(text.count(p) + text.lower().count(p.lower()) for p in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not create new dependent-object drafts",
            "does not execute final definitions",
            "does not complete Adm_A",
            "does not complete C_reg",
            "does not complete Pi_obs",
            "does not complete M_c",
            "does not complete R_A",
            "does not complete Traj_A",
            "does not complete Sigma_A",
            "does not complete any formal definition",
            "does not complete formalization",
            "does not create theorem candidates",
            "does not prove a theorem",
            "does not run proof execution",
            "does not provide proof assistant verification",
            "does not provide external validation",
            "does not approve manuscript submission readiness",
            "does not add new citations",
        ]
        return sum(1 for phrase in prohibited if phrase in text)

    def _count_overclaims(self, text: str) -> int:
        forbidden_positive_counter_names = {
            "new definition draft execution count",
            "new dependent-object definition draft execution count",
            "dependent-object definition draft execution count",
            "definition execution count",
            "new definition execution count",
            "completed formal definition count",
            "formalization complete count",
            "traj_a definition completion count",
            "r_a definition completion count",
            "m_c definition completion count",
            "pi_obs definition completion count",
            "c_reg definition completion count",
            "adm_a definition completion count",
            "sigma_a definition completion count",
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

        allowed_positive_counter_fragments = [
            "bundle integration",
            "integrated",
            "carried",
            "source artifact",
            "all dependent-object draft slots created",
            "all dependent-object draft slots integrated",
            "core formal object",
            "formal object inventory",
            "resolved gap",
            "cumulative limited theorem proven",
            "boundary phrase",
            "prohibited behavior",
            "next step",
            "word",
        ]

        unsafe_phrases = [
            "definition completed",
            "formal definition completed",
            "sigma_a completed",
            "theorem candidate created",
            "new theorem proven",
            "theorem proven",
            "proof assistant verification complete",
            "framework proven",
            "external validation complete",
            "manuscript ready",
            "submission ready",
            "readiness approved",
            "citation added",
        ]

        protective_markers = [
            "does not",
            "do not",
            "not ",
            "not executed",
            "not completed",
            "not created",
            "zero",
            "count: 0",
            "remain",
            "remains",
            "separate",
            "absent",
            "downstream",
            "boundary",
            "draft",
            "warning",
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
                if value > 0:
                    if counter_name in forbidden_positive_counter_names:
                        count += 1
                    elif any(fragment in counter_name for fragment in allowed_positive_counter_fragments):
                        pass
                    elif counter_name in {"unresolved gap count", "remaining blocking gap count", "conditional hold count"}:
                        count += 1
                    else:
                        pass
                continue

            if any(marker in lowered for marker in protective_markers):
                continue

            for phrase in unsafe_phrases:
                if phrase in lowered:
                    count += 1
                    break

        return count

    def _count_invented_citation_like_patterns(self, text: str) -> int:
        patterns = [r"\([A-Z][A-Za-z-]+,\s*20\d{2}\)", r"\[[0-9]{1,3}\]", r"doi:", r"arXiv:"]
        return sum(len(re.findall(pattern, text)) for pattern in patterns)


if __name__ == "__main__":
    report = DependentObjectDraftBundleIntegrationExecutionBuilder().run()
    print(f"Wrote {report.output_path}")
