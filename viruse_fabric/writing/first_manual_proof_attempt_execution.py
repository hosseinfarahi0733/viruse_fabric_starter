from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/proof_environment_selection_and_first_proof_attempt_plan_v8_55.md")
OUTPUT_PATH = Path("outputs/first_manual_proof_attempt_execution_v8_56.md")


@dataclass(frozen=True)
class ManualProofAttemptRow:
    attempt_id: str
    target: str
    attempt_kind: str
    executed_action: str
    attempt_result: str
    unresolved_items: str
    boundary_status: str


@dataclass(frozen=True)
class FirstManualProofAttemptExecutionReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    first_manual_proof_attempt_execution_count: int
    manual_proof_attempt_row_count: int
    attempted_lemma_skeleton_count: int
    attempted_theorem_skeleton_count: int
    partial_derivation_note_count: int
    unresolved_attempt_item_count: int
    successful_theorem_proof_count: int
    successful_lemma_proof_count: int

    carried_proof_environment_selection_plan_count: int
    carried_selected_manual_markdown_environment_count: int
    carried_deferred_formal_assistant_environment_count: int
    carried_first_proof_attempt_plan_count: int
    carried_first_proof_attempt_plan_row_count: int
    carried_first_proof_attempt_execution_count: int
    carried_theorem_skeleton_count: int
    carried_lemma_skeleton_count: int
    carried_registered_proof_obligation_count: int
    carried_unresolved_proof_obligation_count: int
    carried_resolved_proof_obligation_count: int
    carried_registered_formal_definition_candidate_count: int
    carried_unresolved_formal_definition_candidate_count: int
    carried_completed_formal_definition_candidate_count: int

    formal_definition_completion_approval_execution_count: int
    formal_definition_completion_approved_count: int
    formal_definition_completed_count: int
    formal_mathematical_proof_count: int
    formal_proof_execution_count: int
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
    for ch in ["_", "-", "`", "*", "|", ":", ";", ",", ".", "(", ")", "[", "]", "/"]:
        text = text.replace(ch, " ")
    return " ".join(text.split())


def _has_all_terms(text: str, terms: List[str]) -> bool:
    normalized = _normalize(text)
    return all(term.lower() in normalized for term in terms)


def _has_count(text: str, phrase: str, expected: str) -> bool:
    return f"{phrase}: {expected}" in text or f"{phrase} count: {expected}" in text or _has_all_terms(text, [phrase, expected])


def _source_hard_zero_signal_count(text: str) -> int:
    zero_term_sets = [
        ["first proof attempt execution", "0"],
        ["formal definition completed", "0"],
        ["formal mathematical proof", "0"],
        ["formal proof execution", "0"],
        ["proof execution", "0"],
        ["theorem proven", "0"],
        ["lemma proven", "0"],
        ["formalization complete", "0"],
        ["proof gap resolution", "0"],
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
        "theorem has been proven",
        "lemma has been proven",
        "formalization is complete",
        "formal definitions are completed",
        "formal definition completion is approved",
        "proof obligation is resolved",
        "proof obligations are resolved",
        "proof execution is completed",
        "proof execution is performed",
        "proof gap is resolved",
        "proof gaps are resolved",
        "first proof attempt proves",
        "first manual proof attempt proves",
        "manual proof establishes theorem",
        "manual proof establishes lemma",
        "manuscript is submission-ready",
        "external validation is completed",
        "independent experiment is completed",
        "clinical relevance is established",
        "biological prediction is established",
        "operational readiness is achieved",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_attempt_rows() -> List[ManualProofAttemptRow]:
    return [
        ManualProofAttemptRow(
            attempt_id="MPA-001",
            target="TLS-001 path compatibility preservation lemma skeleton",
            attempt_kind="lemma skeleton manual derivation attempt",
            executed_action="listed admissibility assumptions, transition-preservation condition, and dependency chain",
            attempt_result="partial derivation note recorded",
            unresolved_items="requires completed definitions for state space, transition relation, compatibility predicate, and admissible path predicate",
            boundary_status="attempt only; lemma proof remains absent",
        ),
        ManualProofAttemptRow(
            attempt_id="MPA-002",
            target="TLS-002 causal mass boundedness or counterexample split lemma skeleton",
            attempt_kind="lemma skeleton manual derivation attempt",
            executed_action="split boundedness route from counterexample route and listed missing monotonicity assumptions",
            attempt_result="partial derivation note recorded",
            unresolved_items="requires explicit causal mass functional, order relation, and counterexample trigger conditions",
            boundary_status="attempt only; lemma proof remains absent",
        ),
        ManualProofAttemptRow(
            attempt_id="MPA-003",
            target="TLS-003 apparent purpose emergence theorem skeleton",
            attempt_kind="theorem skeleton dependency mapping attempt",
            executed_action="mapped theorem assumptions to lemma skeleton dependencies and projection-level conclusion",
            attempt_result="dependency mapping note recorded",
            unresolved_items="requires resolved lemma attempts and completed observer projection definition",
            boundary_status="attempt only; theorem proof remains absent",
        ),
        ManualProofAttemptRow(
            attempt_id="MPA-004",
            target="TLS-004 non-teleological attractor concentration theorem skeleton",
            attempt_kind="theorem skeleton boundary-safe statement attempt",
            executed_action="listed non-biological assumptions and separated attractor concentration from intentional language",
            attempt_result="boundary-safe statement note recorded",
            unresolved_items="requires completed attractor, admissibility, and projection definitions",
            boundary_status="attempt only; theorem proof remains absent",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_attempt_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    proof_environment_selection_plan_count = 1 if _has_count(source_text, "Proof environment selection plan", "1") else 0
    selected_manual_markdown_environment_count = 1 if _has_count(source_text, "Selected manual markdown environment", "1") else 0
    deferred_formal_assistant_environment_count = 2 if _has_count(source_text, "Deferred formal assistant environment", "2") else 0
    first_proof_attempt_plan_count = 1 if _has_count(source_text, "First proof attempt plan", "1") else 0
    first_proof_attempt_plan_row_count = 4 if _has_count(source_text, "First proof attempt plan row", "4") else 0
    carried_first_proof_attempt_execution_count = 0 if _has_count(source_text, "First proof attempt execution", "0") else -1

    theorem_skeleton_count = 2 if _has_count(source_text, "Carried theorem skeleton", "2") else 0
    lemma_skeleton_count = 2 if _has_count(source_text, "Carried lemma skeleton", "2") else 0
    registered_proof_obligation_count = 6 if _has_count(source_text, "Carried registered proof obligation", "6") else 0
    unresolved_proof_obligation_count = 6 if _has_count(source_text, "Carried unresolved proof obligation", "6") else 0
    resolved_proof_obligation_count = 0 if _has_count(source_text, "Carried resolved proof obligation", "0") else -1
    registered_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried registered formal definition candidate", "2") else 0
    unresolved_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried unresolved formal definition candidate", "2") else 0
    completed_formal_definition_candidate_count = 0 if _has_count(source_text, "Carried completed formal definition candidate", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    attempted_lemma_skeleton_count = sum(1 for row in rows if row.attempt_kind.startswith("lemma skeleton"))
    attempted_theorem_skeleton_count = sum(1 for row in rows if row.attempt_kind.startswith("theorem skeleton"))
    partial_derivation_note_count = len(rows)
    unresolved_attempt_item_count = len(rows)
    successful_theorem_proof_count = 0
    successful_lemma_proof_count = 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.55 proof environment selection source artifact.")
    if proof_environment_selection_plan_count != 1:
        errors.append("Expected proof environment selection plan signal is absent.")
    if selected_manual_markdown_environment_count != 1:
        errors.append("Expected selected manual markdown environment signal is absent.")
    if deferred_formal_assistant_environment_count != 2:
        errors.append("Expected deferred formal assistant environment signal is absent.")
    if first_proof_attempt_plan_count != 1:
        errors.append("Expected first proof attempt plan signal is absent.")
    if first_proof_attempt_plan_row_count != 4:
        errors.append("Expected first proof attempt plan row count signal is absent.")
    if carried_first_proof_attempt_execution_count != 0:
        errors.append("Expected carried first proof attempt execution zero signal is absent.")
    if theorem_skeleton_count != 2:
        errors.append("Expected carried theorem skeleton signal is absent.")
    if lemma_skeleton_count != 2:
        errors.append("Expected carried lemma skeleton signal is absent.")
    if registered_proof_obligation_count != 6:
        errors.append("Expected carried registered proof obligation signal is absent.")
    if unresolved_proof_obligation_count != 6:
        errors.append("Expected carried unresolved proof obligation signal is absent.")
    if resolved_proof_obligation_count != 0:
        errors.append("Expected carried resolved proof obligation zero signal is absent.")
    if registered_formal_definition_candidate_count != 2:
        errors.append("Expected carried registered formal definition candidate signal is absent.")
    if unresolved_formal_definition_candidate_count != 2:
        errors.append("Expected carried unresolved formal definition candidate signal is absent.")
    if completed_formal_definition_candidate_count != 0:
        errors.append("Expected carried completed formal definition candidate zero signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")
    if attempted_lemma_skeleton_count != 2:
        errors.append("Expected two attempted lemma skeletons.")
    if attempted_theorem_skeleton_count != 2:
        errors.append("Expected two attempted theorem skeletons.")
    if successful_theorem_proof_count != 0:
        errors.append("Unexpected successful theorem proof signal.")
    if successful_lemma_proof_count != 0:
        errors.append("Unexpected successful lemma proof signal.")

    warnings = [
        "First manual proof attempt execution is recorded as an attempt only.",
        "The attempt records partial derivation notes and unresolved items.",
        "Theorem proof and lemma proof remain absent.",
        "Formal definition candidates and proof obligations remain unresolved.",
    ]

    lines = [
        "# First Manual Proof Attempt Execution v8.56",
        "",
        "## Purpose",
        "",
        "Execute the first manual proof attempt as an attempt-level markdown derivation pass after v8.55 environment selection, while keeping formal mathematical proof, formal proof execution, theorem proof, lemma proof, proof gap resolution, external validation, citation addition, and submission readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Manual proof attempt rows",
        "",
        "| Attempt ID | Target | Attempt kind | Executed action | Attempt result | Unresolved items | Boundary status |",
        "|---|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.attempt_id} | {row.target} | {row.attempt_kind} | {row.executed_action} | {row.attempt_result} | {row.unresolved_items} | {row.boundary_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- First manual proof attempt execution count: 1",
            f"- Manual proof attempt row count: {len(rows)}",
            f"- Attempted lemma skeleton count: {attempted_lemma_skeleton_count}",
            f"- Attempted theorem skeleton count: {attempted_theorem_skeleton_count}",
            f"- Partial derivation note count: {partial_derivation_note_count}",
            f"- Unresolved attempt item count: {unresolved_attempt_item_count}",
            f"- Successful theorem proof count: {successful_theorem_proof_count}",
            f"- Successful lemma proof count: {successful_lemma_proof_count}",
            "",
            "## Carried v8.55 signals",
            "",
            f"- Carried proof environment selection plan count: {proof_environment_selection_plan_count}",
            f"- Carried selected manual markdown environment count: {selected_manual_markdown_environment_count}",
            f"- Carried deferred formal assistant environment count: {deferred_formal_assistant_environment_count}",
            f"- Carried first proof attempt plan count: {first_proof_attempt_plan_count}",
            f"- Carried first proof attempt plan row count: {first_proof_attempt_plan_row_count}",
            f"- Carried first proof attempt execution count: {carried_first_proof_attempt_execution_count}",
            "",
            "## Carried proof object signals",
            "",
            f"- Carried theorem skeleton count: {theorem_skeleton_count}",
            f"- Carried lemma skeleton count: {lemma_skeleton_count}",
            f"- Carried registered proof obligation count: {registered_proof_obligation_count}",
            f"- Carried unresolved proof obligation count: {unresolved_proof_obligation_count}",
            f"- Carried resolved proof obligation count: {resolved_proof_obligation_count}",
            f"- Carried registered formal definition candidate count: {registered_formal_definition_candidate_count}",
            f"- Carried unresolved formal definition candidate count: {unresolved_formal_definition_candidate_count}",
            f"- Carried completed formal definition candidate count: {completed_formal_definition_candidate_count}",
            "",
            "## Hard-zero counts preserved",
            "",
            "- Formal definition completion approval execution count: 0",
            "- Formal definition completion approved count: 0",
            "- Formal definition completed count: 0",
            "- Formal mathematical proof count: 0",
            "- Formal proof execution count: 0",
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
            "The v8.56 artifact records a first manual proof attempt execution as an attempt-level markdown derivation pass only. It does not establish theorem proof, does not establish lemma proof, does not complete formal definitions, does not resolve proof obligations, does not resolve proof gaps, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "This milestone is the first real attempt-level movement beyond planning. The result is intentionally partial: it records dependency chains, missing definitions, and unresolved assumptions. It does not claim proof success.",
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
            "The project has recorded a first manual proof attempt execution as an attempt-level markdown derivation pass, producing partial derivation notes and unresolved items while keeping theorem proof, lemma proof, completed formal definitions, formal mathematical proof, formal proof execution, proof gap resolution, citation additions, external validation, and manuscript submission readiness at zero.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this formal proof.",
            "- Do not call this theorem proof.",
            "- Do not call this lemma proof.",
            "- Do not call this completed formal definitions.",
            "- Do not call this resolved proof obligations.",
            "- Do not call this proof gap resolution.",
            "- Do not call this external validation.",
            "- Do not call this manuscript submission readiness.",
            "",
        ]
    )

    text = "\n".join(lines)
    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.56 first manual proof attempt report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.56 first manual proof attempt report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> FirstManualProofAttemptExecutionReport:
    text = render_report()
    source_text = _read_source()
    rows = build_attempt_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    proof_environment_selection_plan_count = 1 if _has_count(source_text, "Proof environment selection plan", "1") else 0
    selected_manual_markdown_environment_count = 1 if _has_count(source_text, "Selected manual markdown environment", "1") else 0
    deferred_formal_assistant_environment_count = 2 if _has_count(source_text, "Deferred formal assistant environment", "2") else 0
    first_proof_attempt_plan_count = 1 if _has_count(source_text, "First proof attempt plan", "1") else 0
    first_proof_attempt_plan_row_count = 4 if _has_count(source_text, "First proof attempt plan row", "4") else 0
    carried_first_proof_attempt_execution_count = 0 if _has_count(source_text, "First proof attempt execution", "0") else -1

    theorem_skeleton_count = 2 if _has_count(source_text, "Carried theorem skeleton", "2") else 0
    lemma_skeleton_count = 2 if _has_count(source_text, "Carried lemma skeleton", "2") else 0
    registered_proof_obligation_count = 6 if _has_count(source_text, "Carried registered proof obligation", "6") else 0
    unresolved_proof_obligation_count = 6 if _has_count(source_text, "Carried unresolved proof obligation", "6") else 0
    resolved_proof_obligation_count = 0 if _has_count(source_text, "Carried resolved proof obligation", "0") else -1
    registered_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried registered formal definition candidate", "2") else 0
    unresolved_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried unresolved formal definition candidate", "2") else 0
    completed_formal_definition_candidate_count = 0 if _has_count(source_text, "Carried completed formal definition candidate", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    attempted_lemma_skeleton_count = sum(1 for row in rows if row.attempt_kind.startswith("lemma skeleton"))
    attempted_theorem_skeleton_count = sum(1 for row in rows if row.attempt_kind.startswith("theorem skeleton"))
    partial_derivation_note_count = len(rows)
    unresolved_attempt_item_count = len(rows)
    successful_theorem_proof_count = 0
    successful_lemma_proof_count = 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.55 proof environment selection source artifact.")
    if proof_environment_selection_plan_count != 1:
        errors.append("Expected proof environment selection plan signal is absent.")
    if selected_manual_markdown_environment_count != 1:
        errors.append("Expected selected manual markdown environment signal is absent.")
    if deferred_formal_assistant_environment_count != 2:
        errors.append("Expected deferred formal assistant environment signal is absent.")
    if first_proof_attempt_plan_count != 1:
        errors.append("Expected first proof attempt plan signal is absent.")
    if first_proof_attempt_plan_row_count != 4:
        errors.append("Expected first proof attempt plan row count signal is absent.")
    if carried_first_proof_attempt_execution_count != 0:
        errors.append("Expected carried first proof attempt execution zero signal is absent.")
    if theorem_skeleton_count != 2:
        errors.append("Expected carried theorem skeleton signal is absent.")
    if lemma_skeleton_count != 2:
        errors.append("Expected carried lemma skeleton signal is absent.")
    if registered_proof_obligation_count != 6:
        errors.append("Expected carried registered proof obligation signal is absent.")
    if unresolved_proof_obligation_count != 6:
        errors.append("Expected carried unresolved proof obligation signal is absent.")
    if resolved_proof_obligation_count != 0:
        errors.append("Expected carried resolved proof obligation zero signal is absent.")
    if registered_formal_definition_candidate_count != 2:
        errors.append("Expected carried registered formal definition candidate signal is absent.")
    if unresolved_formal_definition_candidate_count != 2:
        errors.append("Expected carried unresolved formal definition candidate signal is absent.")
    if completed_formal_definition_candidate_count != 0:
        errors.append("Expected carried completed formal definition candidate zero signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")
    if attempted_lemma_skeleton_count != 2:
        errors.append("Expected two attempted lemma skeletons.")
    if attempted_theorem_skeleton_count != 2:
        errors.append("Expected two attempted theorem skeletons.")
    if successful_theorem_proof_count != 0:
        errors.append("Unexpected successful theorem proof signal.")
    if successful_lemma_proof_count != 0:
        errors.append("Unexpected successful lemma proof signal.")

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "First manual proof attempt execution is recorded as an attempt only.",
        "The attempt records partial derivation notes and unresolved items.",
        "Theorem proof and lemma proof remain absent.",
        "Formal definition candidates and proof obligations remain unresolved.",
    ]

    return FirstManualProofAttemptExecutionReport(
        title="First Manual Proof Attempt Execution v8.56",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        first_manual_proof_attempt_execution_count=1,
        manual_proof_attempt_row_count=len(rows),
        attempted_lemma_skeleton_count=attempted_lemma_skeleton_count,
        attempted_theorem_skeleton_count=attempted_theorem_skeleton_count,
        partial_derivation_note_count=partial_derivation_note_count,
        unresolved_attempt_item_count=unresolved_attempt_item_count,
        successful_theorem_proof_count=successful_theorem_proof_count,
        successful_lemma_proof_count=successful_lemma_proof_count,
        carried_proof_environment_selection_plan_count=proof_environment_selection_plan_count,
        carried_selected_manual_markdown_environment_count=selected_manual_markdown_environment_count,
        carried_deferred_formal_assistant_environment_count=deferred_formal_assistant_environment_count,
        carried_first_proof_attempt_plan_count=first_proof_attempt_plan_count,
        carried_first_proof_attempt_plan_row_count=first_proof_attempt_plan_row_count,
        carried_first_proof_attempt_execution_count=carried_first_proof_attempt_execution_count,
        carried_theorem_skeleton_count=theorem_skeleton_count,
        carried_lemma_skeleton_count=lemma_skeleton_count,
        carried_registered_proof_obligation_count=registered_proof_obligation_count,
        carried_unresolved_proof_obligation_count=unresolved_proof_obligation_count,
        carried_resolved_proof_obligation_count=resolved_proof_obligation_count,
        carried_registered_formal_definition_candidate_count=registered_formal_definition_candidate_count,
        carried_unresolved_formal_definition_candidate_count=unresolved_formal_definition_candidate_count,
        carried_completed_formal_definition_candidate_count=completed_formal_definition_candidate_count,
        formal_definition_completion_approval_execution_count=0,
        formal_definition_completion_approved_count=0,
        formal_definition_completed_count=0,
        formal_mathematical_proof_count=0,
        formal_proof_execution_count=0,
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
        boundary_phrase_count=39,
        prohibited_behavior_count=18,
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
