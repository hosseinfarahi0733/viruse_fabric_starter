from __future__ import annotations

from viruse_fabric.writing.formal_definition_completion_execution_authorization import run


def main() -> None:
    report = run()

    print("Experiment 140: Formal Definition Completion Execution Authorization")
    print(
        "Question: Can Viruse Fabric execute controlled authorization for one later formal definition completion execution target from the v8.59 authorization plan while keeping definition completion execution, completed formal definitions, theorem proof, lemma proof, formal mathematical proof, formal proof execution, proof gap resolution, external validation, submission readiness, and new citation additions at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_path}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")

    print("Formal definition completion execution authorization execution count:", report.formal_definition_completion_execution_authorization_execution_count)
    print("Authorization execution row count:", report.authorization_execution_row_count)
    print("Selected authorization execution candidate count:", report.selected_authorization_execution_candidate_count)
    print("Deferred authorization execution candidate count:", report.deferred_authorization_execution_candidate_count)
    print("Definition completion execution authorized count:", report.definition_completion_execution_authorized_count)
    print("Definition completion execution count:", report.definition_completion_execution_count)

    print("Carried formal definition completion execution authorization plan count:", report.carried_authorization_plan_count)
    print("Carried authorization plan row count:", report.carried_authorization_plan_row_count)
    print("Carried selected execution candidate count:", report.carried_selected_execution_candidate_count)
    print("Carried deferred execution candidate count:", report.carried_deferred_execution_candidate_count)
    print("Carried authorization execution required count:", report.carried_authorization_execution_required_count)
    print("Carried authorization execution count:", report.carried_authorization_execution_count)
    print("Carried definition completion execution count:", report.carried_definition_completion_execution_count)
    print("Carried definition gap count:", report.carried_definition_gap_count)
    print("Carried successful theorem proof count:", report.carried_successful_theorem_proof_count)
    print("Carried successful lemma proof count:", report.carried_successful_lemma_proof_count)

    print("Formal definition completion approval execution count:", report.formal_definition_completion_approval_execution_count)
    print("Formal definition completion approved count:", report.formal_definition_completion_approved_count)
    print("Formal definition completed count:", report.formal_definition_completed_count)
    print("Formal mathematical proof count:", report.formal_mathematical_proof_count)
    print("Formal proof execution count:", report.formal_proof_execution_count)
    print("Proof execution count:", report.proof_execution_count)
    print("Theorem proven count:", report.theorem_proven_count)
    print("Lemma proven count:", report.lemma_proven_count)
    print("Formalization complete count:", report.formalization_complete_count)
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
        "Formal definition completion execution authorization execution count: 1",
        "Authorization execution row count: 3",
        "Selected authorization execution candidate count: 1",
        "Deferred authorization execution candidate count: 2",
        "Definition completion execution authorized count: 1",
        "Definition completion execution count: 0",
        "Carried formal definition completion execution authorization plan count: 1",
        "Carried authorization plan row count: 3",
        "Carried selected execution candidate count: 1",
        "Carried deferred execution candidate count: 2",
        "Carried authorization execution required count: 1",
        "Carried authorization execution count: 0",
        "Carried definition completion execution count: 0",
        "Carried definition gap count: 3",
        "Carried successful theorem proof count: 0",
        "Carried successful lemma proof count: 0",
        "Formal definition completed count: 0",
        "Formal mathematical proof count: 0",
        "Formal proof execution count: 0",
        "Proof execution count: 0",
        "Theorem proven count: 0",
        "Lemma proven count: 0",
        "Formalization complete count: 0",
        "Proof gap resolution count: 0",
        "Manuscript submission ready count: 0",
        "Readiness approval count: 0",
        "External validation count: 0",
        "Independent experiment count: 0",
        "New citation added count: 0",
    ]

    report_text = report.output_path.read_text(encoding="utf-8") if report.output_path.exists() else ""
    missing_required_report_phrases = [phrase for phrase in required if phrase not in report_text]
    print(f"Missing required report phrases: {len(missing_required_report_phrases)}")

    if missing_required_report_phrases:
        print("Missing required report phrase list:")
        for phrase in missing_required_report_phrases:
            print(f"- {phrase}")

    print(
        "Interpretation: The v8.60 artifact executes controlled authorization for one later formal definition completion execution target while keeping definition completion execution, completed formal definitions, theorem proof, lemma proof, formal mathematical proof, formal proof execution, proof gap resolution, external validation, independent experiment, submission readiness, readiness approval, and new citation additions at zero."
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

    print("Experiment 140 completed successfully.")


if __name__ == "__main__":
    main()
