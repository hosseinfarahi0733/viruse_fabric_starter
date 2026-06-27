from __future__ import annotations

from viruse_fabric.writing.minimal_path_lemma_dependency_expansion import run


def main() -> None:
    report = run()

    print("Experiment 146: Minimal Path Lemma Dependency Expansion")
    print(
        "Question: Can Viruse Fabric expand the finite R-path proof kernel with three additional minimal manual lemma proofs while keeping theorem proof, proof assistant verification, formalization completion, definition completion execution, completed formal definitions, proof gap resolution, external validation, submission readiness, and new citation additions at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_path}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")

    print("Minimal path lemma dependency expansion count:", report.minimal_path_lemma_dependency_expansion_count)
    print("Dependency expansion kernel count:", report.dependency_expansion_kernel_count)
    print("New lemma statement count:", report.new_lemma_statement_count)
    print("New lemma proof execution count:", report.new_lemma_proof_execution_count)
    print("New lemma proven count:", report.new_lemma_proven_count)
    print("Carried lemma proven count:", report.carried_lemma_proven_count)
    print("Cumulative lemma proven count:", report.cumulative_lemma_proven_count)
    print("Theorem statement count:", report.theorem_statement_count)
    print("Theorem proven count:", report.theorem_proven_count)
    print("Proof assistant verification count:", report.proof_assistant_verification_count)
    print("Formalization complete count:", report.formalization_complete_count)

    print("Carried first minimal formal lemma proof execution count:", report.carried_first_minimal_formal_lemma_proof_execution_count)
    print("Carried formal definition kernel count:", report.carried_formal_definition_kernel_count)
    print("Carried lemma statement count:", report.carried_lemma_statement_count)
    print("Carried lemma proof execution count:", report.carried_lemma_proof_execution_count)
    print("Carried theorem proven count:", report.carried_theorem_proven_count)
    print("Carried proof assistant verification count:", report.carried_proof_assistant_verification_count)
    print("Carried formalization complete count:", report.carried_formalization_complete_count)
    print("Carried completed formal definition count:", report.carried_completed_formal_definition_count)
    print("Carried definition completion execution count:", report.carried_definition_completion_execution_count)
    print("Carried proof gap resolution count:", report.carried_proof_gap_resolution_count)
    print("Carried external validation count:", report.carried_external_validation_count)
    print("Carried new citation added count:", report.carried_new_citation_added_count)

    print("Completed formal definition count:", report.completed_formal_definition_count)
    print("Definition completion execution count:", report.definition_completion_execution_count)
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
        "Minimal path lemma dependency expansion count: 1",
        "Dependency expansion kernel count: 1",
        "New lemma statement count: 3",
        "New lemma proof execution count: 3",
        "New lemma proven count: 3",
        "Carried lemma proven count: 2",
        "Cumulative lemma proven count: 5",
        "Theorem statement count: 0",
        "Theorem proven count: 0",
        "Proof assistant verification count: 0",
        "Formalization complete count: 0",
        "Completed formal definition count: 0",
        "Definition completion execution count: 0",
        "Formal mathematical proof count: 0",
        "Formal proof execution count: 0",
        "Proof execution count: 1",
        "Proof gap resolution count: 0",
        "Manuscript submission ready count: 0",
        "Readiness approval count: 0",
        "External validation count: 0",
        "Independent experiment count: 0",
        "New citation added count: 0",
        "Carried first minimal formal lemma proof execution count: 1",
        "Carried formal definition kernel count: 1",
        "Carried lemma statement count: 2",
        "Carried lemma proof execution count: 2",
        "Carried theorem proven count: 0",
        "Carried proof assistant verification count: 0",
        "Carried formalization complete count: 0",
        "Carried completed formal definition count: 0",
        "Carried definition completion execution count: 0",
        "Carried proof gap resolution count: 0",
        "Carried external validation count: 0",
        "Carried new citation added count: 0",
    ]

    report_text = report.output_path.read_text(encoding="utf-8") if report.output_path.exists() else ""
    missing_required_report_phrases = [phrase for phrase in required if phrase not in report_text]
    print(f"Missing required report phrases: {len(missing_required_report_phrases)}")

    if missing_required_report_phrases:
        print("Missing required report phrase list:")
        for phrase in missing_required_report_phrases:
            print(f"- {phrase}")

    print(
        "Interpretation: The v8.66 artifact expands the finite R-path proof kernel with three additional minimal manual lemma proofs while keeping theorem proof, proof assistant verification, formalization completion, definition completion execution, completed formal definitions, proof gap resolution, external validation, independent experiment, submission readiness, readiness approval, and new citation additions at zero."
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

    print("Experiment 146 completed successfully.")


if __name__ == "__main__":
    main()
