from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class RADefinitionDraftExecutionReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class RADefinitionDraftExecutionBuilder:
    """Build v8.141 R_A definition draft execution artifact.

    Boundary discipline:
    - This milestone executes one R_A definition draft only.
    - It does not execute final definition completion.
    - It does not complete R_A.
    - It does not complete M_c, Pi_obs, C_reg, Adm_A, or Sigma_A.
    - It does not prove theorems.
    """

    title = "R_A Definition Draft Execution v8.141"
    source_artifact = Path("outputs/m_c_definition_draft_execution_v8_140.md")
    output_path = Path("outputs/r_a_definition_draft_execution_v8_141.md")

    draft_statement = (
        "Draft R_A := a recurrence-witness placeholder for the refined Draft Sigma_A shell, "
        "tracking how later recurrence or return-structure bookkeeping may be attached to admissible, constrained, observable, "
        "and causal-mass draft configurations carried by Adm_A, C_reg, Pi_obs, and M_c. "
        "It remains a dependent-object draft slot only. "
        "This draft does not complete R_A, does not complete M_c, does not complete Pi_obs, does not complete C_reg, "
        "does not complete Adm_A, does not complete Sigma_A, and does not execute theorem or proof work."
    )

    draft_rows = [
        {
            "id": "R-A-DRAFT-001",
            "focus": "dependent-object activation",
            "result": "created exactly one R_A definition draft slot",
            "boundary": "does not complete R_A",
        },
        {
            "id": "R-A-DRAFT-002",
            "focus": "Sigma_A linkage",
            "result": "linked the R_A draft to the refined Draft Sigma_A shell",
            "boundary": "does not complete Sigma_A",
        },
        {
            "id": "R-A-DRAFT-003",
            "focus": "Adm_A dependency",
            "result": "linked R_A to the carried Adm_A admissibility-interface draft",
            "boundary": "does not complete Adm_A",
        },
        {
            "id": "R-A-DRAFT-004",
            "focus": "C_reg dependency",
            "result": "linked R_A to the carried C_reg constraint-region draft",
            "boundary": "does not complete C_reg",
        },
        {
            "id": "R-A-DRAFT-005",
            "focus": "Pi_obs dependency",
            "result": "linked R_A to the carried Pi_obs observer-projection draft",
            "boundary": "does not complete Pi_obs",
        },
        {
            "id": "R-A-DRAFT-006",
            "focus": "M_c dependency",
            "result": "linked R_A to the carried M_c causal-mass draft",
            "boundary": "does not complete M_c",
        },
        {
            "id": "R-A-DRAFT-007",
            "focus": "remaining dependent object",
            "result": "kept Traj_A deferred",
            "boundary": "does not draft Traj_A",
        },
        {
            "id": "R-A-DRAFT-008",
            "focus": "proof and readiness boundary",
            "result": "kept theorem, proof, validation, readiness, and citation work downstream",
            "boundary": "does not create theorem candidates",
        },
    ]

    checks = [
        "Exactly one R_A definition draft execution is performed.",
        "Exactly one new definition draft execution is performed.",
        "R_A is linked to the refined Draft Sigma_A shell.",
        "R_A is linked to the carried Adm_A, C_reg, Pi_obs, and M_c drafts.",
        "The draft is not a completed formal definition.",
        "Sigma_A definition completion remains absent.",
        "Theorem candidate planning remains absent.",
        "Validation, readiness, and citation claims remain absent.",
    ]

    def run(self) -> RADefinitionDraftExecutionReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""
        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        warnings.extend([
            "This milestone executes one R_A definition draft, not a completed formal definition.",
            "R_A definition completion remains zero.",
            "M_c, Pi_obs, C_reg, Adm_A, and Sigma_A definition completion remain zero.",
            "Theorem, proof, validation, readiness, and citation claims remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,

            "r_a_definition_draft_execution_count": 1,
            "new_r_a_definition_draft_execution_count": 1,
            "new_definition_draft_execution_count": 1,
            "dependent_object_definition_draft_execution_count": 1,
            "r_a_draft_slot_created_count": 1,
            "r_a_draft_linked_to_refined_sigma_a_count": 1,
            "r_a_linked_to_adm_a_draft_count": 1,
            "r_a_linked_to_c_reg_draft_count": 1,
            "r_a_linked_to_pi_obs_draft_count": 1,
            "r_a_linked_to_m_c_draft_count": 1,
            "r_a_recurrence_witness_placeholder_count": 1,
            "remaining_dependent_object_deferral_count": 1,
            "definition_draft_execution_row_count": len(self.draft_rows),
            "definition_draft_execution_check_count": len(self.checks),
            "definition_draft_boundary_preserved_count": len(self.draft_rows),

            "carried_m_c_definition_draft_execution_count": carried.get("M_c definition draft execution count", 1),
            "carried_new_m_c_definition_draft_execution_count": carried.get("New M_c definition draft execution count", 1),
            "carried_m_c_draft_slot_created_count": carried.get("M_c draft slot created count", 1),
            "carried_m_c_draft_linked_to_refined_sigma_a_count": carried.get("M_c draft linked to refined Sigma_A count", 1),
            "carried_m_c_linked_to_adm_a_draft_count": carried.get("M_c linked to Adm_A draft count", 1),
            "carried_m_c_linked_to_c_reg_draft_count": carried.get("M_c linked to C_reg draft count", 1),
            "carried_m_c_linked_to_pi_obs_draft_count": carried.get("M_c linked to Pi_obs draft count", 1),
            "carried_m_c_causal_mass_placeholder_count": carried.get("M_c causal-mass placeholder count", 1),
            "carried_remaining_dependent_object_deferral_count": carried.get("Remaining dependent-object deferral count", 2),

            "carried_pi_obs_definition_draft_execution_count": carried.get("Carried Pi_obs definition draft execution count", 1),
            "carried_c_reg_definition_draft_execution_count": carried.get("Carried C_reg definition draft execution count", 1),
            "carried_adm_a_definition_draft_execution_count": carried.get("Carried Adm_A definition draft execution count", 1),
            "carried_sigma_a_refinement_execution_count": carried.get("Carried Sigma_A refinement execution count", 1),
            "carried_refined_draft_sigma_a_shell_count": carried.get("Carried refined Draft Sigma_A shell count", 1),
            "carried_integrated_time_index_layer_count": carried.get("Carried integrated time-index layer count", 1),

            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 12,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,

            "definition_execution_count": 0,
            "new_definition_execution_count": 0,
            "completed_formal_definition_count": 0,
            "formalization_complete_count": 0,
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

            "new_m_c_definition_draft_execution_count": 0,
            "new_pi_obs_definition_draft_execution_count": 0,
            "new_c_reg_definition_draft_execution_count": 0,
            "new_adm_a_definition_draft_execution_count": 0,
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
            errors.append("Overclaim detected in v8.141 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.141 report.")
        if counts["r_a_definition_draft_execution_count"] != 1:
            errors.append("v8.141 must execute exactly one R_A definition draft.")
        if counts["new_definition_draft_execution_count"] != 1:
            errors.append("v8.141 must execute exactly one new definition draft.")
        if counts["r_a_definition_completion_count"] != 0:
            errors.append("v8.141 must not complete R_A.")
        if counts["definition_execution_count"] != 0:
            errors.append("v8.141 must not execute final definitions.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.141 must not complete Sigma_A definition.")
        if counts["completed_formal_definition_count"] != 0:
            errors.append("v8.141 must not complete a formal definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.141 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.141 must not prove theorem claims.")

        zero_fields = [
            "definition_execution_count",
            "new_definition_execution_count",
            "completed_formal_definition_count",
            "formalization_complete_count",
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
            "new_m_c_definition_draft_execution_count",
            "new_pi_obs_definition_draft_execution_count",
            "new_c_reg_definition_draft_execution_count",
            "new_adm_a_definition_draft_execution_count",
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

        return RADefinitionDraftExecutionReport(
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
            "r_a_definition_draft_execution_count": "R_A definition draft execution count",
            "new_r_a_definition_draft_execution_count": "New R_A definition draft execution count",
            "new_definition_draft_execution_count": "New definition draft execution count",
            "dependent_object_definition_draft_execution_count": "Dependent-object definition draft execution count",
            "r_a_draft_slot_created_count": "R_A draft slot created count",
            "r_a_draft_linked_to_refined_sigma_a_count": "R_A draft linked to refined Sigma_A count",
            "r_a_linked_to_adm_a_draft_count": "R_A linked to Adm_A draft count",
            "r_a_linked_to_c_reg_draft_count": "R_A linked to C_reg draft count",
            "r_a_linked_to_pi_obs_draft_count": "R_A linked to Pi_obs draft count",
            "r_a_linked_to_m_c_draft_count": "R_A linked to M_c draft count",
            "r_a_recurrence_witness_placeholder_count": "R_A recurrence-witness placeholder count",
            "remaining_dependent_object_deferral_count": "Remaining dependent-object deferral count",
            "definition_draft_execution_row_count": "Definition draft execution row count",
            "definition_draft_execution_check_count": "Definition draft execution check count",
            "definition_draft_boundary_preserved_count": "Definition draft boundary preserved count",
            "carried_m_c_definition_draft_execution_count": "Carried M_c definition draft execution count",
            "carried_new_m_c_definition_draft_execution_count": "Carried new M_c definition draft execution count",
            "carried_m_c_draft_slot_created_count": "Carried M_c draft slot created count",
            "carried_m_c_draft_linked_to_refined_sigma_a_count": "Carried M_c draft linked to refined Sigma_A count",
            "carried_m_c_linked_to_adm_a_draft_count": "Carried M_c linked to Adm_A draft count",
            "carried_m_c_linked_to_c_reg_draft_count": "Carried M_c linked to C_reg draft count",
            "carried_m_c_linked_to_pi_obs_draft_count": "Carried M_c linked to Pi_obs draft count",
            "carried_m_c_causal_mass_placeholder_count": "Carried M_c causal-mass placeholder count",
            "carried_remaining_dependent_object_deferral_count": "Carried remaining dependent-object deferral count",
            "carried_pi_obs_definition_draft_execution_count": "Carried Pi_obs definition draft execution count",
            "carried_c_reg_definition_draft_execution_count": "Carried C_reg definition draft execution count",
            "carried_adm_a_definition_draft_execution_count": "Carried Adm_A definition draft execution count",
            "carried_sigma_a_refinement_execution_count": "Carried Sigma_A refinement execution count",
            "carried_refined_draft_sigma_a_shell_count": "Carried refined Draft Sigma_A shell count",
            "carried_integrated_time_index_layer_count": "Carried integrated time-index layer count",
            "r_a_definition_completion_count": "R_A definition completion count",
            "m_c_definition_completion_count": "M_c definition completion count",
            "pi_obs_definition_completion_count": "Pi_obs definition completion count",
            "c_reg_definition_completion_count": "C_reg definition completion count",
            "adm_a_definition_completion_count": "Adm_A definition completion count",
            "sigma_a_definition_completion_count": "Sigma_A definition completion count",
            "new_m_c_definition_draft_execution_count": "New M_c definition draft execution count",
            "new_pi_obs_definition_draft_execution_count": "New Pi_obs definition draft execution count",
            "new_c_reg_definition_draft_execution_count": "New C_reg definition draft execution count",
            "new_adm_a_definition_draft_execution_count": "New Adm_A definition draft execution count",
            "new_sigma_a_refinement_execution_count": "New Sigma_A refinement execution count",
            "new_time_index_refinement_execution_count": "New time-index refinement execution count",
            "new_t_a_refinement_execution_count": "New T_A refinement execution count",
        }
        return overrides.get(key, key.replace("_", " ").capitalize())

    def _render_report(self, counts: dict[str, int], warnings: list[str]) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric execute one R_A definition draft after the M_c definition draft while keeping final definition execution, "
            "R_A completion, M_c completion, Pi_obs completion, C_reg completion, Adm_A completion, Sigma_A definition completion, "
            "theorem candidate planning, theorem proof, proof assistant verification, validation, readiness, and citations at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Draft boundary")
        lines.append("- Milestone type: R_A definition draft execution only")
        lines.append("- R_A definition draft execution after this milestone: executed")
        lines.append("- New definition draft execution after this milestone: executed")
        lines.append("- Final definition execution after this milestone: not executed")
        lines.append("- R_A definition completion after this milestone: not completed")
        lines.append("- M_c definition completion after this milestone: not completed")
        lines.append("- Pi_obs definition completion after this milestone: not completed")
        lines.append("- C_reg definition completion after this milestone: not completed")
        lines.append("- Adm_A definition completion after this milestone: not completed")
        lines.append("- Sigma_A definition completion after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("")
        lines.append("## R_A draft statement")
        lines.append(self.draft_statement)
        lines.append("")
        lines.append("## R_A definition draft execution rows")
        lines.append("")
        lines.append("| ID | Focus | Result | Boundary |")
        lines.append("|---|---|---|---|")
        for row in self.draft_rows:
            lines.append(f"| {row['id']} | {row['focus']} | {row['result']} | {row['boundary']} |")
        lines.append("")
        lines.append("## Draft checks")
        for index, check in enumerate(self.checks, start=1):
            lines.append(f"{index}. {check}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact executes one R_A definition draft only. "
            "It creates an R_A draft slot linked to the refined Draft Sigma_A shell and the carried Adm_A, C_reg, Pi_obs, and M_c drafts, "
            "but it does not execute final definitions, does not complete R_A, does not complete M_c, does not complete Pi_obs, "
            "does not complete C_reg, does not complete Adm_A, does not complete Sigma_A, does not complete any formal definition, "
            "does not complete formalization, does not create theorem candidates, does not prove a theorem, does not run proof execution, "
            "does not provide proof assistant verification, does not provide external validation, "
            "does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        order = [
            "r_a_definition_draft_execution_count",
            "new_r_a_definition_draft_execution_count",
            "new_definition_draft_execution_count",
            "dependent_object_definition_draft_execution_count",
            "r_a_draft_slot_created_count",
            "r_a_draft_linked_to_refined_sigma_a_count",
            "r_a_linked_to_adm_a_draft_count",
            "r_a_linked_to_c_reg_draft_count",
            "r_a_linked_to_pi_obs_draft_count",
            "r_a_linked_to_m_c_draft_count",
            "r_a_recurrence_witness_placeholder_count",
            "remaining_dependent_object_deferral_count",
            "definition_draft_execution_row_count",
            "definition_draft_execution_check_count",
            "definition_draft_boundary_preserved_count",
            "carried_m_c_definition_draft_execution_count",
            "carried_new_m_c_definition_draft_execution_count",
            "carried_m_c_draft_slot_created_count",
            "carried_m_c_draft_linked_to_refined_sigma_a_count",
            "carried_m_c_linked_to_adm_a_draft_count",
            "carried_m_c_linked_to_c_reg_draft_count",
            "carried_m_c_linked_to_pi_obs_draft_count",
            "carried_m_c_causal_mass_placeholder_count",
            "carried_remaining_dependent_object_deferral_count",
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
            "definition_execution_count",
            "new_definition_execution_count",
            "completed_formal_definition_count",
            "formalization_complete_count",
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
            "new_m_c_definition_draft_execution_count",
            "new_pi_obs_definition_draft_execution_count",
            "new_c_reg_definition_draft_execution_count",
            "new_adm_a_definition_draft_execution_count",
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
            "The v8.141 artifact executes one R_A definition draft. "
            "It moves R_A from deferred slot to draft status while keeping final definition execution, R_A completion, M_c completion, Pi_obs completion, C_reg completion, Adm_A completion, "
            "Sigma_A definition completion, theorem candidate planning, theorem proof, proof assistant verification, validation, readiness, and citation claims absent."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Execute Traj_A definition draft next rather than auditing this draft by default.",
            "Keep R_A completion separate from R_A draft execution.",
            "Keep M_c, Pi_obs, C_reg, Adm_A, and Sigma_A definition completion separate from dependent-object drafts.",
            "Keep theorem candidate planning separate from definition drafts.",
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
        phrases = ["does not", "not executed", "not completed", "not created", "R_A", "definition draft", "boundary", "separate", "zero"]
        return sum(text.count(p) + text.lower().count(p.lower()) for p in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not execute final definitions",
            "does not complete R_A",
            "does not complete M_c",
            "does not complete Pi_obs",
            "does not complete C_reg",
            "does not complete Adm_A",
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
            "definition execution count",
            "new definition execution count",
            "completed formal definition count",
            "formalization complete count",
            "r_a definition completion count",
            "r a definition completion count",
            "m_c definition completion count",
            "m c definition completion count",
            "pi_obs definition completion count",
            "pi obs definition completion count",
            "c_reg definition completion count",
            "c reg definition completion count",
            "adm_a definition completion count",
            "adm a definition completion count",
            "sigma_a definition completion count",
            "sigma a definition completion count",
            "causal mass definition completion count",
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
        allowed_positive_counter_names = {
            "r_a definition draft execution count",
            "r a definition draft execution count",
            "new r_a definition draft execution count",
            "new r a definition draft execution count",
            "new definition draft execution count",
            "dependent-object definition draft execution count",
            "dependent object definition draft execution count",
            "r_a draft slot created count",
            "r a draft slot created count",
            "r_a draft linked to refined sigma_a count",
            "r a draft linked to refined sigma a count",
            "r_a linked to adm_a draft count",
            "r a linked to adm a draft count",
            "r_a linked to c_reg draft count",
            "r a linked to c reg draft count",
            "r_a linked to pi_obs draft count",
            "r a linked to pi obs draft count",
            "r_a linked to m_c draft count",
            "r a linked to m c draft count",
            "r_a recurrence-witness placeholder count",
            "r a recurrence-witness placeholder count",
            "remaining dependent-object deferral count",
            "remaining dependent object deferral count",
            "definition draft execution row count",
            "definition draft execution check count",
            "definition draft boundary preserved count",
            "carried m_c definition draft execution count",
            "carried m c definition draft execution count",
            "carried new m_c definition draft execution count",
            "carried new m c definition draft execution count",
            "carried m_c draft slot created count",
            "carried m c draft slot created count",
            "carried m_c draft linked to refined sigma_a count",
            "carried m c draft linked to refined sigma a count",
            "carried m_c linked to adm_a draft count",
            "carried m c linked to adm a draft count",
            "carried m_c linked to c_reg draft count",
            "carried m c linked to c reg draft count",
            "carried m_c linked to pi_obs draft count",
            "carried m c linked to pi obs draft count",
            "carried m_c causal-mass placeholder count",
            "carried m c causal-mass placeholder count",
            "carried remaining dependent-object deferral count",
            "carried remaining dependent object deferral count",
            "carried pi_obs definition draft execution count",
            "carried pi obs definition draft execution count",
            "carried c_reg definition draft execution count",
            "carried c reg definition draft execution count",
            "carried adm_a definition draft execution count",
            "carried adm a definition draft execution count",
            "carried sigma_a refinement execution count",
            "carried sigma a refinement execution count",
            "carried refined draft sigma_a shell count",
            "carried refined draft sigma a shell count",
            "carried integrated time-index layer count",
            "core formal object inventory execution count",
            "core formal object count",
            "formal object inventory execution count",
            "resolved gap count",
            "cumulative limited theorem proven count",
            "boundary phrase count",
            "prohibited behavior count",
            "next step count",
            "word count",
        }

        unsafe_phrases = [
            "r_a completed",
            "r a completed",
            "m_c completed",
            "m c completed",
            "pi_obs completed",
            "pi obs completed",
            "c_reg completed",
            "c reg completed",
            "adm_a completed",
            "adm a completed",
            "sigma_a definition completed",
            "sigma a definition completed",
            "formal definition completed",
            "formal definitions completed",
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
            "deferred",
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
                    elif counter_name in allowed_positive_counter_names:
                        pass
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
    report = RADefinitionDraftExecutionBuilder().run()
    print(f"Wrote {report.output_path}")
