from __future__ import annotations

from viruse_fabric.writing.formal_definition_completion_targeting_plan import run


def main() -> None:
    report = run()

    print("Experiment 138: Formal Definition Completion Targeting Plan")
    print(
        "Question: Can Viruse Fabric target formal definition completion work from the v8.57 manual proof attempt gap audit while keeping definition completion execution, proof gap resolution, theorem proof, lemma proof, formal mathematical proof, formal proof execution, external validation, submission readiness, and new citation additions at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_path}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")

    print("Formal definition completion targeting plan count:", report.formal_definition_completion_targeting_plan_count)
    print("Formal definition completion target row count:", report.formal_definition_completion_target_row_count)
    print("High-priority definition target count:", report.high_priority_definition_target_count)
    print("Medium-priority definition target count:", report.medium_priority_definition_target_count)
    print("Unresolved definition target count:", report.unresolved_definition_target_count)
    print("Completed definition target count:", report.completed_definition_target_count)
    print("Definition completion execution count:", report.definition_completion_execution_count)

    print("Carried manual proof attempt gap audit count:", report.carried_manual_proof_attempt_gap_audit_count)
    print("Carried proof attempt gap row count:", report.carried_proof_attempt_gap_row_count)
    print("Carried definition gap count:", report.carried_definition_gap_count)
    print("Carried assumption gap count:", report.carried_assumption_gap_count)
    print("Carried dependency gap count:", report.carried_dependency_gap_count)
    print("Carried boundary gap count:", report.carried_boundary_gap_count)
    print("Carried unresolved proof attempt gap count:", report.carried_unresolved_proof_attempt_gap_count)
    print("Carried resolved proof attempt gap count:", report.carried_resolved_proof_attempt_gap_count)
    print("Carried proof attempt gap resolution count:", report.carried_proof_attempt_gap_resolution_count)
    print("Carried successful theorem proof count:", report.carried_successful_theorem_proof_count)
    print("Carried successful lemma proof count:", report.carried_successful_lemma_proof_count)
    print("Carried registered formal definition candidate count:", report.carried_registered_formal_definition_candidate_count)
    print("Carried unresolved formal definition candidate count:", report.carried_unresolved_formal_definition_candidate_count)
    print("Carried completed formal definition candidate count:", report.carried_completed_formal_definition_candidate_count)

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
        "Formal definition completion targeting plan count: 1",
        "Formal definition completion target row count: 3",
        "High-priority definition target count: 2",
        "Medium-priority definition target count: 1",
        "Unresolved definition target count: 3",
        "Completed definition target count: 0",
        "Definition completion execution count: 0",
        "Carried manual proof attempt gap audit count: 1",
        "Carried proof attempt gap row count: 8",
        "Carried definition gap count: 3",
        "Carried assumption gap count: 2",
        "Carried dependency gap count: 1",
        "Carried boundary gap count: 2",
        "Carried unresolved proof attempt gap count: 8",
        "Carried resolved proof attempt gap count: 0",
        "Carried proof attempt gap resolution count: 0",
        "Carried successful theorem proof count: 0",
        "Carried successful lemma proof count: 0",
        "Carried registered formal definition candidate count: 2",
        "Carried unresolved formal definition candidate count: 2",
        "Carried completed formal definition candidate count: 0",
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
        "Interpretation: The v8.58 artifact targets formal definition completion work while keeping definition completion execution, proof gap resolution, theorem proof, lemma proof, formal mathematical proof, formal proof execution, external validation, independent experiment, submission readiness, readiness approval, and new citation additions at zero."
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

    print("Experiment 138 completed successfully.")


if __name__ == "__main__":
    main()
