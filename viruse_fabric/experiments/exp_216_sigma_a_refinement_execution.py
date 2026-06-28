from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.sigma_a_refinement_execution import (
    SigmaARefinementExecutionBuilder,
)


def main() -> int:
    report = SigmaARefinementExecutionBuilder().run()
    output = Path(report.output_path)

    print("Experiment 216: Sigma_A Refinement Execution")
    print(
        "Question: Can Viruse Fabric execute bounded Sigma_A refinement while keeping definition execution, Sigma_A definition completion, "
        "theorem candidate planning, theorem proof, proof assistant verification, validation, readiness, and citations at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_artifact}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")

    keys = [
        "sigma_a_refinement_execution_count",
        "new_sigma_a_refinement_execution_count",
        "draft_sigma_a_refinement_execution_count",
        "executed_sigma_a_refinement_layer_count",
        "refined_draft_sigma_a_shell_count",
        "integrated_time_index_layer_count",
        "integrated_t_a_refinement_layer_count",
        "draft_shell_refinement_link_executed_count",
        "carrier_clause_preserved_count",
        "dependent_object_slots_retained_as_deferred_count",
        "audit_traceability_carried_count",
        "sigma_a_refinement_execution_row_count",
        "sigma_a_refinement_execution_check_count",
        "sigma_a_refinement_boundary_preserved_count",
        "carried_sigma_a_refinement_execution_plan_boundary_audit_count",
        "carried_sigma_a_refinement_plan_boundary_audit_count",
        "carried_draft_sigma_a_refinement_execution_plan_boundary_audit_count",
        "carried_sigma_a_refinement_plan_boundary_audit_row_count",
        "carried_sigma_a_refinement_plan_boundary_preserved_count",
        "carried_planned_sigma_a_refinement_scope_audited_count",
        "carried_planned_time_index_layer_integration_audited_count",
        "carried_time_index_refinement_execution_count",
        "carried_t_a_refinement_execution_count",
        "carried_sigma_a_time_index_refinement_execution_count",
        "new_time_index_refinement_execution_count",
        "new_t_a_refinement_execution_count",
        "time_index_refinement_execution_count",
        "t_a_refinement_execution_count",
        "definition_execution_count",
        "new_definition_execution_count",
        "completed_formal_definition_count",
        "formalization_complete_count",
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
        "sigma_a_refinement_execution_count": "Sigma_A refinement execution count",
        "new_sigma_a_refinement_execution_count": "New Sigma_A refinement execution count",
        "draft_sigma_a_refinement_execution_count": "Draft Sigma_A refinement execution count",
        "executed_sigma_a_refinement_layer_count": "Executed Sigma_A refinement layer count",
        "refined_draft_sigma_a_shell_count": "Refined Draft Sigma_A shell count",
        "integrated_time_index_layer_count": "Integrated time-index layer count",
        "integrated_t_a_refinement_layer_count": "Integrated T_A refinement layer count",
        "draft_shell_refinement_link_executed_count": "Draft shell refinement link executed count",
        "carrier_clause_preserved_count": "Carrier clause preserved count",
        "dependent_object_slots_retained_as_deferred_count": "Dependent object slots retained as deferred count",
        "audit_traceability_carried_count": "Audit traceability carried count",
        "sigma_a_refinement_execution_row_count": "Sigma_A refinement execution row count",
        "sigma_a_refinement_execution_check_count": "Sigma_A refinement execution check count",
        "sigma_a_refinement_boundary_preserved_count": "Sigma_A refinement boundary preserved count",
        "carried_sigma_a_refinement_execution_plan_boundary_audit_count": "Carried Sigma_A refinement execution plan boundary audit count",
        "carried_sigma_a_refinement_plan_boundary_audit_count": "Carried Sigma_A refinement plan boundary audit count",
        "carried_draft_sigma_a_refinement_execution_plan_boundary_audit_count": "Carried Draft Sigma_A refinement execution plan boundary audit count",
        "carried_sigma_a_refinement_plan_boundary_audit_row_count": "Carried Sigma_A refinement plan boundary audit row count",
        "carried_sigma_a_refinement_plan_boundary_preserved_count": "Carried Sigma_A refinement plan boundary preserved count",
        "carried_planned_sigma_a_refinement_scope_audited_count": "Carried planned Sigma_A refinement scope audited count",
        "carried_planned_time_index_layer_integration_audited_count": "Carried planned time-index layer integration audited count",
        "carried_time_index_refinement_execution_count": "Carried time-index refinement execution count",
        "carried_t_a_refinement_execution_count": "Carried T_A refinement execution count",
        "carried_sigma_a_time_index_refinement_execution_count": "Carried Sigma_A time-index refinement execution count",
        "new_time_index_refinement_execution_count": "New time-index refinement execution count",
        "new_t_a_refinement_execution_count": "New T_A refinement execution count",
        "time_index_refinement_execution_count": "Time-index refinement execution count",
        "t_a_refinement_execution_count": "T_A refinement execution count",
        "definition_execution_count": "Definition execution count",
        "new_definition_execution_count": "New definition execution count",
        "completed_formal_definition_count": "Completed formal definition count",
        "formalization_complete_count": "Formalization complete count",
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
        "Sigma_A Refinement Execution v8.136",
        "Sigma_A refinement execution only",
        "Sigma_A refinement execution count: 1",
        "New Sigma_A refinement execution count: 1",
        "Draft Sigma_A refinement execution count: 1",
        "Executed Sigma_A refinement layer count: 1",
        "Refined Draft Sigma_A shell count: 1",
        "Integrated time-index layer count: 1",
        "Integrated T_A refinement layer count: 1",
        "Draft shell refinement link executed count: 1",
        "Carrier clause preserved count: 1",
        "Dependent object slots retained as deferred count: 6",
        "Sigma_A refinement execution row count: 8",
        "Sigma_A refinement execution check count: 8",
        "Sigma_A refinement boundary preserved count: 8",
        "Carried Sigma_A refinement execution plan boundary audit count: 1",
        "Carried Sigma_A refinement plan boundary audit count: 1",
        "Carried planned Sigma_A refinement scope audited count: 1",
        "Carried planned time-index layer integration audited count: 1",
        "New time-index refinement execution count: 0",
        "New T_A refinement execution count: 0",
        "Definition execution count: 0",
        "New definition execution count: 0",
        "Completed formal definition count: 0",
        "Formalization complete count: 0",
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
        "Interpretation: The v8.136 artifact executes bounded Sigma_A refinement while preserving zero counts for definition execution, "
        "Sigma_A completion, theorem candidate planning, theorem proof, proof assistant verification, validation, readiness, and citation claims."
    )
    print("Experiment 216 completed successfully.")
    print("V8_136_OFFICIAL_EXPERIMENT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
