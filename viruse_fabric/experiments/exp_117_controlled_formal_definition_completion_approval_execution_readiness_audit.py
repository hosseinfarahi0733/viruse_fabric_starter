from __future__ import annotations

from viruse_fabric.writing.controlled_formal_definition_completion_approval_execution_readiness_audit import run


def main() -> None:
    report = run()

    print("Experiment 117: Controlled Formal Definition Completion Approval Execution Readiness Audit")
    print(
        "Question: Can Viruse Fabric audit readiness for controlled formal definition completion approval execution while keeping approval execution, approval readiness approval, formal definition completion approval, completed formal definitions, proof execution, formal proof, theorem proof, lemma proof, formalization completion, submission readiness, external validation, and new citation additions at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_path}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")
    print(
        "Controlled formal definition completion approval execution readiness audit count:",
        report.readiness_audit_count,
    )
    print(
        "Controlled formal definition completion approval execution readiness audit row count:",
        report.readiness_audit_row_count,
    )
    print(
        "Controlled formal definition completion approval execution plan source row count:",
        report.approval_execution_plan_source_row_count,
    )
    print(
        "Controlled formal definition completion approval execution plan count:",
        report.approval_execution_plan_count,
    )
    print("Approval execution readiness approved count:", report.approval_execution_readiness_approved_count)
    print("Approval execution transition approved count:", report.approval_execution_transition_approved_count)
    print(
        "Formal definition completion approval execution count:",
        report.formal_definition_completion_approval_execution_count,
    )
    print("Formal definition completion approved count:", report.formal_definition_completion_approved_count)
    print("Formal definition completed count:", report.formal_definition_completed_count)
    print("Formal mathematical proof count:", report.formal_mathematical_proof_count)
    print("Proof execution count:", report.proof_execution_count)
    print("Theorem proven count:", report.theorem_proven_count)
    print("Lemma proven count:", report.lemma_proven_count)
    print("Formalization complete count:", report.formalization_complete_count)
    print("Proof gap resolution count:", report.proof_gap_resolution_count)
    print("Manuscript submission ready count:", report.manuscript_submission_ready_count)
    print("Readiness approval count:", report.readiness_approval_count)
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
        "Controlled formal definition completion approval execution readiness audit count: 1",
        "Controlled formal definition completion approval execution readiness audit row count: 4",
        "Controlled formal definition completion approval execution plan source row count: 4",
        "Approval execution readiness approved count: 0",
        "Approval execution transition approved count: 0",
        "Formal definition completion approval execution count: 0",
        "Formal definition completion approved count: 0",
        "Formal definition completed count: 0",
        "Formal mathematical proof count: 0",
        "Proof execution count: 0",
        "Theorem proven count: 0",
        "Lemma proven count: 0",
        "Formalization complete count: 0",
        "Manuscript submission ready count: 0",
        "Readiness approval count: 0",
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
        "Interpretation: The v8.37 artifact audits readiness for a future controlled formal definition completion approval execution milestone while keeping approval execution, approval readiness approval, formal definition completion approval, completed formal definitions, proof execution, formal mathematical proof, theorem proof, lemma proof, formalization completion, submission readiness, readiness approval, and new citation additions at zero."
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

    print("Experiment 117 completed successfully.")


if __name__ == "__main__":
    main()
