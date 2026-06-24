from __future__ import annotations

from pathlib import Path

from viruse_fabric.validation.scenario_stress_tester import ScenarioStressTester


REQUIRED_REPORT_PHRASES = (
    "stress-tests the internal logic",
    "does not validate the model against external empirical data",
    "coherent constructive routes may appear target-like",
    "tension wells",
    "unsupported routes",
    "strained gateways",
    "conceptual and non-operational",
    "real pathogens",
    "real hosts",
    "executable interventions",
)


def main() -> None:
    print("Experiment 22: Scenario Stress Tests")
    print("Question: Can the project reject broken scenarios without flattening valid ones?")

    tester = ScenarioStressTester()
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
    print(f"Scenario count: {report.scenario_count}")
    print(f"Finding count: {report.finding_count}")
    print(f"Errors: {report.error_count}")
    print(f"Warnings: {report.warning_count}")
    print(f"Rejected invalid scenarios: {report.rejected_invalid_count}")
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
        raise SystemExit("stress test report was not generated")

    if missing_phrases:
        raise SystemExit(1)

    if report.error_count != 0:
        raise SystemExit("stress test produced errors")

    if report.rejected_invalid_count < 2:
        raise SystemExit("invalid scenarios were not rejected strongly enough")

    if not report.passed:
        raise SystemExit("scenario stress test did not pass")

    print("Experiment 22 completed successfully.")


if __name__ == "__main__":
    main()
