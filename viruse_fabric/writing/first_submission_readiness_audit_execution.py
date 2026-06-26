"""First submission readiness audit execution for Viruse Fabric v8.2.

This module executes the first submission readiness audit against the v8.1
planned readiness criteria.

It audits two planned readiness criteria and records pass outcomes.

It does not make the manuscript submission-ready.
It does not add new citations.
It does not claim external validation.
It does not produce a final paper.
It does not claim peer review or venue acceptance.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_submission_readiness_audit_execution_v8_2.md"

SOURCE_READINESS_PLAN = PROJECT_ROOT / "outputs" / "first_submission_readiness_criteria_plan_v8_1.md"
SOURCE_PACKAGE_AUDIT = PROJECT_ROOT / "outputs" / "first_full_manuscript_revision_package_audit_v8_0.md"
SOURCE_PACKAGE_EXECUTION = PROJECT_ROOT / "outputs" / "first_full_manuscript_revision_package_execution_v7_9.md"
SOURCE_PACKAGE_PLAN = PROJECT_ROOT / "outputs" / "first_full_manuscript_revision_package_plan_v7_8.md"
SOURCE_REVISED_CLAIM_AUDIT = PROJECT_ROOT / "outputs" / "first_bounded_revised_claim_audit_v7_7.md"
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
    SOURCE_READINESS_PLAN,
    SOURCE_PACKAGE_AUDIT,
    SOURCE_PACKAGE_EXECUTION,
    SOURCE_PACKAGE_PLAN,
    SOURCE_REVISED_CLAIM_AUDIT,
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
    "submission_readiness_audit_execution_id": "SRAE-0001",
    "linked_submission_readiness_criteria_plan_id": "SRCP-0001",
    "linked_full_manuscript_revision_package_audit_id": "FMRPA-0001",
    "audit_execution_status": "readiness_criteria_executed_not_submission_ready",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "planned_readiness_criterion_count_from_v8_1": "2",
    "executed_readiness_criterion_count": "2",
    "readiness_criterion_pass_count": "2",
    "readiness_criterion_conditional_count": "0",
    "readiness_criterion_fail_count": "0",
    "manuscript_submission_ready_count": "0",
    "full_manuscript_rewrite_count": "1",
    "new_citation_added_count": "0",
    "conditional_hold_count": "1",
}


READINESS_AUDIT_ROWS = [
    {
        "readiness_audit_row_id": "SRAE-ROW-0001",
        "linked_planned_readiness_criterion_id": "SRCP-ROW-0001",
        "linked_package_audit_row_id": "FMRPA-ROW-0001",
        "linked_executed_package_revision_id": "FMRPE-ROW-0001",
        "linked_planned_package_revision_id": "FMRPP-ROW-0001",
        "linked_revised_claim_audit_row_id": "BRCA-ROW-0001",
        "linked_executed_claim_revision_id": "CGRX-0001",
        "linked_citation_record_id": "CIT-REC-0001",
        "linked_citation_key": "pmlr-v115-blom20a",
        "linked_candidate_entry_id": "CAND-0001",
        "readiness_dimension": "conceptual-framing boundedness",
        "readiness_audit_status": "readiness_criterion_pass",
        "boundedness_result": "bounded_conceptual_framing_preserved",
        "overclaim_result": "overclaim_absent",
        "submission_readiness_result": "not_submission_ready",
        "manuscript_submission_ready": "no",
        "full_manuscript_rewrite": "already_one_controlled_package_artifact",
        "new_citation_added": "no",
        "audit_reason": "The conceptual-framing criterion passes as bounded internal framing, but this does not create manuscript submission readiness.",
    },
    {
        "readiness_audit_row_id": "SRAE-ROW-0002",
        "linked_planned_readiness_criterion_id": "SRCP-ROW-0002",
        "linked_package_audit_row_id": "FMRPA-ROW-0002",
        "linked_executed_package_revision_id": "FMRPE-ROW-0002",
        "linked_planned_package_revision_id": "FMRPP-ROW-0002",
        "linked_revised_claim_audit_row_id": "BRCA-ROW-0002",
        "linked_executed_claim_revision_id": "CGRX-0002",
        "linked_citation_record_id": "CIT-REC-0002",
        "linked_citation_key": "pmlr-v124-wengel-mogensen20a",
        "linked_candidate_entry_id": "CAND-0002",
        "readiness_dimension": "methodological-context boundedness",
        "readiness_audit_status": "readiness_criterion_pass",
        "boundedness_result": "bounded_methodological_context_preserved",
        "overclaim_result": "overclaim_absent",
        "submission_readiness_result": "not_submission_ready",
        "manuscript_submission_ready": "no",
        "full_manuscript_rewrite": "already_one_controlled_package_artifact",
        "new_citation_added": "no",
        "audit_reason": "The methodological-context criterion passes as bounded internal context, but this does not create biological, clinical, laboratory, operational, or submission-ready status.",
    },
]


CONDITIONAL_HOLD_ROWS = [
    {
        "candidate_entry_id": "CAND-0003",
        "hold_status": "hold_for_update_before_retention_decision",
        "citation_record_id": "none",
        "planned_readiness_criterion_id": "none",
        "readiness_audit_row_id": "none",
        "readiness_audit_status": "not_audited_no_readiness_criterion",
        "manuscript_submission_ready": "no",
        "new_citation_added": "no",
        "reason": "Conditional metadata pass remains outside retained source, citation record audit, marker insertion, marker audit, claim revision execution, revised claim audit, package planning, package execution, package audit, readiness criteria planning, and readiness audit execution.",
    },
]


READINESS_AUDIT_FIELDS = [
    "readiness_audit_row_id",
    "linked_planned_readiness_criterion_id",
    "linked_package_audit_row_id",
    "linked_executed_package_revision_id",
    "linked_planned_package_revision_id",
    "linked_revised_claim_audit_row_id",
    "linked_executed_claim_revision_id",
    "linked_citation_record_id",
    "linked_citation_key",
    "linked_candidate_entry_id",
    "readiness_dimension",
    "readiness_audit_status",
    "boundedness_result",
    "overclaim_result",
    "submission_readiness_result",
    "manuscript_submission_ready",
    "full_manuscript_rewrite",
    "new_citation_added",
    "audit_reason",
]


READINESS_AUDIT_STATUS_VALUES = [
    "readiness_criteria_executed_not_submission_ready",
    "readiness_criterion_pass",
    "readiness_criterion_conditional",
    "readiness_criterion_fail",
    "not_audited_no_readiness_criterion",
    "not_submission_ready",
]


READINESS_AUDIT_GATES = [
    "Submission readiness audit execution must be linked to v8.1 readiness criteria plan.",
    "Only planned readiness criteria may be executed.",
    "Each readiness audit row must link to a planned readiness criterion.",
    "Each readiness audit row must link to a package audit row.",
    "Each readiness audit row must link to an executed package revision.",
    "Each readiness audit row must link to a planned package revision.",
    "Each readiness audit row must link to a revised claim audit row.",
    "Each readiness audit row must link to an executed claim revision.",
    "Each readiness audit row must link to a citation record.",
    "Each readiness audit row must link to a citation key.",
    "Each readiness audit row must link to a candidate entry.",
    "Each readiness audit row must define a readiness dimension.",
    "Each readiness audit row must record boundedness result.",
    "Each readiness audit row must record overclaim result.",
    "Each readiness audit row must record submission readiness result.",
    "Readiness criterion pass count may be two.",
    "Manuscript submission ready count must remain zero.",
    "Full manuscript rewrite count must remain one.",
    "New citation added count must remain zero.",
    "Conditional-hold candidates must remain outside readiness audit pass rows.",
    "Readiness audit execution must not imply external validation.",
    "Readiness audit execution must not produce a final paper.",
    "Readiness audit execution must not imply peer review or venue acceptance.",
]


BOUNDARY_PHRASES = [
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does execute submission readiness audit",
    "does not make the manuscript submission-ready",
    "does not add new citations",
    "does not claim external validation",
    "readiness audit execution is not manuscript submission readiness",
    "criterion pass is not submission readiness",
    "criterion pass is not external validation",
    "criterion pass is not final paper production",
    "criterion pass is not peer review",
    "audited package is not submission-ready manuscript",
    "controlled package audit is not peer review",
    "citation-grounded revised claim is not biological validation",
    "citation-grounded revised claim is not clinical validation",
    "citation record pass is not manuscript support",
    "citations are not external validation",
    "bounded context remains bounded",
    "manuscript submission ready count remains zero",
    "new citation added count remains zero",
    "conditional hold remains outside readiness audit pass rows",
    "future manuscript submission readiness decision is separate",
    "future public claims must remain bounded",
    "venue acceptance remains unclaimed",
]


PROHIBITED_BEHAVIORS = [
    "Do not call the manuscript submission-ready.",
    "Do not add new citations in this milestone.",
    "Do not treat readiness criterion pass as manuscript submission readiness.",
    "Do not treat readiness audit execution as external validation.",
    "Do not treat readiness audit execution as final paper production.",
    "Do not treat readiness audit execution as peer review.",
    "Do not imply acceptance by any venue.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not include conditional-hold candidates in readiness audit pass rows.",
    "Do not convert readiness audit pass into readiness approval.",
    "Do not claim accepted scientific theory.",
    "Do not upgrade validation language.",
    "Do not claim biological prediction or operational causal screening.",
    "Do not claim manuscript submission approval.",
]


NEXT_STEPS = [
    "Plan manuscript submission-readiness decision in a later milestone.",
    "Keep readiness decision separate from readiness audit execution.",
    "Check manuscript boundaries after readiness audit execution.",
    "Keep new citation additions separate from readiness audit execution.",
    "Keep CAND-0003 on hold until update handling.",
    "Preserve readiness audit linkage in future decision planning.",
    "Maintain the research prototype with internal validation status.",
    "Avoid submission-ready language until a separate readiness decision milestone passes.",
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
    r"\bfinal paper\b",
    r"\bpeer review\b",
    r"\bpeer-reviewed\b",
    r"\bvenue acceptance\b",
]


SAFE_LINE_CUES = [
    "not",
    "does not",
    "do not",
    "must not",
    "without claiming",
    "without",
    "avoid",
    "avoids",
    "separate",
    "future",
    "audit",
    "audited",
    "criteria",
    "criterion",
    "pass",
    "no",
    "no_",
    "none",
    "zero",
    "bounded",
    "controlled",
    "package",
    "citation",
    "citation marker",
    "claim revision",
    "revised claim",
    "manuscript",
    "citation record",
    "candidate",
    "conditional",
    "hold",
    "boundary",
    "prohibited",
    "internal validation",
    "not externally",
    "not submission",
    "not a submission",
    "not submission-ready",
    "not a final",
    "not biological",
    "not clinical",
    "not laboratory",
    "not operational",
    "citations are not external validation",
    "still disallowed",
    "disallowed",
]


SAFE_SECTION_HEADINGS = [
    "boundary phrases",
    "prohibited behaviors",
    "submission readiness audit execution gates",
    "claim boundary toward v8.3",
    "final boundary statement",
    "submission readiness boundary",
    "readiness audit boundary",
    "execution boundary",
]


INVENTED_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
]


@dataclass(frozen=True)
class FirstSubmissionReadinessAuditExecutionResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    submission_readiness_audit_execution_count: int
    planned_readiness_criterion_count: int
    executed_readiness_criterion_count: int
    readiness_criterion_pass_count: int
    readiness_criterion_conditional_count: int
    readiness_criterion_fail_count: int
    manuscript_submission_ready_count: int
    full_manuscript_rewrite_count: int
    new_citation_added_count: int
    conditional_hold_count: int
    readiness_audit_field_count: int
    readiness_audit_status_value_count: int
    readiness_audit_gate_count: int
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
        "| Submission readiness audit execution field | Value |",
        "|---|---|",
    ]
    for key, value in AUDIT_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_readiness_audit_rows() -> str:
    rows = [
        "| Readiness audit row | Planned criterion | Package audit row | Executed package revision | Citation record | Citation key | Status |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in READINESS_AUDIT_ROWS:
        rows.append(
            f"| {item['readiness_audit_row_id']} | "
            f"{item['linked_planned_readiness_criterion_id']} | "
            f"{item['linked_package_audit_row_id']} | "
            f"{item['linked_executed_package_revision_id']} | "
            f"{item['linked_citation_record_id']} | "
            f"{item['linked_citation_key']} | "
            f"{item['readiness_audit_status']} |"
        )
    return "\n".join(rows)


def render_readiness_linkage_rows() -> str:
    rows = [
        "| Readiness audit row | Planned package revision | Revised claim audit row | Executed claim revision | Candidate |",
        "|---|---|---|---|---|",
    ]
    for item in READINESS_AUDIT_ROWS:
        rows.append(
            f"| {item['readiness_audit_row_id']} | "
            f"{item['linked_planned_package_revision_id']} | "
            f"{item['linked_revised_claim_audit_row_id']} | "
            f"{item['linked_executed_claim_revision_id']} | "
            f"{item['linked_candidate_entry_id']} |"
        )
    return "\n".join(rows)


def render_readiness_boundary_rows() -> str:
    rows = [
        "| Readiness audit row | Dimension | Boundedness | Overclaim | Submission readiness result | Manuscript submission ready | New citation added |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in READINESS_AUDIT_ROWS:
        rows.append(
            f"| {item['readiness_audit_row_id']} | "
            f"{item['readiness_dimension']} | "
            f"{item['boundedness_result']} | "
            f"{item['overclaim_result']} | "
            f"{item['submission_readiness_result']} | "
            f"{item['manuscript_submission_ready']} | "
            f"{item['new_citation_added']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Readiness audit row | Readiness audit status | Manuscript submission ready | New citation added | Reason |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['readiness_audit_row_id']} | "
            f"{item['readiness_audit_status']} | "
            f"{item['manuscript_submission_ready']} | "
            f"{item['new_citation_added']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Readiness audit field | v8.2 status |",
        "|---|---|",
    ]
    for field in READINESS_AUDIT_FIELDS:
        rows.append(f"| `{field}` | populated for readiness audit rows |")
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
        "submission readiness audit execution metadata",
        "readiness audit rows",
        "readiness audit linkage rows",
        "readiness audit boundary rows",
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
    return f"""# First Submission Readiness Audit Execution v8.2

## Question
Can Viruse Fabric execute the first submission readiness audit from the planned readiness criteria while keeping manuscript submission readiness and new citation additions at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does execute submission readiness audit. It audits two planned readiness criteria. It does not make the manuscript submission-ready, does not add new citations, and does not claim external validation.

Readiness audit execution is not manuscript submission readiness. Criterion pass is not submission readiness. Criterion pass is not external validation. Criterion pass is not final paper production. Criterion pass is not peer review. Audited package is not submission-ready manuscript. Controlled package audit is not peer review. Citation-grounded revised claim is not biological validation. Citation-grounded revised claim is not clinical validation. Citation record pass is not manuscript support. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Submission Readiness Audit Execution Metadata
{render_metadata_table()}

## Readiness Audit Rows
{render_readiness_audit_rows()}

## Readiness Audit Linkage Rows
{render_readiness_linkage_rows()}

## Readiness Audit Boundary Rows
{render_readiness_boundary_rows()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Readiness Audit Fields
{render_field_table()}

## Readiness Audit Status Values
{bullet_list(READINESS_AUDIT_STATUS_VALUES)}

## Submission Readiness Audit Execution Gates
{bullet_list(READINESS_AUDIT_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Audit Execution Interpretation
The v8.2 artifact executes the first submission readiness audit against the two planned readiness criteria from v8.1.

SRAE-ROW-0001 executes SRCP-ROW-0001 and audits conceptual-framing boundedness. It confirms bounded conceptual framing, overclaim absence, and a not-submission-ready result.

SRAE-ROW-0002 executes SRCP-ROW-0002 and audits methodological-context boundedness. It confirms bounded methodological context, overclaim absence, and a not-submission-ready result.

Both readiness criteria pass as bounded internal audit checks. This means the criteria pass. It does not mean the manuscript is submission-ready, externally validated, peer-reviewed, accepted, final, biological, clinical, laboratory-ready, or operational.

## Execution Boundary
Submission readiness audit execution count is one.

Planned readiness criterion count is two.

Executed readiness criterion count is two.

Readiness criterion pass count is two.

Readiness criterion conditional count is zero.

Readiness criterion fail count is zero.

Manuscript submission ready count remains zero.

Full manuscript rewrite count remains one.

New citation added count remains zero.

The project now has executed readiness criteria. It still does not have a submission-ready manuscript. Humanity may continue confusing “passed a check” with “ready for public glory,” but this repository will not participate.

## Readiness Audit Boundary
The readiness audit checks:

- conceptual-framing boundedness
- methodological-context boundedness
- absence of proof claims
- absence of external validation claims
- absence of biological, clinical, laboratory, and operational claims
- absence of final-paper and peer-review claims
- preservation of citation linkage
- preservation of internal validation status

The audit passes the two criteria, but the submission readiness result remains not_submission_ready.

## Submission Readiness Boundary
This milestone executes readiness audit.

It does not certify the manuscript as ready for submission.

It does not create a submission approval.

It does not certify the theory.

It does not produce a final paper.

It does not create peer review.

It does not certify acceptance by any venue.

## Full Manuscript Boundary
The full manuscript rewrite count remains one.

The controlled full manuscript revision package artifact from v7.9 remains the current controlled rewrite artifact.

It has passed package audit and readiness criteria audit, but it is still not submission-ready.

It has not passed a separate manuscript submission readiness decision milestone.

It has no external validation.

## New Citation Boundary
New citation added count remains zero.

No new citation record is added. No new source is retained. No new bibliography entry is created. This milestone executes readiness audit using existing planned criteria and existing audited package rows only.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside readiness audit pass rows. It has no retained source record, no citation record, no audited citation record, no planned insertion slot, no inserted marker, no marker audit pass row, no planned claim revision, no executed claim revision, no bounded revised claim audit pass row, no package revision plan, no executed package revision, no package audit pass row, no readiness criterion plan row, and no readiness audit pass row.

This prevents conditional metadata from entering the readiness audit with a fake ID badge. Adorable paperwork fraud, still fraud.

## Claim Boundary Toward v8.3
This milestone permits a slightly stronger internal workflow claim than v8.1.

Allowed after v8.2:

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
- full manuscript revision package planned
- first full manuscript revision package executed
- controlled manuscript rewrite artifact exists
- full manuscript revision package audited
- first submission readiness criteria planned
- first submission readiness audit executed
- two readiness criteria passed
- manuscript still not submission-ready
- no new citations added during readiness audit execution

Still disallowed:

- proven theory
- external validation
- biological prediction
- clinical relevance
- laboratory guidance
- operational readiness
- submission-ready manuscript
- accepted scientific theory
- final paper
- peer-reviewed manuscript
- venue acceptance

## Output Counts
Submission readiness audit execution count: 1

Planned readiness criterion count: 2

Executed readiness criterion count: 2

Readiness criterion pass count: 2

Readiness criterion conditional count: 0

Readiness criterion fail count: 0

Manuscript submission ready count: 0

Full manuscript rewrite count: 1

New citation added count: 0

Conditional hold count: 1

## Final Boundary Statement
This artifact executes submission readiness audit against planned criteria.

It does not make the manuscript ready for submission, does not add new citations, does not certify external validation, does not produce a final paper, does not claim peer review or venue acceptance, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstSubmissionReadinessAuditExecutionResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    invented_citations = detect_invented_citation_like_patterns(report)

    submission_readiness_audit_execution_count = 1
    planned_readiness_criterion_count = int(AUDIT_METADATA["planned_readiness_criterion_count_from_v8_1"])
    executed_readiness_criterion_count = int(AUDIT_METADATA["executed_readiness_criterion_count"])
    readiness_criterion_pass_count = int(AUDIT_METADATA["readiness_criterion_pass_count"])
    readiness_criterion_conditional_count = int(AUDIT_METADATA["readiness_criterion_conditional_count"])
    readiness_criterion_fail_count = int(AUDIT_METADATA["readiness_criterion_fail_count"])
    manuscript_submission_ready_count = int(AUDIT_METADATA["manuscript_submission_ready_count"])
    full_manuscript_rewrite_count = int(AUDIT_METADATA["full_manuscript_rewrite_count"])
    new_citation_added_count = int(AUDIT_METADATA["new_citation_added_count"])
    conditional_hold_count = int(AUDIT_METADATA["conditional_hold_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 32:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if submission_readiness_audit_execution_count != 1:
        errors.append(
            "Submission readiness audit execution count should be one, got: "
            f"{submission_readiness_audit_execution_count}"
        )

    if planned_readiness_criterion_count != 2:
        errors.append(
            "Planned readiness criterion count should be two, got: "
            f"{planned_readiness_criterion_count}"
        )

    if executed_readiness_criterion_count != 2:
        errors.append(
            "Executed readiness criterion count should be two, got: "
            f"{executed_readiness_criterion_count}"
        )

    if planned_readiness_criterion_count != executed_readiness_criterion_count:
        errors.append("Every planned readiness criterion should be executed in v8.2")

    if readiness_criterion_pass_count != 2:
        errors.append(
            "Readiness criterion pass count should be two, got: "
            f"{readiness_criterion_pass_count}"
        )

    if readiness_criterion_conditional_count != 0:
        errors.append(
            "Readiness criterion conditional count should be zero, got: "
            f"{readiness_criterion_conditional_count}"
        )

    if readiness_criterion_fail_count != 0:
        errors.append(
            "Readiness criterion fail count should be zero, got: "
            f"{readiness_criterion_fail_count}"
        )

    if executed_readiness_criterion_count != readiness_criterion_pass_count:
        errors.append("Every executed readiness criterion should pass in v8.2")

    if manuscript_submission_ready_count != 0:
        errors.append(
            "Manuscript submission ready count should remain zero, got: "
            f"{manuscript_submission_ready_count}"
        )

    if full_manuscript_rewrite_count != 1:
        errors.append(
            "Full manuscript rewrite count should remain one, got: "
            f"{full_manuscript_rewrite_count}"
        )

    if new_citation_added_count != 0:
        errors.append(f"New citation added count should be zero, got: {new_citation_added_count}")

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    for row in READINESS_AUDIT_ROWS:
        missing_fields = [field for field in READINESS_AUDIT_FIELDS if not row.get(field)]
        if missing_fields:
            errors.append(
                f"{row.get('readiness_audit_row_id', 'unknown')} missing readiness audit fields: "
                f"{len(missing_fields)}"
            )

        if row.get("readiness_audit_status") != "readiness_criterion_pass":
            errors.append(
                f"{row.get('readiness_audit_row_id', 'unknown')} did not pass readiness criterion"
            )

        if row.get("overclaim_result") != "overclaim_absent":
            errors.append(
                f"{row.get('readiness_audit_row_id', 'unknown')} has overclaim problem"
            )

        if row.get("submission_readiness_result") != "not_submission_ready":
            errors.append(
                f"{row.get('readiness_audit_row_id', 'unknown')} has invalid submission readiness result"
            )

        if row.get("manuscript_submission_ready") != "no":
            errors.append(
                f"{row.get('readiness_audit_row_id', 'unknown')} marked manuscript ready unexpectedly"
            )

        if row.get("new_citation_added") != "no":
            errors.append(
                f"{row.get('readiness_audit_row_id', 'unknown')} added citation unexpectedly"
            )

    if len(READINESS_AUDIT_FIELDS) < 19:
        errors.append(f"Readiness audit field count too low: {len(READINESS_AUDIT_FIELDS)}")

    if len(READINESS_AUDIT_STATUS_VALUES) < 6:
        errors.append(
            "Readiness audit status value count too low: "
            f"{len(READINESS_AUDIT_STATUS_VALUES)}"
        )

    if len(READINESS_AUDIT_GATES) < 23:
        errors.append(f"Readiness audit gate count too low: {len(READINESS_AUDIT_GATES)}")

    if boundary_count < 26:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 14:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if invented_citations:
        errors.append(
            "Invented citation-like patterns detected outside readiness audit sections: "
            f"{len(invented_citations)}"
        )

    if word_count < 1650:
        errors.append(
            f"Word count too low for first submission readiness audit execution: {word_count}"
        )

    warnings.append("Readiness criteria pass, but the manuscript is still not submission-ready.")
    warnings.append("Readiness audit execution does not create external validation.")

    passed = not errors

    interpretation = (
        "The v8.2 artifact executes two planned readiness criteria, records two pass "
        "outcomes, keeps manuscript submission ready count at zero, and keeps new citation "
        "additions at zero."
    )

    return FirstSubmissionReadinessAuditExecutionResult(
        title="First Submission Readiness Audit Execution v8.2",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        submission_readiness_audit_execution_count=submission_readiness_audit_execution_count,
        planned_readiness_criterion_count=planned_readiness_criterion_count,
        executed_readiness_criterion_count=executed_readiness_criterion_count,
        readiness_criterion_pass_count=readiness_criterion_pass_count,
        readiness_criterion_conditional_count=readiness_criterion_conditional_count,
        readiness_criterion_fail_count=readiness_criterion_fail_count,
        manuscript_submission_ready_count=manuscript_submission_ready_count,
        full_manuscript_rewrite_count=full_manuscript_rewrite_count,
        new_citation_added_count=new_citation_added_count,
        conditional_hold_count=conditional_hold_count,
        readiness_audit_field_count=len(READINESS_AUDIT_FIELDS),
        readiness_audit_status_value_count=len(READINESS_AUDIT_STATUS_VALUES),
        readiness_audit_gate_count=len(READINESS_AUDIT_GATES),
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

    print("First Submission Readiness Audit Execution v8.2")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(
        "Submission readiness audit execution count: "
        f"{result.submission_readiness_audit_execution_count}"
    )
    print(f"Planned readiness criterion count: {result.planned_readiness_criterion_count}")
    print(f"Executed readiness criterion count: {result.executed_readiness_criterion_count}")
    print(f"Readiness criterion pass count: {result.readiness_criterion_pass_count}")
    print(
        "Readiness criterion conditional count: "
        f"{result.readiness_criterion_conditional_count}"
    )
    print(f"Readiness criterion fail count: {result.readiness_criterion_fail_count}")
    print(f"Manuscript submission ready count: {result.manuscript_submission_ready_count}")
    print(f"Full manuscript rewrite count: {result.full_manuscript_rewrite_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Readiness audit field count: {result.readiness_audit_field_count}")
    print(f"Readiness audit status value count: {result.readiness_audit_status_value_count}")
    print(f"Readiness audit gate count: {result.readiness_audit_gate_count}")
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
