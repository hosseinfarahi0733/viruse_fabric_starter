from __future__ import annotations

from pathlib import Path

from viruse_fabric.validation.projection_perturbation import ProjectionPerturbationTester


REQUIRED_REPORT_PHRASES = (
    "projection perturbation",
    "observer projection profiles",
    "intrinsic fabric scoring fixed",
    "apparent targeting and observer misreading remain distinguishable",
    "Decision rule",
    "Target-like threshold",
    "False-intention threshold",
    "Minimum supported intrinsic margin",
    "Minimum observer false-intention events",
    "Maximum corrected false-intention events",
    "Minimum correction drop percent",
    "Intrinsic false positives",
    "Observer false-intention events",
    "Corrected false-intention events",
    "Correction drop percent",
    "Case-level intrinsic scores",
    "Projection runs",
    "conceptual and non-operational",
    "real pathogens",
    "real hosts",
    "laboratory procedures",
    "executable interventions",
)


def main() -> None:
    print("Experiment 29: Projection Perturbation")
    print(
        "Question: Do projection shifts change observer misreading while intrinsic fabric scoring remains discriminative?"
    )

    tester = ProjectionPerturbationTester()
    report = tester.run()

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
    print(f"Projection count: {report.projection_count}")
    print(f"Run count: {report.run_count}")
    print(f"Intrinsic false positives: {report.intrinsic_false_positive_count}")
    print(f"Observer false intentions: {report.observer_false_intention_count}")
    print(f"Corrected false intentions: {report.corrected_false_intention_count}")
    print(f"Correction drop percent: {report.correction_drop_percent:.2f}")
    print(f"Supported intrinsic margin: {report.supported_intrinsic_margin:.2f}")
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
        raise SystemExit("projection perturbation report was not generated")

    if report.case_count < 6:
        raise SystemExit("too few projection cases were tested")

    if report.projection_count < 6:
        raise SystemExit("too few projection profiles were tested")

    if report.run_count < 36:
        raise SystemExit("too few projection runs were tested")

    if report.intrinsic_false_positive_count != 0:
        raise SystemExit("intrinsic fabric scoring produced false positives")

    if report.observer_false_intention_count < tester.minimum_observer_false_intention_count:
        raise SystemExit("projection perturbation did not produce enough observer false-intention events")

    if report.corrected_false_intention_count > tester.maximum_corrected_false_intention_count:
        raise SystemExit("correction left too many false-intention events")

    if report.correction_drop_percent < tester.minimum_correction_drop_percent:
        raise SystemExit("correction drop percent was too low")

    if report.supported_intrinsic_margin < tester.minimum_supported_intrinsic_margin:
        raise SystemExit("supported intrinsic margin was too low")

    if report.error_count != 0:
        raise SystemExit("projection perturbation produced errors")

    if missing_phrases:
        raise SystemExit(1)

    if not report.passed:
        raise SystemExit("projection perturbation did not pass")

    print("Experiment 29 completed successfully.")


if __name__ == "__main__":
    main()
