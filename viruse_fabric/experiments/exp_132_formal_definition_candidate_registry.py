from __future__ import annotations

from viruse_fabric.writing.formal_definition_candidate_registry import run


def main() -> None:
    report = run()

    print("Experiment 132: Formal Definition Candidate Registry")
    print(
        "Question: Can Viruse Fabric register formal definition candidates from the v8.51 proof obligation registry while keeping completed formal definitions, proof execution, proof resolution, theorem proof, lemma proof, formalization completion, external validation, submission readiness, and new citation additions at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_path}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")

    print("Formal definition candidate registry count:", report.formal_definition_candidate_registry_count)
    print("Formal definition candidate registry row count:", report.formal_definition_candidate_registry_row_count)
    print("Registered formal definition candidate count:", report.registered_formal_definition_candidate_count)
    print("Unresolved formal definition candidate count:", report.unresolved_formal_definition_candidate_count)
    print("Completed formal definition candidate count:", report.completed_formal_definition_candidate_count)

    print("Carried proof obligation registry execution count:", report.carried_proof_obligation_registry_execution_count)
    print("Carried registered proof obligation count:", report.carried_registered_proof_obligation_count)
    print("Carried unresolved proof obligation count:", report.carried_unresolved_proof_obligation_count)
    print("Carried resolved proof obligation count:", report.carried_resolved_proof_obligation_count)
    print("Carried definition candidate count:", report.carried_definition_candidate_count)
    print("Carried theorem candidate count:", report.carried_theorem_candidate_count)
    print("Carried lemma candidate count:", report.carried_lemma_candidate_count)
    print("Proof strategy plan required count:", report.proof_strategy_plan_required_count)
    print("Theorem and lemma skeleton plan required count:", report.theorem_lemma_skeleton_plan_required_count)

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
        "Formal definition candidate registry count: 1",
        "Formal definition candidate registry row count: 2",
        "Registered formal definition candidate count: 2",
        "Unresolved formal definition candidate count: 2",
        "Completed formal definition candidate count: 0",
        "Carried proof obligation registry execution count: 1",
        "Carried registered proof obligation count: 6",
        "Carried unresolved proof obligation count: 6",
        "Carried resolved proof obligation count: 0",
        "Carried definition candidate count: 2",
        "Carried theorem candidate count: 2",
        "Carried lemma candidate count: 2",
        "Proof strategy plan required count: 1",
        "Theorem and lemma skeleton plan required count: 1",
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
        "Interpretation: The v8.52 artifact registers formal definition candidates while keeping formal definition completion, proof execution, proof resolution, theorem proof, lemma proof, formalization completion, external validation, independent experiment, submission readiness, readiness approval, and new citation additions at zero."
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

    print("Experiment 132 completed successfully.")


if __name__ == "__main__":
    main()
