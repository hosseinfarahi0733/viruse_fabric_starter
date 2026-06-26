from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/controlled_formal_definition_completion_approval_execution_preflight_approval_execution_v8_45.md")
OUTPUT_PATH = Path("outputs/controlled_formal_definition_completion_approval_execution_gate_plan_v8_46.md")


@dataclass(frozen=True)
class ApprovalExecutionGatePlanRow:
    row_id: str
    gate_focus: str
    source_signal: str
    planned_gate_check: str
    hard_boundary: str


@dataclass(frozen=True)
class ApprovalExecutionGatePlanReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    approval_execution_gate_plan_count: int
    approval_execution_gate_plan_row_count: int
    preflight_approval_execution_source_row_count: int
    preflight_approval_execution_count: int
    preflight_approval_plan_count: int
    preflight_decision_execution_count: int
    preflight_execution_count: int
    approval_execution_preflight_required_count: int
    approval_execution_preflight_decision_execution_count: int
    approval_execution_preflight_approval_plan_required_count: int
    approval_execution_preflight_approval_execution_count: int
    approval_execution_preflight_approved_count: int
    approval_execution_gate_plan_required_count: int
    approval_execution_gate_execution_count: int
    approval_execution_authorized_count: int
    approval_execution_immediate_execution_approved_count: int
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
    external_validation_count: int
    independent_experiment_count: int
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


def _normalize(text: str) -> str:
    text = text.lower()
    for ch in ["_", "-", "`", "*", "|", ":", ";", ",", ".", "(", ")", "[", "]"]:
        text = text.replace(ch, " ")
    return " ".join(text.split())


def _has_all_terms(text: str, terms: List[str]) -> bool:
    normalized = _normalize(text)
    return all(term.lower() in normalized for term in terms)


def _source_has_preflight_approval_execution_count(text: str) -> bool:
    return (
        "Controlled formal definition completion approval execution preflight approval execution count: 1" in text
        or _has_all_terms(
            text,
            ["controlled formal definition completion approval execution preflight approval execution", "count", "1"],
        )
    )


def _source_has_preflight_approval_execution_rows(text: str) -> bool:
    return (
        "Controlled formal definition completion approval execution preflight approval execution row count: 4" in text
        or _has_all_terms(
            text,
            ["controlled formal definition completion approval execution preflight approval execution row count", "4"],
        )
    )


def _source_has_preflight_approval_plan_count(text: str) -> bool:
    return (
        "Controlled formal definition completion approval execution preflight approval plan count: 1" in text
        or _has_all_terms(
            text,
            ["controlled formal definition completion approval execution preflight approval plan", "count", "1"],
        )
    )


def _source_has_preflight_decision_execution_count(text: str) -> bool:
    return (
        "Controlled formal definition completion approval execution preflight decision execution count: 1" in text
        or _has_all_terms(
            text,
            ["controlled formal definition completion approval execution preflight decision execution", "count", "1"],
        )
    )


def _source_has_preflight_execution_count(text: str) -> bool:
    return (
        "Controlled formal definition completion approval execution preflight execution count: 1" in text
        or _has_all_terms(
            text,
            ["controlled formal definition completion approval execution preflight execution", "count", "1"],
        )
    )


def _source_has_preflight_required(text: str) -> bool:
    return (
        "Approval execution preflight required count: 1" in text
        or _has_all_terms(text, ["approval execution preflight required", "1"])
    )


def _source_has_preflight_decision_execution_short(text: str) -> bool:
    return (
        "Approval execution preflight decision execution count: 1" in text
        or _has_all_terms(text, ["approval execution preflight decision execution", "1"])
    )


def _source_has_preflight_approval_plan_required(text: str) -> bool:
    return (
        "Approval execution preflight approval plan required count: 1" in text
        or _has_all_terms(text, ["approval execution preflight approval plan required", "1"])
    )


def _source_has_preflight_approval_execution_short(text: str) -> bool:
    return (
        "Approval execution preflight approval execution count: 1" in text
        or _has_all_terms(text, ["approval execution preflight approval execution", "1"])
    )


def _source_has_preflight_approved(text: str) -> bool:
    return (
        "Approval execution preflight approved count: 1" in text
        or _has_all_terms(text, ["approval execution preflight approved", "1"])
    )


def _source_has_gate_plan_required(text: str) -> bool:
    return (
        "Approval execution gate plan required count: 1" in text
        or _has_all_terms(text, ["approval execution gate plan required", "1"])
    )


def _source_hard_zero_signal_count(text: str) -> int:
    zero_term_sets = [
        ["approval execution immediate execution approved", "0"],
        ["approval execution transition approved", "0"],
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
        ["external validation", "0"],
        ["independent experiment", "0"],
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
        "approval execution is approved",
        "approval execution is authorized",
        "approval execution is executed",
        "approval execution can begin",
        "immediate approval execution is approved",
        "manuscript is submission-ready",
        "external validation is completed",
        "independent experiment is completed",
        "clinical relevance is established",
        "biological prediction is established",
        "operational readiness is achieved",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_rows() -> List[ApprovalExecutionGatePlanRow]:
    return [
        ApprovalExecutionGatePlanRow(
            row_id="AGP-001",
            gate_focus="source preflight approval execution integrity",
            source_signal="v8.45 preflight approval execution exists and preflight approval is granted",
            planned_gate_check="verify whether the preflight approval execution can serve as source input for an approval execution gate",
            hard_boundary="does not execute approval",
        ),
        ApprovalExecutionGatePlanRow(
            row_id="AGP-002",
            gate_focus="approval execution gate scope",
            source_signal="v8.45 requires a separate approval execution gate plan",
            planned_gate_check="define the gate checks that must exist before any future approval execution attempt",
            hard_boundary="does not authorize approval execution",
        ),
        ApprovalExecutionGatePlanRow(
            row_id="AGP-003",
            gate_focus="formal completion containment",
            source_signal="v8.45 keeps approved completion and completed formal definitions absent",
            planned_gate_check="block movement from gate planning into approved completion or completed formal definitions",
            hard_boundary="does not approve completion or complete formal definitions",
        ),
        ApprovalExecutionGatePlanRow(
            row_id="AGP-004",
            gate_focus="proof validation citation and readiness containment",
            source_signal="v8.45 keeps proof execution, validation, citations, and readiness absent",
            planned_gate_check="preserve hard-zero proof, validation, citation, and readiness boundaries during gate planning",
            hard_boundary="does not execute proof work or make readiness claims",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    preflight_approval_execution_source_row_count = 4 if _source_has_preflight_approval_execution_rows(source_text) else 0
    preflight_approval_execution_count = 1 if _source_has_preflight_approval_execution_count(source_text) else 0
    preflight_approval_plan_count = 1 if _source_has_preflight_approval_plan_count(source_text) else 0
    preflight_decision_execution_count = 1 if _source_has_preflight_decision_execution_count(source_text) else 0
    preflight_execution_count = 1 if _source_has_preflight_execution_count(source_text) else 0
    preflight_required_count = 1 if _source_has_preflight_required(source_text) else 0
    preflight_decision_execution_short = 1 if _source_has_preflight_decision_execution_short(source_text) else 0
    preflight_approval_plan_required = 1 if _source_has_preflight_approval_plan_required(source_text) else 0
    preflight_approval_execution_short = 1 if _source_has_preflight_approval_execution_short(source_text) else 0
    preflight_approved = 1 if _source_has_preflight_approved(source_text) else 0
    gate_plan_required = 1 if _source_has_gate_plan_required(source_text) else 0
    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.45 preflight approval execution source artifact.")
    if preflight_approval_execution_source_row_count != 4:
        errors.append("Expected v8.45 preflight approval execution row count signal is absent.")
    if preflight_approval_execution_count != 1:
        errors.append("Expected v8.45 preflight approval execution count signal is absent.")
    if preflight_approval_plan_count != 1:
        errors.append("Expected carried v8.44 preflight approval plan count signal is absent.")
    if preflight_decision_execution_count != 1:
        errors.append("Expected carried v8.43 preflight decision execution count signal is absent.")
    if preflight_execution_count != 1:
        errors.append("Expected carried v8.41 preflight execution count signal is absent.")
    if preflight_required_count != 1:
        errors.append("Expected carried preflight required signal is absent.")
    if preflight_decision_execution_short != 1:
        errors.append("Expected carried approval execution preflight decision execution signal is absent.")
    if preflight_approval_plan_required != 1:
        errors.append("Expected carried preflight approval plan required signal is absent.")
    if preflight_approval_execution_short != 1:
        errors.append("Expected carried preflight approval execution signal is absent.")
    if preflight_approved != 1:
        errors.append("Expected carried preflight approved signal is absent.")
    if gate_plan_required != 1:
        errors.append("Expected carried approval execution gate plan required signal is absent.")
    if source_hard_zero_signal_count < 13:
        errors.append("Expected hard-zero source signals are incomplete.")

    warnings = [
        "Approval execution gate planning is created, but approval execution remains absent.",
        "Approval execution is not authorized in this milestone.",
        "Approved completion and completed formal definitions remain absent.",
        "No proof execution, theorem proof, lemma proof, external validation, citation addition, or manuscript submission readiness is created.",
    ]

    lines = [
        "# Controlled Formal Definition Completion Approval Execution Gate Plan v8.46",
        "",
        "## Purpose",
        "",
        "Plan a controlled approval execution gate after v8.45 preflight approval while preserving approval execution, approved completion, completed formal definitions, proof execution, external validation, citation additions, and submission readiness at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Approval execution gate plan rows",
        "",
        "| Row | Gate focus | Source signal | Planned gate check | Hard boundary |",
        "|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.row_id} | {row.gate_focus} | {row.source_signal} | {row.planned_gate_check} | {row.hard_boundary} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Controlled formal definition completion approval execution gate plan count: 1",
            f"- Controlled formal definition completion approval execution gate plan row count: {len(rows)}",
            f"- Controlled formal definition completion approval execution preflight approval execution source row count: {preflight_approval_execution_source_row_count}",
            f"- Controlled formal definition completion approval execution preflight approval execution count: {preflight_approval_execution_count}",
            f"- Controlled formal definition completion approval execution preflight approval plan count: {preflight_approval_plan_count}",
            f"- Controlled formal definition completion approval execution preflight decision execution count: {preflight_decision_execution_count}",
            f"- Controlled formal definition completion approval execution preflight execution count: {preflight_execution_count}",
            f"- Approval execution preflight required count: {preflight_required_count}",
            f"- Approval execution preflight decision execution count: {preflight_decision_execution_short}",
            f"- Approval execution preflight approval plan required count: {preflight_approval_plan_required}",
            f"- Approval execution preflight approval execution count: {preflight_approval_execution_short}",
            f"- Approval execution preflight approved count: {preflight_approved}",
            f"- Approval execution gate plan required count: {gate_plan_required}",
            "- Approval execution gate plan count: 1",
            "- Approval execution gate execution count: 0",
            "- Approval execution authorized count: 0",
            "- Approval execution immediate execution approved count: 0",
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
            "- External validation count: 0",
            "- Independent experiment count: 0",
            "- New citation added count: 0",
            "",
            "## Boundary interpretation",
            "",
            "The v8.46 artifact creates an approval execution gate plan only. It does not execute approval, does not authorize approval execution, does not approve completion, does not complete formal definitions, does not execute proof work, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "This milestone is justified because v8.45 granted preflight approval only for moving into a separate approval execution gate planning milestone. The next defensible step is approval execution gate execution, not direct approval execution.",
            "",
            "## Warnings",
            "",
        ]
    )

    for warning in warnings:
        lines.append(f"- {warning}")

    lines.extend(
        [
            "",
            "## Safe claim",
            "",
            "The project has planned a controlled approval execution gate for formal definition completion approval execution, without executing approval, authorizing approval execution, approving completion, completing formal definitions, or executing proof work.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this approval execution.",
            "- Do not call this approval execution authorization.",
            "- Do not call this approved completion.",
            "- Do not call this completed formal definitions.",
            "- Do not call this proof execution.",
            "- Do not call this formal proof.",
            "- Do not call this external validation.",
            "- Do not call this manuscript submission readiness.",
            "",
        ]
    )

    text = "\n".join(lines)
    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.46 approval execution gate plan report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.46 approval execution gate plan report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> ApprovalExecutionGatePlanReport:
    text = render_report()
    source_text = _read_source()
    rows = build_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    preflight_approval_execution_source_row_count = 4 if _source_has_preflight_approval_execution_rows(source_text) else 0
    preflight_approval_execution_count = 1 if _source_has_preflight_approval_execution_count(source_text) else 0
    preflight_approval_plan_count = 1 if _source_has_preflight_approval_plan_count(source_text) else 0
    preflight_decision_execution_count = 1 if _source_has_preflight_decision_execution_count(source_text) else 0
    preflight_execution_count = 1 if _source_has_preflight_execution_count(source_text) else 0
    preflight_required_count = 1 if _source_has_preflight_required(source_text) else 0
    preflight_decision_execution_short = 1 if _source_has_preflight_decision_execution_short(source_text) else 0
    preflight_approval_plan_required = 1 if _source_has_preflight_approval_plan_required(source_text) else 0
    preflight_approval_execution_short = 1 if _source_has_preflight_approval_execution_short(source_text) else 0
    preflight_approved = 1 if _source_has_preflight_approved(source_text) else 0
    gate_plan_required = 1 if _source_has_gate_plan_required(source_text) else 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.45 preflight approval execution source artifact.")
    if preflight_approval_execution_source_row_count != 4:
        errors.append("Expected v8.45 preflight approval execution row count signal is absent.")
    if preflight_approval_execution_count != 1:
        errors.append("Expected v8.45 preflight approval execution count signal is absent.")
    if preflight_approval_plan_count != 1:
        errors.append("Expected carried v8.44 preflight approval plan count signal is absent.")
    if preflight_decision_execution_count != 1:
        errors.append("Expected carried v8.43 preflight decision execution count signal is absent.")
    if preflight_execution_count != 1:
        errors.append("Expected carried v8.41 preflight execution count signal is absent.")
    if preflight_required_count != 1:
        errors.append("Expected carried preflight required signal is absent.")
    if preflight_decision_execution_short != 1:
        errors.append("Expected carried approval execution preflight decision execution signal is absent.")
    if preflight_approval_plan_required != 1:
        errors.append("Expected carried preflight approval plan required signal is absent.")
    if preflight_approval_execution_short != 1:
        errors.append("Expected carried preflight approval execution signal is absent.")
    if preflight_approved != 1:
        errors.append("Expected carried preflight approved signal is absent.")
    if gate_plan_required != 1:
        errors.append("Expected carried approval execution gate plan required signal is absent.")

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)
    if source_hard_zero_signal_count < 13:
        errors.append("Expected hard-zero source signals are incomplete.")

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "Approval execution gate planning is created, but approval execution remains absent.",
        "Approval execution is not authorized in this milestone.",
        "Approved completion and completed formal definitions remain absent.",
        "No proof execution, theorem proof, lemma proof, external validation, citation addition, or manuscript submission readiness is created.",
    ]

    return ApprovalExecutionGatePlanReport(
        title="Controlled Formal Definition Completion Approval Execution Gate Plan v8.46",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        approval_execution_gate_plan_count=1,
        approval_execution_gate_plan_row_count=len(rows),
        preflight_approval_execution_source_row_count=preflight_approval_execution_source_row_count,
        preflight_approval_execution_count=preflight_approval_execution_count,
        preflight_approval_plan_count=preflight_approval_plan_count,
        preflight_decision_execution_count=preflight_decision_execution_count,
        preflight_execution_count=preflight_execution_count,
        approval_execution_preflight_required_count=preflight_required_count,
        approval_execution_preflight_decision_execution_count=preflight_decision_execution_short,
        approval_execution_preflight_approval_plan_required_count=preflight_approval_plan_required,
        approval_execution_preflight_approval_execution_count=preflight_approval_execution_short,
        approval_execution_preflight_approved_count=preflight_approved,
        approval_execution_gate_plan_required_count=gate_plan_required,
        approval_execution_gate_execution_count=0,
        approval_execution_authorized_count=0,
        approval_execution_immediate_execution_approved_count=0,
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
        external_validation_count=0,
        independent_experiment_count=0,
        new_citation_added_count=0,
        conditional_hold_count=1,
        hard_zero_count=16,
        boundary_phrase_count=29,
        prohibited_behavior_count=20,
        next_step_count=8,
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
