from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.manuscript_integration_plan import ManuscriptIntegrationPlanBuilder


REQUIRED_REPORT_PHRASES = (
    "Manuscript Integration Plan",
    "Purpose",
    "Source Artifact Inventory",
    "Full Manuscript Draft v3.2",
    "Manuscript Quality Audit v3.3",
    "Related Work and Positioning Scaffold v3.4",
    "Formal Notation Scaffold v3.5",
    "Integration Map",
    "Warning Reduction Plan",
    "needs_related_work",
    "needs_formal_notation",
    "draft_not_submission_ready",
    "Formal Model Insertion",
    "F = (C, P, A, O)",
    "K(p, C)",
    "alpha(p, A)",
    "I_app",
    "I_false",
    "R(I_app)",
    "Related Work Insertion",
    "causal-chain models",
    "network causality",
    "dynamical systems",
    "constraint-based explanation",
    "observer-dependent interpretation",
    "teleology and apparent purpose",
    "model validation frameworks",
    "Revision Order",
    "Manuscript Boundaries",
    "does not establish external validation",
    "real pathogens",
    "real hosts",
    "biological protocols",
    "laboratory procedures",
    "executable interventions",
    "does not support strong public claims",
    "Next Actions",
    "Integration Status",
    "not submission-ready",
    "research prototype with internal validation",
)


def main() -> None:
    print("Experiment 36: Manuscript Integration Plan")
    print(
        "Question: Can the manuscript revision path integrate positioning and notation while responding to audit warnings?"
    )

    builder = ManuscriptIntegrationPlanBuilder()
    report = builder.run()

    report_path = Path(report.output_path)
    report_exists = report_path.exists()
    report_size = report_path.stat().st_size if report_exists else 0
    report_text = report_path.read_text(encoding="utf-8") if report_exists else ""

    missing_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES
        if phrase not in report_text
    ]

    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")
    print(f"Integration step count: {report.integration_step_count}")
    print(f"Warning action count: {report.warning_action_count}")
    print(f"Boundary count: {report.boundary_count}")
    print(f"Next action count: {report.next_action_count}")
    print(f"Word count: {report.word_count}")
    print(f"Errors: {report.error_count}")
    print(f"Warnings: {report.warning_count}")
    print(f"Passed: {report.passed}")
    print(f"Report exists: {report_exists}")
    print(f"Report size: {report_size}")
    print(f"Missing required report phrases: {len(missing_phrases)}")
    print(f"Interpretation: {report.interpretation}")

    if missing_phrases:
        print("Missing phrases:")
        for phrase in missing_phrases:
            print(f"- {phrase}")

    if not report_exists or report_size <= 0:
        raise SystemExit("manuscript integration plan report was not generated")

    if report.source_artifact_count < builder.minimum_source_artifact_count:
        raise SystemExit("too few source artifacts were listed")

    if report.missing_source_artifact_count != 0:
        raise SystemExit("some source artifacts are missing")

    if report.integration_step_count < builder.minimum_integration_step_count:
        raise SystemExit("too few integration steps were generated")

    if report.warning_action_count < builder.minimum_warning_action_count:
        raise SystemExit("too few warning actions were generated")

    if report.boundary_count < 8:
        raise SystemExit("too few manuscript boundaries were generated")

    if report.next_action_count < 6:
        raise SystemExit("too few next actions were generated")

    if report.word_count < builder.minimum_word_count:
        raise SystemExit("manuscript integration plan is too short")

    if report.error_count != 0:
        raise SystemExit("manuscript integration plan produced errors")

    if missing_phrases:
        raise SystemExit(1)

    if not report.passed:
        raise SystemExit("manuscript integration plan did not pass")

    print("Experiment 36 completed successfully.")


if __name__ == "__main__":
    main()
