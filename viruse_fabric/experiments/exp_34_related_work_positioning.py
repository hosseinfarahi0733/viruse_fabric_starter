from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.related_work_positioning import RelatedWorkPositioningBuilder


REQUIRED_REPORT_PHRASES = (
    "Related Work and Positioning Scaffold",
    "Purpose",
    "Plain-Language Clarification",
    "A constraint is any abstract condition",
    "Constraint geometry",
    "Why Constraints Matter",
    "Positioning Logic",
    "Glossary for Positioning",
    "Conceptual Neighbor Families",
    "Linear causal-chain models",
    "Network causality",
    "Dynamical systems",
    "Constraint-based explanation",
    "Observer-dependent interpretation",
    "Teleology and apparent purpose",
    "Model validation and stress testing",
    "Positioning Statement",
    "research prototype",
    "internal validation",
    "does not provide real citations",
    "does not establish external validation",
    "real pathogens",
    "real hosts",
    "biological protocols",
    "laboratory procedures",
    "executable interventions",
    "Recommendations",
    "Next Manuscript Step",
    "formal notation",
)


def main() -> None:
    print("Experiment 34: Related Work and Positioning Scaffold")
    print(
        "Question: Can the manuscript position Viruse Fabric against neighboring conceptual families while clarifying constraints?"
    )

    builder = RelatedWorkPositioningBuilder()
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
    print(f"Family count: {report.family_count}")
    print(f"Distinction count: {report.distinction_count}")
    print(f"Glossary count: {report.glossary_count}")
    print(f"Boundary count: {report.boundary_count}")
    print(f"Recommendation count: {report.recommendation_count}")
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
        raise SystemExit("related work positioning report was not generated")

    if report.family_count < builder.minimum_family_count:
        raise SystemExit("too few conceptual families were generated")

    if report.distinction_count < builder.minimum_family_count:
        raise SystemExit("too few distinctions were generated")

    if report.glossary_count < builder.minimum_glossary_count:
        raise SystemExit("too few glossary entries were generated")

    if report.boundary_count < 6:
        raise SystemExit("too few boundaries were generated")

    if report.recommendation_count < 6:
        raise SystemExit("too few recommendations were generated")

    if report.word_count < builder.minimum_word_count:
        raise SystemExit("related work positioning scaffold is too short")

    if report.error_count != 0:
        raise SystemExit("related work positioning produced errors")

    if missing_phrases:
        raise SystemExit(1)

    if not report.passed:
        raise SystemExit("related work positioning did not pass")

    print("Experiment 34 completed successfully.")


if __name__ == "__main__":
    main()
