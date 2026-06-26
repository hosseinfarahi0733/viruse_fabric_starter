from __future__ import annotations

from viruse_fabric.writing.proof_obligation_registry_execution import run


def main() -> None:
    report = run()

    print("Experiment 131: Proof Obligation Registry Execution")
    print(
        "Question: Can Viruse Fabric execute a proof obligation registry from the v8.50 proof-track plan while keeping proof execution, proof resolution, theorem proof, lemma proof, completed formal definitions, external validation, submission readiness, and new citation additions at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_path}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")

    print("Proof obligation registry execution count:", report.proof_obligation_registry_execution_count)
    print("Proof obligation registry row count:", report.proof_obligation_registry_row_count)
    print("Registered proof obligation count:", report.registered_proof_obligation_count)
    print("Unresolved proof obligation count:", report.unresolved_proof_obligation_count)
    print("Resolved proof obligation count:", report.resolved_proof_obligation_count)
    print("Proof obligation plan count:", report.proof_obligation_plan_count)
    print("Proof obligation plan source row count:", report.proof_obligation_plan_source_row_count)
    print("Controlled formal proof track entry plan count:", report.formal_proof_track_entry_plan_count)
    print("Theorem candidate count:", report.theorem_candidate_count)
    print("Lemma candidate count:", report.lemma_candidate_count)
    print("Definition candidate count:", report.definition_candidate_count)
    print("Proof strategy plan required count:", report.proof_strategy_plan_required_count)
    print("Formal definition candidate registry required count:", report.formal_definition_candidate_registry_required_count)

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
        "Proof obligation registry execution count: 1",
        "Proof obligation registry row count: 6",
        "Registered proof obligation count: 6",
        "Unresolved proof obligation count: 6",
        "Resolved proof obligation count: 0",
        "Proof obligation plan count: 1",
        "Proof obligation plan source row count: 6",
        "Controlled formal proof track entry plan count: 1",
        "Theorem candidate count: 2",
        "Lemma candidate count: 2",
        "Definition candidate count: 2",
        "Proof strategy plan required count: 1",
        "Formal definition candidate registry required count: 1",
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
        "Interpretation: The v8.51 artifact executes a proof obligation registry while keeping all proof execution, proof resolution, theorem proof, lemma proof, formalization completion, external validation, independent experiment, submission readiness, readiness approval, and new citation additions at zero."
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

    print("Experiment 131 completed successfully.")


if __name__ == "__main__":
    main()
