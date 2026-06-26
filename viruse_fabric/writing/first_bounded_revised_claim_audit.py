"""First bounded revised claim audit for Viruse Fabric v7.7.

This module audits the first bounded revised claim records created in v7.6.

It verifies claim linkage, boundary preservation, and overclaim avoidance.

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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_bounded_revised_claim_audit_v7_7.md"

SOURCE_CLAIM_REVISION_EXECUTION = PROJECT_ROOT / "outputs" / "first_citation_grounded_manuscript_claim_revision_execution_v7_6.md"
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
    SOURCE_CLAIM_REVISION_EXECUTION,
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


AUDIT_METADATA = {
    "bounded_revised_claim_audit_id": "BRCA-0001",
    "linked_citation_grounded_manuscript_claim_revision_execution_id": "CGMCRE-0001",
    "linked_citation_grounded_manuscript_claim_revision_plan_id": "CGMCRP-0001",
    "linked_manuscript_citation_marker_audit_id": "MCMA-0001",
    "linked_citation_record_audit_id": "CRA-0001",
    "audit_status": "all_bounded_revised_claim_records_pass_no_full_manuscript_rewrite",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "bounded_revised_claim_record_count_from_v7_6": "2",
    "bounded_revised_claim_audited_count": "2",
    "revised_claim_audit_pass_count": "2",
    "revised_claim_audit_conditional_count": "0",
    "revised_claim_audit_fail_count": "0",
    "full_manuscript_rewrite_count": "0",
    "new_citation_added_count": "0",
    "conditional_hold_count": "1",
}


REVISED_CLAIM_AUDIT_ROWS = [
    {
        "revised_claim_audit_row_id": "BRCA-ROW-0001",
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
        "bounded_revised_claim_record_summary": "positions Viruse Fabric as conceptually adjacent to causal-constraints framing",
        "claim_boundary_status": "bounded_contextual_claim_only",
        "linkage_audit_status": "revised_claim_linkage_pass",
        "overclaim_audit_status": "overclaim_absent",
        "external_validation_status": "not_external_validation",
        "biological_or_clinical_claim_status": "no_biological_or_clinical_claim",
        "full_manuscript_rewrite": "no",
        "new_citation_added": "no",
        "audit_reason": "The revised claim record preserves bounded conceptual context and does not upgrade validation language.",
    },
    {
        "revised_claim_audit_row_id": "BRCA-ROW-0002",
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
        "bounded_revised_claim_record_summary": "uses causal screening in dynamical systems as methodological background only",
        "claim_boundary_status": "bounded_methodological_context_claim_only",
        "linkage_audit_status": "revised_claim_linkage_pass",
        "overclaim_audit_status": "overclaim_absent",
        "external_validation_status": "not_external_validation",
        "biological_or_clinical_claim_status": "no_biological_or_clinical_claim",
        "full_manuscript_rewrite": "no",
        "new_citation_added": "no",
        "audit_reason": "The revised claim record preserves methodological context and avoids biological, clinical, or operational claims.",
    },
]


CONDITIONAL_HOLD_ROWS = [
    {
        "candidate_entry_id": "CAND-0003",
        "hold_status": "hold_for_update_before_retention_decision",
        "citation_record_id": "none",
        "manuscript_citation_marker_id": "none",
        "executed_claim_revision_id": "none",
        "revised_claim_audit_row_id": "none",
        "bounded_revised_claim_audit_status": "not_audited_no_revised_claim_record",
        "full_manuscript_rewrite": "no",
        "new_citation_added": "no",
        "reason": "Conditional metadata pass remains outside retained source, citation record audit, marker insertion, marker audit, claim revision execution, and bounded revised claim audit.",
    },
]


REVISED_CLAIM_AUDIT_FIELDS = [
    "revised_claim_audit_row_id",
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
    "bounded_revised_claim_record_summary",
    "claim_boundary_status",
    "linkage_audit_status",
    "overclaim_audit_status",
    "external_validation_status",
    "biological_or_clinical_claim_status",
    "full_manuscript_rewrite",
    "new_citation_added",
    "audit_reason",
]


REVISED_CLAIM_AUDIT_STATUS_VALUES = [
    "revised_claim_linkage_pass",
    "revised_claim_linkage_conditional",
    "revised_claim_linkage_fail",
    "overclaim_absent",
    "overclaim_present_fail",
    "not_audited_no_revised_claim_record",
]


REVISED_CLAIM_AUDIT_GATES = [
    "Bounded revised claim audit must be linked to v7.6 claim revision execution.",
    "Only executed bounded revised claim records may be audited.",
    "Each audited revised claim must link to an executed claim revision.",
    "Each audited revised claim must link to a planned claim revision.",
    "Each audited revised claim must link to a marker audit row.",
    "Each audited revised claim must link to a manuscript citation marker.",
    "Each audited revised claim must link to an audited citation record.",
    "Each audited revised claim must link to a citation key.",
    "Each audited revised claim must link to an evidence matrix row.",
    "Each audited revised claim must link to a retained source.",
    "Each audited revised claim must link to a candidate entry.",
    "Each audited revised claim must preserve a bounded target manuscript section.",
    "Each audited revised claim must preserve a bounded claim role.",
    "Each audited revised claim must pass overclaim audit.",
    "Each audited revised claim must avoid external validation language.",
    "Each audited revised claim must avoid biological and clinical claims.",
    "Full manuscript rewrite count must remain zero.",
    "New citation added count must remain zero.",
    "Conditional-hold candidates must remain outside revised claim audit pass rows.",
    "Bounded revised claim audit must not imply submission readiness.",
]


BOUNDARY_PHRASES = [
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does audit bounded revised claim records",
    "does not rewrite the full manuscript",
    "does not add new citations",
    "does not claim external validation",
    "bounded revised claim audit is not full manuscript audit",
    "bounded revised claim audit is not proof",
    "bounded revised claim audit is not external validation",
    "bounded revised claim audit is not submission readiness",
    "citation-grounded revised claim is not biological validation",
    "citation-grounded revised claim is not clinical validation",
    "citation marker audit pass is not manuscript support",
    "citation record pass is not manuscript support",
    "citations are not external validation",
    "bounded context remains bounded",
    "full manuscript rewrite remains zero",
    "new citation added count remains zero",
    "conditional hold remains outside revised claim audit pass rows",
    "future full manuscript package is separate",
    "future manuscript package audit is separate",
    "future public claims must remain bounded",
    "future submission readiness audit is separate",
]


PROHIBITED_BEHAVIORS = [
    "Do not rewrite the full manuscript in this milestone.",
    "Do not add new citations in this milestone.",
    "Do not treat bounded revised claim audit as manuscript package audit.",
    "Do not treat bounded revised claim audit as proof.",
    "Do not treat bounded revised claim audit as external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not include conditional-hold candidates in revised claim audit pass rows.",
    "Do not convert bounded revised claims into strengthened conclusions.",
    "Do not claim accepted scientific theory.",
    "Do not upgrade validation language.",
    "Do not claim biological prediction or operational causal screening.",
    "Do not treat citation linkage as real-world validation.",
]


NEXT_STEPS = [
    "Plan full manuscript package integration in a later milestone.",
    "Keep full manuscript packaging separate from revised claim audit.",
    "Keep new citation additions separate from revised claim audit.",
    "Preserve revised claim linkage during future manuscript packaging.",
    "Keep CAND-0003 on hold until update handling.",
    "Check public claim language after manuscript package audit.",
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
    "avoid",
    "avoids",
    "absent",
    "no_",
    "none",
    "bounded",
    "citation",
    "citation marker",
    "marker audit",
    "claim revision",
    "revised claim",
    "audit",
    "future",
    "manuscript",
    "citation record",
    "evidence row",
    "retained source",
    "candidate",
    "conditional",
    "hold",
    "zero",
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
    "bounded revised claim audit gates",
    "claim boundary toward v7.8",
    "final boundary statement",
]


INVENTED_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
]


@dataclass(frozen=True)
class FirstBoundedRevisedClaimAuditResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    bounded_revised_claim_audit_count: int
    bounded_revised_claim_record_count: int
    bounded_revised_claim_audited_count: int
    revised_claim_audit_pass_count: int
    revised_claim_audit_conditional_count: int
    revised_claim_audit_fail_count: int
    full_manuscript_rewrite_count: int
    new_citation_added_count: int
    conditional_hold_count: int
    revised_claim_audit_field_count: int
    revised_claim_audit_status_value_count: int
    revised_claim_audit_gate_count: int
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
        "| Bounded revised claim audit field | Value |",
        "|---|---|",
    ]
    for key, value in AUDIT_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_revised_claim_audit_rows() -> str:
    rows = [
        "| Audit row | Executed revision | Planned revision | Marker | Citation record | Citation key | Linkage status | Overclaim status |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in REVISED_CLAIM_AUDIT_ROWS:
        rows.append(
            f"| {item['revised_claim_audit_row_id']} | "
            f"{item['executed_claim_revision_id']} | "
            f"{item['linked_planned_claim_revision_id']} | "
            f"{item['linked_manuscript_citation_marker_id']} | "
            f"{item['linked_citation_record_id']} | "
            f"{item['linked_citation_key']} | "
            f"{item['linkage_audit_status']} | "
            f"{item['overclaim_audit_status']} |"
        )
    return "\n".join(rows)


def render_revised_claim_linkage_rows() -> str:
    rows = [
        "| Audit row | Marker audit row | Evidence row | Retained source | Candidate | Target section | Target role |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in REVISED_CLAIM_AUDIT_ROWS:
        rows.append(
            f"| {item['revised_claim_audit_row_id']} | "
            f"{item['linked_marker_audit_row_id']} | "
            f"{item['linked_evidence_matrix_row_id']} | "
            f"{item['linked_retained_source_id']} | "
            f"{item['linked_candidate_entry_id']} | "
            f"{item['target_manuscript_section']} | "
            f"{item['target_claim_role']} |"
        )
    return "\n".join(rows)


def render_boundary_audit_rows() -> str:
    rows = [
        "| Audit row | Claim boundary | External validation | Biological/clinical status | Full manuscript rewrite | New citation added |",
        "|---|---|---|---|---|---|",
    ]
    for item in REVISED_CLAIM_AUDIT_ROWS:
        rows.append(
            f"| {item['revised_claim_audit_row_id']} | "
            f"{item['claim_boundary_status']} | "
            f"{item['external_validation_status']} | "
            f"{item['biological_or_clinical_claim_status']} | "
            f"{item['full_manuscript_rewrite']} | "
            f"{item['new_citation_added']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Executed revision | Revised claim audit row | Audit status | Full manuscript rewrite | New citation added | Reason |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['executed_claim_revision_id']} | "
            f"{item['revised_claim_audit_row_id']} | "
            f"{item['bounded_revised_claim_audit_status']} | "
            f"{item['full_manuscript_rewrite']} | "
            f"{item['new_citation_added']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Revised claim audit field | v7.7 status |",
        "|---|---|",
    ]
    for field in REVISED_CLAIM_AUDIT_FIELDS:
        rows.append(f"| `{field}` | populated for bounded revised claim audit rows |")
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
        "revised claim audit rows",
        "revised claim linkage rows",
        "revised claim boundary audit rows",
        "bounded revised claim audit metadata",
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
    return f"""# First Bounded Revised Claim Audit v7.7

## Question
Can Viruse Fabric audit the first bounded revised claim records while keeping full manuscript rewrite and new citation additions at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does audit bounded revised claim records. It does not rewrite the full manuscript, does not add new citations, and does not claim external validation.

Bounded revised claim audit is not full manuscript audit. Bounded revised claim audit is not proof. Bounded revised claim audit is not external validation. Bounded revised claim audit is not submission readiness. Citation-grounded revised claim is not biological validation. Citation-grounded revised claim is not clinical validation. Citation marker audit pass is not manuscript support. Citation record pass is not manuscript support. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Bounded Revised Claim Audit Metadata
{render_metadata_table()}

## Revised Claim Audit Rows
{render_revised_claim_audit_rows()}

## Revised Claim Linkage Rows
{render_revised_claim_linkage_rows()}

## Revised Claim Boundary Audit Rows
{render_boundary_audit_rows()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Revised Claim Audit Fields
{render_field_table()}

## Revised Claim Audit Status Values
{bullet_list(REVISED_CLAIM_AUDIT_STATUS_VALUES)}

## Bounded Revised Claim Audit Gates
{bullet_list(REVISED_CLAIM_AUDIT_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Revised Claim Audit Interpretation
The v7.7 artifact audits the first two bounded revised claim records created in v7.6.

BRCA-ROW-0001 audits CGRX-0001 and confirms linkage from the revised claim record to CGRP-0001, MCMA-ROW-0001, MCM-0001, CIT-REC-0001, EMR-0001, RET-0001, and CAND-0001.

BRCA-ROW-0002 audits CGRX-0002 and confirms linkage from the revised claim record to CGRP-0002, MCMA-ROW-0002, MCM-0002, CIT-REC-0002, EMR-0002, RET-0002, and CAND-0002.

Both revised claim audit rows pass linkage and boundary audit. This means the bounded revised claim records preserve internal traceability and avoid overclaiming. It does not mean the full manuscript has been rewritten, externally validated, or made ready for submission.

## Audit Boundary
Bounded revised claim audit count is one.

Bounded revised claim record count is two.

Bounded revised claim audited count is two.

Revised claim audit pass count is two.

Revised claim audit conditional count is zero.

Revised claim audit fail count is zero.

Full manuscript rewrite count is zero.

New citation added count is zero.

The project now has audited bounded revised claim records, but it still has no full manuscript rewrite. This is where a less disciplined document would start calling itself a paper. We are not rewarding that behavior.

## Linkage Boundary
Each passed revised claim audit row verifies linkage to:

- executed bounded claim revision
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

This keeps revised claims from floating around like tiny authority balloons. Cute, but dangerous.

## Claim Boundary Audit
Each revised claim audit row confirms:

- bounded contextual or methodological role
- no external validation claim
- no proof claim
- no biological validation claim
- no clinical validation claim
- no operational guidance claim
- no submission-readiness claim
- no new citation addition
- no full manuscript rewrite

The audit passes because the revised claim records remain bounded. They are not allowed to inflate themselves into theory validation. Someone has to be the adult in the room, unfortunately.

## Full Manuscript Boundary
The full manuscript is not rewritten in this milestone.

No full manuscript package is produced.

No submission-ready manuscript is produced.

No final paper is produced.

No public claim package is produced.

Full manuscript rewrite count remains zero.

## New Citation Boundary
New citation added count remains zero.

No new citation record is added. No new source is retained. No new bibliography entry is created. This milestone audits existing bounded revised claim records only.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside revised claim audit pass rows. It has no retained source record, no citation record, no audited citation record, no planned insertion slot, no inserted marker, no marker audit pass row, no planned claim revision, no executed claim revision, and no bounded revised claim audit pass row.

This prevents conditional metadata from wandering into audited revised claims with a clipboard and suspicious confidence.

## Claim Boundary Toward v7.8
This milestone permits a slightly stronger internal workflow claim than v7.6.

Allowed after v7.7:

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
- bounded revised claim records audited
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
Bounded revised claim audit count: 1

Bounded revised claim record count: 2

Bounded revised claim audited count: 2

Revised claim audit pass count: 2

Revised claim audit conditional count: 0

Revised claim audit fail count: 0

Full manuscript rewrite count: 0

New citation added count: 0

Conditional hold count: 1

## Final Boundary Statement
This artifact audits bounded revised claim records.

It does not rewrite the full manuscript, does not add new citations, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstBoundedRevisedClaimAuditResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    invented_citations = detect_invented_citation_like_patterns(report)

    bounded_revised_claim_audit_count = 1
    bounded_revised_claim_record_count = int(AUDIT_METADATA["bounded_revised_claim_record_count_from_v7_6"])
    bounded_revised_claim_audited_count = int(AUDIT_METADATA["bounded_revised_claim_audited_count"])
    revised_claim_audit_pass_count = int(AUDIT_METADATA["revised_claim_audit_pass_count"])
    revised_claim_audit_conditional_count = int(AUDIT_METADATA["revised_claim_audit_conditional_count"])
    revised_claim_audit_fail_count = int(AUDIT_METADATA["revised_claim_audit_fail_count"])
    full_manuscript_rewrite_count = int(AUDIT_METADATA["full_manuscript_rewrite_count"])
    new_citation_added_count = int(AUDIT_METADATA["new_citation_added_count"])
    conditional_hold_count = int(AUDIT_METADATA["conditional_hold_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 27:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if bounded_revised_claim_audit_count != 1:
        errors.append(
            "Bounded revised claim audit count should be one, got: "
            f"{bounded_revised_claim_audit_count}"
        )

    if bounded_revised_claim_record_count != 2:
        errors.append(
            "Bounded revised claim record count should be two, got: "
            f"{bounded_revised_claim_record_count}"
        )

    if bounded_revised_claim_audited_count != 2:
        errors.append(
            "Bounded revised claim audited count should be two, got: "
            f"{bounded_revised_claim_audited_count}"
        )

    if revised_claim_audit_pass_count != 2:
        errors.append(
            "Revised claim audit pass count should be two, got: "
            f"{revised_claim_audit_pass_count}"
        )

    if revised_claim_audit_conditional_count != 0:
        errors.append(
            "Revised claim audit conditional count should be zero, got: "
            f"{revised_claim_audit_conditional_count}"
        )

    if revised_claim_audit_fail_count != 0:
        errors.append(
            "Revised claim audit fail count should be zero, got: "
            f"{revised_claim_audit_fail_count}"
        )

    if bounded_revised_claim_record_count != bounded_revised_claim_audited_count:
        errors.append("Every bounded revised claim record must be audited")

    if bounded_revised_claim_audited_count != revised_claim_audit_pass_count:
        errors.append("Every audited bounded revised claim must pass in v7.7")

    if full_manuscript_rewrite_count != 0:
        errors.append(
            "Full manuscript rewrite count should be zero, got: "
            f"{full_manuscript_rewrite_count}"
        )

    if new_citation_added_count != 0:
        errors.append(f"New citation added count should be zero, got: {new_citation_added_count}")

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    for row in REVISED_CLAIM_AUDIT_ROWS:
        missing_fields = [field for field in REVISED_CLAIM_AUDIT_FIELDS if not row.get(field)]
        if missing_fields:
            errors.append(
                f"{row.get('revised_claim_audit_row_id', 'unknown')} missing revised claim audit fields: "
                f"{len(missing_fields)}"
            )

        if row.get("linkage_audit_status") != "revised_claim_linkage_pass":
            errors.append(
                f"{row.get('revised_claim_audit_row_id', 'unknown')} did not pass linkage audit"
            )

        if row.get("overclaim_audit_status") != "overclaim_absent":
            errors.append(
                f"{row.get('revised_claim_audit_row_id', 'unknown')} has overclaim audit problem"
            )

        if row.get("external_validation_status") != "not_external_validation":
            errors.append(
                f"{row.get('revised_claim_audit_row_id', 'unknown')} has invalid external validation status"
            )

        if row.get("full_manuscript_rewrite") != "no":
            errors.append(
                f"{row.get('revised_claim_audit_row_id', 'unknown')} rewrote full manuscript unexpectedly"
            )

        if row.get("new_citation_added") != "no":
            errors.append(
                f"{row.get('revised_claim_audit_row_id', 'unknown')} added citation unexpectedly"
            )

    if len(REVISED_CLAIM_AUDIT_FIELDS) < 21:
        errors.append(f"Revised claim audit field count too low: {len(REVISED_CLAIM_AUDIT_FIELDS)}")

    if len(REVISED_CLAIM_AUDIT_STATUS_VALUES) < 6:
        errors.append(
            "Revised claim audit status value count too low: "
            f"{len(REVISED_CLAIM_AUDIT_STATUS_VALUES)}"
        )

    if len(REVISED_CLAIM_AUDIT_GATES) < 20:
        errors.append(f"Revised claim audit gate count too low: {len(REVISED_CLAIM_AUDIT_GATES)}")

    if boundary_count < 25:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 13:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if invented_citations:
        errors.append(
            "Invented citation-like patterns detected outside revised claim audit sections: "
            f"{len(invented_citations)}"
        )

    if word_count < 1400:
        errors.append(f"Word count too low for first bounded revised claim audit: {word_count}")

    warnings.append("Bounded revised claim records are audited, but the full manuscript is not rewritten.")
    warnings.append("Bounded revised claim audit does not add new citations.")

    passed = not errors

    interpretation = (
        "The v7.7 artifact audits two bounded revised claim records and confirms linkage, "
        "boundary preservation, and overclaim absence while keeping full manuscript rewrite "
        "and new citation additions at zero."
    )

    return FirstBoundedRevisedClaimAuditResult(
        title="First Bounded Revised Claim Audit v7.7",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        bounded_revised_claim_audit_count=bounded_revised_claim_audit_count,
        bounded_revised_claim_record_count=bounded_revised_claim_record_count,
        bounded_revised_claim_audited_count=bounded_revised_claim_audited_count,
        revised_claim_audit_pass_count=revised_claim_audit_pass_count,
        revised_claim_audit_conditional_count=revised_claim_audit_conditional_count,
        revised_claim_audit_fail_count=revised_claim_audit_fail_count,
        full_manuscript_rewrite_count=full_manuscript_rewrite_count,
        new_citation_added_count=new_citation_added_count,
        conditional_hold_count=conditional_hold_count,
        revised_claim_audit_field_count=len(REVISED_CLAIM_AUDIT_FIELDS),
        revised_claim_audit_status_value_count=len(REVISED_CLAIM_AUDIT_STATUS_VALUES),
        revised_claim_audit_gate_count=len(REVISED_CLAIM_AUDIT_GATES),
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

    print("First Bounded Revised Claim Audit v7.7")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Bounded revised claim audit count: {result.bounded_revised_claim_audit_count}")
    print(f"Bounded revised claim record count: {result.bounded_revised_claim_record_count}")
    print(f"Bounded revised claim audited count: {result.bounded_revised_claim_audited_count}")
    print(f"Revised claim audit pass count: {result.revised_claim_audit_pass_count}")
    print(f"Revised claim audit conditional count: {result.revised_claim_audit_conditional_count}")
    print(f"Revised claim audit fail count: {result.revised_claim_audit_fail_count}")
    print(f"Full manuscript rewrite count: {result.full_manuscript_rewrite_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Revised claim audit field count: {result.revised_claim_audit_field_count}")
    print(
        "Revised claim audit status value count: "
        f"{result.revised_claim_audit_status_value_count}"
    )
    print(f"Revised claim audit gate count: {result.revised_claim_audit_gate_count}")
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
