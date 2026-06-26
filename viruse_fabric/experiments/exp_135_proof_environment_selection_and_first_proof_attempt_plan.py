from __future__ import annotations

from viruse_fabric.writing.proof_environment_selection_and_first_proof_attempt_plan import run


def main() -> None:
    report = run()

    print("Experiment 135: Proof Environment Selection and First Proof Attempt Plan")
    print(
        "Question: Can Viruse Fabric select a conservative proof environment and plan a first proof attempt route from the v8.54 proof strategy plan while keeping first proof attempt execution, proof execution, theorem proof, lemma proof, completed formal definitions, proof gap resolution, external validation, submission readiness, and new citation additions at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_path}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")

    print("Proof environment selection plan count:", report.proof_environment_selection_plan_count)
    print("Proof environment candidate count:", report.proof_environment_candidate_count)
    print("Selected proof environment count:", report.selected_proof_environment_count)
    print("Selected manual markdown environment count:", report.selected_manual_markdown_environment_count)
    print("Deferred formal assistant environment count:", report.deferred_formal_assistant_environment_count)
    print("First proof attempt plan count:", report.first_proof_attempt_plan_count)
    print("First proof attempt plan row count:", report.first_proof_attempt_plan_row_count)

    print("Carried proof strategy plan count:", report.carried_proof_strategy_plan_count)
    print("Carried proof strategy plan row count:", report.carried_proof_strategy_plan_row_count)
    print("Carried manual derivation track count:", report.carried_manual_derivation_track_count)
    print("Carried formal assistant readiness track count:", report.carried_formal_assistant_readiness_track_count)
    print("Carried counterexample audit track count:", report.carried_counterexample_audit_track_count)
    print("Carried boundary audit track count:", report.carried_boundary_audit_track_count)
    print("Carried proof environment selection required count:", report.carried_proof_environment_selection_required_count)
    print("Carried proof execution attempt plan required count:", report.carried_proof_execution_attempt_plan_required_count)

    print("Carried theorem skeleton count:", report.carried_theorem_skeleton_count)
    print("Carried lemma skeleton count:", report.carried_lemma_skeleton_count)
    print("Carried registered proof obligation count:", report.carried_registered_proof_obligation_count)
    print("Carried unresolved proof obligation count:", report.carried_unresolved_proof_obligation_count)
    print("Carried resolved proof obligation count:", report.carried_resolved_proof_obligation_count)
    print("Carried registered formal definition candidate count:", report.carried_registered_formal_definition_candidate_count)
    print("Carried unresolved formal definition candidate count:", report.carried_unresolved_formal_definition_candidate_count)
    print("Carried completed formal definition candidate count:", report.carried_completed_formal_definition_candidate_count)

    print("First proof attempt execution count:", report.first_proof_attempt_execution_count)
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
        "Proof environment selection plan count: 1",
        "Proof environment candidate count: 3",
        "Selected proof environment count: 1",
        "Selected manual markdown environment count: 1",
        "Deferred formal assistant environment count: 2",
        "First proof attempt plan count: 1",
        "First proof attempt plan row count: 4",
        "Carried proof strategy plan count: 1",
        "Carried proof strategy plan row count: 4",
        "Carried manual derivation track count: 1",
        "Carried formal assistant readiness track count: 1",
        "Carried counterexample audit track count: 1",
        "Carried boundary audit track count: 1",
        "Carried proof environment selection required count: 1",
        "Carried proof execution attempt plan required count: 1",
        "Carried theorem skeleton count: 2",
        "Carried lemma skeleton count: 2",
        "Carried registered proof obligation count: 6",
        "Carried unresolved proof obligation count: 6",
        "Carried resolved proof obligation count: 0",
        "Carried registered formal definition candidate count: 2",
        "Carried unresolved formal definition candidate count: 2",
        "Carried completed formal definition candidate count: 0",
        "First proof attempt execution count: 0",
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
        "Interpretation: The v8.55 artifact selects manual markdown derivation as the first proof environment and plans a first proof attempt route while keeping first proof attempt execution, proof execution, theorem proof, lemma proof, completed formal definitions, proof gap resolution, external validation, independent experiment, submission readiness, readiness approval, and new citation additions at zero."
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

    print("Experiment 135 completed successfully.")


if __name__ == "__main__":
    main()
