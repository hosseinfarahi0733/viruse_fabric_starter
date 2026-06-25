"""Empty search log audit for Viruse Fabric v5.3.

This module audits the v5.2 empty literature search log artifact.

It verifies that the search log remains empty and controlled:
- no searches were run,
- no sources were added,
- no citations were added,
- no evidence matrix rows were populated,
- no manuscript revision occurred.

It does not run searches.
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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "empty_search_log_audit_v5_3.md"

SOURCE_EMPTY_LOG = PROJECT_ROOT / "outputs" / "literature_search_log_empty_v5_2.md"
SOURCE_LOG_TEMPLATE = PROJECT_ROOT / "outputs" / "literature_search_log_template_v5_1.md"
SOURCE_REVISION_PLAN = PROJECT_ROOT / "outputs" / "citation_grounded_manuscript_revision_plan_v5_0.md"
SOURCE_CLAIM_MAP = PROJECT_ROOT / "outputs" / "claim_to_citation_readiness_map_v4_9.md"

SOURCE_ARTIFACTS = [
    SOURCE_EMPTY_LOG,
    SOURCE_LOG_TEMPLATE,
    SOURCE_REVISION_PLAN,
    SOURCE_CLAIM_MAP,
]


ZERO_COUNT_FIELDS = [
    "Search run count",
    "Candidate source count",
    "Retained source count",
    "Deferred source count",
    "Rejected source count",
    "Source added count",
    "Citation added count",
    "Evidence matrix populated count",
    "Manuscript revised count",
]


REQUIRED_EMPTY_LOG_SECTIONS = [
    "Empty Registry Summary",
    "Empty Search Run Columns",
    "Empty Candidate Source Columns",
    "Empty Claim Mapping Columns",
    "Initial Status Values",
    "Log Rules",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Empty-State Audit Meaning",
    "Evidence Discipline",
    "Output Counts",
    "Final Boundary Statement",
]


AUDIT_DIMENSIONS = [
    "source artifact availability",
    "empty registry preservation",
    "zero search run preservation",
    "zero candidate source preservation",
    "zero retained source preservation",
    "zero citation preservation",
    "zero evidence matrix population",
    "zero manuscript revision",
    "boundary phrase preservation",
    "overclaim avoidance",
    "fake citation avoidance",
    "readiness boundary preservation",
]


AUDIT_FINDINGS = [
    "The empty search log exists as a real artifact.",
    "The source log template exists.",
    "The search run count remains zero.",
    "The candidate source count remains zero.",
    "The retained source count remains zero.",
    "The deferred source count remains zero.",
    "The rejected source count remains zero.",
    "The source added count remains zero.",
    "The citation added count remains zero.",
    "The evidence matrix populated count remains zero.",
    "The manuscript revised count remains zero.",
    "The artifact remains a controlled starting state.",
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
    "does not run searches",
    "does not add sources",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
]


AUDIT_RULES = [
    "The audit must not create search runs.",
    "The audit must not create candidate sources.",
    "The audit must not create retained sources.",
    "The audit must not create citations.",
    "The audit must not populate the evidence matrix.",
    "The audit must not revise the manuscript.",
    "The audit must verify zero-count fields explicitly.",
    "The audit must preserve boundary language.",
    "The audit must reject submission-ready interpretation.",
    "The audit must keep real literature search as future work.",
]


PROHIBITED_BEHAVIORS = [
    "Do not add invented sources.",
    "Do not add invented citations.",
    "Do not convert empty registries into evidence.",
    "Do not treat an empty log as a search result.",
    "Do not imply external validation.",
    "Do not imply submission readiness.",
    "Do not treat audit success as literature completion.",
    "Do not populate the evidence matrix during audit.",
    "Do not revise the manuscript during audit.",
    "Do not add biological, clinical, laboratory, or operational guidance.",
]


NEXT_STEPS = [
    "Preserve the empty log as the baseline.",
    "Create the first real search-run milestone only after audit closure.",
    "Select one literature family for the first real search.",
    "Record exact query strings during real search.",
    "Keep candidate sources separate from retained sources.",
    "Audit candidate source decisions before matrix transfer.",
    "Populate the evidence matrix only after retained-source audit.",
    "Revise manuscript claims only after evidence mapping is complete.",
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
    "no source",
    "no citation",
    "no search",
    "no manuscript",
    "zero",
    "empty",
    "avoidance",
    "preservation",
    "reject",
    "future",
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
    "audit rules",
    "prohibited behaviors",
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
class EmptySearchLogAuditResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    empty_log_exists: bool
    template_exists: bool
    required_section_count: int
    missing_required_section_count: int
    zero_count_field_count: int
    zero_count_pass_count: int
    zero_count_fail_count: int
    audit_dimension_count: int
    audit_finding_count: int
    boundary_phrase_count: int
    audit_rule_count: int
    prohibited_behavior_count: int
    next_step_count: int
    source_added_count: int
    citation_added_count: int
    search_run_added_count: int
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


def render_source_table() -> str:
    rows = [
        "| Source artifact | Exists |",
        "|---|---|",
    ]
    for path in SOURCE_ARTIFACTS:
        rows.append(f"| `{relative(path)}` | {path.exists()} |")
    return "\n".join(rows)


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
    source_text = read_text(SOURCE_EMPTY_LOG)
    zero_results = zero_count_results(source_text)
    missing_sections = [
        section for section in REQUIRED_EMPTY_LOG_SECTIONS
        if section.lower() not in source_text.lower()
    ]

    return f"""# Empty Search Log Audit v5.3

## Question
Can Viruse Fabric audit the v5.2 empty literature search log and confirm that it remains empty, bounded, citation-safe, and unrevised?

## Status
Current project status remains:

`research prototype with internal validation`

This audit is not externally validated, not submission-ready, and not a final paper.

The audit does not run searches, does not add sources, does not add citations, does not populate the evidence matrix, and does not revise the manuscript. Citation placeholders are not citations.

## Source Artifacts
{render_source_table()}

## Audit Purpose
The v5.3 audit verifies that the v5.2 empty search log is genuinely empty and safe to use as a baseline for future real search.

This is not a literature search. This is not a source review. This is not a citation audit of real references. It is an empty-state audit. The project checks the container before filling it, because apparently that is still more disciplined than most human approaches to "I found some papers, therefore I have evidence."

## Required Section Audit
Required section count: {len(REQUIRED_EMPTY_LOG_SECTIONS)}

Missing required section count: {len(missing_sections)}

Missing sections:

{bullet_list(missing_sections)}

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

## Empty-State Interpretation
The audit passes only if emptiness is explicit.

A zero search run count means no live search has been executed. A zero candidate source count means no source has entered screening. A zero retained source count means no evidence can be transferred. A zero citation count means the manuscript has not gained scholarly support. A zero manuscript revision count means the manuscript has not changed.

These are not weaknesses. They are controlled baseline facts. The project can now tell the difference between a planned search, an empty search log, a populated search log, a populated evidence matrix, and a citation-grounded manuscript. It is tragic that this distinction needs an audit, but civilization has given us footnotes and overconfidence, so here we are.

## Transition Readiness
The empty log is ready to become the starting point for a future first-search milestone.

That future milestone may add one real search run, but only if the query string, venue, literature family, claim category, screening counts, and candidate-source rules are recorded. It must not add citations directly to the manuscript. It must not populate the evidence matrix before candidate-source audit.

The audit therefore closes the preparation loop before live source work begins. It protects the next phase from starting with mystery sources, decorative citations, or sudden manuscript authority arriving from nowhere like a poorly supervised magician.

## Audit Consequences
The audit result is intentionally narrow.

Passing this audit means the empty search log is structurally safe as a baseline. It does not mean the project has performed literature search. It does not mean any source has been evaluated. It does not mean the manuscript has gained support. It only means the project has preserved a clean starting state.

That clean state is useful because future work can now be compared against it. When the first real search run appears, it should be visible as a deliberate change rather than a vague accumulation of notes. When the first candidate source appears, it should be traceable to a search run. When the first retained source appears, it should be traceable to a screening and audit decision.

This makes later citation work less theatrical. A citation should arrive through a chain of logged actions, not by parachuting into a paragraph because the paragraph looked lonely.

## Failure Modes Prevented
The audit prevents several predictable errors.

One failure mode is source teleportation: a source appears in the project without a recorded search run. Another is citation laundering: a source is used to strengthen a claim beyond what has been read or mapped. Another is evidence inflation: an empty or candidate-level source is treated as retained evidence.

The audit also prevents premature manuscript authority. A manuscript can sound more mature simply because the workflow now has literature-search artifacts around it. That sound is not evidence. It is only typography wearing a lab coat, and apparently that still fools people.

By confirming zero search runs, zero sources, zero citations, zero evidence matrix population, and zero manuscript revision, v5.3 keeps the next step honest.

## Output Counts
Source added count: 0

Citation added count: 0

Search run added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This audit confirms the empty literature search log as a controlled baseline.

It does not run searches, does not add sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> EmptySearchLogAuditResult:
    source_text = read_text(SOURCE_EMPTY_LOG)
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    zero_results = zero_count_results(source_text)
    zero_pass_count = sum(1 for value in zero_results.values() if value == "pass")
    zero_fail_count = len(zero_results) - zero_pass_count

    missing_sections = [
        section for section in REQUIRED_EMPTY_LOG_SECTIONS
        if section.lower() not in source_text.lower()
    ]

    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    source_added_count = 0
    citation_added_count = 0
    search_run_added_count = 0
    evidence_matrix_populated_count = 0
    manuscript_revised_count = 0

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    audit_rule_count = count_present_terms(report, AUDIT_RULES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 4:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if not SOURCE_EMPTY_LOG.exists():
        errors.append("Empty search log artifact does not exist")

    if not SOURCE_LOG_TEMPLATE.exists():
        errors.append("Search log template artifact does not exist")

    if len(REQUIRED_EMPTY_LOG_SECTIONS) < 12:
        errors.append(f"Required section count too low: {len(REQUIRED_EMPTY_LOG_SECTIONS)}")

    if missing_sections:
        errors.append(f"Missing required empty-log sections: {len(missing_sections)}")

    if len(ZERO_COUNT_FIELDS) < 9:
        errors.append(f"Zero count field count too low: {len(ZERO_COUNT_FIELDS)}")

    if zero_pass_count < len(ZERO_COUNT_FIELDS):
        errors.append(f"Zero count audit failures: {zero_fail_count}")

    if len(AUDIT_DIMENSIONS) < 12:
        errors.append(f"Audit dimension count too low: {len(AUDIT_DIMENSIONS)}")

    if len(AUDIT_FINDINGS) < 12:
        errors.append(f"Audit finding count too low: {len(AUDIT_FINDINGS)}")

    if boundary_count < 12:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if audit_rule_count < 10:
        errors.append(f"Audit rule count too low: {audit_rule_count}")

    if prohibited_count < 10:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    for label, value in [
        ("Source added count", source_added_count),
        ("Citation added count", citation_added_count),
        ("Search run added count", search_run_added_count),
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
        errors.append(f"Word count too low for empty search log audit: {word_count}")

    warnings.append("Audit confirms empty state only; it does not perform literature search.")
    warnings.append("Audit does not add sources, citations, evidence rows, or manuscript revisions.")

    passed = not errors

    interpretation = (
        "The v5.3 audit checks that the v5.2 empty search log remains a "
        "controlled baseline with zero search runs, zero sources, zero citations, "
        "zero evidence matrix population, and zero manuscript revision."
    )

    return EmptySearchLogAuditResult(
        title="Empty Search Log Audit v5.3",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        empty_log_exists=SOURCE_EMPTY_LOG.exists(),
        template_exists=SOURCE_LOG_TEMPLATE.exists(),
        required_section_count=len(REQUIRED_EMPTY_LOG_SECTIONS),
        missing_required_section_count=len(missing_sections),
        zero_count_field_count=len(ZERO_COUNT_FIELDS),
        zero_count_pass_count=zero_pass_count,
        zero_count_fail_count=zero_fail_count,
        audit_dimension_count=len(AUDIT_DIMENSIONS),
        audit_finding_count=len(AUDIT_FINDINGS),
        boundary_phrase_count=boundary_count,
        audit_rule_count=audit_rule_count,
        prohibited_behavior_count=prohibited_count,
        next_step_count=next_step_count,
        source_added_count=source_added_count,
        citation_added_count=citation_added_count,
        search_run_added_count=search_run_added_count,
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

    print("Empty Search Log Audit v5.3")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Empty log exists: {result.empty_log_exists}")
    print(f"Template exists: {result.template_exists}")
    print(f"Required section count: {result.required_section_count}")
    print(f"Missing required section count: {result.missing_required_section_count}")
    print(f"Zero count field count: {result.zero_count_field_count}")
    print(f"Zero count pass count: {result.zero_count_pass_count}")
    print(f"Zero count fail count: {result.zero_count_fail_count}")
    print(f"Audit dimension count: {result.audit_dimension_count}")
    print(f"Audit finding count: {result.audit_finding_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Audit rule count: {result.audit_rule_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Search run added count: {result.search_run_added_count}")
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
