"""Public release readiness audit for Viruse Fabric v4.6.

This module audits the public-safe release path created through v4.5.

It checks whether the public release bundle, checklist, and supporting audits
are sufficient for cautious public orientation while preserving the boundary
that the project is not externally validated and not submission-ready.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "public_release_readiness_audit_v4_6.md"

REQUIRED_PUBLIC_PATH_ARTIFACTS = [
    PROJECT_ROOT / "outputs" / "public_technical_preview_package_v4_0.md",
    PROJECT_ROOT / "outputs" / "public_preview_quality_audit_v4_1.md",
    PROJECT_ROOT / "outputs" / "one_page_public_preview_v4_2.md",
    PROJECT_ROOT / "outputs" / "one_page_public_preview_audit_v4_3.md",
    PROJECT_ROOT / "outputs" / "public_release_bundle_index_v4_4.md",
    PROJECT_ROOT / "outputs" / "public_release_checklist_v4_5.md",
]

SUPPORTING_ARTIFACTS = [
    PROJECT_ROOT / "outputs" / "integrated_manuscript_draft_v3_7.md",
    PROJECT_ROOT / "outputs" / "integrated_manuscript_quality_audit_v3_8.md",
    PROJECT_ROOT / "outputs" / "citation_placeholder_plan_v3_9.md",
]

READINESS_DIMENSIONS = [
    "Artifact completeness",
    "Audit coverage",
    "Boundary retention",
    "Citation safety",
    "Overclaim control",
    "Release-gate clarity",
    "Audience routing",
    "Visual transformation caution",
    "Submission boundary",
    "External-validation boundary",
]

REQUIRED_BOUNDARY_PHRASES = [
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
    "does not certify external validation",
]

REQUIRED_READINESS_STATEMENTS = [
    "ready for cautious public orientation",
    "not ready for submission",
    "not externally validated",
    "not a final paper",
    "not a validation claim",
    "not biological guidance",
    "not clinical guidance",
    "not laboratory guidance",
    "not operational guidance",
    "visual or slide versions require a separate audit",
]

RELEASE_PATH_GATES = [
    "Full public preview exists.",
    "Full public preview audit exists.",
    "One-page public preview exists.",
    "One-page public preview audit exists.",
    "Public release bundle index exists.",
    "Public release checklist exists.",
    "Citation placeholders remain placeholders.",
    "Public-facing claims remain bounded.",
    "Submission readiness is not claimed.",
    "External validation is not claimed.",
    "Any visual, slide, landing-page, or shorter version requires a new audit.",
    "Project status remains research prototype with internal validation.",
]

RISK_ITEMS = [
    "A public reader may confuse internal validation with external validation.",
    "A shortened version may remove boundary phrases.",
    "A visual design may hide limitations.",
    "Citation placeholders may be mistaken for citations.",
    "The manuscript may be mistaken for a submission-ready paper.",
    "The one-page preview may be mistaken for evidence.",
    "A title or subtitle may accidentally overclaim.",
    "A landing page may turn cautious orientation into promotion.",
]

APPROVED_USE_CASES = [
    "Cautious public technical orientation",
    "Internal reviewer handoff",
    "Collaborator orientation",
    "Release planning",
    "Audience routing",
    "Boundary-preserving communication",
]

DISALLOWED_USE_CASES = [
    "Submission package",
    "External validation claim",
    "Empirical adequacy claim",
    "Biological guidance",
    "Clinical guidance",
    "Laboratory guidance",
    "Operational guidance",
    "Citation-complete manuscript",
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
    r"\bempirically confirmed framework\b",
]

SAFE_LINE_CUES = [
    "not",
    "does not",
    "do not",
    "must not",
    "disallowed",
    "risk",
    "boundary",
    "not claimed",
    "is not claimed",
    "not externally",
    "not submission",
    "not ready",
    "not a final",
    "not biological",
    "not clinical",
    "not laboratory",
    "not operational",
    "citation placeholders are not citations",
    "requires a separate audit",
    "requires a new audit",
    "research prototype",
    "internal validation",
    "audit",
    "gate",
]

SAFE_SECTION_HEADINGS = [
    "risk register",
    "disallowed use cases",
    "release path gates",
    "final boundary statement",
    "readiness verdict",
    "what this audit does not mean",
]

FAKE_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
    r"\(20\d{2}\)",
]


@dataclass(frozen=True)
class PublicReleaseReadinessAuditResult:
    title: str
    output_path: Path
    public_artifact_count: int
    missing_public_artifact_count: int
    supporting_artifact_count: int
    missing_supporting_artifact_count: int
    readiness_dimension_count: int
    boundary_phrase_count: int
    readiness_statement_count: int
    release_gate_count: int
    risk_item_count: int
    approved_use_case_count: int
    disallowed_use_case_count: int
    overclaim_count: int
    fake_citation_count: int
    readiness_score: int
    word_count: int
    errors: list[str]
    warnings: list[str]
    passed: bool
    verdict: str
    interpretation: str


def relative(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT))


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w\-']+\b", text, flags=re.UNICODE))


def count_present_terms(text: str, terms: Iterable[str]) -> int:
    lowered = text.lower()
    return sum(1 for term in terms if term.lower() in lowered)


def bullet_list(items: list[str]) -> str:
    if not items:
        return "- None"
    return "\n".join(f"- {item}" for item in items)


def artifact_table(paths: list[Path]) -> str:
    rows = [
        "| Artifact | Exists |",
        "|---|---|",
    ]
    for path in paths:
        rows.append(f"| `{relative(path)}` | {path.exists()} |")
    return "\n".join(rows)


def missing_paths(paths: list[Path]) -> list[Path]:
    return [path for path in paths if not path.exists()]


def line_is_safe_context(line: str) -> bool:
    lowered = line.lower()
    return any(cue in lowered for cue in SAFE_LINE_CUES)


def detect_overclaims(text: str) -> list[str]:
    findings: list[str] = []
    current_section = ""

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        lowered = stripped.lower()

        if lowered.startswith("## "):
            current_section = lowered.removeprefix("## ").strip()

        if current_section in SAFE_SECTION_HEADINGS:
            continue

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

        lowered = stripped.lower()

        if "citation placeholder" in lowered or "fake citation" in lowered:
            continue

        for pattern in FAKE_CITATION_PATTERNS:
            if re.search(pattern, stripped):
                findings.append(stripped)
                break

    return findings


def estimate_readiness_score(
    *,
    missing_public: int,
    missing_supporting: int,
    dimensions: int,
    boundaries: int,
    readiness_statements: int,
    release_gates: int,
    risks: int,
    approved_uses: int,
    disallowed_uses: int,
    overclaims: int,
    fake_citations: int,
) -> int:
    score = 0

    score += max(0, 20 - missing_public * 5)
    score += max(0, 10 - missing_supporting * 3)
    score += min(10, dimensions)
    score += min(15, boundaries)
    score += min(10, readiness_statements)
    score += min(12, release_gates)
    score += min(8, risks)
    score += min(6, approved_uses)
    score += min(6, disallowed_uses)

    if overclaims == 0:
        score += 7

    if fake_citations == 0:
        score += 6

    return min(score, 100)


def render_report() -> str:
    return f"""# Public Release Readiness Audit v4.6

## Question
Is the Viruse Fabric public-safe release path ready for cautious public orientation while remaining clearly not ready for submission, not externally validated, and not a final paper?

## Status
Current project status remains:

`research prototype with internal validation`

This audit is not a validation claim. It does not certify external validation, empirical adequacy, biological applicability, clinical relevance, laboratory relevance, operational usefulness, or submission readiness.

## Public Path Artifact Check
These are the required public-safe release-path artifacts.

{artifact_table(REQUIRED_PUBLIC_PATH_ARTIFACTS)}

## Supporting Artifact Check
These supporting artifacts help position the public release path, but they do not make the project submission-ready.

{artifact_table(SUPPORTING_ARTIFACTS)}

## Readiness Dimensions
The audit checks the following readiness dimensions:

{bullet_list(READINESS_DIMENSIONS)}

## Release Path Gates
The public-safe path is acceptable only if these gates remain satisfied:

{bullet_list(RELEASE_PATH_GATES)}

## Boundary Retention
These boundary phrases must remain visible across public-safe materials:

{bullet_list(REQUIRED_BOUNDARY_PHRASES)}

## Readiness Statements
The final readiness language is deliberately narrow:

{bullet_list(REQUIRED_READINESS_STATEMENTS)}

## Approved Use Cases
The current bundle may be used for:

{bullet_list(APPROVED_USE_CASES)}

## Disallowed Use Cases
The current bundle must not be used for:

{bullet_list(DISALLOWED_USE_CASES)}

## Risk Register
The remaining public-release risks are known and manageable only if the checklist stays attached to the process.

{bullet_list(RISK_ITEMS)}

## Readiness Verdict
The public-safe path is ready for cautious public orientation.

It is not ready for submission. It is not externally validated. It is not a final paper. It is not a validation claim.

Visual or slide versions require a separate audit. Landing-page versions require a separate audit. Shorter summaries require a separate audit.

## What This Audit Does Not Mean
This audit does not mean the theory has been externally validated.

It does not mean the manuscript is ready for submission.

It does not mean citation placeholders are real citations.

It does not mean the model provides biological guidance, clinical guidance, laboratory guidance, or operational guidance.

It does not replace real literature search, external review, independent validation, or expert critique. Astonishingly, a checklist cannot overthrow peer review by sheer formatting. Humanity survives another day.

## Public Orientation Readiness
The release path is ready only in a narrow communication sense.

A cautious public reader can be shown the technical preview, the one-page preview, and the bundle index to understand what the project is trying to express. That reader should also be able to see the limitation language clearly enough to understand that the current work is internally validated only.

This means the current bundle can support orientation, review, discussion, and planning. It does not support publication claims, validation claims, biological claims, clinical claims, laboratory claims, operational claims, or authority claims. The release materials are useful because they tell the reader where the project stands and where it does not stand.

## Remaining Work Before Submission
Before any submission-style milestone, the project still needs real literature search, real citations, source-grounded related work, external review, and stronger validation planning.

The citation placeholder plan helps prepare that work, but it is not the work itself. The public previews explain the project, but they are not a substitute for a manuscript with verified references. The audits reduce communication risk, but they do not establish scientific truth.

A future submission path should therefore be treated as a separate phase. It should not reuse public-readiness language as if it were submission-readiness language. That would be convenient, and convenience is how projects quietly walk into walls.

## Transformation Rule
Any transformed artifact must be treated as new until audited.

A slide deck is not the same artifact as the one-page preview. A landing page is not the same artifact as the bundle index. A social post is not the same artifact as the technical preview. Each transformation changes emphasis, visibility, context, and reader expectation.

If a transformed version hides the project status, removes citation warnings, weakens limitation language, or makes the theory sound externally validated, it fails the readiness boundary and must be revised before use.

## Final Boundary Statement
The public-release path is internally organized and bounded.

It is ready for cautious public orientation only.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> PublicReleaseReadinessAuditResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing_public = missing_paths(REQUIRED_PUBLIC_PATH_ARTIFACTS)
    missing_supporting = missing_paths(SUPPORTING_ARTIFACTS)
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    boundary_count = count_present_terms(report, REQUIRED_BOUNDARY_PHRASES)
    readiness_statement_count = count_present_terms(report, REQUIRED_READINESS_STATEMENTS)
    release_gate_count = count_present_terms(report, RELEASE_PATH_GATES)
    risk_item_count = count_present_terms(report, RISK_ITEMS)
    approved_use_count = count_present_terms(report, APPROVED_USE_CASES)
    disallowed_use_count = count_present_terms(report, DISALLOWED_USE_CASES)
    word_count = count_words(report)

    readiness_score = estimate_readiness_score(
        missing_public=len(missing_public),
        missing_supporting=len(missing_supporting),
        dimensions=len(READINESS_DIMENSIONS),
        boundaries=boundary_count,
        readiness_statements=readiness_statement_count,
        release_gates=release_gate_count,
        risks=risk_item_count,
        approved_uses=approved_use_count,
        disallowed_uses=disallowed_use_count,
        overclaims=len(overclaims),
        fake_citations=len(fake_citations),
    )

    errors: list[str] = []
    warnings: list[str] = []

    if len(REQUIRED_PUBLIC_PATH_ARTIFACTS) < 6:
        errors.append(f"Public path artifact count too low: {len(REQUIRED_PUBLIC_PATH_ARTIFACTS)}")

    if missing_public:
        errors.append(f"Missing public path artifacts: {len(missing_public)}")

    if len(SUPPORTING_ARTIFACTS) < 3:
        errors.append(f"Supporting artifact count too low: {len(SUPPORTING_ARTIFACTS)}")

    if missing_supporting:
        errors.append(f"Missing supporting artifacts: {len(missing_supporting)}")

    if len(READINESS_DIMENSIONS) < 10:
        errors.append(f"Readiness dimension count too low: {len(READINESS_DIMENSIONS)}")

    if boundary_count < 10:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if readiness_statement_count < 10:
        errors.append(f"Readiness statement count too low: {readiness_statement_count}")

    if release_gate_count < 12:
        errors.append(f"Release gate count too low: {release_gate_count}")

    if risk_item_count < 8:
        errors.append(f"Risk item count too low: {risk_item_count}")

    if approved_use_count < 6:
        errors.append(f"Approved use case count too low: {approved_use_count}")

    if disallowed_use_count < 8:
        errors.append(f"Disallowed use case count too low: {disallowed_use_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if readiness_score < 90:
        errors.append(f"Readiness score too low: {readiness_score}")

    if word_count < 950:
        errors.append(f"Word count too low for public release readiness audit: {word_count}")

    warnings.append("Readiness is limited to cautious public orientation, not submission.")
    warnings.append("Any visual, slide, landing-page, or shorter public artifact requires a separate audit.")

    passed = not errors

    verdict = "ready for cautious public orientation, not ready for submission"

    interpretation = (
        "The v4.6 readiness audit checks whether the public-safe release path "
        "is internally complete, bounded, citation-safe, and free from overclaim. "
        "It supports cautious public orientation only."
    )

    return PublicReleaseReadinessAuditResult(
        title="Public Release Readiness Audit v4.6",
        output_path=OUTPUT_PATH,
        public_artifact_count=len(REQUIRED_PUBLIC_PATH_ARTIFACTS),
        missing_public_artifact_count=len(missing_public),
        supporting_artifact_count=len(SUPPORTING_ARTIFACTS),
        missing_supporting_artifact_count=len(missing_supporting),
        readiness_dimension_count=len(READINESS_DIMENSIONS),
        boundary_phrase_count=boundary_count,
        readiness_statement_count=readiness_statement_count,
        release_gate_count=release_gate_count,
        risk_item_count=risk_item_count,
        approved_use_case_count=approved_use_count,
        disallowed_use_case_count=disallowed_use_count,
        overclaim_count=len(overclaims),
        fake_citation_count=len(fake_citations),
        readiness_score=readiness_score,
        word_count=word_count,
        errors=errors,
        warnings=warnings,
        passed=passed,
        verdict=verdict,
        interpretation=interpretation,
    )


def main() -> None:
    result = generate_report()

    print("Public Release Readiness Audit v4.6")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Public artifact count: {result.public_artifact_count}")
    print(f"Missing public artifact count: {result.missing_public_artifact_count}")
    print(f"Supporting artifact count: {result.supporting_artifact_count}")
    print(f"Missing supporting artifact count: {result.missing_supporting_artifact_count}")
    print(f"Readiness dimension count: {result.readiness_dimension_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Readiness statement count: {result.readiness_statement_count}")
    print(f"Release gate count: {result.release_gate_count}")
    print(f"Risk item count: {result.risk_item_count}")
    print(f"Approved use case count: {result.approved_use_case_count}")
    print(f"Disallowed use case count: {result.disallowed_use_case_count}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Fake citation-like pattern count: {result.fake_citation_count}")
    print(f"Readiness score: {result.readiness_score}")
    print(f"Word count: {result.word_count}")
    print(f"Errors: {len(result.errors)}")
    print(f"Warnings: {len(result.warnings)}")
    print(f"Passed: {result.passed}")
    print(f"Report exists: {result.output_path.exists()}")
    print(f"Report size: {result.output_path.stat().st_size if result.output_path.exists() else 0}")
    print(f"Verdict: {result.verdict}")
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
