"""First evidence matrix population execution for Viruse Fabric v6.7.

This module executes the first evidence matrix population after the v6.6
evidence matrix population plan.

It creates evidence matrix rows only.

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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_evidence_matrix_population_execution_v6_7.md"

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
    "evidence_matrix_population_execution_id": "EMX-0001",
    "linked_evidence_matrix_population_plan_id": "EMP-0001",
    "linked_retained_source_role_audit_id": "RSA-0001",
    "linked_retention_execution_id": "RDE-0001",
    "execution_status": "evidence_matrix_rows_populated_no_citations",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "retained_source_count_from_v6_6": "2",
    "planned_evidence_mapping_count_from_v6_6": "2",
    "evidence_matrix_population_execution_count": "1",
    "evidence_matrix_populated_count": "2",
    "evidence_matrix_row_count": "2",
    "conditional_hold_count": "1",
    "citation_added_count": "0",
    "manuscript_revised_count": "0",
}


EVIDENCE_MATRIX_ROWS = [
    {
        "evidence_matrix_row_id": "EMR-0001",
        "linked_planned_mapping_id": "EMP-ROW-0001",
        "retained_source_id": "RET-0001",
        "linked_candidate_entry_id": "CAND-0001",
        "claim_category": "constraint-based causality and formal framing",
        "evidence_role": "contextual_formal_framing_reference_candidate",
        "source_role_boundary": "formal framing context only",
        "evidence_strength": "contextual_support_not_validation",
        "matrix_population_decision": "populated_not_cited",
        "citation_added": "no",
        "manuscript_revised": "no",
        "row_limit": "Evidence matrix row only; not citation text and not manuscript support in v6.7.",
        "population_reason": "The retained source has a role pass for bounded formal framing context and was planned for future evidence mapping.",
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
        "matrix_population_decision": "populated_not_cited",
        "citation_added": "no",
        "manuscript_revised": "no",
        "row_limit": "Evidence matrix row only; not citation text and not manuscript support in v6.7.",
        "population_reason": "The retained source has a role pass for bounded methodological context and was planned for future evidence mapping.",
    },
]


CONDITIONAL_HOLD_ROWS = [
    {
        "candidate_entry_id": "CAND-0003",
        "hold_status": "hold_for_update_before_retention_decision",
        "retained_source_id": "none",
        "evidence_matrix_row_id": "none",
        "citation_added": "no",
        "manuscript_revised": "no",
        "reason": "Conditional metadata pass remains outside retained source, role audit, and evidence matrix population.",
    },
]


EVIDENCE_ROW_FIELDS = [
    "evidence_matrix_row_id",
    "linked_planned_mapping_id",
    "retained_source_id",
    "linked_candidate_entry_id",
    "claim_category",
    "evidence_role",
    "source_role_boundary",
    "evidence_strength",
    "matrix_population_decision",
    "citation_added",
    "manuscript_revised",
    "row_limit",
    "population_reason",
]


MATRIX_POPULATION_DECISION_VALUES = [
    "populated_not_cited",
    "held_not_populated",
    "population_deferred",
    "citation_not_added",
]


POPULATION_EXECUTION_GATES = [
    "Evidence matrix population execution must be linked to v6.6 population plan.",
    "Evidence matrix population execution must use audited retained-source roles.",
    "Only planned evidence mappings may become evidence matrix rows.",
    "Conditional-hold candidates must remain outside evidence matrix population.",
    "Each evidence matrix row must link to a retained source.",
    "Each evidence matrix row must link to a planned mapping.",
    "Each evidence matrix row must include a bounded claim category.",
    "Each evidence matrix row must include a bounded evidence role.",
    "Each evidence matrix row must include a source role boundary.",
    "Each evidence matrix row must state evidence strength without validation claims.",
    "Evidence matrix rows must not become citations.",
    "Evidence matrix rows must not revise the manuscript.",
    "Citation added count must remain zero.",
    "Manuscript revised count must remain zero.",
    "Population execution must not imply external validation.",
    "Population execution must not imply submission readiness.",
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
    "does populate the evidence matrix",
    "does not add citations",
    "does not revise the manuscript",
    "evidence matrix row is not a citation",
    "evidence matrix population is not citation integration",
    "evidence matrix population is not manuscript revision",
    "contextual support is not external validation",
    "retained source role pass is not manuscript support",
    "citations are not external validation",
    "conditional hold remains outside evidence matrix population",
    "future citation use is separate",
    "future manuscript revision is separate",
]


PROHIBITED_BEHAVIORS = [
    "Do not add citations in this milestone.",
    "Do not revise the manuscript in this milestone.",
    "Do not treat evidence matrix rows as citations.",
    "Do not treat evidence matrix rows as manuscript support.",
    "Do not treat contextual support as external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not include conditional-hold candidates in populated evidence rows.",
    "Do not convert evidence rows into citation text.",
    "Do not rewrite manuscript claims from this milestone.",
    "Do not widen bounded source roles during matrix population.",
]


NEXT_STEPS = [
    "Audit populated evidence matrix rows in a later milestone.",
    "Plan citation integration only after evidence row audit.",
    "Add citations only in a later citation-specific milestone.",
    "Revise manuscript only after citation-grounded integration.",
    "Keep CAND-0003 on hold until update handling.",
    "Preserve evidence role boundaries during citation planning.",
    "Keep public language bounded after evidence matrix population.",
    "Track evidence rows separately from manuscript claims.",
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
    "evidence matrix",
    "evidence row",
    "retained source",
    "role pass",
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
    "population execution gates",
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
class FirstEvidenceMatrixPopulationExecutionResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    evidence_matrix_population_execution_count: int
    retained_source_count: int
    planned_evidence_mapping_count: int
    evidence_matrix_populated_count: int
    evidence_matrix_row_count: int
    conditional_hold_count: int
    citation_added_count: int
    manuscript_revised_count: int
    evidence_row_field_count: int
    matrix_population_decision_value_count: int
    population_execution_gate_count: int
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
        "| Evidence matrix population execution field | Value |",
        "|---|---|",
    ]
    for key, value in EXECUTION_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_evidence_matrix_rows() -> str:
    rows = [
        "| Evidence row id | Planned mapping id | Retained source id | Claim category | Evidence role | Decision | Citation added | Manuscript revised |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in EVIDENCE_MATRIX_ROWS:
        rows.append(
            f"| {item['evidence_matrix_row_id']} | "
            f"{item['linked_planned_mapping_id']} | "
            f"{item['retained_source_id']} | "
            f"{item['claim_category']} | "
            f"{item['evidence_role']} | "
            f"{item['matrix_population_decision']} | "
            f"{item['citation_added']} | "
            f"{item['manuscript_revised']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Retained source id | Evidence row id | Citation added | Manuscript revised | Reason |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['retained_source_id']} | "
            f"{item['evidence_matrix_row_id']} | "
            f"{item['citation_added']} | "
            f"{item['manuscript_revised']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Evidence row field | v6.7 status |",
        "|---|---|",
    ]
    for field in EVIDENCE_ROW_FIELDS:
        rows.append(f"| `{field}` | populated for evidence matrix rows |")
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
    return f"""# First Evidence Matrix Population Execution v6.7

## Question
Can Viruse Fabric execute first evidence matrix population for two audited retained-source roles while keeping citations and manuscript revision at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does populate the evidence matrix. It does not add citations and does not revise the manuscript.

Evidence matrix row is not a citation. Evidence matrix population is not citation integration. Evidence matrix population is not manuscript revision. Contextual support is not external validation. Retained source role pass is not manuscript support. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Evidence Matrix Population Execution Metadata
{render_metadata_table()}

## Populated Evidence Matrix Rows
{render_evidence_matrix_rows()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Evidence Row Fields
{render_field_table()}

## Matrix Population Decision Values
{bullet_list(MATRIX_POPULATION_DECISION_VALUES)}

## Population Execution Gates
{bullet_list(POPULATION_EXECUTION_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Population Execution Interpretation
The v6.7 artifact executes the first evidence matrix population step.

EMR-0001 is populated from EMP-ROW-0001 and links RET-0001 to a bounded claim category for constraint-based causality and formal framing. EMR-0002 is populated from EMP-ROW-0002 and links RET-0002 to a bounded claim category for dynamical-systems screening and methodological context.

These are internal evidence matrix rows. They are not citations. They are not manuscript text. They do not turn the project into an externally validated theory. They only make the evidence workflow less empty, which is progress, not magic.

## Evidence Matrix Boundary
Evidence matrix population execution count is one.

Evidence matrix populated count is two.

Evidence matrix row count is two.

The two rows preserve links to planned mappings, retained sources, candidate entries, claim categories, evidence roles, source role boundaries, and row limits. This makes later evidence-row audit possible.

The rows are deliberately conservative. Each row uses contextual support language and avoids validation language. The evidence matrix can organize support relationships, but it cannot certify the model, validate the theory, or make the manuscript ready.

## Citation Boundary
Citation added count remains zero.

No citation slot is filled. No bibliography entry is created. No reference text is added. No evidence matrix row becomes citation text in this milestone.

A future citation workflow may use audited evidence rows, but that future workflow must be explicit. Evidence rows do not automatically become citations because a table got tired and wanted promotion.

## Manuscript Boundary
Manuscript revised count remains zero.

The manuscript receives no new text, no rewritten claim, no strengthened conclusion, and no citation-grounded revision from this artifact.

The evidence matrix is now less empty, but the manuscript remains unchanged. This is exactly the intended separation between evidence organization and manuscript integration.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside evidence matrix population because it is not retained, not role-audited, and not planned for evidence mapping. It cannot receive an evidence row until it passes the missing prior stages.

This boundary keeps a conditional source from wandering into the evidence matrix wearing a fake badge. Apparently even internal artifacts need security theater.

## Output Counts
Evidence matrix population execution count: 1

Retained source count: 2

Planned evidence mapping count: 2

Evidence matrix populated count: 2

Evidence matrix row count: 2

Conditional hold count: 1

Citation added count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact populates the evidence matrix.

It does not add citations, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstEvidenceMatrixPopulationExecutionResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    evidence_matrix_population_execution_count = int(
        EXECUTION_METADATA["evidence_matrix_population_execution_count"]
    )
    retained_source_count = int(EXECUTION_METADATA["retained_source_count_from_v6_6"])
    planned_evidence_mapping_count = int(
        EXECUTION_METADATA["planned_evidence_mapping_count_from_v6_6"]
    )
    evidence_matrix_populated_count = int(EXECUTION_METADATA["evidence_matrix_populated_count"])
    evidence_matrix_row_count = len(EVIDENCE_MATRIX_ROWS)
    conditional_hold_count = int(EXECUTION_METADATA["conditional_hold_count"])
    citation_added_count = int(EXECUTION_METADATA["citation_added_count"])
    manuscript_revised_count = int(EXECUTION_METADATA["manuscript_revised_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 17:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if evidence_matrix_population_execution_count != 1:
        errors.append(
            "Evidence matrix population execution count should be one, got: "
            f"{evidence_matrix_population_execution_count}"
        )

    if retained_source_count != 2:
        errors.append(f"Retained source count should be two, got: {retained_source_count}")

    if planned_evidence_mapping_count != 2:
        errors.append(
            "Planned evidence mapping count should be two, got: "
            f"{planned_evidence_mapping_count}"
        )

    if evidence_matrix_populated_count != 2:
        errors.append(
            "Evidence matrix populated count should be two, got: "
            f"{evidence_matrix_populated_count}"
        )

    if evidence_matrix_row_count != 2:
        errors.append(f"Evidence matrix row count should be two, got: {evidence_matrix_row_count}")

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    if evidence_matrix_populated_count != evidence_matrix_row_count:
        errors.append("Evidence matrix populated count must equal evidence matrix row count")

    if evidence_matrix_row_count != planned_evidence_mapping_count:
        errors.append("Evidence matrix row count must equal planned evidence mapping count")

    for row in EVIDENCE_MATRIX_ROWS:
        missing_fields = [field for field in EVIDENCE_ROW_FIELDS if not row.get(field)]
        if missing_fields:
            errors.append(
                f"{row.get('evidence_matrix_row_id', 'unknown')} missing evidence fields: "
                f"{len(missing_fields)}"
            )

    for label, value in [
        ("Citation added count", citation_added_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if len(EVIDENCE_ROW_FIELDS) < 13:
        errors.append(f"Evidence row field count too low: {len(EVIDENCE_ROW_FIELDS)}")

    if len(MATRIX_POPULATION_DECISION_VALUES) < 4:
        errors.append(
            "Matrix population decision value count too low: "
            f"{len(MATRIX_POPULATION_DECISION_VALUES)}"
        )

    if len(POPULATION_EXECUTION_GATES) < 16:
        errors.append(
            f"Population execution gate count too low: {len(POPULATION_EXECUTION_GATES)}"
        )

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
        errors.append(
            f"Word count too low for first evidence matrix population execution: {word_count}"
        )

    warnings.append("Evidence matrix rows are populated, but no citations are added.")
    warnings.append("Evidence matrix population does not revise the manuscript.")

    passed = not errors

    interpretation = (
        "The v6.7 artifact creates two evidence matrix rows from planned retained-source "
        "mappings while keeping citations and manuscript revision at zero."
    )

    return FirstEvidenceMatrixPopulationExecutionResult(
        title="First Evidence Matrix Population Execution v6.7",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        evidence_matrix_population_execution_count=evidence_matrix_population_execution_count,
        retained_source_count=retained_source_count,
        planned_evidence_mapping_count=planned_evidence_mapping_count,
        evidence_matrix_populated_count=evidence_matrix_populated_count,
        evidence_matrix_row_count=evidence_matrix_row_count,
        conditional_hold_count=conditional_hold_count,
        citation_added_count=citation_added_count,
        manuscript_revised_count=manuscript_revised_count,
        evidence_row_field_count=len(EVIDENCE_ROW_FIELDS),
        matrix_population_decision_value_count=len(MATRIX_POPULATION_DECISION_VALUES),
        population_execution_gate_count=len(POPULATION_EXECUTION_GATES),
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

    print("First Evidence Matrix Population Execution v6.7")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Evidence matrix population execution count: {result.evidence_matrix_population_execution_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Planned evidence mapping count: {result.planned_evidence_mapping_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Evidence matrix row count: {result.evidence_matrix_row_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Evidence row field count: {result.evidence_row_field_count}")
    print(f"Matrix population decision value count: {result.matrix_population_decision_value_count}")
    print(f"Population execution gate count: {result.population_execution_gate_count}")
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
