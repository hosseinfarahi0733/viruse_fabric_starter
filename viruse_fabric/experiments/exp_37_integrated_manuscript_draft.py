from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.integrated_manuscript_draft import IntegratedManuscriptDraftBuilder


REQUIRED_REPORT_PHRASES = (
    "Integrated Manuscript Draft",
    "Manuscript Status",
    "Integration Rationale",
    "Working Title",
    "Abstract",
    "Introduction",
    "Plain-Language Constraint Clarification",
    "Related Work and Positioning",
    "Linear causal-chain models",
    "Network causality",
    "Dynamical systems",
    "Constraint-based explanation",
    "Observer-dependent interpretation",
    "Teleology and apparent purpose",
    "Model validation and stress testing",
    "Core Thesis",
    "Formal Model",
    "F = (C, P, A, O)",
    "K(p, C)",
    "alpha(p, A)",
    "I_app",
    "I_false",
    "R(I_app)",
    "Delta_R",
    "Interpretive Flow",
    "Validation Mapping",
    "Compact Validation Results",
    "v2.5 Constructive Attractor Ablation",
    "v2.6 Parameter Sensitivity",
    "v2.7 Adversarial Sensitivity",
    "v2.8 Baseline Comparison",
    "v2.9 Projection Perturbation",
    "v3.0 Validation Synthesis",
    "v3.3 Manuscript Quality Audit",
    "Results Interpretation",
    "Limitations",
    "Allowed and Disallowed Claims",
    "Future Work",
    "Human-AI Work Note",
    "Source Artifact Inventory",
    "Research Boundary",
    "Conclusion",
    "research prototype with internal validation",
    "not submission-ready",
    "not externally validated",
    "does not support strong public claims",
    "real pathogens",
    "real hosts",
    "biological protocols",
    "laboratory procedures",
    "executable interventions",
)


def main() -> None:
    print("Experiment 37: Integrated Manuscript Draft")
    print(
        "Question: Can the manuscript integrate positioning, formal notation, validation mapping, and boundaries into a single coherent draft?"
    )

    builder = IntegratedManuscriptDraftBuilder()
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
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing source artifact count: {report.missing_source_artifact_count}")
    print(f"Section count: {report.section_count}")
    print(f"Related family count: {report.related_family_count}")
    print(f"Notation count: {report.notation_count}")
    print(f"Validation row count: {report.validation_row_count}")
    print(f"Boundary count: {report.boundary_count}")
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
        raise SystemExit("integrated manuscript draft was not generated")

    if report.source_artifact_count < builder.minimum_source_artifact_count:
        raise SystemExit("too few source artifacts were listed")

    if report.missing_source_artifact_count != 0:
        raise SystemExit("some source artifacts are missing")

    if report.section_count < builder.minimum_section_count:
        raise SystemExit("too few manuscript sections were generated")

    if report.related_family_count < builder.minimum_related_family_count:
        raise SystemExit("too few related-work families were included")

    if report.notation_count < builder.minimum_notation_count:
        raise SystemExit("too few notation terms were included")

    if report.validation_row_count < builder.minimum_validation_row_count:
        raise SystemExit("too few validation rows were included")

    if report.boundary_count < 8:
        raise SystemExit("too few boundaries were included")

    if report.word_count < builder.minimum_word_count:
        raise SystemExit("integrated manuscript draft is too short")

    if report.error_count != 0:
        raise SystemExit("integrated manuscript draft produced errors")

    if missing_phrases:
        raise SystemExit(1)

    if not report.passed:
        raise SystemExit("integrated manuscript draft did not pass")

    print("Experiment 37 completed successfully.")


if __name__ == "__main__":
    main()
