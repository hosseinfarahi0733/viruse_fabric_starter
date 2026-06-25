from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.full_manuscript_draft import FullManuscriptDraftBuilder
from viruse_fabric.writing.manuscript_quality_audit import ManuscriptQualityAuditor


REQUIRED_REPORT_PHRASES = (
    "Manuscript Quality Audit",
    "Purpose",
    "section coverage",
    "validation evidence",
    "claim boundaries",
    "unsupported overclaims",
    "Summary",
    "Required Section Check",
    "Boundary Phrase Check",
    "Validation Metric Check",
    "Unsupported Overclaim Check",
    "No unsupported overclaim lines detected",
    "Recommendations",
    "needs_related_work",
    "needs_formal_notation",
    "draft_not_submission_ready",
    "Audit Boundary",
    "does not establish external validation",
    "biological prediction",
    "operational use",
)


def main() -> None:
    print("Experiment 33: Manuscript Quality Audit")
    print(
        "Question: Does the full manuscript draft preserve validation evidence, claim boundaries, and research caution?"
    )

    # Rebuild the v3.2 manuscript first so the audit always reads the current generated draft.
    draft_builder = FullManuscriptDraftBuilder()
    draft_report = draft_builder.run()

    auditor = ManuscriptQualityAuditor()
    report = auditor.run()

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
    print(f"Manuscript path: {report.manuscript_path}")
    print(f"Draft word count: {draft_report.word_count}")
    print(f"Section count: {report.section_count}")
    print(f"Word count: {report.word_count}")
    print(f"Required section count: {report.required_section_count}")
    print(f"Missing required section count: {report.missing_required_section_count}")
    print(f"Boundary phrase count: {report.boundary_phrase_count}")
    print(f"Missing boundary phrase count: {report.missing_boundary_phrase_count}")
    print(f"Validation metric count: {report.validation_metric_count}")
    print(f"Overclaim count: {report.overclaim_count}")
    print(f"Weak phrase count: {report.weak_phrase_count}")
    print(f"Recommendation count: {report.recommendation_count}")
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
        raise SystemExit("manuscript quality audit report was not generated")

    if report.section_count < 15:
        raise SystemExit("manuscript section count is too low")

    if report.word_count < auditor.minimum_word_count:
        raise SystemExit("manuscript word count is too low")

    if report.missing_required_section_count != 0:
        raise SystemExit("manuscript is missing required sections")

    if report.missing_boundary_phrase_count != 0:
        raise SystemExit("manuscript is missing boundary phrases")

    if report.validation_metric_count < auditor.minimum_validation_metric_count:
        raise SystemExit("validation metrics are underrepresented")

    if report.overclaim_count != 0:
        raise SystemExit("unsupported overclaims were detected")

    if report.weak_phrase_count != 0:
        raise SystemExit("weak or hype phrases were detected")

    if report.error_count != 0:
        raise SystemExit("manuscript quality audit produced errors")

    if missing_phrases:
        raise SystemExit(1)

    if not report.passed:
        raise SystemExit("manuscript quality audit did not pass")

    print("Experiment 33 completed successfully.")


if __name__ == "__main__":
    main()
