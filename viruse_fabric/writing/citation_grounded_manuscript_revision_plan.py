"""Citation-grounded manuscript revision plan for Viruse Fabric v5.0.

This module generates a revision plan for the integrated manuscript.

It connects:
- the v3.7 integrated manuscript draft,
- the v4.7 literature search protocol,
- the v4.8 literature family evidence matrix,
- the v4.9 claim-to-citation readiness map.

It does not add citations.
It does not add sources.
It does not revise the manuscript text.
It does not claim that literature search has been completed.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "citation_grounded_manuscript_revision_plan_v5_0.md"

SOURCE_MANUSCRIPT = PROJECT_ROOT / "outputs" / "integrated_manuscript_draft_v3_7.md"
SOURCE_MANUSCRIPT_AUDIT = PROJECT_ROOT / "outputs" / "integrated_manuscript_quality_audit_v3_8.md"
SOURCE_CITATION_PLAN = PROJECT_ROOT / "outputs" / "citation_placeholder_plan_v3_9.md"
SOURCE_SEARCH_PROTOCOL = PROJECT_ROOT / "outputs" / "literature_search_protocol_v4_7.md"
SOURCE_EVIDENCE_MATRIX = PROJECT_ROOT / "outputs" / "literature_family_evidence_matrix_v4_8.md"
SOURCE_CLAIM_MAP = PROJECT_ROOT / "outputs" / "claim_to_citation_readiness_map_v4_9.md"

SOURCE_ARTIFACTS = [
    SOURCE_MANUSCRIPT,
    SOURCE_MANUSCRIPT_AUDIT,
    SOURCE_CITATION_PLAN,
    SOURCE_SEARCH_PROTOCOL,
    SOURCE_EVIDENCE_MATRIX,
    SOURCE_CLAIM_MAP,
]


REVISION_TARGETS = [
    {
        "section": "Abstract / Summary",
        "revision_need": "keep conceptual thesis but avoid external-validation language",
        "citation_dependency": "claim map and real literature sources required before stronger positioning",
        "status": "plan only",
    },
    {
        "section": "Introduction",
        "revision_need": "connect the core thesis to constraint, causality, emergence, and teleonomy literature",
        "citation_dependency": "literature-needed claims require real source mapping",
        "status": "plan only",
    },
    {
        "section": "Related Work",
        "revision_need": "replace placeholder positioning with source-grounded literature families",
        "citation_dependency": "v4.7 protocol and v4.8 matrix must be populated later",
        "status": "requires future real search",
    },
    {
        "section": "Formal Model",
        "revision_need": "distinguish project formalism from cited background concepts",
        "citation_dependency": "citation only for background, terminology, or comparison",
        "status": "plan only",
    },
    {
        "section": "Internal Validation",
        "revision_need": "preserve internal-only status and avoid external validation claims",
        "citation_dependency": "no citation can convert internal validation into external validation",
        "status": "boundary protected",
    },
    {
        "section": "Interpretation",
        "revision_need": "separate conceptual interpretation from empirical or operational claims",
        "citation_dependency": "source roles must distinguish support, contrast, context, terminology, method, and boundary",
        "status": "plan only",
    },
    {
        "section": "Limitations",
        "revision_need": "strengthen boundary language after citation integration",
        "citation_dependency": "boundary claims remain visible even after literature is added",
        "status": "boundary protected",
    },
    {
        "section": "Future Work",
        "revision_need": "make external validation and real evidence collection explicit future tasks",
        "citation_dependency": "future-validation-needed claims cannot be upgraded by literature citation alone",
        "status": "future validation required",
    },
]


REVISION_PHASES = [
    "Review v4.9 claim-to-citation readiness map.",
    "Run real literature searches using v4.7 protocol.",
    "Populate v4.8 evidence matrix with real candidate sources.",
    "Audit populated evidence matrix before manuscript use.",
    "Revise related work using retained sources only.",
    "Revise manuscript claims according to citation action and validation boundary.",
    "Re-run manuscript overclaim and fake-citation audit.",
    "Create a citation-grounded manuscript draft only after source mapping is complete.",
]


MANUSCRIPT_GATES = [
    "No citation is inserted before a source is found through real search.",
    "No citation is inserted before the relevant source passage is read.",
    "No citation is inserted before the source is mapped to a claim.",
    "No placeholder is converted into a citation.",
    "No source is used as decorative authority.",
    "No literature citation is used to imply external validation.",
    "No internal validation claim is upgraded into external validation.",
    "No submission-ready language is used.",
    "No biological, clinical, laboratory, or operational guidance is added.",
    "No visual or public artifact is treated as manuscript evidence.",
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
    "no citation is added by this plan",
    "no source is added by this plan",
    "manuscript is not revised by this plan",
]


READINESS_STATEMENTS = [
    "ready for citation-grounded revision planning",
    "not ready for citation insertion",
    "not ready for submission",
    "requires real literature search",
    "requires populated evidence matrix",
    "requires source audit before manuscript use",
    "requires overclaim audit after revision",
    "requires fake-citation audit after revision",
]


PROHIBITED_BEHAVIORS = [
    "Do not add invented citations.",
    "Do not add invented sources.",
    "Do not cite unread sources.",
    "Do not cite a source only because it sounds related.",
    "Do not use citations to imply external validation.",
    "Do not describe the manuscript as submission-ready.",
    "Do not hide internal-validation boundaries.",
    "Do not convert public orientation readiness into manuscript readiness.",
    "Do not add biological, clinical, laboratory, or operational guidance.",
    "Do not revise manuscript claims before evidence mapping is complete.",
]


NEXT_STEPS = [
    "Create a real search log structure.",
    "Run literature searches family by family.",
    "Populate the evidence matrix with candidate sources.",
    "Audit populated matrix rows.",
    "Retain, defer, or reject sources.",
    "Create citation-grounded related-work notes.",
    "Draft a citation-grounded manuscript revision.",
    "Audit the revised manuscript before any submission-style use.",
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
    "must not",
    "no citation",
    "no source",
    "no placeholder",
    "no literature citation",
    "boundary",
    "prohibited",
    "requires",
    "future",
    "internal validation",
    "not externally",
    "not submission",
    "not a final",
    "not biological",
    "not clinical",
    "not laboratory",
    "not operational",
    "citation placeholders are not citations",
    "cannot be upgraded",
]


SAFE_SECTION_HEADINGS = [
    "boundary phrases",
    "manuscript revision gates",
    "prohibited behaviors",
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
class CitationGroundedManuscriptRevisionPlanResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    revision_target_count: int
    revision_phase_count: int
    manuscript_gate_count: int
    boundary_phrase_count: int
    readiness_statement_count: int
    prohibited_behavior_count: int
    next_step_count: int
    source_added_count: int
    citation_added_count: int
    manuscript_revised_count: int
    overclaim_count: int
    fake_citation_count: int
    word_count: int
    errors: list[str]
    warnings: list[str]
    passed: bool
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


def missing_sources() -> list[Path]:
    return [path for path in SOURCE_ARTIFACTS if not path.exists()]


def render_source_table() -> str:
    rows = [
        "| Source artifact | Exists |",
        "|---|---|",
    ]
    for path in SOURCE_ARTIFACTS:
        rows.append(f"| `{relative(path)}` | {path.exists()} |")
    return "\n".join(rows)


def render_revision_target_table() -> str:
    rows = [
        "| Manuscript area | Revision need | Citation dependency | Status |",
        "|---|---|---|---|",
    ]
    for item in REVISION_TARGETS:
        rows.append(
            f"| {item['section']} | {item['revision_need']} | {item['citation_dependency']} | {item['status']} |"
        )
    return "\n".join(rows)


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
    return f"""# Citation-Grounded Manuscript Revision Plan v5.0

## Question
Can Viruse Fabric create a manuscript revision plan that connects citation protocol, evidence matrix, and claim readiness without adding citations, adding sources, or revising the manuscript prematurely?

## Status
Current project status remains:

`research prototype with internal validation`

This plan is not externally validated, not submission-ready, and not a final paper.

No citation is added by this plan. No source is added by this plan. The manuscript is not revised by this plan. Citation placeholders are not citations.

## Source Artifacts
{render_source_table()}

## Purpose
The v5.0 plan defines how the existing manuscript should later be revised once real literature search and evidence mapping have happened.

It is a bridge from preparation to source-grounded revision. It does not perform the revision. That distinction matters because changing a manuscript before the evidence exists is not scholarship; it is just typing with ambition.

## Revision Target Map
{render_revision_target_table()}

## Revision Phases
{bullet_list(REVISION_PHASES)}

## Manuscript Revision Gates
{bullet_list(MANUSCRIPT_GATES)}

## Readiness Statements
{bullet_list(READINESS_STATEMENTS)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Integration Logic
The v4.7 protocol defines how searches should be performed.

The v4.8 evidence matrix defines where real sources should be recorded.

The v4.9 claim map defines what each claim is allowed to become before citation insertion.

The v5.0 plan connects those artifacts to the manuscript. It tells the project which manuscript areas will need revision, what kind of citation dependency they have, and which gates must be passed before the manuscript changes.

## Revision Discipline
A manuscript revision should not treat all claims equally.

Some claims need literature positioning. Some claims are internal status statements. Some are boundary rules. Some are future-validation statements. A citation can help position a claim, but it cannot validate a result that has not been externally validated. This is apparently difficult enough for civilization that the plan writes it down again.

The manuscript should preserve visible limitation language after citations are added. Adding sources often makes prose sound more authoritative. That authority must not leak into claims the project has not earned.

## Manuscript Section Handling
The manuscript should be revised section by section, not as a single global rewrite.

The introduction should receive literature only after the relevant families have real retained sources. Related work should be the most citation-dependent section, because it is where the project must show what it is near, what it differs from, and what it must not pretend to have replaced. The formal model should cite only background, terminology, or comparison sources, while preserving the fact that the Viruse Fabric formalism itself is internally developed.

The internal validation section should remain especially cautious. It may cite methodological standards later if useful, but citations must not transform internal validation into external validation. That would be a very efficient way to manufacture confusion and then call it maturity.

The limitations section should not shrink after citations are added. If anything, citation-grounded revision should make the boundaries clearer, because literature positioning usually reveals more nearby work, more uncertainty, and more reasons to avoid heroic language.

## Source Integration Order
Source integration should follow a strict order.

First, real searches must be run using the protocol. Second, candidate sources must be placed into the evidence matrix. Third, each source must be mapped to a claim and assigned a role. Fourth, the populated matrix must be audited. Only then should citations enter the manuscript.

This order matters because adding citations directly into prose creates a false sense of completion. The manuscript may look more scholarly while becoming less controlled. Apparently formatting can fool human brains; shocking development, filed under "obvious but still dangerous."

## Revision Output Boundary
The output of this milestone is only a plan.

It is not a revised manuscript. It is not a citation-grounded manuscript draft. It is not a bibliography. It is not a literature review. It is not a submission package. It is a controlled bridge toward those later artifacts.

A later milestone may create a populated evidence matrix, but only after real search. A later milestone may create citation-grounded related-work notes, but only after sources are retained. A later milestone may revise the manuscript, but only after the source audit passes.

## Output Counts
Source added count: 0

Citation added count: 0

Manuscript revised count: 0

## Final Boundary Statement
This plan prepares citation-grounded manuscript revision.

It does not provide citations, does not add sources, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> CitationGroundedManuscriptRevisionPlanResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    source_added_count = 0
    citation_added_count = 0
    manuscript_revised_count = 0

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    readiness_count = count_present_terms(report, READINESS_STATEMENTS)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    gate_count = count_present_terms(report, MANUSCRIPT_GATES)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 6:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if len(REVISION_TARGETS) < 8:
        errors.append(f"Revision target count too low: {len(REVISION_TARGETS)}")

    if len(REVISION_PHASES) < 8:
        errors.append(f"Revision phase count too low: {len(REVISION_PHASES)}")

    if gate_count < 10:
        errors.append(f"Manuscript gate count too low: {gate_count}")

    if boundary_count < 11:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if readiness_count < 8:
        errors.append(f"Readiness statement count too low: {readiness_count}")

    if prohibited_count < 10:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    if source_added_count != 0:
        errors.append(f"Source added count should be zero, got: {source_added_count}")

    if citation_added_count != 0:
        errors.append(f"Citation added count should be zero, got: {citation_added_count}")

    if manuscript_revised_count != 0:
        errors.append(f"Manuscript revised count should be zero, got: {manuscript_revised_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if word_count < 1100:
        errors.append(f"Word count too low for citation-grounded manuscript revision plan: {word_count}")

    warnings.append("Plan adds no citations; real literature search and source mapping must happen later.")
    warnings.append("Plan does not revise the manuscript or make it submission-ready.")

    passed = not errors

    interpretation = (
        "The v5.0 plan connects the literature search protocol, evidence matrix, "
        "and claim readiness map to future manuscript revision without adding "
        "sources, citations, or manuscript changes."
    )

    return CitationGroundedManuscriptRevisionPlanResult(
        title="Citation-Grounded Manuscript Revision Plan v5.0",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        revision_target_count=len(REVISION_TARGETS),
        revision_phase_count=len(REVISION_PHASES),
        manuscript_gate_count=gate_count,
        boundary_phrase_count=boundary_count,
        readiness_statement_count=readiness_count,
        prohibited_behavior_count=prohibited_count,
        next_step_count=next_step_count,
        source_added_count=source_added_count,
        citation_added_count=citation_added_count,
        manuscript_revised_count=manuscript_revised_count,
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

    print("Citation-Grounded Manuscript Revision Plan v5.0")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Revision target count: {result.revision_target_count}")
    print(f"Revision phase count: {result.revision_phase_count}")
    print(f"Manuscript gate count: {result.manuscript_gate_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Readiness statement count: {result.readiness_statement_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
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
