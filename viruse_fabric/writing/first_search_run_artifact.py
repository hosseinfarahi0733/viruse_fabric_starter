"""First search run artifact for Viruse Fabric v5.5.

This module generates a controlled first search-run shell.

It connects:
- the v5.4 first literature family search plan,
- the v5.3 empty search log audit,
- the v5.2 empty literature search log,
- the v5.1 literature search log template,
- the v4.9 claim-to-citation readiness map,
- the v4.8 literature family evidence matrix.

It does not execute a live search.
It does not add sources.
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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_search_run_artifact_v5_5.md"

SOURCE_FIRST_SEARCH_PLAN = PROJECT_ROOT / "outputs" / "first_literature_family_search_plan_v5_4.md"
SOURCE_EMPTY_SEARCH_LOG_AUDIT = PROJECT_ROOT / "outputs" / "empty_search_log_audit_v5_3.md"
SOURCE_EMPTY_SEARCH_LOG = PROJECT_ROOT / "outputs" / "literature_search_log_empty_v5_2.md"
SOURCE_SEARCH_LOG_TEMPLATE = PROJECT_ROOT / "outputs" / "literature_search_log_template_v5_1.md"
SOURCE_CLAIM_MAP = PROJECT_ROOT / "outputs" / "claim_to_citation_readiness_map_v4_9.md"
SOURCE_EVIDENCE_MATRIX = PROJECT_ROOT / "outputs" / "literature_family_evidence_matrix_v4_8.md"

SOURCE_ARTIFACTS = [
    SOURCE_FIRST_SEARCH_PLAN,
    SOURCE_EMPTY_SEARCH_LOG_AUDIT,
    SOURCE_EMPTY_SEARCH_LOG,
    SOURCE_SEARCH_LOG_TEMPLATE,
    SOURCE_CLAIM_MAP,
    SOURCE_EVIDENCE_MATRIX,
]


FIRST_SEARCH_RUN = {
    "search_run_id": "SR-0001-SHELL",
    "search_run_status": "planned_not_executed",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "claim_category": "literature-needed: constraints shape possible trajectories",
    "search_venue": "Google Scholar",
    "planned_query_id": "Q-01",
    "planned_query_string": '"constraint" "causality" "dynamical systems"',
    "query_rationale": (
        "Start with the broadest controlled query from v5.4 because it targets the "
        "central relationship between constraints, causality, and dynamical systems."
    ),
    "allowed_use": "future search execution shell only",
    "not_allowed_use": "source evidence, citation support, external validation, or manuscript revision",
}


RUN_SHELL_FIELDS = [
    "search_run_id",
    "search_run_status",
    "search_date",
    "searcher",
    "literature_family",
    "claim_category",
    "search_venue",
    "planned_query_id",
    "planned_query_string",
    "query_rationale",
    "inclusion_criteria_used",
    "exclusion_criteria_used",
    "raw_result_count",
    "screened_result_count",
    "candidate_source_count",
    "retained_source_count",
    "deferred_source_count",
    "rejected_source_count",
    "notes",
]


PENDING_FIELD_VALUES = [
    "search_date: PENDING_REAL_SEARCH",
    "searcher: PENDING_REAL_SEARCH",
    "raw_result_count: PENDING_REAL_SEARCH",
    "screened_result_count: PENDING_REAL_SEARCH",
    "candidate_source_count: 0",
    "retained_source_count: 0",
    "deferred_source_count: 0",
    "rejected_source_count: 0",
    "notes: SEARCH_NOT_EXECUTED_IN_V5_5",
]


EXECUTION_GATES = [
    "The run shell must be created before live search.",
    "The selected literature family must match the v5.4 plan.",
    "The selected query must match a planned query from v5.4.",
    "The search venue must be recorded before execution.",
    "The search date must remain pending until a real search is performed.",
    "Raw result count must remain pending until a real search is performed.",
    "Screened result count must remain pending until screening occurs.",
    "Candidate source count must remain zero until source candidates are recorded.",
    "Retained source count must remain zero until candidate audit passes.",
    "Citation added count must remain zero.",
    "Evidence matrix populated count must remain zero.",
    "Manuscript revised count must remain zero.",
]


INCLUSION_CRITERIA_LINKS = [
    "Use v5.4 inclusion criteria during future execution.",
    "Require relevance to constraints, causality, dynamical systems, emergence, teleonomy, or state-space framing.",
    "Require a link to a v4.9 claim category before candidate source creation.",
    "Allow contrast sources if they clarify boundaries.",
    "Require enough metadata for controlled logging.",
    "Require a decision rationale for candidate source creation.",
    "Defer sources that require full reading before classification.",
    "Do not retain any source during the shell stage.",
]


EXCLUSION_CRITERIA_LINKS = [
    "Exclude keyword-only matches without conceptual relevance.",
    "Exclude sources that encourage external-validation language.",
    "Exclude sources that imply biological, clinical, laboratory, or operational guidance.",
    "Exclude sources with insufficient metadata for controlled logging.",
    "Exclude sources that cannot be linked to a claim category.",
    "Exclude sources used only as decorative authority.",
    "Exclude sources whose source role cannot be defined.",
    "Exclude sources requiring invented bibliographic details.",
]


AUDIT_CHECKS_FOR_NEXT_MILESTONE = [
    "Verify that the run shell exists.",
    "Verify that search_run_status is planned_not_executed.",
    "Verify that no live search date has been recorded.",
    "Verify that raw_result_count remains pending.",
    "Verify that screened_result_count remains pending.",
    "Verify that candidate_source_count remains zero.",
    "Verify that retained_source_count remains zero.",
    "Verify that source_added_count remains zero.",
    "Verify that citation_added_count remains zero.",
    "Verify that evidence_matrix_populated_count remains zero.",
    "Verify that manuscript_revised_count remains zero.",
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
    "citation placeholders are not citations",
    "no live search is executed by this artifact",
    "no source is added by this artifact",
    "no citation is added by this artifact",
    "the evidence matrix is not populated by this artifact",
    "the manuscript is not revised by this artifact",
]


PROHIBITED_BEHAVIORS = [
    "Do not execute a live search in this milestone.",
    "Do not add real sources in this milestone.",
    "Do not add citations in this milestone.",
    "Do not invent authors, titles, venues, identifiers, or publication years.",
    "Do not populate the evidence matrix.",
    "Do not revise the manuscript.",
    "Do not treat a planned run shell as a completed search.",
    "Do not treat a planned query as evidence.",
    "Do not imply external validation.",
    "Do not imply submission readiness.",
    "Do not add biological, clinical, laboratory, or operational guidance.",
]


NEXT_STEPS = [
    "Audit this first search run shell.",
    "Execute the planned search only in a later milestone.",
    "Record the real search date during execution.",
    "Record raw result count during execution.",
    "Record screened result count after screening.",
    "Create candidate source entries only after screening.",
    "Audit candidate source entries before retention.",
    "Populate the evidence matrix only after retained-source audit.",
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
    r"\bcompleted search\b",
]


SAFE_LINE_CUES = [
    "not",
    "does not",
    "do not",
    "must not",
    "no live search",
    "no source",
    "no citation",
    "not allowed",
    "pending",
    "planned",
    "shell",
    "zero",
    "future",
    "later",
    "boundary",
    "prohibited",
    "exclude",
    "audit",
    "internal validation",
    "not externally",
    "not submission",
    "not a final",
    "not biological",
    "not clinical",
    "not laboratory",
    "not operational",
    "citation placeholders are not citations",
]


SAFE_SECTION_HEADINGS = [
    "boundary phrases",
    "prohibited behaviors",
    "exclusion criteria links",
    "execution gates",
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
class FirstSearchRunArtifactResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    run_shell_count: int
    executed_search_count: int
    run_shell_field_count: int
    pending_field_count: int
    execution_gate_count: int
    inclusion_link_count: int
    exclusion_link_count: int
    audit_check_count: int
    boundary_phrase_count: int
    prohibited_behavior_count: int
    next_step_count: int
    search_run_count: int
    candidate_source_count: int
    retained_source_count: int
    source_added_count: int
    citation_added_count: int
    evidence_matrix_populated_count: int
    manuscript_revised_count: int
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


def render_run_shell_table() -> str:
    rows = [
        "| Field | Value |",
        "|---|---|",
    ]
    for key, value in FIRST_SEARCH_RUN.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_field_table(fields: list[str]) -> str:
    rows = [
        "| Run shell field | v5.5 status |",
        "|---|---|",
    ]
    for field in fields:
        rows.append(f"| `{field}` | defined or pending for future real search |")
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

        if "citation placeholder" in lowered or "fake citation" in lowered:
            continue

        for pattern in FAKE_CITATION_PATTERNS:
            if re.search(pattern, stripped):
                findings.append(stripped)
                break

    return findings


def render_report() -> str:
    return f"""# First Search Run Artifact v5.5

## Question
Can Viruse Fabric instantiate the first controlled search-run shell without executing a live search, adding sources, adding citations, populating the evidence matrix, or revising the manuscript?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

No live search is executed by this artifact. No source is added by this artifact. No citation is added by this artifact. The evidence matrix is not populated by this artifact. The manuscript is not revised by this artifact. Citation placeholders are not citations.

## Source Artifacts
{render_source_table()}

## First Search Run Shell
{render_run_shell_table()}

## Run Shell Fields
{render_field_table(RUN_SHELL_FIELDS)}

## Pending Field Values
{bullet_list(PENDING_FIELD_VALUES)}

## Execution Gates
{bullet_list(EXECUTION_GATES)}

## Inclusion Criteria Links
{bullet_list(INCLUSION_CRITERIA_LINKS)}

## Exclusion Criteria Links
{bullet_list(EXCLUSION_CRITERIA_LINKS)}

## Audit Checks for Next Milestone
{bullet_list(AUDIT_CHECKS_FOR_NEXT_MILESTONE)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Artifact Logic
The first search run artifact is a shell, not an executed search.

It gives the next milestone a controlled object to audit before live search begins. The selected family, query, venue, claim category, and rationale are visible. Counts that depend on real search remain pending or zero. This prevents the project from quietly sliding from planning into evidence without a recorded transition.

A run shell is useful because it makes future execution auditable. When the live search occurs later, the diff should show exactly what changed: date, searcher, raw count, screened count, and candidate source count. If those fields appear without a dedicated search execution milestone, the process has failed. Software at least has the courtesy to fail loudly; humans tend to call it "workflow flexibility."

## Evidence Boundary
This artifact provides no evidence.

A planned query is not a search result. A search venue is not a source. A run identifier is not a citation. A pending count is not a measurement. A shell with zero candidates cannot support a manuscript claim.

The artifact exists so that later evidence can enter through a controlled path. First shell, then execution, then screening, then candidate audit, then retained-source decision, then evidence matrix population, then manuscript revision. Skipping these stages would be faster in the same way falling downstairs is faster than walking.

## Output Counts
Run shell count: 1

Executed search count: 0

Search run count: 0

Candidate source count: 0

Retained source count: 0

Source added count: 0

Citation added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact prepares the first future search run.

It does not execute a live search, does not add sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstSearchRunArtifactResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    run_shell_count = 1
    executed_search_count = 0
    search_run_count = 0
    candidate_source_count = 0
    retained_source_count = 0
    source_added_count = 0
    citation_added_count = 0
    evidence_matrix_populated_count = 0
    manuscript_revised_count = 0

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 6:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if run_shell_count != 1:
        errors.append(f"Run shell count should be one, got: {run_shell_count}")

    if executed_search_count != 0:
        errors.append(f"Executed search count should be zero, got: {executed_search_count}")

    if len(RUN_SHELL_FIELDS) < 18:
        errors.append(f"Run shell field count too low: {len(RUN_SHELL_FIELDS)}")

    if len(PENDING_FIELD_VALUES) < 8:
        errors.append(f"Pending field count too low: {len(PENDING_FIELD_VALUES)}")

    if len(EXECUTION_GATES) < 12:
        errors.append(f"Execution gate count too low: {len(EXECUTION_GATES)}")

    if len(INCLUSION_CRITERIA_LINKS) < 8:
        errors.append(f"Inclusion link count too low: {len(INCLUSION_CRITERIA_LINKS)}")

    if len(EXCLUSION_CRITERIA_LINKS) < 8:
        errors.append(f"Exclusion link count too low: {len(EXCLUSION_CRITERIA_LINKS)}")

    if len(AUDIT_CHECKS_FOR_NEXT_MILESTONE) < 10:
        errors.append(f"Audit check count too low: {len(AUDIT_CHECKS_FOR_NEXT_MILESTONE)}")

    if boundary_count < 13:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 10:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    for label, value in [
        ("Search run count", search_run_count),
        ("Candidate source count", candidate_source_count),
        ("Retained source count", retained_source_count),
        ("Source added count", source_added_count),
        ("Citation added count", citation_added_count),
        ("Evidence matrix populated count", evidence_matrix_populated_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if word_count < 1200:
        errors.append(f"Word count too low for first search run artifact: {word_count}")

    warnings.append("Artifact creates a search-run shell only; no live search is executed.")
    warnings.append("Artifact does not add sources, citations, evidence rows, or manuscript revisions.")

    passed = not errors

    interpretation = (
        "The v5.5 artifact instantiates one controlled first-search run shell "
        "without executing live search, adding sources, adding citations, "
        "populating the evidence matrix, or revising the manuscript."
    )

    return FirstSearchRunArtifactResult(
        title="First Search Run Artifact v5.5",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        run_shell_count=run_shell_count,
        executed_search_count=executed_search_count,
        run_shell_field_count=len(RUN_SHELL_FIELDS),
        pending_field_count=len(PENDING_FIELD_VALUES),
        execution_gate_count=len(EXECUTION_GATES),
        inclusion_link_count=len(INCLUSION_CRITERIA_LINKS),
        exclusion_link_count=len(EXCLUSION_CRITERIA_LINKS),
        audit_check_count=len(AUDIT_CHECKS_FOR_NEXT_MILESTONE),
        boundary_phrase_count=boundary_count,
        prohibited_behavior_count=prohibited_count,
        next_step_count=next_step_count,
        search_run_count=search_run_count,
        candidate_source_count=candidate_source_count,
        retained_source_count=retained_source_count,
        source_added_count=source_added_count,
        citation_added_count=citation_added_count,
        evidence_matrix_populated_count=evidence_matrix_populated_count,
        manuscript_revised_count=manuscript_revised_count,
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

    print("First Search Run Artifact v5.5")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Run shell count: {result.run_shell_count}")
    print(f"Executed search count: {result.executed_search_count}")
    print(f"Run shell field count: {result.run_shell_field_count}")
    print(f"Pending field count: {result.pending_field_count}")
    print(f"Execution gate count: {result.execution_gate_count}")
    print(f"Inclusion link count: {result.inclusion_link_count}")
    print(f"Exclusion link count: {result.exclusion_link_count}")
    print(f"Audit check count: {result.audit_check_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Search run count: {result.search_run_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
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
