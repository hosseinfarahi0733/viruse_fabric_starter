"""One-page public preview audit for Viruse Fabric v4.3.

This module audits the v4.2 one-page public preview.

The audit checks whether the shortened public preview:
- remains compact,
- keeps required sections,
- preserves scientific boundaries,
- avoids overclaiming,
- avoids fake citations,
- keeps internal validation separate from external validation,
- remains not submission-ready,
- remains not biological, clinical, laboratory, or operational guidance.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

SOURCE_PATH = PROJECT_ROOT / "outputs" / "one_page_public_preview_v4_2.md"
SOURCE_FULL_PREVIEW_PATH = PROJECT_ROOT / "outputs" / "public_technical_preview_package_v4_0.md"
SOURCE_PUBLIC_AUDIT_PATH = PROJECT_ROOT / "outputs" / "public_preview_quality_audit_v4_1.md"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "one_page_public_preview_audit_v4_3.md"


REQUIRED_SECTIONS = [
    "One-Page Public Preview",
    "Status",
    "Thesis",
    "Plain-Language Summary",
    "Core Model",
    "Internal Validation",
    "What It Is Not",
    "Current Public Use",
    "Next Step",
]


BOUNDARY_PHRASES = [
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "not biological guidance",
    "not clinical guidance",
    "not laboratory guidance",
    "not operational guidance",
    "citation placeholders are not citations",
    "internal validation only",
    "does not provide external validation",
]


CORE_TERMS = [
    "constraint",
    "constraint-geometric",
    "constraints",
    "possible paths",
    "constructive attractors",
    "observer projection",
    "apparent intentionality",
    "F = (C, P, A, O)",
    "internal validation",
]


LIMITATION_TERMS = [
    "not ",
    "does not",
    "without",
    "cannot",
    "boundary",
    "internal validation only",
    "not externally validated",
    "not submission-ready",
]


OVERCLAIM_PATTERNS = [
    r"\bproves\b",
    r"\bproven\b",
    r"\bestablishes\b",
    r"\bdefinitive\b",
    r"\buniversal theory\b",
    r"\bexternally validated\b",
    r"\bclinical relevance\b",
    r"\blaboratory relevance\b",
    r"\bbiological intervention\b",
    r"\boperational intervention\b",
    r"\bpredicts real biological systems\b",
    r"\bready for submission\b",
    r"\bpublication-ready\b",
    r"\bsubmission-ready manuscript\b",
]


SAFE_LINE_CUES = [
    "not",
    "does not",
    "no claim",
    "without",
    "cannot",
    "should not",
    "boundary",
    "limitation",
    "prototype",
    "internal validation",
    "not externally",
    "not submission",
    "not biological",
    "not clinical",
    "not laboratory",
    "not operational",
    "what it is not",
]


FAKE_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
    r"\(20\d{2}\)",
]


@dataclass(frozen=True)
class OnePageAuditResult:
    title: str
    source_path: Path
    output_path: Path
    source_exists: bool
    full_preview_exists: bool
    public_audit_exists: bool
    section_count: int
    word_count: int
    required_section_count: int
    missing_required_section_count: int
    boundary_phrase_count: int
    core_term_count: int
    limitation_language_count: int
    overclaim_count: int
    fake_citation_count: int
    compactness_status: str
    one_page_readiness_score: int
    recommendation_count: int
    errors: list[str]
    warnings: list[str]
    passed: bool
    interpretation: str


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w\-']+\b", text, flags=re.UNICODE))


def count_sections(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.startswith("## "))


def count_present_terms(text: str, terms: Iterable[str]) -> int:
    lowered = text.lower()
    return sum(1 for term in terms if term.lower() in lowered)


def missing_required_sections(text: str) -> list[str]:
    lowered = text.lower()
    return [section for section in REQUIRED_SECTIONS if f"## {section}".lower() not in lowered]


def line_is_safe_context(line: str) -> bool:
    lowered = line.lower()
    return any(cue in lowered for cue in SAFE_LINE_CUES)


def detect_overclaims(text: str) -> list[str]:
    findings: list[str] = []

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        lowered = stripped.lower()

        if line_is_safe_context(lowered):
            continue

        for pattern in OVERCLAIM_PATTERNS:
            if re.search(pattern, lowered, flags=re.IGNORECASE):
                findings.append(stripped)
                break

    return findings


def detect_fake_citations(text: str) -> list[str]:
    findings: list[str] = []

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        if "citation placeholder" in stripped.lower():
            continue

        for pattern in FAKE_CITATION_PATTERNS:
            if re.search(pattern, stripped):
                findings.append(stripped)
                break

    return findings


def compactness_status(word_count: int) -> str:
    if word_count < 650:
        return "too short"
    if word_count > 950:
        return "too long"
    if word_count > 850:
        return "compact but layout-sensitive"
    return "compact"


def estimate_score(
    *,
    source_exists: bool,
    full_preview_exists: bool,
    public_audit_exists: bool,
    missing_sections: int,
    word_count: int,
    boundary_count: int,
    core_terms: int,
    limitations: int,
    overclaims: int,
    fake_citations: int,
) -> int:
    score = 0

    if source_exists:
        score += 10

    if full_preview_exists:
        score += 5

    if public_audit_exists:
        score += 5

    score += min(20, max(0, 20 - missing_sections * 3))

    if 650 <= word_count <= 950:
        score += 15

    score += min(15, boundary_count)
    score += min(10, core_terms)
    score += min(10, limitations // 2)

    if overclaims == 0:
        score += 5

    if fake_citations == 0:
        score += 5

    return min(score, 100)


def build_recommendations(
    *,
    missing_sections: list[str],
    word_count: int,
    boundary_count: int,
    overclaims: int,
    fake_citations: int,
) -> list[str]:
    recommendations: list[str] = []

    if not missing_sections:
        recommendations.append("Preserve the current one-page section structure.")
    else:
        recommendations.append("Restore missing sections before public use.")

    if 650 <= word_count <= 950:
        recommendations.append("Keep the one-page preview within the current compact word range.")
    elif word_count < 650:
        recommendations.append("Expand the one-page preview enough to preserve context and boundaries.")
    else:
        recommendations.append("Shorten the preview while preserving boundary phrases.")

    if boundary_count >= 8:
        recommendations.append("Keep boundary phrases visible even if the preview is visually redesigned.")
    else:
        recommendations.append("Increase boundary visibility before sharing.")

    if overclaims == 0:
        recommendations.append("Maintain the current anti-overclaim language.")
    else:
        recommendations.append("Rewrite overclaiming lines into prototype-status language.")

    if fake_citations == 0:
        recommendations.append("Keep citation placeholders clearly marked as non-citations.")
    else:
        recommendations.append("Remove fake citation-like patterns before any public use.")

    recommendations.append("Re-audit after any shortening, visual formatting, or public rewrite.")

    return recommendations


def bullet_lines(items: list[str]) -> str:
    if not items:
        return "- None"
    return "\n".join(f"- {item}" for item in items)


def render_markdown_report(
    *,
    source_exists: bool,
    full_preview_exists: bool,
    public_audit_exists: bool,
    section_count: int,
    word_count: int,
    missing_sections: list[str],
    boundary_count: int,
    core_terms: int,
    limitations: int,
    overclaim_lines: list[str],
    fake_citation_lines: list[str],
    compact_status: str,
    score: int,
    recommendations: list[str],
    errors: list[str],
    warnings: list[str],
    passed: bool,
    interpretation: str,
) -> str:
    return f"""# One-Page Public Preview Audit v4.3

## Question
Does the v4.2 one-page public preview remain compact, bounded, clear, citation-safe, and free from overclaim after compression?

## Source
- One-page preview: `outputs/one_page_public_preview_v4_2.md`
- Full public preview exists: {full_preview_exists}
- Public preview quality audit exists: {public_audit_exists}
- Source exists: {source_exists}
- Audit output: `outputs/one_page_public_preview_audit_v4_3.md`

## Summary Metrics
- Section count: {section_count}
- Word count: {word_count}
- Required section count: {len(REQUIRED_SECTIONS)}
- Missing required section count: {len(missing_sections)}
- Boundary phrase count: {boundary_count}
- Core term coverage count: {core_terms}
- Limitation language count: {limitations}
- Overclaim count: {len(overclaim_lines)}
- Fake citation-like pattern count: {len(fake_citation_lines)}
- Compactness status: {compact_status}
- One-page readiness score: {score}
- Recommendation count: {len(recommendations)}
- Errors: {len(errors)}
- Warnings: {len(warnings)}
- Passed: {passed}

## Required Section Check
Missing required sections:

{bullet_lines(missing_sections)}

## Boundary Retention
The shortened preview must preserve these boundaries:

- research prototype with internal validation
- not externally validated
- not submission-ready
- not a final paper
- not biological guidance
- not clinical guidance
- not laboratory guidance
- not operational guidance
- citation placeholders are not citations

Result:

- Boundary phrase count: {boundary_count}
- Status: {"acceptable" if boundary_count >= 8 else "needs revision"}

## Compactness Check
The preview should remain compact without becoming too thin to carry the project's boundaries.

Result:

- Word count: {word_count}
- Compactness status: {compact_status}
- Status: {"acceptable" if 650 <= word_count <= 950 else "needs revision"}

## Concept Coverage
The preview should still include enough conceptual vocabulary for orientation.

Result:

- Core term coverage count: {core_terms}
- Status: {"acceptable" if core_terms >= 7 else "needs revision"}

## Overclaim Control
Detected overclaim lines:

{bullet_lines(overclaim_lines)}

## Citation Safety
Detected fake citation-like lines:

{bullet_lines(fake_citation_lines)}

## Limitation Visibility
The one-page preview should retain enough limitation language to prevent public-facing inflation.

Result:

- Limitation language count: {limitations}
- Status: {"acceptable" if limitations >= 18 else "needs revision"}

## Recommendations
{bullet_lines(recommendations)}

## Errors
{bullet_lines(errors)}

## Warnings
{bullet_lines(warnings)}

## Interpretation
{interpretation}

## Audit Status
This audit supports the v4.2 one-page preview as a compact public-safe orientation artifact.

It does not certify external validation, empirical adequacy, biological applicability, clinical relevance, laboratory relevance, operational usefulness, or submission readiness.

Current project status remains:

`research prototype with internal validation`
"""


def generate_report() -> OnePageAuditResult:
    text = read_text(SOURCE_PATH)

    source_exists = SOURCE_PATH.exists()
    full_preview_exists = SOURCE_FULL_PREVIEW_PATH.exists()
    public_audit_exists = SOURCE_PUBLIC_AUDIT_PATH.exists()

    sections = count_sections(text)
    words = count_words(text)
    missing_sections = missing_required_sections(text)
    boundaries = count_present_terms(text, BOUNDARY_PHRASES)
    core_terms = count_present_terms(text, CORE_TERMS)
    limitations = sum(text.lower().count(term) for term in LIMITATION_TERMS)
    overclaim_lines = detect_overclaims(text)
    fake_citation_lines = detect_fake_citations(text)

    compact_status = compactness_status(words)

    score = estimate_score(
        source_exists=source_exists,
        full_preview_exists=full_preview_exists,
        public_audit_exists=public_audit_exists,
        missing_sections=len(missing_sections),
        word_count=words,
        boundary_count=boundaries,
        core_terms=core_terms,
        limitations=limitations,
        overclaims=len(overclaim_lines),
        fake_citations=len(fake_citation_lines),
    )

    errors: list[str] = []
    warnings: list[str] = []

    if not source_exists:
        errors.append(f"Missing source one-page preview: {SOURCE_PATH.relative_to(PROJECT_ROOT)}")

    if not full_preview_exists:
        errors.append(f"Missing full public preview: {SOURCE_FULL_PREVIEW_PATH.relative_to(PROJECT_ROOT)}")

    if not public_audit_exists:
        errors.append(f"Missing public preview quality audit: {SOURCE_PUBLIC_AUDIT_PATH.relative_to(PROJECT_ROOT)}")

    if sections < 9:
        errors.append(f"Section count too low: {sections}")

    if words < 650:
        errors.append(f"Word count too low for one-page public preview: {words}")

    if words > 950:
        errors.append(f"Word count too high for one-page public preview: {words}")

    if missing_sections:
        errors.append(f"Missing required sections: {len(missing_sections)}")

    if boundaries < 8:
        errors.append(f"Boundary phrase count too low: {boundaries}")

    if core_terms < 7:
        errors.append(f"Core term coverage too low: {core_terms}")

    if limitations < 18:
        errors.append(f"Limitation language count too low: {limitations}")

    if overclaim_lines:
        errors.append(f"Overclaim lines detected: {len(overclaim_lines)}")

    if fake_citation_lines:
        errors.append(f"Fake citation-like lines detected: {len(fake_citation_lines)}")

    if score < 85:
        errors.append(f"One-page readiness score too low: {score}")

    if words == 650:
        warnings.append("Word count is exactly at the lower bound; future edits should avoid trimming.")

    warnings.append("Any visual or shorter version must be re-audited before broad public use.")

    recommendations = build_recommendations(
        missing_sections=missing_sections,
        word_count=words,
        boundary_count=boundaries,
        overclaims=len(overclaim_lines),
        fake_citations=len(fake_citation_lines),
    )

    passed = not errors

    interpretation = (
        "The v4.3 audit checks that the compressed v4.2 one-page public preview "
        "retains required sections, boundaries, limitation language, citation "
        "safety, and anti-overclaim controls. It supports cautious public-facing "
        "orientation, not external validation or submission readiness."
    )

    report = render_markdown_report(
        source_exists=source_exists,
        full_preview_exists=full_preview_exists,
        public_audit_exists=public_audit_exists,
        section_count=sections,
        word_count=words,
        missing_sections=missing_sections,
        boundary_count=boundaries,
        core_terms=core_terms,
        limitations=limitations,
        overclaim_lines=overclaim_lines,
        fake_citation_lines=fake_citation_lines,
        compact_status=compact_status,
        score=score,
        recommendations=recommendations,
        errors=errors,
        warnings=warnings,
        passed=passed,
        interpretation=interpretation,
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    return OnePageAuditResult(
        title="One-Page Public Preview Audit v4.3",
        source_path=SOURCE_PATH,
        output_path=OUTPUT_PATH,
        source_exists=source_exists,
        full_preview_exists=full_preview_exists,
        public_audit_exists=public_audit_exists,
        section_count=sections,
        word_count=words,
        required_section_count=len(REQUIRED_SECTIONS),
        missing_required_section_count=len(missing_sections),
        boundary_phrase_count=boundaries,
        core_term_count=core_terms,
        limitation_language_count=limitations,
        overclaim_count=len(overclaim_lines),
        fake_citation_count=len(fake_citation_lines),
        compactness_status=compact_status,
        one_page_readiness_score=score,
        recommendation_count=len(recommendations),
        errors=errors,
        warnings=warnings,
        passed=passed,
        interpretation=interpretation,
    )


def main() -> None:
    result = generate_report()

    print("One-Page Public Preview Audit v4.3")
    print(f"Source preview: {result.source_path.relative_to(PROJECT_ROOT)}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source exists: {result.source_exists}")
    print(f"Full public preview exists: {result.full_preview_exists}")
    print(f"Public preview quality audit exists: {result.public_audit_exists}")
    print(f"Section count: {result.section_count}")
    print(f"Word count: {result.word_count}")
    print(f"Required section count: {result.required_section_count}")
    print(f"Missing required section count: {result.missing_required_section_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Core term coverage count: {result.core_term_count}")
    print(f"Limitation language count: {result.limitation_language_count}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Fake citation-like pattern count: {result.fake_citation_count}")
    print(f"Compactness status: {result.compactness_status}")
    print(f"One-page readiness score: {result.one_page_readiness_score}")
    print(f"Recommendation count: {result.recommendation_count}")
    print(f"Errors: {len(result.errors)}")
    print(f"Warnings: {len(result.warnings)}")
    print(f"Passed: {result.passed}")
    print(f"Report exists: {result.output_path.exists()}")
    print(f"Report size: {result.output_path.stat().st_size if result.output_path.exists() else 0}")
    print(f"Interpretation: {result.interpretation}")

    if result.errors:
        print("Errors:")
        for error in result.errors:
            print(f"- {error}")

    if result.warnings:
        print("Warnings:")
        for warning in result.warnings:
            print(f"- {warning}")

    if not result.passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
