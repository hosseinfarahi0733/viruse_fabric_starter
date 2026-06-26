"""Manuscript submission readiness decision plan for Viruse Fabric v8.3.

This module plans the first manuscript submission readiness decision layer
from the v8.2 submission readiness audit execution.

It does not execute a submission readiness decision.
It does not make the manuscript submission-ready.
It does not add new citations.
It does not claim external validation.
It does not produce a final paper.
It does not claim formal mathematical proof.
It does not claim independent experiment.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "manuscript_submission_readiness_decision_plan_v8_3.md"

SOURCE_READINESS_AUDIT = PROJECT_ROOT / "outputs" / "first_submission_readiness_audit_execution_v8_2.md"
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
    SOURCE_READINESS_AUDIT,
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


PLAN_METADATA = {
    "submission_readiness_decision_plan_id": "SRDP-0001",
    "linked_submission_readiness_audit_execution_id": "SRAE-0001",
    "linked_submission_readiness_criteria_plan_id": "SRCP-0001",
    "linked_full_manuscript_revision_package_audit_id": "FMRPA-0001",
    "plan_status": "decision_plan_only_no_decision_execution",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "executed_readiness_criterion_count_from_v8_2": "2",
    "planned_decision_row_count": "2",
    "submission_readiness_decision_execution_count": "0",
    "manuscript_submission_ready_count": "0",
    "full_manuscript_rewrite_count": "1",
    "new_citation_added_count": "0",
    "conditional_hold_count": "1",
}


PLANNED_DECISION_ROWS = [
    {
        "planned_decision_row_id": "SRDP-ROW-0001",
        "linked_readiness_audit_row_id": "SRAE-ROW-0001",
        "linked_planned_readiness_criterion_id": "SRCP-ROW-0001",
        "linked_package_audit_row_id": "FMRPA-ROW-0001",
        "linked_executed_package_revision_id": "FMRPE-ROW-0001",
        "linked_citation_record_id": "CIT-REC-0001",
        "linked_citation_key": "pmlr-v115-blom20a",
        "linked_candidate_entry_id": "CAND-0001",
        "decision_dimension": "conceptual-framing submission decision boundary",
        "planned_decision_check": "Decide later whether the bounded conceptual-framing pass can support a manuscript readiness decision without becoming proof, external validation, final paper status, or venue acceptance.",
        "decision_execution_status": "not_executed_plan_only",
        "planned_decision_outcome": "future_decision_required_not_ready_now",
        "manuscript_submission_ready": "no",
        "formal_mathematical_proof": "no",
        "independent_experiment": "no",
        "external_validation": "no",
        "new_citation_added": "no",
        "planning_reason": "A readiness criterion pass needs a separate decision layer before any readiness claim can be considered.",
    },
    {
        "planned_decision_row_id": "SRDP-ROW-0002",
        "linked_readiness_audit_row_id": "SRAE-ROW-0002",
        "linked_planned_readiness_criterion_id": "SRCP-ROW-0002",
        "linked_package_audit_row_id": "FMRPA-ROW-0002",
        "linked_executed_package_revision_id": "FMRPE-ROW-0002",
        "linked_citation_record_id": "CIT-REC-0002",
        "linked_citation_key": "pmlr-v124-wengel-mogensen20a",
        "linked_candidate_entry_id": "CAND-0002",
        "decision_dimension": "methodological-context submission decision boundary",
        "planned_decision_check": "Decide later whether the bounded methodological-context pass can support a manuscript readiness decision without becoming biological prediction, clinical relevance, laboratory guidance, operational readiness, or venue acceptance.",
        "decision_execution_status": "not_executed_plan_only",
        "planned_decision_outcome": "future_decision_required_not_ready_now",
        "manuscript_submission_ready": "no",
        "formal_mathematical_proof": "no",
        "independent_experiment": "no",
        "external_validation": "no",
        "new_citation_added": "no",
        "planning_reason": "A methodological-context readiness pass needs a separate decision layer before any readiness claim can be considered.",
    },
]


CONDITIONAL_HOLD_ROWS = [
    {
        "candidate_entry_id": "CAND-0003",
        "hold_status": "hold_for_update_before_retention_decision",
        "readiness_audit_row_id": "none",
        "planned_decision_row_id": "none",
        "decision_plan_status": "not_planned_no_readiness_audit_pass",
        "manuscript_submission_ready": "no",
        "formal_mathematical_proof": "no",
        "independent_experiment": "no",
        "external_validation": "no",
        "new_citation_added": "no",
        "reason": "Conditional metadata pass remains outside retained source, citation record audit, marker insertion, marker audit, claim revision execution, revised claim audit, package planning, package execution, package audit, readiness criteria planning, readiness audit execution, and decision planning.",
    },
]


DECISION_PLAN_FIELDS = [
    "planned_decision_row_id",
    "linked_readiness_audit_row_id",
    "linked_planned_readiness_criterion_id",
    "linked_package_audit_row_id",
    "linked_executed_package_revision_id",
    "linked_citation_record_id",
    "linked_citation_key",
    "linked_candidate_entry_id",
    "decision_dimension",
    "planned_decision_check",
    "decision_execution_status",
    "planned_decision_outcome",
    "manuscript_submission_ready",
    "formal_mathematical_proof",
    "independent_experiment",
    "external_validation",
    "new_citation_added",
    "planning_reason",
]


DECISION_PLAN_STATUS_VALUES = [
    "decision_plan_only_no_decision_execution",
    "not_executed_plan_only",
    "future_decision_required_not_ready_now",
    "not_planned_no_readiness_audit_pass",
    "manuscript_submission_ready_count_zero",
    "no_formal_mathematical_proof",
    "no_independent_experiment",
    "no_external_validation",
]


DECISION_PLAN_GATES = [
    "Submission readiness decision planning must be linked to v8.2 readiness audit execution.",
    "Only executed readiness audit pass rows may enter decision planning.",
    "Each decision row must link to a readiness audit row.",
    "Each decision row must link to a planned readiness criterion.",
    "Each decision row must link to a package audit row.",
    "Each decision row must link to an executed package revision.",
    "Each decision row must link to a citation record.",
    "Each decision row must link to a citation key.",
    "Each decision row must link to a candidate entry.",
    "Each decision row must define a decision dimension.",
    "Each decision row must remain plan-only.",
    "Submission readiness decision execution count must remain zero.",
    "Manuscript submission ready count must remain zero.",
    "Full manuscript rewrite count must remain one.",
    "New citation added count must remain zero.",
    "Formal mathematical proof count must remain zero.",
    "Independent experiment count must remain zero.",
    "External validation count must remain zero.",
    "Conditional-hold candidates must remain outside decision planning.",
    "Decision planning must not imply submission readiness.",
    "Decision planning must not imply external validation.",
    "Decision planning must not imply formal proof.",
    "Decision planning must not imply independent validation.",
    "Decision planning must not produce a final paper.",
]


BOUNDARY_PHRASES = [
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does plan manuscript submission readiness decision",
    "does not execute submission readiness decision",
    "does not make the manuscript submission-ready",
    "does not add new citations",
    "does not claim external validation",
    "does not claim formal mathematical proof",
    "does not claim independent experiment",
    "decision plan is not decision execution",
    "decision plan is not submission readiness",
    "decision plan is not external validation",
    "decision plan is not formal proof",
    "decision plan is not independent experiment",
    "decision plan is not final paper production",
    "readiness criterion pass is not submission approval",
    "readiness audit pass is not manuscript support",
    "audited package is not submission-ready manuscript",
    "citations are not external validation",
    "bounded context remains bounded",
    "manuscript submission ready count remains zero",
    "new citation added count remains zero",
    "conditional hold remains outside decision planning",
    "future submission readiness decision execution is separate",
    "venue acceptance remains unclaimed",
]


PROHIBITED_BEHAVIORS = [
    "Do not execute submission readiness decision in this milestone.",
    "Do not call the manuscript submission-ready.",
    "Do not add new citations in this milestone.",
    "Do not treat decision planning as readiness approval.",
    "Do not treat readiness audit pass as manuscript submission readiness.",
    "Do not treat decision planning as external validation.",
    "Do not treat decision planning as formal mathematical proof.",
    "Do not treat decision planning as independent experiment.",
    "Do not treat decision planning as final paper production.",
    "Do not imply acceptance by any venue.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not include conditional-hold candidates in decision rows.",
    "Do not claim accepted scientific theory.",
    "Do not upgrade validation language.",
    "Do not claim biological prediction or operational causal screening.",
]


NEXT_STEPS = [
    "Execute manuscript submission-readiness decision in a later milestone.",
    "Keep decision execution separate from decision planning.",
    "Keep formal mathematical proof separate from readiness decision work.",
    "Keep independent validation separate from readiness decision work.",
    "Keep new citation additions separate from decision planning.",
    "Keep CAND-0003 on hold until update handling.",
    "Maintain the research prototype with internal validation status.",
    "Avoid submission-ready language until a separate decision execution milestone passes.",
]


OVERCLAIM_PATTERNS = [
    r"\bproves\b",
    r"\bproven\b",
    r"\bestablishes\b",
    r"\bdefinitive\b",
    r"\buniversal theory\b",
    r"\bformal mathematical proof\b",
    r"\bindependent experiment\b",
    r"\bexternally validated\b",
    r"\bexternal validation\b",
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
    "plan",
    "planned",
    "decision",
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
    "manuscript",
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
    "not ready",
    "not proof",
    "not independent",
    "not external",
    "citations are not external validation",
    "still disallowed",
    "disallowed",
]


SAFE_SECTION_HEADINGS = [
    "boundary phrases",
    "prohibited behaviors",
    "manuscript submission readiness decision plan gates",
    "claim boundary toward v8.4",
    "final boundary statement",
    "submission readiness boundary",
    "decision planning boundary",
    "proof and validation boundary",
]


INVENTED_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
]


@dataclass(frozen=True)
class ManuscriptSubmissionReadinessDecisionPlanResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    submission_readiness_decision_plan_count: int
    executed_readiness_criterion_count: int
    planned_decision_row_count: int
    submission_readiness_decision_execution_count: int
    manuscript_submission_ready_count: int
    full_manuscript_rewrite_count: int
    new_citation_added_count: int
    conditional_hold_count: int
    decision_plan_field_count: int
    decision_plan_status_value_count: int
    decision_plan_gate_count: int
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
    rows = ["| Source artifact | Exists |", "|---|---|"]
    for path in SOURCE_ARTIFACTS:
        rows.append(f"| `{relative(path)}` | {path.exists()} |")
    return "\n".join(rows)


def render_metadata_table() -> str:
    rows = ["| Submission readiness decision plan field | Value |", "|---|---|"]
    for key, value in PLAN_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_decision_rows() -> str:
    rows = [
        "| Decision row | Readiness audit row | Planned criterion | Package audit row | Citation record | Citation key | Status |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in PLANNED_DECISION_ROWS:
        rows.append(
            f"| {item['planned_decision_row_id']} | "
            f"{item['linked_readiness_audit_row_id']} | "
            f"{item['linked_planned_readiness_criterion_id']} | "
            f"{item['linked_package_audit_row_id']} | "
            f"{item['linked_citation_record_id']} | "
            f"{item['linked_citation_key']} | "
            f"{item['decision_execution_status']} |"
        )
    return "\n".join(rows)


def render_decision_boundary_rows() -> str:
    rows = [
        "| Decision row | Dimension | Decision execution | Manuscript ready | Formal proof | Independent experiment | External validation | New citation added |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in PLANNED_DECISION_ROWS:
        rows.append(
            f"| {item['planned_decision_row_id']} | "
            f"{item['decision_dimension']} | "
            f"{item['decision_execution_status']} | "
            f"{item['manuscript_submission_ready']} | "
            f"{item['formal_mathematical_proof']} | "
            f"{item['independent_experiment']} | "
            f"{item['external_validation']} | "
            f"{item['new_citation_added']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Decision row | Decision plan status | Manuscript ready | Formal proof | Independent experiment | External validation | New citation added |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['planned_decision_row_id']} | "
            f"{item['decision_plan_status']} | "
            f"{item['manuscript_submission_ready']} | "
            f"{item['formal_mathematical_proof']} | "
            f"{item['independent_experiment']} | "
            f"{item['external_validation']} | "
            f"{item['new_citation_added']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = ["| Decision plan field | v8.3 status |", "|---|---|"]
    for field in DECISION_PLAN_FIELDS:
        rows.append(f"| `{field}` | populated for decision planning rows |")
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
        "submission readiness decision plan metadata",
        "planned decision rows",
        "decision boundary rows",
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
    return f"""# Manuscript Submission Readiness Decision Plan v8.3

## Question
Can Viruse Fabric plan a manuscript submission readiness decision layer from the v8.2 readiness audit while keeping decision execution, manuscript submission readiness, formal proof, independent experiment, external validation, and new citation additions at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does plan manuscript submission readiness decision. It does not execute submission readiness decision, does not make the manuscript submission-ready, does not add new citations, does not claim external validation, does not claim formal mathematical proof, and does not claim independent experiment.

Decision plan is not decision execution. Decision plan is not submission readiness. Decision plan is not external validation. Decision plan is not formal proof. Decision plan is not independent experiment. Decision plan is not final paper production. Readiness criterion pass is not submission approval. Readiness audit pass is not manuscript support. Audited package is not submission-ready manuscript. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Submission Readiness Decision Plan Metadata
{render_metadata_table()}

## Planned Decision Rows
{render_decision_rows()}

## Decision Boundary Rows
{render_decision_boundary_rows()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Decision Plan Fields
{render_field_table()}

## Decision Plan Status Values
{bullet_list(DECISION_PLAN_STATUS_VALUES)}

## Manuscript Submission Readiness Decision Plan Gates
{bullet_list(DECISION_PLAN_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Decision Plan Interpretation
The v8.3 artifact plans the first manuscript submission readiness decision layer from the v8.2 readiness audit execution.

SRDP-ROW-0001 plans a future decision check for the conceptual-framing readiness audit pass, linked to SRAE-ROW-0001, SRCP-ROW-0001, FMRPA-ROW-0001, FMRPE-ROW-0001, CIT-REC-0001, and CAND-0001.

SRDP-ROW-0002 plans a future decision check for the methodological-context readiness audit pass, linked to SRAE-ROW-0002, SRCP-ROW-0002, FMRPA-ROW-0002, FMRPE-ROW-0002, CIT-REC-0002, and CAND-0002.

These are decision plans only. They do not execute the decision, do not approve submission readiness, do not add citations, do not prove the theory, do not create an independent experiment, and do not create external validation.

## Decision Planning Boundary
Submission readiness decision plan count is one.

Executed readiness criterion count is two.

Planned decision row count is two.

Submission readiness decision execution count is zero.

Manuscript submission ready count remains zero.

Full manuscript rewrite count remains one.

New citation added count remains zero.

The project now has a planned decision layer, but it still has no submission-ready manuscript. A future decision box has been drawn on the map; civilization, naturally, will try to confuse the map with the destination. We will not.

## Submission Readiness Boundary
This milestone does not execute a submission readiness decision.

It does not certify the manuscript as ready for submission.

It does not create submission approval.

It does not certify the theory.

It does not produce a final paper.

It does not create peer review.

It does not certify acceptance by any venue.

## Proof and Validation Boundary
This milestone does not create formal mathematical proof.

It does not create independent experiment.

It does not create external validation.

It does not create biological validation.

It does not create clinical validation.

It does not create laboratory validation.

It does not create operational validation.

The project remains an internally audited research prototype.

## New Citation Boundary
New citation added count remains zero.

No new citation record is added. No new source is retained. No new bibliography entry is created. This milestone plans decision rows using existing readiness audit pass rows only.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside decision planning. It has no retained source record, no citation record, no audited citation record, no planned insertion slot, no inserted marker, no marker audit pass row, no planned claim revision, no executed claim revision, no bounded revised claim audit pass row, no package revision plan, no executed package revision, no package audit pass row, no readiness criterion plan row, no readiness audit pass row, and no decision plan row.

This prevents conditional metadata from strolling into a decision meeting wearing a fake badge and a tiny clipboard. Paperwork theater remains rejected.

## Claim Boundary Toward v8.4
This milestone permits a slightly stronger internal workflow claim than v8.2.

Allowed after v8.3:

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
- first manuscript submission readiness decision plan created
- manuscript still not submission-ready
- no readiness decision executed
- no formal mathematical proof
- no independent experiment
- no external validation
- no new citations added during decision planning

Still disallowed:

- proven theory
- formal mathematical proof
- independent experiment
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
Submission readiness decision plan count: 1

Executed readiness criterion count: 2

Planned decision row count: 2

Submission readiness decision execution count: 0

Manuscript submission ready count: 0

Full manuscript rewrite count: 1

New citation added count: 0

Conditional hold count: 1

## Final Boundary Statement
This artifact plans a manuscript submission readiness decision layer.

It does not execute the decision, does not make the manuscript ready for submission, does not add new citations, does not certify external validation, does not provide formal mathematical proof, does not provide independent experiment, does not produce a final paper, does not claim peer review or venue acceptance, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> ManuscriptSubmissionReadinessDecisionPlanResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    invented_citations = detect_invented_citation_like_patterns(report)

    submission_readiness_decision_plan_count = 1
    executed_readiness_criterion_count = int(PLAN_METADATA["executed_readiness_criterion_count_from_v8_2"])
    planned_decision_row_count = int(PLAN_METADATA["planned_decision_row_count"])
    submission_readiness_decision_execution_count = int(
        PLAN_METADATA["submission_readiness_decision_execution_count"]
    )
    manuscript_submission_ready_count = int(PLAN_METADATA["manuscript_submission_ready_count"])
    full_manuscript_rewrite_count = int(PLAN_METADATA["full_manuscript_rewrite_count"])
    new_citation_added_count = int(PLAN_METADATA["new_citation_added_count"])
    conditional_hold_count = int(PLAN_METADATA["conditional_hold_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 33:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if submission_readiness_decision_plan_count != 1:
        errors.append(
            "Submission readiness decision plan count should be one, got: "
            f"{submission_readiness_decision_plan_count}"
        )

    if executed_readiness_criterion_count != 2:
        errors.append(
            "Executed readiness criterion count should be two, got: "
            f"{executed_readiness_criterion_count}"
        )

    if planned_decision_row_count != 2:
        errors.append(f"Planned decision row count should be two, got: {planned_decision_row_count}")

    if executed_readiness_criterion_count != planned_decision_row_count:
        errors.append("Each executed readiness criterion should map to one decision plan row")

    if submission_readiness_decision_execution_count != 0:
        errors.append(
            "Submission readiness decision execution count should be zero, got: "
            f"{submission_readiness_decision_execution_count}"
        )

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

    for row in PLANNED_DECISION_ROWS:
        missing_fields = [field for field in DECISION_PLAN_FIELDS if not row.get(field)]
        if missing_fields:
            errors.append(
                f"{row.get('planned_decision_row_id', 'unknown')} missing decision plan fields: "
                f"{len(missing_fields)}"
            )

        if row.get("decision_execution_status") != "not_executed_plan_only":
            errors.append(
                f"{row.get('planned_decision_row_id', 'unknown')} has unexpected decision execution status"
            )

        if row.get("manuscript_submission_ready") != "no":
            errors.append(
                f"{row.get('planned_decision_row_id', 'unknown')} marked manuscript ready unexpectedly"
            )

        if row.get("formal_mathematical_proof") != "no":
            errors.append(
                f"{row.get('planned_decision_row_id', 'unknown')} claims formal proof unexpectedly"
            )

        if row.get("independent_experiment") != "no":
            errors.append(
                f"{row.get('planned_decision_row_id', 'unknown')} claims independent experiment unexpectedly"
            )

        if row.get("external_validation") != "no":
            errors.append(
                f"{row.get('planned_decision_row_id', 'unknown')} claims external validation unexpectedly"
            )

        if row.get("new_citation_added") != "no":
            errors.append(
                f"{row.get('planned_decision_row_id', 'unknown')} added citation unexpectedly"
            )

    if len(DECISION_PLAN_FIELDS) < 18:
        errors.append(f"Decision plan field count too low: {len(DECISION_PLAN_FIELDS)}")

    if len(DECISION_PLAN_STATUS_VALUES) < 8:
        errors.append(
            f"Decision plan status value count too low: {len(DECISION_PLAN_STATUS_VALUES)}"
        )

    if len(DECISION_PLAN_GATES) < 24:
        errors.append(f"Decision plan gate count too low: {len(DECISION_PLAN_GATES)}")

    if boundary_count < 27:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 15:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if invented_citations:
        errors.append(
            "Invented citation-like patterns detected outside decision plan sections: "
            f"{len(invented_citations)}"
        )

    if word_count < 1650:
        errors.append(
            f"Word count too low for manuscript submission readiness decision plan: {word_count}"
        )

    warnings.append("Decision layer is planned, but readiness decision is not executed.")
    warnings.append("No formal mathematical proof or independent experiment is created.")

    passed = not errors

    interpretation = (
        "The v8.3 artifact plans two manuscript submission readiness decision rows from "
        "executed readiness audit pass rows while keeping decision execution, manuscript "
        "submission readiness, formal proof, independent experiment, external validation, "
        "and new citation additions at zero."
    )

    return ManuscriptSubmissionReadinessDecisionPlanResult(
        title="Manuscript Submission Readiness Decision Plan v8.3",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        submission_readiness_decision_plan_count=submission_readiness_decision_plan_count,
        executed_readiness_criterion_count=executed_readiness_criterion_count,
        planned_decision_row_count=planned_decision_row_count,
        submission_readiness_decision_execution_count=submission_readiness_decision_execution_count,
        manuscript_submission_ready_count=manuscript_submission_ready_count,
        full_manuscript_rewrite_count=full_manuscript_rewrite_count,
        new_citation_added_count=new_citation_added_count,
        conditional_hold_count=conditional_hold_count,
        decision_plan_field_count=len(DECISION_PLAN_FIELDS),
        decision_plan_status_value_count=len(DECISION_PLAN_STATUS_VALUES),
        decision_plan_gate_count=len(DECISION_PLAN_GATES),
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

    print("Manuscript Submission Readiness Decision Plan v8.3")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(
        "Submission readiness decision plan count: "
        f"{result.submission_readiness_decision_plan_count}"
    )
    print(f"Executed readiness criterion count: {result.executed_readiness_criterion_count}")
    print(f"Planned decision row count: {result.planned_decision_row_count}")
    print(
        "Submission readiness decision execution count: "
        f"{result.submission_readiness_decision_execution_count}"
    )
    print(f"Manuscript submission ready count: {result.manuscript_submission_ready_count}")
    print(f"Full manuscript rewrite count: {result.full_manuscript_rewrite_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Decision plan field count: {result.decision_plan_field_count}")
    print(f"Decision plan status value count: {result.decision_plan_status_value_count}")
    print(f"Decision plan gate count: {result.decision_plan_gate_count}")
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
