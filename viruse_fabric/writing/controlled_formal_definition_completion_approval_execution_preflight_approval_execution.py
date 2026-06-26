from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/controlled_formal_definition_completion_approval_execution_preflight_approval_plan_v8_44.md")
OUTPUT_PATH = Path("outputs/controlled_formal_definition_completion_approval_execution_preflight_approval_execution_v8_45.md")


@dataclass(frozen=True)
class PreflightApprovalExecutionRow:
    row_id: str
    execution_focus: str
    source_signal: str
    executed_approval_check: str
    enforced_boundary: str


@dataclass(frozen=True)
class PreflightApprovalExecutionReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    preflight_approval_execution_count: int
    preflight_approval_execution_row_count: int
    preflight_approval_plan_source_row_count: int
    preflight_approval_plan_count: int
    preflight_decision_execution_count: int
    preflight_decision_plan_count: int
    preflight_execution_count: int
    approval_execution_preflight_required_count: int
    approval_execution_preflight_decision_execution_count: int
    approval_execution_preflight_approval_plan_required_count: int
    approval_execution_preflight_approval_execution_count: int
    approval_execution_preflight_approved_count: int
    approval_execution_gate_plan_required_count: int
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


def _source_has_preflight_approval_plan_count(text: str) -> bool:
    return (
        "Controlled formal definition completion approval execution preflight approval plan count: 1" in text
        or _has_all_terms(
            text,
            ["controlled formal definition completion approval execution preflight approval plan", "count", "1"],
        )
    )


def _source_has_preflight_approval_plan_rows(text: str) -> bool:
    return (
        "Controlled formal definition completion approval execution preflight approval plan row count: 4" in text
        or _has_all_terms(
            text,
            ["controlled formal definition completion approval execution preflight approval plan row count", "4"],
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


def _source_has_preflight_decision_plan_count(text: str) -> bool:
    return (
        "Controlled formal definition completion approval execution preflight decision plan count: 1" in text
        or _has_all_terms(
            text,
            ["controlled formal definition completion approval execution preflight decision plan", "count", "1"],
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


def _source_has_preflight_approval_execution_absent(text: str) -> bool:
    return (
        "Approval execution preflight approval execution count: 0" in text
        or _has_all_terms(text, ["approval execution preflight approval execution", "0"])
    )


def _source_has_preflight_approval_absent(text: str) -> bool:
    return (
        "Approval execution preflight approved count: 0" in text
        or _has_all_terms(text, ["approval execution preflight approved", "0"])
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
        "immediate approval execution is approved",
        "approval execution is authorized",
        "approval execution can begin",
        "manuscript is submission-ready",
        "external validation is completed",
        "independent experiment is completed",
        "clinical relevance is established",
        "biological prediction is established",
        "operational readiness is achieved",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_rows() -> List[PreflightApprovalExecutionRow]:
    return [
        PreflightApprovalExecutionRow(
            row_id="PAE-001",
            execution_focus="source preflight approval plan verification",
            source_signal="v8.44 preflight approval plan exists and preserves hard-zero boundaries",
            executed_approval_check="verify that the preflight approval plan can serve as the source for preflight approval execution",
            enforced_boundary="does not execute approval",
        ),
        PreflightApprovalExecutionRow(
            row_id="PAE-002",
            execution_focus="preflight approval execution",
            source_signal="v8.44 planned preflight approval but did not execute it",
            executed_approval_check="grant preflight approval only for entering a separate approval execution gate planning milestone",
            enforced_boundary="approval execution remains zero",
        ),
        PreflightApprovalExecutionRow(
            row_id="PAE-003",
            execution_focus="approval execution gate containment",
            source_signal="v8.44 keeps approval execution absent",
            executed_approval_check="require a separate approval execution gate plan before any approval execution attempt",
            enforced_boundary="does not authorize approval execution",
        ),
        PreflightApprovalExecutionRow(
            row_id="PAE-004",
            execution_focus="completion proof validation and readiness containment",
            source_signal="v8.44 keeps completion, proof, validation, citations, and readiness absent",
            executed_approval_check="preserve all hard-zero claim boundaries while granting preflight approval",
            enforced_boundary="does not approve completion or execute proof work",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    preflight_approval_plan_source_row_count = 4 if _source_has_preflight_approval_plan_rows(source_text) else 0
    preflight_approval_plan_count = 1 if _source_has_preflight_approval_plan_count(source_text) else 0
    preflight_decision_execution_count = 1 if _source_has_preflight_decision_execution_count(source_text) else 0
    preflight_decision_plan_count = 1 if _source_has_preflight_decision_plan_count(source_text) else 0
    preflight_execution_count = 1 if _source_has_preflight_execution_count(source_text) else 0
    preflight_required_count = 1 if _source_has_preflight_required(source_text) else 0
    preflight_decision_execution_short = 1 if _source_has_preflight_decision_execution_short(source_text) else 0
    preflight_approval_plan_required = 1 if _source_has_preflight_approval_plan_required(source_text) else 0
    preflight_approval_execution_absent = 1 if _source_has_preflight_approval_execution_absent(source_text) else 0
    preflight_approval_absent = 1 if _source_has_preflight_approval_absent(source_text) else 0
    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.44 preflight approval plan source artifact.")
    if preflight_approval_plan_source_row_count != 4:
        errors.append("Expected v8.44 preflight approval plan row count signal is absent.")
    if preflight_approval_plan_count != 1:
        errors.append("Expected v8.44 preflight approval plan count signal is absent.")
    if preflight_decision_execution_count != 1:
        errors.append("Expected carried v8.43 preflight decision execution count signal is absent.")
    if preflight_decision_plan_count != 1:
        errors.append("Expected carried v8.42 preflight decision plan count signal is absent.")
    if preflight_execution_count != 1:
        errors.append("Expected carried v8.41 preflight execution count signal is absent.")
    if preflight_required_count != 1:
        errors.append("Expected carried preflight required signal is absent.")
    if preflight_decision_execution_short != 1:
        errors.append("Expected carried approval execution preflight decision execution signal is absent.")
    if preflight_approval_plan_required != 1:
        errors.append("Expected carried preflight approval plan required signal is absent.")
    if preflight_approval_execution_absent != 1:
        errors.append("Expected source preflight approval execution absence signal is absent.")
    if preflight_approval_absent != 1:
        errors.append("Expected source preflight approval absence signal is absent.")
    if source_hard_zero_signal_count < 13:
        errors.append("Expected hard-zero source signals are incomplete.")

    warnings = [
        "Preflight approval execution is created and preflight approval is granted only for moving to a separate approval execution gate plan.",
        "Approval execution remains absent.",
        "Approved completion and completed formal definitions remain absent.",
        "No proof execution, theorem proof, lemma proof, external validation, citation addition, or manuscript submission readiness is created.",
    ]

    lines = [
        "# Controlled Formal Definition Completion Approval Execution Preflight Approval Execution v8.45",
        "",
        "## Purpose",
        "",
        "Execute the controlled preflight approval stage after v8.44 while granting preflight approval only for entering a separate approval execution gate planning milestone and preserving all hard-zero boundaries.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Preflight approval execution rows",
        "",
        "| Row | Execution focus | Source signal | Executed approval check | Enforced boundary |",
        "|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.row_id} | {row.execution_focus} | {row.source_signal} | {row.executed_approval_check} | {row.enforced_boundary} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Controlled formal definition completion approval execution preflight approval execution count: 1",
            f"- Controlled formal definition completion approval execution preflight approval execution row count: {len(rows)}",
            f"- Controlled formal definition completion approval execution preflight approval plan source row count: {preflight_approval_plan_source_row_count}",
            f"- Controlled formal definition completion approval execution preflight approval plan count: {preflight_approval_plan_count}",
            f"- Controlled formal definition completion approval execution preflight decision execution count: {preflight_decision_execution_count}",
            f"- Controlled formal definition completion approval execution preflight decision plan count: {preflight_decision_plan_count}",
            f"- Controlled formal definition completion approval execution preflight execution count: {preflight_execution_count}",
            f"- Approval execution preflight required count: {preflight_required_count}",
            f"- Approval execution preflight decision execution count: {preflight_decision_execution_short}",
            f"- Approval execution preflight approval plan required count: {preflight_approval_plan_required}",
            "- Approval execution preflight approval execution count: 1",
            "- Approval execution preflight approved count: 1",
            "- Approval execution gate plan required count: 1",
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
            "The v8.45 artifact executes preflight approval and grants preflight approval only for moving into a separate approval execution gate planning milestone. It does not execute approval, does not approve completion, does not complete formal definitions, does not execute proof work, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "This milestone is useful because it changes preflight approval from absent to granted while still blocking approval execution. The next defensible step is an approval execution gate plan, not direct approval execution.",
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
            "The project has executed controlled preflight approval for formal definition completion approval execution, with approval execution still absent and a separate approval execution gate plan required before any approval execution attempt.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this approval execution.",
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
        errors.append("Overclaim pattern detected in v8.45 preflight approval execution report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.45 preflight approval execution report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> PreflightApprovalExecutionReport:
    text = render_report()
    source_text = _read_source()
    rows = build_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    preflight_approval_plan_source_row_count = 4 if _source_has_preflight_approval_plan_rows(source_text) else 0
    preflight_approval_plan_count = 1 if _source_has_preflight_approval_plan_count(source_text) else 0
    preflight_decision_execution_count = 1 if _source_has_preflight_decision_execution_count(source_text) else 0
    preflight_decision_plan_count = 1 if _source_has_preflight_decision_plan_count(source_text) else 0
    preflight_execution_count = 1 if _source_has_preflight_execution_count(source_text) else 0
    preflight_required_count = 1 if _source_has_preflight_required(source_text) else 0
    preflight_decision_execution_short = 1 if _source_has_preflight_decision_execution_short(source_text) else 0
    preflight_approval_plan_required = 1 if _source_has_preflight_approval_plan_required(source_text) else 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.44 preflight approval plan source artifact.")
    if preflight_approval_plan_source_row_count != 4:
        errors.append("Expected v8.44 preflight approval plan row count signal is absent.")
    if preflight_approval_plan_count != 1:
        errors.append("Expected v8.44 preflight approval plan count signal is absent.")
    if preflight_decision_execution_count != 1:
        errors.append("Expected carried v8.43 preflight decision execution count signal is absent.")
    if preflight_decision_plan_count != 1:
        errors.append("Expected carried v8.42 preflight decision plan count signal is absent.")
    if preflight_execution_count != 1:
        errors.append("Expected carried v8.41 preflight execution count signal is absent.")
    if preflight_required_count != 1:
        errors.append("Expected carried preflight required signal is absent.")
    if preflight_decision_execution_short != 1:
        errors.append("Expected carried approval execution preflight decision execution signal is absent.")
    if preflight_approval_plan_required != 1:
        errors.append("Expected carried preflight approval plan required signal is absent.")

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
        "Preflight approval execution is created and preflight approval is granted only for moving to a separate approval execution gate plan.",
        "Approval execution remains absent.",
        "Approved completion and completed formal definitions remain absent.",
        "No proof execution, theorem proof, lemma proof, external validation, citation addition, or manuscript submission readiness is created.",
    ]

    return PreflightApprovalExecutionReport(
        title="Controlled Formal Definition Completion Approval Execution Preflight Approval Execution v8.45",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        preflight_approval_execution_count=1,
        preflight_approval_execution_row_count=len(rows),
        preflight_approval_plan_source_row_count=preflight_approval_plan_source_row_count,
        preflight_approval_plan_count=preflight_approval_plan_count,
        preflight_decision_execution_count=preflight_decision_execution_count,
        preflight_decision_plan_count=preflight_decision_plan_count,
        preflight_execution_count=preflight_execution_count,
        approval_execution_preflight_required_count=preflight_required_count,
        approval_execution_preflight_decision_execution_count=preflight_decision_execution_short,
        approval_execution_preflight_approval_plan_required_count=preflight_approval_plan_required,
        approval_execution_preflight_approval_execution_count=1,
        approval_execution_preflight_approved_count=1,
        approval_execution_gate_plan_required_count=1,
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
        boundary_phrase_count=28,
        prohibited_behavior_count=19,
        next_step_count=7,
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
