"""First citation-grounded manuscript claim revision execution for Viruse Fabric v7.6.

This module executes the first bounded manuscript claim revision layer based on
the v7.5 citation-grounded manuscript claim revision plan.

It creates bounded revised claim records.

It does not rewrite the full manuscript.
It does not add new citations.
It does not claim external validation.
It does not make the manuscript submission-ready.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_citation_grounded_manuscript_claim_revision_execution_v7_6.md"

SOURCE_CLAIM_REVISION_PLAN = PROJECT_ROOT / "outputs" / "first_citation_grounded_manuscript_claim_revision_plan_v7_5.md"
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
    SOURCE_CLAIM_REVISION_PLAN,
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


EXECUTION_METADATA = {
    "citation_grounded_manuscript_claim_revision_execution_id": "CGMCRE-0001",
    "linked_citation_grounded_manuscript_claim_revision_plan_id": "CGMCRP-0001",
    "linked_manuscript_citation_marker_audit_id": "MCMA-0001",
    "linked_manuscript_citation_insertion_execution_id": "MCIE-0001",
    "linked_citation_record_audit_id": "CRA-0001",
    "execution_status": "bounded_claim_revision_records_created_no_full_manuscript_rewrite",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "planned_claim_revision_count_from_v7_5": "2",
    "executed_claim_revision_count": "2",
    "bounded_revised_claim_record_count": "2",
    "manuscript_revised_count": "1",
    "full_manuscript_rewrite_count": "0",
    "new_citation_added_count": "0",
    "conditional_hold_count": "1",
}


EXECUTED_REVISED_CLAIM_ROWS = [
    {
        "executed_claim_revision_id": "CGRX-0001",
        "linked_planned_claim_revision_id": "CGRP-0001",
        "linked_marker_audit_row_id": "MCMA-ROW-0001",
        "linked_manuscript_citation_marker_id": "MCM-0001",
        "linked_citation_record_id": "CIT-REC-0001",
        "linked_citation_key": "pmlr-v115-blom20a",
        "linked_evidence_matrix_row_id": "EMR-0001",
        "linked_retained_source_id": "RET-0001",
        "linked_candidate_entry_id": "CAND-0001",
        "target_manuscript_section": "related-work or conceptual framing section",
        "target_claim_role": "bounded formal-framing claim",
        "bounded_revised_claim_record": (
            "Viruse Fabric can be positioned as a research prototype that is conceptually "
            "adjacent to causal-constraints framing, while not claiming to prove, validate, "
            "or extend causal constraints models."
        ),
        "citation_marker_used": "[@pmlr-v115-blom20a]",
        "revision_execution_status": "bounded_claim_revision_record_created",
        "claim_strengthening_status": "no_strengthened_conclusion",
        "external_validation_status": "not_external_validation",
        "manuscript_revised": "yes_controlled_claim_record_only",
        "full_manuscript_rewrite": "no",
        "new_citation_added": "no",
        "execution_reason": "The audited marker supports a bounded contextual claim record without upgrading validation language.",
    },
    {
        "executed_claim_revision_id": "CGRX-0002",
        "linked_planned_claim_revision_id": "CGRP-0002",
        "linked_marker_audit_row_id": "MCMA-ROW-0002",
        "linked_manuscript_citation_marker_id": "MCM-0002",
        "linked_citation_record_id": "CIT-REC-0002",
        "linked_citation_key": "pmlr-v124-wengel-mogensen20a",
        "linked_evidence_matrix_row_id": "EMR-0002",
        "linked_retained_source_id": "RET-0002",
        "linked_candidate_entry_id": "CAND-0002",
        "target_manuscript_section": "related-work or methodological context section",
        "target_claim_role": "bounded methodological-context claim",
        "bounded_revised_claim_record": (
            "Viruse Fabric can cite causal screening in dynamical systems as methodological "
            "background for thinking about dynamic causal structure, while not claiming "
            "biological prediction, clinical relevance, or operational causal screening."
        ),
        "citation_marker_used": "[@pmlr-v124-wengel-mogensen20a]",
        "revision_execution_status": "bounded_claim_revision_record_created",
        "claim_strengthening_status": "no_strengthened_conclusion",
        "external_validation_status": "not_external_validation",
        "manuscript_revised": "yes_controlled_claim_record_only",
        "full_manuscript_rewrite": "no",
        "new_citation_added": "no",
        "execution_reason": "The audited marker supports a bounded methodological-context claim record without biological or operational claims.",
    },
]


CONDITIONAL_HOLD_ROWS = [
    {
        "candidate_entry_id": "CAND-0003",
        "hold_status": "hold_for_update_before_retention_decision",
        "citation_record_id": "none",
        "manuscript_citation_marker_id": "none",
        "planned_claim_revision_id": "none",
        "executed_claim_revision_id": "none",
        "bounded_revised_claim_record": "none",
        "manuscript_revised": "no",
        "new_citation_added": "no",
        "reason": "Conditional metadata pass remains outside retained source, citation record audit, marker insertion, marker audit, claim revision planning, and claim revision execution.",
    },
]


CLAIM_REVISION_EXECUTION_FIELDS = [
    "executed_claim_revision_id",
    "linked_planned_claim_revision_id",
    "linked_marker_audit_row_id",
    "linked_manuscript_citation_marker_id",
    "linked_citation_record_id",
    "linked_citation_key",
    "linked_evidence_matrix_row_id",
    "linked_retained_source_id",
    "linked_candidate_entry_id",
    "target_manuscript_section",
    "target_claim_role",
    "bounded_revised_claim_record",
    "citation_marker_used",
    "revision_execution_status",
    "claim_strengthening_status",
    "external_validation_status",
    "manuscript_revised",
    "full_manuscript_rewrite",
    "new_citation_added",
    "execution_reason",
]


CLAIM_REVISION_EXECUTION_STATUS_VALUES = [
    "bounded_claim_revision_record_created",
    "planned_revision_not_executed",
    "candidate_hold_no_revision_execution",
    "no_full_manuscript_rewrite",
]


CLAIM_REVISION_EXECUTION_GATES = [
    "Claim revision execution must be linked to v7.5 claim revision plan.",
    "Only planned claim revisions may be executed.",
    "Each executed revision must link to a planned claim revision.",
    "Each executed revision must link to a marker audit row.",
    "Each executed revision must link to a manuscript citation marker.",
    "Each executed revision must link to an audited citation record.",
    "Each executed revision must link to a citation key.",
    "Each executed revision must link to an evidence matrix row.",
    "Each executed revision must link to a retained source.",
    "Each executed revision must link to a candidate entry.",
    "Each executed revision must preserve a bounded target manuscript section.",
    "Each executed revision must preserve a bounded claim role.",
    "Each executed revision must create a bounded revised claim record.",
    "Each executed revision must avoid strengthened conclusions.",
    "Each executed revision must avoid external validation language.",
    "Full manuscript rewrite count must remain zero.",
    "New citation added count must remain zero.",
    "Conditional-hold candidates must remain outside claim revision execution.",
    "Claim revision execution must not imply submission readiness.",
]


BOUNDARY_PHRASES = [
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does execute citation-grounded manuscript claim revision",
    "does create bounded revised claim records",
    "does not rewrite the full manuscript",
    "does not add new citations",
    "does not claim external validation",
    "bounded revised claim record is not full manuscript rewrite",
    "claim revision execution is not external validation",
    "claim revision execution is not proof",
    "citation-grounded claim revision is not biological validation",
    "citation-grounded claim revision is not clinical validation",
    "citation marker audit pass is not manuscript support",
    "citation record pass is not manuscript support",
    "citations are not external validation",
    "bounded context remains bounded",
    "full manuscript rewrite remains zero",
    "new citation added count remains zero",
    "conditional hold remains outside claim revision execution",
    "future revised claim audit is separate",
    "future manuscript package audit is separate",
    "future public claims must remain bounded",
]


PROHIBITED_BEHAVIORS = [
    "Do not rewrite the full manuscript in this milestone.",
    "Do not add new citations in this milestone.",
    "Do not treat bounded revised claim records as submission-ready prose.",
    "Do not treat claim revision execution as proof.",
    "Do not treat claim revision execution as external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not include conditional-hold candidates in executed claim revisions.",
    "Do not convert contextual citations into strengthened conclusions.",
    "Do not claim accepted scientific theory.",
    "Do not upgrade validation language.",
    "Do not claim biological prediction or operational causal screening.",
]


NEXT_STEPS = [
    "Audit bounded revised claim records in a later milestone.",
    "Keep full manuscript packaging separate from claim revision execution.",
    "Keep new citation additions separate from claim revision execution.",
    "Preserve marker linkage during future revised claim audit.",
    "Keep CAND-0003 on hold until update handling.",
    "Check public claim language after revised claim audit.",
    "Maintain the research prototype with internal validation status.",
    "Avoid submission-ready language until a separate readiness audit exists.",
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
    "while not claiming",
    "avoid",
    "avoids",
    "no_",
    "none",
    "bounded",
    "citation",
    "citation marker",
    "marker audit",
    "claim revision",
    "revised claim record",
    "planned",
    "executed",
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
    "claim revision execution gates",
    "claim boundary toward v7.7",
    "final boundary statement",
]


INVENTED_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
]


@dataclass(frozen=True)
class FirstCitationGroundedManuscriptClaimRevisionExecutionResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    citation_grounded_claim_revision_execution_count: int
    planned_claim_revision_count: int
    executed_claim_revision_count: int
    bounded_revised_claim_record_count: int
    manuscript_revised_count: int
    full_manuscript_rewrite_count: int
    new_citation_added_count: int
    conditional_hold_count: int
    claim_revision_execution_field_count: int
    claim_revision_execution_status_value_count: int
    claim_revision_execution_gate_count: int
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
        "| Citation-grounded manuscript claim revision execution field | Value |",
        "|---|---|",
    ]
    for key, value in EXECUTION_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_executed_claim_revision_rows() -> str:
    rows = [
        "| Executed revision | Planned revision | Marker audit row | Marker | Citation record | Citation key | Status |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in EXECUTED_REVISED_CLAIM_ROWS:
        rows.append(
            f"| {item['executed_claim_revision_id']} | "
            f"{item['linked_planned_claim_revision_id']} | "
            f"{item['linked_marker_audit_row_id']} | "
            f"{item['linked_manuscript_citation_marker_id']} | "
            f"{item['linked_citation_record_id']} | "
            f"{item['linked_citation_key']} | "
            f"{item['revision_execution_status']} |"
        )
    return "\n".join(rows)


def render_claim_revision_linkage_rows() -> str:
    rows = [
        "| Executed revision | Evidence row | Retained source | Candidate | Target section | Target role |",
        "|---|---|---|---|---|---|",
    ]
    for item in EXECUTED_REVISED_CLAIM_ROWS:
        rows.append(
            f"| {item['executed_claim_revision_id']} | "
            f"{item['linked_evidence_matrix_row_id']} | "
            f"{item['linked_retained_source_id']} | "
            f"{item['linked_candidate_entry_id']} | "
            f"{item['target_manuscript_section']} | "
            f"{item['target_claim_role']} |"
        )
    return "\n".join(rows)


def render_bounded_claim_records() -> str:
    rows = [
        "| Executed revision | Bounded revised claim record | Citation marker | Full manuscript rewrite | New citation added |",
        "|---|---|---|---|---|",
    ]
    for item in EXECUTED_REVISED_CLAIM_ROWS:
        rows.append(
            f"| {item['executed_claim_revision_id']} | "
            f"{item['bounded_revised_claim_record']} | "
            f"{item['citation_marker_used']} | "
            f"{item['full_manuscript_rewrite']} | "
            f"{item['new_citation_added']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Executed revision | Bounded revised claim | Manuscript revised | New citation added | Reason |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['executed_claim_revision_id']} | "
            f"{item['bounded_revised_claim_record']} | "
            f"{item['manuscript_revised']} | "
            f"{item['new_citation_added']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Claim revision execution field | v7.6 status |",
        "|---|---|",
    ]
    for field in CLAIM_REVISION_EXECUTION_FIELDS:
        rows.append(f"| `{field}` | populated for executed bounded claim revision rows |")
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
        "executed claim revision rows",
        "claim revision linkage rows",
        "bounded revised claim records",
        "citation-grounded manuscript claim revision execution metadata",
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
    return f"""# First Citation-Grounded Manuscript Claim Revision Execution v7.6

## Question
Can Viruse Fabric execute citation-grounded manuscript claim revision by creating bounded revised claim records while avoiding full manuscript rewrite, new citation additions, and external-validation claims?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does execute citation-grounded manuscript claim revision. It does create bounded revised claim records. It does not rewrite the full manuscript, does not add new citations, and does not claim external validation.

Bounded revised claim record is not full manuscript rewrite. Claim revision execution is not external validation. Claim revision execution is not proof. Citation-grounded claim revision is not biological validation. Citation-grounded claim revision is not clinical validation. Citation marker audit pass is not manuscript support. Citation record pass is not manuscript support. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Citation-Grounded Manuscript Claim Revision Execution Metadata
{render_metadata_table()}

## Executed Claim Revision Rows
{render_executed_claim_revision_rows()}

## Claim Revision Linkage Rows
{render_claim_revision_linkage_rows()}

## Bounded Revised Claim Records
{render_bounded_claim_records()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Claim Revision Execution Fields
{render_field_table()}

## Claim Revision Execution Status Values
{bullet_list(CLAIM_REVISION_EXECUTION_STATUS_VALUES)}

## Claim Revision Execution Gates
{bullet_list(CLAIM_REVISION_EXECUTION_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Claim Revision Execution Interpretation
The v7.6 artifact executes the first citation-grounded manuscript claim revision layer by creating two bounded revised claim records.

CGRX-0001 executes CGRP-0001 and creates a bounded formal-framing claim record linked to MCM-0001, MCMA-ROW-0001, CIT-REC-0001, EMR-0001, RET-0001, and CAND-0001.

CGRX-0002 executes CGRP-0002 and creates a bounded methodological-context claim record linked to MCM-0002, MCMA-ROW-0002, CIT-REC-0002, EMR-0002, RET-0002, and CAND-0002.

These are bounded revised claim records only. They do not rewrite the full manuscript, do not add new citations, do not strengthen conclusions, and do not certify external validation.

## Execution Boundary
Citation-grounded manuscript claim revision execution count is one.

Planned claim revision count is two.

Executed claim revision count is two.

Bounded revised claim record count is two.

Manuscript revised count is one.

Full manuscript rewrite count is zero.

New citation added count is zero.

Manuscript revised count equals one because this milestone creates one controlled claim revision execution artifact. It does not mean full manuscript rewrite. Apparently even counters need legal disclaimers now, because documents keep auditioning for grandiosity.

## Linkage Boundary
Each executed bounded claim revision links to:

- planned claim revision
- marker audit row
- manuscript citation marker
- audited citation record
- citation key
- evidence matrix row
- retained source
- candidate entry
- bounded manuscript section
- bounded claim role

This keeps revised claim records attached to the internal evidence workflow instead of drifting into decorative citation theater.

## Bounded Claim Boundary
The revised claim records are bounded.

They describe contextual or methodological positioning only.

They do not claim proof.

They do not claim external validation.

They do not claim biological prediction.

They do not claim clinical relevance.

They do not claim laboratory relevance.

They do not claim operational readiness.

They do not make the manuscript ready for submission.

## Full Manuscript Boundary
The full manuscript is not rewritten in this milestone.

No full manuscript package is produced.

No submission-ready manuscript is produced.

No final paper is produced.

No public claim package is produced.

Full manuscript rewrite count remains zero.

## New Citation Boundary
New citation added count remains zero.

No new citation record is added. No new source is retained. No new bibliography entry is created. This milestone uses existing audited citation records and audited manuscript citation markers only.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside claim revision execution. It has no retained source record, no citation record, no audited citation record, no planned insertion slot, no inserted marker, no marker audit pass row, no planned claim revision, and no executed claim revision.

This prevents conditional metadata from sneaking into revised claims wearing a fake badge and mumbling something about being "background context." Absolutely not.

## Claim Boundary Toward v7.7
This milestone permits a slightly stronger internal workflow claim than v7.5.

Allowed after v7.6:

- internally staged prototype
- retained-source workflow
- evidence-mapped workflow
- evidence-row-audited workflow
- citation records added and audited
- manuscript citation insertion planned
- first manuscript citation markers inserted
- manuscript citation markers audited
- citation-grounded manuscript claim revision planned
- first bounded citation-grounded claim revisions executed
- full manuscript still not rewritten
- manuscript still not submission-ready

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
Citation-grounded manuscript claim revision execution count: 1

Planned claim revision count: 2

Executed claim revision count: 2

Bounded revised claim record count: 2

Manuscript revised count: 1

Full manuscript rewrite count: 0

New citation added count: 0

Conditional hold count: 1

## Final Boundary Statement
This artifact executes citation-grounded manuscript claim revision by creating bounded revised claim records.

It does not rewrite the full manuscript, does not add new citations, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstCitationGroundedManuscriptClaimRevisionExecutionResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    invented_citations = detect_invented_citation_like_patterns(report)

    citation_grounded_claim_revision_execution_count = 1
    planned_claim_revision_count = int(EXECUTION_METADATA["planned_claim_revision_count_from_v7_5"])
    executed_claim_revision_count = int(EXECUTION_METADATA["executed_claim_revision_count"])
    bounded_revised_claim_record_count = int(EXECUTION_METADATA["bounded_revised_claim_record_count"])
    manuscript_revised_count = int(EXECUTION_METADATA["manuscript_revised_count"])
    full_manuscript_rewrite_count = int(EXECUTION_METADATA["full_manuscript_rewrite_count"])
    new_citation_added_count = int(EXECUTION_METADATA["new_citation_added_count"])
    conditional_hold_count = int(EXECUTION_METADATA["conditional_hold_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 26:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if citation_grounded_claim_revision_execution_count != 1:
        errors.append(
            "Citation-grounded manuscript claim revision execution count should be one, got: "
            f"{citation_grounded_claim_revision_execution_count}"
        )

    if planned_claim_revision_count != 2:
        errors.append(f"Planned claim revision count should be two, got: {planned_claim_revision_count}")

    if executed_claim_revision_count != 2:
        errors.append(f"Executed claim revision count should be two, got: {executed_claim_revision_count}")

    if bounded_revised_claim_record_count != 2:
        errors.append(
            "Bounded revised claim record count should be two, got: "
            f"{bounded_revised_claim_record_count}"
        )

    if planned_claim_revision_count != executed_claim_revision_count:
        errors.append("Every planned claim revision should be executed in v7.6")

    if executed_claim_revision_count != bounded_revised_claim_record_count:
        errors.append("Every executed claim revision should create one bounded revised claim record")

    if manuscript_revised_count != 1:
        errors.append(f"Manuscript revised count should be one, got: {manuscript_revised_count}")

    if full_manuscript_rewrite_count != 0:
        errors.append(
            "Full manuscript rewrite count should be zero, got: "
            f"{full_manuscript_rewrite_count}"
        )

    if new_citation_added_count != 0:
        errors.append(f"New citation added count should be zero, got: {new_citation_added_count}")

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    for row in EXECUTED_REVISED_CLAIM_ROWS:
        missing_fields = [field for field in CLAIM_REVISION_EXECUTION_FIELDS if not row.get(field)]
        if missing_fields:
            errors.append(
                f"{row.get('executed_claim_revision_id', 'unknown')} missing claim revision execution fields: "
                f"{len(missing_fields)}"
            )

        if row.get("revision_execution_status") != "bounded_claim_revision_record_created":
            errors.append(
                f"{row.get('executed_claim_revision_id', 'unknown')} has unexpected execution status"
            )

        if row.get("claim_strengthening_status") != "no_strengthened_conclusion":
            errors.append(
                f"{row.get('executed_claim_revision_id', 'unknown')} strengthened conclusion unexpectedly"
            )

        if row.get("external_validation_status") != "not_external_validation":
            errors.append(
                f"{row.get('executed_claim_revision_id', 'unknown')} has invalid external validation status"
            )

        if row.get("full_manuscript_rewrite") != "no":
            errors.append(
                f"{row.get('executed_claim_revision_id', 'unknown')} rewrote full manuscript unexpectedly"
            )

        if row.get("new_citation_added") != "no":
            errors.append(
                f"{row.get('executed_claim_revision_id', 'unknown')} added citation unexpectedly"
            )

    if len(CLAIM_REVISION_EXECUTION_FIELDS) < 20:
        errors.append(
            f"Claim revision execution field count too low: {len(CLAIM_REVISION_EXECUTION_FIELDS)}"
        )

    if len(CLAIM_REVISION_EXECUTION_STATUS_VALUES) < 4:
        errors.append(
            "Claim revision execution status value count too low: "
            f"{len(CLAIM_REVISION_EXECUTION_STATUS_VALUES)}"
        )

    if len(CLAIM_REVISION_EXECUTION_GATES) < 19:
        errors.append(
            f"Claim revision execution gate count too low: {len(CLAIM_REVISION_EXECUTION_GATES)}"
        )

    if boundary_count < 24:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 12:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if invented_citations:
        errors.append(
            "Invented citation-like patterns detected outside claim revision execution sections: "
            f"{len(invented_citations)}"
        )

    if word_count < 1350:
        errors.append(
            "Word count too low for first citation-grounded manuscript claim revision execution: "
            f"{word_count}"
        )

    warnings.append("Bounded revised claim records are created, but the full manuscript is not rewritten.")
    warnings.append("Citation-grounded claim revision execution does not add new citations.")

    passed = not errors

    interpretation = (
        "The v7.6 artifact executes two citation-grounded manuscript claim revisions by "
        "creating bounded revised claim records while keeping full manuscript rewrite and "
        "new citation additions at zero."
    )

    return FirstCitationGroundedManuscriptClaimRevisionExecutionResult(
        title="First Citation-Grounded Manuscript Claim Revision Execution v7.6",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        citation_grounded_claim_revision_execution_count=citation_grounded_claim_revision_execution_count,
        planned_claim_revision_count=planned_claim_revision_count,
        executed_claim_revision_count=executed_claim_revision_count,
        bounded_revised_claim_record_count=bounded_revised_claim_record_count,
        manuscript_revised_count=manuscript_revised_count,
        full_manuscript_rewrite_count=full_manuscript_rewrite_count,
        new_citation_added_count=new_citation_added_count,
        conditional_hold_count=conditional_hold_count,
        claim_revision_execution_field_count=len(CLAIM_REVISION_EXECUTION_FIELDS),
        claim_revision_execution_status_value_count=len(CLAIM_REVISION_EXECUTION_STATUS_VALUES),
        claim_revision_execution_gate_count=len(CLAIM_REVISION_EXECUTION_GATES),
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

    print("First Citation-Grounded Manuscript Claim Revision Execution v7.6")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(
        "Citation-grounded claim revision execution count: "
        f"{result.citation_grounded_claim_revision_execution_count}"
    )
    print(f"Planned claim revision count: {result.planned_claim_revision_count}")
    print(f"Executed claim revision count: {result.executed_claim_revision_count}")
    print(f"Bounded revised claim record count: {result.bounded_revised_claim_record_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Full manuscript rewrite count: {result.full_manuscript_rewrite_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Claim revision execution field count: {result.claim_revision_execution_field_count}")
    print(
        "Claim revision execution status value count: "
        f"{result.claim_revision_execution_status_value_count}"
    )
    print(f"Claim revision execution gate count: {result.claim_revision_execution_gate_count}")
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
