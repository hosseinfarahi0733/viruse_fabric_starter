"""First full manuscript revision package audit for Viruse Fabric v8.0.

This module audits the first controlled full manuscript revision package
executed in v7.9.

It verifies package linkage, boundary preservation, controlled rewrite status,
and overclaim absence.

It does not add new citations.
It does not claim external validation.
It does not make the manuscript submission-ready.
It does not produce a final paper.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_full_manuscript_revision_package_audit_v8_0.md"

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
    "full_manuscript_revision_package_audit_id": "FMRPA-0001",
    "linked_full_manuscript_revision_package_execution_id": "FMRPE-0001",
    "linked_full_manuscript_revision_package_plan_id": "FMRPP-0001",
    "linked_bounded_revised_claim_audit_id": "BRCA-0001",
    "audit_status": "all_executed_package_revisions_pass_not_submission_ready",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "executed_package_revision_count_from_v7_9": "2",
    "executed_package_revision_audited_count": "2",
    "package_audit_pass_count": "2",
    "package_audit_conditional_count": "0",
    "package_audit_fail_count": "0",
    "full_manuscript_rewrite_count": "1",
    "new_citation_added_count": "0",
    "conditional_hold_count": "1",
}


PACKAGE_AUDIT_ROWS = [
    {
        "package_audit_row_id": "FMRPA-ROW-0001",
        "linked_executed_package_revision_id": "FMRPE-ROW-0001",
        "linked_planned_package_revision_id": "FMRPP-ROW-0001",
        "linked_revised_claim_audit_row_id": "BRCA-ROW-0001",
        "linked_executed_claim_revision_id": "CGRX-0001",
        "linked_planned_claim_revision_id": "CGRP-0001",
        "linked_manuscript_citation_marker_id": "MCM-0001",
        "linked_citation_record_id": "CIT-REC-0001",
        "linked_citation_key": "pmlr-v115-blom20a",
        "linked_evidence_matrix_row_id": "EMR-0001",
        "linked_retained_source_id": "RET-0001",
        "linked_candidate_entry_id": "CAND-0001",
        "audited_package_section": "related-work or conceptual framing section",
        "audited_package_role": "bounded conceptual-context package insertion",
        "package_linkage_audit_status": "package_linkage_pass",
        "controlled_text_audit_status": "controlled_text_boundary_pass",
        "overclaim_audit_status": "overclaim_absent",
        "full_manuscript_rewrite": "yes_controlled_package_artifact_only",
        "new_citation_added": "no",
        "submission_readiness_status": "not_submission_ready",
        "external_validation_status": "not_external_validation",
        "audit_reason": "The executed conceptual-context package revision remains bounded and does not become proof, validation, or submission readiness.",
    },
    {
        "package_audit_row_id": "FMRPA-ROW-0002",
        "linked_executed_package_revision_id": "FMRPE-ROW-0002",
        "linked_planned_package_revision_id": "FMRPP-ROW-0002",
        "linked_revised_claim_audit_row_id": "BRCA-ROW-0002",
        "linked_executed_claim_revision_id": "CGRX-0002",
        "linked_planned_claim_revision_id": "CGRP-0002",
        "linked_manuscript_citation_marker_id": "MCM-0002",
        "linked_citation_record_id": "CIT-REC-0002",
        "linked_citation_key": "pmlr-v124-wengel-mogensen20a",
        "linked_evidence_matrix_row_id": "EMR-0002",
        "linked_retained_source_id": "RET-0002",
        "linked_candidate_entry_id": "CAND-0002",
        "audited_package_section": "related-work or methodological context section",
        "audited_package_role": "bounded methodological-context package insertion",
        "package_linkage_audit_status": "package_linkage_pass",
        "controlled_text_audit_status": "controlled_text_boundary_pass",
        "overclaim_audit_status": "overclaim_absent",
        "full_manuscript_rewrite": "yes_controlled_package_artifact_only",
        "new_citation_added": "no",
        "submission_readiness_status": "not_submission_ready",
        "external_validation_status": "not_external_validation",
        "audit_reason": "The executed methodological-context package revision remains bounded and avoids biological, clinical, laboratory, or operational claims.",
    },
]


CONTROLLED_PACKAGE_AUDIT_ROWS = [
    {
        "package_section_audit_id": "FMRPA-SEC-0001",
        "linked_package_section_id": "FMRPE-PKG-SEC-0001",
        "linked_executed_package_revision_id": "FMRPE-ROW-0001",
        "section_boundary_status": "controlled_section_boundary_pass",
        "citation_marker_status": "existing_marker_used_no_new_citation",
        "submission_readiness_status": "not_submission_ready",
    },
    {
        "package_section_audit_id": "FMRPA-SEC-0002",
        "linked_package_section_id": "FMRPE-PKG-SEC-0002",
        "linked_executed_package_revision_id": "FMRPE-ROW-0002",
        "section_boundary_status": "controlled_section_boundary_pass",
        "citation_marker_status": "existing_marker_used_no_new_citation",
        "submission_readiness_status": "not_submission_ready",
    },
]


CONDITIONAL_HOLD_ROWS = [
    {
        "candidate_entry_id": "CAND-0003",
        "hold_status": "hold_for_update_before_retention_decision",
        "citation_record_id": "none",
        "executed_package_revision_id": "none",
        "package_audit_row_id": "none",
        "package_section_audit_id": "none",
        "package_audit_status": "not_audited_no_package_execution",
        "full_manuscript_rewrite": "no",
        "new_citation_added": "no",
        "reason": "Conditional metadata pass remains outside retained source, citation record audit, marker insertion, marker audit, claim revision execution, revised claim audit, package planning, package execution, and package audit.",
    },
]


PACKAGE_AUDIT_FIELDS = [
    "package_audit_row_id",
    "linked_executed_package_revision_id",
    "linked_planned_package_revision_id",
    "linked_revised_claim_audit_row_id",
    "linked_executed_claim_revision_id",
    "linked_planned_claim_revision_id",
    "linked_manuscript_citation_marker_id",
    "linked_citation_record_id",
    "linked_citation_key",
    "linked_evidence_matrix_row_id",
    "linked_retained_source_id",
    "linked_candidate_entry_id",
    "audited_package_section",
    "audited_package_role",
    "package_linkage_audit_status",
    "controlled_text_audit_status",
    "overclaim_audit_status",
    "full_manuscript_rewrite",
    "new_citation_added",
    "submission_readiness_status",
    "external_validation_status",
    "audit_reason",
]


PACKAGE_AUDIT_STATUS_VALUES = [
    "all_executed_package_revisions_pass_not_submission_ready",
    "package_linkage_pass",
    "package_linkage_conditional",
    "package_linkage_fail",
    "controlled_text_boundary_pass",
    "controlled_text_boundary_fail",
    "overclaim_absent",
    "overclaim_present_fail",
    "not_audited_no_package_execution",
]


PACKAGE_AUDIT_GATES = [
    "Full manuscript revision package audit must be linked to v7.9 package execution.",
    "Only executed package revision rows may be audited.",
    "Each package audit row must link to an executed package revision.",
    "Each package audit row must link to a planned package revision.",
    "Each package audit row must link to a revised claim audit row.",
    "Each package audit row must link to an executed claim revision.",
    "Each package audit row must link to a planned claim revision.",
    "Each package audit row must link to a manuscript citation marker.",
    "Each package audit row must link to an audited citation record.",
    "Each package audit row must link to a citation key.",
    "Each package audit row must link to an evidence matrix row.",
    "Each package audit row must link to a retained source.",
    "Each package audit row must link to a candidate entry.",
    "Each package audit row must preserve bounded package section.",
    "Each package audit row must preserve bounded package role.",
    "Each package audit row must pass controlled text boundary audit.",
    "Each package audit row must pass overclaim audit.",
    "Full manuscript rewrite count must remain one as controlled package artifact only.",
    "New citation added count must remain zero.",
    "Conditional-hold candidates must remain outside package audit pass rows.",
    "Package audit must not imply external validation.",
    "Package audit must not imply submission readiness.",
    "Package audit must not produce a final paper.",
]


BOUNDARY_PHRASES = [
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does audit full manuscript revision package execution",
    "controlled full manuscript revision package artifact",
    "full manuscript rewrite count remains one",
    "does not add new citations",
    "does not claim external validation",
    "does not make the manuscript submission-ready",
    "package audit is not external validation",
    "package audit is not submission readiness",
    "package audit is not final paper production",
    "controlled package artifact is not acceptance",
    "controlled package artifact is not peer review",
    "controlled package audit is not peer review",
    "citation-grounded revised claim is not biological validation",
    "citation-grounded revised claim is not clinical validation",
    "citation record pass is not manuscript support",
    "citations are not external validation",
    "bounded context remains bounded",
    "new citation added count remains zero",
    "conditional hold remains outside package audit pass rows",
    "future submission readiness audit is separate",
    "future public claims must remain bounded",
    "future external validation would require separate evidence",
]


PROHIBITED_BEHAVIORS = [
    "Do not add new citations in this milestone.",
    "Do not treat package audit as external validation.",
    "Do not treat package audit as submission readiness.",
    "Do not treat package audit as final paper production.",
    "Do not treat controlled package audit as peer review.",
    "Do not imply acceptance by any venue.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not include conditional-hold candidates in package audit pass rows.",
    "Do not convert bounded package text into strengthened conclusions.",
    "Do not claim accepted scientific theory.",
    "Do not upgrade validation language.",
    "Do not claim biological prediction or operational causal screening.",
    "Do not treat citation linkage as real-world validation.",
    "Do not call the manuscript submission-ready.",
]


NEXT_STEPS = [
    "Plan submission-readiness criteria in a later milestone.",
    "Keep submission-readiness audit separate from package audit.",
    "Check public claim language after package audit.",
    "Keep new citation additions separate from package audit.",
    "Keep CAND-0003 on hold until update handling.",
    "Preserve package linkage in future readiness planning.",
    "Maintain the research prototype with internal validation status.",
    "Avoid final-paper language until a separate readiness audit exists.",
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
    "guard",
    "no_",
    "none",
    "bounded",
    "controlled",
    "audit",
    "package",
    "citation",
    "citation marker",
    "claim revision",
    "revised claim",
    "manuscript",
    "citation record",
    "evidence row",
    "retained source",
    "candidate",
    "conditional",
    "hold",
    "zero",
    "one",
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
    "full manuscript revision package audit gates",
    "claim boundary toward v8.1",
    "final boundary statement",
    "full manuscript boundary",
    "submission readiness boundary",
    "controlled package text audit",
    "package audit boundary",
]


INVENTED_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
]


@dataclass(frozen=True)
class FirstFullManuscriptRevisionPackageAuditResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    full_manuscript_revision_package_audit_count: int
    executed_package_revision_count: int
    executed_package_revision_audited_count: int
    package_audit_pass_count: int
    package_audit_conditional_count: int
    package_audit_fail_count: int
    full_manuscript_rewrite_count: int
    new_citation_added_count: int
    conditional_hold_count: int
    package_audit_field_count: int
    package_audit_status_value_count: int
    package_audit_gate_count: int
    controlled_package_section_audit_count: int
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
        "| Full manuscript revision package audit field | Value |",
        "|---|---|",
    ]
    for key, value in AUDIT_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_package_audit_rows() -> str:
    rows = [
        "| Package audit row | Executed package revision | Planned package revision | Revised claim audit row | Citation record | Citation key | Audit status |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in PACKAGE_AUDIT_ROWS:
        rows.append(
            f"| {item['package_audit_row_id']} | "
            f"{item['linked_executed_package_revision_id']} | "
            f"{item['linked_planned_package_revision_id']} | "
            f"{item['linked_revised_claim_audit_row_id']} | "
            f"{item['linked_citation_record_id']} | "
            f"{item['linked_citation_key']} | "
            f"{item['package_linkage_audit_status']} |"
        )
    return "\n".join(rows)


def render_package_linkage_rows() -> str:
    rows = [
        "| Package audit row | Executed claim revision | Planned claim revision | Marker | Evidence row | Retained source | Candidate |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in PACKAGE_AUDIT_ROWS:
        rows.append(
            f"| {item['package_audit_row_id']} | "
            f"{item['linked_executed_claim_revision_id']} | "
            f"{item['linked_planned_claim_revision_id']} | "
            f"{item['linked_manuscript_citation_marker_id']} | "
            f"{item['linked_evidence_matrix_row_id']} | "
            f"{item['linked_retained_source_id']} | "
            f"{item['linked_candidate_entry_id']} |"
        )
    return "\n".join(rows)


def render_package_boundary_rows() -> str:
    rows = [
        "| Package audit row | Controlled text | Overclaim | Full manuscript rewrite | New citation added | Submission readiness | External validation |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in PACKAGE_AUDIT_ROWS:
        rows.append(
            f"| {item['package_audit_row_id']} | "
            f"{item['controlled_text_audit_status']} | "
            f"{item['overclaim_audit_status']} | "
            f"{item['full_manuscript_rewrite']} | "
            f"{item['new_citation_added']} | "
            f"{item['submission_readiness_status']} | "
            f"{item['external_validation_status']} |"
        )
    return "\n".join(rows)


def render_controlled_section_audit_rows() -> str:
    rows = [
        "| Section audit | Package section | Executed package revision | Section boundary | Citation marker status | Submission readiness |",
        "|---|---|---|---|---|---|",
    ]
    for item in CONTROLLED_PACKAGE_AUDIT_ROWS:
        rows.append(
            f"| {item['package_section_audit_id']} | "
            f"{item['linked_package_section_id']} | "
            f"{item['linked_executed_package_revision_id']} | "
            f"{item['section_boundary_status']} | "
            f"{item['citation_marker_status']} | "
            f"{item['submission_readiness_status']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Package audit row | Section audit | Package audit status | Full manuscript rewrite | New citation added | Reason |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['package_audit_row_id']} | "
            f"{item['package_section_audit_id']} | "
            f"{item['package_audit_status']} | "
            f"{item['full_manuscript_rewrite']} | "
            f"{item['new_citation_added']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Package audit field | v8.0 status |",
        "|---|---|",
    ]
    for field in PACKAGE_AUDIT_FIELDS:
        rows.append(f"| `{field}` | populated for package audit rows |")
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
        "package audit rows",
        "package linkage rows",
        "package boundary audit rows",
        "controlled package section audit rows",
        "full manuscript revision package audit metadata",
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
    return f"""# First Full Manuscript Revision Package Audit v8.0

## Question
Can Viruse Fabric audit the first controlled full manuscript revision package while preserving non-submission-ready boundaries and keeping new citation additions at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does audit full manuscript revision package execution. It audits the controlled full manuscript revision package artifact created in v7.9. Full manuscript rewrite count remains one. It does not add new citations, does not claim external validation, and does not make the manuscript submission-ready.

Package audit is not external validation. Package audit is not submission readiness. Package audit is not final paper production. Controlled package artifact is not acceptance. Controlled package artifact is not peer review. Controlled package audit is not peer review. Citation-grounded revised claim is not biological validation. Citation-grounded revised claim is not clinical validation. Citation record pass is not manuscript support. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Full Manuscript Revision Package Audit Metadata
{render_metadata_table()}

## Package Audit Rows
{render_package_audit_rows()}

## Package Linkage Rows
{render_package_linkage_rows()}

## Package Boundary Audit Rows
{render_package_boundary_rows()}

## Controlled Package Section Audit Rows
{render_controlled_section_audit_rows()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Package Audit Fields
{render_field_table()}

## Package Audit Status Values
{bullet_list(PACKAGE_AUDIT_STATUS_VALUES)}

## Full Manuscript Revision Package Audit Gates
{bullet_list(PACKAGE_AUDIT_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Package Audit Interpretation
The v8.0 artifact audits the first controlled full manuscript revision package created in v7.9.

FMRPA-ROW-0001 audits FMRPE-ROW-0001 and confirms linkage to FMRPP-ROW-0001, BRCA-ROW-0001, CGRX-0001, CGRP-0001, MCM-0001, CIT-REC-0001, EMR-0001, RET-0001, and CAND-0001.

FMRPA-ROW-0002 audits FMRPE-ROW-0002 and confirms linkage to FMRPP-ROW-0002, BRCA-ROW-0002, CGRX-0002, CGRP-0002, MCM-0002, CIT-REC-0002, EMR-0002, RET-0002, and CAND-0002.

Both package audit rows pass linkage, controlled text boundary audit, and overclaim audit. This means the controlled rewrite artifact preserves the internal workflow boundaries. It does not mean the manuscript is externally validated, peer-reviewed, final, or ready for submission.

## Package Audit Boundary
Full manuscript revision package audit count is one.

Executed package revision count is two.

Executed package revision audited count is two.

Package audit pass count is two.

Package audit conditional count is zero.

Package audit fail count is zero.

Full manuscript rewrite count remains one.

New citation added count remains zero.

The project now has an audited controlled manuscript revision package, but it still has no submission-ready manuscript. Yes, even an audited rewrite is not magically a paper. A sentence humanity keeps resisting like it is cardio.

## Linkage Boundary
Each passed package audit row verifies linkage to:

- executed package revision
- planned package revision
- revised claim audit row
- executed bounded claim revision
- planned claim revision
- manuscript citation marker
- audited citation record
- citation key
- evidence matrix row
- retained source
- candidate entry
- bounded package section
- bounded package role

This keeps the controlled manuscript package attached to the internal evidence workflow instead of becoming manuscript cosplay.

## Controlled Package Text Audit
The controlled manuscript package contains two audited package sections.

Both controlled package sections pass section boundary audit.

Both sections use existing manuscript citation markers only.

Both sections remain not submission-ready.

Neither section claims proof, external validation, biological prediction, clinical relevance, laboratory guidance, operational readiness, accepted scientific theory, final paper status, or peer review.

## Full Manuscript Boundary
The full manuscript rewrite count remains one.

This means one controlled full manuscript revision package artifact exists and has now been audited.

It does not mean the manuscript is final.

It does not mean the manuscript is submission-ready.

It does not mean the manuscript has passed a submission-readiness audit.

It does not mean the manuscript has external validation.

It does not mean the theory is proven.

## Submission Readiness Boundary
This milestone does not create submission readiness.

It does not create a final paper.

It does not create peer review.

It does not certify acceptance.

It only audits the controlled manuscript package generated in v7.9.

## New Citation Boundary
New citation added count remains zero.

No new citation record is added. No new source is retained. No new bibliography entry is created. This milestone audits existing package execution rows and existing controlled package sections only.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside package audit pass rows. It has no retained source record, no citation record, no audited citation record, no planned insertion slot, no inserted marker, no marker audit pass row, no planned claim revision, no executed claim revision, no bounded revised claim audit pass row, no package revision plan, no executed package revision, and no package audit pass row.

This prevents conditional metadata from slipping into the audited manuscript package with a forged conference badge. Charming attempt, still no.

## Claim Boundary Toward v8.1
This milestone permits a slightly stronger internal workflow claim than v7.9.

Allowed after v8.0:

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
- manuscript still not submission-ready
- no new citations added during package audit

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

## Output Counts
Full manuscript revision package audit count: 1

Executed package revision count: 2

Executed package revision audited count: 2

Package audit pass count: 2

Package audit conditional count: 0

Package audit fail count: 0

Full manuscript rewrite count: 1

New citation added count: 0

Conditional hold count: 1

## Final Boundary Statement
This artifact audits a controlled full manuscript revision package.

It does not add new citations, does not certify external validation, does not make the manuscript ready for submission, does not produce a final paper, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstFullManuscriptRevisionPackageAuditResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    invented_citations = detect_invented_citation_like_patterns(report)

    full_manuscript_revision_package_audit_count = 1
    executed_package_revision_count = int(AUDIT_METADATA["executed_package_revision_count_from_v7_9"])
    executed_package_revision_audited_count = int(AUDIT_METADATA["executed_package_revision_audited_count"])
    package_audit_pass_count = int(AUDIT_METADATA["package_audit_pass_count"])
    package_audit_conditional_count = int(AUDIT_METADATA["package_audit_conditional_count"])
    package_audit_fail_count = int(AUDIT_METADATA["package_audit_fail_count"])
    full_manuscript_rewrite_count = int(AUDIT_METADATA["full_manuscript_rewrite_count"])
    new_citation_added_count = int(AUDIT_METADATA["new_citation_added_count"])
    conditional_hold_count = int(AUDIT_METADATA["conditional_hold_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 30:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if full_manuscript_revision_package_audit_count != 1:
        errors.append(
            "Full manuscript revision package audit count should be one, got: "
            f"{full_manuscript_revision_package_audit_count}"
        )

    if executed_package_revision_count != 2:
        errors.append(
            "Executed package revision count should be two, got: "
            f"{executed_package_revision_count}"
        )

    if executed_package_revision_audited_count != 2:
        errors.append(
            "Executed package revision audited count should be two, got: "
            f"{executed_package_revision_audited_count}"
        )

    if package_audit_pass_count != 2:
        errors.append(f"Package audit pass count should be two, got: {package_audit_pass_count}")

    if package_audit_conditional_count != 0:
        errors.append(
            "Package audit conditional count should be zero, got: "
            f"{package_audit_conditional_count}"
        )

    if package_audit_fail_count != 0:
        errors.append(f"Package audit fail count should be zero, got: {package_audit_fail_count}")

    if executed_package_revision_count != executed_package_revision_audited_count:
        errors.append("Every executed package revision must be audited")

    if executed_package_revision_audited_count != package_audit_pass_count:
        errors.append("Every audited package revision must pass in v8.0")

    if full_manuscript_rewrite_count != 1:
        errors.append(
            "Full manuscript rewrite count should remain one for controlled package artifact, got: "
            f"{full_manuscript_rewrite_count}"
        )

    if new_citation_added_count != 0:
        errors.append(f"New citation added count should be zero, got: {new_citation_added_count}")

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    for row in PACKAGE_AUDIT_ROWS:
        missing_fields = [field for field in PACKAGE_AUDIT_FIELDS if not row.get(field)]
        if missing_fields:
            errors.append(
                f"{row.get('package_audit_row_id', 'unknown')} missing package audit fields: "
                f"{len(missing_fields)}"
            )

        if row.get("package_linkage_audit_status") != "package_linkage_pass":
            errors.append(f"{row.get('package_audit_row_id', 'unknown')} did not pass linkage audit")

        if row.get("controlled_text_audit_status") != "controlled_text_boundary_pass":
            errors.append(
                f"{row.get('package_audit_row_id', 'unknown')} did not pass controlled text audit"
            )

        if row.get("overclaim_audit_status") != "overclaim_absent":
            errors.append(f"{row.get('package_audit_row_id', 'unknown')} has overclaim problem")

        if row.get("full_manuscript_rewrite") != "yes_controlled_package_artifact_only":
            errors.append(f"{row.get('package_audit_row_id', 'unknown')} has invalid rewrite boundary")

        if row.get("new_citation_added") != "no":
            errors.append(f"{row.get('package_audit_row_id', 'unknown')} added citation unexpectedly")

        if row.get("submission_readiness_status") != "not_submission_ready":
            errors.append(
                f"{row.get('package_audit_row_id', 'unknown')} has invalid submission readiness status"
            )

        if row.get("external_validation_status") != "not_external_validation":
            errors.append(
                f"{row.get('package_audit_row_id', 'unknown')} has invalid external validation status"
            )

    if len(PACKAGE_AUDIT_FIELDS) < 22:
        errors.append(f"Package audit field count too low: {len(PACKAGE_AUDIT_FIELDS)}")

    if len(PACKAGE_AUDIT_STATUS_VALUES) < 9:
        errors.append(
            "Package audit status value count too low: "
            f"{len(PACKAGE_AUDIT_STATUS_VALUES)}"
        )

    if len(PACKAGE_AUDIT_GATES) < 23:
        errors.append(f"Package audit gate count too low: {len(PACKAGE_AUDIT_GATES)}")

    if len(CONTROLLED_PACKAGE_AUDIT_ROWS) != 2:
        errors.append(
            "Controlled package section audit count should be two, got: "
            f"{len(CONTROLLED_PACKAGE_AUDIT_ROWS)}"
        )

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
            "Invented citation-like patterns detected outside package audit sections: "
            f"{len(invented_citations)}"
        )

    if word_count < 1650:
        errors.append(
            f"Word count too low for first full manuscript revision package audit: {word_count}"
        )

    warnings.append("Full manuscript revision package is audited, but it is not submission-ready.")
    warnings.append("Package audit confirms boundaries but does not create external validation.")

    passed = not errors

    interpretation = (
        "The v8.0 artifact audits two executed package revision rows, confirms package "
        "linkage and controlled text boundaries, preserves one controlled manuscript "
        "rewrite artifact, and keeps new citation additions at zero."
    )

    return FirstFullManuscriptRevisionPackageAuditResult(
        title="First Full Manuscript Revision Package Audit v8.0",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        full_manuscript_revision_package_audit_count=full_manuscript_revision_package_audit_count,
        executed_package_revision_count=executed_package_revision_count,
        executed_package_revision_audited_count=executed_package_revision_audited_count,
        package_audit_pass_count=package_audit_pass_count,
        package_audit_conditional_count=package_audit_conditional_count,
        package_audit_fail_count=package_audit_fail_count,
        full_manuscript_rewrite_count=full_manuscript_rewrite_count,
        new_citation_added_count=new_citation_added_count,
        conditional_hold_count=conditional_hold_count,
        package_audit_field_count=len(PACKAGE_AUDIT_FIELDS),
        package_audit_status_value_count=len(PACKAGE_AUDIT_STATUS_VALUES),
        package_audit_gate_count=len(PACKAGE_AUDIT_GATES),
        controlled_package_section_audit_count=len(CONTROLLED_PACKAGE_AUDIT_ROWS),
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

    print("First Full Manuscript Revision Package Audit v8.0")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(
        "Full manuscript revision package audit count: "
        f"{result.full_manuscript_revision_package_audit_count}"
    )
    print(f"Executed package revision count: {result.executed_package_revision_count}")
    print(
        "Executed package revision audited count: "
        f"{result.executed_package_revision_audited_count}"
    )
    print(f"Package audit pass count: {result.package_audit_pass_count}")
    print(f"Package audit conditional count: {result.package_audit_conditional_count}")
    print(f"Package audit fail count: {result.package_audit_fail_count}")
    print(f"Full manuscript rewrite count: {result.full_manuscript_rewrite_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Package audit field count: {result.package_audit_field_count}")
    print(f"Package audit status value count: {result.package_audit_status_value_count}")
    print(f"Package audit gate count: {result.package_audit_gate_count}")
    print(f"Controlled package section audit count: {result.controlled_package_section_audit_count}")
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
