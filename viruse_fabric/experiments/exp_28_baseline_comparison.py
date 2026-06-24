from __future__ import annotations

from pathlib import Path

from viruse_fabric.validation.baseline_comparison import BaselineComparator


REQUIRED_REPORT_PHRASES = (
    "baseline comparison",
    "route-shape baseline",
    "observer-salience baseline",
    "efficiency baseline",
    "reduced linear baseline",
    "Decision rule",
    "Target-like threshold",
    "Minimum Viruse Fabric separation margin",
    "Negative controls should not cross the target-like threshold",
    "Model summary",
    "Case scores",
    "False positive count",
    "Passed discrimination",
    "A useful baseline test should expose false positive behavior in simpler models",
    "conceptual and non-operational",
    "real pathogens",
    "real hosts",
    "laboratory procedures",
    "executable interventions",
)


def main() -> None:
    print("Experiment 28: Baseline Comparison")
    print("Question: Does Viruse Fabric explain the target-like case better than simpler baselines?")

    comparator = BaselineComparator()
    report = comparator.run()

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
    print(f"Model count: {report.model_count}")
    print(f"Baseline count: {report.baseline_count}")
    print(f"Baseline failure count: {report.baseline_failure_count}")
    print(f"Fabric margin: {report.fabric_margin:.2f}")
    print(f"Fabric false positives: {report.fabric_false_positive_count}")
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
        raise SystemExit("baseline comparison report was not generated")

    if report.case_count < 7:
        raise SystemExit("too few baseline comparison cases were tested")

    if report.model_count < 5:
        raise SystemExit("too few models were compared")

    if report.baseline_count < 4:
        raise SystemExit("too few baselines were compared")

    if report.baseline_failure_count < comparator.minimum_baseline_failure_count:
        raise SystemExit("not enough baselines were weaker than Viruse Fabric")

    if report.fabric_false_positive_count != 0:
        raise SystemExit("Viruse Fabric produced false positives")

    if report.fabric_margin < comparator.minimum_fabric_margin:
        raise SystemExit("Viruse Fabric separation margin was too low")

    if report.error_count != 0:
        raise SystemExit("baseline comparison produced errors")

    if missing_phrases:
        raise SystemExit(1)

    if not report.passed:
        raise SystemExit("baseline comparison did not pass")

    print("Experiment 28 completed successfully.")


if __name__ == "__main__":
    main()
