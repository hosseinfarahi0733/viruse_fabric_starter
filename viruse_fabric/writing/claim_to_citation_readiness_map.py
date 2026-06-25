"""Claim-to-citation readiness map for Viruse Fabric v4.9.

This module generates a readiness map for project claims.

It classifies each claim by:
- citation need,
- evidence need,
- source status,
- manuscript readiness,
- public-use readiness,
- validation boundary.

It does not add citations.
It does not invent sources.
It does not claim that literature search has been completed.

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
    PROJECT_ROOT,
)


OUTPUT_PATH = PROJECT_ROOT / "outputs" / "claim_to_citation_readiness_map_v4_9.md"

SOURCE_PROTOCOL_PATH = PROJECT_ROOT / "outputs" / "literature_search_protocol_v4_7.md"
SOURCE_MATRIX_PATH = PROJECT_ROOT / "outputs" / "literature_family_evidence_matrix_v4_8.md"
SOURCE_PLACEHOLDER_PLAN_PATH = PROJECT_ROOT / "outputs" / "citation_placeholder_plan_v3_9.md"
SOURCE_MANUSCRIPT_PATH = PROJECT_ROOT / "outputs" / "integrated_manuscript_draft_v3_7.md"


SOURCE_ARTIFACTS = [
    SOURCE_PROTOCOL_PATH,
    SOURCE_MATRIX_PATH,
    SOURCE_PLACEHOLDER_PLAN_PATH,
    SOURCE_MANUSCRIPT_PATH,
]


READINESS_CATEGORIES = [
    "literature-needed",
    "internal-status",
    "boundary-rule",
    "release-governance",
    "future-validation-needed",
    "manuscript-development-rule",
]


CITATION_ACTIONS = [
    "requires real source before citation insertion",
    "citation optional only if discussing standards",
    "no citation required for internal status",
    "no citation required for boundary rule",
    "future validation evidence required before stronger claim",
    "do not cite until source is read and mapped",
]


CLAIM_USE_LEVELS = [
    "safe for internal documentation",
    "safe for cautious public orientation",
    "allowed in manuscript with boundary language",
    "allowed in manuscript only after real source mapping",
    "not allowed as submission-style claim yet",
    "not allowed as external-validation claim",
]


EVIDENCE_NEEDS = [
    "literature positioning",
    "terminology grounding",
    "contrast source",
    "context source",
    "methodological standard",
    "future external validation",
    "internal audit trail",
    "no evidence needed beyond boundary discipline",
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
    "no citation is added by this map",
    "no source is added by this map",
]


MAP_RULES = [
    "Every claim must be classified before citation insertion.",
    "No claim may receive a citation until a real source is found and read.",
    "No source may be cited only because it sounds related.",
    "Internal project status claims do not become external validation claims.",
    "Boundary rules do not need decorative citations.",
    "Literature-needed claims require source mapping before manuscript use.",
    "Future-validation-needed claims cannot be strengthened by literature citation alone.",
    "Public-use readiness is not the same as submission readiness.",
    "A claim may be clear and still not be citation-ready.",
    "A claim may be citation-ready and still not be externally validated.",
]


PROHIBITED_BEHAVIORS = [
    "Do not add invented citations.",
    "Do not add invented sources.",
    "Do not convert placeholders into citations.",
    "Do not cite unread sources.",
    "Do not use citation language to imply external validation.",
    "Do not use manuscript language that implies submission readiness.",
    "Do not turn boundary claims into scientific findings.",
    "Do not turn public orientation into empirical validation.",
    "Do not add biological, clinical, laboratory, or operational guidance.",
    "Do not hide claim categories that still need future validation.",
]


NEXT_STEPS = [
    "Use the v4.8 matrix as the source intake structure.",
    "Run real searches using the v4.7 protocol.",
    "Populate source rows only after real search.",
    "Map every candidate source to one claim category.",
    "Separate support, contrast, context, terminology, method, and boundary roles.",
    "Audit populated rows before manuscript citation use.",
    "Revise manuscript claims only after sources are mapped.",
    "Create a citation-grounded manuscript revision after evidence mapping.",
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
    "not externally",
    "not submission",
    "not a final",
    "not biological",
    "not clinical",
    "not laboratory",
    "not operational",
    "citation placeholders are not citations",
    "boundary",
    "prohibited",
    "future validation",
    "cannot be strengthened",
    "claim may be",
    "not allowed",
]


SAFE_SECTION_HEADINGS = [
    "boundary phrases",
    "map rules",
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
class ClaimToCitationReadinessMapResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    claim_count: int
    readiness_category_count: int
    citation_action_count: int
    claim_use_level_count: int
    evidence_need_count: int
    map_row_count: int
    citation_ready_count: int
    literature_needed_count: int
    future_validation_needed_count: int
    boundary_rule_count: int
    internal_status_count: int
    source_added_count: int
    citation_added_count: int
    boundary_phrase_count: int
    map_rule_count: int
    prohibited_behavior_count: int
    next_step_count: int
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


def short_claim(index: int, claim: str) -> str:
    cleaned = claim.strip()
    if len(cleaned) > 80:
        cleaned = cleaned[:77].rstrip() + "..."
    return f"C{index:02d}: {cleaned}"


def classify_claim(claim: str, status: str, needs_literature: str) -> dict[str, str]:
    claim_lower = claim.lower()
    status_lower = status.lower()
    needs_lower = needs_literature.lower()

    if "external validation" in claim_lower or "externally validated" in claim_lower:
        return {
            "readiness": "boundary-rule",
            "citation_action": "no citation required for boundary rule",
            "evidence_need": "no evidence needed beyond boundary discipline",
            "public_use": "safe for cautious public orientation",
            "manuscript_use": "allowed in manuscript with boundary language",
            "validation_boundary": "must not imply external validation",
        }

    if "biological" in claim_lower or "clinical" in claim_lower or "laboratory" in claim_lower or "operational" in claim_lower:
        return {
            "readiness": "boundary-rule",
            "citation_action": "no citation required for boundary rule",
            "evidence_need": "no evidence needed beyond boundary discipline",
            "public_use": "safe for cautious public orientation",
            "manuscript_use": "allowed in manuscript with boundary language",
            "validation_boundary": "must not become guidance",
        }

    if "citation placeholders" in claim_lower:
        return {
            "readiness": "boundary-rule",
            "citation_action": "no citation required for boundary rule",
            "evidence_need": "internal audit trail",
            "public_use": "safe for internal documentation",
            "manuscript_use": "allowed in manuscript with boundary language",
            "validation_boundary": "citation integrity rule",
        }

    if "internal project status" in status_lower or "internal validation only" in needs_lower:
        return {
            "readiness": "internal-status",
            "citation_action": "no citation required for internal status",
            "evidence_need": "internal audit trail",
            "public_use": "safe for cautious public orientation",
            "manuscript_use": "allowed in manuscript with boundary language",
            "validation_boundary": "internal validation only",
        }

    if "release-governance" in status_lower or "release" in status_lower:
        return {
            "readiness": "release-governance",
            "citation_action": "citation optional only if discussing standards",
            "evidence_need": "internal audit trail",
            "public_use": "safe for internal documentation",
            "manuscript_use": "not a scientific claim",
            "validation_boundary": "release readiness is not scientific validation",
        }

    if "requires literature positioning" in status_lower:
        return {
            "readiness": "literature-needed",
            "citation_action": "requires real source before citation insertion",
            "evidence_need": "literature positioning",
            "public_use": "safe for cautious public orientation with boundary language",
            "manuscript_use": "allowed in manuscript only after real source mapping",
            "validation_boundary": "literature support is not external validation",
        }

    if "validation" in claim_lower:
        return {
            "readiness": "future-validation-needed",
            "citation_action": "future validation evidence required before stronger claim",
            "evidence_need": "future external validation",
            "public_use": "not allowed as external-validation claim",
            "manuscript_use": "not allowed as submission-style claim yet",
            "validation_boundary": "requires future validation",
        }

    return {
        "readiness": "manuscript-development-rule",
        "citation_action": "do not cite until source is read and mapped",
        "evidence_need": "context source",
        "public_use": "safe for internal documentation",
        "manuscript_use": "allowed in manuscript with boundary language",
        "validation_boundary": "development rule only",
    }


def map_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    for index, item in enumerate(CLAIM_CATEGORIES, start=1):
        claim = item["claim"]
        needs = item["needs_literature"]
        status = item["status"]
        classified = classify_claim(claim, status, needs)

        rows.append(
            {
                "claim_id": f"C{index:02d}",
                "claim": short_claim(index, claim),
                "protocol_status": status,
                "literature_need": needs,
                "readiness": classified["readiness"],
                "citation_action": classified["citation_action"],
                "evidence_need": classified["evidence_need"],
                "public_use": classified["public_use"],
                "manuscript_use": classified["manuscript_use"],
                "validation_boundary": classified["validation_boundary"],
                "source_added": "0",
                "citation_added": "0",
            }
        )

    return rows


def render_source_table() -> str:
    rows = [
        "| Source artifact | Exists |",
        "|---|---|",
    ]

    for path in SOURCE_ARTIFACTS:
        rows.append(f"| `{relative(path)}` | {path.exists()} |")

    return "\n".join(rows)


def render_claim_table() -> str:
    rows = [
        "| Claim ID | Claim | Readiness | Citation action | Evidence need | Public use | Manuscript use | Validation boundary | Sources added | Citations added |",
        "|---|---|---|---|---|---|---|---|---:|---:|",
    ]

    for row in map_rows():
        rows.append(
            "| {claim_id} | {claim} | {readiness} | {citation_action} | {evidence_need} | {public_use} | {manuscript_use} | {validation_boundary} | {source_added} | {citation_added} |".format(
                **row
            )
        )

    return "\n".join(rows)


def render_category_summary() -> str:
    rows = [
        "| Readiness category | Claim count |",
        "|---|---:|",
    ]

    data = map_rows()

    for category in READINESS_CATEGORIES:
        count = sum(1 for row in data if row["readiness"] == category)
        rows.append(f"| {category} | {count} |")

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
    return f"""# Claim-to-Citation Readiness Map v4.9

## Question
Can Viruse Fabric classify its current claims by citation readiness before adding sources, citations, or submission-style language?

## Status
Current project status remains:

`research prototype with internal validation`

This map is not externally validated, not submission-ready, and not a final paper.

No citation is added by this map. No source is added by this map. Citation placeholders are not citations.

## Source Artifacts
{render_source_table()}

## Purpose
The v4.9 map determines what each claim is allowed to become next.

It separates literature-needed claims from internal status claims, boundary rules, release-governance statements, future-validation claims, and manuscript-development rules. This prevents a future manuscript revision from treating every sentence as if it needs the same kind of source, which is how citation sections become ornamental furniture.

## Readiness Category Summary
{render_category_summary()}

## Claim-to-Citation Map
Source added count: 0

Citation added count: 0

{render_claim_table()}

## Citation Actions
{bullet_list(CITATION_ACTIONS)}

## Claim Use Levels
{bullet_list(CLAIM_USE_LEVELS)}

## Evidence Needs
{bullet_list(EVIDENCE_NEEDS)}

## Map Rules
{bullet_list(MAP_RULES)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Interpretation
This map does not make the manuscript citation-grounded by itself.

It prepares the next step by telling the project which claims need literature positioning, which claims are internal project-status statements, which claims are boundary rules, and which claims would require future validation before stronger language is allowed.

A claim can be important and still not citation-ready. A claim can be clear and still need literature positioning. A claim can be useful for public orientation and still not be allowed as a submission-style statement. These distinctions are tedious, but less tedious than retracting inflated claims later while pretending everyone meant the cautious version all along.

## Claim Readiness Notes
The map treats citation readiness as a controlled transition rather than a decoration step.

A literature-needed claim is not wrong merely because it still needs sources. It is simply unfinished from a manuscript perspective. Those claims should remain available for internal development and cautious public orientation, but they should not be upgraded into submission-style claims until real sources have been found, read, mapped, and audited.

An internal-status claim serves a different function. It describes where the project currently stands. It should not be cited as if it were a scientific result, because it is not trying to be one. The status statement "research prototype with internal validation" is a project boundary, not a discovered law of nature. The universe, somehow, will survive this distinction.

A boundary-rule claim is also different. Sentences such as "not externally validated" or "not clinical guidance" protect the scope of the project. They do not need decorative citations. Adding citations to boundary rules can actually make the text less clear by suggesting that the boundary depends on a source rather than on the project's actual evidentiary status.

## Manuscript Integration Notes
Future manuscript revision should use this map conservatively.

If a claim is marked literature-needed, the manuscript should either keep it as a clearly framed conceptual claim or wait until source mapping is complete. If a claim is marked future-validation-needed, it should not be strengthened by literature citations alone. Literature can contextualize a claim, but it cannot perform validation that has not happened.

If a claim is marked boundary-rule, the manuscript should preserve it visibly. Removing boundary language to make prose smoother would make the manuscript more polished and less honest, which is a classic human achievement and therefore banned here.

The map also protects against citation laundering. A source should not be used to make a claim look stronger than the source actually allows. A source can support terminology, provide contrast, supply historical context, or motivate a comparison. It cannot automatically validate the Viruse Fabric framework.

## Public Communication Notes
Public-facing use should follow the same distinctions.

A claim that is safe for cautious public orientation is not automatically safe for a paper abstract, grant proposal, or submission cover letter. Public orientation explains what the project is trying to do. Submission language implies a higher standard of evidence, positioning, and external scrutiny.

This distinction matters because public summaries tend to compress nuance first. If a claim loses its boundary phrase during compression, it should be treated as a changed claim and re-audited. A shorter sentence is not always a clearer sentence; sometimes it is just a more efficient mistake.

## Final Boundary Statement
This map prepares future citation-grounded revision.

It does not provide citations, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> ClaimToCitationReadinessMapResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    rows = map_rows()
    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    citation_ready_count = sum(
        1
        for row in rows
        if row["citation_action"] in {
            "requires real source before citation insertion",
            "citation optional only if discussing standards",
        }
    )
    literature_needed_count = sum(1 for row in rows if row["readiness"] == "literature-needed")
    future_validation_needed_count = sum(1 for row in rows if row["readiness"] == "future-validation-needed")
    boundary_rule_count = sum(1 for row in rows if row["readiness"] == "boundary-rule")
    internal_status_count = sum(1 for row in rows if row["readiness"] == "internal-status")
    source_added_count = sum(int(row["source_added"]) for row in rows)
    citation_added_count = sum(int(row["citation_added"]) for row in rows)

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    map_rule_count = count_present_terms(report, MAP_RULES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 4:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if len(rows) < 8:
        errors.append(f"Claim count too low: {len(rows)}")

    if len(READINESS_CATEGORIES) < 6:
        errors.append(f"Readiness category count too low: {len(READINESS_CATEGORIES)}")

    if len(CITATION_ACTIONS) < 6:
        errors.append(f"Citation action count too low: {len(CITATION_ACTIONS)}")

    if len(CLAIM_USE_LEVELS) < 6:
        errors.append(f"Claim use level count too low: {len(CLAIM_USE_LEVELS)}")

    if len(EVIDENCE_NEEDS) < 8:
        errors.append(f"Evidence need count too low: {len(EVIDENCE_NEEDS)}")

    if literature_needed_count < 2:
        errors.append(f"Literature-needed claim count too low: {literature_needed_count}")

    if boundary_rule_count < 3:
        errors.append(f"Boundary rule count too low: {boundary_rule_count}")

    if internal_status_count < 1:
        errors.append(f"Internal status count too low: {internal_status_count}")

    if source_added_count != 0:
        errors.append(f"Source added count should be zero, got: {source_added_count}")

    if citation_added_count != 0:
        errors.append(f"Citation added count should be zero, got: {citation_added_count}")

    if boundary_count < 10:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if map_rule_count < 10:
        errors.append(f"Map rule count too low: {map_rule_count}")

    if prohibited_count < 10:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if word_count < 1300:
        errors.append(f"Word count too low for claim-to-citation readiness map: {word_count}")

    warnings.append("Map adds no citations; real literature search must happen later.")
    warnings.append("Citation readiness does not imply external validation or submission readiness.")

    passed = not errors

    interpretation = (
        "The v4.9 map classifies current claims by citation readiness, "
        "evidence need, allowed use, and validation boundary without adding "
        "sources or citations."
    )

    return ClaimToCitationReadinessMapResult(
        title="Claim-to-Citation Readiness Map v4.9",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        claim_count=len(rows),
        readiness_category_count=len(READINESS_CATEGORIES),
        citation_action_count=len(CITATION_ACTIONS),
        claim_use_level_count=len(CLAIM_USE_LEVELS),
        evidence_need_count=len(EVIDENCE_NEEDS),
        map_row_count=len(rows),
        citation_ready_count=citation_ready_count,
        literature_needed_count=literature_needed_count,
        future_validation_needed_count=future_validation_needed_count,
        boundary_rule_count=boundary_rule_count,
        internal_status_count=internal_status_count,
        source_added_count=source_added_count,
        citation_added_count=citation_added_count,
        boundary_phrase_count=boundary_count,
        map_rule_count=map_rule_count,
        prohibited_behavior_count=prohibited_count,
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

    print("Claim-to-Citation Readiness Map v4.9")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Claim count: {result.claim_count}")
    print(f"Readiness category count: {result.readiness_category_count}")
    print(f"Citation action count: {result.citation_action_count}")
    print(f"Claim use level count: {result.claim_use_level_count}")
    print(f"Evidence need count: {result.evidence_need_count}")
    print(f"Map row count: {result.map_row_count}")
    print(f"Citation-ready count: {result.citation_ready_count}")
    print(f"Literature-needed count: {result.literature_needed_count}")
    print(f"Future-validation-needed count: {result.future_validation_needed_count}")
    print(f"Boundary rule count: {result.boundary_rule_count}")
    print(f"Internal status count: {result.internal_status_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Map rule count: {result.map_rule_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
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
