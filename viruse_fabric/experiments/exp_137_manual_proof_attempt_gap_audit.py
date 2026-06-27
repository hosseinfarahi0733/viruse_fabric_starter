from __future__ import annotations

from viruse_fabric.writing.manual_proof_attempt_gap_audit import run


def main() -> None:
    report = run()

    print("Experiment 137: Manual Proof Attempt Gap Audit")
    print(
        "Question: Can Viruse Fabric audit gaps from the v8.56 first manual proof attempt while keeping proof gap resolution, theorem proof, lemma proof, completed formal definitions, formal mathematical proof, formal proof execution, external validation, submission readiness, and new citation additions at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_path}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")

    print("Manual proof attempt gap audit count:", report.manual_proof_attempt_gap_audit_count)
    print("Audited manual proof attempt row count:", report.audited_manual_proof_attempt_row_count)
    print("Proof attempt gap row count:", report.proof_attempt_gap_row_count)
    print("Definition gap count:", report.definition_gap_count)
    print("Assumption gap count:", report.assumption_gap_count)
    print("Dependency gap count:", report.dependency_gap_count)
    print("Boundary gap count:", report.boundary_gap_count)
    print("Unresolved proof attempt gap count:", report.unresolved_proof_attempt_gap_count)
    print("Resolved proof attempt gap count:", report.resolved_proof_attempt_gap_count)
    print("Proof attempt gap resolution count:", report.proof_attempt_gap_resolution_count)

    print("Carried first manual proof attempt execution count:", report.carried_first_manual_proof_attempt_execution_count)
    print("Carried manual proof attempt row count:", report.carried_manual_proof_attempt_row_count)
    print("Carried attempted lemma skeleton count:", report.carried_attempted_lemma_skeleton_count)
    print("Carried attempted theorem skeleton count:", report.carried_attempted_theorem_skeleton_count)
    print("Carried partial derivation note count:", report.carried_partial_derivation_note_count)
    print("Carried unresolved attempt item count:", report.carried_unresolved_attempt_item_count)
    print("Carried successful theorem proof count:", report.carried_successful_theorem_proof_count)
    print("Carried successful lemma proof count:", report.carried_successful_lemma_proof_count)

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
        "Manual proof attempt gap audit count: 1",
        "Audited manual proof attempt row count: 4",
        "Proof attempt gap row count: 8",
        "Definition gap count: 3",
        "Assumption gap count: 2",
        "Dependency gap count: 1",
        "Boundary gap count: 2",
        "Unresolved proof attempt gap count: 8",
        "Resolved proof attempt gap count: 0",
        "Proof attempt gap resolution count: 0",
        "Carried first manual proof attempt execution count: 1",
        "Carried manual proof attempt row count: 4",
        "Carried attempted lemma skeleton count: 2",
        "Carried attempted theorem skeleton count: 2",
        "Carried partial derivation note count: 4",
        "Carried unresolved attempt item count: 4",
        "Carried successful theorem proof count: 0",
        "Carried successful lemma proof count: 0",
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
        "Interpretation: The v8.57 artifact audits manual proof attempt gaps while keeping proof gap resolution, theorem proof, lemma proof, completed formal definitions, formal mathematical proof, formal proof execution, external validation, independent experiment, submission readiness, readiness approval, and new citation additions at zero."
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

    print("Experiment 137 completed successfully.")


if __name__ == "__main__":
    main()
