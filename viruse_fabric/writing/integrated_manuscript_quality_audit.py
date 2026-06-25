"""Integrated manuscript quality audit for Viruse Fabric v3.8.

This module audits the integrated manuscript draft produced in v3.7.

It checks whether the draft preserves the project's cautious research status,
keeps boundaries visible, integrates formal notation and related-work
positioning, includes validation mapping, and avoids overclaiming.

The audit is intentionally internal. It does not certify submission readiness,
external validation, biological applicability, or any operational intervention.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

SOURCE_PATH = PROJECT_ROOT / "outputs" / "integrated_manuscript_draft_v3_7.md"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "integrated_manuscript_quality_audit_v3_8.md"


BOUNDARY_PHRASES = [
    "research prototype with internal validation",
    "internal validation",
    "not a final paper",
    "not a submission-ready manuscript",
    "cautious technical-review artifact",
    "does not establish external validation",
    "does not support biological intervention",
    "does not provide operational biological guidance",
    "no claim is made",
    "conceptual-computational",
    "abstract",
]


NOTATION_TERMS = [
    "F = (C, P, A, O)",
    "C",
    "P",
    "A",
    "O",
    "K(p, C)",
    "alpha(p, A)",
    "I_app(p, O)",
    "I_false",
    "R(I_app)",
    "Delta_R",
    "path compatibility",
    "attractor concentration",
    "apparent intentionality",
]


RELATED_WORK_TERMS = [
    "Linear causal-chain models",
    "Network causality",
    "Dynamical systems",
    "Constraint-based explanation",
    "Observer-dependent interpretation",
    "Teleology and apparent purpose",
    "Model validation and stress testing",
    "Related Work",
    "Positioning",
]


VALIDATION_TERMS = [
    "scenario stress",
    "constructive attractor ablation",
    "parameter sensitivity",
    "adversarial sensitivity",
    "baseline comparison",
    "projection perturbation",
    "validation synthesis",
    "validation mapping",
    "validation results",
    "validation table",
]


SUBMISSION_READY_BAD_PHRASES = [
    "submission-ready manuscript",
    "ready for submission",
    "publication-ready",
    "ready for publication",
]


OVERCLAIM_PATTERNS = [
    r"\bproves\b",
    r"\bproven\b",
    r"\bestablishes\b",
    r"\bdefinitive\b",
    r"\buniversal theory\b",
    r"\bvalidated externally\b",
    r"\bexternal validation is established\b",
    r"\bpredicts real biological systems\b",
    r"\boperational biological\b",
    r"\blaboratory protocol\b",
    r"\bclinical protocol\b",
    r"\bactionable intervention\b",
    r"\bhost-pathogen\b",
    r"\bdose\b",
    r"\breceptor\b",
]


NEGATION_OR_BOUNDARY_CUES = [
    "not",
    "does not",
    "no claim",
    "without",
    "cannot",
    "should not",
    "not yet",
    "no external",
    "not a",
    "boundary",
    "limitation",
    "cautious",
    "prototype",
]


SAFE_OVERCLAIM_CONTEXT_CUES = [
    "disallowed",
    "unsupported",
    "not supported",
    "boundary",
    "boundaries",
    "limitation",
    "limitations",
    "must not",
    "should not",
    "non-goals",
    "excluded",
    "anti-overclaim",
    "claim control",
]


FAKE_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
    r"\(20\d{2}\)",
]


@dataclass(frozen=True)
class AuditResult:
    title: str
    source_path: Path
    output_path: Path
    source_exists: bool
    section_count: int
    word_count: int
    boundary_count: int
    notation_count: int
    related_work_count: int
    validation_count: int
    validation_table_present: bool
    fake_citation_count: int
    overclaim_count: int
    submission_ready_claim_count: int
    recommendation_count: int
    errors: list[str]
    warnings: list[str]
    passed: bool
    interpretation: str


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def count_sections(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.startswith("## "))


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w\-']+\b", text, flags=re.UNICODE))


def count_present_terms(text: str, terms: Iterable[str]) -> int:
    lowered = text.lower()
    return sum(1 for term in terms if term.lower() in lowered)


def line_has_boundary_cue(line: str) -> bool:
    lowered = line.lower()
    return any(cue in lowered for cue in NEGATION_OR_BOUNDARY_CUES)


def safe_overclaim_context(active_headers: list[str]) -> bool:
    context = " / ".join(active_headers).lower()
    return any(cue in context for cue in SAFE_OVERCLAIM_CONTEXT_CUES)


def update_header_context(line: str, active_headers: list[str]) -> list[str]:
    if not line.startswith("#"):
        return active_headers

    level = len(line) - len(line.lstrip("#"))
    title = line.lstrip("#").strip()

    trimmed = active_headers[: max(level - 1, 0)]
    trimmed.append(title)
    return trimmed


def find_overclaim_lines(text: str) -> list[str]:
    findings: list[str] = []
    active_headers: list[str] = []

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        active_headers = update_header_context(stripped, active_headers)

        lowered = stripped.lower()

        if line_has_boundary_cue(lowered):
            continue

        if safe_overclaim_context(active_headers):
            continue

        for pattern in OVERCLAIM_PATTERNS:
            if re.search(pattern, lowered, flags=re.IGNORECASE):
                findings.append(stripped)
                break

    return findings


def find_fake_citations(text: str) -> list[str]:
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


def find_submission_ready_claims(text: str) -> list[str]:
    findings: list[str] = []
    active_headers: list[str] = []

    for line in text.splitlines():
        stripped = line.strip()

        if not stripped:
            continue

        active_headers = update_header_context(stripped, active_headers)

        lowered = stripped.lower()

        if line_has_boundary_cue(lowered):
            continue

        if safe_overclaim_context(active_headers):
            continue

        for phrase in SUBMISSION_READY_BAD_PHRASES:
            if phrase in lowered:
                findings.append(stripped)
                break

    return findings


def validation_table_present(text: str) -> bool:
    lowered = text.lower()
    table_markers = [
        "|",
        "validation",
        "result",
    ]
    return all(marker in lowered for marker in table_markers)


def build_recommendations(result_like: dict[str, int | bool]) -> list[str]:
    recommendations: list[str] = []

    if result_like["overclaim_count"] == 0:
        recommendations.append("Preserve the current anti-overclaim language in later manuscript edits.")
    else:
        recommendations.append("Rewrite overclaiming lines into cautious internal-validation language.")

    if result_like["boundary_count"] >= 8:
        recommendations.append("Keep research-boundary phrases visible in the abstract, validation, and limitation sections.")
    else:
        recommendations.append("Add more explicit boundary phrases near the manuscript's claims and conclusion.")

    if result_like["notation_count"] >= 10:
        recommendations.append("Keep notation as a scaffold rather than presenting it as a complete formal theory.")
    else:
        recommendations.append("Strengthen formal notation integration and define each symbol near first use.")

    if result_like["related_work_count"] >= 7:
        recommendations.append("Proceed to literature mapping without inventing citations.")
    else:
        recommendations.append("Expand related-work positioning before planning real citations.")

    if result_like["validation_count"] >= 7 and result_like["validation_table_present"]:
        recommendations.append("Use the compact validation table as the anchor for later review.")
    else:
        recommendations.append("Make the validation mapping and validation table more explicit.")

    recommendations.append("Do not describe the manuscript as submission-ready until citation mapping and external review exist.")

    return recommendations


def generate_report() -> AuditResult:
    text = read_text(SOURCE_PATH)
    source_exists = SOURCE_PATH.exists()

    sections = count_sections(text)
    words = count_words(text)
    boundaries = count_present_terms(text, BOUNDARY_PHRASES)
    notation = count_present_terms(text, NOTATION_TERMS)
    related = count_present_terms(text, RELATED_WORK_TERMS)
    validation = count_present_terms(text, VALIDATION_TERMS)
    table_present = validation_table_present(text)

    overclaim_lines = find_overclaim_lines(text)
    fake_citation_lines = find_fake_citations(text)
    submission_ready_claims = find_submission_ready_claims(text)

    errors: list[str] = []
    warnings: list[str] = []

    if not source_exists:
        errors.append(f"Missing source manuscript: {SOURCE_PATH.relative_to(PROJECT_ROOT)}")

    if sections < 18:
        errors.append(f"Section count too low: {sections}")

    if words < 2500:
        errors.append(f"Word count too low for integrated manuscript audit: {words}")

    if boundaries < 6:
        errors.append(f"Boundary phrase count too low: {boundaries}")

    if notation < 9:
        errors.append(f"Formal notation integration too weak: {notation}")

    if related < 7:
        errors.append(f"Related-work positioning integration too weak: {related}")

    if validation < 7:
        errors.append(f"Validation mapping integration too weak: {validation}")

    if not table_present:
        errors.append("Validation table or compact validation result structure not detected.")

    if overclaim_lines:
        errors.append(f"Overclaiming lines detected: {len(overclaim_lines)}")

    if submission_ready_claims:
        errors.append(f"Submission-ready claim detected: {len(submission_ready_claims)}")

    if fake_citation_lines:
        errors.append(f"Possible fake citation placeholders detected: {len(fake_citation_lines)}")

    if boundaries < 9:
        warnings.append("Boundary coverage is acceptable but should remain visible during future edits.")

    if notation < 12:
        warnings.append("Notation coverage is acceptable but should be reviewed for readability.")

    if related < 9:
        warnings.append("Related-work positioning is present but still needs real literature mapping.")

    metrics = {
        "overclaim_count": len(overclaim_lines),
        "boundary_count": boundaries,
        "notation_count": notation,
        "related_work_count": related,
        "validation_count": validation,
        "validation_table_present": table_present,
    }

    recommendations = build_recommendations(metrics)

    passed = not errors

    interpretation = (
        "The integrated manuscript draft preserves a cautious internal-validation "
        "status while combining positioning, notation, validation mapping, and "
        "explicit research boundaries. It remains an internal technical-review "
        "artifact, not a final paper and not a submission-ready manuscript."
    )

    report = render_markdown_report(
        title="Integrated Manuscript Quality Audit v3.8",
        source_exists=source_exists,
        sections=sections,
        words=words,
        boundaries=boundaries,
        notation=notation,
        related=related,
        validation=validation,
        table_present=table_present,
        overclaim_lines=overclaim_lines,
        fake_citation_lines=fake_citation_lines,
        submission_ready_claims=submission_ready_claims,
        recommendations=recommendations,
        errors=errors,
        warnings=warnings,
        passed=passed,
        interpretation=interpretation,
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    return AuditResult(
        title="Integrated Manuscript Quality Audit v3.8",
        source_path=SOURCE_PATH,
        output_path=OUTPUT_PATH,
        source_exists=source_exists,
        section_count=sections,
        word_count=words,
        boundary_count=boundaries,
        notation_count=notation,
        related_work_count=related,
        validation_count=validation,
        validation_table_present=table_present,
        fake_citation_count=len(fake_citation_lines),
        overclaim_count=len(overclaim_lines),
        submission_ready_claim_count=len(submission_ready_claims),
        recommendation_count=len(recommendations),
        errors=errors,
        warnings=warnings,
        passed=passed,
        interpretation=interpretation,
    )


def render_markdown_report(
    *,
    title: str,
    source_exists: bool,
    sections: int,
    words: int,
    boundaries: int,
    notation: int,
    related: int,
    validation: int,
    table_present: bool,
    overclaim_lines: list[str],
    fake_citation_lines: list[str],
    submission_ready_claims: list[str],
    recommendations: list[str],
    errors: list[str],
    warnings: list[str],
    passed: bool,
    interpretation: str,
) -> str:
    def bullet_lines(items: list[str]) -> str:
        if not items:
            return "- None"
        return "\n".join(f"- {item}" for item in items)

    return f"""# {title}

## Question
Does the v3.7 integrated manuscript preserve quality, caution, and internal coherence after combining the manuscript base, related-work positioning, formal notation, validation mapping, and research boundaries?

## Source
- Source manuscript: `outputs/integrated_manuscript_draft_v3_7.md`
- Source exists: {source_exists}
- Audit output: `outputs/integrated_manuscript_quality_audit_v3_8.md`

## Summary Metrics
- Section count: {sections}
- Word count: {words}
- Boundary phrase count: {boundaries}
- Formal notation integration count: {notation}
- Related-work positioning count: {related}
- Validation mapping count: {validation}
- Validation table present: {table_present}
- Overclaim count: {len(overclaim_lines)}
- Possible fake citation count: {len(fake_citation_lines)}
- Submission-ready claim count: {len(submission_ready_claims)}
- Recommendation count: {len(recommendations)}
- Errors: {len(errors)}
- Warnings: {len(warnings)}
- Passed: {passed}

## Quality Checks

### 1. Research Boundary Preservation
The manuscript must remain a research prototype with internal validation.

The audit checks for explicit boundary phrases such as internal validation, cautious technical review, absence of external validation, and non-submission status.

Result:

- Boundary phrase count: {boundaries}
- Status: {"acceptable" if boundaries >= 6 else "needs revision"}

### 2. Overclaim Control
The manuscript must not claim proof, universal validity, external validation, biological prediction, operational guidance, or submission readiness.

Result:

- Overclaim count: {len(overclaim_lines)}
- Submission-ready claim count: {len(submission_ready_claims)}
- Status: {"clean" if not overclaim_lines and not submission_ready_claims else "needs revision"}

Detected overclaim lines:

{bullet_lines(overclaim_lines)}

Detected submission-ready claims:

{bullet_lines(submission_ready_claims)}

### 3. Formal Notation Integration
The manuscript should include the formal notation scaffold without pretending that the notation is a complete mathematical theory.

Expected notation family:

- `F = (C, P, A, O)`
- `K(p, C)`
- `alpha(p, A)`
- `I_app(p, O)`
- `I_false`
- `R(I_app)`
- `Delta_R`

Result:

- Formal notation integration count: {notation}
- Status: {"acceptable" if notation >= 9 else "needs revision"}

### 4. Related-Work Positioning
The manuscript should position Viruse Fabric against adjacent conceptual families without fabricating citations.

Expected families include:

- Linear causal-chain models
- Network causality
- Dynamical systems
- Constraint-based explanation
- Observer-dependent interpretation
- Teleology and apparent purpose
- Model validation and stress testing

Result:

- Related-work positioning count: {related}
- Possible fake citation count: {len(fake_citation_lines)}
- Status: {"acceptable" if related >= 7 and not fake_citation_lines else "needs revision"}

Detected possible fake citations:

{bullet_lines(fake_citation_lines)}

### 5. Validation Mapping
The manuscript should include compact validation mapping and keep all validation claims internal.

Result:

- Validation mapping count: {validation}
- Validation table present: {table_present}
- Status: {"acceptable" if validation >= 7 and table_present else "needs revision"}

### 6. Submission Readiness Boundary
The manuscript must not be described as submission-ready.

Result:

- Submission-ready claim count: {len(submission_ready_claims)}
- Status: {"clean" if not submission_ready_claims else "needs revision"}

## Recommendations
{bullet_lines(recommendations)}

## Errors
{bullet_lines(errors)}

## Warnings
{bullet_lines(warnings)}

## Interpretation
{interpretation}

## Audit Status
This audit supports the manuscript as a cautious technical-review artifact.

It does not certify external validation, empirical adequacy, biological applicability, laboratory relevance, clinical relevance, or submission readiness.

Current project status remains:

`research prototype with internal validation`
"""


def main() -> None:
    result = generate_report()

    print("Integrated Manuscript Quality Audit v3.8")
    print(f"Source manuscript: {result.source_path.relative_to(PROJECT_ROOT)}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source exists: {result.source_exists}")
    print(f"Section count: {result.section_count}")
    print(f"Word count: {result.word_count}")
    print(f"Boundary phrase count: {result.boundary_count}")
    print(f"Formal notation integration count: {result.notation_count}")
    print(f"Related-work positioning count: {result.related_work_count}")
    print(f"Validation mapping count: {result.validation_count}")
    print(f"Validation table present: {result.validation_table_present}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Possible fake citation count: {result.fake_citation_count}")
    print(f"Submission-ready claim count: {result.submission_ready_claim_count}")
    print(f"Recommendation count: {result.recommendation_count}")
    print(f"Errors: {len(result.errors)}")
    print(f"Warnings: {len(result.warnings)}")
    print(f"Passed: {result.passed}")
    print(f"Report exists: {result.output_path.exists()}")
    print(f"Report size: {result.output_path.stat().st_size if result.output_path.exists() else 0}")
    print(f"Interpretation: {result.interpretation}")

    if not result.passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
