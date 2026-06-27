from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.sigma_a_carrier_type_selection_decision_execution import (
    SigmaACarrierTypeSelectionDecisionExecutionBuilder,
)


def main() -> int:
    builder = SigmaACarrierTypeSelectionDecisionExecutionBuilder()
    report = builder.run()

    output = Path(report.output_path)

    print("Experiment 190: Sigma_A Carrier-Type Selection Decision Execution")
    print(
        "Question: Can Viruse Fabric execute a bounded Sigma_A carrier-type selection decision after boundary planning while keeping "
        "carrier refinement execution, Sigma_A refinement execution, new draft execution, definition execution, Sigma_A definition completion, "
        "theorem candidate planning, theorem proof, proof assistant verification, external validation, independent experiment, submission readiness, "
        "readiness approval, and new citation additions at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_artifact}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")
    print(f"Sigma_A carrier-type selection decision execution count: {report.sigma_a_carrier_type_selection_decision_execution_count}")
    print(f"Carrier type selection count: {report.carrier_type_selection_count}")
    print(f"Carrier type selection decision count: {report.carrier_type_selection_decision_count}")
    print(f"Carrier type selection execution count: {report.carrier_type_selection_execution_count}")
    print(f"Candidate carrier option considered count: {report.candidate_carrier_option_considered_count}")
    print(f"Selection criterion applied count: {report.selection_criterion_applied_count}")
    print(f"Selected carrier type count: {report.selected_carrier_type_count}")
    print(f"Selected typed-product carrier count: {report.selected_typed_product_carrier_count}")
    print(f"Non-selected carrier type count: {report.non_selected_carrier_type_count}")
    print(f"Auxiliary structured-schema representation count: {report.auxiliary_structured_schema_representation_count}")
    print(f"Carrier selection rationale row count: {report.carrier_selection_rationale_row_count}")
    print(f"Carried Sigma_A carrier-type selection decision boundary plan count: {report.carried_sigma_a_carrier_type_selection_decision_boundary_plan_count}")
    print(f"Carried selection boundary criterion count: {report.carried_selection_boundary_criterion_count}")
    print(f"Carried selection decision question count: {report.carried_selection_decision_question_count}")
    print(f"Carried candidate carrier option count: {report.carried_candidate_carrier_option_count}")
    print(f"Carried Sigma_A carrier-type option audit execution count: {report.carried_sigma_a_carrier_type_option_audit_execution_count}")
    print(f"Carried carrier type option audited count: {report.carried_carrier_type_option_audited_count}")
    print(f"Carried Sigma_A carrier time-index refinement plan count: {report.carried_sigma_a_carrier_time_index_refinement_plan_count}")
    print(f"Carried Sigma_A draft consistency boundary audit count: {report.carried_sigma_a_draft_consistency_boundary_audit_count}")
    print(f"Core formal object inventory execution count: {report.core_formal_object_inventory_execution_count}")
    print(f"Core formal object count: {report.core_formal_object_count}")
    print(f"Formal object inventory execution count: {report.formal_object_inventory_execution_count}")
    print(f"Resolved gap count: {report.resolved_gap_count}")
    print(f"Unresolved gap count: {report.unresolved_gap_count}")
    print(f"Remaining blocking gap count: {report.remaining_blocking_gap_count}")
    print(f"Conditional hold count: {report.conditional_hold_count}")
    print(f"Carrier type refinement execution count: {report.carrier_type_refinement_execution_count}")
    print(f"Carrier refinement execution count: {report.carrier_refinement_execution_count}")
    print(f"Time-index refinement execution count: {report.time_index_refinement_execution_count}")
    print(f"Sigma_A refinement execution count: {report.sigma_a_refinement_execution_count}")
    print(f"New Sigma_A draft clause count: {report.new_sigma_a_draft_clause_count}")
    print(f"New definition draft execution count: {report.new_definition_draft_execution_count}")
    print(f"Definition inventory execution count: {report.definition_inventory_execution_count}")
    print(f"Definition execution count: {report.definition_execution_count}")
    print(f"New definition execution count: {report.new_definition_execution_count}")
    print(f"Completed formal definition count: {report.completed_formal_definition_count}")
    print(f"Formalization complete count: {report.formalization_complete_count}")
    print(f"Sigma_A definition completion count: {report.sigma_a_definition_completion_count}")
    print(f"Stabilization predicate definition completion count: {report.stabilization_predicate_definition_completion_count}")
    print(f"Attractor class definition completion count: {report.attractor_class_definition_completion_count}")
    print(f"Constraint region definition completion count: {report.constraint_region_definition_completion_count}")
    print(f"Causal mass definition completion count: {report.causal_mass_definition_completion_count}")
    print(f"Observer projection definition completion count: {report.observer_projection_definition_completion_count}")
    print(f"Completion decision plan count: {report.completion_decision_plan_count}")
    print(f"Completion decision count: {report.completion_decision_count}")
    print(f"Completion execution count: {report.completion_execution_count}")
    print(f"Completion execution authorized count: {report.completion_execution_authorized_count}")
    print(f"Theorem candidate plan count: {report.theorem_candidate_plan_count}")
    print(f"New theorem proven count: {report.new_theorem_proven_count}")
    print(f"Cumulative limited theorem proven count: {report.cumulative_limited_theorem_proven_count}")
    print(f"Proof assistant verification count: {report.proof_assistant_verification_count}")
    print(f"Formal mathematical proof count: {report.formal_mathematical_proof_count}")
    print(f"Formal proof execution count: {report.formal_proof_execution_count}")
    print(f"Proof execution count: {report.proof_execution_count}")
    print(f"Proof gap resolution count: {report.proof_gap_resolution_count}")
    print(f"Definition completion execution count: {report.definition_completion_execution_count}")
    print(f"Full framework formal proof count: {report.full_framework_formal_proof_count}")
    print(f"Manuscript submission ready count: {report.manuscript_submission_ready_count}")
    print(f"Readiness approval count: {report.readiness_approval_count}")
    print(f"External validation count: {report.external_validation_count}")
    print(f"Independent experiment count: {report.independent_experiment_count}")
    print(f"New citation added count: {report.new_citation_added_count}")
    print(f"Hard zero count: {report.hard_zero_count}")
    print(f"Boundary phrase count: {report.boundary_phrase_count}")
    print(f"Prohibited behavior count: {report.prohibited_behavior_count}")
    print(f"Next step count: {report.next_step_count}")
    print(f"Overclaim count: {report.overclaim_count}")
    print(f"Invented citation-like pattern count: {report.invented_citation_like_pattern_count}")
    print(f"Word count: {report.word_count}")
    print(f"Errors: {report.error_count}")
    print(f"Warnings: {report.warning_count}")
    print(f"Passed: {report.passed}")
    print(f"Report exists: {output.exists()}")
    print(f"Report size: {output.stat().st_size if output.exists() else 0}")

    required_phrases = [
        "Sigma_A Carrier-Type Selection Decision Execution v8.110",
        "Selected carrier type: typed-product carrier",
        "Auxiliary explanatory representation retained: structured-schema carrier",
        "Sigma_A carrier-type selection decision execution count: 1",
        "Carrier type selection count: 1",
        "Carrier type selection decision count: 1",
        "Carrier type selection execution count: 1",
        "Candidate carrier option considered count: 5",
        "Selection criterion applied count: 8",
        "Selected carrier type count: 1",
        "Selected typed-product carrier count: 1",
        "Non-selected carrier type count: 4",
        "Carrier type refinement execution count: 0",
        "Carrier refinement execution count: 0",
        "Time-index refinement execution count: 0",
        "Sigma_A refinement execution count: 0",
        "New Sigma_A draft clause count: 0",
        "New definition draft execution count: 0",
        "Definition execution count: 0",
        "Sigma_A definition completion count: 0",
        "Completed formal definition count: 0",
        "Theorem candidate plan count: 0",
        "New theorem proven count: 0",
        "Proof assistant verification count: 0",
        "External validation count: 0",
        "Manuscript submission ready count: 0",
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

    if missing:
        return 1

    if not report.passed:
        return 1

    print(
        "Interpretation: The v8.110 artifact selects typed-product carrier for future Sigma_A refinement while preserving zero counts for "
        "carrier refinement execution, Sigma_A refinement execution, new draft execution, definition execution, Sigma_A completion, theorem candidate planning, "
        "theorem proof, proof assistant verification, validation, readiness, and citation claims."
    )
    print("Experiment 190 completed successfully.")
    print("V8_110_OFFICIAL_EXPERIMENT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
