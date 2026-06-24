from __future__ import annotations

from pathlib import Path

from viruse_fabric.validation.parameter_sensitivity import ParameterSensitivitySweeper


REQUIRED_REPORT_PHRASES = (
    "sensitivity sweep",
    "moderate scoring-weight perturbations",
    "Minimum stability rate",
    "Profiles tested",
    "Stability rate",
    "supported constructive route remains dominant",
    "disrupted or unsupported cases",
    "conceptual and non-operational",
    "real pathogens",
    "real hosts",
    "laboratory procedures",
    "executable interventions",
)


def main() -> None:
    print("Experiment 26: Parameter Sensitivity Sweep")
    print("Question: Does the main validation result remain stable under moderate weight perturbations?")

    sweeper = ParameterSensitivitySweeper()
    report = sweeper.run()

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
    print(f"Profile count: {report.profile_count}")
    print(f"Stable count: {report.stable_count}")
    print(f"Unstable count: {report.unstable_count}")
    print(f"Stability rate: {report.stability_rate:.2%}")
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
        raise SystemExit("parameter sensitivity report was not generated")

    if report.profile_count < 100:
        raise SystemExit("too few sensitivity profiles were tested")

    if report.stability_rate < sweeper.minimum_stability_rate:
        raise SystemExit("stability rate did not pass the minimum threshold")

    if report.error_count != 0:
        raise SystemExit("parameter sensitivity sweep produced errors")

    if missing_phrases:
        raise SystemExit(1)

    if not report.passed:
        raise SystemExit("parameter sensitivity sweep did not pass")

    print("Experiment 26 completed successfully.")


if __name__ == "__main__":
    main()
