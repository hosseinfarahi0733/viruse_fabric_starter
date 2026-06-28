from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.pi_obs_definition_draft_execution import (
    PiObsDefinitionDraftExecutionBuilder,
)


def main() -> int:
    report = PiObsDefinitionDraftExecutionBuilder().run()
    output = Path(report.output_path)

    print("Experiment 219: Pi_obs Definition Draft Execution")
    print(
        "Question: Can Viruse Fabric execute one Pi_obs definition draft while keeping final definition execution, Pi_obs completion, "
        "C_reg completion, Adm_A completion, Sigma_A definition completion, theorem candidate planning, theorem proof, proof assistant verification, validation, readiness, and citations at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_artifact}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")

    keys = [
        "pi_obs_definition_draft_execution_count",
        "new_pi_obs_definition_draft_execution_count",
        "new_definition_draft_execution_count",
        "dependent_object_definition_draft_execution_count",
        "pi_obs_draft_slot_created_count",
        "pi_obs_draft_linked_to_refined_sigma_a_count",
        "pi_obs_linked_to_adm_a_draft_count",
        "pi_obs_linked_to_c_reg_draft_count",
        "pi_obs_observer_projection_placeholder_count",
        "remaining_dependent_object_deferral_count",
        "definition_draft_execution_row_count",
        "definition_draft_execution_check_count",
        "definition_draft_boundary_preserved_count",
        "carried_c_reg_definition_draft_execution_count",
        "carried_c_reg_draft_linked_to_refined_sigma_a_count",
        "carried_c_reg_linked_to_adm_a_draft_count",
        "carried_adm_a_definition_draft_execution_count",
        "carried_sigma_a_refinement_execution_count",
        "carried_refined_draft_sigma_a_shell_count",
        "carried_integrated_time_index_layer_count",
        "definition_execution_count",
        "new_definition_execution_count",
        "completed_formal_definition_count",
        "formalization_complete_count",
        "pi_obs_definition_completion_count",
        "c_reg_definition_completion_count",
        "adm_a_definition_completion_count",
        "sigma_a_definition_completion_count",
        "theorem_candidate_plan_count",
        "new_theorem_proven_count",
        "cumulative_limited_theorem_proven_count",
        "proof_assistant_verification_count",
        "external_validation_count",
        "independent_experiment_count",
        "manuscript_submission_ready_count",
        "readiness_approval_count",
        "new_citation_added_count",
        "overclaim_count",
        "invented_citation_like_pattern_count",
    ]

    labels = {
        "pi_obs_definition_draft_execution_count": "Pi_obs definition draft execution count",
        "new_pi_obs_definition_draft_execution_count": "New Pi_obs definition draft execution count",
        "new_definition_draft_execution_count": "New definition draft execution count",
        "dependent_object_definition_draft_execution_count": "Dependent-object definition draft execution count",
        "pi_obs_draft_slot_created_count": "Pi_obs draft slot created count",
        "pi_obs_draft_linked_to_refined_sigma_a_count": "Pi_obs draft linked to refined Sigma_A count",
        "pi_obs_linked_to_adm_a_draft_count": "Pi_obs linked to Adm_A draft count",
        "pi_obs_linked_to_c_reg_draft_count": "Pi_obs linked to C_reg draft count",
        "pi_obs_observer_projection_placeholder_count": "Pi_obs observer-projection placeholder count",
        "remaining_dependent_object_deferral_count": "Remaining dependent-object deferral count",
        "definition_draft_execution_row_count": "Definition draft execution row count",
        "definition_draft_execution_check_count": "Definition draft execution check count",
        "definition_draft_boundary_preserved_count": "Definition draft boundary preserved count",
        "carried_c_reg_definition_draft_execution_count": "Carried C_reg definition draft execution count",
        "carried_c_reg_draft_linked_to_refined_sigma_a_count": "Carried C_reg draft linked to refined Sigma_A count",
        "carried_c_reg_linked_to_adm_a_draft_count": "Carried C_reg linked to Adm_A draft count",
        "carried_adm_a_definition_draft_execution_count": "Carried Adm_A definition draft execution count",
        "carried_sigma_a_refinement_execution_count": "Carried Sigma_A refinement execution count",
        "carried_refined_draft_sigma_a_shell_count": "Carried refined Draft Sigma_A shell count",
        "carried_integrated_time_index_layer_count": "Carried integrated time-index layer count",
        "definition_execution_count": "Definition execution count",
        "new_definition_execution_count": "New definition execution count",
        "completed_formal_definition_count": "Completed formal definition count",
        "formalization_complete_count": "Formalization complete count",
        "pi_obs_definition_completion_count": "Pi_obs definition completion count",
        "c_reg_definition_completion_count": "C_reg definition completion count",
        "adm_a_definition_completion_count": "Adm_A definition completion count",
        "sigma_a_definition_completion_count": "Sigma_A definition completion count",
        "theorem_candidate_plan_count": "Theorem candidate plan count",
        "new_theorem_proven_count": "New theorem proven count",
        "cumulative_limited_theorem_proven_count": "Cumulative limited theorem proven count",
        "proof_assistant_verification_count": "Proof assistant verification count",
        "external_validation_count": "External validation count",
        "independent_experiment_count": "Independent experiment count",
        "manuscript_submission_ready_count": "Manuscript submission ready count",
        "readiness_approval_count": "Readiness approval count",
        "new_citation_added_count": "New citation added count",
        "overclaim_count": "Overclaim count",
        "invented_citation_like_pattern_count": "Invented citation-like pattern count",
    }

    for key in keys:
        print(f"{labels[key]}: {getattr(report, key)}")

    print(f"Boundary phrase count: {report.boundary_phrase_count}")
    print(f"Prohibited behavior count: {report.prohibited_behavior_count}")
    print(f"Next step count: {report.next_step_count}")
    print(f"Word count: {report.word_count}")
    print(f"Errors: {report.error_count}")
    print(f"Warnings: {report.warning_count}")
    print(f"Passed: {report.passed}")
    print(f"Report exists: {output.exists()}")
    print(f"Report size: {output.stat().st_size if output.exists() else 0}")

    required_phrases = [
        "Pi_obs Definition Draft Execution v8.139",
        "Pi_obs definition draft execution only",
        "Pi_obs definition draft execution count: 1",
        "New Pi_obs definition draft execution count: 1",
        "New definition draft execution count: 1",
        "Dependent-object definition draft execution count: 1",
        "Pi_obs draft slot created count: 1",
        "Pi_obs draft linked to refined Sigma_A count: 1",
        "Pi_obs linked to Adm_A draft count: 1",
        "Pi_obs linked to C_reg draft count: 1",
        "Pi_obs observer-projection placeholder count: 1",
        "Remaining dependent-object deferral count: 3",
        "Definition draft execution row count: 8",
        "Definition draft execution check count: 8",
        "Definition draft boundary preserved count: 8",
        "Carried C_reg definition draft execution count: 1",
        "Carried C_reg draft linked to refined Sigma_A count: 1",
        "Carried C_reg linked to Adm_A draft count: 1",
        "Carried Adm_A definition draft execution count: 1",
        "Carried Sigma_A refinement execution count: 1",
        "Carried refined Draft Sigma_A shell count: 1",
        "Carried integrated time-index layer count: 1",
        "Definition execution count: 0",
        "New definition execution count: 0",
        "Completed formal definition count: 0",
        "Formalization complete count: 0",
        "Pi_obs definition completion count: 0",
        "C_reg definition completion count: 0",
        "Adm_A definition completion count: 0",
        "Sigma_A definition completion count: 0",
        "Theorem candidate plan count: 0",
        "New theorem proven count: 0",
        "Proof assistant verification count: 0",
        "External validation count: 0",
        "Independent experiment count: 0",
        "Manuscript submission ready count: 0",
        "Readiness approval count: 0",
        "New citation added count: 0",
    ]

    text = output.read_text(encoding="utf-8") if output.exists() else ""
    missing = [phrase for phrase in required_phrases if phrase not in text]
    print(f"Missing required report phrases: {len(missing)}")
    for phrase in missing:
        print(f"Missing phrase: {phrase}")

    if report.errors:
        print("Errors:")
        for error in report.errors:
            print(f"- {error}")

    if report.warnings:
        print("Warnings:")
        for warning in report.warnings:
            print(f"- {warning}")

    if missing or not report.passed:
        return 1

    print(
        "Interpretation: The v8.139 artifact executes one Pi_obs definition draft while preserving zero counts for final definition execution, "
        "Pi_obs completion, C_reg completion, Adm_A completion, Sigma_A completion, theorem candidate planning, theorem proof, proof assistant verification, validation, readiness, and citation claims."
    )
    print("Experiment 219 completed successfully.")
    print("V8_139_OFFICIAL_EXPERIMENT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
