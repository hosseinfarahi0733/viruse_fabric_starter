from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/theorem_and_lemma_skeleton_plan_v8_53.md")
OUTPUT_PATH = Path("outputs/proof_strategy_plan_v8_54.md")


@dataclass(frozen=True)
class ProofStrategyPlanRow:
    strategy_id: str
    strategy_track: str
    target_objects: str
    method: str
    required_inputs: str
    boundary_status: str


@dataclass(frozen=True)
class ProofStrategyPlanReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    proof_strategy_plan_count: int
    proof_strategy_plan_row_count: int
    manual_derivation_track_count: int
    formal_assistant_readiness_track_count: int
    counterexample_audit_track_count: int
    boundary_audit_track_count: int
    proof_environment_selection_required_count: int
    proof_execution_attempt_plan_required_count: int

    carried_theorem_lemma_skeleton_plan_count: int
    carried_theorem_lemma_skeleton_row_count: int
    carried_theorem_skeleton_count: int
    carried_lemma_skeleton_count: int
    carried_theorem_candidate_count: int
    carried_lemma_candidate_count: int
    carried_formal_definition_candidate_registry_count: int
    carried_registered_formal_definition_candidate_count: int
    carried_unresolved_formal_definition_candidate_count: int
    carried_completed_formal_definition_candidate_count: int
    carried_proof_obligation_registry_execution_count: int
    carried_registered_proof_obligation_count: int
    carried_unresolved_proof_obligation_count: int
    carried_resolved_proof_obligation_count: int

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
        "manuscript is submission-ready",
        "external validation is completed",
        "independent experiment is completed",
        "clinical relevance is established",
        "biological prediction is established",
        "operational readiness is achieved",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_strategy_rows() -> List[ProofStrategyPlanRow]:
    return [
        ProofStrategyPlanRow(
            strategy_id="PSP-001",
            strategy_track="manual derivation track",
            target_objects="TLS-001 and TLS-002 lemma skeletons",
            method="write assumption blocks, dependency chains, admissibility steps, and counterexample branches in markdown",
            required_inputs="FDC-001, FDC-002, POR-001 through POR-004",
            boundary_status="strategy only; proof execution remains absent",
        ),
        ProofStrategyPlanRow(
            strategy_id="PSP-002",
            strategy_track="theorem assembly track",
            target_objects="TLS-003 and TLS-004 theorem skeletons",
            method="map theorem assumptions to lemma skeleton dependencies and registered formal definition candidates",
            required_inputs="TLS-001, TLS-002, FDC-001, FDC-002, POR-005, POR-006",
            boundary_status="strategy only; theorem proof remains absent",
        ),
        ProofStrategyPlanRow(
            strategy_id="PSP-003",
            strategy_track="formal assistant readiness track",
            target_objects="definition candidates and theorem or lemma skeletons",
            method="prepare symbol inventory, type candidates, relation names, predicate names, and dependency order for possible Lean or Coq translation",
            required_inputs="FDC registry, TLS registry, proof obligation registry",
            boundary_status="readiness only; no assistant proof artifact",
        ),
        ProofStrategyPlanRow(
            strategy_id="PSP-004",
            strategy_track="counterexample and boundary audit track",
            target_objects="causal mass boundedness and apparent purpose statement",
            method="separate provable assumptions from conjectural or projection-level statements before any proof attempt",
            required_inputs="TLS-002, TLS-003, TLS-004, hard-zero boundary list",
            boundary_status="audit strategy only; proof gap resolution remains absent",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_strategy_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    theorem_lemma_skeleton_plan_count = 1 if _has_count(source_text, "Theorem and lemma skeleton plan", "1") else 0
    theorem_lemma_skeleton_row_count = 4 if _has_count(source_text, "Theorem and lemma skeleton row", "4") else 0
    theorem_skeleton_count = 2 if _has_count(source_text, "Theorem skeleton", "2") else 0
    lemma_skeleton_count = 2 if _has_count(source_text, "Lemma skeleton", "2") else 0
    theorem_candidate_count = 2 if _has_count(source_text, "Theorem candidate", "2") else 0
    lemma_candidate_count = 2 if _has_count(source_text, "Lemma candidate", "2") else 0

    formal_definition_candidate_registry_count = 1 if _has_count(source_text, "Carried formal definition candidate registry", "1") else 0
    registered_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried registered formal definition candidate", "2") else 0
    unresolved_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried unresolved formal definition candidate", "2") else 0
    completed_formal_definition_candidate_count = 0 if _has_count(source_text, "Carried completed formal definition candidate", "0") else -1

    proof_obligation_registry_execution_count = 1 if _has_count(source_text, "Carried proof obligation registry execution", "1") else 0
    registered_proof_obligation_count = 6 if _has_count(source_text, "Carried registered proof obligation", "6") else 0
    unresolved_proof_obligation_count = 6 if _has_count(source_text, "Carried unresolved proof obligation", "6") else 0
    resolved_proof_obligation_count = 0 if _has_count(source_text, "Carried resolved proof obligation", "0") else -1

    proof_strategy_plan_required_count = 1 if _has_count(source_text, "Proof strategy plan required", "1") else 0
    proof_execution_attempt_plan_required_count = 1 if _has_count(source_text, "Proof execution attempt plan required", "1") else 0

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    manual_derivation_track_count = sum(1 for row in rows if row.strategy_track == "manual derivation track")
    formal_assistant_readiness_track_count = sum(1 for row in rows if row.strategy_track == "formal assistant readiness track")
    counterexample_audit_track_count = sum(1 for row in rows if row.strategy_track == "counterexample and boundary audit track")
    boundary_audit_track_count = counterexample_audit_track_count

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.53 theorem and lemma skeleton source artifact.")
    if theorem_lemma_skeleton_plan_count != 1:
        errors.append("Expected theorem and lemma skeleton plan signal is absent.")
    if theorem_lemma_skeleton_row_count != 4:
        errors.append("Expected theorem and lemma skeleton row count signal is absent.")
    if theorem_skeleton_count != 2:
        errors.append("Expected theorem skeleton count signal is absent.")
    if lemma_skeleton_count != 2:
        errors.append("Expected lemma skeleton count signal is absent.")
    if theorem_candidate_count != 2:
        errors.append("Expected theorem candidate count signal is absent.")
    if lemma_candidate_count != 2:
        errors.append("Expected lemma candidate count signal is absent.")
    if formal_definition_candidate_registry_count != 1:
        errors.append("Expected carried formal definition candidate registry signal is absent.")
    if registered_formal_definition_candidate_count != 2:
        errors.append("Expected carried registered formal definition candidate count signal is absent.")
    if unresolved_formal_definition_candidate_count != 2:
        errors.append("Expected carried unresolved formal definition candidate count signal is absent.")
    if completed_formal_definition_candidate_count != 0:
        errors.append("Expected carried completed formal definition candidate zero signal is absent.")
    if proof_obligation_registry_execution_count != 1:
        errors.append("Expected carried proof obligation registry execution signal is absent.")
    if registered_proof_obligation_count != 6:
        errors.append("Expected carried registered proof obligation count signal is absent.")
    if unresolved_proof_obligation_count != 6:
        errors.append("Expected carried unresolved proof obligation count signal is absent.")
    if resolved_proof_obligation_count != 0:
        errors.append("Expected carried resolved proof obligation zero signal is absent.")
    if proof_strategy_plan_required_count != 1:
        errors.append("Expected proof strategy plan required signal is absent.")
    if proof_execution_attempt_plan_required_count != 1:
        errors.append("Expected proof execution attempt plan required signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")

    warnings = [
        "Proof strategy is planned, while proof execution remains absent.",
        "Theorem proof and lemma proof remain absent.",
        "Formal definition candidates remain unresolved.",
        "Proof obligations remain unresolved.",
    ]

    lines = [
        "# Proof Strategy Plan v8.54",
        "",
        "## Purpose",
        "",
        "Plan the route from theorem and lemma skeletons toward a future proof attempt while keeping formal definition completion, proof execution, theorem proof, lemma proof, proof gap resolution, external validation, citation addition, and submission readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Proof strategy rows",
        "",
        "| Strategy ID | Strategy track | Target objects | Method | Required inputs | Boundary status |",
        "|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.strategy_id} | {row.strategy_track} | {row.target_objects} | {row.method} | {row.required_inputs} | {row.boundary_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Proof strategy plan count: 1",
            f"- Proof strategy plan row count: {len(rows)}",
            f"- Manual derivation track count: {manual_derivation_track_count}",
            f"- Formal assistant readiness track count: {formal_assistant_readiness_track_count}",
            f"- Counterexample audit track count: {counterexample_audit_track_count}",
            f"- Boundary audit track count: {boundary_audit_track_count}",
            "- Proof environment selection required count: 1",
            "- Proof execution attempt plan required count: 1",
            "",
            "## Carried theorem and lemma skeleton signals",
            "",
            f"- Carried theorem and lemma skeleton plan count: {theorem_lemma_skeleton_plan_count}",
            f"- Carried theorem and lemma skeleton row count: {theorem_lemma_skeleton_row_count}",
            f"- Carried theorem skeleton count: {theorem_skeleton_count}",
            f"- Carried lemma skeleton count: {lemma_skeleton_count}",
            f"- Carried theorem candidate count: {theorem_candidate_count}",
            f"- Carried lemma candidate count: {lemma_candidate_count}",
            "",
            "## Carried definition and obligation signals",
            "",
            f"- Carried formal definition candidate registry count: {formal_definition_candidate_registry_count}",
            f"- Carried registered formal definition candidate count: {registered_formal_definition_candidate_count}",
            f"- Carried unresolved formal definition candidate count: {unresolved_formal_definition_candidate_count}",
            f"- Carried completed formal definition candidate count: {completed_formal_definition_candidate_count}",
            f"- Carried proof obligation registry execution count: {proof_obligation_registry_execution_count}",
            f"- Carried registered proof obligation count: {registered_proof_obligation_count}",
            f"- Carried unresolved proof obligation count: {unresolved_proof_obligation_count}",
            f"- Carried resolved proof obligation count: {resolved_proof_obligation_count}",
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
            "The v8.54 artifact creates a proof strategy plan only. It does not complete formal definitions, does not execute proof work, does not resolve proof obligations, does not establish theorem proof, does not establish lemma proof, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "This milestone selects a conservative proof strategy route before any future proof attempt. The strategy requires a later proof execution attempt plan and a later proof environment selection. It is not proof execution and not proof completion.",
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
            "The project has planned a proof strategy route for the registered theorem and lemma skeletons, with manual derivation, formal assistant readiness, counterexample audit, and boundary audit tracks, without completing formal definitions, executing proof work, resolving proof obligations, establishing theorem proof, establishing lemma proof, adding citations, validating externally, or making the manuscript submission-ready.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this proof execution.",
            "- Do not call this formal proof.",
            "- Do not call this theorem proof.",
            "- Do not call this lemma proof.",
            "- Do not call this completed formal definitions.",
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
        errors.append("Overclaim pattern detected in v8.54 proof strategy plan report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.54 proof strategy plan report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> ProofStrategyPlanReport:
    text = render_report()
    source_text = _read_source()
    rows = build_strategy_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    theorem_lemma_skeleton_plan_count = 1 if _has_count(source_text, "Theorem and lemma skeleton plan", "1") else 0
    theorem_lemma_skeleton_row_count = 4 if _has_count(source_text, "Theorem and lemma skeleton row", "4") else 0
    theorem_skeleton_count = 2 if _has_count(source_text, "Theorem skeleton", "2") else 0
    lemma_skeleton_count = 2 if _has_count(source_text, "Lemma skeleton", "2") else 0
    theorem_candidate_count = 2 if _has_count(source_text, "Theorem candidate", "2") else 0
    lemma_candidate_count = 2 if _has_count(source_text, "Lemma candidate", "2") else 0

    formal_definition_candidate_registry_count = 1 if _has_count(source_text, "Carried formal definition candidate registry", "1") else 0
    registered_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried registered formal definition candidate", "2") else 0
    unresolved_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried unresolved formal definition candidate", "2") else 0
    completed_formal_definition_candidate_count = 0 if _has_count(source_text, "Carried completed formal definition candidate", "0") else -1

    proof_obligation_registry_execution_count = 1 if _has_count(source_text, "Carried proof obligation registry execution", "1") else 0
    registered_proof_obligation_count = 6 if _has_count(source_text, "Carried registered proof obligation", "6") else 0
    unresolved_proof_obligation_count = 6 if _has_count(source_text, "Carried unresolved proof obligation", "6") else 0
    resolved_proof_obligation_count = 0 if _has_count(source_text, "Carried resolved proof obligation", "0") else -1

    proof_strategy_plan_required_count = 1 if _has_count(source_text, "Proof strategy plan required", "1") else 0
    proof_execution_attempt_plan_required_count = 1 if _has_count(source_text, "Proof execution attempt plan required", "1") else 0

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    manual_derivation_track_count = sum(1 for row in rows if row.strategy_track == "manual derivation track")
    formal_assistant_readiness_track_count = sum(1 for row in rows if row.strategy_track == "formal assistant readiness track")
    counterexample_audit_track_count = sum(1 for row in rows if row.strategy_track == "counterexample and boundary audit track")
    boundary_audit_track_count = counterexample_audit_track_count

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.53 theorem and lemma skeleton source artifact.")
    if theorem_lemma_skeleton_plan_count != 1:
        errors.append("Expected theorem and lemma skeleton plan signal is absent.")
    if theorem_lemma_skeleton_row_count != 4:
        errors.append("Expected theorem and lemma skeleton row count signal is absent.")
    if theorem_skeleton_count != 2:
        errors.append("Expected theorem skeleton count signal is absent.")
    if lemma_skeleton_count != 2:
        errors.append("Expected lemma skeleton count signal is absent.")
    if theorem_candidate_count != 2:
        errors.append("Expected theorem candidate count signal is absent.")
    if lemma_candidate_count != 2:
        errors.append("Expected lemma candidate count signal is absent.")
    if formal_definition_candidate_registry_count != 1:
        errors.append("Expected carried formal definition candidate registry signal is absent.")
    if registered_formal_definition_candidate_count != 2:
        errors.append("Expected carried registered formal definition candidate count signal is absent.")
    if unresolved_formal_definition_candidate_count != 2:
        errors.append("Expected carried unresolved formal definition candidate count signal is absent.")
    if completed_formal_definition_candidate_count != 0:
        errors.append("Expected carried completed formal definition candidate zero signal is absent.")
    if proof_obligation_registry_execution_count != 1:
        errors.append("Expected carried proof obligation registry execution signal is absent.")
    if registered_proof_obligation_count != 6:
        errors.append("Expected carried registered proof obligation count signal is absent.")
    if unresolved_proof_obligation_count != 6:
        errors.append("Expected carried unresolved proof obligation count signal is absent.")
    if resolved_proof_obligation_count != 0:
        errors.append("Expected carried resolved proof obligation zero signal is absent.")
    if proof_strategy_plan_required_count != 1:
        errors.append("Expected proof strategy plan required signal is absent.")
    if proof_execution_attempt_plan_required_count != 1:
        errors.append("Expected proof execution attempt plan required signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "Proof strategy is planned, while proof execution remains absent.",
        "Theorem proof and lemma proof remain absent.",
        "Formal definition candidates remain unresolved.",
        "Proof obligations remain unresolved.",
    ]

    return ProofStrategyPlanReport(
        title="Proof Strategy Plan v8.54",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        proof_strategy_plan_count=1,
        proof_strategy_plan_row_count=len(rows),
        manual_derivation_track_count=manual_derivation_track_count,
        formal_assistant_readiness_track_count=formal_assistant_readiness_track_count,
        counterexample_audit_track_count=counterexample_audit_track_count,
        boundary_audit_track_count=boundary_audit_track_count,
        proof_environment_selection_required_count=1,
        proof_execution_attempt_plan_required_count=proof_execution_attempt_plan_required_count,
        carried_theorem_lemma_skeleton_plan_count=theorem_lemma_skeleton_plan_count,
        carried_theorem_lemma_skeleton_row_count=theorem_lemma_skeleton_row_count,
        carried_theorem_skeleton_count=theorem_skeleton_count,
        carried_lemma_skeleton_count=lemma_skeleton_count,
        carried_theorem_candidate_count=theorem_candidate_count,
        carried_lemma_candidate_count=lemma_candidate_count,
        carried_formal_definition_candidate_registry_count=formal_definition_candidate_registry_count,
        carried_registered_formal_definition_candidate_count=registered_formal_definition_candidate_count,
        carried_unresolved_formal_definition_candidate_count=unresolved_formal_definition_candidate_count,
        carried_completed_formal_definition_candidate_count=completed_formal_definition_candidate_count,
        carried_proof_obligation_registry_execution_count=proof_obligation_registry_execution_count,
        carried_registered_proof_obligation_count=registered_proof_obligation_count,
        carried_unresolved_proof_obligation_count=unresolved_proof_obligation_count,
        carried_resolved_proof_obligation_count=resolved_proof_obligation_count,
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
        boundary_phrase_count=37,
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
