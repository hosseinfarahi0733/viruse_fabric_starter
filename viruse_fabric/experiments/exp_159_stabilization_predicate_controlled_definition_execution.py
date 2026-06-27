from __future__ import annotations

from viruse_fabric.writing.stabilization_predicate_controlled_definition_execution import run


def main() -> None:
    report = run()

    print("Experiment 159: Stabilization Predicate Controlled Definition Execution")
    print(
        "Question: Can Viruse Fabric execute a controlled draft clause set for Sigma_A while keeping predicate definition completion, attractor-class definition completion, theorem proof, proof execution, proof assistant verification, completed formalization, framework-level proof, external validation, submission readiness, and new citation additions at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_path}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")

    print("Stabilization predicate controlled definition execution count:", report.stabilization_predicate_controlled_definition_execution_count)
    print("Definition execution count:", report.definition_execution_count)
    print("Stabilization predicate draft clause count:", report.stabilization_predicate_draft_clause_count)
    print("Carrier domain clause count:", report.carrier_domain_clause_count)
    print("Local persistence clause count:", report.local_persistence_clause_count)
    print("Recurrence clause count:", report.recurrence_clause_count)
    print("Exclusion clause count:", report.exclusion_clause_count)
    print("Audit dependency clause count:", report.audit_dependency_clause_count)
    print("Stabilization predicate definition completion count:", report.stabilization_predicate_definition_completion_count)
    print("Attractor class definition completion count:", report.attractor_class_definition_completion_count)
    print("Constraint region definition completion count:", report.constraint_region_definition_completion_count)
    print("Causal mass definition completion count:", report.causal_mass_definition_completion_count)
    print("Observer projection definition completion count:", report.observer_projection_definition_completion_count)

    print("Carried stabilization predicate definition plan count:", report.carried_stabilization_predicate_definition_plan_count)
    print("Carried stabilization predicate requirement row count:", report.carried_stabilization_predicate_requirement_row_count)
    print("Carried selected predicate placeholder count:", report.carried_selected_predicate_placeholder_count)
    print("Carried planned predicate symbol count:", report.carried_planned_predicate_symbol_count)
    print("Carried planned definition target count:", report.carried_planned_definition_target_count)
    print("Carried definition execution count:", report.carried_definition_execution_count)
    print("Carried stabilization predicate definition completion count:", report.carried_stabilization_predicate_definition_completion_count)
    print("Carried attractor class definition completion count:", report.carried_attractor_class_definition_completion_count)
    print("Carried constraint region definition completion count:", report.carried_constraint_region_definition_completion_count)
    print("Carried causal mass definition completion count:", report.carried_causal_mass_definition_completion_count)
    print("Carried observer projection definition completion count:", report.carried_observer_projection_definition_completion_count)
    print("Carried new theorem proven count:", report.carried_new_theorem_proven_count)
    print("Carried proof execution count:", report.carried_proof_execution_count)
    print("Carried proof assistant verification count:", report.carried_proof_assistant_verification_count)
    print("Carried formalization complete count:", report.carried_formalization_complete_count)
    print("Carried completed formal definition count:", report.carried_completed_formal_definition_count)
    print("Carried definition completion execution count:", report.carried_definition_completion_execution_count)
    print("Carried full framework formal proof count:", report.carried_full_framework_formal_proof_count)
    print("Carried proof gap resolution count:", report.carried_proof_gap_resolution_count)
    print("Carried external validation count:", report.carried_external_validation_count)
    print("Carried new citation added count:", report.carried_new_citation_added_count)
    print("Carried cumulative limited theorem proven count:", report.carried_cumulative_limited_theorem_proven_count)

    print("New theorem proven count:", report.new_theorem_proven_count)
    print("Cumulative limited theorem proven count:", report.cumulative_limited_theorem_proven_count)
    print("Proof assistant verification count:", report.proof_assistant_verification_count)
    print("Formalization complete count:", report.formalization_complete_count)
    print("Completed formal definition count:", report.completed_formal_definition_count)
    print("Definition completion execution count:", report.definition_completion_execution_count)
    print("Full framework formal proof count:", report.full_framework_formal_proof_count)
    print("Formal mathematical proof count:", report.formal_mathematical_proof_count)
    print("Formal proof execution count:", report.formal_proof_execution_count)
    print("Proof execution count:", report.proof_execution_count)
    print("Proof gap resolution count:", report.proof_gap_resolution_count)
    print("Manuscript submission ready count:", report.manuscript_submission_ready_count)
    print("Readiness approval count:", report.readiness_approval_count)
    print("External validation count:", report.external_validation_count)
    print("Independent experiment count:", report.independent_experiment_count)
    print("New citation added count:", report.new_citation_added_count)

    print("Conditional hold count:", report.conditional_hold_count)
    print("Hard zero count:", report.hard_zero_count)
    print("Boundary phrase count:", report.boundary_phrase_count)
    print("Prohibited behavior count:", report.prohibited_behavior_count)
    print("Next step count:", report.next_step_count)
    print("Overclaim count:", report.overclaim_count)
    print("Invented citation-like pattern count:", report.invented_citation_like_pattern_count)
    print(f"Word count: {report.word_count}")
    print(f"Errors: {len(report.errors)}")
    print(f"Warnings: {len(report.warnings)}")
    print(f"Passed: {report.passed}")
    print(f"Report exists: {report.output_path.exists()}")
    print(f"Report size: {report.output_path.stat().st_size if report.output_path.exists() else 0}")

    required = [
        "Stabilization predicate controlled definition execution count: 1",
        "Definition execution count: 1",
        "Stabilization predicate draft clause count: 6",
        "Carrier domain clause count: 1",
        "Local persistence clause count: 1",
        "Recurrence clause count: 1",
        "Exclusion clause count: 1",
        "Audit dependency clause count: 1",
        "Stabilization predicate definition completion count: 0",
        "Attractor class definition completion count: 0",
        "Constraint region definition completion count: 0",
        "Causal mass definition completion count: 0",
        "Observer projection definition completion count: 0",
        "New theorem proven count: 0",
        "Cumulative limited theorem proven count: 5",
        "Proof assistant verification count: 0",
        "Formalization complete count: 0",
        "Completed formal definition count: 0",
        "Definition completion execution count: 0",
        "Full framework formal proof count: 0",
        "Formal mathematical proof count: 0",
        "Formal proof execution count: 0",
        "Proof execution count: 0",
        "Proof gap resolution count: 0",
        "Manuscript submission ready count: 0",
        "Readiness approval count: 0",
        "External validation count: 0",
        "Independent experiment count: 0",
        "New citation added count: 0",
        "Carried stabilization predicate definition plan count: 1",
        "Carried stabilization predicate requirement row count: 6",
        "Carried selected predicate placeholder count: 1",
        "Carried planned predicate symbol count: 1",
        "Carried planned definition target count: 1",
        "Carried definition execution count: 0",
        "Carried stabilization predicate definition completion count: 0",
        "Carried attractor class definition completion count: 0",
        "Carried constraint region definition completion count: 0",
        "Carried causal mass definition completion count: 0",
        "Carried observer projection definition completion count: 0",
        "Carried new theorem proven count: 0",
        "Carried proof execution count: 0",
        "Carried proof assistant verification count: 0",
        "Carried formalization complete count: 0",
        "Carried completed formal definition count: 0",
        "Carried definition completion execution count: 0",
        "Carried full framework formal proof count: 0",
        "Carried proof gap resolution count: 0",
        "Carried external validation count: 0",
        "Carried new citation added count: 0",
        "Carried cumulative limited theorem proven count: 5",
    ]

    report_text = report.output_path.read_text(encoding="utf-8") if report.output_path.exists() else ""
    missing_required_report_phrases = [phrase for phrase in required if phrase not in report_text]
    print(f"Missing required report phrases: {len(missing_required_report_phrases)}")

    if missing_required_report_phrases:
        print("Missing required report phrase list:")
        for phrase in missing_required_report_phrases:
            print(f"- {phrase}")

    print(
        "Interpretation: The v8.79 artifact executes a controlled draft clause set for Sigma_A while keeping predicate definition completion, attractor-class definition completion, theorem proof, proof execution, proof assistant verification, completed formalization, framework-level proof, external validation, independent experiment, submission readiness, readiness approval, and new citation additions at zero."
    )

    if report.warnings:
        print("Warnings:")
        for warning in report.warnings:
            print(f"- {warning}")

    if report.errors:
        print("Errors:")
        for error in report.errors:
            print(f"- {error}")

    if missing_required_report_phrases:
        raise SystemExit(1)

    if not report.passed:
        raise SystemExit(1)

    print("Experiment 159 completed successfully.")


if __name__ == "__main__":
    main()
