from __future__ import annotations

from pathlib import Path

from viruse_fabric.demo.public_demo import PublicDemoPackage


REQUIRED_REPORT_PHRASES = (
    "public entry point",
    "Recommended inspection order",
    "Causality is not a chain; it is a geometry of constraints",
    "علیت زنجیره نیست؛ هندسه‌ی قیود است",
    "Safety boundary",
    "does not provide external empirical validation",
    "does not predict real biological outcomes",
    "does not claim that apparent targeting is real intention",
    "Demo commands",
    "python -m viruse_fabric.experiments.exp_20_theory_manifest",
    "python -m viruse_fabric.experiments.exp_21_visual_explanation",
    "python -m viruse_fabric.experiments.exp_22_scenario_stress_tests",
)


def main() -> None:
    print("Experiment 23: Public Demo Package")
    print("Question: Can the project provide a public-facing entry point for its current milestones and outputs?")

    package = PublicDemoPackage()
    report = package.build()

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
    print(f"Milestone count: {report.milestone_count}")
    print(f"Artifact count: {report.artifact_count}")
    print(f"Missing required artifacts: {report.missing_required_count}")
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
        raise SystemExit("public demo report was not generated")

    if report.missing_required_count != 0:
        raise SystemExit("public demo package is missing required artifacts")

    if missing_phrases:
        raise SystemExit(1)

    if not report.passed:
        raise SystemExit("public demo package did not pass")

    print("Experiment 23 completed successfully.")


if __name__ == "__main__":
    main()
