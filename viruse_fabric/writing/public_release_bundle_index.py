"""Public release bundle index for Viruse Fabric v4.4.

This module generates an index of public-safe release artifacts.

The index identifies:
- which artifacts exist,
- which audience each artifact is for,
- what each artifact may be used for,
- what each artifact must not be used for,
- which boundaries must remain visible,
- what should happen before any broader public release.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "public_release_bundle_index_v4_4.md"


PUBLIC_ARTIFACTS = [
    {
        "name": "Citation Placeholder Plan v3.9",
        "path": PROJECT_ROOT / "outputs" / "citation_placeholder_plan_v3_9.md",
        "audience": "internal research and literature-mapping preparation",
        "use": "maps citation needs to literature families without inventing citations",
        "do_not_use_for": "bibliography, literature review, or real citation claims",
        "status": "planning artifact",
    },
    {
        "name": "Public Technical Preview Package v4.0",
        "path": PROJECT_ROOT / "outputs" / "public_technical_preview_package_v4_0.md",
        "audience": "technical readers who need a careful full overview",
        "use": "explains thesis, concepts, validation status, citation status, limitations, and next steps",
        "do_not_use_for": "submission, external validation claims, or operational guidance",
        "status": "public-safe technical preview",
    },
    {
        "name": "Public Preview Quality Audit v4.1",
        "path": PROJECT_ROOT / "outputs" / "public_preview_quality_audit_v4_1.md",
        "audience": "internal reviewers and release gatekeepers",
        "use": "checks the v4.0 public preview for boundaries, clarity, citation safety, and overclaim control",
        "do_not_use_for": "public-facing introduction by itself",
        "status": "quality audit",
    },
    {
        "name": "One-Page Public Preview v4.2",
        "path": PROJECT_ROOT / "outputs" / "one_page_public_preview_v4_2.md",
        "audience": "technical public readers who need a compact orientation",
        "use": "provides a short public-safe introduction to the project",
        "do_not_use_for": "final paper, external validation evidence, or standalone scientific proof",
        "status": "compact public preview",
    },
    {
        "name": "One-Page Public Preview Audit v4.3",
        "path": PROJECT_ROOT / "outputs" / "one_page_public_preview_audit_v4_3.md",
        "audience": "internal reviewers checking the compressed version",
        "use": "confirms that the one-page preview retained boundaries after compression",
        "do_not_use_for": "public-facing introduction by itself",
        "status": "quality audit",
    },
    {
        "name": "Integrated Manuscript Draft v3.7",
        "path": PROJECT_ROOT / "outputs" / "integrated_manuscript_draft_v3_7.md",
        "audience": "technical reviewers and manuscript collaborators",
        "use": "provides the integrated manuscript body with positioning, notation, validation mapping, and boundaries",
        "do_not_use_for": "submission-ready manuscript or public claim package",
        "status": "internal technical-review manuscript",
    },
    {
        "name": "Integrated Manuscript Quality Audit v3.8",
        "path": PROJECT_ROOT / "outputs" / "integrated_manuscript_quality_audit_v3_8.md",
        "audience": "internal manuscript reviewers",
        "use": "checks integrated manuscript quality, overclaim control, notation integration, and citation safety",
        "do_not_use_for": "external validation certification",
        "status": "manuscript audit",
    },
    {
        "name": "Fabric Diagram v2.1",
        "path": PROJECT_ROOT / "outputs" / "fabric_diagram_v2_1.png",
        "audience": "visual orientation and future slide/landing-page preparation",
        "use": "supports visual explanation of the constraint-fabric idea",
        "do_not_use_for": "evidence, validation, or standalone explanation without boundary text",
        "status": "visual support artifact",
    },
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
]


UNSAFE_USE_PHRASES = [
    "Do not present the bundle as external validation.",
    "Do not present the manuscript as submission-ready.",
    "Do not turn citation placeholders into citations.",
    "Do not use public previews as evidence of empirical adequacy.",
    "Do not use the visual diagram without boundary text.",
    "Do not make biological, clinical, laboratory, or operational claims.",
    "Do not remove limitation language when shortening or designing the material.",
]


RELEASE_GATES = [
    "All public-safe artifacts must exist.",
    "The one-page preview must have a passing audit.",
    "The full public preview must have a passing audit.",
    "Citation placeholders must remain clearly marked as placeholders.",
    "Any visual, slide, landing-page, or shorter version must receive a new audit.",
    "The project status must remain research prototype with internal validation.",
]


NEXT_STEPS = [
    "Create a public release checklist.",
    "Prepare a visual or slide version only after deciding the exact audience.",
    "Audit any visual or slide version before sharing.",
    "Perform real literature search before adding citations.",
    "Keep internal validation separate from external validation.",
    "Delay submission-style language until citation mapping and external review exist.",
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
    "do not",
    "do_not_use_for",
    "do not use for",
    "must not",
    "no claim",
    "without",
    "cannot",
    "should not",
    "boundary",
    "limitation",
    "limitations",
    "prototype",
    "internal validation",
    "not externally",
    "not submission",
    "not a final",
    "not biological",
    "not clinical",
    "not laboratory",
    "not operational",
    "unsafe use",
    "submission-ready manuscript or public claim package",
]


FAKE_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
    r"\(20\d{2}\)",
]


@dataclass(frozen=True)
class PublicReleaseBundleIndexResult:
    title: str
    output_path: Path
    artifact_count: int
    missing_artifact_count: int
    audience_count: int
    status_count: int
    boundary_phrase_count: int
    unsafe_use_count: int
    release_gate_count: int
    next_step_count: int
    overclaim_count: int
    fake_citation_count: int
    word_count: int
    errors: list[str]
    warnings: list[str]
    passed: bool
    interpretation: str


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w\-']+\b", text, flags=re.UNICODE))


def count_present_terms(text: str, terms: Iterable[str]) -> int:
    lowered = text.lower()
    return sum(1 for term in terms if term.lower() in lowered)


def missing_artifacts() -> list[dict[str, object]]:
    return [artifact for artifact in PUBLIC_ARTIFACTS if not artifact["path"].exists()]


def relative(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT))


def bullet_list(items: list[str]) -> str:
    if not items:
        return "- None"
    return "\n".join(f"- {item}" for item in items)


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


def render_artifact_table() -> str:
    rows = [
        "| Artifact | Path | Audience | Status | Exists |",
        "|---|---|---|---|---|",
    ]

    for artifact in PUBLIC_ARTIFACTS:
        path = artifact["path"]
        rows.append(
            f"| {artifact['name']} | `{relative(path)}` | {artifact['audience']} | {artifact['status']} | {path.exists()} |"
        )

    return "\n".join(rows)


def render_artifact_details() -> str:
    sections: list[str] = []

    for artifact in PUBLIC_ARTIFACTS:
        path = artifact["path"]
        sections.append(
            f"""### {artifact["name"]}

Path:
`{relative(path)}`

Exists:
{path.exists()}

Audience:
{artifact["audience"]}

Intended use:
{artifact["use"]}

Do not use for:
{artifact["do_not_use_for"]}

Status:
{artifact["status"]}
"""
        )

    return "\n".join(sections)


def render_report() -> str:
    artifact_table = render_artifact_table()
    artifact_details = render_artifact_details()

    boundary_lines = bullet_list(REQUIRED_BOUNDARY_PHRASES)
    unsafe_lines = bullet_list(UNSAFE_USE_PHRASES)
    release_gate_lines = bullet_list(RELEASE_GATES)
    next_step_lines = bullet_list(NEXT_STEPS)

    return f"""# Public Release Bundle Index v4.4

## Question
Can Viruse Fabric organize its public-safe artifacts into a release bundle index without overclaiming, inventing citations, or weakening project boundaries?

## Status
Current project status remains:

`research prototype with internal validation`

This bundle is not externally validated, not submission-ready, and not a final paper.

It is a public-safe release index for cautious technical orientation.

## Bundle Summary
The v4.4 bundle index gathers the public-facing and release-support artifacts created across v3.9 through v4.3.

It does not create new scientific claims. It does not certify external validation. It does not convert citation placeholders into citations. It does not provide biological guidance, clinical guidance, laboratory guidance, or operational guidance.

The purpose is practical: give future reviewers, collaborators, or public-facing material builders a clear map of which files exist, what each file is for, and what each file must not be used for.

## Artifact Table
{artifact_table}

## Artifact Details
{artifact_details}

## Required Boundary Phrases
These boundary phrases must remain visible whenever the bundle is used, shortened, redesigned, or converted into slides, a landing page, or a visual release.

{boundary_lines}

## Unsafe Uses
The bundle must not be used in the following ways:

{unsafe_lines}

## Release Gates
Before any broader public use, these gates should remain satisfied:

{release_gate_lines}

## Recommended Next Steps
{next_step_lines}

## Audience Map
- Technical reviewer: start with the Public Technical Preview Package v4.0.
- Fast orientation reader: start with the One-Page Public Preview v4.2.
- Internal release checker: start with the Public Preview Quality Audit v4.1 and One-Page Public Preview Audit v4.3.
- Manuscript collaborator: start with the Integrated Manuscript Draft v3.7 and Integrated Manuscript Quality Audit v3.8.
- Literature-mapping collaborator: start with the Citation Placeholder Plan v3.9.
- Visual designer: use Fabric Diagram v2.1 only with boundary text attached.

## Release Interpretation
The public-safe release path is now organized, but not complete as a scientific publication path.

The bundle supports cautious public-facing technical orientation. It does not support external validation claims, submission-readiness claims, biological applicability claims, clinical relevance claims, laboratory relevance claims, or operational usefulness claims.

The boring boundary language stays because removing it would make the bundle shinier and less honest, which is apparently how many public-facing scientific disasters begin.

## Final Boundary Statement
This release bundle index is a navigation artifact.

It helps organize public-safe materials, but it does not certify the theory, validate it externally, or make the manuscript ready for submission.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> PublicReleaseBundleIndexResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_artifacts()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    artifact_count = len(PUBLIC_ARTIFACTS)
    audience_count = len({artifact["audience"] for artifact in PUBLIC_ARTIFACTS})
    status_count = len({artifact["status"] for artifact in PUBLIC_ARTIFACTS})
    boundary_count = count_present_terms(report, REQUIRED_BOUNDARY_PHRASES)
    unsafe_count = count_present_terms(report, UNSAFE_USE_PHRASES)
    release_gate_count = count_present_terms(report, RELEASE_GATES)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if artifact_count < 8:
        errors.append(f"Artifact count too low: {artifact_count}")

    if missing:
        errors.append(f"Missing public bundle artifacts: {len(missing)}")

    if audience_count < 6:
        errors.append(f"Audience count too low: {audience_count}")

    if status_count < 5:
        errors.append(f"Status count too low: {status_count}")

    if boundary_count < 9:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if unsafe_count < 7:
        errors.append(f"Unsafe use count too low: {unsafe_count}")

    if release_gate_count < 6:
        errors.append(f"Release gate count too low: {release_gate_count}")

    if next_step_count < 6:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if word_count < 900:
        errors.append(f"Word count too low for release bundle index: {word_count}")

    if word_count > 2200:
        warnings.append("Release bundle index is long; consider a shorter checklist after this artifact is closed.")

    warnings.append("Any visual, slide, or landing-page version must be separately audited.")

    passed = not errors

    interpretation = (
        "The v4.4 public release bundle index organizes the public-safe outputs "
        "into a navigable release map while preserving project boundaries, "
        "citation safety, and the internal-validation status."
    )

    return PublicReleaseBundleIndexResult(
        title="Public Release Bundle Index v4.4",
        output_path=OUTPUT_PATH,
        artifact_count=artifact_count,
        missing_artifact_count=len(missing),
        audience_count=audience_count,
        status_count=status_count,
        boundary_phrase_count=boundary_count,
        unsafe_use_count=unsafe_count,
        release_gate_count=release_gate_count,
        next_step_count=next_step_count,
        overclaim_count=len(overclaims),
        fake_citation_count=len(fake_citations),
        word_count=word_count,
        errors=errors,
        warnings=warnings,
        passed=passed,
        interpretation=interpretation,
    )


def main() -> None:
    result = generate_report()

    print("Public Release Bundle Index v4.4")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Artifact count: {result.artifact_count}")
    print(f"Missing artifact count: {result.missing_artifact_count}")
    print(f"Audience count: {result.audience_count}")
    print(f"Status count: {result.status_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Unsafe use count: {result.unsafe_use_count}")
    print(f"Release gate count: {result.release_gate_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Fake citation-like pattern count: {result.fake_citation_count}")
    print(f"Word count: {result.word_count}")
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
