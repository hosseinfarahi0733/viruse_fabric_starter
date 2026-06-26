"""First full manuscript revision package plan for Viruse Fabric v7.8.

This module plans the first full manuscript revision package layer based on
audited bounded revised claim records.

It does not execute the package.
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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_full_manuscript_revision_package_plan_v7_8.md"

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
    "full_manuscript_revision_package_plan_id": "FMRPP-0001",
    "linked_bounded_revised_claim_audit_id": "BRCA-0001",
    "linked_citation_grounded_manuscript_claim_revision_execution_id": "CGMCRE-0001",
    "linked_citation_grounded_manuscript_claim_revision_plan_id": "CGMCRP-0001",
    "linked_manuscript_citation_marker_audit_id": "MCMA-0001",
    "plan_status": "package_plan_only_no_full_manuscript_rewrite",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "audited_bounded_revised_claim_record_count_from_v7_7": "2",
    "planned_package_revision_count": "2",
    "full_manuscript_revision_package_execution_count": "0",
    "full_manuscript_rewrite_count": "0",
    "new_citation_added_count": "0",
    "conditional_hold_count": "1",
}


PLANNED_PACKAGE_REVISION_ROWS = [
    {
        "planned_package_revision_id": "FMRPP-ROW-0001",
        "linked_revised_claim_audit_row_id": "BRCA-ROW-0001",
        "linked_executed_claim_revision_id": "CGRX-0001",
        "linked_planned_claim_revision_id": "CGRP-0001",
        "linked_manuscript_citation_marker_id": "MCM-0001",
        "linked_citation_record_id": "CIT-REC-0001",
        "linked_citation_key": "pmlr-v115-blom20a",
        "linked_evidence_matrix_row_id": "EMR-0001",
        "linked_retained_source_id": "RET-0001",
        "linked_candidate_entry_id": "CAND-0001",
        "planned_manuscript_package_section": "related-work or conceptual framing section",
        "planned_package_revision_role": "bounded conceptual-context package insertion",
        "planned_package_action": "plan_for_future_full_manuscript_package_integration_only",
        "package_execution_status": "not_executed_plan_only",
        "full_manuscript_rewrite": "no",
        "new_citation_added": "no",
        "overclaim_guard": "Do not turn conceptual adjacency into proof, validation, or extension.",
        "planning_reason": "The audited bounded revised claim can later be integrated into a full manuscript revision package as contextual framing only.",
    },
    {
        "planned_package_revision_id": "FMRPP-ROW-0002",
        "linked_revised_claim_audit_row_id": "BRCA-ROW-0002",
        "linked_executed_claim_revision_id": "CGRX-0002",
        "linked_planned_claim_revision_id": "CGRP-0002",
        "linked_manuscript_citation_marker_id": "MCM-0002",
        "linked_citation_record_id": "CIT-REC-0002",
        "linked_citation_key": "pmlr-v124-wengel-mogensen20a",
        "linked_evidence_matrix_row_id": "EMR-0002",
        "linked_retained_source_id": "RET-0002",
        "linked_candidate_entry_id": "CAND-0002",
        "planned_manuscript_package_section": "related-work or methodological context section",
        "planned_package_revision_role": "bounded methodological-context package insertion",
        "planned_package_action": "plan_for_future_full_manuscript_package_integration_only",
        "package_execution_status": "not_executed_plan_only",
        "full_manuscript_rewrite": "no",
        "new_citation_added": "no",
        "overclaim_guard": "Do not turn methodological background into biological prediction, clinical relevance, or operational screening.",
        "planning_reason": "The audited bounded revised claim can later be integrated into a full manuscript revision package as methodological background only.",
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
        "planned_package_revision": "no",
        "full_manuscript_rewrite": "no",
        "new_citation_added": "no",
        "reason": "Conditional metadata pass remains outside retained source, citation record audit, marker insertion, marker audit, claim revision execution, revised claim audit, and full manuscript package planning.",
    },
]


PACKAGE_PLAN_FIELDS = [
    "planned_package_revision_id",
    "linked_revised_claim_audit_row_id",
    "linked_executed_claim_revision_id",
    "linked_planned_claim_revision_id",
    "linked_manuscript_citation_marker_id",
    "linked_citation_record_id",
    "linked_citation_key",
    "linked_evidence_matrix_row_id",
    "linked_retained_source_id",
    "linked_candidate_entry_id",
    "planned_manuscript_package_section",
    "planned_package_revision_role",
    "planned_package_action",
    "package_execution_status",
    "full_manuscript_rewrite",
    "new_citation_added",
    "overclaim_guard",
    "planning_reason",
]


PACKAGE_PLAN_STATUS_VALUES = [
    "package_plan_only_no_full_manuscript_rewrite",
    "not_executed_plan_only",
    "candidate_hold_no_package_revision_plan",
    "future_package_execution_required",
]


PACKAGE_PLAN_GATES = [
    "Full manuscript revision package planning must be linked to v7.7 bounded revised claim audit.",
    "Only audited bounded revised claim records may enter package planning.",
    "Each planned package revision must link to a revised claim audit row.",
    "Each planned package revision must link to an executed claim revision.",
    "Each planned package revision must link to a planned claim revision.",
    "Each planned package revision must link to a manuscript citation marker.",
    "Each planned package revision must link to an audited citation record.",
    "Each planned package revision must link to a citation key.",
    "Each planned package revision must link to an evidence matrix row.",
    "Each planned package revision must link to a retained source.",
    "Each planned package revision must link to a candidate entry.",
    "Each planned package revision must have a bounded package section.",
    "Each planned package revision must have a bounded package role.",
    "Each planned package revision must include an overclaim guard.",
    "Full manuscript revision package planning must not execute the package.",
    "Full manuscript rewrite count must remain zero.",
    "New citation added count must remain zero.",
    "Conditional-hold candidates must remain outside package planning.",
    "Package planning must not imply external validation or submission readiness.",
]


BOUNDARY_PHRASES = [
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does plan full manuscript revision package integration",
    "does not execute full manuscript revision package",
    "does not rewrite the full manuscript",
    "does not add new citations",
    "does not claim external validation",
    "full manuscript revision package plan is not full manuscript rewrite",
    "package plan is not package execution",
    "package plan is not proof",
    "package plan is not external validation",
    "package plan is not submission readiness",
    "audited bounded revised claim is not full manuscript support",
    "citation-grounded revised claim is not biological validation",
    "citation-grounded revised claim is not clinical validation",
    "citation record pass is not manuscript support",
    "citations are not external validation",
    "bounded context remains bounded",
    "full manuscript rewrite remains zero",
    "new citation added count remains zero",
    "conditional hold remains outside package planning",
    "future package execution is separate",
    "future package audit is separate",
    "future submission readiness audit is separate",
]


PROHIBITED_BEHAVIORS = [
    "Do not execute the full manuscript revision package in this milestone.",
    "Do not rewrite the full manuscript in this milestone.",
    "Do not add new citations in this milestone.",
    "Do not treat package planning as package execution.",
    "Do not treat package planning as proof.",
    "Do not treat package planning as external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not include conditional-hold candidates in package revision plans.",
    "Do not convert bounded revised claims into strengthened conclusions.",
    "Do not claim accepted scientific theory.",
    "Do not upgrade validation language.",
    "Do not claim biological prediction or operational causal screening.",
]


NEXT_STEPS = [
    "Execute full manuscript revision package integration in a later milestone.",
    "Keep package execution separate from package planning.",
    "Audit any executed full manuscript package after execution.",
    "Keep new citation additions separate from package planning.",
    "Preserve revised claim linkage during future package execution.",
    "Keep CAND-0003 on hold until update handling.",
    "Check public claim language after future package audit.",
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
    "avoid",
    "guard",
    "no_",
    "none",
    "bounded",
    "plan",
    "planned",
    "future",
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
    "full manuscript revision package plan gates",
    "claim boundary toward v7.9",
    "final boundary statement",
]


INVENTED_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
]


@dataclass(frozen=True)
class FirstFullManuscriptRevisionPackagePlanResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    full_manuscript_revision_package_plan_count: int
    audited_bounded_revised_claim_record_count: int
    planned_package_revision_count: int
    full_manuscript_revision_package_execution_count: int
    full_manuscript_rewrite_count: int
    new_citation_added_count: int
    conditional_hold_count: int
    package_plan_field_count: int
    package_plan_status_value_count: int
    package_plan_gate_count: int
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
        "| Full manuscript revision package plan field | Value |",
        "|---|---|",
    ]
    for key, value in PLAN_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_planned_package_revision_rows() -> str:
    rows = [
        "| Planned package revision | Revised claim audit row | Executed revision | Citation record | Citation key | Package status |",
        "|---|---|---|---|---|---|",
    ]
    for item in PLANNED_PACKAGE_REVISION_ROWS:
        rows.append(
            f"| {item['planned_package_revision_id']} | "
            f"{item['linked_revised_claim_audit_row_id']} | "
            f"{item['linked_executed_claim_revision_id']} | "
            f"{item['linked_citation_record_id']} | "
            f"{item['linked_citation_key']} | "
            f"{item['package_execution_status']} |"
        )
    return "\n".join(rows)


def render_package_linkage_rows() -> str:
    rows = [
        "| Planned package revision | Planned claim revision | Marker | Evidence row | Retained source | Candidate |",
        "|---|---|---|---|---|---|",
    ]
    for item in PLANNED_PACKAGE_REVISION_ROWS:
        rows.append(
            f"| {item['planned_package_revision_id']} | "
            f"{item['linked_planned_claim_revision_id']} | "
            f"{item['linked_manuscript_citation_marker_id']} | "
            f"{item['linked_evidence_matrix_row_id']} | "
            f"{item['linked_retained_source_id']} | "
            f"{item['linked_candidate_entry_id']} |"
        )
    return "\n".join(rows)


def render_package_role_rows() -> str:
    rows = [
        "| Planned package revision | Package section | Package role | Full manuscript rewrite | New citation added |",
        "|---|---|---|---|---|",
    ]
    for item in PLANNED_PACKAGE_REVISION_ROWS:
        rows.append(
            f"| {item['planned_package_revision_id']} | "
            f"{item['planned_manuscript_package_section']} | "
            f"{item['planned_package_revision_role']} | "
            f"{item['full_manuscript_rewrite']} | "
            f"{item['new_citation_added']} |"
        )
    return "\n".join(rows)


def render_overclaim_guard_rows() -> str:
    rows = [
        "| Planned package revision | Overclaim guard | Planning reason |",
        "|---|---|---|",
    ]
    for item in PLANNED_PACKAGE_REVISION_ROWS:
        rows.append(
            f"| {item['planned_package_revision_id']} | "
            f"{item['overclaim_guard']} | "
            f"{item['planning_reason']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Planned package revision | Full manuscript rewrite | New citation added | Reason |",
        "|---|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['planned_package_revision']} | "
            f"{item['full_manuscript_rewrite']} | "
            f"{item['new_citation_added']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Package plan field | v7.8 status |",
        "|---|---|",
    ]
    for field in PACKAGE_PLAN_FIELDS:
        rows.append(f"| `{field}` | populated for package planning rows |")
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
        "planned package revision rows",
        "package linkage rows",
        "package role rows",
        "package overclaim guard rows",
        "full manuscript revision package plan metadata",
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
    return f"""# First Full Manuscript Revision Package Plan v7.8

## Question
Can Viruse Fabric plan a full manuscript revision package from audited bounded revised claim records while keeping package execution, full manuscript rewrite, and new citation additions at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does plan full manuscript revision package integration. It does not execute full manuscript revision package, does not rewrite the full manuscript, does not add new citations, and does not claim external validation.

Full manuscript revision package plan is not full manuscript rewrite. Package plan is not package execution. Package plan is not proof. Package plan is not external validation. Package plan is not submission readiness. Audited bounded revised claim is not full manuscript support. Citation-grounded revised claim is not biological validation. Citation-grounded revised claim is not clinical validation. Citation record pass is not manuscript support. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Full Manuscript Revision Package Plan Metadata
{render_metadata_table()}

## Planned Package Revision Rows
{render_planned_package_revision_rows()}

## Package Linkage Rows
{render_package_linkage_rows()}

## Package Role Rows
{render_package_role_rows()}

## Package Overclaim Guard Rows
{render_overclaim_guard_rows()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Package Plan Fields
{render_field_table()}

## Package Plan Status Values
{bullet_list(PACKAGE_PLAN_STATUS_VALUES)}

## Full Manuscript Revision Package Plan Gates
{bullet_list(PACKAGE_PLAN_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Package Plan Interpretation
The v7.8 artifact plans the first full manuscript revision package layer from audited bounded revised claim records.

FMRPP-ROW-0001 plans future package integration from BRCA-ROW-0001, CGRX-0001, CGRP-0001, MCM-0001, CIT-REC-0001, EMR-0001, RET-0001, and CAND-0001.

FMRPP-ROW-0002 plans future package integration from BRCA-ROW-0002, CGRX-0002, CGRP-0002, MCM-0002, CIT-REC-0002, EMR-0002, RET-0002, and CAND-0002.

These are package revision plans only. They do not execute package integration, do not rewrite the full manuscript, do not add new citations, and do not create a submission-ready manuscript.

## Planning Boundary
Full manuscript revision package plan count is one.

Audited bounded revised claim record count is two.

Planned package revision count is two.

Full manuscript revision package execution count is zero.

Full manuscript rewrite count is zero.

New citation added count is zero.

The project now has a plan for a full manuscript revision package, but it still has no executed package and no full manuscript rewrite. This is where documents often start inflating like a grant proposal in humid weather. We are not encouraging that behavior.

## Linkage Boundary
Each planned package revision links to:

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

This keeps future package integration attached to the internal evidence workflow instead of letting it become a decorative manuscript fog machine.

## Package Role Boundary
The package plan defines where audited bounded revised claims may later enter a full manuscript package.

It does not apply package text.

It does not rewrite manuscript sections.

It does not reorganize the manuscript.

It does not produce a final manuscript.

It does not produce a public claim package.

It does not create submission readiness.

## Full Manuscript Boundary
The full manuscript is not rewritten in this milestone.

No full manuscript revision package is executed.

No final manuscript is produced.

No submission-ready manuscript is produced.

No public claim package is produced.

Full manuscript rewrite count remains zero.

## New Citation Boundary
New citation added count remains zero.

No new citation record is added. No new source is retained. No new bibliography entry is created. This milestone uses existing audited bounded revised claim records only.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside package planning. It has no retained source record, no citation record, no audited citation record, no planned insertion slot, no inserted marker, no marker audit pass row, no planned claim revision, no executed claim revision, no bounded revised claim audit pass row, and no package revision plan.

This prevents conditional metadata from wandering into a future manuscript package while pretending it was invited. It was not.

## Claim Boundary Toward v7.9
This milestone permits a slightly stronger internal workflow claim than v7.7.

Allowed after v7.8:

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
Full manuscript revision package plan count: 1

Audited bounded revised claim record count: 2

Planned package revision count: 2

Full manuscript revision package execution count: 0

Full manuscript rewrite count: 0

New citation added count: 0

Conditional hold count: 1

## Final Boundary Statement
This artifact plans full manuscript revision package integration from audited bounded revised claim records.

It does not execute the package, does not rewrite the full manuscript, does not add new citations, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstFullManuscriptRevisionPackagePlanResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    invented_citations = detect_invented_citation_like_patterns(report)

    full_manuscript_revision_package_plan_count = 1
    audited_bounded_revised_claim_record_count = int(
        PLAN_METADATA["audited_bounded_revised_claim_record_count_from_v7_7"]
    )
    planned_package_revision_count = int(PLAN_METADATA["planned_package_revision_count"])
    full_manuscript_revision_package_execution_count = int(
        PLAN_METADATA["full_manuscript_revision_package_execution_count"]
    )
    full_manuscript_rewrite_count = int(PLAN_METADATA["full_manuscript_rewrite_count"])
    new_citation_added_count = int(PLAN_METADATA["new_citation_added_count"])
    conditional_hold_count = int(PLAN_METADATA["conditional_hold_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 28:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if full_manuscript_revision_package_plan_count != 1:
        errors.append(
            "Full manuscript revision package plan count should be one, got: "
            f"{full_manuscript_revision_package_plan_count}"
        )

    if audited_bounded_revised_claim_record_count != 2:
        errors.append(
            "Audited bounded revised claim record count should be two, got: "
            f"{audited_bounded_revised_claim_record_count}"
        )

    if planned_package_revision_count != 2:
        errors.append(
            "Planned package revision count should be two, got: "
            f"{planned_package_revision_count}"
        )

    if audited_bounded_revised_claim_record_count != planned_package_revision_count:
        errors.append("Each audited bounded revised claim should map to one package revision plan")

    if full_manuscript_revision_package_execution_count != 0:
        errors.append(
            "Full manuscript revision package execution count should be zero, got: "
            f"{full_manuscript_revision_package_execution_count}"
        )

    if full_manuscript_rewrite_count != 0:
        errors.append(
            "Full manuscript rewrite count should be zero, got: "
            f"{full_manuscript_rewrite_count}"
        )

    if new_citation_added_count != 0:
        errors.append(f"New citation added count should be zero, got: {new_citation_added_count}")

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    for row in PLANNED_PACKAGE_REVISION_ROWS:
        missing_fields = [field for field in PACKAGE_PLAN_FIELDS if not row.get(field)]
        if missing_fields:
            errors.append(
                f"{row.get('planned_package_revision_id', 'unknown')} missing package plan fields: "
                f"{len(missing_fields)}"
            )

        if row.get("package_execution_status") != "not_executed_plan_only":
            errors.append(
                f"{row.get('planned_package_revision_id', 'unknown')} has unexpected execution status"
            )

        if row.get("full_manuscript_rewrite") != "no":
            errors.append(
                f"{row.get('planned_package_revision_id', 'unknown')} rewrote full manuscript unexpectedly"
            )

        if row.get("new_citation_added") != "no":
            errors.append(
                f"{row.get('planned_package_revision_id', 'unknown')} added citation unexpectedly"
            )

    if len(PACKAGE_PLAN_FIELDS) < 18:
        errors.append(f"Package plan field count too low: {len(PACKAGE_PLAN_FIELDS)}")

    if len(PACKAGE_PLAN_STATUS_VALUES) < 4:
        errors.append(
            "Package plan status value count too low: "
            f"{len(PACKAGE_PLAN_STATUS_VALUES)}"
        )

    if len(PACKAGE_PLAN_GATES) < 19:
        errors.append(f"Package plan gate count too low: {len(PACKAGE_PLAN_GATES)}")

    if boundary_count < 26:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 13:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if invented_citations:
        errors.append(
            "Invented citation-like patterns detected outside package plan sections: "
            f"{len(invented_citations)}"
        )

    if word_count < 1450:
        errors.append(
            f"Word count too low for first full manuscript revision package plan: {word_count}"
        )

    warnings.append("Full manuscript revision package is planned, but not executed.")
    warnings.append("Full manuscript revision package planning does not rewrite the manuscript.")

    passed = not errors

    interpretation = (
        "The v7.8 artifact plans a full manuscript revision package from two audited "
        "bounded revised claim records while keeping package execution, full manuscript "
        "rewrite, and new citation additions at zero."
    )

    return FirstFullManuscriptRevisionPackagePlanResult(
        title="First Full Manuscript Revision Package Plan v7.8",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        full_manuscript_revision_package_plan_count=full_manuscript_revision_package_plan_count,
        audited_bounded_revised_claim_record_count=audited_bounded_revised_claim_record_count,
        planned_package_revision_count=planned_package_revision_count,
        full_manuscript_revision_package_execution_count=full_manuscript_revision_package_execution_count,
        full_manuscript_rewrite_count=full_manuscript_rewrite_count,
        new_citation_added_count=new_citation_added_count,
        conditional_hold_count=conditional_hold_count,
        package_plan_field_count=len(PACKAGE_PLAN_FIELDS),
        package_plan_status_value_count=len(PACKAGE_PLAN_STATUS_VALUES),
        package_plan_gate_count=len(PACKAGE_PLAN_GATES),
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

    print("First Full Manuscript Revision Package Plan v7.8")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(
        "Full manuscript revision package plan count: "
        f"{result.full_manuscript_revision_package_plan_count}"
    )
    print(
        "Audited bounded revised claim record count: "
        f"{result.audited_bounded_revised_claim_record_count}"
    )
    print(f"Planned package revision count: {result.planned_package_revision_count}")
    print(
        "Full manuscript revision package execution count: "
        f"{result.full_manuscript_revision_package_execution_count}"
    )
    print(f"Full manuscript rewrite count: {result.full_manuscript_rewrite_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Package plan field count: {result.package_plan_field_count}")
    print(f"Package plan status value count: {result.package_plan_status_value_count}")
    print(f"Package plan gate count: {result.package_plan_gate_count}")
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
