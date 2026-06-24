from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.full_manuscript_draft import FullManuscriptDraftBuilder


REQUIRED_REPORT_PHRASES = (
    "Viruse Fabric Full Manuscript Draft",
    "Manuscript Status",
    "full manuscript draft for cautious technical review",
    "Working Title",
    "Abstract",
    "Introduction",
    "Core Thesis",
    "Formal Model",
    "Validation Sequence",
    "Results",
    "Limitations",
    "Allowed and Disallowed Claims",
    "Future Work",
    "Human-AI Work Note",
    "Source Artifact Inventory",
    "Research Boundary",
    "Conclusion",
    "research prototype with internal validation",
    "conceptual and non-operational",
    "real pathogens",
    "real hosts",
    "biological protocols",
    "laboratory procedures",
    "executable interventions",
    "not for strong public claims",
)


def main() -> None:
    print("Experiment 32: Full Manuscript Draft")
    print(
        "Question: Can the manuscript skeleton be expanded into a cautious full technical draft?"
    )

    builder = FullManuscriptDraftBuilder()
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
    print(f"Section count: {report.section_count}")
    print(f"Source artifact count: {report.source_artifact_count}")
    print(f"Missing artifact count: {report.missing_artifact_count}")
    print(f"Allowed claim count: {report.allowed_claim_count}")
    print(f"Disallowed claim count: {report.disallowed_claim_count}")
    print(f"Readiness status: {report.readiness_status}")
    print(f"Word count: {report.word_count}")
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
        raise SystemExit("full manuscript draft was not generated")

    if report.section_count < builder.minimum_section_count:
        raise SystemExit("too few manuscript sections were generated")

    if report.missing_artifact_count != 0:
        raise SystemExit("some manuscript source artifacts are missing")

    if report.allowed_claim_count < 5:
        raise SystemExit("allowed claims are under-specified")

    if report.disallowed_claim_count < 5:
        raise SystemExit("disallowed claims are under-specified")

    if report.word_count < builder.minimum_word_count:
        raise SystemExit("full manuscript draft is too short")

    if report.error_count != 0:
        raise SystemExit("full manuscript draft produced errors")

    if missing_phrases:
        raise SystemExit(1)

    if not report.passed:
        raise SystemExit("full manuscript draft did not pass")

    print("Experiment 32 completed successfully.")


if __name__ == "__main__":
    main()
