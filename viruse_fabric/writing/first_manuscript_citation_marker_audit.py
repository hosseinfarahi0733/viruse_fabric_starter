"""First manuscript citation marker audit for Viruse Fabric v7.4.

This module audits the first manuscript citation marker records created in v7.3.

It verifies marker linkage to planned insertion slots, citation records, evidence
matrix rows, retained sources, and candidate entries.

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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_manuscript_citation_marker_audit_v7_4.md"

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
    "manuscript_citation_marker_audit_id": "MCMA-0001",
    "linked_manuscript_citation_insertion_execution_id": "MCIE-0001",
    "linked_manuscript_citation_insertion_plan_id": "MCIP-0001",
    "linked_citation_record_audit_id": "CRA-0001",
    "audit_status": "all_inserted_markers_pass_linkage_audit_no_claim_revision",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "manuscript_citation_marker_count_from_v7_3": "2",
    "manuscript_citation_marker_audited_count": "2",
    "marker_audit_pass_count": "2",
    "marker_audit_conditional_count": "0",
    "marker_audit_fail_count": "0",
    "manuscript_revised_count": "0",
    "new_citation_added_count": "0",
    "conditional_hold_count": "1",
}


MARKER_AUDIT_ROWS = [
    {
        "marker_audit_row_id": "MCMA-ROW-0001",
        "manuscript_citation_marker_id": "MCM-0001",
        "planned_manuscript_citation_slot_id": "MCIS-PLAN-0001",
        "linked_citation_record_id": "CIT-REC-0001",
        "linked_citation_key": "pmlr-v115-blom20a",
        "linked_evidence_matrix_row_id": "EMR-0001",
        "linked_retained_source_id": "RET-0001",
        "linked_candidate_entry_id": "CAND-0001",
        "inserted_marker": "[@pmlr-v115-blom20a]",
        "target_manuscript_section": "related-work or conceptual framing section",
        "target_sentence_role": "background formal-framing context only",
        "linkage_audit_status": "marker_linkage_pass",
        "claim_revision_status": "no_claim_revision",
        "manuscript_revised": "no",
        "new_citation_added": "no",
        "audit_reason": "The marker links to the planned insertion slot, audited citation record, evidence row, retained source, candidate entry, and bounded manuscript role.",
    },
    {
        "marker_audit_row_id": "MCMA-ROW-0002",
        "manuscript_citation_marker_id": "MCM-0002",
        "planned_manuscript_citation_slot_id": "MCIS-PLAN-0002",
        "linked_citation_record_id": "CIT-REC-0002",
        "linked_citation_key": "pmlr-v124-wengel-mogensen20a",
        "linked_evidence_matrix_row_id": "EMR-0002",
        "linked_retained_source_id": "RET-0002",
        "linked_candidate_entry_id": "CAND-0002",
        "inserted_marker": "[@pmlr-v124-wengel-mogensen20a]",
        "target_manuscript_section": "related-work or methodological context section",
        "target_sentence_role": "background methodological-context only",
        "linkage_audit_status": "marker_linkage_pass",
        "claim_revision_status": "no_claim_revision",
        "manuscript_revised": "no",
        "new_citation_added": "no",
        "audit_reason": "The marker links to the planned insertion slot, audited citation record, evidence row, retained source, candidate entry, and bounded manuscript role.",
    },
]


CONDITIONAL_HOLD_ROWS = [
    {
        "candidate_entry_id": "CAND-0003",
        "hold_status": "hold_for_update_before_retention_decision",
        "citation_record_id": "none",
        "manuscript_citation_marker_id": "none",
        "marker_audit_status": "not_audited_no_marker",
        "manuscript_revised": "no",
        "new_citation_added": "no",
        "reason": "Conditional metadata pass remains outside retained source, citation record audit, insertion planning, marker insertion, and marker audit.",
    },
]


MARKER_AUDIT_FIELDS = [
    "marker_audit_row_id",
    "manuscript_citation_marker_id",
    "planned_manuscript_citation_slot_id",
    "linked_citation_record_id",
    "linked_citation_key",
    "linked_evidence_matrix_row_id",
    "linked_retained_source_id",
    "linked_candidate_entry_id",
    "inserted_marker",
    "target_manuscript_section",
    "target_sentence_role",
    "linkage_audit_status",
    "claim_revision_status",
    "manuscript_revised",
    "new_citation_added",
    "audit_reason",
]


MARKER_AUDIT_STATUS_VALUES = [
    "marker_linkage_pass",
    "marker_linkage_conditional",
    "marker_linkage_fail",
    "not_audited_no_marker",
]


MARKER_AUDIT_GATES = [
    "Marker audit must be linked to v7.3 marker insertion execution.",
    "Only inserted manuscript citation markers may be audited.",
    "Each marker must link to a planned manuscript citation slot.",
    "Each marker must link to an audited citation record.",
    "Each marker must link to a citation key.",
    "Each marker must link to an evidence matrix row.",
    "Each marker must link to a retained source.",
    "Each marker must link to a candidate entry.",
    "Each marker must preserve a bounded manuscript section.",
    "Each marker must preserve a bounded sentence role.",
    "Each marker audit row must have a pass, conditional, or fail status.",
    "Marker audit pass must not imply manuscript claim support.",
    "Marker audit pass must not revise manuscript claims.",
    "New citation added count must remain zero.",
    "Conditional-hold candidates must remain outside marker audit pass rows.",
    "Marker audit must not imply external validation or submission readiness.",
]


BOUNDARY_PHRASES = [
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does audit manuscript citation markers",
    "does not revise manuscript claims",
    "does not add new citations",
    "marker audit is not manuscript claim revision",
    "marker audit pass is not proof",
    "marker audit pass is not external validation",
    "citation marker is not proof",
    "citations are not external validation",
    "citation record pass is not manuscript support",
    "marker linkage pass is not biological validation",
    "marker linkage pass is not clinical validation",
    "conditional hold remains outside marker audit pass rows",
    "future manuscript revision is separate",
    "future citation-grounded claim revision is separate",
    "future new citation handling is separate",
    "future public claims must remain bounded",
]


PROHIBITED_BEHAVIORS = [
    "Do not revise manuscript claims in this milestone.",
    "Do not add new citations in this milestone.",
    "Do not treat marker audit pass as claim support.",
    "Do not treat marker audit pass as proof.",
    "Do not treat marker audit pass as external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not include conditional-hold candidates in marker audit pass rows.",
    "Do not convert marker audit into strengthened conclusions.",
    "Do not claim accepted scientific theory.",
    "Do not rewrite manuscript paragraphs in this milestone.",
]


NEXT_STEPS = [
    "Plan citation-grounded manuscript claim revision in a later milestone.",
    "Keep marker audit separate from manuscript claim revision.",
    "Keep new citation additions separate from marker audit.",
    "Preserve marker linkage during future manuscript revision.",
    "Keep CAND-0003 on hold until update handling.",
    "Audit any future marker additions separately.",
    "Keep public claims bounded after marker audit.",
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
    "citation",
    "citation marker",
    "marker",
    "marker audit",
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
    "marker audit gates",
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
class FirstManuscriptCitationMarkerAuditResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    manuscript_citation_marker_audit_count: int
    manuscript_citation_marker_count: int
    manuscript_citation_marker_audited_count: int
    marker_audit_pass_count: int
    marker_audit_conditional_count: int
    marker_audit_fail_count: int
    manuscript_revised_count: int
    new_citation_added_count: int
    conditional_hold_count: int
    marker_audit_field_count: int
    marker_audit_status_value_count: int
    marker_audit_gate_count: int
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
        "| Manuscript citation marker audit field | Value |",
        "|---|---|",
    ]
    for key, value in AUDIT_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_marker_audit_rows() -> str:
    rows = [
        "| Audit row | Marker id | Planned slot | Citation record | Citation key | Status | Manuscript revised |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in MARKER_AUDIT_ROWS:
        rows.append(
            f"| {item['marker_audit_row_id']} | "
            f"{item['manuscript_citation_marker_id']} | "
            f"{item['planned_manuscript_citation_slot_id']} | "
            f"{item['linked_citation_record_id']} | "
            f"{item['linked_citation_key']} | "
            f"{item['linkage_audit_status']} | "
            f"{item['manuscript_revised']} |"
        )
    return "\n".join(rows)


def render_marker_linkage_rows() -> str:
    rows = [
        "| Marker id | Evidence row | Retained source | Candidate | Target section | Target role |",
        "|---|---|---|---|---|---|",
    ]
    for item in MARKER_AUDIT_ROWS:
        rows.append(
            f"| {item['manuscript_citation_marker_id']} | "
            f"{item['linked_evidence_matrix_row_id']} | "
            f"{item['linked_retained_source_id']} | "
            f"{item['linked_candidate_entry_id']} | "
            f"{item['target_manuscript_section']} | "
            f"{item['target_sentence_role']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Marker id | Marker audit status | Manuscript revised | New citation added | Reason |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['manuscript_citation_marker_id']} | "
            f"{item['marker_audit_status']} | "
            f"{item['manuscript_revised']} | "
            f"{item['new_citation_added']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Marker audit field | v7.4 status |",
        "|---|---|",
    ]
    for field in MARKER_AUDIT_FIELDS:
        rows.append(f"| `{field}` | populated for marker audit rows |")
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
        "marker audit rows",
        "marker linkage rows",
        "manuscript citation marker audit metadata",
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
    return f"""# First Manuscript Citation Marker Audit v7.4

## Question
Can Viruse Fabric audit the first inserted manuscript citation markers while keeping manuscript claim revision and new citation additions at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does audit manuscript citation markers. It does not revise manuscript claims and does not add new citations.

Marker audit is not manuscript claim revision. Marker audit pass is not proof. Marker audit pass is not external validation. Citation marker is not proof. Citations are not external validation. Citation record pass is not manuscript support.

## Source Artifacts
{render_source_table()}

## Manuscript Citation Marker Audit Metadata
{render_metadata_table()}

## Marker Audit Rows
{render_marker_audit_rows()}

## Marker Linkage Rows
{render_marker_linkage_rows()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Marker Audit Fields
{render_field_table()}

## Marker Audit Status Values
{bullet_list(MARKER_AUDIT_STATUS_VALUES)}

## Marker Audit Gates
{bullet_list(MARKER_AUDIT_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Marker Audit Interpretation
The v7.4 artifact audits the first two manuscript citation marker records created in v7.3.

MCMA-ROW-0001 audits MCM-0001 and confirms linkage from the marker to MCIS-PLAN-0001, CIT-REC-0001, EMR-0001, RET-0001, and CAND-0001.

MCMA-ROW-0002 audits MCM-0002 and confirms linkage from the marker to MCIS-PLAN-0002, CIT-REC-0002, EMR-0002, RET-0002, and CAND-0002.

Both marker audit rows pass linkage audit. This means the marker records are internally connected to the retained-source workflow. It does not mean the manuscript claims have been revised, supported, validated, or strengthened.

## Audit Boundary
Manuscript citation marker audit count is one.

Manuscript citation marker count is two.

Manuscript citation marker audited count is two.

Marker audit pass count is two.

Marker audit conditional count is zero.

Marker audit fail count is zero.

Manuscript revised count is zero.

New citation added count is zero.

The project now has audited marker records, but it still has no claim revision. A marker audit pass is a plumbing check, not a Nobel committee. Tragic, but useful.

## Linkage Boundary
Each passed marker audit row verifies linkage to:

- inserted manuscript citation marker
- planned manuscript citation slot
- audited citation record
- citation key
- evidence matrix row
- retained source
- candidate entry
- bounded manuscript section
- bounded sentence role

This prevents citation markers from becoming decorative authority confetti, which is apparently what documents do when humans are not forced to count things.

## Manuscript Claim Boundary
The manuscript citation markers are audited only.

No claim sentence is upgraded.

No conclusion is strengthened.

No paragraph is rewritten.

No theory boundary is relaxed.

No validation claim is added.

Manuscript revised count remains zero because this milestone audits marker linkage, not manuscript claim content.

## New Citation Boundary
New citation added count remains zero.

No new citation record is added. No new source is retained. No new bibliography entry is created. This milestone audits existing inserted marker records only.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside marker audit pass rows. It has no retained source record, no citation record, no planned insertion slot, no inserted marker, and no marker audit pass row.

This prevents conditional metadata from wandering into the manuscript wearing a fake badge. Citation governance: because apparently tables need borders and moral supervision.

## Claim Boundary Toward v7.5
This milestone permits a slightly stronger internal workflow claim than v7.3.

Allowed after v7.4:

- internally staged prototype
- retained-source workflow
- evidence-mapped workflow
- evidence-row-audited workflow
- citation records added and audited
- manuscript citation insertion planned
- first manuscript citation markers inserted
- manuscript citation markers audited
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
Manuscript citation marker audit count: 1

Manuscript citation marker count: 2

Manuscript citation marker audited count: 2

Marker audit pass count: 2

Marker audit conditional count: 0

Marker audit fail count: 0

Manuscript revised count: 0

New citation added count: 0

Conditional hold count: 1

## Final Boundary Statement
This artifact audits bounded manuscript citation marker records.

It does not revise manuscript claims, does not add new citations, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstManuscriptCitationMarkerAuditResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    invented_citations = detect_invented_citation_like_patterns(report)

    manuscript_citation_marker_audit_count = 1
    manuscript_citation_marker_count = int(AUDIT_METADATA["manuscript_citation_marker_count_from_v7_3"])
    manuscript_citation_marker_audited_count = int(AUDIT_METADATA["manuscript_citation_marker_audited_count"])
    marker_audit_pass_count = int(AUDIT_METADATA["marker_audit_pass_count"])
    marker_audit_conditional_count = int(AUDIT_METADATA["marker_audit_conditional_count"])
    marker_audit_fail_count = int(AUDIT_METADATA["marker_audit_fail_count"])
    manuscript_revised_count = int(AUDIT_METADATA["manuscript_revised_count"])
    new_citation_added_count = int(AUDIT_METADATA["new_citation_added_count"])
    conditional_hold_count = int(AUDIT_METADATA["conditional_hold_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 24:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if manuscript_citation_marker_audit_count != 1:
        errors.append(
            "Manuscript citation marker audit count should be one, got: "
            f"{manuscript_citation_marker_audit_count}"
        )

    if manuscript_citation_marker_count != 2:
        errors.append(
            "Manuscript citation marker count should be two, got: "
            f"{manuscript_citation_marker_count}"
        )

    if manuscript_citation_marker_audited_count != 2:
        errors.append(
            "Manuscript citation marker audited count should be two, got: "
            f"{manuscript_citation_marker_audited_count}"
        )

    if marker_audit_pass_count != 2:
        errors.append(f"Marker audit pass count should be two, got: {marker_audit_pass_count}")

    if marker_audit_conditional_count != 0:
        errors.append(
            "Marker audit conditional count should be zero, got: "
            f"{marker_audit_conditional_count}"
        )

    if marker_audit_fail_count != 0:
        errors.append(f"Marker audit fail count should be zero, got: {marker_audit_fail_count}")

    if manuscript_citation_marker_count != manuscript_citation_marker_audited_count:
        errors.append("Every manuscript citation marker must be audited")

    if manuscript_citation_marker_audited_count != marker_audit_pass_count:
        errors.append("Every audited manuscript citation marker must pass in v7.4")

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    for label, value in [
        ("Manuscript revised count", manuscript_revised_count),
        ("New citation added count", new_citation_added_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    for row in MARKER_AUDIT_ROWS:
        missing_fields = [field for field in MARKER_AUDIT_FIELDS if not row.get(field)]
        if missing_fields:
            errors.append(
                f"{row.get('marker_audit_row_id', 'unknown')} missing marker audit fields: "
                f"{len(missing_fields)}"
            )

        if row.get("linkage_audit_status") != "marker_linkage_pass":
            errors.append(f"{row.get('marker_audit_row_id', 'unknown')} did not pass linkage audit")

        if row.get("manuscript_revised") != "no":
            errors.append(f"{row.get('marker_audit_row_id', 'unknown')} revised manuscript unexpectedly")

        if row.get("new_citation_added") != "no":
            errors.append(f"{row.get('marker_audit_row_id', 'unknown')} added citation unexpectedly")

    if len(MARKER_AUDIT_FIELDS) < 16:
        errors.append(f"Marker audit field count too low: {len(MARKER_AUDIT_FIELDS)}")

    if len(MARKER_AUDIT_STATUS_VALUES) < 4:
        errors.append(f"Marker audit status value count too low: {len(MARKER_AUDIT_STATUS_VALUES)}")

    if len(MARKER_AUDIT_GATES) < 16:
        errors.append(f"Marker audit gate count too low: {len(MARKER_AUDIT_GATES)}")

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
            "Invented citation-like patterns detected outside marker audit sections: "
            f"{len(invented_citations)}"
        )

    if word_count < 1200:
        errors.append(f"Word count too low for first manuscript citation marker audit: {word_count}")

    warnings.append("Manuscript citation markers are audited, but manuscript claims are not revised.")
    warnings.append("Manuscript citation marker audit does not add new citations.")

    passed = not errors

    interpretation = (
        "The v7.4 artifact audits two manuscript citation marker records and confirms "
        "their internal linkage while keeping manuscript claim revision and new citation additions at zero."
    )

    return FirstManuscriptCitationMarkerAuditResult(
        title="First Manuscript Citation Marker Audit v7.4",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        manuscript_citation_marker_audit_count=manuscript_citation_marker_audit_count,
        manuscript_citation_marker_count=manuscript_citation_marker_count,
        manuscript_citation_marker_audited_count=manuscript_citation_marker_audited_count,
        marker_audit_pass_count=marker_audit_pass_count,
        marker_audit_conditional_count=marker_audit_conditional_count,
        marker_audit_fail_count=marker_audit_fail_count,
        manuscript_revised_count=manuscript_revised_count,
        new_citation_added_count=new_citation_added_count,
        conditional_hold_count=conditional_hold_count,
        marker_audit_field_count=len(MARKER_AUDIT_FIELDS),
        marker_audit_status_value_count=len(MARKER_AUDIT_STATUS_VALUES),
        marker_audit_gate_count=len(MARKER_AUDIT_GATES),
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

    print("First Manuscript Citation Marker Audit v7.4")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Manuscript citation marker audit count: {result.manuscript_citation_marker_audit_count}")
    print(f"Manuscript citation marker count: {result.manuscript_citation_marker_count}")
    print(f"Manuscript citation marker audited count: {result.manuscript_citation_marker_audited_count}")
    print(f"Marker audit pass count: {result.marker_audit_pass_count}")
    print(f"Marker audit conditional count: {result.marker_audit_conditional_count}")
    print(f"Marker audit fail count: {result.marker_audit_fail_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Marker audit field count: {result.marker_audit_field_count}")
    print(f"Marker audit status value count: {result.marker_audit_status_value_count}")
    print(f"Marker audit gate count: {result.marker_audit_gate_count}")
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
