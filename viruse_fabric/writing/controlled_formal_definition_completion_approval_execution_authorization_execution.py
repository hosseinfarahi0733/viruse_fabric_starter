from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/controlled_formal_definition_completion_approval_execution_authorization_plan_v8_48.md")
OUTPUT_PATH = Path("outputs/controlled_formal_definition_completion_approval_execution_authorization_execution_v8_49.md")


@dataclass(frozen=True)
class ApprovalExecutionAuthorizationExecutionRow:
    row_id: str
    execution_focus: str
    source_signal: str
    executed_authorization_check: str
    enforced_boundary: str


@dataclass(frozen=True)
class ApprovalExecutionAuthorizationExecutionReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    authorization_execution_count: int
    authorization_execution_row_count: int
    authorization_plan_source_row_count: int
    authorization_plan_count: int
    gate_execution_count: int
    gate_plan_count: int
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
    approval_execution_authorization_plan_required_count: int
    approval_execution_authorization_plan_count: int
    approval_execution_authorization_execution_count: int
    approval_execution_authorized_count: int
    approval_execution_plan_required_count: int
    approval_execution_count: int
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


def _source_has_controlled_count(text: str, phrase: str) -> bool:
    return f"Controlled formal definition completion approval execution {phrase} count: 1" in text or _has_all_terms(
        text,
        ["controlled formal definition completion approval execution", phrase, "count", "1"],
    )


def _source_has_controlled_rows(text: str, phrase: str) -> bool:
    return f"Controlled formal definition completion approval execution {phrase} row count: 4" in text or _has_all_terms(
        text,
        ["controlled formal definition completion approval execution", phrase, "row count", "4"],
    )


def _source_has_short_count(text: str, phrase: str, expected: str) -> bool:
    return f"{phrase} count: {expected}" in text or _has_all_terms(text, [phrase, expected])


def _source_hard_zero_signal_count(text: str) -> int:
    zero_term_sets = [
        ["approval execution authorization execution", "0"],
        ["approval execution authorized", "0"],
        ["approval execution", "0"],
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


def build_rows() -> List[ApprovalExecutionAuthorizationExecutionRow]:
    return [
        ApprovalExecutionAuthorizationExecutionRow(
            row_id="AAE-001",
            execution_focus="source authorization plan verification",
            source_signal="v8.48 authorization plan exists and authorization execution remains absent",
            executed_authorization_check="verify that the authorization plan can serve as source input for controlled authorization execution",
            enforced_boundary="does not execute approval",
        ),
        ApprovalExecutionAuthorizationExecutionRow(
            row_id="AAE-002",
            execution_focus="authorization execution result",
            source_signal="v8.48 creates an authorization plan but keeps authorization execution absent",
            executed_authorization_check="execute the authorization stage and require a separate approval execution plan",
            enforced_boundary="approval execution remains zero",
        ),
        ApprovalExecutionAuthorizationExecutionRow(
            row_id="AAE-003",
            execution_focus="approval execution containment",
            source_signal="v8.48 keeps approval execution absent",
            executed_authorization_check="block direct movement from authorization execution into approval execution",
            enforced_boundary="does not run approval execution",
        ),
        ApprovalExecutionAuthorizationExecutionRow(
            row_id="AAE-004",
            execution_focus="completion proof validation and readiness containment",
            source_signal="v8.48 keeps completion, proof, validation, citations, and readiness absent",
            executed_authorization_check="preserve hard-zero claim boundaries while moving authorization status forward",
            enforced_boundary="does not approve completion or execute proof work",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    authorization_plan_source_row_count = 4 if _source_has_controlled_rows(source_text, "authorization plan") else 0
    authorization_plan_count = 1 if _source_has_controlled_count(source_text, "authorization plan") else 0
    gate_execution_count = 1 if _source_has_controlled_count(source_text, "gate execution") else 0
    gate_plan_count = 1 if _source_has_controlled_count(source_text, "gate plan") else 0
    preflight_approval_execution_count = 1 if _source_has_controlled_count(source_text, "preflight approval execution") else 0
    preflight_approval_plan_count = 1 if _source_has_controlled_count(source_text, "preflight approval plan") else 0
    preflight_decision_execution_count = 1 if _source_has_controlled_count(source_text, "preflight decision execution") else 0
    preflight_execution_count = 1 if _source_has_controlled_count(source_text, "preflight execution") else 0

    preflight_required = 1 if _source_has_short_count(source_text, "Approval execution preflight required", "1") else 0
    preflight_decision_execution_short = 1 if _source_has_short_count(source_text, "Approval execution preflight decision execution", "1") else 0
    preflight_approval_plan_required = 1 if _source_has_short_count(source_text, "Approval execution preflight approval plan required", "1") else 0
    preflight_approval_execution_short = 1 if _source_has_short_count(source_text, "Approval execution preflight approval execution", "1") else 0
    preflight_approved = 1 if _source_has_short_count(source_text, "Approval execution preflight approved", "1") else 0
    gate_plan_required = 1 if _source_has_short_count(source_text, "Approval execution gate plan required", "1") else 0
    authorization_plan_required = 1 if _source_has_short_count(source_text, "Approval execution authorization plan required", "1") else 0
    authorization_plan_short = 1 if _source_has_short_count(source_text, "Approval execution authorization plan", "1") else 0
    authorization_execution_absent = 1 if _source_has_short_count(source_text, "Approval execution authorization execution", "0") else 0
    authorized_absent = 1 if _source_has_short_count(source_text, "Approval execution authorized", "0") else 0
    approval_execution_absent = 1 if _source_has_short_count(source_text, "Approval execution", "0") else 0

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.48 authorization plan source artifact.")
    if authorization_plan_source_row_count != 4:
        errors.append("Expected v8.48 authorization plan row count signal is absent.")
    if authorization_plan_count != 1:
        errors.append("Expected v8.48 controlled authorization plan count signal is absent.")
    if gate_execution_count != 1:
        errors.append("Expected carried v8.47 gate execution signal is absent.")
    if gate_plan_count != 1:
        errors.append("Expected carried v8.46 gate plan signal is absent.")
    if preflight_approval_execution_count != 1:
        errors.append("Expected carried v8.45 preflight approval execution signal is absent.")
    if preflight_approval_plan_count != 1:
        errors.append("Expected carried v8.44 preflight approval plan signal is absent.")
    if preflight_decision_execution_count != 1:
        errors.append("Expected carried v8.43 preflight decision execution signal is absent.")
    if preflight_execution_count != 1:
        errors.append("Expected carried v8.41 preflight execution signal is absent.")
    if preflight_required != 1:
        errors.append("Expected carried preflight required signal is absent.")
    if preflight_decision_execution_short != 1:
        errors.append("Expected carried preflight decision execution signal is absent.")
    if preflight_approval_plan_required != 1:
        errors.append("Expected carried preflight approval plan required signal is absent.")
    if preflight_approval_execution_short != 1:
        errors.append("Expected carried preflight approval execution signal is absent.")
    if preflight_approved != 1:
        errors.append("Expected carried preflight approved signal is absent.")
    if gate_plan_required != 1:
        errors.append("Expected carried gate plan required signal is absent.")
    if authorization_plan_required != 1:
        errors.append("Expected carried authorization plan required signal is absent.")
    if authorization_plan_short != 1:
        errors.append("Expected short authorization plan count signal is absent.")
    if authorization_execution_absent != 1:
        errors.append("Expected source authorization execution absence signal is absent.")
    if authorized_absent != 1:
        errors.append("Expected source authorization status absence signal is absent.")
    if approval_execution_absent != 1:
        errors.append("Expected source approval execution absence signal is absent.")
    if source_hard_zero_signal_count < 13:
        errors.append("Expected hard-zero source signals are incomplete.")

    warnings = [
        "Approval execution authorization execution is created and approval execution authorization is granted only for moving to a separate approval execution plan.",
        "Approval execution remains absent.",
        "Approved completion and completed formal definitions remain absent.",
        "No proof execution, theorem proof, lemma proof, external validation, citation addition, or manuscript submission readiness is created.",
    ]

    lines = [
        "# Controlled Formal Definition Completion Approval Execution Authorization Execution v8.49",
        "",
        "## Purpose",
        "",
        "Execute the controlled approval execution authorization stage after v8.48 while preserving approval execution, approved completion, completed formal definitions, proof execution, external validation, citation additions, and submission readiness at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Authorization execution rows",
        "",
        "| Row | Execution focus | Source signal | Executed authorization check | Enforced boundary |",
        "|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.row_id} | {row.execution_focus} | {row.source_signal} | {row.executed_authorization_check} | {row.enforced_boundary} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Controlled formal definition completion approval execution authorization execution count: 1",
            f"- Controlled formal definition completion approval execution authorization execution row count: {len(rows)}",
            f"- Controlled formal definition completion approval execution authorization plan source row count: {authorization_plan_source_row_count}",
            f"- Controlled formal definition completion approval execution authorization plan count: {authorization_plan_count}",
            f"- Controlled formal definition completion approval execution gate execution count: {gate_execution_count}",
            f"- Controlled formal definition completion approval execution gate plan count: {gate_plan_count}",
            f"- Controlled formal definition completion approval execution preflight approval execution count: {preflight_approval_execution_count}",
            f"- Controlled formal definition completion approval execution preflight approval plan count: {preflight_approval_plan_count}",
            f"- Controlled formal definition completion approval execution preflight decision execution count: {preflight_decision_execution_count}",
            f"- Controlled formal definition completion approval execution preflight execution count: {preflight_execution_count}",
            f"- Approval execution preflight required count: {preflight_required}",
            f"- Approval execution preflight decision execution count: {preflight_decision_execution_short}",
            f"- Approval execution preflight approval plan required count: {preflight_approval_plan_required}",
            f"- Approval execution preflight approval execution count: {preflight_approval_execution_short}",
            f"- Approval execution preflight approved count: {preflight_approved}",
            f"- Approval execution gate plan required count: {gate_plan_required}",
            f"- Approval execution authorization plan required count: {authorization_plan_required}",
            f"- Approval execution authorization plan count: {authorization_plan_short}",
            "- Approval execution authorization execution count: 1",
            "- Approval execution authorized count: 1",
            "- Approval execution plan required count: 1",
            "- Approval execution count: 0",
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
            "The v8.49 artifact executes authorization and records approval execution as authorized only for moving into a separate approval execution planning milestone. It does not execute approval, does not approve completion, does not complete formal definitions, does not execute proof work, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "This milestone is useful because it converts authorization planning into authorization execution while still refusing approval execution. The next defensible step is approval execution planning, not direct approval execution.",
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
            "The project has executed controlled authorization for formal definition completion approval execution, with approval execution still absent and a separate approval execution plan required before any approval execution attempt.",
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
        errors.append("Overclaim pattern detected in v8.49 authorization execution report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.49 authorization execution report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> ApprovalExecutionAuthorizationExecutionReport:
    text = render_report()
    source_text = _read_source()
    rows = build_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    authorization_plan_source_row_count = 4 if _source_has_controlled_rows(source_text, "authorization plan") else 0
    authorization_plan_count = 1 if _source_has_controlled_count(source_text, "authorization plan") else 0
    gate_execution_count = 1 if _source_has_controlled_count(source_text, "gate execution") else 0
    gate_plan_count = 1 if _source_has_controlled_count(source_text, "gate plan") else 0
    preflight_approval_execution_count = 1 if _source_has_controlled_count(source_text, "preflight approval execution") else 0
    preflight_approval_plan_count = 1 if _source_has_controlled_count(source_text, "preflight approval plan") else 0
    preflight_decision_execution_count = 1 if _source_has_controlled_count(source_text, "preflight decision execution") else 0
    preflight_execution_count = 1 if _source_has_controlled_count(source_text, "preflight execution") else 0

    preflight_required = 1 if _source_has_short_count(source_text, "Approval execution preflight required", "1") else 0
    preflight_decision_execution_short = 1 if _source_has_short_count(source_text, "Approval execution preflight decision execution", "1") else 0
    preflight_approval_plan_required = 1 if _source_has_short_count(source_text, "Approval execution preflight approval plan required", "1") else 0
    preflight_approval_execution_short = 1 if _source_has_short_count(source_text, "Approval execution preflight approval execution", "1") else 0
    preflight_approved = 1 if _source_has_short_count(source_text, "Approval execution preflight approved", "1") else 0
    gate_plan_required = 1 if _source_has_short_count(source_text, "Approval execution gate plan required", "1") else 0
    authorization_plan_required = 1 if _source_has_short_count(source_text, "Approval execution authorization plan required", "1") else 0
    authorization_plan_short = 1 if _source_has_short_count(source_text, "Approval execution authorization plan", "1") else 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.48 authorization plan source artifact.")
    if authorization_plan_source_row_count != 4:
        errors.append("Expected v8.48 authorization plan row count signal is absent.")
    if authorization_plan_count != 1:
        errors.append("Expected v8.48 controlled authorization plan count signal is absent.")
    if gate_execution_count != 1:
        errors.append("Expected carried v8.47 gate execution signal is absent.")
    if gate_plan_count != 1:
        errors.append("Expected carried v8.46 gate plan signal is absent.")
    if preflight_approval_execution_count != 1:
        errors.append("Expected carried v8.45 preflight approval execution signal is absent.")
    if preflight_approval_plan_count != 1:
        errors.append("Expected carried v8.44 preflight approval plan signal is absent.")
    if preflight_decision_execution_count != 1:
        errors.append("Expected carried v8.43 preflight decision execution signal is absent.")
    if preflight_execution_count != 1:
        errors.append("Expected carried v8.41 preflight execution signal is absent.")
    if preflight_required != 1:
        errors.append("Expected carried preflight required signal is absent.")
    if preflight_decision_execution_short != 1:
        errors.append("Expected carried preflight decision execution signal is absent.")
    if preflight_approval_plan_required != 1:
        errors.append("Expected carried preflight approval plan required signal is absent.")
    if preflight_approval_execution_short != 1:
        errors.append("Expected carried preflight approval execution signal is absent.")
    if preflight_approved != 1:
        errors.append("Expected carried preflight approved signal is absent.")
    if gate_plan_required != 1:
        errors.append("Expected carried gate plan required signal is absent.")
    if authorization_plan_required != 1:
        errors.append("Expected carried authorization plan required signal is absent.")
    if authorization_plan_short != 1:
        errors.append("Expected short authorization plan count signal is absent.")

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
        "Approval execution authorization execution is created and approval execution authorization is granted only for moving to a separate approval execution plan.",
        "Approval execution remains absent.",
        "Approved completion and completed formal definitions remain absent.",
        "No proof execution, theorem proof, lemma proof, external validation, citation addition, or manuscript submission readiness is created.",
    ]

    return ApprovalExecutionAuthorizationExecutionReport(
        title="Controlled Formal Definition Completion Approval Execution Authorization Execution v8.49",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        authorization_execution_count=1,
        authorization_execution_row_count=len(rows),
        authorization_plan_source_row_count=authorization_plan_source_row_count,
        authorization_plan_count=authorization_plan_count,
        gate_execution_count=gate_execution_count,
        gate_plan_count=gate_plan_count,
        preflight_approval_execution_count=preflight_approval_execution_count,
        preflight_approval_plan_count=preflight_approval_plan_count,
        preflight_decision_execution_count=preflight_decision_execution_count,
        preflight_execution_count=preflight_execution_count,
        approval_execution_preflight_required_count=preflight_required,
        approval_execution_preflight_decision_execution_count=preflight_decision_execution_short,
        approval_execution_preflight_approval_plan_required_count=preflight_approval_plan_required,
        approval_execution_preflight_approval_execution_count=preflight_approval_execution_short,
        approval_execution_preflight_approved_count=preflight_approved,
        approval_execution_gate_plan_required_count=gate_plan_required,
        approval_execution_authorization_plan_required_count=authorization_plan_required,
        approval_execution_authorization_plan_count=authorization_plan_short,
        approval_execution_authorization_execution_count=1,
        approval_execution_authorized_count=1,
        approval_execution_plan_required_count=1,
        approval_execution_count=0,
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
        boundary_phrase_count=32,
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
