"""Literature search log template for Viruse Fabric v5.1.

This module generates a controlled literature search log template.

It connects:
- the v4.7 literature search protocol,
- the v4.8 literature family evidence matrix,
- the v4.9 claim-to-citation readiness map,
- the v5.0 citation-grounded manuscript revision plan,
- the v3.9 citation placeholder plan.

It does not run literature searches.
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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "literature_search_log_template_v5_1.md"

SOURCE_SEARCH_PROTOCOL = PROJECT_ROOT / "outputs" / "literature_search_protocol_v4_7.md"
SOURCE_EVIDENCE_MATRIX = PROJECT_ROOT / "outputs" / "literature_family_evidence_matrix_v4_8.md"
SOURCE_CLAIM_MAP = PROJECT_ROOT / "outputs" / "claim_to_citation_readiness_map_v4_9.md"
SOURCE_REVISION_PLAN = PROJECT_ROOT / "outputs" / "citation_grounded_manuscript_revision_plan_v5_0.md"
SOURCE_CITATION_PLAN = PROJECT_ROOT / "outputs" / "citation_placeholder_plan_v3_9.md"

SOURCE_ARTIFACTS = [
    SOURCE_SEARCH_PROTOCOL,
    SOURCE_EVIDENCE_MATRIX,
    SOURCE_CLAIM_MAP,
    SOURCE_REVISION_PLAN,
    SOURCE_CITATION_PLAN,
]


SEARCH_LOG_FIELDS = [
    "search_run_id",
    "search_date",
    "searcher",
    "literature_family",
    "claim_category",
    "search_venue",
    "query_string",
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


SOURCE_REVIEW_FIELDS = [
    "candidate_source_id",
    "source_status",
    "source_role",
    "title_pending",
    "author_pending",
    "year_pending",
    "venue_pending",
    "identifier_pending",
    "abstract_screening_notes",
    "relevant_passage_notes",
    "claim_link",
    "evidence_strength",
    "boundary_effect",
    "decision",
    "decision_rationale",
    "audit_notes",
]


CLAIM_MAPPING_FIELDS = [
    "claim_id",
    "claim_text",
    "readiness_category",
    "citation_action",
    "evidence_need",
    "allowed_use_level",
    "validation_boundary",
    "candidate_source_id",
    "source_role",
    "decision",
    "revision_instruction",
]


SOURCE_STATUS_VALUES = [
    "unreviewed",
    "screened",
    "candidate",
    "retained",
    "deferred",
    "rejected",
]


SOURCE_ROLE_VALUES = [
    "background",
    "terminology",
    "comparison",
    "contrast",
    "method_context",
    "boundary_context",
]


DECISION_VALUES = [
    "retain_for_later_mapping",
    "defer_pending_full_read",
    "reject_as_irrelevant",
    "reject_as_overclaim_risk",
    "reject_as_insufficient_support",
]


AUDIT_RULES = [
    "Every search run must record the exact query string.",
    "Every candidate source must be linked to a literature family.",
    "Every candidate source must be linked to at least one claim category before manuscript use.",
    "Every retained source must have a source role.",
    "Every retained source must have a decision rationale.",
    "No source can be cited before relevant passages are reviewed.",
    "No source can be used to imply external validation.",
    "No citation placeholder can be converted into a citation.",
    "No source can be inserted directly into the manuscript from this log template.",
    "A populated search log must be audited before evidence matrix population.",
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
    "no source is added by this template",
    "no citation is added by this template",
    "the evidence matrix is not populated by this template",
    "the manuscript is not revised by this template",
]


PROHIBITED_BEHAVIORS = [
    "Do not add invented sources.",
    "Do not add invented citations.",
    "Do not record fake author names.",
    "Do not record fake identifiers.",
    "Do not cite unread sources.",
    "Do not treat search results as retained evidence.",
    "Do not treat a candidate source as a validated source.",
    "Do not use sources as decorative authority.",
    "Do not imply external validation from literature context.",
    "Do not use this template as a submission-ready bibliography.",
]


NEXT_STEPS = [
    "Create a real search log file from this template.",
    "Run searches family by family.",
    "Record each query string exactly.",
    "Screen results using inclusion and exclusion criteria.",
    "Record candidate sources without citing them yet.",
    "Audit candidate source decisions.",
    "Populate the evidence matrix only after candidate audit.",
    "Prepare citation-grounded manuscript notes only after retained sources are mapped.",
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
    r"\bsubmission-ready bibliography\b",
]


SAFE_LINE_CUES = [
    "not",
    "does not",
    "do not",
    "must not",
    "no source",
    "no citation",
    "no source can",
    "no citation placeholder",
    "cannot",
    "template",
    "boundary",
    "prohibited",
    "future",
    "pending",
    "reject",
    "unreviewed",
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
class LiteratureSearchLogTemplateResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    search_log_field_count: int
    source_review_field_count: int
    claim_mapping_field_count: int
    source_status_value_count: int
    source_role_value_count: int
    decision_value_count: int
    audit_rule_count: int
    boundary_phrase_count: int
    prohibited_behavior_count: int
    next_step_count: int
    source_added_count: int
    citation_added_count: int
    populated_source_count: int
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


def render_field_table(title: str, fields: list[str]) -> str:
    rows = [
        f"| {title} field | Required | Purpose |",
        "|---|---|---|",
    ]
    for field in fields:
        readable = field.replace("_", " ")
        rows.append(f"| `{field}` | yes | record {readable} for controlled later audit |")
    return "\n".join(rows)


def render_value_table(title: str, values: list[str]) -> str:
    rows = [
        f"| {title} value | Meaning |",
        "|---|---|",
    ]
    for value in values:
        rows.append(f"| `{value}` | controlled value for later review and audit |")
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
    return f"""# Literature Search Log Template v5.1

## Question
Can Viruse Fabric create a controlled template for future literature search logging without adding sources, adding citations, populating the evidence matrix, or revising the manuscript?

## Status
Current project status remains:

`research prototype with internal validation`

This template is not externally validated, not submission-ready, and not a final paper.

No source is added by this template. No citation is added by this template. The evidence matrix is not populated by this template. The manuscript is not revised by this template. Citation placeholders are not citations.

## Source Artifacts
{render_source_table()}

## Purpose
The v5.1 template defines how future search activity should be recorded before any evidence matrix is populated.

It is a log structure, not a search result. It is a control layer between search protocol and evidence population. That sounds bureaucratic because it is, but bureaucracy is occasionally what keeps a research prototype from turning into a decorative bibliography with delusions of grandeur.

## Search Run Fields
{render_field_table("Search run", SEARCH_LOG_FIELDS)}

## Candidate Source Review Fields
{render_field_table("Candidate source review", SOURCE_REVIEW_FIELDS)}

## Claim Mapping Fields
{render_field_table("Claim mapping", CLAIM_MAPPING_FIELDS)}

## Source Status Values
{render_value_table("Source status", SOURCE_STATUS_VALUES)}

## Source Role Values
{render_value_table("Source role", SOURCE_ROLE_VALUES)}

## Decision Values
{render_value_table("Decision", DECISION_VALUES)}

## Empty Search Run Template
| Field | Value |
|---|---|
| `search_run_id` | `SEARCH_RUN_ID_PENDING` |
| `search_date` | `DATE_PENDING` |
| `literature_family` | `FAMILY_PENDING` |
| `claim_category` | `CLAIM_CATEGORY_PENDING` |
| `search_venue` | `VENUE_PENDING` |
| `query_string` | `QUERY_STRING_PENDING` |
| `raw_result_count` | `COUNT_PENDING` |
| `candidate_source_count` | `COUNT_PENDING` |
| `retained_source_count` | `0` |
| `notes` | `NOTES_PENDING` |

## Empty Candidate Source Template
| Field | Value |
|---|---|
| `candidate_source_id` | `SOURCE_ID_PENDING` |
| `source_status` | `unreviewed` |
| `source_role` | `ROLE_PENDING` |
| `title_pending` | `TITLE_PENDING` |
| `author_pending` | `AUTHOR_PENDING` |
| `year_pending` | `YEAR_PENDING` |
| `identifier_pending` | `IDENTIFIER_PENDING` |
| `claim_link` | `CLAIM_ID_PENDING` |
| `decision` | `DECISION_PENDING` |
| `decision_rationale` | `RATIONALE_PENDING` |

## Audit Rules
{bullet_list(AUDIT_RULES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Template Use Logic
The search log should be created before live literature search begins.

Each search run should record the exact query string, venue, family, claim category, and screening outcome. Each candidate source should remain a candidate until it is read and mapped. Retained sources should move into the evidence matrix only after audit.

This template prevents a common failure mode: finding a source, liking its title, and then letting the manuscript pretend the source already supports the claim. The human brain is very talented at mistaking familiarity for evidence, which is charming in a campfire story and useless in a manuscript.

## Relationship to Evidence Matrix
The evidence matrix remains empty until real candidate sources pass review.

The log records search activity. The matrix records evidence decisions. The manuscript uses neither directly until the relevant source role, claim link, decision value, and boundary effect are clear.

This separation matters because a search hit is not evidence. A candidate source is not a retained source. A retained source is not automatically a citation. A citation is not external validation. The project writes these distinctions repeatedly because apparently one sentence was not enough for civilization.

## Output Counts
Source added count: 0

Citation added count: 0

Populated source count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This template prepares future literature search logging.

It does not add sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> LiteratureSearchLogTemplateResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    source_added_count = 0
    citation_added_count = 0
    populated_source_count = 0
    evidence_matrix_populated_count = 0
    manuscript_revised_count = 0

    audit_rule_count = count_present_terms(report, AUDIT_RULES)
    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 5:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if len(SEARCH_LOG_FIELDS) < 16:
        errors.append(f"Search log field count too low: {len(SEARCH_LOG_FIELDS)}")

    if len(SOURCE_REVIEW_FIELDS) < 14:
        errors.append(f"Source review field count too low: {len(SOURCE_REVIEW_FIELDS)}")

    if len(CLAIM_MAPPING_FIELDS) < 10:
        errors.append(f"Claim mapping field count too low: {len(CLAIM_MAPPING_FIELDS)}")

    if len(SOURCE_STATUS_VALUES) < 6:
        errors.append(f"Source status value count too low: {len(SOURCE_STATUS_VALUES)}")

    if len(SOURCE_ROLE_VALUES) < 6:
        errors.append(f"Source role value count too low: {len(SOURCE_ROLE_VALUES)}")

    if len(DECISION_VALUES) < 5:
        errors.append(f"Decision value count too low: {len(DECISION_VALUES)}")

    if audit_rule_count < 10:
        errors.append(f"Audit rule count too low: {audit_rule_count}")

    if boundary_count < 12:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 10:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    if source_added_count != 0:
        errors.append(f"Source added count should be zero, got: {source_added_count}")

    if citation_added_count != 0:
        errors.append(f"Citation added count should be zero, got: {citation_added_count}")

    if populated_source_count != 0:
        errors.append(f"Populated source count should be zero, got: {populated_source_count}")

    if evidence_matrix_populated_count != 0:
        errors.append(
            f"Evidence matrix populated count should be zero, got: {evidence_matrix_populated_count}"
        )

    if manuscript_revised_count != 0:
        errors.append(f"Manuscript revised count should be zero, got: {manuscript_revised_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if word_count < 1200:
        errors.append(f"Word count too low for literature search log template: {word_count}")

    warnings.append("Template adds no sources or citations; real search must happen later.")
    warnings.append("Template does not populate the evidence matrix or revise the manuscript.")

    passed = not errors

    interpretation = (
        "The v5.1 template defines a controlled log structure for future real "
        "literature searches without adding sources, citations, evidence rows, "
        "or manuscript revisions."
    )

    return LiteratureSearchLogTemplateResult(
        title="Literature Search Log Template v5.1",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        search_log_field_count=len(SEARCH_LOG_FIELDS),
        source_review_field_count=len(SOURCE_REVIEW_FIELDS),
        claim_mapping_field_count=len(CLAIM_MAPPING_FIELDS),
        source_status_value_count=len(SOURCE_STATUS_VALUES),
        source_role_value_count=len(SOURCE_ROLE_VALUES),
        decision_value_count=len(DECISION_VALUES),
        audit_rule_count=audit_rule_count,
        boundary_phrase_count=boundary_count,
        prohibited_behavior_count=prohibited_count,
        next_step_count=next_step_count,
        source_added_count=source_added_count,
        citation_added_count=citation_added_count,
        populated_source_count=populated_source_count,
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

    print("Literature Search Log Template v5.1")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Search log field count: {result.search_log_field_count}")
    print(f"Source review field count: {result.source_review_field_count}")
    print(f"Claim mapping field count: {result.claim_mapping_field_count}")
    print(f"Source status value count: {result.source_status_value_count}")
    print(f"Source role value count: {result.source_role_value_count}")
    print(f"Decision value count: {result.decision_value_count}")
    print(f"Audit rule count: {result.audit_rule_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Populated source count: {result.populated_source_count}")
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
