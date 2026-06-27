from __future__ import annotations

from viruse_fabric.writing.mutual_reachability_equivalence_theorem_attempt import run


def main() -> None:
    report = run()

    print("Experiment 152: Mutual Reachability Equivalence Theorem Attempt")
    print(
        "Question: Can Viruse Fabric prove that mutual finite R-path reachability is an equivalence relation while keeping proof assistant verification, completed formalization, completed definitions, framework-level proof, proof gap resolution, external validation, submission readiness, and new citation additions at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_path}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")

    print("Mutual reachability equivalence theorem attempt count:", report.mutual_reachability_equivalence_theorem_attempt_count)
    print("Theorem attempt count:", report.theorem_attempt_count)
    print("Theorem statement count:", report.theorem_statement_count)
    print("Theorem proof execution count:", report.theorem_proof_execution_count)
    print("New theorem proven count:", report.new_theorem_proven_count)
    print("Carried cumulative limited theorem proven count:", report.carried_cumulative_limited_theorem_proven_count)
    print("Cumulative limited theorem proven count:", report.cumulative_limited_theorem_proven_count)
    print("Mutual reachability relation definition count:", report.mutual_reachability_relation_definition_count)
    print("Equivalence property count:", report.equivalence_property_count)
    print("Theorem dependency count:", report.theorem_dependency_count)

    print("Carried reachability preorder theorem attempt count:", report.carried_reachability_preorder_theorem_attempt_count)
    print("Carried reachability relation definition count:", report.carried_reachability_relation_definition_count)
    print("Carried preorder property count:", report.carried_preorder_property_count)
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
        "Mutual reachability equivalence theorem attempt count: 1",
        "Theorem attempt count: 1",
        "Theorem statement count: 1",
        "Theorem proof execution count: 1",
        "New theorem proven count: 1",
        "Carried cumulative limited theorem proven count: 3",
        "Cumulative limited theorem proven count: 4",
        "Mutual reachability relation definition count: 1",
        "Equivalence property count: 3",
        "Theorem dependency count: 1",
        "Proof assistant verification count: 0",
        "Formalization complete count: 0",
        "Completed formal definition count: 0",
        "Definition completion execution count: 0",
        "Full framework formal proof count: 0",
        "Formal mathematical proof count: 0",
        "Formal proof execution count: 0",
        "Proof execution count: 1",
        "Proof gap resolution count: 0",
        "Manuscript submission ready count: 0",
        "Readiness approval count: 0",
        "External validation count: 0",
        "Independent experiment count: 0",
        "New citation added count: 0",
        "Carried reachability preorder theorem attempt count: 1",
        "Carried reachability relation definition count: 1",
        "Carried preorder property count: 2",
        "Carried new theorem proven count: 1",
        "Carried proof execution count: 1",
        "Carried proof assistant verification count: 0",
        "Carried formalization complete count: 0",
        "Carried completed formal definition count: 0",
        "Carried definition completion execution count: 0",
        "Carried full framework formal proof count: 0",
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
        "Interpretation: The v8.72 artifact proves one additional limited theorem showing mutual finite R-path reachability is an equivalence relation while keeping proof assistant verification, completed formalization, completed definitions, framework-level proof, proof gap resolution, external validation, independent experiment, submission readiness, readiness approval, and new citation additions at zero."
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

    print("Experiment 152 completed successfully.")


if __name__ == "__main__":
    main()
