from __future__ import annotations

from viruse_fabric.writing.drafted_formal_definition_boundary_audit import run


def main() -> None:
    report = run()

    print("Experiment 142: Drafted Formal Definition Boundary Audit")
    print(
        "Question: Can Viruse Fabric audit boundary issues in the v8.61 drafted formal definition items while keeping all draft boundary issues unresolved and keeping definition completion execution, completed formal definitions, theorem proof, lemma proof, formal mathematical proof, formal proof execution, proof gap resolution, external validation, submission readiness, and new citation additions at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_path}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")

    print("Drafted formal definition boundary audit count:", report.drafted_formal_definition_boundary_audit_count)
    print("Audited drafted definition item count:", report.audited_drafted_definition_item_count)
    print("Draft boundary issue count:", report.draft_boundary_issue_count)
    print("Domain boundary issue count:", report.domain_boundary_issue_count)
    print("Axiom boundary issue count:", report.axiom_boundary_issue_count)
    print("Semantic boundary issue count:", report.semantic_boundary_issue_count)
    print("Dependency boundary issue count:", report.dependency_boundary_issue_count)
    print("Unresolved draft boundary issue count:", report.unresolved_draft_boundary_issue_count)
    print("Resolved draft boundary issue count:", report.resolved_draft_boundary_issue_count)
    print("Completed definition item count:", report.completed_definition_item_count)
    print("Completed formal definition count:", report.completed_formal_definition_count)
    print("Definition completion execution count:", report.definition_completion_execution_count)
    print("Formal definition completion audit required count:", report.formal_definition_completion_audit_required_count)

    print("Carried controlled formal definition drafting execution count:", report.carried_controlled_formal_definition_drafting_execution_count)
    print("Carried drafted definition package count:", report.carried_drafted_definition_package_count)
    print("Carried drafted definition item count:", report.carried_drafted_definition_item_count)
    print("Carried drafted signature count:", report.carried_drafted_signature_count)
    print("Carried unresolved drafting boundary count:", report.carried_unresolved_drafting_boundary_count)
    print("Carried completed definition item count:", report.carried_completed_definition_item_count)
    print("Carried completed formal definition count:", report.carried_completed_formal_definition_count)
    print("Carried formal definition completion audit required count:", report.carried_formal_definition_completion_audit_required_count)
    print("Carried definition completion execution count:", report.carried_definition_completion_execution_count)
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
        "Drafted formal definition boundary audit count: 1",
        "Audited drafted definition item count: 5",
        "Draft boundary issue count: 10",
        "Domain boundary issue count: 3",
        "Axiom boundary issue count: 3",
        "Semantic boundary issue count: 2",
        "Dependency boundary issue count: 2",
        "Unresolved draft boundary issue count: 10",
        "Resolved draft boundary issue count: 0",
        "Completed definition item count: 0",
        "Completed formal definition count: 0",
        "Definition completion execution count: 0",
        "Formal definition completion audit required count: 1",
        "Carried controlled formal definition drafting execution count: 1",
        "Carried drafted definition package count: 1",
        "Carried drafted definition item count: 5",
        "Carried drafted signature count: 5",
        "Carried unresolved drafting boundary count: 5",
        "Carried completed definition item count: 0",
        "Carried completed formal definition count: 0",
        "Carried formal definition completion audit required count: 1",
        "Carried definition completion execution count: 0",
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
        "Interpretation: The v8.62 artifact audits boundary issues in drafted formal definition items while keeping all draft boundary issues unresolved and keeping definition completion execution, completed formal definitions, theorem proof, lemma proof, formal mathematical proof, formal proof execution, proof gap resolution, external validation, independent experiment, submission readiness, readiness approval, and new citation additions at zero."
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

    print("Experiment 142 completed successfully.")


if __name__ == "__main__":
    main()
