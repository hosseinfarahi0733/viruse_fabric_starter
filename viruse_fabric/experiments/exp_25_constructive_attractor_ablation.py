from __future__ import annotations

from pathlib import Path

from viruse_fabric.validation.constructive_attractor_ablation import (
    ConstructiveAttractorAblationTester,
)


REQUIRED_REPORT_PHRASES = (
    "constructive attractor",
    "Ablation result",
    "Apparent targeting drop",
    "Observer misreading drop",
    "route shape alone",
    "conceptual and non-operational",
    "real pathogens",
    "real hosts",
    "laboratory procedures",
    "executable interventions",
)


def main() -> None:
    print("Experiment 25: Constructive Attractor Ablation")
    print("Question: Does apparent targeting collapse when constructive attractor support is removed?")

    tester = ConstructiveAttractorAblationTester()
    report = tester.run()

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
    print(f"Case count: {report.case_count}")
    print(f"Finding count: {report.finding_count}")
    print(f"Errors: {report.error_count}")
    print(f"Warnings: {report.warning_count}")
    print(f"Targeting drop percent: {report.targeting_drop_percent:.2f}")
    print(f"Misreading drop percent: {report.misreading_drop_percent:.2f}")
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
        raise SystemExit("constructive attractor ablation report was not generated")

    if report.error_count != 0:
        raise SystemExit("constructive attractor ablation produced errors")

    if report.targeting_drop_percent < tester.minimum_targeting_drop_percent:
        raise SystemExit("targeting drop did not pass the minimum threshold")

    if report.misreading_drop_percent < tester.minimum_misreading_drop_percent:
        raise SystemExit("observer misreading drop did not pass the minimum threshold")

    if missing_phrases:
        raise SystemExit(1)

    if not report.passed:
        raise SystemExit("constructive attractor ablation did not pass")

    print("Experiment 25 completed successfully.")


if __name__ == "__main__":
    main()
