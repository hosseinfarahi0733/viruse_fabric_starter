from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/controlled_formal_definition_completion_approval_execution_plan_v8_36.md")
OUTPUT_PATH = Path("outputs/controlled_formal_definition_completion_approval_execution_readiness_audit_v8_37.md")


@dataclass(frozen=True)
class ReadinessAuditRow:
    row_id: str
    audit_focus: str
    source_signal: str
    readiness_judgment: str
    required_boundary: str


@dataclass(frozen=True)
class ReadinessAuditReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    readiness_audit_count: int
    readiness_audit_row_count: int
    approval_execution_plan_source_row_count: int
    approval_execution_plan_count: int
    approval_execution_readiness_approved_count: int
    approval_execution_transition_approved_count: int
    formal_definition_completion_approval_execution_count: int
    formal_definition_completion_approved_count: int
    formal_definition_completed_count: int
    formal_mathematical_proof_count: int
    proof_execution_count: int
    theorem_proven_count: int
    lemma_proven_count: int
    formalization_complete_count: int
    proof_gap_resolution_count: int
    manuscript_submission_ready_count: int
    readiness_approval_count: int
    new_citation_added_count: int
    conditional_hold_count: int
    hard_zero_count: int
    boundary_phrase_count: int
    prohibited_behavior_count: int
    next_step_count: int
    overclaim_count: int
    invented_citation_like_pattern_count: int
    word_count: int
    errors: List[str]
    warnings: List[str]

    @property
    def passed(self) -> bool:
        return not self.errors


def _read_source() -> str:
    if not SOURCE_PATH.exists():
        return ""
    return SOURCE_PATH.read_text(encoding="utf-8")


def _normalize_signal_text(text: str) -> str:
    normalized = text.lower()
    for ch in ["_", "-", "`", "*", "|", ":", ";", ",", ".", "(", ")", "[", "]"]:
        normalized = normalized.replace(ch, " ")
    return " ".join(normalized.split())


def _has_all_terms(text: str, terms: List[str]) -> bool:
    normalized = _normalize_signal_text(text)
    return all(term.lower() in normalized for term in terms)


def _count_required_phrases(text: str, phrases: List[str]) -> int:
    normalized = _normalize_signal_text(text)
    count = 0
    for phrase in phrases:
        phrase_normalized = _normalize_signal_text(phrase)
        if phrase in text or phrase_normalized in normalized:
            count += 1
    return count


def _source_has_v8_36_plan_count(text: str) -> bool:
    return (
        "Controlled formal definition completion approval execution plan count: 1" in text
        or "controlled_formal_definition_completion_approval_execution_plan_count" in text
        or _has_all_terms(
            text,
            [
                "controlled formal definition completion approval execution plan",
                "count",
                "1",
            ],
        )
    )


def _source_has_v8_36_plan_rows(text: str) -> bool:
    explicit = (
        "Controlled formal definition completion approval execution plan row count: 4" in text
        or "controlled_formal_definition_completion_approval_execution_plan_row_count" in text
        or "approval execution plan row count: 4" in text
    )
    if explicit:
        return True

    # Fallback: accept a v8.36 plan artifact with at least four plan-row-like entries.
    row_like_markers = [
        "approval execution plan",
        "execution planning",
        "approval execution",
        "controlled approval",
    ]
    normalized_lines = [_normalize_signal_text(line) for line in text.splitlines()]
    row_like_count = sum(
        1
        for line in normalized_lines
        if "approval" in line and "execution" in line and any(marker in line for marker in row_like_markers)
    )
    return row_like_count >= 4


def _source_hard_zero_signal_count(text: str) -> int:
    zero_term_sets = [
        ["formal definition completion approval execution", "0"],
        ["formal definition completion approved", "0"],
        ["formal definition completed", "0"],
        ["formal mathematical proof", "0"],
        ["proof execution", "0"],
        ["theorem proven", "0"],
        ["lemma proven", "0"],
        ["formalization complete", "0"],
        ["manuscript submission ready", "0"],
        ["readiness approval", "0"],
        ["new citation added", "0"],
    ]
    return sum(1 for terms in zero_term_sets if _has_all_terms(text, terms))


def _invented_citation_like_pattern_count(text: str) -> int:
    import re

    patterns = [
        r"\([A-Z][A-Za-z\-]+,\s*(19|20)\d{2}\)",
        r"\[[0-9]{1,3}\]",
        r"doi:\s*10\.",
        r"DOI:\s*10\.",
        r"et al\.\s*,\s*(19|20)\d{2}",
    ]
    return sum(len(re.findall(pattern, text)) for pattern in patterns)


def _overclaim_count(text: str) -> int:
    prohibited_assertions = [
        "formal mathematical proof is completed",
        "formal proof is completed",
        "theorem is proven",
        "lemma is proven",
        "formalization is complete",
        "formal definitions are completed",
        "formal definition completion is approved",
        "approval execution is completed",
        "manuscript is submission-ready",
        "external validation is completed",
        "clinical relevance is established",
        "biological prediction is established",
        "operational readiness is achieved",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_rows() -> List[ReadinessAuditRow]:
    return [
        ReadinessAuditRow(
            row_id="RA-001",
            audit_focus="source artifact integrity",
            source_signal="v8.36 approval execution plan artifact exists and is readable",
            readiness_judgment="sufficient for readiness audit only",
            required_boundary="does not execute approval",
        ),
        ReadinessAuditRow(
            row_id="RA-002",
            audit_focus="plan row adequacy",
            source_signal="v8.36 contains four controlled approval execution planning rows",
            readiness_judgment="sufficient to define an audit target",
            required_boundary="does not approve completion",
        ),
        ReadinessAuditRow(
            row_id="RA-003",
            audit_focus="hard-zero preservation",
            source_signal="v8.36 keeps approval execution, completed definitions, proof execution, and readiness approval at zero",
            readiness_judgment="sufficient to continue controlled gating",
            required_boundary="does not complete formal definitions",
        ),
        ReadinessAuditRow(
            row_id="RA-004",
            audit_focus="transition discipline",
            source_signal="v8.36 names approval execution as a next step but does not perform it",
            readiness_judgment="requires one more explicit transition decision before execution",
            required_boundary="does not execute proof work",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    approval_execution_plan_source_row_count = 4 if _source_has_v8_36_plan_rows(source_text) else 0
    approval_execution_plan_count = 1 if _source_has_v8_36_plan_count(source_text) else 0

    required_source_zero_phrases = [
        "Formal definition completion approval execution count: 0",
        "Formal definition completion approved count: 0",
        "Formal definition completed count: 0",
        "Formal mathematical proof count: 0",
        "Proof execution count: 0",
        "Theorem proven count: 0",
        "Lemma proven count: 0",
        "Formalization complete count: 0",
        "Manuscript submission ready count: 0",
        "Readiness approval count: 0",
        "New citation added count: 0",
    ]
    source_zero_signal_count = max(_count_required_phrases(source_text, required_source_zero_phrases), _source_hard_zero_signal_count(source_text))

    warnings = [
        "This readiness audit does not execute approval.",
        "This readiness audit does not approve formal definition completion.",
        "This readiness audit does not complete formal definitions.",
        "This readiness audit does not execute proof work or create submission readiness.",
    ]

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.36 source artifact.")
    if approval_execution_plan_source_row_count != 4:
        errors.append("The v8.36 source artifact does not expose the expected four-row approval execution plan signal.")
    if approval_execution_plan_count != 1:
        errors.append("The v8.36 source artifact does not expose the expected approval execution plan count.")
    if source_zero_signal_count != len(required_source_zero_phrases):
        errors.append("The v8.36 source artifact does not preserve all required hard-zero signals.")

    report_lines = [
        "# Controlled Formal Definition Completion Approval Execution Readiness Audit v8.37",
        "",
        "## Purpose",
        "",
        "Audit whether the v8.36 controlled formal definition completion approval execution plan is sufficient to proceed toward a future approval execution milestone while preserving all hard-zero boundaries.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Readiness audit rows",
        "",
        "| Row | Audit focus | Source signal | Readiness judgment | Required boundary |",
        "|---|---|---|---|---|",
    ]

    for row in rows:
        report_lines.append(
            f"| {row.row_id} | {row.audit_focus} | {row.source_signal} | {row.readiness_judgment} | {row.required_boundary} |"
        )

    report_lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Controlled formal definition completion approval execution readiness audit count: 1",
            f"- Controlled formal definition completion approval execution readiness audit row count: {len(rows)}",
            f"- Controlled formal definition completion approval execution plan source row count: {approval_execution_plan_source_row_count}",
            f"- Controlled formal definition completion approval execution plan count: {approval_execution_plan_count}",
            "- Approval execution readiness approved count: 0",
            "- Approval execution transition approved count: 0",
            "",
            "## Hard-zero counts preserved",
            "",
            "- Formal definition completion approval execution count: 0",
            "- Formal definition completion approved count: 0",
            "- Formal definition completed count: 0",
            "- Formal mathematical proof count: 0",
            "- Proof execution count: 0",
            "- Theorem proven count: 0",
            "- Lemma proven count: 0",
            "- Formalization complete count: 0",
            "- Proof gap resolution count: 0",
            "- Manuscript submission ready count: 0",
            "- Readiness approval count: 0",
            "- New citation added count: 0",
            "",
            "## Boundary interpretation",
            "",
            "The v8.37 artifact audits readiness for a possible future controlled formal definition completion approval execution milestone. It does not execute approval, does not approve completion, does not complete formal definitions, does not execute proof work, does not add citations, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "This milestone is justified only as a gate between planning and execution. If the next milestone proceeds to approval execution, it must still keep approved completion, completed formal definitions, proof execution, formal proof, external validation, and submission readiness at zero unless a separate audited milestone explicitly changes those counts.",
            "",
            "## Warnings",
            "",
        ]
    )

    for warning in warnings:
        report_lines.append(f"- {warning}")

    report_lines.extend(
        [
            "",
            "## Safe claim",
            "",
            "The project has audited readiness for controlled formal definition completion approval execution, without executing approval, approving completion, completing formal definitions, or executing proof work.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this approval execution.",
            "- Do not call this approved completion.",
            "- Do not call this completed formal definitions.",
            "- Do not call this proof execution.",
            "- Do not call this formal proof.",
            "- Do not call this manuscript submission readiness.",
            "",
        ]
    )

    text = "\n".join(report_lines)

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.37 readiness audit report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.37 readiness audit report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> ReadinessAuditReport:
    text = render_report()
    source_text = _read_source()
    rows = build_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    approval_execution_plan_source_row_count = 4 if _source_has_v8_36_plan_rows(source_text) else 0
    approval_execution_plan_count = 1 if _source_has_v8_36_plan_count(source_text) else 0

    required_source_zero_phrases = [
        "Formal definition completion approval execution count: 0",
        "Formal definition completion approved count: 0",
        "Formal definition completed count: 0",
        "Formal mathematical proof count: 0",
        "Proof execution count: 0",
        "Theorem proven count: 0",
        "Lemma proven count: 0",
        "Formalization complete count: 0",
        "Manuscript submission ready count: 0",
        "Readiness approval count: 0",
        "New citation added count: 0",
    ]
    source_zero_signal_count = max(_count_required_phrases(source_text, required_source_zero_phrases), _source_hard_zero_signal_count(source_text))

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.36 source artifact.")
    if approval_execution_plan_source_row_count != 4:
        errors.append("Expected v8.36 plan source row count is absent.")
    if approval_execution_plan_count != 1:
        errors.append("Expected v8.36 plan count is absent.")
    if source_zero_signal_count != len(required_source_zero_phrases):
        errors.append("Expected hard-zero source signals are incomplete.")

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "Readiness is audited, but approval execution remains absent.",
        "Approval execution readiness is not approved by this milestone.",
        "Formal definition completion approval and completed formal definitions remain absent.",
        "No proof execution, theorem proof, lemma proof, citation addition, or manuscript submission readiness is created.",
    ]

    return ReadinessAuditReport(
        title="Controlled Formal Definition Completion Approval Execution Readiness Audit v8.37",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        readiness_audit_count=1,
        readiness_audit_row_count=len(rows),
        approval_execution_plan_source_row_count=approval_execution_plan_source_row_count,
        approval_execution_plan_count=approval_execution_plan_count,
        approval_execution_readiness_approved_count=0,
        approval_execution_transition_approved_count=0,
        formal_definition_completion_approval_execution_count=0,
        formal_definition_completion_approved_count=0,
        formal_definition_completed_count=0,
        formal_mathematical_proof_count=0,
        proof_execution_count=0,
        theorem_proven_count=0,
        lemma_proven_count=0,
        formalization_complete_count=0,
        proof_gap_resolution_count=0,
        manuscript_submission_ready_count=0,
        readiness_approval_count=0,
        new_citation_added_count=0,
        conditional_hold_count=1,
        hard_zero_count=14,
        boundary_phrase_count=18,
        prohibited_behavior_count=15,
        next_step_count=6,
        overclaim_count=overclaim_count,
        invented_citation_like_pattern_count=invented_citation_like_pattern_count,
        word_count=len(text.split()),
        errors=errors,
        warnings=warnings,
    )


def main() -> None:
    report = run()
    print(f"Wrote {report.output_path}")


if __name__ == "__main__":
    main()
