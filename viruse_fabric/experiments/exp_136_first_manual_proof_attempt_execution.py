from __future__ import annotations

from viruse_fabric.writing.first_manual_proof_attempt_execution import run


def main() -> None:
    report = run()

    print("Experiment 136: First Manual Proof Attempt Execution")
    print(
        "Question: Can Viruse Fabric record a first manual proof attempt execution as an attempt-level markdown derivation pass while keeping theorem proof, lemma proof, completed formal definitions, formal mathematical proof, formal proof execution, proof gap resolution, external validation, submission readiness, and new citation additions at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_path}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")

    print("First manual proof attempt execution count:", report.first_manual_proof_attempt_execution_count)
    print("Manual proof attempt row count:", report.manual_proof_attempt_row_count)
    print("Attempted lemma skeleton count:", report.attempted_lemma_skeleton_count)
    print("Attempted theorem skeleton count:", report.attempted_theorem_skeleton_count)
    print("Partial derivation note count:", report.partial_derivation_note_count)
    print("Unresolved attempt item count:", report.unresolved_attempt_item_count)
    print("Successful theorem proof count:", report.successful_theorem_proof_count)
    print("Successful lemma proof count:", report.successful_lemma_proof_count)

    print("Carried proof environment selection plan count:", report.carried_proof_environment_selection_plan_count)
    print("Carried selected manual markdown environment count:", report.carried_selected_manual_markdown_environment_count)
    print("Carried deferred formal assistant environment count:", report.carried_deferred_formal_assistant_environment_count)
    print("Carried first proof attempt plan count:", report.carried_first_proof_attempt_plan_count)
    print("Carried first proof attempt plan row count:", report.carried_first_proof_attempt_plan_row_count)
    print("Carried first proof attempt execution count:", report.carried_first_proof_attempt_execution_count)

    print("Carried theorem skeleton count:", report.carried_theorem_skeleton_count)
    print("Carried lemma skeleton count:", report.carried_lemma_skeleton_count)
    print("Carried registered proof obligation count:", report.carried_registered_proof_obligation_count)
    print("Carried unresolved proof obligation count:", report.carried_unresolved_proof_obligation_count)
    print("Carried resolved proof obligation count:", report.carried_resolved_proof_obligation_count)
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
        "First manual proof attempt execution count: 1",
        "Manual proof attempt row count: 4",
        "Attempted lemma skeleton count: 2",
        "Attempted theorem skeleton count: 2",
        "Partial derivation note count: 4",
        "Unresolved attempt item count: 4",
        "Successful theorem proof count: 0",
        "Successful lemma proof count: 0",
        "Carried proof environment selection plan count: 1",
        "Carried selected manual markdown environment count: 1",
        "Carried deferred formal assistant environment count: 2",
        "Carried first proof attempt plan count: 1",
        "Carried first proof attempt plan row count: 4",
        "Carried first proof attempt execution count: 0",
        "Carried theorem skeleton count: 2",
        "Carried lemma skeleton count: 2",
        "Carried registered proof obligation count: 6",
        "Carried unresolved proof obligation count: 6",
        "Carried resolved proof obligation count: 0",
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
        "Interpretation: The v8.56 artifact records a first manual proof attempt execution as an attempt-level markdown derivation pass while keeping theorem proof, lemma proof, completed formal definitions, formal mathematical proof, formal proof execution, proof gap resolution, external validation, independent experiment, submission readiness, readiness approval, and new citation additions at zero."
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

    print("Experiment 136 completed successfully.")


if __name__ == "__main__":
    main()
