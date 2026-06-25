"""Literature family evidence matrix for Viruse Fabric v4.8.

This module generates an empty evidence matrix for future real sources.

It does not add citations.
It does not invent sources.
It does not claim that any literature search has already been completed.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable

from viruse_fabric.writing.literature_search_protocol import (
    CLAIM_CATEGORIES,
    LITERATURE_FAMILIES,
    PROJECT_ROOT,
)


SOURCE_PROTOCOL_PATH = PROJECT_ROOT / "outputs" / "literature_search_protocol_v4_7.md"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "literature_family_evidence_matrix_v4_8.md"


SOURCE_STATUS_VALUES = [
    "empty pending real search",
    "candidate pending review",
    "retained after reading",
    "deferred after review",
    "rejected after review",
]


SOURCE_ROLE_VALUES = [
    "support",
    "contrast",
    "context",
    "terminology",
    "method",
    "boundary",
]


DECISION_VALUES = [
    "pending real search",
    "retain",
    "defer",
    "reject",
]


EVIDENCE_FIELDS = [
    "literature family",
    "claim category",
    "source title",
    "authors",
    "venue",
    "year",
    "search venue",
    "query string",
    "source role",
    "relevant passage summary",
    "boundary note",
    "decision",
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
    "no source is added by this matrix",
    "empty pending real search",
]


MATRIX_RULES = [
    "Every row starts empty.",
    "No source title may be inserted before real search.",
    "No author name may be inserted before real search.",
    "No venue may be inserted before real search.",
    "No year may be inserted before real search.",
    "No citation may be added from this matrix alone.",
    "A retained source must be read before manuscript use.",
    "A source must map to a specific claim category.",
    "A source must have a source role.",
    "A source must have a boundary note before citation insertion.",
]


NEXT_STEPS = [
    "Use the v4.7 search protocol to run real searches.",
    "Record search venue, query string, and search date.",
    "Add candidate sources only after they are found through real search.",
    "Read the relevant source passage before retaining a source.",
    "Classify each source as support, contrast, context, terminology, method, or boundary.",
    "Reject decorative citations.",
    "Re-audit the evidence matrix after candidate sources are added.",
    "Do not revise the manuscript with citations until sources are mapped.",
]


PROHIBITED_BEHAVIORS = [
    "Do not invent source titles.",
    "Do not invent authors.",
    "Do not invent venues.",
    "Do not invent years.",
    "Do not treat a query as a citation.",
    "Do not treat a placeholder as a citation.",
    "Do not imply external validation.",
    "Do not imply submission readiness.",
    "Do not add biological, clinical, laboratory, or operational guidance.",
    "Do not hide contrast sources because they are inconvenient.",
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
    "no source",
    "no citation",
    "no author",
    "no venue",
    "no year",
    "empty",
    "pending",
    "placeholder",
    "boundary",
    "prohibited",
    "rules",
    "not externally",
    "not submission",
    "not a final",
    "not biological",
    "not clinical",
    "not laboratory",
    "not operational",
    "citation placeholders are not citations",
]


SAFE_SECTION_HEADINGS = [
    "boundary phrases",
    "matrix rules",
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
class LiteratureFamilyEvidenceMatrixResult:
    title: str
    output_path: Path
    source_protocol_exists: bool
    literature_family_count: int
    claim_category_count: int
    matrix_row_count: int
    source_status_count: int
    source_role_count: int
    decision_value_count: int
    evidence_field_count: int
    boundary_phrase_count: int
    matrix_rule_count: int
    next_step_count: int
    prohibited_behavior_count: int
    populated_source_count: int
    invented_source_count: int
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


def short_claim_key(index: int, claim: str) -> str:
    cleaned = claim.strip()
    if len(cleaned) > 72:
        cleaned = cleaned[:69].rstrip() + "..."
    return f"C{index:02d}: {cleaned}"


def expected_role_for(family: str, claim_status: str) -> str:
    lowered_family = family.lower()
    lowered_status = claim_status.lower()

    if "boundary" in lowered_status or "internal" in lowered_status:
        return "boundary or context"

    if "causal" in lowered_family or "constraint" in lowered_family:
        return "support, contrast, or terminology"

    if "attractor" in lowered_family or "dynamical" in lowered_family:
        return "terminology, context, or contrast"

    if "teleology" in lowered_family or "purpose" in lowered_family:
        return "contrast, context, or terminology"

    if "observer" in lowered_family:
        return "context, terminology, or boundary"

    return "context, contrast, or terminology"


def required_evidence_type_for(claim_status: str) -> str:
    lowered = claim_status.lower()

    if "requires literature positioning" in lowered:
        return "source required before manuscript citation"

    if "internal" in lowered:
        return "internal status note, citation optional only if discussing standards"

    if "boundary" in lowered:
        return "boundary rule, citation not required unless standards are discussed"

    return "development rule, citation optional depending on manuscript use"


def matrix_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    for family_index, family_item in enumerate(LITERATURE_FAMILIES, start=1):
        family_name = family_item["family"]

        for claim_index, claim_item in enumerate(CLAIM_CATEGORIES, start=1):
            claim = claim_item["claim"]
            status = claim_item["status"]

            rows.append(
                {
                    "row_id": f"LF{family_index:02d}-C{claim_index:02d}",
                    "family": family_name,
                    "claim": short_claim_key(claim_index, claim),
                    "expected_role": expected_role_for(family_name, status),
                    "required_evidence_type": required_evidence_type_for(status),
                    "source_status": "empty pending real search",
                    "source_count": "0",
                    "decision": "pending real search",
                }
            )

    return rows


def render_matrix_table() -> str:
    rows = [
        "| Row ID | Literature family | Claim category | Expected source role | Required evidence type | Source status | Source count | Decision |",
        "|---|---|---|---|---|---|---:|---|",
    ]

    for row in matrix_rows():
        rows.append(
            "| {row_id} | {family} | {claim} | {expected_role} | {required_evidence_type} | {source_status} | {source_count} | {decision} |".format(
                **row
            )
        )

    return "\n".join(rows)


def render_family_summary() -> str:
    rows = [
        "| Literature family | Future query count from protocol | Matrix row count | Current source count |",
        "|---|---:|---:|---:|",
    ]

    for family_item in LITERATURE_FAMILIES:
        rows.append(
            f"| {family_item['family']} | {len(family_item['queries'])} | {len(CLAIM_CATEGORIES)} | 0 |"
        )

    return "\n".join(rows)


def render_claim_summary() -> str:
    rows = [
        "| Claim category | Status from protocol | Matrix row count | Current source count |",
        "|---|---|---:|---:|",
    ]

    for claim_index, claim_item in enumerate(CLAIM_CATEGORIES, start=1):
        rows.append(
            f"| {short_claim_key(claim_index, claim_item['claim'])} | {claim_item['status']} | {len(LITERATURE_FAMILIES)} | 0 |"
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
    return f"""# Literature Family Evidence Matrix v4.8

## Question
Can Viruse Fabric create a structured evidence matrix for future real sources without inventing sources, adding citations, or weakening the literature-search protocol?

## Status
Current project status remains:

`research prototype with internal validation`

This matrix is not externally validated, not submission-ready, and not a final paper.

No source is added by this matrix. No citation is added by this matrix. Citation placeholders are not citations.

## Source Protocol
- Source protocol: `outputs/literature_search_protocol_v4_7.md`
- Source protocol exists: {SOURCE_PROTOCOL_PATH.exists()}
- Matrix output: `outputs/literature_family_evidence_matrix_v4_8.md`

## Purpose
The v4.8 matrix converts the v4.7 literature search protocol into a structured table for future evidence handling.

It prepares the project for real source collection while keeping all source slots empty. This prevents the usual academic magic trick where a matrix appears, citations appear inside it, and nobody admits they were never searched, read, or mapped.

## Literature Family Summary
{render_family_summary()}

## Claim Category Summary
{render_claim_summary()}

## Evidence Matrix
Every row is intentionally empty pending real search.

Populated source count: 0

Invented source count: 0

{render_matrix_table()}

## Evidence Fields
Future retained sources must include these fields:

{bullet_list(EVIDENCE_FIELDS)}

## Source Status Values
{bullet_list(SOURCE_STATUS_VALUES)}

## Source Role Values
{bullet_list(SOURCE_ROLE_VALUES)}

## Decision Values
{bullet_list(DECISION_VALUES)}

## Matrix Rules
{bullet_list(MATRIX_RULES)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Interpretation
The matrix creates a disciplined structure for future evidence collection.

It does not claim that evidence has been found. It does not claim that sources have been read. It does not create citations. It does not move the manuscript closer to submission by itself.

The matrix is useful because it forces every future source to answer three questions: which literature family, which claim category, and which source role. Annoying, yes. Necessary, also yes. Scholarship is mostly preventing future confusion from dressing up as insight.

## Final Boundary Statement
This matrix is an empty structure for future real literature evidence.

It does not provide citations, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> LiteratureFamilyEvidenceMatrixResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    rows = matrix_rows()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    populated_source_count = sum(1 for row in rows if row["source_count"] != "0")
    invented_source_count = 0

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    matrix_rule_count = count_present_terms(report, MATRIX_RULES)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if not SOURCE_PROTOCOL_PATH.exists():
        errors.append(f"Missing source protocol: {relative(SOURCE_PROTOCOL_PATH)}")

    if len(LITERATURE_FAMILIES) < 8:
        errors.append(f"Literature family count too low: {len(LITERATURE_FAMILIES)}")

    if len(CLAIM_CATEGORIES) < 8:
        errors.append(f"Claim category count too low: {len(CLAIM_CATEGORIES)}")

    expected_rows = len(LITERATURE_FAMILIES) * len(CLAIM_CATEGORIES)
    if len(rows) != expected_rows:
        errors.append(f"Matrix row count mismatch: {len(rows)} != {expected_rows}")

    if len(rows) < 64:
        errors.append(f"Matrix row count too low: {len(rows)}")

    if len(SOURCE_STATUS_VALUES) < 5:
        errors.append(f"Source status count too low: {len(SOURCE_STATUS_VALUES)}")

    if len(SOURCE_ROLE_VALUES) < 6:
        errors.append(f"Source role count too low: {len(SOURCE_ROLE_VALUES)}")

    if len(DECISION_VALUES) < 4:
        errors.append(f"Decision value count too low: {len(DECISION_VALUES)}")

    if len(EVIDENCE_FIELDS) < 12:
        errors.append(f"Evidence field count too low: {len(EVIDENCE_FIELDS)}")

    if boundary_count < 10:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if matrix_rule_count < 10:
        errors.append(f"Matrix rule count too low: {matrix_rule_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    if prohibited_count < 10:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if populated_source_count != 0:
        errors.append(f"Populated source count should be zero, got: {populated_source_count}")

    if invented_source_count != 0:
        errors.append(f"Invented source count should be zero, got: {invented_source_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if word_count < 1400:
        errors.append(f"Word count too low for literature family evidence matrix: {word_count}")

    warnings.append("Matrix contains no real sources; real literature search must happen later.")
    warnings.append("Any populated source rows must be audited before manuscript citation use.")

    passed = not errors

    interpretation = (
        "The v4.8 matrix creates an empty evidence structure that maps literature "
        "families to claim categories while preserving citation integrity, "
        "boundary language, and the internal-validation status."
    )

    return LiteratureFamilyEvidenceMatrixResult(
        title="Literature Family Evidence Matrix v4.8",
        output_path=OUTPUT_PATH,
        source_protocol_exists=SOURCE_PROTOCOL_PATH.exists(),
        literature_family_count=len(LITERATURE_FAMILIES),
        claim_category_count=len(CLAIM_CATEGORIES),
        matrix_row_count=len(rows),
        source_status_count=len(SOURCE_STATUS_VALUES),
        source_role_count=len(SOURCE_ROLE_VALUES),
        decision_value_count=len(DECISION_VALUES),
        evidence_field_count=len(EVIDENCE_FIELDS),
        boundary_phrase_count=boundary_count,
        matrix_rule_count=matrix_rule_count,
        next_step_count=next_step_count,
        prohibited_behavior_count=prohibited_count,
        populated_source_count=populated_source_count,
        invented_source_count=invented_source_count,
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

    print("Literature Family Evidence Matrix v4.8")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source protocol exists: {result.source_protocol_exists}")
    print(f"Literature family count: {result.literature_family_count}")
    print(f"Claim category count: {result.claim_category_count}")
    print(f"Matrix row count: {result.matrix_row_count}")
    print(f"Source status count: {result.source_status_count}")
    print(f"Source role count: {result.source_role_count}")
    print(f"Decision value count: {result.decision_value_count}")
    print(f"Evidence field count: {result.evidence_field_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Matrix rule count: {result.matrix_rule_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Populated source count: {result.populated_source_count}")
    print(f"Invented source count: {result.invented_source_count}")
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
