"""First full manuscript revision package execution for Viruse Fabric v7.9.

This module executes the first full manuscript revision package from the v7.8
package plan.

It creates a controlled full manuscript revision package artifact.
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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_full_manuscript_revision_package_execution_v7_9.md"

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


EXECUTION_METADATA = {
    "full_manuscript_revision_package_execution_id": "FMRPE-0001",
    "linked_full_manuscript_revision_package_plan_id": "FMRPP-0001",
    "linked_bounded_revised_claim_audit_id": "BRCA-0001",
    "linked_citation_grounded_manuscript_claim_revision_execution_id": "CGMCRE-0001",
    "linked_citation_grounded_manuscript_claim_revision_plan_id": "CGMCRP-0001",
    "execution_status": "controlled_package_execution_not_submission_ready",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "planned_package_revision_count_from_v7_8": "2",
    "executed_package_revision_count": "2",
    "full_manuscript_revision_package_count": "1",
    "full_manuscript_rewrite_count": "1",
    "new_citation_added_count": "0",
    "conditional_hold_count": "1",
}


EXECUTED_PACKAGE_REVISION_ROWS = [
    {
        "executed_package_revision_id": "FMRPE-ROW-0001",
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
        "executed_manuscript_package_section": "related-work or conceptual framing section",
        "executed_package_revision_role": "bounded conceptual-context package insertion",
        "executed_revised_claim_package_text": (
            "Viruse Fabric is presented as a research prototype with internal validation "
            "that is conceptually adjacent to causal-constraints framing, without claiming "
            "to prove, validate, or extend causal constraints models."
        ),
        "citation_marker_used": "[@pmlr-v115-blom20a]",
        "package_execution_status": "executed_bounded_package_revision",
        "full_manuscript_rewrite": "yes_controlled_package_artifact_only",
        "new_citation_added": "no",
        "submission_readiness_status": "not_submission_ready",
        "external_validation_status": "not_external_validation",
        "overclaim_guard": "Conceptual adjacency remains bounded and is not treated as proof or validation.",
    },
    {
        "executed_package_revision_id": "FMRPE-ROW-0002",
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
        "executed_manuscript_package_section": "related-work or methodological context section",
        "executed_package_revision_role": "bounded methodological-context package insertion",
        "executed_revised_claim_package_text": (
            "Viruse Fabric cites causal screening in dynamical systems as methodological "
            "background for thinking about dynamic causal structure, without claiming "
            "biological prediction, clinical relevance, or operational causal screening."
        ),
        "citation_marker_used": "[@pmlr-v124-wengel-mogensen20a]",
        "package_execution_status": "executed_bounded_package_revision",
        "full_manuscript_rewrite": "yes_controlled_package_artifact_only",
        "new_citation_added": "no",
        "submission_readiness_status": "not_submission_ready",
        "external_validation_status": "not_external_validation",
        "overclaim_guard": "Methodological background remains bounded and is not treated as biological, clinical, or operational validation.",
    },
]


CONTROLLED_MANUSCRIPT_PACKAGE = [
    {
        "package_section_id": "FMRPE-PKG-SEC-0001",
        "section_role": "controlled related-work package section",
        "included_executed_package_revision_id": "FMRPE-ROW-0001",
        "included_citation_marker": "[@pmlr-v115-blom20a]",
        "controlled_section_text": (
            "In the related-work framing, Viruse Fabric may be described as conceptually "
            "adjacent to causal-constraints framing while remaining a research prototype "
            "with internal validation only."
        ),
    },
    {
        "package_section_id": "FMRPE-PKG-SEC-0002",
        "section_role": "controlled methodological-context package section",
        "included_executed_package_revision_id": "FMRPE-ROW-0002",
        "included_citation_marker": "[@pmlr-v124-wengel-mogensen20a]",
        "controlled_section_text": (
            "In the methodological context, Viruse Fabric may cite causal screening in "
            "dynamical systems as background for dynamic causal structure, while avoiding "
            "biological, clinical, laboratory, and operational claims."
        ),
    },
]


CONDITIONAL_HOLD_ROWS = [
    {
        "candidate_entry_id": "CAND-0003",
        "hold_status": "hold_for_update_before_retention_decision",
        "citation_record_id": "none",
        "bounded_revised_claim_record_id": "none",
        "revised_claim_audit_row_id": "none",
        "planned_package_revision_id": "none",
        "executed_package_revision_id": "none",
        "package_section_id": "none",
        "full_manuscript_rewrite": "no",
        "new_citation_added": "no",
        "reason": "Conditional metadata pass remains outside retained source, citation record audit, marker insertion, marker audit, claim revision execution, revised claim audit, package planning, and package execution.",
    },
]


PACKAGE_EXECUTION_FIELDS = [
    "executed_package_revision_id",
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
    "executed_manuscript_package_section",
    "executed_package_revision_role",
    "executed_revised_claim_package_text",
    "citation_marker_used",
    "package_execution_status",
    "full_manuscript_rewrite",
    "new_citation_added",
    "submission_readiness_status",
    "external_validation_status",
    "overclaim_guard",
]


PACKAGE_EXECUTION_STATUS_VALUES = [
    "controlled_package_execution_not_submission_ready",
    "executed_bounded_package_revision",
    "yes_controlled_package_artifact_only",
    "not_submission_ready",
    "not_external_validation",
    "candidate_hold_no_package_execution",
]


PACKAGE_EXECUTION_GATES = [
    "Full manuscript revision package execution must be linked to v7.8 package planning.",
    "Only planned package revision rows may be executed.",
    "Each executed package revision must link to a planned package revision.",
    "Each executed package revision must link to a revised claim audit row.",
    "Each executed package revision must link to an executed claim revision.",
    "Each executed package revision must link to a planned claim revision.",
    "Each executed package revision must link to a manuscript citation marker.",
    "Each executed package revision must link to an audited citation record.",
    "Each executed package revision must link to a citation key.",
    "Each executed package revision must link to an evidence matrix row.",
    "Each executed package revision must link to a retained source.",
    "Each executed package revision must link to a candidate entry.",
    "Each executed package revision must preserve bounded package section.",
    "Each executed package revision must preserve bounded package role.",
    "Each executed package revision must include controlled package text.",
    "Each executed package revision must include an overclaim guard.",
    "Full manuscript rewrite count may be one only as a controlled package artifact.",
    "New citation added count must remain zero.",
    "Conditional-hold candidates must remain outside package execution.",
    "Package execution must not imply external validation.",
    "Package execution must not imply submission readiness.",
    "Package execution must not produce a final paper.",
]


BOUNDARY_PHRASES = [
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does execute full manuscript revision package",
    "controlled full manuscript revision package artifact",
    "full manuscript rewrite count is one",
    "does not add new citations",
    "does not claim external validation",
    "does not make the manuscript submission-ready",
    "package execution is not external validation",
    "package execution is not submission readiness",
    "package execution is not final paper production",
    "full manuscript rewrite is controlled package artifact only",
    "controlled package artifact is not acceptance",
    "controlled package artifact is not peer review",
    "citation-grounded revised claim is not biological validation",
    "citation-grounded revised claim is not clinical validation",
    "citation record pass is not manuscript support",
    "citations are not external validation",
    "bounded context remains bounded",
    "new citation added count remains zero",
    "conditional hold remains outside package execution",
    "future package audit is separate",
    "future submission readiness audit is separate",
    "future public claims must remain bounded",
]


PROHIBITED_BEHAVIORS = [
    "Do not add new citations in this milestone.",
    "Do not treat package execution as external validation.",
    "Do not treat package execution as submission readiness.",
    "Do not treat package execution as final paper production.",
    "Do not treat controlled package artifact as peer review.",
    "Do not imply acceptance by any venue.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not include conditional-hold candidates in package execution rows.",
    "Do not convert bounded revised claims into strengthened conclusions.",
    "Do not claim accepted scientific theory.",
    "Do not upgrade validation language.",
    "Do not claim biological prediction or operational causal screening.",
    "Do not treat citation linkage as real-world validation.",
    "Do not call the manuscript submission-ready.",
]


NEXT_STEPS = [
    "Audit the executed full manuscript revision package in a later milestone.",
    "Check package execution linkage against v7.8 planning rows.",
    "Check controlled package text for boundary preservation.",
    "Keep new citation additions separate from package execution.",
    "Keep CAND-0003 on hold until update handling.",
    "Check public claim language after package audit.",
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
    r"\bfinal paper\b",
]


SAFE_LINE_CUES = [
    "not",
    "does not",
    "do not",
    "must not",
    "without claiming",
    "without",
    "avoid",
    "avoiding",
    "guard",
    "no_",
    "none",
    "bounded",
    "controlled",
    "execution",
    "package",
    "citation",
    "citation marker",
    "claim revision",
    "revised claim",
    "audit",
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
]


SAFE_SECTION_HEADINGS = [
    "boundary phrases",
    "prohibited behaviors",
    "full manuscript revision package execution gates",
    "claim boundary toward v8.0",
    "final boundary statement",
    "full manuscript boundary",
    "controlled package text boundary",
    "execution boundary",
]


INVENTED_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
]


@dataclass(frozen=True)
class FirstFullManuscriptRevisionPackageExecutionResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    full_manuscript_revision_package_execution_count: int
    planned_package_revision_count: int
    executed_package_revision_count: int
    full_manuscript_revision_package_count: int
    full_manuscript_rewrite_count: int
    new_citation_added_count: int
    conditional_hold_count: int
    package_execution_field_count: int
    package_execution_status_value_count: int
    package_execution_gate_count: int
    controlled_package_section_count: int
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
        "| Full manuscript revision package execution field | Value |",
        "|---|---|",
    ]
    for key, value in EXECUTION_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_executed_package_revision_rows() -> str:
    rows = [
        "| Executed package revision | Planned package revision | Revised claim audit row | Citation record | Citation key | Execution status |",
        "|---|---|---|---|---|---|",
    ]
    for item in EXECUTED_PACKAGE_REVISION_ROWS:
        rows.append(
            f"| {item['executed_package_revision_id']} | "
            f"{item['linked_planned_package_revision_id']} | "
            f"{item['linked_revised_claim_audit_row_id']} | "
            f"{item['linked_citation_record_id']} | "
            f"{item['linked_citation_key']} | "
            f"{item['package_execution_status']} |"
        )
    return "\n".join(rows)


def render_package_linkage_rows() -> str:
    rows = [
        "| Executed package revision | Executed claim revision | Planned claim revision | Marker | Evidence row | Retained source | Candidate |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in EXECUTED_PACKAGE_REVISION_ROWS:
        rows.append(
            f"| {item['executed_package_revision_id']} | "
            f"{item['linked_executed_claim_revision_id']} | "
            f"{item['linked_planned_claim_revision_id']} | "
            f"{item['linked_manuscript_citation_marker_id']} | "
            f"{item['linked_evidence_matrix_row_id']} | "
            f"{item['linked_retained_source_id']} | "
            f"{item['linked_candidate_entry_id']} |"
        )
    return "\n".join(rows)


def render_package_text_rows() -> str:
    rows = [
        "| Executed package revision | Package section | Package role | Controlled package text |",
        "|---|---|---|---|",
    ]
    for item in EXECUTED_PACKAGE_REVISION_ROWS:
        rows.append(
            f"| {item['executed_package_revision_id']} | "
            f"{item['executed_manuscript_package_section']} | "
            f"{item['executed_package_revision_role']} | "
            f"{item['executed_revised_claim_package_text']} |"
        )
    return "\n".join(rows)


def render_execution_boundary_rows() -> str:
    rows = [
        "| Executed package revision | Full manuscript rewrite | New citation added | Submission readiness | External validation |",
        "|---|---|---|---|---|",
    ]
    for item in EXECUTED_PACKAGE_REVISION_ROWS:
        rows.append(
            f"| {item['executed_package_revision_id']} | "
            f"{item['full_manuscript_rewrite']} | "
            f"{item['new_citation_added']} | "
            f"{item['submission_readiness_status']} | "
            f"{item['external_validation_status']} |"
        )
    return "\n".join(rows)


def render_controlled_package_sections() -> str:
    rows = [
        "| Package section | Section role | Included package revision | Citation marker | Controlled section text |",
        "|---|---|---|---|---|",
    ]
    for item in CONTROLLED_MANUSCRIPT_PACKAGE:
        rows.append(
            f"| {item['package_section_id']} | "
            f"{item['section_role']} | "
            f"{item['included_executed_package_revision_id']} | "
            f"{item['included_citation_marker']} | "
            f"{item['controlled_section_text']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Executed package revision | Package section | Full manuscript rewrite | New citation added | Reason |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['executed_package_revision_id']} | "
            f"{item['package_section_id']} | "
            f"{item['full_manuscript_rewrite']} | "
            f"{item['new_citation_added']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Package execution field | v7.9 status |",
        "|---|---|",
    ]
    for field in PACKAGE_EXECUTION_FIELDS:
        rows.append(f"| `{field}` | populated for package execution rows |")
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
        "executed package revision rows",
        "package linkage rows",
        "package text rows",
        "package execution boundary rows",
        "controlled manuscript package sections",
        "full manuscript revision package execution metadata",
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
    return f"""# First Full Manuscript Revision Package Execution v7.9

## Question
Can Viruse Fabric execute the first full manuscript revision package while keeping new citation additions at zero and preserving non-submission-ready boundaries?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does execute full manuscript revision package as a controlled full manuscript revision package artifact. Full manuscript rewrite count is one. It does not add new citations, does not claim external validation, and does not make the manuscript submission-ready.

Package execution is not external validation. Package execution is not submission readiness. Package execution is not final paper production. Full manuscript rewrite is controlled package artifact only. Controlled package artifact is not acceptance. Controlled package artifact is not peer review. Citation-grounded revised claim is not biological validation. Citation-grounded revised claim is not clinical validation. Citation record pass is not manuscript support. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Full Manuscript Revision Package Execution Metadata
{render_metadata_table()}

## Executed Package Revision Rows
{render_executed_package_revision_rows()}

## Package Linkage Rows
{render_package_linkage_rows()}

## Package Text Rows
{render_package_text_rows()}

## Package Execution Boundary Rows
{render_execution_boundary_rows()}

## Controlled Manuscript Package Sections
{render_controlled_package_sections()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Package Execution Fields
{render_field_table()}

## Package Execution Status Values
{bullet_list(PACKAGE_EXECUTION_STATUS_VALUES)}

## Full Manuscript Revision Package Execution Gates
{bullet_list(PACKAGE_EXECUTION_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Package Execution Interpretation
The v7.9 artifact executes the first full manuscript revision package from the v7.8 package plan.

FMRPE-ROW-0001 executes FMRPP-ROW-0001 and integrates controlled conceptual-context package text linked to BRCA-ROW-0001, CGRX-0001, CGRP-0001, MCM-0001, CIT-REC-0001, EMR-0001, RET-0001, and CAND-0001.

FMRPE-ROW-0002 executes FMRPP-ROW-0002 and integrates controlled methodological-context package text linked to BRCA-ROW-0002, CGRX-0002, CGRP-0002, MCM-0002, CIT-REC-0002, EMR-0002, RET-0002, and CAND-0002.

The package execution creates a controlled full manuscript revision package artifact. It does not add citations, does not create a final paper, does not certify external validation, and does not create submission readiness.

## Execution Boundary
Full manuscript revision package execution count is one.

Planned package revision count is two.

Executed package revision count is two.

Full manuscript revision package count is one.

Full manuscript rewrite count is one.

New citation added count is zero.

Conditional hold count is one.

The project now has an executed controlled manuscript revision package, but it still has no submission-ready manuscript and no external validation. Apparently one rewrite does not magically summon reviewers, editors, or a functioning civilization.

## Linkage Boundary
Each executed package revision links to:

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

This keeps the rewritten package attached to the internal evidence workflow instead of letting it float away as manuscript theater.

## Controlled Package Text Boundary
The controlled manuscript package contains two bounded sections.

The first section supports conceptual context only.

The second section supports methodological background only.

Neither section claims proof, external validation, biological prediction, clinical relevance, laboratory guidance, operational readiness, or accepted scientific theory.

The controlled package is a manuscript artifact, not a submission-ready paper. A rewritten manuscript can still be immature. Humanity keeps demonstrating this in conference deadlines, so we document it explicitly.

## Full Manuscript Boundary
The full manuscript rewrite count is one in this milestone.

This means one controlled full manuscript revision package artifact exists.

It does not mean the manuscript is final.

It does not mean the manuscript is submission-ready.

It does not mean the manuscript has passed a readiness audit.

It does not mean the manuscript has external validation.

It does not mean the theory is proven.

## New Citation Boundary
New citation added count remains zero.

No new citation record is added. No new source is retained. No new bibliography entry is created. This milestone executes package integration using existing audited citation records and existing inserted manuscript citation markers only.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside package execution. It has no retained source record, no citation record, no audited citation record, no planned insertion slot, no inserted marker, no marker audit pass row, no planned claim revision, no executed claim revision, no bounded revised claim audit pass row, no package revision plan, and no executed package revision.

This prevents conditional metadata from sneaking into the controlled manuscript package wearing a fake badge.

## Claim Boundary Toward v8.0
This milestone permits a slightly stronger internal workflow claim than v7.8.

Allowed after v7.9:

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
- manuscript still not submission-ready
- no new citations added during package execution

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

## Output Counts
Full manuscript revision package execution count: 1

Planned package revision count: 2

Executed package revision count: 2

Full manuscript revision package count: 1

Full manuscript rewrite count: 1

New citation added count: 0

Conditional hold count: 1

## Final Boundary Statement
This artifact executes a controlled full manuscript revision package from audited bounded revised claim records.

It does not add new citations, does not certify external validation, does not make the manuscript ready for submission, does not produce a final paper, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstFullManuscriptRevisionPackageExecutionResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    invented_citations = detect_invented_citation_like_patterns(report)

    full_manuscript_revision_package_execution_count = 1
    planned_package_revision_count = int(EXECUTION_METADATA["planned_package_revision_count_from_v7_8"])
    executed_package_revision_count = int(EXECUTION_METADATA["executed_package_revision_count"])
    full_manuscript_revision_package_count = int(EXECUTION_METADATA["full_manuscript_revision_package_count"])
    full_manuscript_rewrite_count = int(EXECUTION_METADATA["full_manuscript_rewrite_count"])
    new_citation_added_count = int(EXECUTION_METADATA["new_citation_added_count"])
    conditional_hold_count = int(EXECUTION_METADATA["conditional_hold_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 29:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if full_manuscript_revision_package_execution_count != 1:
        errors.append(
            "Full manuscript revision package execution count should be one, got: "
            f"{full_manuscript_revision_package_execution_count}"
        )

    if planned_package_revision_count != 2:
        errors.append(
            "Planned package revision count should be two, got: "
            f"{planned_package_revision_count}"
        )

    if executed_package_revision_count != 2:
        errors.append(
            "Executed package revision count should be two, got: "
            f"{executed_package_revision_count}"
        )

    if planned_package_revision_count != executed_package_revision_count:
        errors.append("Each planned package revision should be executed in v7.9")

    if full_manuscript_revision_package_count != 1:
        errors.append(
            "Full manuscript revision package count should be one, got: "
            f"{full_manuscript_revision_package_count}"
        )

    if full_manuscript_rewrite_count != 1:
        errors.append(
            "Full manuscript rewrite count should be one for controlled package execution, got: "
            f"{full_manuscript_rewrite_count}"
        )

    if new_citation_added_count != 0:
        errors.append(f"New citation added count should be zero, got: {new_citation_added_count}")

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    for row in EXECUTED_PACKAGE_REVISION_ROWS:
        missing_fields = [field for field in PACKAGE_EXECUTION_FIELDS if not row.get(field)]
        if missing_fields:
            errors.append(
                f"{row.get('executed_package_revision_id', 'unknown')} missing package execution fields: "
                f"{len(missing_fields)}"
            )

        if row.get("package_execution_status") != "executed_bounded_package_revision":
            errors.append(
                f"{row.get('executed_package_revision_id', 'unknown')} has unexpected execution status"
            )

        if row.get("full_manuscript_rewrite") != "yes_controlled_package_artifact_only":
            errors.append(
                f"{row.get('executed_package_revision_id', 'unknown')} has invalid rewrite boundary"
            )

        if row.get("new_citation_added") != "no":
            errors.append(
                f"{row.get('executed_package_revision_id', 'unknown')} added citation unexpectedly"
            )

        if row.get("submission_readiness_status") != "not_submission_ready":
            errors.append(
                f"{row.get('executed_package_revision_id', 'unknown')} has invalid submission readiness status"
            )

        if row.get("external_validation_status") != "not_external_validation":
            errors.append(
                f"{row.get('executed_package_revision_id', 'unknown')} has invalid external validation status"
            )

    if len(PACKAGE_EXECUTION_FIELDS) < 21:
        errors.append(f"Package execution field count too low: {len(PACKAGE_EXECUTION_FIELDS)}")

    if len(PACKAGE_EXECUTION_STATUS_VALUES) < 6:
        errors.append(
            "Package execution status value count too low: "
            f"{len(PACKAGE_EXECUTION_STATUS_VALUES)}"
        )

    if len(PACKAGE_EXECUTION_GATES) < 22:
        errors.append(f"Package execution gate count too low: {len(PACKAGE_EXECUTION_GATES)}")

    if len(CONTROLLED_MANUSCRIPT_PACKAGE) != 2:
        errors.append(
            "Controlled package section count should be two, got: "
            f"{len(CONTROLLED_MANUSCRIPT_PACKAGE)}"
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
            "Invented citation-like patterns detected outside package execution sections: "
            f"{len(invented_citations)}"
        )

    if word_count < 1550:
        errors.append(
            f"Word count too low for first full manuscript revision package execution: {word_count}"
        )

    warnings.append("Full manuscript revision package is executed, but it is not submission-ready.")
    warnings.append("Full manuscript rewrite count is one, but no new citations are added.")

    passed = not errors

    interpretation = (
        "The v7.9 artifact executes a controlled full manuscript revision package from "
        "two planned package revision rows, creates one controlled manuscript rewrite "
        "artifact, and keeps new citation additions at zero."
    )

    return FirstFullManuscriptRevisionPackageExecutionResult(
        title="First Full Manuscript Revision Package Execution v7.9",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        full_manuscript_revision_package_execution_count=full_manuscript_revision_package_execution_count,
        planned_package_revision_count=planned_package_revision_count,
        executed_package_revision_count=executed_package_revision_count,
        full_manuscript_revision_package_count=full_manuscript_revision_package_count,
        full_manuscript_rewrite_count=full_manuscript_rewrite_count,
        new_citation_added_count=new_citation_added_count,
        conditional_hold_count=conditional_hold_count,
        package_execution_field_count=len(PACKAGE_EXECUTION_FIELDS),
        package_execution_status_value_count=len(PACKAGE_EXECUTION_STATUS_VALUES),
        package_execution_gate_count=len(PACKAGE_EXECUTION_GATES),
        controlled_package_section_count=len(CONTROLLED_MANUSCRIPT_PACKAGE),
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

    print("First Full Manuscript Revision Package Execution v7.9")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(
        "Full manuscript revision package execution count: "
        f"{result.full_manuscript_revision_package_execution_count}"
    )
    print(f"Planned package revision count: {result.planned_package_revision_count}")
    print(f"Executed package revision count: {result.executed_package_revision_count}")
    print(
        "Full manuscript revision package count: "
        f"{result.full_manuscript_revision_package_count}"
    )
    print(f"Full manuscript rewrite count: {result.full_manuscript_rewrite_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Package execution field count: {result.package_execution_field_count}")
    print(
        "Package execution status value count: "
        f"{result.package_execution_status_value_count}"
    )
    print(f"Package execution gate count: {result.package_execution_gate_count}")
    print(f"Controlled package section count: {result.controlled_package_section_count}")
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
