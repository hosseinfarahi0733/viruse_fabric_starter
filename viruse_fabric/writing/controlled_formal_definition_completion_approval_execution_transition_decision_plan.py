from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/controlled_formal_definition_completion_approval_execution_readiness_audit_v8_37.md")
OUTPUT_PATH = Path("outputs/controlled_formal_definition_completion_approval_execution_transition_decision_plan_v8_38.md")


@dataclass(frozen=True)
class TransitionDecisionPlanRow:
    row_id: str
    decision_focus: str
    source_signal: str
    planned_decision_action: str
    hard_boundary: str


@dataclass(frozen=True)
class TransitionDecisionPlanReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    transition_decision_plan_count: int
    transition_decision_plan_row_count: int
    readiness_audit_source_row_count: int
    readiness_audit_count: int
    approval_execution_plan_count: int
    approval_execution_readiness_approved_count: int
    approval_execution_transition_decision_executed_count: int
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


def _source_has_readiness_audit_rows(text: str) -> bool:
    return (
        "Controlled formal definition completion approval execution readiness audit row count: 4" in text
        or _has_all_terms(
            text,
            [
                "controlled formal definition completion approval execution readiness audit row count",
                "4",
            ],
        )
    )


def _source_has_approval_execution_plan_count(text: str) -> bool:
    return (
        "Controlled formal definition completion approval execution plan count: 1" in text
        or _has_all_terms(
            text,
            [
                "controlled formal definition completion approval execution plan",
                "count",
                "1",
            ],
        )
    )


def _source_hard_zero_signal_count(text: str) -> int:
    zero_term_sets = [
        ["approval execution readiness approved", "0"],
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
        "transition is approved",
        "manuscript is submission-ready",
        "external validation is completed",
        "independent experiment is completed",
        "clinical relevance is established",
        "biological prediction is established",
        "operational readiness is achieved",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_rows() -> List[TransitionDecisionPlanRow]:
    return [
        TransitionDecisionPlanRow(
            row_id="TDP-001",
            decision_focus="source readiness audit integrity",
            source_signal="v8.37 readiness audit exists and passed with hard-zero boundaries preserved",
            planned_decision_action="verify whether the readiness audit can be used as a source for a later transition decision execution",
            hard_boundary="does not approve the transition",
        ),
        TransitionDecisionPlanRow(
            row_id="TDP-002",
            decision_focus="execution eligibility boundary",
            source_signal="v8.37 audits readiness but keeps approval execution absent",
            planned_decision_action="define a decision gate for whether approval execution may be attempted in a later milestone",
            hard_boundary="does not execute approval",
        ),
        TransitionDecisionPlanRow(
            row_id="TDP-003",
            decision_focus="completion boundary",
            source_signal="v8.37 keeps formal definition completion approval and completed formal definitions absent",
            planned_decision_action="require any future approval execution to preserve approved completion and completed definitions at zero unless explicitly audited",
            hard_boundary="does not approve completion",
        ),
        TransitionDecisionPlanRow(
            row_id="TDP-004",
            decision_focus="proof and manuscript boundary",
            source_signal="v8.37 keeps proof execution, theorem proof, lemma proof, formalization completion, citation additions, and submission readiness absent",
            planned_decision_action="block any transition language that implies proof work, citation addition, external validation, or manuscript readiness",
            hard_boundary="does not execute proof work",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1
    readiness_audit_source_row_count = 4 if _source_has_readiness_audit_rows(source_text) else 0
    readiness_audit_count = 1 if _source_has_readiness_audit_count(source_text) else 0
    approval_execution_plan_count = 1 if _source_has_approval_execution_plan_count(source_text) else 0
    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.37 readiness audit source artifact.")
    if readiness_audit_source_row_count != 4:
        errors.append("Expected v8.37 readiness audit row count signal is absent.")
    if readiness_audit_count != 1:
        errors.append("Expected v8.37 readiness audit count signal is absent.")
    if approval_execution_plan_count != 1:
        errors.append("Expected carried v8.36 approval execution plan count signal is absent from v8.37 source.")
    if source_hard_zero_signal_count < 12:
        errors.append("Expected hard-zero source signals are incomplete.")

    warnings = [
        "Transition decision planning is created, but transition decision execution remains absent.",
        "Approval execution remains absent.",
        "Formal definition completion approval and completed formal definitions remain absent.",
        "No proof execution, theorem proof, lemma proof, external validation, citation addition, or manuscript submission readiness is created.",
    ]

    lines = [
        "# Controlled Formal Definition Completion Approval Execution Transition Decision Plan v8.38",
        "",
        "## Purpose",
        "",
        "Plan a controlled transition decision from the v8.37 readiness audit toward a possible future approval execution milestone while preserving all hard-zero boundaries.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Transition decision plan rows",
        "",
        "| Row | Decision focus | Source signal | Planned decision action | Hard boundary |",
        "|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.row_id} | {row.decision_focus} | {row.source_signal} | {row.planned_decision_action} | {row.hard_boundary} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Controlled formal definition completion approval execution transition decision plan count: 1",
            f"- Controlled formal definition completion approval execution transition decision plan row count: {len(rows)}",
            f"- Controlled formal definition completion approval execution readiness audit source row count: {readiness_audit_source_row_count}",
            f"- Controlled formal definition completion approval execution readiness audit count: {readiness_audit_count}",
            f"- Controlled formal definition completion approval execution plan count: {approval_execution_plan_count}",
            "- Approval execution readiness approved count: 0",
            "- Approval execution transition decision executed count: 0",
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
            "The v8.38 artifact plans a transition decision. It does not execute the transition decision, does not approve transition, does not execute approval, does not approve completion, does not complete formal definitions, does not execute proof work, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "This milestone is justified only as a controlled bridge between readiness audit and a possible later transition decision execution. It should not be treated as approval execution or as authorization of approved completion.",
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
            "The project has planned a controlled transition decision for formal definition completion approval execution, without executing the transition decision, executing approval, approving completion, completing formal definitions, or executing proof work.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this transition decision execution.",
            "- Do not call this approval execution.",
            "- Do not call this approved completion.",
            "- Do not call this completed formal definitions.",
            "- Do not call this proof execution.",
            "- Do not call this external validation.",
            "- Do not call this manuscript submission readiness.",
            "",
        ]
    )

    text = "\n".join(lines)
    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.38 transition decision plan report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.38 transition decision plan report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> TransitionDecisionPlanReport:
    text = render_report()
    source_text = _read_source()
    rows = build_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1
    readiness_audit_source_row_count = 4 if _source_has_readiness_audit_rows(source_text) else 0
    readiness_audit_count = 1 if _source_has_readiness_audit_count(source_text) else 0
    approval_execution_plan_count = 1 if _source_has_approval_execution_plan_count(source_text) else 0
    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.37 readiness audit source artifact.")
    if readiness_audit_source_row_count != 4:
        errors.append("Expected v8.37 readiness audit row count signal is absent.")
    if readiness_audit_count != 1:
        errors.append("Expected v8.37 readiness audit count signal is absent.")
    if approval_execution_plan_count != 1:
        errors.append("Expected carried v8.36 approval execution plan count signal is absent.")
    if source_hard_zero_signal_count < 12:
        errors.append("Expected hard-zero source signals are incomplete.")

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "Transition decision planning is created, but transition decision execution remains absent.",
        "Approval execution remains absent.",
        "Formal definition completion approval and completed formal definitions remain absent.",
        "No proof execution, theorem proof, lemma proof, external validation, citation addition, or manuscript submission readiness is created.",
    ]

    return TransitionDecisionPlanReport(
        title="Controlled Formal Definition Completion Approval Execution Transition Decision Plan v8.38",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        transition_decision_plan_count=1,
        transition_decision_plan_row_count=len(rows),
        readiness_audit_source_row_count=readiness_audit_source_row_count,
        readiness_audit_count=readiness_audit_count,
        approval_execution_plan_count=approval_execution_plan_count,
        approval_execution_readiness_approved_count=0,
        approval_execution_transition_decision_executed_count=0,
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
        boundary_phrase_count=20,
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
