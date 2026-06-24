from __future__ import annotations

from pathlib import Path

from viruse_fabric.validation.validation_synthesis import ValidationSynthesisBuilder


REQUIRED_REPORT_PHRASES = (
    "Validation Synthesis and Research Readiness",
    "Executive Summary",
    "research prototype with internal validation",
    "Overall readiness score",
    "Validation Milestones",
    "Claims Supported by the Current Evidence",
    "Claims Not Supported Yet",
    "Milestone-Level Interpretation",
    "Readiness Scores",
    "External validation has not been completed",
    "Research Boundary",
    "conceptual and non-operational",
    "real pathogens",
    "real hosts",
    "biological protocols",
    "laboratory procedures",
    "executable interventions",
    "Final Readiness Statement",
    "not yet ready for strong public claims",
)


def main() -> None:
    print("Experiment 30: Validation Synthesis and Research Readiness")
    print(
        "Question: What can Viruse Fabric responsibly claim after the internal validation sequence?"
    )

    builder = ValidationSynthesisBuilder()
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
    print(f"Milestone count: {report.milestone_count}")
    print(f"Implemented validation count: {report.implemented_validation_count}")
    print(f"Passed validation count: {report.passed_validation_count}")
    print(f"Total errors: {report.total_errors}")
    print(f"Total warnings: {report.total_warnings}")
    print(f"Missing report count: {report.missing_report_count}")
    print(f"Readiness score: {report.readiness_score}")
    print(f"Research status: {report.research_status}")
    print(f"Finding count: {report.finding_count}")
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
        raise SystemExit("validation synthesis report was not generated")

    if report.milestone_count < builder.minimum_milestones:
        raise SystemExit("too few validation milestones were summarized")

    if report.implemented_validation_count < builder.minimum_implemented_validations:
        raise SystemExit("too few implemented validation tests were summarized")

    if report.passed_validation_count != report.implemented_validation_count:
        raise SystemExit("not all implemented validation tests passed")

    if report.total_errors != 0:
        raise SystemExit("summarized validation sequence contains errors")

    if report.missing_report_count != 0:
        raise SystemExit("some validation report files are missing")

    if report.readiness_score < builder.minimum_readiness_score:
        raise SystemExit("research readiness score is below the required prototype threshold")

    if report.error_count != 0:
        raise SystemExit("validation synthesis produced errors")

    if missing_phrases:
        raise SystemExit(1)

    if not report.passed:
        raise SystemExit("validation synthesis did not pass")

    print("Experiment 30 completed successfully.")


if __name__ == "__main__":
    main()
