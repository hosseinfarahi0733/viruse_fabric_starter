from __future__ import annotations

from pathlib import Path

from viruse_fabric.validation.validation_protocol import ValidationProtocolBuilder


REQUIRED_REPORT_PHRASES = (
    "conceptual-computational research prototype",
    "identify what would make it fail",
    "Constructive attractor ablation",
    "Tension well injection",
    "Parameter sensitivity sweep",
    "Baseline comparison",
    "Negative control scenarios",
    "External validation boundary",
    "research prototype only",
    "does not use real pathogens",
    "laboratory protocols",
    "executable biological procedures",
)


def main() -> None:
    print("Experiment 24: Validation Protocol")
    print("Question: Can the project define what would strengthen, weaken, or falsify its current claims?")

    builder = ValidationProtocolBuilder()
    report = builder.build()

    report_path = Path(report.output_path)
    report_text = report_path.read_text(encoding="utf-8")

    missing_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES
        if phrase not in report_text
    ]

    report_exists = report_path.exists()
    report_size = report_path.stat().st_size if report_exists else 0

    print(f"Title: {report.title}")
    print(f"Output path: {report.output_path}")
    print(f"Criterion count: {report.criterion_count}")
    print(f"High priority count: {report.high_priority_count}")
    print(f"Failure condition count: {report.failure_condition_count}")
    print(f"Presentation status: {report.presentation_status}")
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
        raise SystemExit("validation protocol report was not generated")

    if report.criterion_count < 8:
        raise SystemExit("validation protocol has too few criteria")

    if report.high_priority_count < 5:
        raise SystemExit("validation protocol has too few high-priority criteria")

    if report.failure_condition_count < 6:
        raise SystemExit("validation protocol has too few failure conditions")

    if report.presentation_status != "research prototype only":
        raise SystemExit("presentation status is too strong")

    if missing_phrases:
        raise SystemExit(1)

    if not report.passed:
        raise SystemExit("validation protocol did not pass")

    print("Experiment 24 completed successfully.")


if __name__ == "__main__":
    main()
