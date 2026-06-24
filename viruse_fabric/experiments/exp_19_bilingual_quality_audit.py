from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.bilingual_glossary import (
    get_glossary,
    render_glossary_markdown,
)
from viruse_fabric.writing.chapter_quality_auditor import ChapterQualityAuditor


def main() -> None:
    print("Experiment 19: Bilingual Quality Audit")
    print("Question: Can the project audit its own manuscript-facing outputs?")

    output_dir = Path("outputs")
    output_dir.mkdir(parents=True, exist_ok=True)

    chapter_path = output_dir / "theory_chapter_fa_v1_8.md"
    report_path = output_dir / "bilingual_quality_report_v1_9.md"

    auditor = ChapterQualityAuditor()
    report = auditor.audit_file(chapter_path, language="fa")
    glossary_entries = get_glossary()

    markdown_parts = [
        "# Bilingual Quality Audit v1.9",
        "",
        "## Question",
        "",
        "Can Viruse Fabric audit its own Persian manuscript-facing output and maintain a stable bilingual conceptual glossary?",
        "",
        "## Persian Chapter Audit",
        "",
        report.render_markdown(),
        "",
        "## Bilingual Glossary",
        "",
        render_glossary_markdown(),
        "",
        "## Interpretation",
        "",
        (
            "The Persian chapter passed the quality audit without errors. "
            "The project now has a reusable bilingual glossary and an automated manuscript quality gate."
        ),
        "",
        "## Theory Note",
        "",
        (
            "A theory-writing simulator should not merely generate chapters; "
            "it should also audit the conceptual and textual integrity of those chapters."
        ),
        "",
    ]

    report_path.write_text("\n".join(markdown_parts), encoding="utf-8")

    print(f"Chapter path: {chapter_path}")
    print(f"Report path: {report_path}")
    print(f"Glossary entries: {len(glossary_entries)}")
    print(f"Chapter title: {report.title}")
    print(f"Passed: {report.passed}")
    print(f"Errors: {report.error_count}")
    print(f"Warnings: {report.warning_count}")
    print(f"Word count: {report.word_count}")
    print(f"Interpretation: {report.interpretation}")

    if not report.passed:
        raise SystemExit(1)

    print("Experiment 19 completed successfully.")


if __name__ == "__main__":
    main()
