"""Public release checklist for Viruse Fabric v4.5.

This module generates an executable public-release checklist.

The checklist converts the v4.4 public release bundle index into practical
release gates, allowed language, disallowed language, and artifact checks.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

SOURCE_BUNDLE_INDEX = PROJECT_ROOT / "outputs" / "public_release_bundle_index_v4_4.md"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "public_release_checklist_v4_5.md"


REQUIRED_ARTIFACTS = [
    PROJECT_ROOT / "outputs" / "citation_placeholder_plan_v3_9.md",
    PROJECT_ROOT / "outputs" / "public_technical_preview_package_v4_0.md",
    PROJECT_ROOT / "outputs" / "public_preview_quality_audit_v4_1.md",
    PROJECT_ROOT / "outputs" / "one_page_public_preview_v4_2.md",
    PROJECT_ROOT / "outputs" / "one_page_public_preview_audit_v4_3.md",
    PROJECT_ROOT / "outputs" / "integrated_manuscript_draft_v3_7.md",
    PROJECT_ROOT / "outputs" / "integrated_manuscript_quality_audit_v3_8.md",
    PROJECT_ROOT / "outputs" / "public_release_bundle_index_v4_4.md",
]


RELEASE_GATES = [
    "Bundle index exists and is current.",
    "All public-safe artifacts exist.",
    "Full public preview has a passing audit.",
    "One-page public preview has a passing audit.",
    "Citation placeholders remain clearly marked as placeholders.",
    "No fake citation-like patterns appear in the checklist.",
    "No overclaiming language appears outside boundary or disallowed-language contexts.",
    "Project status remains research prototype with internal validation.",
    "External validation is not claimed.",
    "Submission readiness is not claimed.",
    "Biological, clinical, laboratory, and operational guidance are not claimed.",
    "Any visual, slide, landing-page, or shorter version is separately audited before use.",
]


ALLOWED_PUBLIC_LANGUAGE = [
    "research prototype with internal validation",
    "public-safe technical orientation",
    "internal validation only",
    "conceptual framework",
    "constraint-geometric model",
    "one-page public preview",
    "citation placeholders are not citations",
    "not externally validated",
    "not submission-ready",
]


DISALLOWED_PUBLIC_LANGUAGE = [
    "externally validated theory",
    "submission-ready manuscript",
    "proven universal theory",
    "biological guidance",
    "clinical guidance",
    "laboratory guidance",
    "operational guidance",
    "predicts real biological systems",
    "publication-ready result",
    "empirically confirmed framework",
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
]


AUDIT_REQUIREMENTS = [
    "Audit any shortened public text.",
    "Audit any slide version.",
    "Audit any visual or landing-page version.",
    "Audit any rewritten one-page summary.",
    "Audit any artifact that changes boundary wording.",
    "Audit any artifact that adds citation-like text.",
]


NEXT_STEPS = [
    "Use the checklist before sharing any public-facing artifact.",
    "Create a slide or landing-page draft only after selecting the target audience.",
    "Run a dedicated audit for any slide or landing-page draft.",
    "Perform real literature search before replacing citation placeholders.",
    "Keep the manuscript separate from public preview materials.",
    "Keep external validation language out of public release materials until such validation exists.",
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
    "disallowed public language",
    "not claimed",
    "is not claimed",
    "no overclaim",
    "boundary",
    "boundary phrases",
    "citation placeholders are not citations",
    "research prototype",
    "internal validation",
    "not externally",
    "not submission",
    "not biological",
    "not clinical",
    "not laboratory",
    "not operational",
    "audit",
    "gate",
]

SAFE_SECTION_HEADINGS = [
    "disallowed public language",
    "boundary phrases",
    "release gates",
    "audit requirements",
    "release procedure",
    "final boundary statement",
]


FAKE_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
    r"\(20\d{2}\)",
]


@dataclass(frozen=True)
class PublicReleaseChecklistResult:
    title: str
    source_bundle_index: Path
    output_path: Path
    source_exists: bool
    required_artifact_count: int
    missing_artifact_count: int
    release_gate_count: int
    allowed_language_count: int
    disallowed_language_count: int
    boundary_phrase_count: int
    audit_requirement_count: int
    next_step_count: int
    overclaim_count: int
    fake_citation_count: int
    word_count: int
    errors: list[str]
    warnings: list[str]
    passed: bool
    interpretation: str


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


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


def artifact_rows() -> str:
    rows = [
        "| Artifact | Exists |",
        "|---|---|",
    ]

    for path in REQUIRED_ARTIFACTS:
        rows.append(f"| `{relative(path)}` | {path.exists()} |")

    return "\n".join(rows)


def missing_artifacts() -> list[Path]:
    return [path for path in REQUIRED_ARTIFACTS if not path.exists()]


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


def render_report() -> str:
    return f"""# Public Release Checklist v4.5

## Question
Can Viruse Fabric convert the v4.4 public release bundle index into an executable checklist for cautious public use?

## Status
Current project status remains:

`research prototype with internal validation`

This checklist is not externally validated, not submission-ready, and not a final paper.

It does not provide biological guidance, clinical guidance, laboratory guidance, or operational guidance.

## Source
- Bundle index: `outputs/public_release_bundle_index_v4_4.md`
- Checklist output: `outputs/public_release_checklist_v4_5.md`

## Required Artifact Check
Every artifact below must exist before the current public-safe release bundle is treated as internally complete.

{artifact_rows()}

## Release Gates
The following gates must be satisfied before any public-facing release, share, visual redesign, slide deck, landing page, or shorter summary is used.

{bullet_list(RELEASE_GATES)}

## Allowed Public Language
The following language is allowed because it preserves status, limitation, and scope.

{bullet_list(ALLOWED_PUBLIC_LANGUAGE)}

## Disallowed Public Language
The following language is disallowed public language. It must not be used as a claim, title, subtitle, caption, announcement, abstract sentence, or promotional phrase.

{bullet_list(DISALLOWED_PUBLIC_LANGUAGE)}

## Boundary Phrases
These boundary phrases should remain visible in public-facing materials.

{bullet_list(BOUNDARY_PHRASES)}

## Audit Requirements
Any transformation of the public materials must be audited again.

{bullet_list(AUDIT_REQUIREMENTS)}

## Release Procedure
1. Confirm all required artifacts exist.
2. Confirm the bundle index exists.
3. Confirm the full public preview audit passed.
4. Confirm the one-page public preview audit passed.
5. Confirm no citation placeholder has been turned into a citation.
6. Confirm no external validation is claimed.
7. Confirm no submission readiness is claimed.
8. Confirm no biological, clinical, laboratory, or operational guidance is claimed.
9. Confirm any visual, slide, landing-page, or shorter version has its own audit.
10. Confirm the final visible status remains: research prototype with internal validation.

## Checklist Use Notes
This checklist should be used as a release gate, not as a promotional summary.

A reviewer should read it before sharing any public-facing material, especially when the material has been shortened, redesigned, converted into slides, or rewritten for a non-specialist audience. The main risk is not that the project has no boundaries. The main risk is that a public-facing version quietly removes those boundaries because they are visually inconvenient.

The checklist therefore treats boundary language as part of the artifact, not as optional decoration. A release version that removes the project status, citation-placeholder warning, or internal-validation limitation should be treated as a different artifact and audited again.

This checklist also separates audience convenience from scientific readiness. A one-page preview may be suitable for orientation while still being unsuitable as a paper, evidence package, or validation claim. A technical preview may be useful for collaborators while still requiring real citations, literature positioning, external review, and independent validation before any submission-style use.

The checklist should be applied conservatively. When a phrase sounds more impressive than the current evidence supports, the phrase should be rejected. When a design choice hides limitations, the design should be rejected. Apparently clarity and honesty still need paperwork. Here it is.

## Public Release Decision Rule
A public-facing artifact may be treated as release-safe only if all of the following remain true:

- The artifact states the project status clearly.
- The artifact does not imply external validation.
- The artifact does not imply submission readiness.
- The artifact does not turn citation placeholders into real citations.
- The artifact does not provide biological, clinical, laboratory, or operational guidance.
- The artifact has an audit if it is shortened, redesigned, converted into slides, or rewritten.
- The artifact preserves enough limitation language for a reader to understand what has not been established.

If any of these conditions fail, the artifact should be revised and re-audited before use.

## Next Steps
{bullet_list(NEXT_STEPS)}

## Interpretation
The checklist turns the public release bundle into a practical gatekeeping artifact.

Its role is boring on purpose: prevent public-facing drift, stop boundary erosion, and keep the project from being inflated into claims it has not earned. Boring checklists are how serious work avoids becoming a confetti cannon of nonsense.

## Final Boundary Statement
This checklist supports controlled public-safe orientation only.

It does not certify external validation, submission readiness, biological applicability, clinical relevance, laboratory relevance, operational usefulness, or empirical adequacy.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> PublicReleaseChecklistResult:
    source_exists = SOURCE_BUNDLE_INDEX.exists()
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_artifacts()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    allowed_count = count_present_terms(report, ALLOWED_PUBLIC_LANGUAGE)
    disallowed_count = count_present_terms(report, DISALLOWED_PUBLIC_LANGUAGE)
    release_gate_count = count_present_terms(report, RELEASE_GATES)
    audit_requirement_count = count_present_terms(report, AUDIT_REQUIREMENTS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if not source_exists:
        errors.append(f"Missing source bundle index: {relative(SOURCE_BUNDLE_INDEX)}")

    if len(REQUIRED_ARTIFACTS) < 8:
        errors.append(f"Required artifact count too low: {len(REQUIRED_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing required artifacts: {len(missing)}")

    if release_gate_count < 12:
        errors.append(f"Release gate count too low: {release_gate_count}")

    if allowed_count < 9:
        errors.append(f"Allowed language count too low: {allowed_count}")

    if disallowed_count < 9:
        errors.append(f"Disallowed language count too low: {disallowed_count}")

    if boundary_count < 9:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if audit_requirement_count < 6:
        errors.append(f"Audit requirement count too low: {audit_requirement_count}")

    if next_step_count < 6:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if word_count < 850:
        errors.append(f"Word count too low for public release checklist: {word_count}")

    if word_count > 1900:
        warnings.append("Checklist is long; keep any later operational version compact and re-audited.")

    warnings.append("Checklist does not replace real literature search, external review, or external validation.")

    passed = not errors

    interpretation = (
        "The v4.5 checklist converts the public release bundle into practical "
        "release gates while preserving boundary language, citation safety, "
        "and the internal-validation status."
    )

    return PublicReleaseChecklistResult(
        title="Public Release Checklist v4.5",
        source_bundle_index=SOURCE_BUNDLE_INDEX,
        output_path=OUTPUT_PATH,
        source_exists=source_exists,
        required_artifact_count=len(REQUIRED_ARTIFACTS),
        missing_artifact_count=len(missing),
        release_gate_count=release_gate_count,
        allowed_language_count=allowed_count,
        disallowed_language_count=disallowed_count,
        boundary_phrase_count=boundary_count,
        audit_requirement_count=audit_requirement_count,
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

    print("Public Release Checklist v4.5")
    print(f"Source bundle index: {result.source_bundle_index.relative_to(PROJECT_ROOT)}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source exists: {result.source_exists}")
    print(f"Required artifact count: {result.required_artifact_count}")
    print(f"Missing artifact count: {result.missing_artifact_count}")
    print(f"Release gate count: {result.release_gate_count}")
    print(f"Allowed language count: {result.allowed_language_count}")
    print(f"Disallowed language count: {result.disallowed_language_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Audit requirement count: {result.audit_requirement_count}")
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
