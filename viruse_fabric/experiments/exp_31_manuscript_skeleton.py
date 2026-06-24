from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.manuscript_skeleton import ManuscriptSkeletonBuilder


REQUIRED_REPORT_PHRASES = (
    "Viruse Fabric Manuscript Skeleton",
    "Manuscript Status",
    "manuscript skeleton for cautious technical review",
    "Working Title",
    "Core Sentence",
    "Causality is not a chain; it is a geometry of constraints.",
    "Human-AI Work Note",
    "Abstract Draft",
    "Proposed Manuscript Structure",
    "Formal Model",
    "Validation Protocol",
    "Validation Results",
    "Research Readiness",
    "Limitations",
    "Allowed Claims",
    "Disallowed Claims",
    "Source Artifact Inventory",
    "Research Boundary",
    "conceptual and non-operational",
    "real pathogens",
    "real hosts",
    "biological protocols",
    "laboratory procedures",
    "executable interventions",
    "Next Writing Step",
)


def main() -> None:
    print("Experiment 31: Manuscript Skeleton")
    print(
        "Question: Can the validated research prototype be converted into a cautious manuscript structure?"
    )

    builder = ManuscriptSkeletonBuilder()
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
    print(f"Validation section count: {report.validation_section_count}")
    print(f"Source artifact count: {report.source_artifact_count}")
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
        raise SystemExit("manuscript skeleton report was not generated")

    if report.section_count < 10:
        raise SystemExit("too few manuscript sections were generated")

    if report.validation_section_count < 5:
        raise SystemExit("validation is underrepresented in the manuscript skeleton")

    if report.source_artifact_count < 14:
        raise SystemExit("too few source artifacts were included")

    if report.allowed_claim_count < 5:
        raise SystemExit("allowed claims are under-specified")

    if report.disallowed_claim_count < 5:
        raise SystemExit("disallowed claims are under-specified")

    if report.word_count < 900:
        raise SystemExit("manuscript skeleton is too short")

    if report.error_count != 0:
        raise SystemExit("manuscript skeleton produced errors")

    if missing_phrases:
        raise SystemExit(1)

    if not report.passed:
        raise SystemExit("manuscript skeleton did not pass")

    print("Experiment 31 completed successfully.")


if __name__ == "__main__":
    main()
