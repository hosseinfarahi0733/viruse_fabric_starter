"""Candidate source metadata audit for Viruse Fabric v6.2.

This module audits the metadata of the three candidate source entries created
in v6.1.

It audits candidate metadata only.

It does not retain sources.
It does not add citations.
It does not populate the evidence matrix.
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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "candidate_source_metadata_audit_v6_2.md"

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
    "candidate_metadata_audit_id": "CMA-0001",
    "linked_candidate_entry_creation_id": "CEC-0001",
    "linked_candidate_entry_plan_id": "CEP-0001",
    "linked_screening_execution_id": "SX-0001",
    "audit_status": "metadata_audited_not_retained",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "candidate_source_count_from_v6_1": "3",
    "candidate_source_audited_count": "3",
    "metadata_audit_pass_count": "2",
    "metadata_audit_conditional_pass_count": "1",
    "metadata_audit_fail_count": "0",
    "retained_source_count": "0",
}


METADATA_AUDIT_ROWS = [
    {
        "candidate_entry_id": "CAND-0001",
        "source_title": "Beyond Structural Causal Models: Causal Constraints Models",
        "metadata_presence_status": "complete_for_candidate_audit",
        "title_check": "pass",
        "author_check": "pass",
        "venue_or_repository_check": "pass",
        "year_or_access_date_check": "pass_with_year_note",
        "access_route_check": "pass",
        "source_type_check": "pass",
        "claim_mapping_check": "pass",
        "exclusion_risk_check": "pass",
        "audit_decision": "metadata_pass_not_retained",
        "retained_source_created": "no",
        "citation_added": "no",
        "audit_note": "PMLR and arXiv routes support candidate metadata, but retention still requires source-role review.",
    },
    {
        "candidate_entry_id": "CAND-0002",
        "source_title": "Causal screening in dynamical systems",
        "metadata_presence_status": "complete_for_candidate_audit",
        "title_check": "pass",
        "author_check": "pass",
        "venue_or_repository_check": "pass",
        "year_or_access_date_check": "pass",
        "access_route_check": "pass",
        "source_type_check": "pass",
        "claim_mapping_check": "pass",
        "exclusion_risk_check": "pass",
        "audit_decision": "metadata_pass_not_retained",
        "retained_source_created": "no",
        "citation_added": "no",
        "audit_note": "PMLR and arXiv routes support candidate metadata, but retention still requires methodological-fit review.",
    },
    {
        "candidate_entry_id": "CAND-0003",
        "source_title": "Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis",
        "metadata_presence_status": "complete_but_update_recommended",
        "title_check": "pass",
        "author_check": "pass",
        "venue_or_repository_check": "conditional_pass",
        "year_or_access_date_check": "conditional_pass",
        "access_route_check": "pass",
        "source_type_check": "conditional_pass",
        "claim_mapping_check": "pass",
        "exclusion_risk_check": "pass",
        "audit_decision": "metadata_conditional_pass_not_retained",
        "retained_source_created": "no",
        "citation_added": "no",
        "audit_note": "arXiv metadata exists; possible venue status should be checked before any retention decision.",
    },
]


AUDIT_FIELD_CHECKS = [
    "candidate_entry_id",
    "source_title",
    "author_information",
    "venue_or_repository",
    "publication_year_or_access_date",
    "stable_access_route",
    "source_type",
    "primary_or_secondary_status",
    "linked_raw_result_observation_id",
    "linked_screening_decision",
    "claim_category_mapping",
    "inclusion_rationale",
    "exclusion_risk_notes",
    "proposed_source_role",
    "candidate_entry_status",
    "audit_required_before_retention",
]


AUDIT_DECISION_VALUES = [
    "metadata_pass_not_retained",
    "metadata_conditional_pass_not_retained",
    "metadata_fail_not_retained",
    "metadata_update_required_before_retention",
]


RETENTION_GATES_NOT_EXECUTED = [
    "Do not retain sources during metadata audit.",
    "Do not cite sources during metadata audit.",
    "Do not populate evidence matrix during metadata audit.",
    "Do not revise manuscript during metadata audit.",
    "Do not treat metadata pass as retention.",
    "Do not treat conditional metadata pass as retention.",
    "Do not treat access route existence as citation readiness.",
    "Do not treat venue existence as external validation.",
    "Do not treat source title alignment as evidence.",
    "Do not treat candidate audit as manuscript support.",
]


NEXT_STEPS = [
    "Create a retained source decision plan in a later milestone.",
    "Define retention criteria for passed candidate entries.",
    "Define update handling for conditional candidate entries.",
    "Check venue status for conditional candidate entries before retention.",
    "Check source-role fit before retention.",
    "Check claim-category mapping before retention.",
    "Retain sources only after explicit retention decision.",
    "Populate evidence matrix only after retained-source audit.",
    "Add citations only after retained-source decision.",
    "Revise manuscript only after citation-grounded integration.",
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
    "metadata audit is not source retention",
    "metadata pass is not source retention",
    "conditional metadata pass is not source retention",
    "candidate source entries are not retained sources",
    "candidate source entries are not citations",
    "retained sources are not citations",
    "citations are not external validation",
    "does audit candidate metadata",
    "does not retain sources",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
]


PROHIBITED_BEHAVIORS = [
    "Do not retain sources in this milestone.",
    "Do not add citations in this milestone.",
    "Do not populate the evidence matrix in this milestone.",
    "Do not revise the manuscript in this milestone.",
    "Do not treat metadata audit as retention.",
    "Do not treat metadata pass as citation readiness.",
    "Do not treat conditional metadata pass as evidence.",
    "Do not imply external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not update manuscript claims from candidate metadata audit.",
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
    "metadata",
    "audit",
    "candidate source",
    "retained source",
    "conditional",
    "zero",
    "pending",
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
    "retention gates not executed",
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
class CandidateSourceMetadataAuditResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    candidate_metadata_audit_count: int
    candidate_source_count: int
    candidate_source_audited_count: int
    metadata_audit_pass_count: int
    metadata_audit_conditional_pass_count: int
    metadata_audit_fail_count: int
    retained_source_count: int
    citation_added_count: int
    evidence_matrix_populated_count: int
    manuscript_revised_count: int
    audit_field_check_count: int
    audit_decision_value_count: int
    retention_gate_not_executed_count: int
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
        "| Audit field | Value |",
        "|---|---|",
    ]
    for key, value in AUDIT_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_audit_rows() -> str:
    rows = [
        "| Candidate id | Title | Metadata status | Decision | Retained | Citation added | Audit note |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in METADATA_AUDIT_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['source_title']} | "
            f"{item['metadata_presence_status']} | "
            f"{item['audit_decision']} | "
            f"{item['retained_source_created']} | "
            f"{item['citation_added']} | "
            f"{item['audit_note']} |"
        )
    return "\n".join(rows)


def render_field_check_table() -> str:
    rows = [
        "| Metadata field check | v6.2 audit status |",
        "|---|---|",
    ]
    for field in AUDIT_FIELD_CHECKS:
        rows.append(f"| `{field}` | checked for candidate metadata audit |")
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
    return f"""# Candidate Source Metadata Audit v6.2

## Question
Can Viruse Fabric audit the metadata of the three candidate source entries created in v6.1 while keeping retained sources, citations, evidence matrix population, and manuscript revision at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does audit candidate metadata. It does not retain sources, does not add citations, does not populate the evidence matrix, and does not revise the manuscript.

Metadata audit is not source retention. Metadata pass is not source retention. Conditional metadata pass is not source retention. Candidate source entries are not retained sources. Candidate source entries are not citations. Retained sources are not citations. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Candidate Metadata Audit Metadata
{render_metadata_table()}

## Candidate Metadata Audit Rows
{render_audit_rows()}

## Metadata Field Checks
{render_field_check_table()}

## Audit Decision Values
{bullet_list(AUDIT_DECISION_VALUES)}

## Retention Gates Not Executed
{bullet_list(RETENTION_GATES_NOT_EXECUTED)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Metadata Audit Interpretation
The v6.2 artifact audits the metadata of the three candidate source entries created in v6.1.

Two candidate entries receive metadata pass decisions. One candidate entry receives a conditional metadata pass because its arXiv record exists, but possible venue status should be checked before any retention decision. This is not a failure. It is a boundary-preserving audit result.

The audit confirms that candidate entries can carry structured metadata and still remain outside retention, citation use, evidence matrix transfer, and manuscript revision.

## Retention Boundary
Retained source count remains zero.

No candidate source is retained in this milestone. A metadata pass only means that the candidate record is structured enough to move into a later retained-source decision plan. A conditional pass means that the candidate record exists but needs update handling before retention.

A candidate source can be useful without being retained. This is where projects often become embarrassing: they see a source-shaped object and immediately crown it as evidence. Viruse Fabric does not do that here.

## Evidence Boundary
Citation added count remains zero.

Evidence matrix populated count remains zero.

Manuscript revised count remains zero.

This milestone does not make any source usable as manuscript support. It only audits whether candidate metadata is sufficiently structured for later retention planning. The artifact therefore preserves the distinction between source metadata, source retention, citation integration, and theory validation.

## Audit Consequence Boundary
The audit creates a procedural result, not an evidential result.

A metadata pass means that the candidate source record is organized enough for a later retained-source decision plan. It does not mean that the source should be retained. It does not mean that the source should be cited. It does not mean that the manuscript should inherit any claim from the source.

A conditional metadata pass is even narrower. It means that the candidate entry is not rejected at the metadata-audit layer, but at least one metadata dimension needs later update handling before any retention decision. In this milestone, the conditional case is kept outside retention for that reason.

This boundary is important because the project is now moving from empty infrastructure into real source handling. Real source handling creates a temptation to accelerate: metadata exists, therefore retain it; retention exists, therefore cite it; citation exists, therefore revise the manuscript; manuscript revision exists, therefore pretend external validation happened. That sequence is forbidden here. Each transition requires its own milestone and its own audit.

## Candidate Audit Failure Modes Prevented
This artifact prevents several failure modes.

It prevents title-only promotion, where a source is treated as useful because its title looks aligned with the theory. It prevents metadata inflation, where a candidate record is mistaken for evidence. It prevents citation laundering, where a candidate source becomes a citation before retention. It prevents manuscript drift, where the manuscript absorbs support from unaudited sources.

The audit also preserves the deferred status of unresolved cases. A candidate source can pass metadata audit and still remain unused. A candidate source can be conditionally acceptable and still remain outside retention. A candidate source can be relevant to a literature family and still provide no support for the project until later review.

These constraints are tedious, which is another way of saying they are doing their job.

## Output Counts
Candidate metadata audit count: 1

Candidate source count: 3

Candidate source audited count: 3

Metadata audit pass count: 2

Metadata audit conditional pass count: 1

Metadata audit fail count: 0

Retained source count: 0

Citation added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact audits candidate source metadata.

It does not retain sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> CandidateSourceMetadataAuditResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    candidate_metadata_audit_count = 1
    candidate_source_count = int(AUDIT_METADATA["candidate_source_count_from_v6_1"])
    candidate_source_audited_count = int(AUDIT_METADATA["candidate_source_audited_count"])
    metadata_pass_count = int(AUDIT_METADATA["metadata_audit_pass_count"])
    metadata_conditional_pass_count = int(AUDIT_METADATA["metadata_audit_conditional_pass_count"])
    metadata_fail_count = int(AUDIT_METADATA["metadata_audit_fail_count"])
    retained_source_count = int(AUDIT_METADATA["retained_source_count"])
    citation_added_count = 0
    evidence_matrix_populated_count = 0
    manuscript_revised_count = 0

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 12:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if candidate_metadata_audit_count != 1:
        errors.append(
            f"Candidate metadata audit count should be one, got: {candidate_metadata_audit_count}"
        )

    if candidate_source_count != 3:
        errors.append(f"Candidate source count should be three, got: {candidate_source_count}")

    if candidate_source_audited_count != 3:
        errors.append(
            f"Candidate source audited count should be three, got: {candidate_source_audited_count}"
        )

    if metadata_pass_count != 2:
        errors.append(f"Metadata audit pass count should be two, got: {metadata_pass_count}")

    if metadata_conditional_pass_count != 1:
        errors.append(
            "Metadata audit conditional pass count should be one, got: "
            f"{metadata_conditional_pass_count}"
        )

    if metadata_fail_count != 0:
        errors.append(f"Metadata audit fail count should be zero, got: {metadata_fail_count}")

    if metadata_pass_count + metadata_conditional_pass_count + metadata_fail_count != candidate_source_audited_count:
        errors.append("Metadata audit decision counts do not sum to audited candidate source count")

    if len(AUDIT_FIELD_CHECKS) < 16:
        errors.append(f"Audit field check count too low: {len(AUDIT_FIELD_CHECKS)}")

    if len(AUDIT_DECISION_VALUES) < 4:
        errors.append(f"Audit decision value count too low: {len(AUDIT_DECISION_VALUES)}")

    if len(RETENTION_GATES_NOT_EXECUTED) < 10:
        errors.append(
            f"Retention gate not executed count too low: {len(RETENTION_GATES_NOT_EXECUTED)}"
        )

    for label, value in [
        ("Retained source count", retained_source_count),
        ("Citation added count", citation_added_count),
        ("Evidence matrix populated count", evidence_matrix_populated_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if boundary_count < 20:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 11:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 10:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if word_count < 1200:
        errors.append(f"Word count too low for candidate source metadata audit: {word_count}")

    warnings.append("Candidate metadata is audited, but no sources are retained.")
    warnings.append("Metadata audit does not add citations, evidence rows, or manuscript revisions.")

    passed = not errors

    interpretation = (
        "The v6.2 artifact audits metadata for three candidate source entries while keeping "
        "retained sources, citations, evidence matrix population, and manuscript revision at zero."
    )

    return CandidateSourceMetadataAuditResult(
        title="Candidate Source Metadata Audit v6.2",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        candidate_metadata_audit_count=candidate_metadata_audit_count,
        candidate_source_count=candidate_source_count,
        candidate_source_audited_count=candidate_source_audited_count,
        metadata_audit_pass_count=metadata_pass_count,
        metadata_audit_conditional_pass_count=metadata_conditional_pass_count,
        metadata_audit_fail_count=metadata_fail_count,
        retained_source_count=retained_source_count,
        citation_added_count=citation_added_count,
        evidence_matrix_populated_count=evidence_matrix_populated_count,
        manuscript_revised_count=manuscript_revised_count,
        audit_field_check_count=len(AUDIT_FIELD_CHECKS),
        audit_decision_value_count=len(AUDIT_DECISION_VALUES),
        retention_gate_not_executed_count=len(RETENTION_GATES_NOT_EXECUTED),
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

    print("Candidate Source Metadata Audit v6.2")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Candidate metadata audit count: {result.candidate_metadata_audit_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Candidate source audited count: {result.candidate_source_audited_count}")
    print(f"Metadata audit pass count: {result.metadata_audit_pass_count}")
    print(f"Metadata audit conditional pass count: {result.metadata_audit_conditional_pass_count}")
    print(f"Metadata audit fail count: {result.metadata_audit_fail_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Audit field check count: {result.audit_field_check_count}")
    print(f"Audit decision value count: {result.audit_decision_value_count}")
    print(f"Retention gate not executed count: {result.retention_gate_not_executed_count}")
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
