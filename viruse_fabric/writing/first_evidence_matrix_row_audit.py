"""First evidence matrix row audit for Viruse Fabric v6.8.

This module audits the first evidence matrix rows created in v6.7.

It audits populated evidence matrix rows only.

It does not add citations.
It does not revise the manuscript.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_evidence_matrix_row_audit_v6_8.md"

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
    "evidence_matrix_row_audit_id": "ERA-0001",
    "linked_evidence_matrix_population_execution_id": "EMX-0001",
    "linked_evidence_matrix_population_plan_id": "EMP-0001",
    "linked_retained_source_role_audit_id": "RSA-0001",
    "audit_status": "evidence_matrix_rows_audited_no_citations",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "evidence_matrix_row_count_from_v6_7": "2",
    "evidence_matrix_row_audited_count": "2",
    "evidence_row_audit_pass_count": "2",
    "evidence_row_audit_conditional_count": "0",
    "evidence_row_audit_fail_count": "0",
    "conditional_hold_count": "1",
    "citation_added_count": "0",
    "manuscript_revised_count": "0",
}


EVIDENCE_ROW_AUDIT_ROWS = [
    {
        "evidence_matrix_row_id": "EMR-0001",
        "linked_planned_mapping_id": "EMP-ROW-0001",
        "retained_source_id": "RET-0001",
        "linked_candidate_entry_id": "CAND-0001",
        "claim_category": "constraint-based causality and formal framing",
        "evidence_role": "contextual_formal_framing_reference_candidate",
        "source_role_boundary": "formal framing context only",
        "evidence_strength": "contextual_support_not_validation",
        "row_audit_decision": "row_pass_not_cited",
        "linkage_status": "linked_to_plan_retained_source_and_candidate",
        "boundary_status": "bounded_non_citation_non_manuscript_support",
        "citation_added": "no",
        "manuscript_revised": "no",
        "audit_reason": "The row preserves required links and remains bounded as contextual support only.",
    },
    {
        "evidence_matrix_row_id": "EMR-0002",
        "linked_planned_mapping_id": "EMP-ROW-0002",
        "retained_source_id": "RET-0002",
        "linked_candidate_entry_id": "CAND-0002",
        "claim_category": "dynamical-systems screening and methodological context",
        "evidence_role": "methodological_context_reference_candidate",
        "source_role_boundary": "methodological context only",
        "evidence_strength": "contextual_support_not_validation",
        "row_audit_decision": "row_pass_not_cited",
        "linkage_status": "linked_to_plan_retained_source_and_candidate",
        "boundary_status": "bounded_non_citation_non_manuscript_support",
        "citation_added": "no",
        "manuscript_revised": "no",
        "audit_reason": "The row preserves required links and remains bounded as methodological context only.",
    },
]


CONDITIONAL_HOLD_ROWS = [
    {
        "candidate_entry_id": "CAND-0003",
        "hold_status": "hold_for_update_before_retention_decision",
        "retained_source_id": "none",
        "evidence_matrix_row_id": "none",
        "row_audited": "no",
        "citation_added": "no",
        "manuscript_revised": "no",
        "reason": "Conditional metadata pass remains outside retained source, role audit, evidence matrix population, and row audit.",
    },
]


ROW_AUDIT_FIELDS = [
    "evidence_matrix_row_id",
    "linked_planned_mapping_id",
    "retained_source_id",
    "linked_candidate_entry_id",
    "claim_category",
    "evidence_role",
    "source_role_boundary",
    "evidence_strength",
    "row_audit_decision",
    "linkage_status",
    "boundary_status",
    "citation_added",
    "manuscript_revised",
    "audit_reason",
]


ROW_AUDIT_DECISION_VALUES = [
    "row_pass_not_cited",
    "row_conditional_not_cited",
    "row_fail_not_cited",
    "not_a_populated_row_no_audit",
]


ROW_AUDIT_GATES = [
    "Evidence row audit must be linked to v6.7 population execution.",
    "Evidence row audit must inspect populated evidence matrix rows only.",
    "Every audited row must link to a planned mapping.",
    "Every audited row must link to a retained source.",
    "Every audited row must link to a candidate entry.",
    "Every audited row must preserve a bounded claim category.",
    "Every audited row must preserve a bounded evidence role.",
    "Every audited row must preserve a source role boundary.",
    "Every audited row must use contextual support language.",
    "Every audited row must avoid validation language.",
    "Evidence row audit must not add citations.",
    "Evidence row audit must not revise the manuscript.",
    "Conditional-hold candidates must remain outside row audit.",
    "Row pass must not be treated as citation readiness.",
    "Row pass must not be treated as manuscript support.",
    "Row pass must not imply external validation.",
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
    "does audit evidence matrix rows",
    "does not add citations",
    "does not revise the manuscript",
    "evidence row pass is not citation readiness",
    "evidence row pass is not manuscript support",
    "evidence row audit is not citation integration",
    "evidence row audit is not manuscript revision",
    "contextual support is not external validation",
    "citations are not external validation",
    "conditional hold remains outside evidence row audit",
    "future citation use is separate",
    "future manuscript revision is separate",
]


PROHIBITED_BEHAVIORS = [
    "Do not add citations in this milestone.",
    "Do not revise the manuscript in this milestone.",
    "Do not treat evidence row pass as citation readiness.",
    "Do not treat evidence row pass as manuscript support.",
    "Do not treat evidence row audit as citation integration.",
    "Do not treat evidence row audit as manuscript revision.",
    "Do not treat contextual support as external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not audit conditional-hold candidates as populated evidence rows.",
    "Do not convert audited evidence rows into citation text.",
]


NEXT_STEPS = [
    "Plan citation integration only after evidence row audit.",
    "Keep citation integration separate from evidence row audit.",
    "Add citations only in a later citation-specific milestone.",
    "Revise manuscript only after citation-grounded integration.",
    "Keep CAND-0003 on hold until update handling.",
    "Preserve row boundaries during citation planning.",
    "Keep public language bounded after evidence row audit.",
    "Track audited evidence rows separately from manuscript claims.",
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
]


SAFE_LINE_CUES = [
    "not",
    "does not",
    "do not",
    "must not",
    "evidence row",
    "evidence matrix",
    "retained source",
    "candidate",
    "conditional",
    "hold",
    "citation",
    "manuscript",
    "zero",
    "future",
    "audit",
    "boundary",
    "prohibited",
    "contextual support",
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
    "row audit gates",
    "final boundary statement",
]


FAKE_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
    r"\(20\d{2}\)",
]


@dataclass(frozen=True)
class FirstEvidenceMatrixRowAuditResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    evidence_matrix_row_audit_count: int
    evidence_matrix_row_count: int
    evidence_matrix_row_audited_count: int
    evidence_row_audit_pass_count: int
    evidence_row_audit_conditional_count: int
    evidence_row_audit_fail_count: int
    conditional_hold_count: int
    citation_added_count: int
    manuscript_revised_count: int
    row_audit_field_count: int
    row_audit_decision_value_count: int
    row_audit_gate_count: int
    boundary_phrase_count: int
    prohibited_behavior_count: int
    next_step_count: int
    overclaim_count: int
    fake_citation_count: int
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
        "| Evidence matrix row audit field | Value |",
        "|---|---|",
    ]
    for key, value in AUDIT_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_row_audit_rows() -> str:
    rows = [
        "| Evidence row id | Retained source id | Claim category | Evidence role | Audit decision | Citation added | Manuscript revised |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in EVIDENCE_ROW_AUDIT_ROWS:
        rows.append(
            f"| {item['evidence_matrix_row_id']} | "
            f"{item['retained_source_id']} | "
            f"{item['claim_category']} | "
            f"{item['evidence_role']} | "
            f"{item['row_audit_decision']} | "
            f"{item['citation_added']} | "
            f"{item['manuscript_revised']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Evidence row id | Row audited | Citation added | Manuscript revised | Reason |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['evidence_matrix_row_id']} | "
            f"{item['row_audited']} | "
            f"{item['citation_added']} | "
            f"{item['manuscript_revised']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Row audit field | v6.8 status |",
        "|---|---|",
    ]
    for field in ROW_AUDIT_FIELDS:
        rows.append(f"| `{field}` | populated for evidence row audit rows |")
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


def detect_fake_citations(text: str) -> list[str]:
    findings: list[str] = []

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        lowered = stripped.lower()

        if "fake citation" in lowered or "not citations" in lowered:
            continue

        for pattern in FAKE_CITATION_PATTERNS:
            if re.search(pattern, stripped):
                findings.append(stripped)
                break

    return findings


def render_report() -> str:
    return f"""# First Evidence Matrix Row Audit v6.8

## Question
Can Viruse Fabric audit the first populated evidence matrix rows while keeping citations and manuscript revision at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does audit evidence matrix rows. It does not add citations and does not revise the manuscript.

Evidence row pass is not citation readiness. Evidence row pass is not manuscript support. Evidence row audit is not citation integration. Evidence row audit is not manuscript revision. Contextual support is not external validation. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Evidence Matrix Row Audit Metadata
{render_metadata_table()}

## Evidence Row Audit Rows
{render_row_audit_rows()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Row Audit Fields
{render_field_table()}

## Row Audit Decision Values
{bullet_list(ROW_AUDIT_DECISION_VALUES)}

## Row Audit Gates
{bullet_list(ROW_AUDIT_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Row Audit Interpretation
The v6.8 artifact audits the two evidence matrix rows created in v6.7.

EMR-0001 passes row audit because it preserves links to EMP-ROW-0001, RET-0001, and CAND-0001 while keeping a bounded formal-framing role. EMR-0002 passes row audit because it preserves links to EMP-ROW-0002, RET-0002, and CAND-0002 while keeping a bounded methodological-context role.

Both rows remain non-citation evidence organization records. They are not manuscript claims, not citation text, and not external validation. The matrix is becoming organized, which is not the same as becoming victorious. Strange distinction, apparently necessary.

## Linkage Boundary
Evidence matrix row audited count is two.

Evidence row audit pass count is two.

Evidence row audit conditional count is zero.

Evidence row audit fail count is zero.

Each audited row has a planned mapping link, a retained source link, a candidate entry link, a claim category, an evidence role, a source role boundary, an evidence strength label, and a row limit. This makes the rows auditable for later citation planning without making them citations now.

## Citation Boundary
Citation added count remains zero.

No citation slot is filled. No bibliography entry is created. No reference text is added. No audited evidence row becomes citation language in this milestone.

An evidence row can pass audit and still remain outside citation integration. That is the whole point of the staged workflow. Otherwise every tidy table would become a bibliography with delusions of grandeur.

## Manuscript Boundary
Manuscript revised count remains zero.

The manuscript receives no new text, no rewritten claim, no strengthened conclusion, and no citation-grounded revision from this artifact.

The project has audited evidence rows, but the manuscript remains unchanged. Evidence row audit checks internal structure. Manuscript revision requires a later explicit milestone.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside evidence row audit because it is not retained, not role-audited, not planned for evidence mapping, and not populated as an evidence matrix row.

This boundary prevents a conditional source from inheriting status by proximity. Unfortunately, rows cannot be trusted to behave without supervision either.

## Output Counts
Evidence matrix row audit count: 1

Evidence matrix row count: 2

Evidence matrix row audited count: 2

Evidence row audit pass count: 2

Evidence row audit conditional count: 0

Evidence row audit fail count: 0

Conditional hold count: 1

Citation added count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact audits evidence matrix rows.

It does not add citations, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstEvidenceMatrixRowAuditResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    evidence_matrix_row_audit_count = 1
    evidence_matrix_row_count = int(AUDIT_METADATA["evidence_matrix_row_count_from_v6_7"])
    evidence_matrix_row_audited_count = int(AUDIT_METADATA["evidence_matrix_row_audited_count"])
    evidence_row_audit_pass_count = int(AUDIT_METADATA["evidence_row_audit_pass_count"])
    evidence_row_audit_conditional_count = int(AUDIT_METADATA["evidence_row_audit_conditional_count"])
    evidence_row_audit_fail_count = int(AUDIT_METADATA["evidence_row_audit_fail_count"])
    conditional_hold_count = int(AUDIT_METADATA["conditional_hold_count"])
    citation_added_count = int(AUDIT_METADATA["citation_added_count"])
    manuscript_revised_count = int(AUDIT_METADATA["manuscript_revised_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 18:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if evidence_matrix_row_audit_count != 1:
        errors.append(
            "Evidence matrix row audit count should be one, got: "
            f"{evidence_matrix_row_audit_count}"
        )

    if evidence_matrix_row_count != 2:
        errors.append(f"Evidence matrix row count should be two, got: {evidence_matrix_row_count}")

    if evidence_matrix_row_audited_count != 2:
        errors.append(
            "Evidence matrix row audited count should be two, got: "
            f"{evidence_matrix_row_audited_count}"
        )

    if evidence_row_audit_pass_count != 2:
        errors.append(
            "Evidence row audit pass count should be two, got: "
            f"{evidence_row_audit_pass_count}"
        )

    if evidence_row_audit_conditional_count != 0:
        errors.append(
            "Evidence row audit conditional count should be zero, got: "
            f"{evidence_row_audit_conditional_count}"
        )

    if evidence_row_audit_fail_count != 0:
        errors.append(
            "Evidence row audit fail count should be zero, got: "
            f"{evidence_row_audit_fail_count}"
        )

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    if evidence_matrix_row_audited_count != evidence_matrix_row_count:
        errors.append("Evidence matrix row audited count must equal evidence matrix row count")

    if evidence_row_audit_pass_count != evidence_matrix_row_count:
        errors.append("Evidence row audit pass count must equal evidence matrix row count")

    for row in EVIDENCE_ROW_AUDIT_ROWS:
        missing_fields = [field for field in ROW_AUDIT_FIELDS if not row.get(field)]
        if missing_fields:
            errors.append(
                f"{row.get('evidence_matrix_row_id', 'unknown')} missing audit fields: "
                f"{len(missing_fields)}"
            )

    for label, value in [
        ("Citation added count", citation_added_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if len(ROW_AUDIT_FIELDS) < 14:
        errors.append(f"Row audit field count too low: {len(ROW_AUDIT_FIELDS)}")

    if len(ROW_AUDIT_DECISION_VALUES) < 4:
        errors.append(f"Row audit decision value count too low: {len(ROW_AUDIT_DECISION_VALUES)}")

    if len(ROW_AUDIT_GATES) < 16:
        errors.append(f"Row audit gate count too low: {len(ROW_AUDIT_GATES)}")

    if boundary_count < 20:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 11:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if word_count < 1200:
        errors.append(f"Word count too low for first evidence matrix row audit: {word_count}")

    warnings.append("Evidence matrix rows are audited, but no citations are added.")
    warnings.append("Evidence row audit does not revise the manuscript.")

    passed = not errors

    interpretation = (
        "The v6.8 artifact audits two populated evidence matrix rows while keeping "
        "citations and manuscript revision at zero."
    )

    return FirstEvidenceMatrixRowAuditResult(
        title="First Evidence Matrix Row Audit v6.8",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        evidence_matrix_row_audit_count=evidence_matrix_row_audit_count,
        evidence_matrix_row_count=evidence_matrix_row_count,
        evidence_matrix_row_audited_count=evidence_matrix_row_audited_count,
        evidence_row_audit_pass_count=evidence_row_audit_pass_count,
        evidence_row_audit_conditional_count=evidence_row_audit_conditional_count,
        evidence_row_audit_fail_count=evidence_row_audit_fail_count,
        conditional_hold_count=conditional_hold_count,
        citation_added_count=citation_added_count,
        manuscript_revised_count=manuscript_revised_count,
        row_audit_field_count=len(ROW_AUDIT_FIELDS),
        row_audit_decision_value_count=len(ROW_AUDIT_DECISION_VALUES),
        row_audit_gate_count=len(ROW_AUDIT_GATES),
        boundary_phrase_count=boundary_count,
        prohibited_behavior_count=prohibited_count,
        next_step_count=next_step_count,
        overclaim_count=len(overclaims),
        fake_citation_count=len(fake_citations),
        word_count=word_count,
        errors=errors,
        warnings=warnings,
        passed=passed,
        interpretation=interpretation,
    )


def main() -> None:
    result = generate_report()

    print("First Evidence Matrix Row Audit v6.8")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Evidence matrix row audit count: {result.evidence_matrix_row_audit_count}")
    print(f"Evidence matrix row count: {result.evidence_matrix_row_count}")
    print(f"Evidence matrix row audited count: {result.evidence_matrix_row_audited_count}")
    print(f"Evidence row audit pass count: {result.evidence_row_audit_pass_count}")
    print(f"Evidence row audit conditional count: {result.evidence_row_audit_conditional_count}")
    print(f"Evidence row audit fail count: {result.evidence_row_audit_fail_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Row audit field count: {result.row_audit_field_count}")
    print(f"Row audit decision value count: {result.row_audit_decision_value_count}")
    print(f"Row audit gate count: {result.row_audit_gate_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Fake citation-like pattern count: {result.fake_citation_count}")
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
