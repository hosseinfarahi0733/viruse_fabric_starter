"""First candidate source entry creation for Viruse Fabric v6.1.

This module creates the first real candidate source entries after the v6.0
candidate source entry plan.

It creates candidate source entries only.

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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_candidate_source_entry_creation_v6_1.md"

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


CREATION_METADATA = {
    "candidate_entry_creation_id": "CEC-0001",
    "linked_candidate_entry_plan_id": "CEP-0001",
    "linked_screening_execution_id": "SX-0001",
    "linked_search_execution_id": "SE-0001",
    "creation_status": "candidate_entries_created_not_retained",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "claim_category": "literature-needed: constraints shape possible trajectories",
    "planned_candidate_entry_row_count_from_v6_0": "5",
    "candidate_source_count": "3",
    "deferred_source_count": "2",
    "retained_source_count": "0",
}


CANDIDATE_SOURCE_ENTRIES = [
    {
        "candidate_entry_id": "CAND-0001",
        "linked_raw_result_observation_id": "raw_result_observation_02",
        "linked_screening_decision": "pass_to_candidate_entry_planning",
        "source_title": "Beyond Structural Causal Models: Causal Constraints Models",
        "author_information": "Tineke Blom; Stephan Bongers; Joris M. Mooij",
        "venue_or_repository": "Proceedings of Machine Learning Research / UAI proceedings; arXiv record also available",
        "publication_year_or_access_date": "2020 proceedings record; 2018 arXiv record",
        "stable_access_route": "https://proceedings.mlr.press/v115/blom20a.html",
        "source_type": "conference_paper_with_preprint_record",
        "primary_or_secondary_status": "primary_research_source",
        "claim_category_mapping": "constraints and causal models for dynamical systems",
        "inclusion_rationale": "Directly addresses causal constraints models and dynamical systems at equilibrium.",
        "exclusion_risk_notes": "Candidate status only; source role must be audited before retention or citation use.",
        "proposed_source_role": "formal_framing",
        "candidate_entry_status": "candidate_created_pending_metadata_audit",
        "audit_required_before_retention": "yes",
    },
    {
        "candidate_entry_id": "CAND-0002",
        "linked_raw_result_observation_id": "raw_result_observation_03",
        "linked_screening_decision": "pass_to_candidate_entry_planning",
        "source_title": "Causal screening in dynamical systems",
        "author_information": "Søren Wengel Mogensen",
        "venue_or_repository": "Proceedings of Machine Learning Research / UAI 2020",
        "publication_year_or_access_date": "2020",
        "stable_access_route": "https://proceedings.mlr.press/v124/wengel-mogensen20a.html",
        "source_type": "conference_paper",
        "primary_or_secondary_status": "primary_research_source",
        "claim_category_mapping": "causal screening methods for dynamical systems",
        "inclusion_rationale": "Directly addresses causal screening in dynamical systems.",
        "exclusion_risk_notes": "Candidate status only; methodological fit must be audited before retention or citation use.",
        "proposed_source_role": "methodological_context",
        "candidate_entry_status": "candidate_created_pending_metadata_audit",
        "audit_required_before_retention": "yes",
    },
    {
        "candidate_entry_id": "CAND-0003",
        "linked_raw_result_observation_id": "raw_result_observation_05",
        "linked_screening_decision": "pass_to_candidate_entry_planning",
        "source_title": "Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis",
        "author_information": "Nicholas Tagliapietra; Katharina Ensinger; Christoph Zimmer; Osman Mian",
        "venue_or_repository": "arXiv",
        "publication_year_or_access_date": "2025 arXiv record",
        "stable_access_route": "https://arxiv.org/abs/2512.14361",
        "source_type": "preprint",
        "primary_or_secondary_status": "primary_research_source_pending_venue_audit",
        "claim_category_mapping": "causal structure learning for dynamical systems",
        "inclusion_rationale": "Addresses causal structure learning in dynamical systems and may support methodological context later.",
        "exclusion_risk_notes": "Preprint candidate status only; venue status and fit must be audited before retention or citation use.",
        "proposed_source_role": "future_validation_context",
        "candidate_entry_status": "candidate_created_pending_metadata_audit",
        "audit_required_before_retention": "yes",
    },
]


DEFERRED_SOURCE_ROWS = [
    {
        "raw_result_observation_id": "raw_result_observation_01",
        "raw_title": "Information-theoretic formulation of dynamical systems",
        "screening_decision": "defer_for_candidate_entry_planning",
        "candidate_source_created": "no",
        "reason": "Deferred in v5.9; not promoted to candidate entry in v6.1.",
    },
    {
        "raw_result_observation_id": "raw_result_observation_04",
        "raw_title": "Causality and independence in perfectly adapted dynamical systems",
        "screening_decision": "defer_for_candidate_entry_planning",
        "candidate_source_created": "no",
        "reason": "Deferred in v5.9; not promoted to candidate entry in v6.1.",
    },
]


CANDIDATE_ENTRY_FIELDS = [
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


CANDIDATE_AUDIT_GATES = [
    "Candidate entry must link to a v5.9 raw observation.",
    "Candidate entry must link to a v5.9 pass-to-candidate-planning decision.",
    "Candidate entry must include source title.",
    "Candidate entry must include author information.",
    "Candidate entry must include venue or repository.",
    "Candidate entry must include publication year or access date.",
    "Candidate entry must include stable access route.",
    "Candidate entry must include source type.",
    "Candidate entry must include primary or secondary status.",
    "Candidate entry must include claim-category mapping.",
    "Candidate entry must include inclusion rationale.",
    "Candidate entry must include exclusion-risk notes.",
    "Candidate entry must not be treated as retained source.",
    "Candidate entry must not be treated as citation.",
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
    "candidate source entries are not retained sources",
    "candidate source entries are not citations",
    "candidate source entries are not external validation",
    "retained sources are not citations",
    "citations are not external validation",
    "does create candidate source entries",
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
    "Do not treat candidate source entries as retained sources.",
    "Do not treat candidate source entries as citations.",
    "Do not treat candidate source entries as external validation.",
    "Do not treat title-level relevance as sufficient for retention.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not convert deferred raw observations into candidate entries in this milestone.",
]


NEXT_STEPS = [
    "Audit candidate source metadata in a later milestone.",
    "Check stable access routes before retention.",
    "Check source type and venue status before retention.",
    "Check claim-category mapping before retention.",
    "Check source role before retention.",
    "Retain sources only after candidate metadata audit.",
    "Populate the evidence matrix only after retained-source audit.",
    "Add citations only after retained-source decision.",
    "Revise manuscript only after citation-grounded integration.",
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
    "candidate source",
    "candidate entry",
    "retained source",
    "zero",
    "deferred",
    "pending",
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
    "candidate audit gates",
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
class FirstCandidateSourceEntryCreationResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    candidate_entry_creation_count: int
    candidate_source_count: int
    deferred_source_count: int
    retained_source_count: int
    source_added_count: int
    citation_added_count: int
    evidence_matrix_populated_count: int
    manuscript_revised_count: int
    candidate_entry_field_count: int
    candidate_audit_gate_count: int
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
        "| Creation field | Value |",
        "|---|---|",
    ]
    for key, value in CREATION_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_candidate_entries() -> str:
    rows = [
        "| Candidate id | Raw observation | Title | Authors | Venue or repository | Access route | Status |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in CANDIDATE_SOURCE_ENTRIES:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['linked_raw_result_observation_id']} | "
            f"{item['source_title']} | "
            f"{item['author_information']} | "
            f"{item['venue_or_repository']} | "
            f"{item['stable_access_route']} | "
            f"{item['candidate_entry_status']} |"
        )
    return "\n".join(rows)


def render_deferred_rows() -> str:
    rows = [
        "| Raw observation | Title | Screening decision | Candidate source created | Reason |",
        "|---|---|---|---|---|",
    ]
    for item in DEFERRED_SOURCE_ROWS:
        rows.append(
            f"| {item['raw_result_observation_id']} | "
            f"{item['raw_title']} | "
            f"{item['screening_decision']} | "
            f"{item['candidate_source_created']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table(fields: list[str]) -> str:
    rows = [
        "| Candidate entry field | v6.1 status |",
        "|---|---|",
    ]
    for field in fields:
        rows.append(f"| `{field}` | populated for candidate entries only |")
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
    return f"""# First Candidate Source Entry Creation v6.1

## Question
Can Viruse Fabric create the first candidate source entries from the v5.9 pass-to-candidate-planning decisions while keeping retained sources, citations, evidence matrix population, and manuscript revision at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does create candidate source entries. It does not retain sources, does not add citations, does not populate the evidence matrix, and does not revise the manuscript.

Candidate source entries are not retained sources. Candidate source entries are not citations. Candidate source entries are not external validation. Retained sources are not citations. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Candidate Entry Creation Metadata
{render_metadata_table()}

## Candidate Source Entries Created
{render_candidate_entries()}

## Deferred Raw Observations Not Created as Candidate Sources
{render_deferred_rows()}

## Candidate Entry Fields
{render_field_table(CANDIDATE_ENTRY_FIELDS)}

## Candidate Audit Gates
{bullet_list(CANDIDATE_AUDIT_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Candidate Entry Interpretation
The v6.1 artifact creates the first candidate source entries in the Viruse Fabric literature workflow.

This is the first milestone where candidate source count is intentionally nonzero. The count is three because only the three v5.9 pass-to-candidate-planning decisions are promoted into candidate entries. The two deferred raw observations remain outside candidate source creation.

This is progress, but it is still not retention. A candidate entry is an auditable source record. It records metadata, linkage, proposed role, and risk notes. It does not mean that the source is accepted as evidence. It does not mean the source can be cited. It does not mean the manuscript has new support.

## Metadata Integrity Boundary
Each candidate entry includes title, author information, venue or repository, year or access-date information, stable access route, source type, primary or secondary status, linked raw observation id, linked screening decision, claim-category mapping, inclusion rationale, exclusion-risk notes, proposed source role, candidate status, and audit requirement.

Those fields are sufficient for candidate entry creation, not for retention. Retention requires later audit. Source role requires later audit. Citation use requires later retained-source decision. Evidence matrix population requires later retained-source audit.

The candidate layer is a staging layer. It is allowed to be useful. It is not allowed to pretend to be evidence, because apparently even files need moral supervision now.

## Retention Boundary
Retained source count remains zero.

No candidate entry is retained in this milestone. No candidate entry is transferred to the evidence matrix. No candidate entry is used as a citation. No candidate entry changes the manuscript.

A later milestone must audit metadata before retention. The audit should check access route stability, authorship, source type, venue or repository status, claim-category fit, source role, and exclusion risk.

## Output Counts
Candidate entry creation count: 1

Candidate source count: 3

Deferred source count: 2

Retained source count: 0

Source added count: 3

Citation added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact creates first candidate source entries.

It does not retain sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstCandidateSourceEntryCreationResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    candidate_entry_creation_count = 1
    candidate_source_count = len(CANDIDATE_SOURCE_ENTRIES)
    deferred_source_count = len(DEFERRED_SOURCE_ROWS)
    retained_source_count = int(CREATION_METADATA["retained_source_count"])
    source_added_count = candidate_source_count
    citation_added_count = 0
    evidence_matrix_populated_count = 0
    manuscript_revised_count = 0

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 11:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if candidate_entry_creation_count != 1:
        errors.append(
            f"Candidate entry creation count should be one, got: {candidate_entry_creation_count}"
        )

    if candidate_source_count != 3:
        errors.append(f"Candidate source count should be three, got: {candidate_source_count}")

    if deferred_source_count != 2:
        errors.append(f"Deferred source count should be two, got: {deferred_source_count}")

    for entry in CANDIDATE_SOURCE_ENTRIES:
        missing_fields = [field for field in CANDIDATE_ENTRY_FIELDS if not entry.get(field)]
        if missing_fields:
            errors.append(
                f"{entry.get('candidate_entry_id', 'unknown')} missing fields: {len(missing_fields)}"
            )

    if len(CANDIDATE_ENTRY_FIELDS) < 16:
        errors.append(f"Candidate entry field count too low: {len(CANDIDATE_ENTRY_FIELDS)}")

    if len(CANDIDATE_AUDIT_GATES) < 14:
        errors.append(f"Candidate audit gate count too low: {len(CANDIDATE_AUDIT_GATES)}")

    for label, value in [
        ("Retained source count", retained_source_count),
        ("Citation added count", citation_added_count),
        ("Evidence matrix populated count", evidence_matrix_populated_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if source_added_count != 3:
        errors.append(f"Source added count should be three candidate entries, got: {source_added_count}")

    if boundary_count < 18:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 11:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 9:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if word_count < 1200:
        errors.append(f"Word count too low for first candidate source entry creation: {word_count}")

    warnings.append("Candidate source entries are created, but none are retained.")
    warnings.append("Candidate source entries do not add citations, evidence rows, or manuscript revisions.")

    passed = not errors

    interpretation = (
        "The v6.1 artifact creates three candidate source entries from pass-to-candidate-planning "
        "decisions while keeping retained sources, citations, evidence matrix population, and "
        "manuscript revision at zero."
    )

    return FirstCandidateSourceEntryCreationResult(
        title="First Candidate Source Entry Creation v6.1",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        candidate_entry_creation_count=candidate_entry_creation_count,
        candidate_source_count=candidate_source_count,
        deferred_source_count=deferred_source_count,
        retained_source_count=retained_source_count,
        source_added_count=source_added_count,
        citation_added_count=citation_added_count,
        evidence_matrix_populated_count=evidence_matrix_populated_count,
        manuscript_revised_count=manuscript_revised_count,
        candidate_entry_field_count=len(CANDIDATE_ENTRY_FIELDS),
        candidate_audit_gate_count=len(CANDIDATE_AUDIT_GATES),
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

    print("First Candidate Source Entry Creation v6.1")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Candidate entry creation count: {result.candidate_entry_creation_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Deferred source count: {result.deferred_source_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Candidate entry field count: {result.candidate_entry_field_count}")
    print(f"Candidate audit gate count: {result.candidate_audit_gate_count}")
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
