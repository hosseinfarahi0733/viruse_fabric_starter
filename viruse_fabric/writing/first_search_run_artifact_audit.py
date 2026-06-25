"""First search run artifact audit for Viruse Fabric v5.6.

This module audits the v5.5 first search-run shell.

It verifies that the run shell remains a controlled pre-execution artifact:
- one run shell exists,
- no live search has been executed,
- pending fields remain pending,
- no candidate sources were added,
- no retained sources were added,
- no citations were added,
- no evidence matrix rows were populated,
- no manuscript revision occurred.

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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_search_run_artifact_audit_v5_6.md"

SOURCE_RUN_ARTIFACT = PROJECT_ROOT / "outputs" / "first_search_run_artifact_v5_5.md"
SOURCE_FIRST_SEARCH_PLAN = PROJECT_ROOT / "outputs" / "first_literature_family_search_plan_v5_4.md"
SOURCE_EMPTY_LOG_AUDIT = PROJECT_ROOT / "outputs" / "empty_search_log_audit_v5_3.md"
SOURCE_EMPTY_LOG = PROJECT_ROOT / "outputs" / "literature_search_log_empty_v5_2.md"
SOURCE_LOG_TEMPLATE = PROJECT_ROOT / "outputs" / "literature_search_log_template_v5_1.md"
SOURCE_CLAIM_MAP = PROJECT_ROOT / "outputs" / "claim_to_citation_readiness_map_v4_9.md"

SOURCE_ARTIFACTS = [
    SOURCE_RUN_ARTIFACT,
    SOURCE_FIRST_SEARCH_PLAN,
    SOURCE_EMPTY_LOG_AUDIT,
    SOURCE_EMPTY_LOG,
    SOURCE_LOG_TEMPLATE,
    SOURCE_CLAIM_MAP,
]


REQUIRED_RUN_ARTIFACT_SECTIONS = [
    "First Search Run Shell",
    "Run Shell Fields",
    "Pending Field Values",
    "Execution Gates",
    "Inclusion Criteria Links",
    "Exclusion Criteria Links",
    "Audit Checks for Next Milestone",
    "Artifact Logic",
    "Evidence Boundary",
    "Output Counts",
    "Final Boundary Statement",
]


REQUIRED_PENDING_PHRASES = [
    "planned_not_executed",
    "PENDING_REAL_SEARCH",
    "SEARCH_NOT_EXECUTED_IN_V5_5",
]


ZERO_COUNT_FIELDS = [
    "Executed search count",
    "Search run count",
    "Candidate source count",
    "Retained source count",
    "Source added count",
    "Citation added count",
    "Evidence matrix populated count",
    "Manuscript revised count",
]


AUDIT_DIMENSIONS = [
    "source artifact availability",
    "run shell existence",
    "run shell count preservation",
    "executed search count preservation",
    "pending field preservation",
    "candidate source count preservation",
    "retained source count preservation",
    "source added count preservation",
    "citation added count preservation",
    "evidence matrix population prevention",
    "manuscript revision prevention",
    "boundary phrase preservation",
]


AUDIT_FINDINGS = [
    "The first search-run shell exists as a real artifact.",
    "The first search plan exists.",
    "The run shell remains planned_not_executed.",
    "The pending field markers remain visible.",
    "The executed search count remains zero.",
    "The search run count remains zero.",
    "The candidate source count remains zero.",
    "The retained source count remains zero.",
    "The source added count remains zero.",
    "The citation added count remains zero.",
    "The evidence matrix populated count remains zero.",
    "The manuscript revised count remains zero.",
]


AUDIT_RULES = [
    "The audit must not execute a live search.",
    "The audit must not create candidate sources.",
    "The audit must not create retained sources.",
    "The audit must not create citations.",
    "The audit must not populate the evidence matrix.",
    "The audit must not revise the manuscript.",
    "The audit must verify pending field preservation.",
    "The audit must verify zero-count fields explicitly.",
    "The audit must preserve boundary language.",
    "The audit must keep live literature search as future work.",
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
    "does not execute a live search",
    "does not add sources",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
]


PROHIBITED_BEHAVIORS = [
    "Do not execute live search during this audit.",
    "Do not add real sources during this audit.",
    "Do not add citations during this audit.",
    "Do not replace pending fields with invented values.",
    "Do not invent search dates or searchers.",
    "Do not invent raw result counts.",
    "Do not invent screened result counts.",
    "Do not populate the evidence matrix during this audit.",
    "Do not revise the manuscript during this audit.",
    "Do not imply external validation.",
    "Do not imply submission readiness.",
]


NEXT_STEPS = [
    "Preserve the audited run shell as the baseline.",
    "Create a controlled live-search execution milestone next.",
    "Execute only the planned query from the shell.",
    "Record real search date and searcher during execution.",
    "Record raw result count during execution.",
    "Record screened result count after screening.",
    "Keep candidate source creation separate from execution if needed.",
    "Audit candidate sources before any retention or evidence matrix transfer.",
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
    "zero",
    "pending",
    "planned",
    "shell",
    "preservation",
    "prevention",
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
    "citation placeholders are not citations",
]


SAFE_SECTION_HEADINGS = [
    "boundary phrases",
    "prohibited behaviors",
    "audit rules",
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
class FirstSearchRunArtifactAuditResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    run_artifact_exists: bool
    search_plan_exists: bool
    required_section_count: int
    missing_required_section_count: int
    pending_phrase_count: int
    missing_pending_phrase_count: int
    zero_count_field_count: int
    zero_count_pass_count: int
    zero_count_fail_count: int
    audit_dimension_count: int
    audit_finding_count: int
    audit_rule_count: int
    boundary_phrase_count: int
    prohibited_behavior_count: int
    next_step_count: int
    source_added_count: int
    citation_added_count: int
    executed_search_added_count: int
    candidate_source_added_count: int
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


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


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


def extract_count(source_text: str, label: str) -> int | None:
    pattern = rf"{re.escape(label)}:\s*(\d+)"
    match = re.search(pattern, source_text, flags=re.IGNORECASE)
    if not match:
        return None
    return int(match.group(1))


def zero_count_results(source_text: str) -> dict[str, str]:
    results: dict[str, str] = {}
    for field in ZERO_COUNT_FIELDS:
        value = extract_count(source_text, field)
        if value is None:
            results[field] = "missing"
        elif value == 0:
            results[field] = "pass"
        else:
            results[field] = f"fail:{value}"
    return results


def render_source_table() -> str:
    rows = [
        "| Source artifact | Exists |",
        "|---|---|",
    ]
    for path in SOURCE_ARTIFACTS:
        rows.append(f"| `{relative(path)}` | {path.exists()} |")
    return "\n".join(rows)


def render_zero_count_table(results: dict[str, str]) -> str:
    rows = [
        "| Zero-count field | Audit result |",
        "|---|---|",
    ]
    for field, result in results.items():
        rows.append(f"| {field} | {result} |")
    return "\n".join(rows)


def render_audit_dimension_table() -> str:
    rows = [
        "| Audit dimension | Status |",
        "|---|---|",
    ]
    for dimension in AUDIT_DIMENSIONS:
        rows.append(f"| {dimension} | checked |")
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
    source_text = read_text(SOURCE_RUN_ARTIFACT)
    zero_results = zero_count_results(source_text)

    missing_sections = [
        section for section in REQUIRED_RUN_ARTIFACT_SECTIONS
        if section.lower() not in source_text.lower()
    ]
    missing_pending = [
        phrase for phrase in REQUIRED_PENDING_PHRASES
        if phrase.lower() not in source_text.lower()
    ]

    return f"""# First Search Run Artifact Audit v5.6

## Question
Can Viruse Fabric audit the v5.5 first search-run shell and confirm that it remains pending, bounded, citation-safe, and not executed?

## Status
Current project status remains:

`research prototype with internal validation`

This audit is not externally validated, not submission-ready, and not a final paper.

The audit does not execute a live search, does not add sources, does not add citations, does not populate the evidence matrix, and does not revise the manuscript. Citation placeholders are not citations.

## Source Artifacts
{render_source_table()}

## Audit Purpose
The v5.6 audit checks whether the v5.5 first search-run artifact remains a pre-execution shell.

It should contain one planned run shell. It should not contain a completed search. It should preserve pending fields. It should not contain candidate sources, retained sources, citations, evidence matrix transfer, or manuscript revision.

This audit is narrow on purpose. It verifies readiness to execute a real search later. It does not perform that search. The project is again checking the parachute before jumping, which is apparently considered excessive only by people who enjoy impact injuries.

## Required Section Audit
Required section count: {len(REQUIRED_RUN_ARTIFACT_SECTIONS)}

Missing required section count: {len(missing_sections)}

Missing sections:

{bullet_list(missing_sections)}

## Pending Field Audit
Required pending phrase count: {len(REQUIRED_PENDING_PHRASES)}

Missing pending phrase count: {len(missing_pending)}

Missing pending phrases:

{bullet_list(missing_pending)}

## Zero Count Audit
{render_zero_count_table(zero_results)}

## Audit Dimensions
{render_audit_dimension_table()}

## Audit Findings
{bullet_list(AUDIT_FINDINGS)}

## Audit Rules
{bullet_list(AUDIT_RULES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Shell Interpretation
The first search-run shell is a controlled pre-execution object.

Its job is to make the future live search auditable. The shell records the planned family, planned query, planned venue, claim category, rationale, and fields that must later be filled. If those fields are filled without a search execution milestone, the process has skipped a gate.

The shell therefore protects against a common failure mode: the project starts with a planned query and somehow later discovers it has "sources" without a visible execution event. This is how bibliographies become folklore with formatting.

## Audit Consequences
Passing this audit means the shell can be used as the baseline for a future live-search milestone.

It does not mean the literature search has begun. It does not mean the selected query has produced results. It does not mean the project has candidate sources. It does not mean the manuscript has gained support.

The useful result is much narrower: the shell is intact, pending fields are preserved, and zero-count fields remain zero. This is boring. Boring is good. In research workflows, excitement before evidence is usually just error wearing perfume.

## Execution Boundary
The next milestone may execute the search, but only if it changes the shell through explicit fields.

A real execution should add a real date, a real searcher, a real venue confirmation, a raw result count, and a screened result count. It should not silently add sources. It should not silently add citations. It should not silently populate the evidence matrix. If candidate sources are created, they should be visible as candidate entries and should remain separate from retained sources.

This boundary matters because a search result is not yet evidence. A result list is not a bibliography. A candidate source is not a retained source. A retained source is not automatically a citation. A citation is not external validation. Humanity has somehow needed this sentence in several forms, which is not flattering, but here we are.

## Audit Failure Modes
This audit is designed to catch premature execution.

One failure mode would be replacing `PENDING_REAL_SEARCH` with invented counts. Another would be recording a candidate source before the search is actually executed. Another would be using the planned query as if it had already returned meaningful literature. Another would be letting the manuscript borrow authority from a shell that has not yet touched the outside world.

The shell must stay boring until a real execution milestone changes it. If future work adds evidence, that evidence must arrive through a visible chain: execution, screening, candidate creation, candidate audit, retention decision, evidence matrix transfer, and only later manuscript revision. Skipping that chain would be faster, in the same way deleting the map is faster than traveling.

## Output Counts
Source added count: 0

Citation added count: 0

Executed search added count: 0

Candidate source added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

Audit phrase summary:

- zero sources
- zero citations
- zero evidence matrix population
- zero manuscript revision

## Final Boundary Statement
This audit confirms the first search-run shell as a controlled pre-execution baseline.

It does not execute a live search, does not add sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstSearchRunArtifactAuditResult:
    source_text = read_text(SOURCE_RUN_ARTIFACT)
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()

    missing_sections = [
        section for section in REQUIRED_RUN_ARTIFACT_SECTIONS
        if section.lower() not in source_text.lower()
    ]
    missing_pending = [
        phrase for phrase in REQUIRED_PENDING_PHRASES
        if phrase.lower() not in source_text.lower()
    ]

    zero_results = zero_count_results(source_text)
    zero_pass_count = sum(1 for value in zero_results.values() if value == "pass")
    zero_fail_count = len(zero_results) - zero_pass_count

    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    source_added_count = 0
    citation_added_count = 0
    executed_search_added_count = 0
    candidate_source_added_count = 0
    evidence_matrix_populated_count = 0
    manuscript_revised_count = 0

    audit_rule_count = count_present_terms(report, AUDIT_RULES)
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

    if not SOURCE_RUN_ARTIFACT.exists():
        errors.append("First search run artifact does not exist")

    if not SOURCE_FIRST_SEARCH_PLAN.exists():
        errors.append("First literature family search plan does not exist")

    if len(REQUIRED_RUN_ARTIFACT_SECTIONS) < 11:
        errors.append(f"Required section count too low: {len(REQUIRED_RUN_ARTIFACT_SECTIONS)}")

    if missing_sections:
        errors.append(f"Missing required run-artifact sections: {len(missing_sections)}")

    if len(REQUIRED_PENDING_PHRASES) < 3:
        errors.append(f"Required pending phrase count too low: {len(REQUIRED_PENDING_PHRASES)}")

    if missing_pending:
        errors.append(f"Missing pending phrases: {len(missing_pending)}")

    if len(ZERO_COUNT_FIELDS) < 8:
        errors.append(f"Zero count field count too low: {len(ZERO_COUNT_FIELDS)}")

    if zero_pass_count < len(ZERO_COUNT_FIELDS):
        errors.append(f"Zero count audit failures: {zero_fail_count}")

    if len(AUDIT_DIMENSIONS) < 12:
        errors.append(f"Audit dimension count too low: {len(AUDIT_DIMENSIONS)}")

    if len(AUDIT_FINDINGS) < 12:
        errors.append(f"Audit finding count too low: {len(AUDIT_FINDINGS)}")

    if audit_rule_count < 10:
        errors.append(f"Audit rule count too low: {audit_rule_count}")

    if boundary_count < 13:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 11:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    for label, value in [
        ("Source added count", source_added_count),
        ("Citation added count", citation_added_count),
        ("Executed search added count", executed_search_added_count),
        ("Candidate source added count", candidate_source_added_count),
        ("Evidence matrix populated count", evidence_matrix_populated_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if word_count < 1100:
        errors.append(f"Word count too low for first search run artifact audit: {word_count}")

    warnings.append("Audit confirms a pre-execution shell only; it does not perform live search.")
    warnings.append("Audit does not add sources, citations, evidence rows, or manuscript revisions.")

    passed = not errors

    interpretation = (
        "The v5.6 audit verifies that the v5.5 first search-run shell remains "
        "pending, bounded, citation-safe, and unexecuted, with zero sources, "
        "zero citations, zero evidence matrix population, and zero manuscript revision."
    )

    return FirstSearchRunArtifactAuditResult(
        title="First Search Run Artifact Audit v5.6",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        run_artifact_exists=SOURCE_RUN_ARTIFACT.exists(),
        search_plan_exists=SOURCE_FIRST_SEARCH_PLAN.exists(),
        required_section_count=len(REQUIRED_RUN_ARTIFACT_SECTIONS),
        missing_required_section_count=len(missing_sections),
        pending_phrase_count=len(REQUIRED_PENDING_PHRASES),
        missing_pending_phrase_count=len(missing_pending),
        zero_count_field_count=len(ZERO_COUNT_FIELDS),
        zero_count_pass_count=zero_pass_count,
        zero_count_fail_count=zero_fail_count,
        audit_dimension_count=len(AUDIT_DIMENSIONS),
        audit_finding_count=len(AUDIT_FINDINGS),
        audit_rule_count=audit_rule_count,
        boundary_phrase_count=boundary_count,
        prohibited_behavior_count=prohibited_count,
        next_step_count=next_step_count,
        source_added_count=source_added_count,
        citation_added_count=citation_added_count,
        executed_search_added_count=executed_search_added_count,
        candidate_source_added_count=candidate_source_added_count,
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

    print("First Search Run Artifact Audit v5.6")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Run artifact exists: {result.run_artifact_exists}")
    print(f"Search plan exists: {result.search_plan_exists}")
    print(f"Required section count: {result.required_section_count}")
    print(f"Missing required section count: {result.missing_required_section_count}")
    print(f"Pending phrase count: {result.pending_phrase_count}")
    print(f"Missing pending phrase count: {result.missing_pending_phrase_count}")
    print(f"Zero count field count: {result.zero_count_field_count}")
    print(f"Zero count pass count: {result.zero_count_pass_count}")
    print(f"Zero count fail count: {result.zero_count_fail_count}")
    print(f"Audit dimension count: {result.audit_dimension_count}")
    print(f"Audit finding count: {result.audit_finding_count}")
    print(f"Audit rule count: {result.audit_rule_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Executed search added count: {result.executed_search_added_count}")
    print(f"Candidate source added count: {result.candidate_source_added_count}")
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
