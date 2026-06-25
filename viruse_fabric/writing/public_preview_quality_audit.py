"""Public preview quality audit for Viruse Fabric v4.1.

This module audits the v4.0 public technical preview package.

The audit checks whether the public-facing preview:
- preserves the internal-validation boundary,
- avoids overclaiming,
- avoids fake citations,
- remains understandable to a technical public audience,
- keeps limitations visible,
- avoids biological, clinical, laboratory, and operational guidance,
- keeps citation placeholders separate from real citations.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

SOURCE_PATH = PROJECT_ROOT / "outputs" / "public_technical_preview_package_v4_0.md"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "public_preview_quality_audit_v4_1.md"


REQUIRED_PUBLIC_SECTIONS = [
    "Public Technical Preview",
    "One-Sentence Thesis",
    "Plain-Language Summary",
    "What the Project Is",
    "What the Project Is Not",
    "Core Concepts",
    "Conceptual Model",
    "Validation Status",
    "Manuscript Status",
    "Citation Status",
    "Limitations",
    "Safe Public Description",
    "Public Communication Guidance",
    "Suggested Public Abstract",
    "Review Checklist",
    "Next Steps",
    "Final Boundary Statement",
]


BOUNDARY_PHRASES = [
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "not operational guidance",
    "not biological guidance",
    "not clinical guidance",
    "not laboratory guidance",
    "internal validation only",
    "does not provide external validation",
    "does not establish empirical adequacy",
    "does not support biological intervention",
    "does not support clinical intervention",
    "does not support laboratory use",
    "does not support operational use",
    "citation placeholders are not citations",
]


CORE_CONCEPT_TERMS = [
    "constraint",
    "constraint geometry",
    "constructive attractor",
    "path compatibility",
    "observer projection",
    "apparent intentionality",
    "F = (C, P, A, O)",
    "K(p, C)",
    "I_app(p, O)",
]


PUBLIC_CLARITY_TERMS = [
    "plain-language",
    "safe phrasing",
    "safe public description",
    "suggested public abstract",
    "review checklist",
    "what the project is",
    "what the project is not",
    "use this kind of language",
    "avoid this kind of language",
    "technical preview",
]


LIMITATION_TERMS = [
    "does not",
    "not ",
    "without",
    "cannot",
    "should not",
    "limitations",
    "boundary",
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
    "not yet",
    "boundary",
    "limitation",
    "limitations",
    "prototype",
    "internal validation",
    "not externally",
    "not submission",
    "not a final",
    "not operational",
    "not biological",
    "not clinical",
    "not laboratory",
    "avoid this kind",
    "unsafe",
    "outside the current project boundary",
]


SAFE_SECTION_CUES = [
    "what the project is not",
    "unsafe validation statement",
    "limitations",
    "final boundary statement",
    "review checklist",
    "public communication guidance",
    "avoid this kind of language",
    "what the project is not",
]


FAKE_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
    r"\(20\d{2}\)",
]


@dataclass(frozen=True)
class PublicPreviewAuditResult:
    title: str
    source_path: Path
    output_path: Path
    source_exists: bool
    source_section_count: int
    source_word_count: int
    required_section_count: int
    missing_required_section_count: int
    boundary_phrase_count: int
    core_concept_count: int
    public_clarity_count: int
    limitation_language_count: int
    overclaim_count: int
    fake_citation_count: int
    public_readiness_score: int
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
    return [section for section in REQUIRED_PUBLIC_SECTIONS if f"## {section}".lower() not in lowered]


def update_header_context(line: str, active_headers: list[str]) -> list[str]:
    if not line.startswith("#"):
        return active_headers

    level = len(line) - len(line.lstrip("#"))
    title = line.lstrip("#").strip()

    trimmed = active_headers[: max(level - 1, 0)]
    trimmed.append(title)
    return trimmed


def line_is_safe_context(line: str) -> bool:
    lowered = line.lower()
    return any(cue in lowered for cue in SAFE_LINE_CUES)


def safe_section_context(active_headers: list[str], previous_line: str) -> bool:
    context = " / ".join(active_headers + [previous_line]).lower()
    return any(cue in context for cue in SAFE_SECTION_CUES)


def detect_overclaims(text: str) -> list[str]:
    findings: list[str] = []
    active_headers: list[str] = []
    previous_nonempty = ""

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        active_headers = update_header_context(stripped, active_headers)
        lowered = stripped.lower()

        if line_is_safe_context(lowered):
            previous_nonempty = stripped
            continue

        if safe_section_context(active_headers, previous_nonempty):
            previous_nonempty = stripped
            continue

        for pattern in OVERCLAIM_PATTERNS:
            if re.search(pattern, lowered, flags=re.IGNORECASE):
                findings.append(stripped)
                break

        previous_nonempty = stripped

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


def estimate_public_readiness_score(
    *,
    source_exists: bool,
    missing_sections: int,
    boundary_count: int,
    core_concepts: int,
    clarity_count: int,
    limitation_count: int,
    overclaims: int,
    fake_citations: int,
    word_count: int,
) -> int:
    score = 0

    if source_exists:
        score += 10

    score += min(20, max(0, 20 - missing_sections * 3))
    score += min(20, boundary_count)
    score += min(15, core_concepts)
    score += min(10, clarity_count)
    score += min(10, limitation_count // 4)

    if word_count >= 1500:
        score += 5

    if overclaims == 0:
        score += 5

    if fake_citations == 0:
        score += 5

    return min(score, 100)


def build_recommendations(
    *,
    boundary_count: int,
    clarity_count: int,
    overclaims: int,
    fake_citations: int,
    missing_sections: list[str],
) -> list[str]:
    recommendations: list[str] = []

    if not missing_sections:
        recommendations.append("Preserve the current public section structure in later rewrites.")
    else:
        recommendations.append("Restore missing public-facing sections before release.")

    if boundary_count >= 12:
        recommendations.append("Keep boundary phrases visible in any shorter public version.")
    else:
        recommendations.append("Add more explicit boundary language near validation and public claims.")

    if clarity_count >= 8:
        recommendations.append("Keep the plain-language and safe-language contrast sections.")
    else:
        recommendations.append("Add more public-facing explanation before sharing outside technical readers.")

    if overclaims == 0:
        recommendations.append("Maintain the current anti-overclaim wording.")
    else:
        recommendations.append("Rewrite overclaiming lines into prototype-status language.")

    if fake_citations == 0:
        recommendations.append("Keep citation placeholders clearly separated from real citations.")
    else:
        recommendations.append("Remove fake citation-like patterns before public use.")

    recommendations.append("Run another audit after shortening or formatting the preview.")

    return recommendations


def bullet_lines(items: list[str]) -> str:
    if not items:
        return "- None"
    return "\n".join(f"- {item}" for item in items)


def render_markdown_report(
    *,
    source_exists: bool,
    source_sections: int,
    source_words: int,
    missing_sections: list[str],
    boundary_count: int,
    core_concept_count: int,
    clarity_count: int,
    limitation_count: int,
    overclaim_lines: list[str],
    fake_citation_lines: list[str],
    score: int,
    recommendations: list[str],
    errors: list[str],
    warnings: list[str],
    passed: bool,
    interpretation: str,
) -> str:
    return f"""# Public Preview Quality Audit v4.1

## Question
Does the v4.0 public technical preview remain safe, clear, bounded, and suitable for cautious public-facing technical review?

## Source
- Source preview: `outputs/public_technical_preview_package_v4_0.md`
- Source exists: {source_exists}
- Audit output: `outputs/public_preview_quality_audit_v4_1.md`

## Summary Metrics
- Source section count: {source_sections}
- Source word count: {source_words}
- Required public section count: {len(REQUIRED_PUBLIC_SECTIONS)}
- Missing required section count: {len(missing_sections)}
- Boundary phrase count: {boundary_count}
- Core concept coverage count: {core_concept_count}
- Public clarity count: {clarity_count}
- Limitation language count: {limitation_count}
- Overclaim count: {len(overclaim_lines)}
- Fake citation-like pattern count: {len(fake_citation_lines)}
- Public readiness score: {score}
- Recommendation count: {len(recommendations)}
- Errors: {len(errors)}
- Warnings: {len(warnings)}
- Passed: {passed}

## Required Section Check
Missing required sections:

{bullet_lines(missing_sections)}

## Boundary Visibility
The preview must keep these boundaries visible:

- research prototype with internal validation
- not externally validated
- not submission-ready
- not biological guidance
- not clinical guidance
- not laboratory guidance
- not operational guidance
- citation placeholders are not citations

Result:

- Boundary phrase count: {boundary_count}
- Status: {"acceptable" if boundary_count >= 12 else "needs revision"}

## Public Clarity
The preview should be understandable to a technical public audience. It should define the core vocabulary before using it heavily.

Result:

- Core concept coverage count: {core_concept_count}
- Public clarity count: {clarity_count}
- Status: {"acceptable" if core_concept_count >= 8 and clarity_count >= 8 else "needs revision"}

## Overclaim Control
The preview must not claim proof, external validation, universal theory status, biological prediction, or submission readiness.

Detected overclaim lines:

{bullet_lines(overclaim_lines)}

## Citation Safety
The preview must not include invented citations, fake author-year claims, fake DOI strings, fake arXiv identifiers, or numbered bibliography entries.

Detected fake citation-like lines:

{bullet_lines(fake_citation_lines)}

## Limitations
The preview should keep limitation language visible enough that readers cannot confuse a technical preview with a completed theory.

Result:

- Limitation language count: {limitation_count}
- Status: {"acceptable" if limitation_count >= 40 else "needs revision"}

## Recommendations
{bullet_lines(recommendations)}

## Errors
{bullet_lines(errors)}

## Warnings
{bullet_lines(warnings)}

## Interpretation
{interpretation}

## Audit Status
This audit supports the v4.0 package as a public-safe technical preview.

It does not certify external validation, empirical adequacy, biological applicability, clinical relevance, laboratory relevance, operational usefulness, or submission readiness.

Current project status remains:

`research prototype with internal validation`
"""


def generate_report() -> PublicPreviewAuditResult:
    text = read_text(SOURCE_PATH)
    source_exists = SOURCE_PATH.exists()

    source_sections = count_sections(text)
    source_words = count_words(text)
    missing_sections = missing_required_sections(text)

    boundary_count = count_present_terms(text, BOUNDARY_PHRASES)
    core_concepts = count_present_terms(text, CORE_CONCEPT_TERMS)
    clarity_count = count_present_terms(text, PUBLIC_CLARITY_TERMS)
    limitation_count = sum(text.lower().count(term) for term in LIMITATION_TERMS)

    overclaim_lines = detect_overclaims(text)
    fake_citation_lines = detect_fake_citations(text)

    score = estimate_public_readiness_score(
        source_exists=source_exists,
        missing_sections=len(missing_sections),
        boundary_count=boundary_count,
        core_concepts=core_concepts,
        clarity_count=clarity_count,
        limitation_count=limitation_count,
        overclaims=len(overclaim_lines),
        fake_citations=len(fake_citation_lines),
        word_count=source_words,
    )

    errors: list[str] = []
    warnings: list[str] = []

    if not source_exists:
        errors.append(f"Missing source preview: {SOURCE_PATH.relative_to(PROJECT_ROOT)}")

    if source_sections < 18:
        errors.append(f"Source section count too low: {source_sections}")

    if source_words < 1500:
        errors.append(f"Source word count too low: {source_words}")

    if missing_sections:
        errors.append(f"Missing required public sections: {len(missing_sections)}")

    if boundary_count < 12:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if core_concepts < 8:
        errors.append(f"Core concept coverage too low: {core_concepts}")

    if clarity_count < 8:
        errors.append(f"Public clarity count too low: {clarity_count}")

    if limitation_count < 40:
        errors.append(f"Limitation language count too low: {limitation_count}")

    if overclaim_lines:
        errors.append(f"Overclaim lines detected: {len(overclaim_lines)}")

    if fake_citation_lines:
        errors.append(f"Fake citation-like lines detected: {len(fake_citation_lines)}")

    if score < 80:
        errors.append(f"Public readiness score too low: {score}")

    if score < 90:
        warnings.append("Public readiness is acceptable but should be reviewed before broad sharing.")

    warnings.append("Any shortened version should be re-audited because compression often removes boundaries first.")

    recommendations = build_recommendations(
        boundary_count=boundary_count,
        clarity_count=clarity_count,
        overclaims=len(overclaim_lines),
        fake_citations=len(fake_citation_lines),
        missing_sections=missing_sections,
    )

    passed = not errors

    interpretation = (
        "The v4.1 audit checks that the v4.0 public technical preview remains "
        "bounded, understandable, citation-safe, and free from overclaiming. "
        "It supports cautious public-facing technical review while preserving "
        "the project's internal-validation status."
    )

    report = render_markdown_report(
        source_exists=source_exists,
        source_sections=source_sections,
        source_words=source_words,
        missing_sections=missing_sections,
        boundary_count=boundary_count,
        core_concept_count=core_concepts,
        clarity_count=clarity_count,
        limitation_count=limitation_count,
        overclaim_lines=overclaim_lines,
        fake_citation_lines=fake_citation_lines,
        score=score,
        recommendations=recommendations,
        errors=errors,
        warnings=warnings,
        passed=passed,
        interpretation=interpretation,
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    return PublicPreviewAuditResult(
        title="Public Preview Quality Audit v4.1",
        source_path=SOURCE_PATH,
        output_path=OUTPUT_PATH,
        source_exists=source_exists,
        source_section_count=source_sections,
        source_word_count=source_words,
        required_section_count=len(REQUIRED_PUBLIC_SECTIONS),
        missing_required_section_count=len(missing_sections),
        boundary_phrase_count=boundary_count,
        core_concept_count=core_concepts,
        public_clarity_count=clarity_count,
        limitation_language_count=limitation_count,
        overclaim_count=len(overclaim_lines),
        fake_citation_count=len(fake_citation_lines),
        public_readiness_score=score,
        recommendation_count=len(recommendations),
        errors=errors,
        warnings=warnings,
        passed=passed,
        interpretation=interpretation,
    )


def main() -> None:
    result = generate_report()

    print("Public Preview Quality Audit v4.1")
    print(f"Source preview: {result.source_path.relative_to(PROJECT_ROOT)}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source exists: {result.source_exists}")
    print(f"Source section count: {result.source_section_count}")
    print(f"Source word count: {result.source_word_count}")
    print(f"Required public section count: {result.required_section_count}")
    print(f"Missing required section count: {result.missing_required_section_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Core concept coverage count: {result.core_concept_count}")
    print(f"Public clarity count: {result.public_clarity_count}")
    print(f"Limitation language count: {result.limitation_language_count}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Fake citation-like pattern count: {result.fake_citation_count}")
    print(f"Public readiness score: {result.public_readiness_score}")
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
