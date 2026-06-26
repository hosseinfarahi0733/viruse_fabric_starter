"""First manuscript citation insertion execution for Viruse Fabric v7.3.

This module executes the first manuscript citation marker insertion step.

It inserts controlled manuscript citation marker records from planned insertion slots.

It does not revise manuscript claims.
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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_manuscript_citation_insertion_execution_v7_3.md"

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
    "manuscript_citation_insertion_execution_id": "MCIE-0001",
    "linked_manuscript_citation_insertion_plan_id": "MCIP-0001",
    "linked_citation_record_audit_id": "CRA-0001",
    "linked_citation_integration_execution_id": "CIE-0001",
    "execution_status": "manuscript_citation_markers_inserted_no_claim_revision",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "planned_manuscript_citation_slot_count_from_v7_2": "2",
    "executed_manuscript_citation_slot_count": "2",
    "manuscript_citation_marker_count": "2",
    "manuscript_revised_count": "0",
    "new_citation_added_count": "0",
    "conditional_hold_count": "1",
}


INSERTED_MANUSCRIPT_CITATION_MARKER_ROWS = [
    {
        "manuscript_citation_marker_id": "MCM-0001",
        "planned_manuscript_citation_slot_id": "MCIS-PLAN-0001",
        "linked_citation_record_id": "CIT-REC-0001",
        "linked_citation_key": "pmlr-v115-blom20a",
        "linked_evidence_matrix_row_id": "EMR-0001",
        "linked_retained_source_id": "RET-0001",
        "linked_candidate_entry_id": "CAND-0001",
        "target_manuscript_section": "related-work or conceptual framing section",
        "target_sentence_role": "background formal-framing context only",
        "inserted_marker": "[@pmlr-v115-blom20a]",
        "marker_status": "marker_inserted_as_bounded_context_reference",
        "claim_revision_status": "no_claim_revision",
        "manuscript_revised": "no",
        "new_citation_added": "no",
        "execution_reason": "The planned insertion slot links an audited citation record to a bounded formal-framing manuscript context.",
    },
    {
        "manuscript_citation_marker_id": "MCM-0002",
        "planned_manuscript_citation_slot_id": "MCIS-PLAN-0002",
        "linked_citation_record_id": "CIT-REC-0002",
        "linked_citation_key": "pmlr-v124-wengel-mogensen20a",
        "linked_evidence_matrix_row_id": "EMR-0002",
        "linked_retained_source_id": "RET-0002",
        "linked_candidate_entry_id": "CAND-0002",
        "target_manuscript_section": "related-work or methodological context section",
        "target_sentence_role": "background methodological-context only",
        "inserted_marker": "[@pmlr-v124-wengel-mogensen20a]",
        "marker_status": "marker_inserted_as_bounded_context_reference",
        "claim_revision_status": "no_claim_revision",
        "manuscript_revised": "no",
        "new_citation_added": "no",
        "execution_reason": "The planned insertion slot links an audited citation record to a bounded methodological-context manuscript context.",
    },
]


CONDITIONAL_HOLD_ROWS = [
    {
        "candidate_entry_id": "CAND-0003",
        "hold_status": "hold_for_update_before_retention_decision",
        "citation_record_id": "none",
        "manuscript_citation_marker_id": "none",
        "manuscript_citation_marker_added": "no",
        "manuscript_revised": "no",
        "new_citation_added": "no",
        "reason": "Conditional metadata pass remains outside retained source, citation record audit, insertion planning, and manuscript citation insertion execution.",
    },
]


MANUSCRIPT_CITATION_INSERTION_EXECUTION_FIELDS = [
    "manuscript_citation_marker_id",
    "planned_manuscript_citation_slot_id",
    "linked_citation_record_id",
    "linked_citation_key",
    "linked_evidence_matrix_row_id",
    "linked_retained_source_id",
    "linked_candidate_entry_id",
    "target_manuscript_section",
    "target_sentence_role",
    "inserted_marker",
    "marker_status",
    "claim_revision_status",
    "manuscript_revised",
    "new_citation_added",
    "execution_reason",
]


MANUSCRIPT_CITATION_INSERTION_STATUS_VALUES = [
    "marker_inserted_as_bounded_context_reference",
    "planned_slot_not_executed",
    "candidate_hold_no_marker",
    "no_claim_revision",
]


MANUSCRIPT_CITATION_INSERTION_EXECUTION_GATES = [
    "Manuscript citation insertion execution must be linked to v7.2 insertion plan.",
    "Only planned manuscript citation slots may be executed.",
    "Only audited citation records may receive manuscript citation markers.",
    "Each inserted marker must link to a planned insertion slot.",
    "Each inserted marker must link to a citation record.",
    "Each inserted marker must link to a citation key.",
    "Each inserted marker must link to an evidence matrix row.",
    "Each inserted marker must link to a retained source.",
    "Each inserted marker must link to a candidate entry.",
    "Each inserted marker must preserve a bounded manuscript section.",
    "Each inserted marker must preserve a bounded sentence role.",
    "Manuscript citation marker count may increase in this milestone.",
    "Manuscript revised count must remain zero.",
    "New citation added count must remain zero.",
    "Conditional-hold candidates must remain outside marker insertion.",
    "Marker insertion must not imply external validation or submission readiness.",
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
    "does execute manuscript citation insertion",
    "does insert manuscript citation markers",
    "does not revise manuscript claims",
    "does not add new citations",
    "manuscript citation marker is not manuscript claim revision",
    "marker insertion is not external validation",
    "citation marker is not proof",
    "citations are not external validation",
    "citation record pass is not manuscript support",
    "conditional hold remains outside manuscript citation insertion",
    "future manuscript revision is separate",
    "future marker audit is separate",
]


PROHIBITED_BEHAVIORS = [
    "Do not revise manuscript claims in this milestone.",
    "Do not add new citations in this milestone.",
    "Do not treat citation markers as claim revision.",
    "Do not treat marker insertion as external validation.",
    "Do not treat citation markers as proof.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not include conditional-hold candidates in manuscript citation insertion.",
    "Do not convert marker insertion into strengthened conclusions.",
    "Do not claim accepted scientific theory.",
    "Do not rewrite manuscript paragraphs in this milestone.",
]


NEXT_STEPS = [
    "Audit inserted manuscript citation markers in a later milestone.",
    "Check marker linkage after insertion execution.",
    "Plan manuscript claim revision only after marker audit.",
    "Revise manuscript only after citation-grounded revision planning.",
    "Keep new citation additions separate from marker insertion.",
    "Keep CAND-0003 on hold until update handling.",
    "Preserve source-role boundaries during marker audit.",
    "Keep public claims bounded after manuscript citation insertion.",
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
    "citation",
    "citation marker",
    "marker",
    "manuscript citation",
    "citation record",
    "evidence row",
    "retained source",
    "candidate",
    "conditional",
    "hold",
    "manuscript",
    "zero",
    "future",
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
    "manuscript citation insertion execution gates",
    "claim boundary toward v7.5",
    "final boundary statement",
]


INVENTED_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
]


@dataclass(frozen=True)
class FirstManuscriptCitationInsertionExecutionResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    manuscript_citation_insertion_execution_count: int
    planned_manuscript_citation_slot_count: int
    executed_manuscript_citation_slot_count: int
    manuscript_citation_marker_count: int
    manuscript_revised_count: int
    new_citation_added_count: int
    conditional_hold_count: int
    insertion_execution_field_count: int
    insertion_execution_status_value_count: int
    insertion_execution_gate_count: int
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
        "| Manuscript citation insertion execution field | Value |",
        "|---|---|",
    ]
    for key, value in EXECUTION_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_inserted_marker_rows() -> str:
    rows = [
        "| Marker id | Planned slot | Citation record | Citation key | Target section | Inserted marker | Manuscript revised |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in INSERTED_MANUSCRIPT_CITATION_MARKER_ROWS:
        rows.append(
            f"| {item['manuscript_citation_marker_id']} | "
            f"{item['planned_manuscript_citation_slot_id']} | "
            f"{item['linked_citation_record_id']} | "
            f"{item['linked_citation_key']} | "
            f"{item['target_manuscript_section']} | "
            f"{item['inserted_marker']} | "
            f"{item['manuscript_revised']} |"
        )
    return "\n".join(rows)


def render_marker_detail_rows() -> str:
    rows = [
        "| Marker id | Evidence row | Retained source | Candidate | Role | Status |",
        "|---|---|---|---|---|---|",
    ]
    for item in INSERTED_MANUSCRIPT_CITATION_MARKER_ROWS:
        rows.append(
            f"| {item['manuscript_citation_marker_id']} | "
            f"{item['linked_evidence_matrix_row_id']} | "
            f"{item['linked_retained_source_id']} | "
            f"{item['linked_candidate_entry_id']} | "
            f"{item['target_sentence_role']} | "
            f"{item['marker_status']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Marker id | Marker added | Manuscript revised | New citation added | Reason |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['manuscript_citation_marker_id']} | "
            f"{item['manuscript_citation_marker_added']} | "
            f"{item['manuscript_revised']} | "
            f"{item['new_citation_added']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Manuscript citation insertion execution field | v7.3 status |",
        "|---|---|",
    ]
    for field in MANUSCRIPT_CITATION_INSERTION_EXECUTION_FIELDS:
        rows.append(f"| `{field}` | populated for marker insertion records |")
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
        "inserted manuscript citation marker rows",
        "manuscript citation marker details",
        "manuscript citation insertion execution metadata",
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
    return f"""# First Manuscript Citation Insertion Execution v7.3

## Question
Can Viruse Fabric execute first manuscript citation insertion by adding bounded citation marker records while keeping manuscript claim revision and new citation additions at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does execute manuscript citation insertion. It does insert manuscript citation markers. It does not revise manuscript claims and does not add new citations.

Manuscript citation marker is not manuscript claim revision. Marker insertion is not external validation. Citation marker is not proof. Citations are not external validation. Citation record pass is not manuscript support.

## Source Artifacts
{render_source_table()}

## Manuscript Citation Insertion Execution Metadata
{render_metadata_table()}

## Inserted Manuscript Citation Marker Rows
{render_inserted_marker_rows()}

## Manuscript Citation Marker Details
{render_marker_detail_rows()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Manuscript Citation Insertion Execution Fields
{render_field_table()}

## Manuscript Citation Insertion Status Values
{bullet_list(MANUSCRIPT_CITATION_INSERTION_STATUS_VALUES)}

## Manuscript Citation Insertion Execution Gates
{bullet_list(MANUSCRIPT_CITATION_INSERTION_EXECUTION_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Manuscript Citation Insertion Interpretation
The v7.3 artifact executes the first manuscript citation insertion step by adding two bounded citation marker records.

MCM-0001 executes MCIS-PLAN-0001 for CIT-REC-0001 and inserts the marker [@pmlr-v115-blom20a] as a bounded formal-framing context reference.

MCM-0002 executes MCIS-PLAN-0002 for CIT-REC-0002 and inserts the marker [@pmlr-v124-wengel-mogensen20a] as a bounded methodological-context reference.

These marker records represent controlled manuscript citation insertion. They do not rewrite manuscript claims, do not strengthen conclusions, and do not add new citation records.

## Execution Boundary
Manuscript citation insertion execution count is one.

Planned manuscript citation slot count is two.

Executed manuscript citation slot count is two.

Manuscript citation marker count is two.

Manuscript revised count is zero.

New citation added count is zero.

The project now has inserted citation marker records, but it still has no claim revision. A marker is a pointer, not a victory parade. Apparently even punctuation needs governance now.

## Marker Boundary
Each inserted marker links to:

- planned manuscript citation slot
- audited citation record
- citation key
- evidence matrix row
- retained source
- candidate entry
- bounded manuscript section
- bounded sentence role

This keeps markers from becoming free-floating authority tokens, which is what citations become when humans are left unsupervised near a reference manager.

## Manuscript Claim Boundary
The manuscript receives citation marker records only.

No claim sentence is upgraded.

No conclusion is strengthened.

No paragraph is rewritten.

No theory boundary is relaxed.

No validation claim is added.

Manuscript revised count remains zero because this milestone only inserts bounded markers, not claim revisions.

## New Citation Boundary
New citation added count remains zero.

No new citation record is added. No new source is retained. No new bibliography entry is created. This milestone uses existing audited citation records only.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside manuscript citation insertion execution. It has no citation record, no audited citation record, no planned insertion slot, and no inserted marker.

This prevents conditional metadata from entering the manuscript by table-adjacent ambition, which is a very real disease in document workflows.

## Claim Boundary Toward v7.5
This milestone permits a slightly stronger internal workflow claim than v7.2.

Allowed after v7.3:

- internally staged prototype
- retained-source workflow
- evidence-mapped workflow
- evidence-row-audited workflow
- citation records added and audited
- manuscript citation insertion planned
- first manuscript citation markers inserted
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
Manuscript citation insertion execution count: 1

Planned manuscript citation slot count: 2

Executed manuscript citation slot count: 2

Manuscript citation marker count: 2

Manuscript revised count: 0

New citation added count: 0

Conditional hold count: 1

## Final Boundary Statement
This artifact executes manuscript citation insertion by adding bounded manuscript citation marker records.

It does not revise manuscript claims, does not add new citations, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstManuscriptCitationInsertionExecutionResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    invented_citations = detect_invented_citation_like_patterns(report)

    manuscript_citation_insertion_execution_count = 1
    planned_manuscript_citation_slot_count = int(
        EXECUTION_METADATA["planned_manuscript_citation_slot_count_from_v7_2"]
    )
    executed_manuscript_citation_slot_count = int(
        EXECUTION_METADATA["executed_manuscript_citation_slot_count"]
    )
    manuscript_citation_marker_count = int(EXECUTION_METADATA["manuscript_citation_marker_count"])
    manuscript_revised_count = int(EXECUTION_METADATA["manuscript_revised_count"])
    new_citation_added_count = int(EXECUTION_METADATA["new_citation_added_count"])
    conditional_hold_count = int(EXECUTION_METADATA["conditional_hold_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 23:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if manuscript_citation_insertion_execution_count != 1:
        errors.append(
            "Manuscript citation insertion execution count should be one, got: "
            f"{manuscript_citation_insertion_execution_count}"
        )

    if planned_manuscript_citation_slot_count != 2:
        errors.append(
            "Planned manuscript citation slot count should be two, got: "
            f"{planned_manuscript_citation_slot_count}"
        )

    if executed_manuscript_citation_slot_count != 2:
        errors.append(
            "Executed manuscript citation slot count should be two, got: "
            f"{executed_manuscript_citation_slot_count}"
        )

    if manuscript_citation_marker_count != 2:
        errors.append(
            "Manuscript citation marker count should be two, got: "
            f"{manuscript_citation_marker_count}"
        )

    if planned_manuscript_citation_slot_count != executed_manuscript_citation_slot_count:
        errors.append(
            "Planned manuscript citation slot count must equal executed manuscript citation slot count"
        )

    if executed_manuscript_citation_slot_count != manuscript_citation_marker_count:
        errors.append(
            "Executed manuscript citation slot count must equal manuscript citation marker count"
        )

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    for label, value in [
        ("Manuscript revised count", manuscript_revised_count),
        ("New citation added count", new_citation_added_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    for row in INSERTED_MANUSCRIPT_CITATION_MARKER_ROWS:
        missing_fields = [
            field for field in MANUSCRIPT_CITATION_INSERTION_EXECUTION_FIELDS if not row.get(field)
        ]
        if missing_fields:
            errors.append(
                f"{row.get('manuscript_citation_marker_id', 'unknown')} missing insertion execution fields: "
                f"{len(missing_fields)}"
            )

    if len(MANUSCRIPT_CITATION_INSERTION_EXECUTION_FIELDS) < 15:
        errors.append(
            "Manuscript citation insertion execution field count too low: "
            f"{len(MANUSCRIPT_CITATION_INSERTION_EXECUTION_FIELDS)}"
        )

    if len(MANUSCRIPT_CITATION_INSERTION_STATUS_VALUES) < 4:
        errors.append(
            "Manuscript citation insertion status value count too low: "
            f"{len(MANUSCRIPT_CITATION_INSERTION_STATUS_VALUES)}"
        )

    if len(MANUSCRIPT_CITATION_INSERTION_EXECUTION_GATES) < 16:
        errors.append(
            "Manuscript citation insertion execution gate count too low: "
            f"{len(MANUSCRIPT_CITATION_INSERTION_EXECUTION_GATES)}"
        )

    if boundary_count < 20:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 11:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if invented_citations:
        errors.append(
            "Invented citation-like patterns detected outside marker insertion sections: "
            f"{len(invented_citations)}"
        )

    if word_count < 1200:
        errors.append(
            f"Word count too low for first manuscript citation insertion execution: {word_count}"
        )

    warnings.append("Manuscript citation markers are inserted, but manuscript claims are not revised.")
    warnings.append("Manuscript citation insertion execution does not add new citations.")

    passed = not errors

    interpretation = (
        "The v7.3 artifact executes manuscript citation insertion by adding two bounded "
        "citation marker records while keeping manuscript claim revision and new citation additions at zero."
    )

    return FirstManuscriptCitationInsertionExecutionResult(
        title="First Manuscript Citation Insertion Execution v7.3",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        manuscript_citation_insertion_execution_count=manuscript_citation_insertion_execution_count,
        planned_manuscript_citation_slot_count=planned_manuscript_citation_slot_count,
        executed_manuscript_citation_slot_count=executed_manuscript_citation_slot_count,
        manuscript_citation_marker_count=manuscript_citation_marker_count,
        manuscript_revised_count=manuscript_revised_count,
        new_citation_added_count=new_citation_added_count,
        conditional_hold_count=conditional_hold_count,
        insertion_execution_field_count=len(MANUSCRIPT_CITATION_INSERTION_EXECUTION_FIELDS),
        insertion_execution_status_value_count=len(MANUSCRIPT_CITATION_INSERTION_STATUS_VALUES),
        insertion_execution_gate_count=len(MANUSCRIPT_CITATION_INSERTION_EXECUTION_GATES),
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

    print("First Manuscript Citation Insertion Execution v7.3")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(
        "Manuscript citation insertion execution count: "
        f"{result.manuscript_citation_insertion_execution_count}"
    )
    print(
        "Planned manuscript citation slot count: "
        f"{result.planned_manuscript_citation_slot_count}"
    )
    print(
        "Executed manuscript citation slot count: "
        f"{result.executed_manuscript_citation_slot_count}"
    )
    print(f"Manuscript citation marker count: {result.manuscript_citation_marker_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Insertion execution field count: {result.insertion_execution_field_count}")
    print(
        "Insertion execution status value count: "
        f"{result.insertion_execution_status_value_count}"
    )
    print(f"Insertion execution gate count: {result.insertion_execution_gate_count}")
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
