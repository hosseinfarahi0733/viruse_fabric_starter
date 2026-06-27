from __future__ import annotations

from viruse_fabric.writing.attractor_class_scaffold_boundary_audit import run


def main() -> None:
    report = run()

    print("Experiment 157: Attractor Class Scaffold Boundary Audit")
    print(
        "Question: Can Viruse Fabric audit the attractor-class candidate scaffold created in v8.76 while keeping new scaffold creation, theorem proof, proof execution, proof assistant verification, completed formalization, completed definitions, framework-level proof, proof gap resolution, external validation, submission readiness, and new citation additions at zero?"
    )
    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact: {report.source_path}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")

    print("Attractor class scaffold boundary audit count:", report.attractor_class_scaffold_boundary_audit_count)
    print("Audited scaffold count:", report.audited_scaffold_count)
    print("Scaffold boundary row count:", report.scaffold_boundary_row_count)
    print("Allowed claim count:", report.allowed_claim_count)
    print("Blocked claim count:", report.blocked_claim_count)

    print("New bridge execution count:", report.new_bridge_execution_count)
    print("New attractor class candidate scaffold count:", report.new_attractor_class_candidate_scaffold_count)
    print("New theorem proven count:", report.new_theorem_proven_count)
    print("Proof execution count:", report.proof_execution_count)
    print("Attractor class theorem attempt count:", report.attractor_class_theorem_attempt_count)
    print("Attractor class theorem proven count:", report.attractor_class_theorem_proven_count)
    print("Attractor class definition completion count:", report.attractor_class_definition_completion_count)
    print("Constraint region definition completion count:", report.constraint_region_definition_completion_count)
    print("Causal mass definition completion count:", report.causal_mass_definition_completion_count)
    print("Observer projection definition completion count:", report.observer_projection_definition_completion_count)

    print("Carried attractor class bridge execution count:", report.carried_attractor_class_bridge_execution_count)
    print("Carried authorized bridge consumed count:", report.carried_authorized_bridge_consumed_count)
    print("Carried attractor class candidate scaffold count:", report.carried_attractor_class_candidate_scaffold_count)
    print("Carried quotient carrier count:", report.carried_quotient_carrier_count)
    print("Carried stabilization predicate placeholder count:", report.carried_stabilization_predicate_placeholder_count)
    print("Carried bridge boundary row count:", report.carried_bridge_boundary_row_count)
    print("Carried attractor class theorem attempt count:", report.carried_attractor_class_theorem_attempt_count)
    print("Carried attractor class theorem proven count:", report.carried_attractor_class_theorem_proven_count)
    print("Carried attractor class definition completion count:", report.carried_attractor_class_definition_completion_count)
    print("Carried constraint region definition completion count:", report.carried_constraint_region_definition_completion_count)
    print("Carried causal mass definition completion count:", report.carried_causal_mass_definition_completion_count)
    print("Carried observer projection definition completion count:", report.carried_observer_projection_definition_completion_count)
    print("Carried cumulative limited theorem proven count:", report.carried_cumulative_limited_theorem_proven_count)
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

    print("Cumulative limited theorem proven count:", report.cumulative_limited_theorem_proven_count)
    print("Proof assistant verification count:", report.proof_assistant_verification_count)
    print("Formalization complete count:", report.formalization_complete_count)
    print("Completed formal definition count:", report.completed_formal_definition_count)
    print("Definition completion execution count:", report.definition_completion_execution_count)
    print("Full framework formal proof count:", report.full_framework_formal_proof_count)
    print("Formal mathematical proof count:", report.formal_mathematical_proof_count)
    print("Formal proof execution count:", report.formal_proof_execution_count)
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
        "Attractor class scaffold boundary audit count: 1",
        "Audited scaffold count: 1",
        "Scaffold boundary row count: 6",
        "Allowed claim count: 6",
        "Blocked claim count: 6",
        "New bridge execution count: 0",
        "New attractor class candidate scaffold count: 0",
        "New theorem proven count: 0",
        "Proof execution count: 0",
        "Attractor class theorem attempt count: 0",
        "Attractor class theorem proven count: 0",
        "Attractor class definition completion count: 0",
        "Constraint region definition completion count: 0",
        "Causal mass definition completion count: 0",
        "Observer projection definition completion count: 0",
        "Cumulative limited theorem proven count: 5",
        "Proof assistant verification count: 0",
        "Formalization complete count: 0",
        "Completed formal definition count: 0",
        "Definition completion execution count: 0",
        "Full framework formal proof count: 0",
        "Formal mathematical proof count: 0",
        "Formal proof execution count: 0",
        "Proof gap resolution count: 0",
        "Manuscript submission ready count: 0",
        "Readiness approval count: 0",
        "External validation count: 0",
        "Independent experiment count: 0",
        "New citation added count: 0",
        "Carried attractor class bridge execution count: 1",
        "Carried authorized bridge consumed count: 1",
        "Carried attractor class candidate scaffold count: 1",
        "Carried quotient carrier count: 1",
        "Carried stabilization predicate placeholder count: 1",
        "Carried bridge boundary row count: 6",
        "Carried attractor class theorem attempt count: 0",
        "Carried attractor class theorem proven count: 0",
        "Carried attractor class definition completion count: 0",
        "Carried constraint region definition completion count: 0",
        "Carried causal mass definition completion count: 0",
        "Carried observer projection definition completion count: 0",
        "Carried cumulative limited theorem proven count: 5",
        "Carried new theorem proven count: 0",
        "Carried proof execution count: 0",
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
        "Interpretation: The v8.77 artifact audits the attractor-class candidate scaffold created in v8.76 while keeping new scaffold creation, theorem proof, proof execution, proof assistant verification, completed formalization, completed definitions, framework-level proof, proof gap resolution, external validation, independent experiment, submission readiness, readiness approval, and new citation additions at zero."
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

    print("Experiment 157 completed successfully.")


if __name__ == "__main__":
    main()
