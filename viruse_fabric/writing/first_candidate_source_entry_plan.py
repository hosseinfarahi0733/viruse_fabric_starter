"""First candidate source entry plan for Viruse Fabric v6.0.

This module creates a controlled plan for future candidate source entry creation.

It uses the v5.9 screening decisions as input.

It plans candidate source entries only.

It does not create candidate sources.
It does not retain sources.
It does not add citations.
It does not populate the evidence matrix.
It does not revise the manuscript.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_candidate_source_entry_plan_v6_0.md"

SOURCE_SCREENING_EXECUTION = PROJECT_ROOT / "outputs" / "first_raw_result_screening_execution_v5_9.md"
SOURCE_SCREENING_PLAN = PROJECT_ROOT / "outputs" / "first_raw_result_screening_plan_v5_8.md"
SOURCE_LIVE_SEARCH = PROJECT_ROOT / "outputs" / "first_controlled_live_search_execution_v5_7.md"
SOURCE_SEARCH_AUDIT = PROJECT_ROOT / "outputs" / "first_search_run_artifact_audit_v5_6.md"
SOURCE_SEARCH_SHELL = PROJECT_ROOT / "outputs" / "first_search_run_artifact_v5_5.md"
SOURCE_SEARCH_PLAN = PROJECT_ROOT / "outputs" / "first_literature_family_search_plan_v5_4.md"
SOURCE_EMPTY_LOG = PROJECT_ROOT / "outputs" / "literature_search_log_empty_v5_2.md"
SOURCE_LOG_TEMPLATE = PROJECT_ROOT / "outputs" / "literature_search_log_template_v5_1.md"
SOURCE_CLAIM_MAP = PROJECT_ROOT / "outputs" / "claim_to_citation_readiness_map_v4_9.md"
SOURCE_EVIDENCE_MATRIX = PROJECT_ROOT / "outputs" / "literature_family_evidence_matrix_v4_8.md"

SOURCE_ARTIFACTS = [
    SOURCE_SCREENING_EXECUTION,
    SOURCE_SCREENING_PLAN,
    SOURCE_LIVE_SEARCH,
    SOURCE_SEARCH_AUDIT,
    SOURCE_SEARCH_SHELL,
    SOURCE_SEARCH_PLAN,
    SOURCE_EMPTY_LOG,
    SOURCE_LOG_TEMPLATE,
    SOURCE_CLAIM_MAP,
    SOURCE_EVIDENCE_MATRIX,
]


PLAN_METADATA = {
    "candidate_entry_plan_id": "CEP-0001",
    "linked_screening_execution_id": "SX-0001",
    "linked_search_execution_id": "SE-0001",
    "linked_screening_plan_id": "SP-0001",
    "plan_status": "planned_not_created",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "claim_category": "literature-needed: constraints shape possible trajectories",
    "screened_result_count_from_v5_9": "5",
    "pass_to_candidate_planning_count_from_v5_9": "3",
    "defer_to_candidate_planning_count_from_v5_9": "2",
    "candidate_source_count": "0",
    "retained_source_count": "0",
}


PLANNED_CANDIDATE_ENTRY_ROWS = [
    {
        "raw_result_observation_id": "raw_result_observation_01",
        "screening_decision": "defer_for_candidate_entry_planning",
        "entry_plan_status": "metadata_check_required_before_candidate_entry",
        "candidate_source_created": "no",
    },
    {
        "raw_result_observation_id": "raw_result_observation_02",
        "screening_decision": "pass_to_candidate_entry_planning",
        "entry_plan_status": "candidate_entry_planning_allowed",
        "candidate_source_created": "no",
    },
    {
        "raw_result_observation_id": "raw_result_observation_03",
        "screening_decision": "pass_to_candidate_entry_planning",
        "entry_plan_status": "candidate_entry_planning_allowed",
        "candidate_source_created": "no",
    },
    {
        "raw_result_observation_id": "raw_result_observation_04",
        "screening_decision": "defer_for_candidate_entry_planning",
        "entry_plan_status": "metadata_check_required_before_candidate_entry",
        "candidate_source_created": "no",
    },
    {
        "raw_result_observation_id": "raw_result_observation_05",
        "screening_decision": "pass_to_candidate_entry_planning",
        "entry_plan_status": "candidate_entry_planning_allowed",
        "candidate_source_created": "no",
    },
]


REQUIRED_CANDIDATE_METADATA_FIELDS = [
    "candidate_entry_id",
    "source_title",
    "author_information",
    "venue_or_repository",
    "publication_year_or_access_date",
    "stable_access_route",
    "source_type",
    "primary_or_secondary_status",
    "linked_raw_result_observation_id",
    "linked_screening_decision",
    "claim_category_mapping",
    "inclusion_rationale",
    "exclusion_risk_notes",
    "proposed_source_role",
    "candidate_entry_status",
    "audit_required_before_retention",
]


CANDIDATE_STATUS_VALUES = [
    "planned_not_created",
    "metadata_required",
    "candidate_entry_allowed_later",
    "deferred_until_metadata_check",
    "blocked_until_source_audit",
]


PROPOSED_SOURCE_ROLE_VALUES = [
    "background_context",
    "formal_framing",
    "contrast_source",
    "boundary_clarification",
    "future_validation_context",
    "do_not_use_for_external_validation_claims",
]


ENTRY_CREATION_GATES = [
    "Candidate entry creation must be separate from screening execution.",
    "Candidate entry creation must use stable metadata.",
    "Candidate entry creation must link back to raw observation id.",
    "Candidate entry creation must link back to screening decision.",
    "Candidate entry creation must map to a claim category.",
    "Candidate entry creation must include inclusion rationale.",
    "Candidate entry creation must include exclusion-risk notes.",
    "Candidate entry creation must assign proposed source role.",
    "Candidate entry creation must not retain sources.",
    "Candidate entry creation must not add citations.",
    "Candidate entry creation must not populate the evidence matrix.",
    "Candidate entry creation must not revise the manuscript.",
]


METADATA_AUDIT_REQUIREMENTS = [
    "Check whether source title is stable.",
    "Check whether author information is available.",
    "Check whether venue or repository is identifiable.",
    "Check whether year or access date can be recorded without invention.",
    "Check whether access route is stable enough for later review.",
    "Check whether the source type can be classified.",
    "Check whether primary or secondary status can be determined.",
    "Check whether claim-category mapping is justified.",
    "Check whether inclusion rationale is explicit.",
    "Check whether exclusion-risk notes are explicit.",
    "Check whether proposed source role is bounded.",
    "Check whether source should remain outside retention until audited.",
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
    "candidate source entry plan is not candidate source creation",
    "candidate source planning is not source retention",
    "candidate sources are not retained sources",
    "retained sources are not citations",
    "citations are not external validation",
    "does not create candidate sources",
    "does not retain sources",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
]


PROHIBITED_BEHAVIORS = [
    "Do not create candidate sources in this milestone.",
    "Do not retain sources in this milestone.",
    "Do not add citations in this milestone.",
    "Do not populate the evidence matrix in this milestone.",
    "Do not revise the manuscript in this milestone.",
    "Do not treat screening decisions as source entries.",
    "Do not treat candidate-entry planning as retention.",
    "Do not treat planned metadata fields as real metadata.",
    "Do not imply external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
]


NEXT_STEPS = [
    "Create first candidate source entries in a later milestone.",
    "Populate candidate metadata only from real source records.",
    "Keep candidate entries separate from retained sources.",
    "Audit candidate metadata before retention.",
    "Retain sources only after candidate audit.",
    "Populate the evidence matrix only after retained-source audit.",
    "Add citations only after retained-source decision.",
    "Revise manuscript only after citation-grounded integration.",
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
    r"\bsubmission-ready\b",
]


SAFE_LINE_CUES = [
    "not",
    "does not",
    "do not",
    "must not",
    "candidate source",
    "candidate-entry",
    "planning",
    "retained source",
    "zero",
    "metadata",
    "later",
    "boundary",
    "prohibited",
    "internal validation",
    "not externally",
    "not submission",
    "not a final",
    "not biological",
    "not clinical",
    "not laboratory",
    "not operational",
    "citations are not external validation",
]


SAFE_SECTION_HEADINGS = [
    "boundary phrases",
    "prohibited behaviors",
    "entry creation gates",
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
class FirstCandidateSourceEntryPlanResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    candidate_entry_plan_count: int
    planned_candidate_entry_row_count: int
    pass_to_candidate_planning_count: int
    defer_to_candidate_planning_count: int
    candidate_source_count: int
    retained_source_count: int
    source_added_count: int
    citation_added_count: int
    evidence_matrix_populated_count: int
    manuscript_revised_count: int
    required_metadata_field_count: int
    candidate_status_value_count: int
    proposed_source_role_count: int
    entry_creation_gate_count: int
    metadata_audit_requirement_count: int
    boundary_phrase_count: int
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


def render_source_table() -> str:
    rows = [
        "| Source artifact | Exists |",
        "|---|---|",
    ]
    for path in SOURCE_ARTIFACTS:
        rows.append(f"| `{relative(path)}` | {path.exists()} |")
    return "\n".join(rows)


def render_metadata_table() -> str:
    rows = [
        "| Plan field | Value |",
        "|---|---|",
    ]
    for key, value in PLAN_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_planned_candidate_rows() -> str:
    rows = [
        "| Raw observation id | Screening decision | Entry plan status | Candidate source created |",
        "|---|---|---|---|",
    ]
    for item in PLANNED_CANDIDATE_ENTRY_ROWS:
        rows.append(
            f"| {item['raw_result_observation_id']} | "
            f"{item['screening_decision']} | "
            f"{item['entry_plan_status']} | "
            f"{item['candidate_source_created']} |"
        )
    return "\n".join(rows)


def render_field_table(fields: list[str]) -> str:
    rows = [
        "| Candidate metadata field | v6.0 status |",
        "|---|---|",
    ]
    for field in fields:
        rows.append(f"| `{field}` | required later, not populated here |")
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

        if "fake citation" in lowered or "not citations" in lowered:
            continue

        for pattern in FAKE_CITATION_PATTERNS:
            if re.search(pattern, stripped):
                findings.append(stripped)
                break

    return findings


def render_report() -> str:
    return f"""# First Candidate Source Entry Plan v6.0

## Question
Can Viruse Fabric plan the first candidate source entry workflow after screening execution without creating candidate sources, retaining sources, adding citations, populating the evidence matrix, or revising the manuscript?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This is a candidate source entry plan. Candidate source entry plan is not candidate source creation. Candidate source planning is not source retention. Candidate sources are not retained sources. Retained sources are not citations. Citations are not external validation.

This artifact does not create candidate sources, does not retain sources, does not add citations, does not populate the evidence matrix, and does not revise the manuscript.

## Source Artifacts
{render_source_table()}

## Candidate Entry Plan Metadata
{render_metadata_table()}

## Planned Candidate Entry Rows
{render_planned_candidate_rows()}

## Required Candidate Metadata Fields
{render_field_table(REQUIRED_CANDIDATE_METADATA_FIELDS)}

## Candidate Status Values
{bullet_list(CANDIDATE_STATUS_VALUES)}

## Proposed Source Role Values
{bullet_list(PROPOSED_SOURCE_ROLE_VALUES)}

## Entry Creation Gates
{bullet_list(ENTRY_CREATION_GATES)}

## Metadata Audit Requirements
{bullet_list(METADATA_AUDIT_REQUIREMENTS)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Candidate Entry Interpretation
The v6.0 artifact plans the first candidate source entry workflow after the v5.9 screening execution.

The v5.9 screening execution produced three pass-to-candidate-planning decisions and two defer-to-candidate-planning decisions. That is not the same as creating candidate sources. The current artifact only defines what must be collected before candidate entries can exist.

This distinction matters because a screened raw observation still has no stable source record inside the project. It may have a title. It may look relevant. It may deserve metadata work. But it is not yet a candidate source. A project that treats screened titles as sources is not doing literature grounding; it is arranging words into a confidence costume.

## Metadata Boundary
Candidate entry creation requires real metadata.

A future candidate entry must identify a stable title, authorship information, venue or repository, year or access date when appropriate, access route, source type, primary or secondary status, linked raw observation id, linked screening decision, claim-category mapping, inclusion rationale, exclusion-risk notes, proposed source role, candidate status, and audit requirement.

None of those fields are populated in this milestone. They are only defined as required fields. This prevents a plan from masquerading as a database. Plans love doing that when nobody is watching. Very bureaucratic of them.

## Retention Boundary
Candidate source planning is not retention.

A candidate source, once created later, will still require audit before retention. Retention will require a separate decision. Only retained and audited sources may later enter the evidence matrix. Only after evidence matrix population should citation-grounded manuscript revision be considered.

The workflow therefore remains deliberately staged: screening decision, candidate entry plan, candidate entry creation, candidate metadata audit, retention decision, evidence matrix transfer, citation integration, manuscript revision. It is slow because each boundary prevents a different kind of nonsense.

## Output Counts
Candidate entry plan count: 1

Planned candidate entry row count: 5

Pass to candidate planning count: 3

Defer to candidate planning count: 2

Candidate source count: 0

Retained source count: 0

Source added count: 0

Citation added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact plans first candidate source entry.

It does not create candidate sources, does not retain sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstCandidateSourceEntryPlanResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    candidate_entry_plan_count = 1
    planned_candidate_entry_row_count = len(PLANNED_CANDIDATE_ENTRY_ROWS)
    pass_count = sum(
        1 for item in PLANNED_CANDIDATE_ENTRY_ROWS
        if item["screening_decision"] == "pass_to_candidate_entry_planning"
    )
    defer_count = sum(
        1 for item in PLANNED_CANDIDATE_ENTRY_ROWS
        if item["screening_decision"] == "defer_for_candidate_entry_planning"
    )
    candidate_source_count = int(PLAN_METADATA["candidate_source_count"])
    retained_source_count = int(PLAN_METADATA["retained_source_count"])
    source_added_count = 0
    citation_added_count = 0
    evidence_matrix_populated_count = 0
    manuscript_revised_count = 0

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 10:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if candidate_entry_plan_count != 1:
        errors.append(f"Candidate entry plan count should be one, got: {candidate_entry_plan_count}")

    if planned_candidate_entry_row_count != 5:
        errors.append(
            f"Planned candidate entry row count should be five, got: {planned_candidate_entry_row_count}"
        )

    if pass_count != 3:
        errors.append(f"Pass to candidate planning count should be three, got: {pass_count}")

    if defer_count != 2:
        errors.append(f"Defer to candidate planning count should be two, got: {defer_count}")

    if len(REQUIRED_CANDIDATE_METADATA_FIELDS) < 16:
        errors.append(
            f"Required metadata field count too low: {len(REQUIRED_CANDIDATE_METADATA_FIELDS)}"
        )

    if len(CANDIDATE_STATUS_VALUES) < 5:
        errors.append(f"Candidate status value count too low: {len(CANDIDATE_STATUS_VALUES)}")

    if len(PROPOSED_SOURCE_ROLE_VALUES) < 6:
        errors.append(f"Proposed source role count too low: {len(PROPOSED_SOURCE_ROLE_VALUES)}")

    if len(ENTRY_CREATION_GATES) < 12:
        errors.append(f"Entry creation gate count too low: {len(ENTRY_CREATION_GATES)}")

    if len(METADATA_AUDIT_REQUIREMENTS) < 12:
        errors.append(
            f"Metadata audit requirement count too low: {len(METADATA_AUDIT_REQUIREMENTS)}"
        )

    for label, value in [
        ("Candidate source count", candidate_source_count),
        ("Retained source count", retained_source_count),
        ("Source added count", source_added_count),
        ("Citation added count", citation_added_count),
        ("Evidence matrix populated count", evidence_matrix_populated_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if boundary_count < 17:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 11:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if word_count < 1200:
        errors.append(f"Word count too low for first candidate source entry plan: {word_count}")

    warnings.append("Candidate source entry plan creates no candidate sources.")
    warnings.append("Candidate source entry plan does not add citations, evidence rows, or manuscript revisions.")

    passed = not errors

    interpretation = (
        "The v6.0 artifact plans the first candidate source entry workflow after "
        "screening execution while keeping candidate sources, retained sources, "
        "citations, evidence matrix population, and manuscript revision at zero."
    )

    return FirstCandidateSourceEntryPlanResult(
        title="First Candidate Source Entry Plan v6.0",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        candidate_entry_plan_count=candidate_entry_plan_count,
        planned_candidate_entry_row_count=planned_candidate_entry_row_count,
        pass_to_candidate_planning_count=pass_count,
        defer_to_candidate_planning_count=defer_count,
        candidate_source_count=candidate_source_count,
        retained_source_count=retained_source_count,
        source_added_count=source_added_count,
        citation_added_count=citation_added_count,
        evidence_matrix_populated_count=evidence_matrix_populated_count,
        manuscript_revised_count=manuscript_revised_count,
        required_metadata_field_count=len(REQUIRED_CANDIDATE_METADATA_FIELDS),
        candidate_status_value_count=len(CANDIDATE_STATUS_VALUES),
        proposed_source_role_count=len(PROPOSED_SOURCE_ROLE_VALUES),
        entry_creation_gate_count=len(ENTRY_CREATION_GATES),
        metadata_audit_requirement_count=len(METADATA_AUDIT_REQUIREMENTS),
        boundary_phrase_count=boundary_count,
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

    print("First Candidate Source Entry Plan v6.0")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Candidate entry plan count: {result.candidate_entry_plan_count}")
    print(f"Planned candidate entry row count: {result.planned_candidate_entry_row_count}")
    print(f"Pass to candidate planning count: {result.pass_to_candidate_planning_count}")
    print(f"Defer to candidate planning count: {result.defer_to_candidate_planning_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Required metadata field count: {result.required_metadata_field_count}")
    print(f"Candidate status value count: {result.candidate_status_value_count}")
    print(f"Proposed source role count: {result.proposed_source_role_count}")
    print(f"Entry creation gate count: {result.entry_creation_gate_count}")
    print(f"Metadata audit requirement count: {result.metadata_audit_requirement_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
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
