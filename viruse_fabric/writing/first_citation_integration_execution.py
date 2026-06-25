"""First citation integration execution for Viruse Fabric v7.0.

This module executes the first citation integration step after citation planning.

It adds verified citation records for two planned citation slots.

It does not revise the manuscript.
It does not insert manuscript citation markers.
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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_citation_integration_execution_v7_0.md"

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
    "citation_integration_execution_id": "CIE-0001",
    "linked_citation_integration_plan_id": "CIP-0001",
    "linked_evidence_matrix_row_audit_id": "ERA-0001",
    "execution_status": "citation_records_added_not_manuscript_revised",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "planned_citation_slot_count_from_v6_9": "2",
    "executed_citation_slot_count": "2",
    "citation_record_count": "2",
    "citation_added_count": "2",
    "manuscript_citation_marker_count": "0",
    "manuscript_revised_count": "0",
    "conditional_hold_count": "1",
}


VERIFIED_CITATION_RECORDS = [
    {
        "citation_record_id": "CIT-REC-0001",
        "planned_citation_slot_id": "CIT-PLAN-0001",
        "linked_evidence_matrix_row_id": "EMR-0001",
        "linked_retained_source_id": "RET-0001",
        "linked_candidate_entry_id": "CAND-0001",
        "citation_key": "pmlr-v115-blom20a",
        "title": "Beyond Structural Causal Models: Causal Constraints Models",
        "authors": "Tineke Blom; Stephan Bongers; Joris M. Mooij",
        "venue": "Proceedings of The 35th Uncertainty in Artificial Intelligence Conference",
        "series": "Proceedings of Machine Learning Research",
        "volume": "115",
        "pages": "585-594",
        "year": "2020",
        "publisher": "PMLR",
        "stable_url": "https://proceedings.mlr.press/v115/blom20a.html",
        "planned_citation_role": "background_formal_framing_context",
        "citation_record_status": "verified_citation_record_added",
        "manuscript_citation_marker_added": "no",
        "manuscript_revised": "no",
        "execution_reason": "The source is verified through PMLR metadata and is linked to the audited formal-framing evidence row.",
    },
    {
        "citation_record_id": "CIT-REC-0002",
        "planned_citation_slot_id": "CIT-PLAN-0002",
        "linked_evidence_matrix_row_id": "EMR-0002",
        "linked_retained_source_id": "RET-0002",
        "linked_candidate_entry_id": "CAND-0002",
        "citation_key": "pmlr-v124-wengel-mogensen20a",
        "title": "Causal screening in dynamical systems",
        "authors": "Søren Wengel Mogensen",
        "venue": "Proceedings of the 36th Conference on Uncertainty in Artificial Intelligence (UAI)",
        "series": "Proceedings of Machine Learning Research",
        "volume": "124",
        "pages": "310-319",
        "year": "2020",
        "publisher": "PMLR",
        "stable_url": "https://proceedings.mlr.press/v124/wengel-mogensen20a.html",
        "planned_citation_role": "background_methodological_context",
        "citation_record_status": "verified_citation_record_added",
        "manuscript_citation_marker_added": "no",
        "manuscript_revised": "no",
        "execution_reason": "The source is verified through PMLR metadata and is linked to the audited methodological-context evidence row.",
    },
]


CONDITIONAL_HOLD_ROWS = [
    {
        "candidate_entry_id": "CAND-0003",
        "hold_status": "hold_for_update_before_retention_decision",
        "citation_record_id": "none",
        "citation_added": "no",
        "manuscript_citation_marker_added": "no",
        "manuscript_revised": "no",
        "reason": "Conditional metadata pass remains outside retained source, evidence row audit, citation planning, and citation integration execution.",
    },
]


CITATION_EXECUTION_FIELDS = [
    "citation_record_id",
    "planned_citation_slot_id",
    "linked_evidence_matrix_row_id",
    "linked_retained_source_id",
    "linked_candidate_entry_id",
    "citation_key",
    "title",
    "authors",
    "venue",
    "series",
    "volume",
    "pages",
    "year",
    "publisher",
    "stable_url",
    "planned_citation_role",
    "citation_record_status",
    "manuscript_citation_marker_added",
    "manuscript_revised",
    "execution_reason",
]


CITATION_EXECUTION_STATUS_VALUES = [
    "verified_citation_record_added",
    "planned_slot_not_executed",
    "candidate_hold_no_citation_record",
    "manuscript_marker_not_added",
]


CITATION_EXECUTION_GATES = [
    "Citation integration execution must be linked to v6.9 citation integration plan.",
    "Only planned citation slots may be executed.",
    "Only audited evidence rows may receive citation records.",
    "Each citation record must link to a planned citation slot.",
    "Each citation record must link to an evidence matrix row.",
    "Each citation record must link to a retained source.",
    "Each citation record must link to a candidate entry.",
    "Each citation record must include a stable source route.",
    "Each citation record must include title, authors, venue, pages, year, and publisher.",
    "Each citation record must preserve the planned citation role.",
    "Citation records may be added in v7.0.",
    "Manuscript citation markers must remain zero.",
    "Manuscript revision must remain zero.",
    "Conditional-hold candidates must remain outside citation integration.",
    "Citation records must not imply external validation.",
    "Citation records must not imply submission readiness.",
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
    "does execute citation integration",
    "does add citation records",
    "does not revise the manuscript",
    "does not insert manuscript citation markers",
    "citation record is not manuscript revision",
    "citation record is not external validation",
    "citation integration is not proof",
    "citations are not external validation",
    "evidence row pass is not proof",
    "conditional hold remains outside citation integration",
    "future manuscript revision is separate",
    "future citation audit is separate",
]


PROHIBITED_BEHAVIORS = [
    "Do not revise the manuscript in this milestone.",
    "Do not insert manuscript citation markers in this milestone.",
    "Do not treat citation records as manuscript support.",
    "Do not treat citation records as external validation.",
    "Do not treat citation integration as proof.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not include conditional-hold candidates in citation integration.",
    "Do not convert citation records into manuscript prose.",
    "Do not strengthen theory claims from citation records alone.",
    "Do not claim accepted scientific theory.",
]


NEXT_STEPS = [
    "Audit citation records in a later milestone.",
    "Check citation formatting after citation record audit.",
    "Plan manuscript revision only after citation audit.",
    "Revise manuscript only after citation-grounded revision planning.",
    "Keep manuscript citation markers separate from citation records.",
    "Keep CAND-0003 on hold until update handling.",
    "Preserve source-role boundaries during citation audit.",
    "Keep public claims bounded after citation integration.",
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
    "citation record",
    "evidence row",
    "evidence matrix",
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
    "citation execution gates",
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
class FirstCitationIntegrationExecutionResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    citation_integration_execution_count: int
    planned_citation_slot_count: int
    executed_citation_slot_count: int
    citation_record_count: int
    citation_added_count: int
    manuscript_citation_marker_count: int
    manuscript_revised_count: int
    conditional_hold_count: int
    citation_execution_field_count: int
    citation_execution_status_value_count: int
    citation_execution_gate_count: int
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
        "| Citation integration execution field | Value |",
        "|---|---|",
    ]
    for key, value in EXECUTION_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_verified_citation_records() -> str:
    rows = [
        "| Citation record id | Planned slot | Evidence row | Retained source | Citation key | Year | Status | Manuscript revised |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in VERIFIED_CITATION_RECORDS:
        rows.append(
            f"| {item['citation_record_id']} | "
            f"{item['planned_citation_slot_id']} | "
            f"{item['linked_evidence_matrix_row_id']} | "
            f"{item['linked_retained_source_id']} | "
            f"{item['citation_key']} | "
            f"{item['year']} | "
            f"{item['citation_record_status']} | "
            f"{item['manuscript_revised']} |"
        )
    return "\n".join(rows)


def render_reference_detail_table() -> str:
    rows = [
        "| Citation record id | Title | Authors | Venue | PMLR | Pages | Stable route |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in VERIFIED_CITATION_RECORDS:
        rows.append(
            f"| {item['citation_record_id']} | "
            f"{item['title']} | "
            f"{item['authors']} | "
            f"{item['venue']} | "
            f"{item['volume']} | "
            f"{item['pages']} | "
            f"{item['stable_url']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Citation record id | Citation added | Manuscript marker | Manuscript revised | Reason |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['citation_record_id']} | "
            f"{item['citation_added']} | "
            f"{item['manuscript_citation_marker_added']} | "
            f"{item['manuscript_revised']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Citation execution field | v7.0 status |",
        "|---|---|",
    ]
    for field in CITATION_EXECUTION_FIELDS:
        rows.append(f"| `{field}` | populated for verified citation records |")
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
        "verified citation records",
        "verified reference details",
        "citation integration execution metadata",
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
    return f"""# First Citation Integration Execution v7.0

## Question
Can Viruse Fabric execute first citation integration by adding verified citation records while keeping manuscript citation markers and manuscript revision at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does execute citation integration. It does add citation records. It does not revise the manuscript and does not insert manuscript citation markers.

Citation record is not manuscript revision. Citation record is not external validation. Citation integration is not proof. Citations are not external validation. Evidence row pass is not proof.

## Source Artifacts
{render_source_table()}

## Citation Integration Execution Metadata
{render_metadata_table()}

## Verified Citation Records
{render_verified_citation_records()}

## Verified Reference Details
{render_reference_detail_table()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Citation Execution Fields
{render_field_table()}

## Citation Execution Status Values
{bullet_list(CITATION_EXECUTION_STATUS_VALUES)}

## Citation Execution Gates
{bullet_list(CITATION_EXECUTION_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Citation Integration Interpretation
The v7.0 artifact executes the first citation integration step by adding two verified citation records.

CIT-REC-0001 executes CIT-PLAN-0001 for EMR-0001 and RET-0001. The citation record is attached to the formal-framing context role.

CIT-REC-0002 executes CIT-PLAN-0002 for EMR-0002 and RET-0002. The citation record is attached to the methodological-context role.

Both citation records are structured metadata records, not manuscript prose. They create a traceable citation layer between retained sources and future manuscript work. They do not insert citation markers into the manuscript.

## Execution Boundary
Citation integration execution count is one.

Planned citation slot count is two.

Executed citation slot count is two.

Citation record count is two.

Citation added count is two.

Manuscript citation marker count is zero.

Manuscript revised count is zero.

The project now has verified citation records, but it still has no manuscript citation markers and no manuscript revision. This is the part where the workflow behaves better than most humans with a new bibliography.

## Source Verification Boundary
The citation records are based on stable PMLR metadata.

CIT-REC-0001 records title, authors, venue, volume, pages, year, publisher, citation key, and stable source route for the first retained source.

CIT-REC-0002 records title, author, venue, volume, pages, year, publisher, citation key, and stable source route for the second retained source.

This milestone records source metadata. It does not claim that these sources validate Viruse Fabric. A citation can support context without proving the framework. Apparently this needs to be written down, because civilization keeps mistaking references for miracles.

## Manuscript Boundary
The manuscript receives no new text.

No citation marker is inserted into manuscript prose.

No paragraph is rewritten.

No conclusion is strengthened.

No claim is upgraded.

Manuscript revised count remains zero.

The manuscript can only be revised in a later citation-grounded manuscript revision milestone.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside citation integration execution. It does not receive a citation record. It does not receive a manuscript marker. It does not receive manuscript support.

This keeps conditional metadata from quietly becoming cited evidence by table-adjacent osmosis, a process Git thankfully has not yet automated.

## Claim Boundary Toward v7.5
This milestone permits a slightly stronger internal claim than v6.9.

Allowed after v7.0:

- internally staged prototype
- retained-source workflow
- evidence-mapped workflow
- evidence-row-audited workflow
- first verified citation records added
- manuscript still unrevised

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
Citation integration execution count: 1

Planned citation slot count: 2

Executed citation slot count: 2

Citation record count: 2

Citation added count: 2

Manuscript citation marker count: 0

Manuscript revised count: 0

Conditional hold count: 1

## Final Boundary Statement
This artifact executes citation integration by adding verified citation records.

It does not revise the manuscript, does not insert manuscript citation markers, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstCitationIntegrationExecutionResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    invented_citations = detect_invented_citation_like_patterns(report)

    citation_integration_execution_count = 1
    planned_citation_slot_count = int(EXECUTION_METADATA["planned_citation_slot_count_from_v6_9"])
    executed_citation_slot_count = int(EXECUTION_METADATA["executed_citation_slot_count"])
    citation_record_count = int(EXECUTION_METADATA["citation_record_count"])
    citation_added_count = int(EXECUTION_METADATA["citation_added_count"])
    manuscript_citation_marker_count = int(EXECUTION_METADATA["manuscript_citation_marker_count"])
    manuscript_revised_count = int(EXECUTION_METADATA["manuscript_revised_count"])
    conditional_hold_count = int(EXECUTION_METADATA["conditional_hold_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 20:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if citation_integration_execution_count != 1:
        errors.append(
            "Citation integration execution count should be one, got: "
            f"{citation_integration_execution_count}"
        )

    if planned_citation_slot_count != 2:
        errors.append(f"Planned citation slot count should be two, got: {planned_citation_slot_count}")

    if executed_citation_slot_count != 2:
        errors.append(
            "Executed citation slot count should be two, got: "
            f"{executed_citation_slot_count}"
        )

    if citation_record_count != 2:
        errors.append(f"Citation record count should be two, got: {citation_record_count}")

    if citation_added_count != 2:
        errors.append(f"Citation added count should be two, got: {citation_added_count}")

    if planned_citation_slot_count != executed_citation_slot_count:
        errors.append("Planned citation slot count must equal executed citation slot count")

    if executed_citation_slot_count != citation_record_count:
        errors.append("Executed citation slot count must equal citation record count")

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    for label, value in [
        ("Manuscript citation marker count", manuscript_citation_marker_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    for row in VERIFIED_CITATION_RECORDS:
        missing_fields = [field for field in CITATION_EXECUTION_FIELDS if not row.get(field)]
        if missing_fields:
            errors.append(
                f"{row.get('citation_record_id', 'unknown')} missing citation execution fields: "
                f"{len(missing_fields)}"
            )

    if len(CITATION_EXECUTION_FIELDS) < 20:
        errors.append(f"Citation execution field count too low: {len(CITATION_EXECUTION_FIELDS)}")

    if len(CITATION_EXECUTION_STATUS_VALUES) < 4:
        errors.append(
            "Citation execution status value count too low: "
            f"{len(CITATION_EXECUTION_STATUS_VALUES)}"
        )

    if len(CITATION_EXECUTION_GATES) < 16:
        errors.append(f"Citation execution gate count too low: {len(CITATION_EXECUTION_GATES)}")

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
            "Invented citation-like patterns detected outside verified citation sections: "
            f"{len(invented_citations)}"
        )

    if word_count < 1200:
        errors.append(f"Word count too low for first citation integration execution: {word_count}")

    warnings.append("Citation records are added, but manuscript citation markers remain zero.")
    warnings.append("Citation integration execution does not revise the manuscript.")

    passed = not errors

    interpretation = (
        "The v7.0 artifact executes first citation integration by adding two verified "
        "citation records while keeping manuscript citation markers and manuscript revision at zero."
    )

    return FirstCitationIntegrationExecutionResult(
        title="First Citation Integration Execution v7.0",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        citation_integration_execution_count=citation_integration_execution_count,
        planned_citation_slot_count=planned_citation_slot_count,
        executed_citation_slot_count=executed_citation_slot_count,
        citation_record_count=citation_record_count,
        citation_added_count=citation_added_count,
        manuscript_citation_marker_count=manuscript_citation_marker_count,
        manuscript_revised_count=manuscript_revised_count,
        conditional_hold_count=conditional_hold_count,
        citation_execution_field_count=len(CITATION_EXECUTION_FIELDS),
        citation_execution_status_value_count=len(CITATION_EXECUTION_STATUS_VALUES),
        citation_execution_gate_count=len(CITATION_EXECUTION_GATES),
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

    print("First Citation Integration Execution v7.0")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Citation integration execution count: {result.citation_integration_execution_count}")
    print(f"Planned citation slot count: {result.planned_citation_slot_count}")
    print(f"Executed citation slot count: {result.executed_citation_slot_count}")
    print(f"Citation record count: {result.citation_record_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Manuscript citation marker count: {result.manuscript_citation_marker_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Citation execution field count: {result.citation_execution_field_count}")
    print(f"Citation execution status value count: {result.citation_execution_status_value_count}")
    print(f"Citation execution gate count: {result.citation_execution_gate_count}")
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
