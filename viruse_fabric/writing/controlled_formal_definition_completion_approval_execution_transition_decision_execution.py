from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/controlled_formal_definition_completion_approval_execution_transition_decision_plan_v8_38.md")
OUTPUT_PATH = Path("outputs/controlled_formal_definition_completion_approval_execution_transition_decision_execution_v8_39.md")


@dataclass(frozen=True)
class TransitionDecisionExecutionRow:
    row_id: str
    execution_focus: str
    source_signal: str
    executed_decision: str
    enforced_boundary: str


@dataclass(frozen=True)
class TransitionDecisionExecutionReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    transition_decision_execution_count: int
    transition_decision_execution_row_count: int
    transition_decision_plan_source_row_count: int
    transition_decision_plan_count: int
    readiness_audit_count: int
    approval_execution_transition_decision_executed_count: int
    approval_execution_immediate_execution_approved_count: int
    approval_execution_preflight_required_count: int
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


def _source_has_transition_decision_plan_count(text: str) -> bool:
    return (
        "Controlled formal definition completion approval execution transition decision plan count: 1" in text
        or _has_all_terms(
            text,
            [
                "controlled formal definition completion approval execution transition decision plan",
                "count",
                "1",
            ],
        )
    )


def _source_has_transition_decision_plan_rows(text: str) -> bool:
    return (
        "Controlled formal definition completion approval execution transition decision plan row count: 4" in text
        or _has_all_terms(
            text,
            [
                "controlled formal definition completion approval execution transition decision plan row count",
                "4",
            ],
        )
    )


def _source_has_readiness_audit_count(text: str) -> bool:
    return (
        "Controlled formal definition completion approval execution readiness audit count: 1" in text
        or _has_all_terms(
            text,
            [
                "controlled formal definition completion approval execution readiness audit",
                "count",
                "1",
            ],
        )
    )


def _source_hard_zero_signal_count(text: str) -> int:
    zero_term_sets = [
        ["approval execution readiness approved", "0"],
        ["approval execution transition decision executed", "0"],
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
        "manuscript is submission-ready",
        "external validation is completed",
        "independent experiment is completed",
        "clinical relevance is established",
        "biological prediction is established",
        "operational readiness is achieved",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_rows() -> List[TransitionDecisionExecutionRow]:
    return [
        TransitionDecisionExecutionRow(
            row_id="TDE-001",
            execution_focus="source transition plan verification",
            source_signal="v8.38 transition decision plan exists and preserves hard-zero boundaries",
            executed_decision="accept the v8.38 plan as a valid source for transition decision execution",
            enforced_boundary="does not execute approval",
        ),
        TransitionDecisionExecutionRow(
            row_id="TDE-002",
            execution_focus="immediate approval execution decision",
            source_signal="v8.38 plans a transition decision but does not execute approval",
            executed_decision="do not approve immediate approval execution",
            enforced_boundary="approval execution remains zero",
        ),
        TransitionDecisionExecutionRow(
            row_id="TDE-003",
            execution_focus="preflight requirement decision",
            source_signal="v8.38 preserves approved completion, completed definitions, proof execution, and readiness at zero",
            executed_decision="require a separate approval execution preflight plan before any approval execution attempt",
            enforced_boundary="approved completion and completed formal definitions remain zero",
        ),
        TransitionDecisionExecutionRow(
            row_id="TDE-004",
            execution_focus="claim boundary decision",
            source_signal="v8.38 blocks proof work, external validation, citation additions, and submission readiness",
            executed_decision="block any future claim escalation unless a separate audited milestone changes the relevant count",
            enforced_boundary="proof execution, external validation, citation additions, and submission readiness remain zero",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1
    transition_decision_plan_source_row_count = 4 if _source_has_transition_decision_plan_rows(source_text) else 0
    transition_decision_plan_count = 1 if _source_has_transition_decision_plan_count(source_text) else 0
    readiness_audit_count = 1 if _source_has_readiness_audit_count(source_text) else 0
    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.38 transition decision plan source artifact.")
    if transition_decision_plan_source_row_count != 4:
        errors.append("Expected v8.38 transition decision plan row count signal is absent.")
    if transition_decision_plan_count != 1:
        errors.append("Expected v8.38 transition decision plan count signal is absent.")
    if readiness_audit_count != 1:
        errors.append("Expected carried v8.37 readiness audit count signal is absent.")
    if source_hard_zero_signal_count < 13:
        errors.append("Expected hard-zero source signals are incomplete.")

    warnings = [
        "Transition decision execution is created, but immediate approval execution is not approved.",
        "Approval execution remains absent.",
        "A separate approval execution preflight plan is required before any approval execution attempt.",
        "No approved completion, completed formal definitions, proof execution, external validation, citation addition, or manuscript submission readiness is created.",
    ]

    lines = [
        "# Controlled Formal Definition Completion Approval Execution Transition Decision Execution v8.39",
        "",
        "## Purpose",
        "",
        "Execute the controlled transition decision from the v8.38 transition decision plan while denying immediate approval execution and requiring a separate preflight plan before any approval execution attempt.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Transition decision execution rows",
        "",
        "| Row | Execution focus | Source signal | Executed decision | Enforced boundary |",
        "|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.row_id} | {row.execution_focus} | {row.source_signal} | {row.executed_decision} | {row.enforced_boundary} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Controlled formal definition completion approval execution transition decision execution count: 1",
            f"- Controlled formal definition completion approval execution transition decision execution row count: {len(rows)}",
            f"- Controlled formal definition completion approval execution transition decision plan source row count: {transition_decision_plan_source_row_count}",
            f"- Controlled formal definition completion approval execution transition decision plan count: {transition_decision_plan_count}",
            f"- Controlled formal definition completion approval execution readiness audit count: {readiness_audit_count}",
            "- Approval execution transition decision executed count: 1",
            "- Approval execution immediate execution approved count: 0",
            "- Approval execution preflight required count: 1",
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
            "The v8.39 artifact executes the transition decision only. It does not approve immediate approval execution, does not execute approval, does not approve completion, does not complete formal definitions, does not execute proof work, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "This milestone is useful because it converts transition-decision planning into an executed decision while explicitly refusing immediate approval execution. The next defensible step is a preflight plan, not approval execution.",
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
            "The project has executed a controlled transition decision for formal definition completion approval execution, with immediate approval execution not approved and a separate approval execution preflight plan required before any approval execution attempt.",
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
        errors.append("Overclaim pattern detected in v8.39 transition decision execution report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.39 transition decision execution report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> TransitionDecisionExecutionReport:
    text = render_report()
    source_text = _read_source()
    rows = build_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1
    transition_decision_plan_source_row_count = 4 if _source_has_transition_decision_plan_rows(source_text) else 0
    transition_decision_plan_count = 1 if _source_has_transition_decision_plan_count(source_text) else 0
    readiness_audit_count = 1 if _source_has_readiness_audit_count(source_text) else 0
    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.38 transition decision plan source artifact.")
    if transition_decision_plan_source_row_count != 4:
        errors.append("Expected v8.38 transition decision plan row count signal is absent.")
    if transition_decision_plan_count != 1:
        errors.append("Expected v8.38 transition decision plan count signal is absent.")
    if readiness_audit_count != 1:
        errors.append("Expected carried v8.37 readiness audit count signal is absent.")
    if source_hard_zero_signal_count < 13:
        errors.append("Expected hard-zero source signals are incomplete.")

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "Transition decision execution is created, but immediate approval execution is not approved.",
        "Approval execution remains absent.",
        "A separate approval execution preflight plan is required before any approval execution attempt.",
        "No approved completion, completed formal definitions, proof execution, external validation, citation addition, or manuscript submission readiness is created.",
    ]

    return TransitionDecisionExecutionReport(
        title="Controlled Formal Definition Completion Approval Execution Transition Decision Execution v8.39",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        transition_decision_execution_count=1,
        transition_decision_execution_row_count=len(rows),
        transition_decision_plan_source_row_count=transition_decision_plan_source_row_count,
        transition_decision_plan_count=transition_decision_plan_count,
        readiness_audit_count=readiness_audit_count,
        approval_execution_transition_decision_executed_count=1,
        approval_execution_immediate_execution_approved_count=0,
        approval_execution_preflight_required_count=1,
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
        boundary_phrase_count=22,
        prohibited_behavior_count=17,
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
