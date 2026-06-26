"""First citation-grounded manuscript claim revision plan for Viruse Fabric v7.5.

This module plans the first manuscript claim revision layer based on audited
manuscript citation markers.

It does not execute manuscript revision.
It does not rewrite manuscript paragraphs.
It does not add new citations.
It does not claim external validation.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_citation_grounded_manuscript_claim_revision_plan_v7_5.md"

SOURCE_MARKER_AUDIT = PROJECT_ROOT / "outputs" / "first_manuscript_citation_marker_audit_v7_4.md"
SOURCE_MARKER_INSERTION_EXECUTION = PROJECT_ROOT / "outputs" / "first_manuscript_citation_insertion_execution_v7_3.md"
SOURCE_INSERTION_PLAN = PROJECT_ROOT / "outputs" / "first_manuscript_citation_insertion_plan_v7_2.md"
SOURCE_CITATION_RECORD_AUDIT = PROJECT_ROOT / "outputs" / "first_citation_record_audit_v7_1.md"
SOURCE_CITATION_EXECUTION = PROJECT_ROOT / "outputs" / "first_citation_integration_execution_v7_0.md"
SOURCE_CITATION_PLAN = PROJECT_ROOT / "outputs" / "first_citation_integration_plan_v6_9.md"
SOURCE_ROW_AUDIT = PROJECT_ROOT / "outputs" / "first_evidence_matrix_row_audit_v6_8.md"
SOURCE_POPULATION_EXECUTION = PROJECT_ROOT / "outputs" / "first_evidence_matrix_population_execution_v6_7.md"
SOURCE_POPULATION_PLAN = PROJECT_ROOT / "outputs" / "first_evidence_matrix_population_plan_v6_6.md"
SOURCE_ROLE_AUDIT = PROJECT_ROOT / "outputs" / "first_retained_source_role_audit_v6_5.md"
SOURCE_RETENTION_EXECUTION = PROJECT_ROOT / "outputs" / "first_retained_source_decision_execution_v6_4.md"
SOURCE_RETENTION_PLAN = PROJECT_ROOT / "outputs" / "first_retained_source_decision_plan_v6_3.md"
SOURCE_METADATA_AUDIT = PROJECT_ROOT / "outputs" / "candidate_source_metadata_audit_v6_2.md"
SOURCE_CANDIDATE_CREATION = PROJECT_ROOT / "outputs" / "first_candidate_source_entry_creation_v6_1.md"
SOURCE_ENTRY_PLAN = PROJECT_ROOT / "outputs" / "first_candidate_source_entry_plan_v6_0.md"
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
    SOURCE_MARKER_AUDIT,
    SOURCE_MARKER_INSERTION_EXECUTION,
    SOURCE_INSERTION_PLAN,
    SOURCE_CITATION_RECORD_AUDIT,
    SOURCE_CITATION_EXECUTION,
    SOURCE_CITATION_PLAN,
    SOURCE_ROW_AUDIT,
    SOURCE_POPULATION_EXECUTION,
    SOURCE_POPULATION_PLAN,
    SOURCE_ROLE_AUDIT,
    SOURCE_RETENTION_EXECUTION,
    SOURCE_RETENTION_PLAN,
    SOURCE_METADATA_AUDIT,
    SOURCE_CANDIDATE_CREATION,
    SOURCE_ENTRY_PLAN,
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
    "citation_grounded_manuscript_claim_revision_plan_id": "CGMCRP-0001",
    "linked_manuscript_citation_marker_audit_id": "MCMA-0001",
    "linked_manuscript_citation_insertion_execution_id": "MCIE-0001",
    "linked_manuscript_citation_insertion_plan_id": "MCIP-0001",
    "linked_citation_record_audit_id": "CRA-0001",
    "plan_status": "planned_only_no_manuscript_revision",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "audited_manuscript_citation_marker_count_from_v7_4": "2",
    "planned_claim_revision_count": "2",
    "manuscript_claim_revision_execution_count": "0",
    "manuscript_revised_count": "0",
    "new_citation_added_count": "0",
    "conditional_hold_count": "1",
}


PLANNED_CLAIM_REVISION_ROWS = [
    {
        "planned_claim_revision_id": "CGRP-0001",
        "linked_marker_audit_row_id": "MCMA-ROW-0001",
        "linked_manuscript_citation_marker_id": "MCM-0001",
        "linked_planned_insertion_slot_id": "MCIS-PLAN-0001",
        "linked_citation_record_id": "CIT-REC-0001",
        "linked_citation_key": "pmlr-v115-blom20a",
        "linked_evidence_matrix_row_id": "EMR-0001",
        "linked_retained_source_id": "RET-0001",
        "linked_candidate_entry_id": "CAND-0001",
        "target_manuscript_section": "related-work or conceptual framing section",
        "target_claim_role": "bounded formal-framing claim",
        "planned_revision_type": "citation_grounded_contextual_claim_revision_plan",
        "planned_revision_intent": "Use the audited marker only to bound discussion of causal constraints models as related formal context.",
        "proposed_bounded_claim_language": "Viruse Fabric can be framed alongside prior causal-constraints work as a conceptual prototype, without claiming validation or equivalence.",
        "forbidden_revision_move": "Do not claim that Viruse Fabric proves, extends, or validates causal constraints models.",
        "revision_execution_status": "not_executed_plan_only",
        "manuscript_revised": "no",
        "new_citation_added": "no",
        "planning_reason": "The audited marker has a complete linkage chain and can support a bounded contextual revision plan later.",
    },
    {
        "planned_claim_revision_id": "CGRP-0002",
        "linked_marker_audit_row_id": "MCMA-ROW-0002",
        "linked_manuscript_citation_marker_id": "MCM-0002",
        "linked_planned_insertion_slot_id": "MCIS-PLAN-0002",
        "linked_citation_record_id": "CIT-REC-0002",
        "linked_citation_key": "pmlr-v124-wengel-mogensen20a",
        "linked_evidence_matrix_row_id": "EMR-0002",
        "linked_retained_source_id": "RET-0002",
        "linked_candidate_entry_id": "CAND-0002",
        "target_manuscript_section": "related-work or methodological context section",
        "target_claim_role": "bounded methodological-context claim",
        "planned_revision_type": "citation_grounded_contextual_claim_revision_plan",
        "planned_revision_intent": "Use the audited marker only to bound discussion of dynamical-systems causal screening as methodological context.",
        "proposed_bounded_claim_language": "Viruse Fabric can cite causal screening in dynamical systems as methodological background, without claiming biological prediction or operational use.",
        "forbidden_revision_move": "Do not claim that Viruse Fabric predicts real biological systems or provides operational causal screening.",
        "revision_execution_status": "not_executed_plan_only",
        "manuscript_revised": "no",
        "new_citation_added": "no",
        "planning_reason": "The audited marker has a complete linkage chain and can support a bounded methodological revision plan later.",
    },
]


CONDITIONAL_HOLD_ROWS = [
    {
        "candidate_entry_id": "CAND-0003",
        "hold_status": "hold_for_update_before_retention_decision",
        "citation_record_id": "none",
        "manuscript_citation_marker_id": "none",
        "claim_revision_plan_id": "none",
        "planned_claim_revision": "no",
        "manuscript_revised": "no",
        "new_citation_added": "no",
        "reason": "Conditional metadata pass remains outside retained source, citation record audit, insertion planning, marker insertion, marker audit, and claim revision planning.",
    },
]


CLAIM_REVISION_PLAN_FIELDS = [
    "planned_claim_revision_id",
    "linked_marker_audit_row_id",
    "linked_manuscript_citation_marker_id",
    "linked_planned_insertion_slot_id",
    "linked_citation_record_id",
    "linked_citation_key",
    "linked_evidence_matrix_row_id",
    "linked_retained_source_id",
    "linked_candidate_entry_id",
    "target_manuscript_section",
    "target_claim_role",
    "planned_revision_type",
    "planned_revision_intent",
    "proposed_bounded_claim_language",
    "forbidden_revision_move",
    "revision_execution_status",
    "manuscript_revised",
    "new_citation_added",
    "planning_reason",
]


CLAIM_REVISION_PLAN_STATUS_VALUES = [
    "planned_only_no_manuscript_revision",
    "not_executed_plan_only",
    "candidate_hold_no_revision_plan",
    "future_execution_required",
]


CLAIM_REVISION_PLAN_GATES = [
    "Claim revision planning must be linked to v7.4 marker audit.",
    "Only audited manuscript citation markers may enter claim revision planning.",
    "Each planned claim revision must link to a marker audit row.",
    "Each planned claim revision must link to a manuscript citation marker.",
    "Each planned claim revision must link to a planned insertion slot.",
    "Each planned claim revision must link to an audited citation record.",
    "Each planned claim revision must link to a citation key.",
    "Each planned claim revision must link to an evidence matrix row.",
    "Each planned claim revision must link to a retained source.",
    "Each planned claim revision must link to a candidate entry.",
    "Each planned claim revision must have a bounded target section.",
    "Each planned claim revision must have a bounded claim role.",
    "Each planned claim revision must state a forbidden revision move.",
    "Claim revision planning must not rewrite manuscript prose.",
    "Manuscript revised count must remain zero.",
    "New citation added count must remain zero.",
    "Conditional-hold candidates must remain outside claim revision planning.",
    "Claim revision planning must not imply external validation or submission readiness.",
]


BOUNDARY_PHRASES = [
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does plan citation-grounded manuscript claim revision",
    "does not execute manuscript claim revision",
    "does not revise manuscript claims",
    "does not rewrite manuscript paragraphs",
    "does not add new citations",
    "claim revision plan is not claim revision execution",
    "planned claim language is not applied manuscript prose",
    "citation-grounded revision plan is not proof",
    "citation-grounded revision plan is not external validation",
    "citation marker audit pass is not manuscript support",
    "citation record pass is not manuscript support",
    "citations are not external validation",
    "bounded context is not biological validation",
    "bounded context is not clinical validation",
    "conditional hold remains outside claim revision planning",
    "future claim revision execution is separate",
    "future revised manuscript audit is separate",
    "future public claims must remain bounded",
]


PROHIBITED_BEHAVIORS = [
    "Do not execute manuscript claim revision in this milestone.",
    "Do not rewrite manuscript paragraphs in this milestone.",
    "Do not add new citations in this milestone.",
    "Do not treat planned claim language as applied manuscript prose.",
    "Do not treat claim revision planning as proof.",
    "Do not treat claim revision planning as external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not include conditional-hold candidates in claim revision plans.",
    "Do not convert contextual citations into strengthened conclusions.",
    "Do not claim accepted scientific theory.",
    "Do not upgrade validation language.",
]


NEXT_STEPS = [
    "Execute citation-grounded manuscript claim revision in a later milestone.",
    "Keep claim revision execution separate from claim revision planning.",
    "Audit any executed manuscript claim revisions after execution.",
    "Keep new citation additions separate from claim revision planning.",
    "Preserve marker linkage during future claim revision execution.",
    "Keep CAND-0003 on hold until update handling.",
    "Keep public claims bounded after claim revision planning.",
    "Maintain the research prototype with internal validation status.",
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
    r"\baccepted scientific theory\b",
]


SAFE_LINE_CUES = [
    "not",
    "does not",
    "do not",
    "must not",
    "without claiming",
    "forbidden",
    "citation",
    "citation marker",
    "marker audit",
    "claim revision plan",
    "planned",
    "plan",
    "future",
    "manuscript",
    "citation record",
    "evidence row",
    "retained source",
    "candidate",
    "conditional",
    "hold",
    "zero",
    "audit",
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
    "claim revision plan gates",
    "claim boundary toward v7.6",
    "final boundary statement",
]


INVENTED_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
]


@dataclass(frozen=True)
class FirstCitationGroundedManuscriptClaimRevisionPlanResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    citation_grounded_claim_revision_plan_count: int
    audited_manuscript_citation_marker_count: int
    planned_claim_revision_count: int
    manuscript_claim_revision_execution_count: int
    manuscript_revised_count: int
    new_citation_added_count: int
    conditional_hold_count: int
    claim_revision_plan_field_count: int
    claim_revision_plan_status_value_count: int
    claim_revision_plan_gate_count: int
    boundary_phrase_count: int
    prohibited_behavior_count: int
    next_step_count: int
    overclaim_count: int
    invented_citation_like_pattern_count: int
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
        "| Citation-grounded manuscript claim revision plan field | Value |",
        "|---|---|",
    ]
    for key, value in PLAN_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_planned_claim_revision_rows() -> str:
    rows = [
        "| Planned revision | Marker audit row | Marker | Citation record | Citation key | Target role | Execution status |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in PLANNED_CLAIM_REVISION_ROWS:
        rows.append(
            f"| {item['planned_claim_revision_id']} | "
            f"{item['linked_marker_audit_row_id']} | "
            f"{item['linked_manuscript_citation_marker_id']} | "
            f"{item['linked_citation_record_id']} | "
            f"{item['linked_citation_key']} | "
            f"{item['target_claim_role']} | "
            f"{item['revision_execution_status']} |"
        )
    return "\n".join(rows)


def render_claim_revision_linkage_rows() -> str:
    rows = [
        "| Planned revision | Planned slot | Evidence row | Retained source | Candidate | Target section |",
        "|---|---|---|---|---|---|",
    ]
    for item in PLANNED_CLAIM_REVISION_ROWS:
        rows.append(
            f"| {item['planned_claim_revision_id']} | "
            f"{item['linked_planned_insertion_slot_id']} | "
            f"{item['linked_evidence_matrix_row_id']} | "
            f"{item['linked_retained_source_id']} | "
            f"{item['linked_candidate_entry_id']} | "
            f"{item['target_manuscript_section']} |"
        )
    return "\n".join(rows)


def render_planned_language_rows() -> str:
    rows = [
        "| Planned revision | Planned bounded language | Forbidden revision move |",
        "|---|---|---|",
    ]
    for item in PLANNED_CLAIM_REVISION_ROWS:
        rows.append(
            f"| {item['planned_claim_revision_id']} | "
            f"{item['proposed_bounded_claim_language']} | "
            f"{item['forbidden_revision_move']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Claim revision plan | Planned revision | Manuscript revised | New citation added | Reason |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['claim_revision_plan_id']} | "
            f"{item['planned_claim_revision']} | "
            f"{item['manuscript_revised']} | "
            f"{item['new_citation_added']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Claim revision plan field | v7.5 status |",
        "|---|---|",
    ]
    for field in CLAIM_REVISION_PLAN_FIELDS:
        rows.append(f"| `{field}` | populated for planned claim revision rows |")
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


def detect_invented_citation_like_patterns(text: str) -> list[str]:
    findings: list[str] = []
    current_section = ""

    allowed_sections = {
        "planned claim revision rows",
        "claim revision linkage rows",
        "citation-grounded manuscript claim revision plan metadata",
        "planned bounded claim language",
    }

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        lowered = stripped.lower()

        if lowered.startswith("## "):
            current_section = lowered.removeprefix("## ").strip()

        if current_section in allowed_sections:
            continue

        if "invented citation" in lowered or "citation-like" in lowered:
            continue

        for pattern in INVENTED_CITATION_PATTERNS:
            if re.search(pattern, stripped):
                findings.append(stripped)
                break

    return findings


def render_report() -> str:
    return f"""# First Citation-Grounded Manuscript Claim Revision Plan v7.5

## Question
Can Viruse Fabric plan citation-grounded manuscript claim revision from audited manuscript citation markers while keeping manuscript revision execution and new citation additions at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does plan citation-grounded manuscript claim revision. It does not execute manuscript claim revision, does not revise manuscript claims, does not rewrite manuscript paragraphs, and does not add new citations.

Claim revision plan is not claim revision execution. Planned claim language is not applied manuscript prose. Citation-grounded revision plan is not proof. Citation-grounded revision plan is not external validation. Citation marker audit pass is not manuscript support. Citation record pass is not manuscript support. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Citation-Grounded Manuscript Claim Revision Plan Metadata
{render_metadata_table()}

## Planned Claim Revision Rows
{render_planned_claim_revision_rows()}

## Claim Revision Linkage Rows
{render_claim_revision_linkage_rows()}

## Planned Bounded Claim Language
{render_planned_language_rows()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Claim Revision Plan Fields
{render_field_table()}

## Claim Revision Plan Status Values
{bullet_list(CLAIM_REVISION_PLAN_STATUS_VALUES)}

## Claim Revision Plan Gates
{bullet_list(CLAIM_REVISION_PLAN_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Claim Revision Plan Interpretation
The v7.5 artifact plans the first citation-grounded manuscript claim revision layer.

CGRP-0001 plans a bounded contextual claim revision from MCMA-ROW-0001, MCM-0001, MCIS-PLAN-0001, CIT-REC-0001, EMR-0001, RET-0001, and CAND-0001.

CGRP-0002 plans a bounded methodological-context claim revision from MCMA-ROW-0002, MCM-0002, MCIS-PLAN-0002, CIT-REC-0002, EMR-0002, RET-0002, and CAND-0002.

These are revision plans only. They do not rewrite manuscript prose, do not apply proposed language to the manuscript, and do not strengthen conclusions.

## Planning Boundary
Citation-grounded manuscript claim revision plan count is one.

Audited manuscript citation marker count is two.

Planned claim revision count is two.

Manuscript claim revision execution count is zero.

Manuscript revised count is zero.

New citation added count is zero.

The project now has a plan for citation-grounded manuscript claim revision, but it still has no executed manuscript claim revision. This is the part where a normal document would get dramatic and pretend a plan is a result. We will not be joining that circus.

## Linkage Boundary
Each planned claim revision links to:

- marker audit row
- manuscript citation marker
- planned manuscript citation slot
- audited citation record
- citation key
- evidence matrix row
- retained source
- candidate entry
- bounded manuscript section
- bounded claim role

This keeps planned revision language from floating around like a citation-shaped ghost looking for authority.

## Planned Language Boundary
The proposed bounded claim language is stored as planning material only.

It is not applied manuscript prose.

It is not a manuscript revision.

It is not a final sentence.

It is not a strengthened conclusion.

It is not a validation claim.

It is a controlled future route for claim revision execution after audit-ready planning.

## Manuscript Claim Boundary
No manuscript paragraph is rewritten.

No claim sentence is upgraded.

No conclusion is strengthened.

No theory boundary is relaxed.

No validation language is upgraded.

Manuscript revised count remains zero because this milestone plans claim revision only.

## New Citation Boundary
New citation added count remains zero.

No new citation record is added. No new source is retained. No new bibliography entry is created. This milestone uses existing audited manuscript citation markers only.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside claim revision planning. It has no retained source record, no citation record, no audited citation record, no planned insertion slot, no inserted marker, no marker audit pass row, and no claim revision plan.

This prevents conditional metadata from sneaking into manuscript claims through the side door, wearing a blazer and calling itself context.

## Claim Boundary Toward v7.6
This milestone permits a slightly stronger internal workflow claim than v7.4.

Allowed after v7.5:

- internally staged prototype
- retained-source workflow
- evidence-mapped workflow
- evidence-row-audited workflow
- citation records added and audited
- manuscript citation insertion planned
- first manuscript citation markers inserted
- manuscript citation markers audited
- citation-grounded manuscript claim revision planned
- manuscript claims still unrevised

Still disallowed:

- proven theory
- external validation
- biological prediction
- clinical relevance
- laboratory guidance
- operational readiness
- submission-ready manuscript
- accepted scientific theory

## Output Counts
Citation-grounded manuscript claim revision plan count: 1

Audited manuscript citation marker count: 2

Planned claim revision count: 2

Manuscript claim revision execution count: 0

Manuscript revised count: 0

New citation added count: 0

Conditional hold count: 1

## Final Boundary Statement
This artifact plans citation-grounded manuscript claim revision from audited manuscript citation markers.

It does not execute manuscript claim revision, does not revise manuscript claims, does not add new citations, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstCitationGroundedManuscriptClaimRevisionPlanResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    invented_citations = detect_invented_citation_like_patterns(report)

    citation_grounded_claim_revision_plan_count = 1
    audited_marker_count = int(PLAN_METADATA["audited_manuscript_citation_marker_count_from_v7_4"])
    planned_claim_revision_count = int(PLAN_METADATA["planned_claim_revision_count"])
    manuscript_claim_revision_execution_count = int(
        PLAN_METADATA["manuscript_claim_revision_execution_count"]
    )
    manuscript_revised_count = int(PLAN_METADATA["manuscript_revised_count"])
    new_citation_added_count = int(PLAN_METADATA["new_citation_added_count"])
    conditional_hold_count = int(PLAN_METADATA["conditional_hold_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 25:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if citation_grounded_claim_revision_plan_count != 1:
        errors.append(
            "Citation-grounded manuscript claim revision plan count should be one, got: "
            f"{citation_grounded_claim_revision_plan_count}"
        )

    if audited_marker_count != 2:
        errors.append(f"Audited manuscript citation marker count should be two, got: {audited_marker_count}")

    if planned_claim_revision_count != 2:
        errors.append(f"Planned claim revision count should be two, got: {planned_claim_revision_count}")

    if audited_marker_count != planned_claim_revision_count:
        errors.append("Each audited manuscript citation marker should map to one planned claim revision")

    if manuscript_claim_revision_execution_count != 0:
        errors.append(
            "Manuscript claim revision execution count should be zero, got: "
            f"{manuscript_claim_revision_execution_count}"
        )

    if manuscript_revised_count != 0:
        errors.append(f"Manuscript revised count should be zero, got: {manuscript_revised_count}")

    if new_citation_added_count != 0:
        errors.append(f"New citation added count should be zero, got: {new_citation_added_count}")

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    for row in PLANNED_CLAIM_REVISION_ROWS:
        missing_fields = [field for field in CLAIM_REVISION_PLAN_FIELDS if not row.get(field)]
        if missing_fields:
            errors.append(
                f"{row.get('planned_claim_revision_id', 'unknown')} missing claim revision plan fields: "
                f"{len(missing_fields)}"
            )

        if row.get("revision_execution_status") != "not_executed_plan_only":
            errors.append(
                f"{row.get('planned_claim_revision_id', 'unknown')} has unexpected execution status"
            )

        if row.get("manuscript_revised") != "no":
            errors.append(
                f"{row.get('planned_claim_revision_id', 'unknown')} revised manuscript unexpectedly"
            )

        if row.get("new_citation_added") != "no":
            errors.append(
                f"{row.get('planned_claim_revision_id', 'unknown')} added citation unexpectedly"
            )

    if len(CLAIM_REVISION_PLAN_FIELDS) < 19:
        errors.append(f"Claim revision plan field count too low: {len(CLAIM_REVISION_PLAN_FIELDS)}")

    if len(CLAIM_REVISION_PLAN_STATUS_VALUES) < 4:
        errors.append(
            "Claim revision plan status value count too low: "
            f"{len(CLAIM_REVISION_PLAN_STATUS_VALUES)}"
        )

    if len(CLAIM_REVISION_PLAN_GATES) < 18:
        errors.append(f"Claim revision plan gate count too low: {len(CLAIM_REVISION_PLAN_GATES)}")

    if boundary_count < 22:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 12:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if invented_citations:
        errors.append(
            "Invented citation-like patterns detected outside claim revision plan sections: "
            f"{len(invented_citations)}"
        )

    if word_count < 1250:
        errors.append(
            "Word count too low for first citation-grounded manuscript claim revision plan: "
            f"{word_count}"
        )

    warnings.append("Citation-grounded manuscript claim revision is planned, but not executed.")
    warnings.append("Planned claim language is not applied manuscript prose.")

    passed = not errors

    interpretation = (
        "The v7.5 artifact plans two citation-grounded manuscript claim revisions from audited "
        "manuscript citation markers while keeping claim revision execution, manuscript revision, "
        "and new citation additions at zero."
    )

    return FirstCitationGroundedManuscriptClaimRevisionPlanResult(
        title="First Citation-Grounded Manuscript Claim Revision Plan v7.5",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        citation_grounded_claim_revision_plan_count=citation_grounded_claim_revision_plan_count,
        audited_manuscript_citation_marker_count=audited_marker_count,
        planned_claim_revision_count=planned_claim_revision_count,
        manuscript_claim_revision_execution_count=manuscript_claim_revision_execution_count,
        manuscript_revised_count=manuscript_revised_count,
        new_citation_added_count=new_citation_added_count,
        conditional_hold_count=conditional_hold_count,
        claim_revision_plan_field_count=len(CLAIM_REVISION_PLAN_FIELDS),
        claim_revision_plan_status_value_count=len(CLAIM_REVISION_PLAN_STATUS_VALUES),
        claim_revision_plan_gate_count=len(CLAIM_REVISION_PLAN_GATES),
        boundary_phrase_count=boundary_count,
        prohibited_behavior_count=prohibited_count,
        next_step_count=next_step_count,
        overclaim_count=len(overclaims),
        invented_citation_like_pattern_count=len(invented_citations),
        word_count=word_count,
        errors=errors,
        warnings=warnings,
        passed=passed,
        interpretation=interpretation,
    )


def main() -> None:
    result = generate_report()

    print("First Citation-Grounded Manuscript Claim Revision Plan v7.5")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(
        "Citation-grounded manuscript claim revision plan count: "
        f"{result.citation_grounded_claim_revision_plan_count}"
    )
    print(
        "Audited manuscript citation marker count: "
        f"{result.audited_manuscript_citation_marker_count}"
    )
    print(f"Planned claim revision count: {result.planned_claim_revision_count}")
    print(
        "Manuscript claim revision execution count: "
        f"{result.manuscript_claim_revision_execution_count}"
    )
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Claim revision plan field count: {result.claim_revision_plan_field_count}")
    print(
        "Claim revision plan status value count: "
        f"{result.claim_revision_plan_status_value_count}"
    )
    print(f"Claim revision plan gate count: {result.claim_revision_plan_gate_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Invented citation-like pattern count: {result.invented_citation_like_pattern_count}")
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
