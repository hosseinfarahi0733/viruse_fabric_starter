from __future__ import annotations

from pathlib import Path

from viruse_fabric.validation.adversarial_sensitivity import AdversarialSensitivitySweeper


REQUIRED_REPORT_PHRASES = (
    "adversarial sensitivity sweep",
    "hostile but interpretable configurations",
    "decoy cases",
    "Minimum adversarial stability rate",
    "Minimum supported-route margin",
    "Cases tested",
    "Profiles tested",
    "Stable profiles",
    "Unstable profiles",
    "Stability rate",
    "Top-case counts",
    "Failure reason counts",
    "Closest adversarial runs",
    "Warnings identify fragile regions",
    "conceptual and non-operational",
    "real pathogens",
    "real hosts",
    "laboratory procedures",
    "executable interventions",
)


def main() -> None:
    print("Experiment 27: Adversarial Sensitivity Sweep")
    print(
        "Question: Does the model remain usable under hostile weight settings and decoy pressure?"
    )

    sweeper = AdversarialSensitivitySweeper()
    report = sweeper.run()

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
        raise SystemExit("adversarial sensitivity report was not generated")

    if report.case_count < 7:
        raise SystemExit("too few adversarial cases were tested")

    if report.profile_count < 8000:
        raise SystemExit("too few adversarial profiles were tested")

    if report.stability_rate < sweeper.minimum_stability_rate:
        raise SystemExit("adversarial stability rate did not pass the minimum threshold")

    if report.error_count != 0:
        raise SystemExit("adversarial sensitivity sweep produced errors")

    if missing_phrases:
        raise SystemExit(1)

    if not report.passed:
        raise SystemExit("adversarial sensitivity sweep did not pass")

    print("Experiment 27 completed successfully.")


if __name__ == "__main__":
    main()
