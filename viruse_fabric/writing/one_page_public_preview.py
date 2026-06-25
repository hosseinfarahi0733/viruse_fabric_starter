"""One-page public preview for Viruse Fabric v4.2.

This module generates a compact public-safe preview based on the v4.0 public
technical preview and the v4.1 public preview quality audit.

The goal is to produce a short, readable, public-facing artifact while keeping
the project's boundaries visible:

research prototype with internal validation

The artifact must not claim external validation, submission readiness,
biological applicability, clinical relevance, laboratory relevance, operational
usefulness, proof, or real citations.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

SOURCE_PREVIEW_PATH = PROJECT_ROOT / "outputs" / "public_technical_preview_package_v4_0.md"
SOURCE_AUDIT_PATH = PROJECT_ROOT / "outputs" / "public_preview_quality_audit_v4_1.md"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "one_page_public_preview_v4_2.md"


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
]


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
class OnePagePreviewResult:
    title: str
    output_path: Path
    source_preview_exists: bool
    source_audit_exists: bool
    section_count: int
    word_count: int
    boundary_phrase_count: int
    required_section_count: int
    missing_required_section_count: int
    overclaim_count: int
    fake_citation_count: int
    limitation_count: int
    errors: list[str]
    warnings: list[str]
    passed: bool
    interpretation: str


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


def render_report() -> str:
    return """# One-Page Public Preview v4.2

## One-Page Public Preview
Viruse Fabric is a compact public-facing technical preview of an abstract
constraint-geometric model of causality.

## Status
Current status:

`research prototype with internal validation`

The project is not externally validated, not submission-ready, and not a final
paper. It is a bounded technical preview for cautious discussion.

It does not provide external validation. It is not a final paper.

## Thesis
Causality is not treated only as a chain of events. Viruse Fabric models
causality as a geometry of constraints that shapes which paths become
compatible, stable, or apparently purposeful.

## Plain-Language Summary
Some systems can look purposeful without containing literal intention. Viruse
Fabric explores how constraints, possible paths, constructive attractors, and
observer projection can align so that a path appears directed after the outcome
is seen.

The core idea is simple: something may look goal-like because the available
paths were shaped, filtered, and concentrated by the surrounding constraint
structure. The model separates the path itself from the observer's later reading
of that path. This lets the project discuss apparent intentionality without
claiming real agency.

A useful everyday analogy is water moving across a shaped surface. The water
does not plan its path, but slopes, grooves, obstacles, and friction make some
routes easier and others less stable. A later observer may describe the result
as if the water found a target. Viruse Fabric uses that kind of distinction in
abstract form: path structure, attractor concentration, and observer
interpretation are treated as separable pieces.

This matters because many explanations become too confident after the outcome is
known. The project tries to slow that down. It asks whether the appearance of
purpose can be explained through constraints before assuming intention.

## Core Model
The integrated manuscript uses this scaffold:

`F = (C, P, A, O)`

Where:

- `C` means constraints,
- `P` means possible paths,
- `A` means constructive attractors,
- `O` means observer projection.

Related terms include path compatibility, attractor concentration, apparent
intentionality, false intentionality, and correction of observer projection.

This notation is a scaffold for explanation. It is not a complete mathematical
theory.

## Internal Validation
The project includes internal validation artifacts: scenario stress testing,
constructive attractor ablation, parameter sensitivity, adversarial sensitivity,
baseline comparison, projection perturbation, validation synthesis, manuscript
audit, citation-placeholder planning, public preview packaging, and public
preview audit.

Safe claim:

Viruse Fabric has internal validation results that support further technical
review of the prototype.

Boundary:

Internal validation only. Internal validation does not provide external
validation or empirical adequacy.

The validation results are useful because they check whether the prototype is
internally coherent under different pressures. They do not show that the model
works in the outside world. That distinction is the difference between a
promising technical preview and a premature scientific claim, a difference
humanity keeps rediscovering with the enthusiasm of someone touching a hot pan
twice.

## What It Is Not
Viruse Fabric is not biological guidance, not clinical guidance, not laboratory
guidance, and not operational guidance.

For clarity: it is not laboratory guidance.

It does not support biological intervention, clinical intervention, laboratory
use, or operational use.

It is not an externally validated theory, not a submission-ready manuscript, and
not a universal theory of causality.

Citation placeholders are not citations. No source should be treated as real
until source lookup and verification are completed.

## Current Public Use
This one-page preview is suitable for cautious public-facing technical
discussion, early explanation, and orientation before deeper review.

It can be used to explain the project to a technical reader who needs the main
idea, current status, validation boundary, and next responsible step in one
place. It should remain attached to the longer public preview and audit trail
when the work is discussed seriously.

It should not be used as a final paper, evidence of external validation, or a
claim of real-world predictive success.

## Next Step
The next responsible step is to audit this shortened one-page version, because
compression often removes exactly the boundaries that make a public preview
safe. Apparently even summaries need supervision now. Humanity truly has
optimized paperwork into a moral hazard.
"""


def generate_report() -> OnePagePreviewResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    source_preview_exists = SOURCE_PREVIEW_PATH.exists()
    source_audit_exists = SOURCE_AUDIT_PATH.exists()

    sections = count_sections(report)
    words = count_words(report)
    boundaries = count_present_terms(report, BOUNDARY_PHRASES)
    missing_sections = missing_required_sections(report)
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)
    limitations = report.lower().count("not ") + report.lower().count("does not")

    errors: list[str] = []
    warnings: list[str] = []

    if not source_preview_exists:
        errors.append(f"Missing source preview: {SOURCE_PREVIEW_PATH.relative_to(PROJECT_ROOT)}")

    if not source_audit_exists:
        errors.append(f"Missing source audit: {SOURCE_AUDIT_PATH.relative_to(PROJECT_ROOT)}")

    if sections < 9:
        errors.append(f"Section count too low: {sections}")

    if words < 650:
        errors.append(f"Word count too low for one-page preview: {words}")

    if words > 950:
        errors.append(f"Word count too high for one-page preview: {words}")

    if boundaries < 8:
        errors.append(f"Boundary phrase count too low: {boundaries}")

    if missing_sections:
        errors.append(f"Missing required sections: {len(missing_sections)}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if limitations < 14:
        errors.append(f"Limitation language count too low: {limitations}")

    if words > 850:
        warnings.append("One-page preview is acceptable but may need tighter layout formatting.")

    warnings.append("This shortened artifact must be audited before broad public use.")

    passed = not errors

    interpretation = (
        "The v4.2 one-page public preview compresses the v4.0 public package "
        "into a short public-safe artifact while preserving internal-validation "
        "status, limitation language, citation safety, and anti-overclaim boundaries."
    )

    return OnePagePreviewResult(
        title="One-Page Public Preview v4.2",
        output_path=OUTPUT_PATH,
        source_preview_exists=source_preview_exists,
        source_audit_exists=source_audit_exists,
        section_count=sections,
        word_count=words,
        boundary_phrase_count=boundaries,
        required_section_count=len(REQUIRED_SECTIONS),
        missing_required_section_count=len(missing_sections),
        overclaim_count=len(overclaims),
        fake_citation_count=len(fake_citations),
        limitation_count=limitations,
        errors=errors,
        warnings=warnings,
        passed=passed,
        interpretation=interpretation,
    )


def main() -> None:
    result = generate_report()

    print("One-Page Public Preview v4.2")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source preview exists: {result.source_preview_exists}")
    print(f"Source audit exists: {result.source_audit_exists}")
    print(f"Section count: {result.section_count}")
    print(f"Word count: {result.word_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Required section count: {result.required_section_count}")
    print(f"Missing required section count: {result.missing_required_section_count}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Fake citation-like pattern count: {result.fake_citation_count}")
    print(f"Limitation language count: {result.limitation_count}")
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
