from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.controlled_sigma_a_definition_completion_execution import (
    ControlledSigmaADefinitionCompletionExecutionBuilder,
)


def main() -> int:
    report = ControlledSigmaADefinitionCompletionExecutionBuilder().run()
    output = Path(report.output_path)

    print("Experiment 227: Controlled Sigma_A Definition Completion Execution")
    print(
        "Question: Can Viruse Fabric execute controlled Sigma_A definition completion while keeping dependent-object completion, "
        "full formalization, theorem candidate planning, theorem proof, validation, readiness approval, and citations at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_artifact}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")

    keys = [
        "controlled_sigma_a_definition_completion_execution_count",
        "new_controlled_sigma_a_definition_completion_execution_count",
        "sigma_a_definition_completion_execution_count",
        "definition_completion_execution_count",
        "completion_execution_count",
        "definition_execution_count",
        "new_definition_execution_count",
        "sigma_a_definition_completion_count",
        "completed_sigma_a_definition_count",
        "completed_formal_definition_count",
        "controlled_completion_gate_execution_count",
        "completion_execution_row_count",
        "completion_execution_check_count",
        "completion_execution_boundary_preserved_count",
        "imported_controlled_sigma_a_definition_completion_execution_plan_count",
        "imported_new_controlled_sigma_a_definition_completion_execution_plan_count",
        "imported_sigma_a_definition_completion_execution_plan_count",
        "imported_definition_completion_execution_plan_count",
        "imported_execution_plan_row_count",
        "imported_execution_plan_check_count",
        "imported_execution_plan_gate_count",
        "imported_readiness_boundary_audit_count",
        "imported_audited_dependent_object_draft_bundle_count",
        "imported_audited_dependent_object_draft_count",
        "imported_audited_bundle_linked_to_refined_sigma_a_count",
        "imported_audited_planned_future_sigma_a_definition_completion_scope_count",
        "imported_audited_planned_future_completion_gate_count",
        "new_controlled_sigma_a_definition_completion_execution_plan_count",
        "controlled_sigma_a_definition_completion_execution_plan_count",
        "sigma_a_definition_completion_execution_plan_count",
        "definition_completion_execution_plan_count",
        "formalization_complete_count",
        "dependent_object_definition_completion_count",
        "adm_a_definition_completion_count",
        "c_reg_definition_completion_count",
        "pi_obs_definition_completion_count",
        "m_c_definition_completion_count",
        "r_a_definition_completion_count",
        "traj_a_definition_completion_count",
        "completion_decision_count",
        "completion_execution_authorized_count",
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
        "controlled_sigma_a_definition_completion_execution_count": "Controlled Sigma_A definition completion execution count",
        "new_controlled_sigma_a_definition_completion_execution_count": "New controlled Sigma_A definition completion execution count",
        "sigma_a_definition_completion_execution_count": "Sigma_A definition completion execution count",
        "definition_completion_execution_count": "Definition completion execution count",
        "completion_execution_count": "Completion execution count",
        "definition_execution_count": "Definition execution count",
        "new_definition_execution_count": "New definition execution count",
        "sigma_a_definition_completion_count": "Sigma_A definition completion count",
        "completed_sigma_a_definition_count": "Completed Sigma_A definition count",
        "completed_formal_definition_count": "Completed formal definition count",
        "controlled_completion_gate_execution_count": "Controlled completion gate execution count",
        "completion_execution_row_count": "Completion execution row count",
        "completion_execution_check_count": "Completion execution check count",
        "completion_execution_boundary_preserved_count": "Completion execution boundary preserved count",
        "imported_controlled_sigma_a_definition_completion_execution_plan_count": "Imported controlled Sigma_A definition completion execution plan count",
        "imported_new_controlled_sigma_a_definition_completion_execution_plan_count": "Imported new controlled Sigma_A definition completion execution plan count",
        "imported_sigma_a_definition_completion_execution_plan_count": "Imported Sigma_A definition completion execution plan count",
        "imported_definition_completion_execution_plan_count": "Imported definition completion execution plan count",
        "imported_execution_plan_row_count": "Imported execution plan row count",
        "imported_execution_plan_check_count": "Imported execution plan check count",
        "imported_execution_plan_gate_count": "Imported execution plan gate count",
        "imported_readiness_boundary_audit_count": "Imported readiness boundary audit count",
        "imported_audited_dependent_object_draft_bundle_count": "Imported audited dependent-object draft bundle count",
        "imported_audited_dependent_object_draft_count": "Imported audited dependent-object draft count",
        "imported_audited_bundle_linked_to_refined_sigma_a_count": "Imported audited bundle linked to refined Sigma_A count",
        "imported_audited_planned_future_sigma_a_definition_completion_scope_count": "Imported audited planned future Sigma_A definition completion scope count",
        "imported_audited_planned_future_completion_gate_count": "Imported audited planned future completion gate count",
        "new_controlled_sigma_a_definition_completion_execution_plan_count": "New controlled Sigma_A definition completion execution plan count",
        "controlled_sigma_a_definition_completion_execution_plan_count": "Controlled Sigma_A definition completion execution plan count",
        "sigma_a_definition_completion_execution_plan_count": "Sigma_A definition completion execution plan count",
        "definition_completion_execution_plan_count": "Definition completion execution plan count",
        "formalization_complete_count": "Formalization complete count",
        "dependent_object_definition_completion_count": "Dependent-object definition completion count",
        "adm_a_definition_completion_count": "Adm_A definition completion count",
        "c_reg_definition_completion_count": "C_reg definition completion count",
        "pi_obs_definition_completion_count": "Pi_obs definition completion count",
        "m_c_definition_completion_count": "M_c definition completion count",
        "r_a_definition_completion_count": "R_A definition completion count",
        "traj_a_definition_completion_count": "Traj_A definition completion count",
        "completion_decision_count": "Completion decision count",
        "completion_execution_authorized_count": "Completion execution authorized count",
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
        "Controlled Sigma_A Definition Completion Execution v8.147",
        "Controlled Sigma_A definition completion execution count: 1",
        "New controlled Sigma_A definition completion execution count: 1",
        "Sigma_A definition completion execution count: 1",
        "Definition completion execution count: 1",
        "Completion execution count: 1",
        "Definition execution count: 1",
        "New definition execution count: 1",
        "Sigma_A definition completion count: 1",
        "Completed Sigma_A definition count: 1",
        "Completed formal definition count: 1",
        "Controlled completion gate execution count: 8",
        "Completion execution row count: 8",
        "Completion execution check count: 8",
        "Completion execution boundary preserved count: 8",
        "Imported controlled Sigma_A definition completion execution plan count: 1",
        "Imported new controlled Sigma_A definition completion execution plan count: 1",
        "Imported Sigma_A definition completion execution plan count: 1",
        "Imported definition completion execution plan count: 1",
        "Imported execution plan row count: 8",
        "Imported execution plan check count: 8",
        "Imported execution plan gate count: 8",
        "Imported readiness boundary audit count: 1",
        "Imported audited dependent-object draft bundle count: 1",
        "Imported audited dependent-object draft count: 6",
        "Imported audited bundle linked to refined Sigma_A count: 1",
        "Imported audited planned future Sigma_A definition completion scope count: 1",
        "Imported audited planned future completion gate count: 8",
        "New controlled Sigma_A definition completion execution plan count: 0",
        "Controlled Sigma_A definition completion execution plan count: 0",
        "Sigma_A definition completion execution plan count: 0",
        "Definition completion execution plan count: 0",
        "Formalization complete count: 0",
        "Dependent-object definition completion count: 0",
        "Adm_A definition completion count: 0",
        "C_reg definition completion count: 0",
        "Pi_obs definition completion count: 0",
        "M_c definition completion count: 0",
        "R_A definition completion count: 0",
        "Traj_A definition completion count: 0",
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
        "Interpretation: The v8.147 artifact executes controlled Sigma_A definition completion while preserving zero counts for dependent-object completion, "
        "full formalization, theorem candidate planning, theorem proof, validation, readiness approval, and citation claims."
    )
    print("Experiment 227 completed successfully.")
    print("V8_147_OFFICIAL_EXPERIMENT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
