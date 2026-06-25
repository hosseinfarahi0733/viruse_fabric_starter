from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.formal_notation_scaffold import FormalNotationScaffoldBuilder


REQUIRED_REPORT_PHRASES = (
    "Formal Notation Scaffold",
    "Purpose",
    "Core Formal Object",
    "F = (C, P, A, O)",
    "constraint set",
    "path space",
    "constructive attractor set",
    "observer projection",
    "Working Definitions",
    "A constraint is any abstract condition",
    "Constraint geometry",
    "Path compatibility",
    "constructive attractor",
    "Apparent intentionality",
    "False intentionality",
    "Projection correction",
    "Notation Table",
    "Formal Relations",
    "K(p, C)",
    "alpha(p, A)",
    "I_app",
    "I_false",
    "R(I_app)",
    "Delta_R",
    "Interpretive Flow",
    "constraints -> compatible paths -> attractor concentration -> observer projection -> apparent intentionality",
    "Minimal Example Logic",
    "Manuscript Boundaries",
    "not a formal proof",
    "not a complete mathematical theory",
    "not externally validated",
    "real pathogens",
    "real hosts",
    "biological protocols",
    "laboratory procedures",
    "executable interventions",
    "does not support strong public claims",
    "Recommendations",
    "Next Manuscript Step",
)


def main() -> None:
    print("Experiment 35: Formal Notation Scaffold")
    print(
        "Question: Can Viruse Fabric be given a cautious symbolic vocabulary without pretending to be a completed proof?"
    )

    builder = FormalNotationScaffoldBuilder()
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
    print(f"Notation count: {report.notation_count}")
    print(f"Relation count: {report.relation_count}")
    print(f"Definition count: {report.definition_count}")
    print(f"Boundary count: {report.boundary_count}")
    print(f"Example count: {report.example_count}")
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
        raise SystemExit("formal notation scaffold report was not generated")

    if report.notation_count < builder.minimum_notation_count:
        raise SystemExit("too few notation entries were generated")

    if report.relation_count < builder.minimum_relation_count:
        raise SystemExit("too few formal relations were generated")

    if report.definition_count < builder.minimum_definition_count:
        raise SystemExit("too few definitions were generated")

    if report.boundary_count < 7:
        raise SystemExit("too few boundaries were generated")

    if report.example_count < 4:
        raise SystemExit("too few examples were generated")

    if report.word_count < builder.minimum_word_count:
        raise SystemExit("formal notation scaffold is too short")

    if report.error_count != 0:
        raise SystemExit("formal notation scaffold produced errors")

    if missing_phrases:
        raise SystemExit(1)

    if not report.passed:
        raise SystemExit("formal notation scaffold did not pass")

    print("Experiment 35 completed successfully.")


if __name__ == "__main__":
    main()
