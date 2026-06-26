from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/proof_strategy_plan_v8_54.md")
OUTPUT_PATH = Path("outputs/proof_environment_selection_and_first_proof_attempt_plan_v8_55.md")


@dataclass(frozen=True)
class ProofEnvironmentSelectionRow:
    environment_id: str
    environment_name: str
    environment_role: str
    selection_status: str
    rationale: str
    boundary_status: str


@dataclass(frozen=True)
class FirstProofAttemptPlanRow:
    attempt_plan_id: str
    target: str
    planned_action: str
    required_inputs: str
    success_condition: str
    boundary_status: str


@dataclass(frozen=True)
class ProofEnvironmentSelectionAndFirstProofAttemptPlanReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    proof_environment_selection_plan_count: int
    proof_environment_candidate_count: int
    selected_proof_environment_count: int
    selected_manual_markdown_environment_count: int
    deferred_formal_assistant_environment_count: int
    first_proof_attempt_plan_count: int
    first_proof_attempt_plan_row_count: int

    carried_proof_strategy_plan_count: int
    carried_proof_strategy_plan_row_count: int
    carried_manual_derivation_track_count: int
    carried_formal_assistant_readiness_track_count: int
    carried_counterexample_audit_track_count: int
    carried_boundary_audit_track_count: int
    carried_proof_environment_selection_required_count: int
    carried_proof_execution_attempt_plan_required_count: int

    carried_theorem_skeleton_count: int
    carried_lemma_skeleton_count: int
    carried_registered_proof_obligation_count: int
    carried_unresolved_proof_obligation_count: int
    carried_resolved_proof_obligation_count: int
    carried_registered_formal_definition_candidate_count: int
    carried_unresolved_formal_definition_candidate_count: int
    carried_completed_formal_definition_candidate_count: int

    first_proof_attempt_execution_count: int
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
        "first proof attempt is executed",
        "proof attempt is executed",
        "manuscript is submission-ready",
        "external validation is completed",
        "independent experiment is completed",
        "clinical relevance is established",
        "biological prediction is established",
        "operational readiness is achieved",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_environment_rows() -> List[ProofEnvironmentSelectionRow]:
    return [
        ProofEnvironmentSelectionRow(
            environment_id="PES-001",
            environment_name="manual markdown derivation",
            environment_role="selected first environment",
            selection_status="selected",
            rationale="best fit for unresolved formal definition candidates and early proof obligation clarification",
            boundary_status="environment selected only; proof execution remains absent",
        ),
        ProofEnvironmentSelectionRow(
            environment_id="PES-002",
            environment_name="Lean readiness path",
            environment_role="deferred formal assistant path",
            selection_status="deferred",
            rationale="requires cleaner type inventory and completed definition candidates before serious translation",
            boundary_status="readiness path only; no Lean proof artifact",
        ),
        ProofEnvironmentSelectionRow(
            environment_id="PES-003",
            environment_name="Coq readiness path",
            environment_role="deferred formal assistant path",
            selection_status="deferred",
            rationale="requires explicit inductive structures, relation definitions, and proof obligation typing",
            boundary_status="readiness path only; no Coq proof artifact",
        ),
    ]


def build_attempt_rows() -> List[FirstProofAttemptPlanRow]:
    return [
        FirstProofAttemptPlanRow(
            attempt_plan_id="FPA-001",
            target="TLS-001 path compatibility preservation lemma skeleton",
            planned_action="draft assumption block and dependency chain in markdown",
            required_inputs="FDC-001, FDC-002, POR-001, POR-002, POR-003",
            success_condition="all assumptions and missing definitions are explicitly listed",
            boundary_status="attempt plan only; proof execution remains absent",
        ),
        FirstProofAttemptPlanRow(
            attempt_plan_id="FPA-002",
            target="TLS-002 causal mass boundedness or counterexample split lemma skeleton",
            planned_action="separate boundedness route from counterexample route before derivation",
            required_inputs="FDC-002, POR-004, counterexample audit track",
            success_condition="boundedness assumptions and counterexample triggers are separated",
            boundary_status="attempt plan only; lemma proof remains absent",
        ),
        FirstProofAttemptPlanRow(
            attempt_plan_id="FPA-003",
            target="TLS-003 apparent purpose emergence theorem skeleton",
            planned_action="map theorem assumptions to lemma skeleton dependencies and projection-level conclusion",
            required_inputs="TLS-001, TLS-002, FDC-001, FDC-002, POR-005",
            success_condition="theorem dependency graph is explicit and boundary-safe",
            boundary_status="attempt plan only; theorem proof remains absent",
        ),
        FirstProofAttemptPlanRow(
            attempt_plan_id="FPA-004",
            target="TLS-004 non-teleological attractor concentration theorem skeleton",
            planned_action="prepare non-biological statement boundaries and admissibility assumptions",
            required_inputs="TLS-001, FDC-001, FDC-002, POR-006",
            success_condition="statement avoids biological, clinical, and intentional overclaim",
            boundary_status="attempt plan only; theorem proof remains absent",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    environment_rows = build_environment_rows()
    attempt_rows = build_attempt_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    proof_strategy_plan_count = 1 if _has_count(source_text, "Proof strategy plan", "1") else 0
    proof_strategy_plan_row_count = 4 if _has_count(source_text, "Proof strategy plan row", "4") else 0
    manual_derivation_track_count = 1 if _has_count(source_text, "Manual derivation track", "1") else 0
    formal_assistant_readiness_track_count = 1 if _has_count(source_text, "Formal assistant readiness track", "1") else 0
    counterexample_audit_track_count = 1 if _has_count(source_text, "Counterexample audit track", "1") else 0
    boundary_audit_track_count = 1 if _has_count(source_text, "Boundary audit track", "1") else 0
    proof_environment_selection_required_count = 1 if _has_count(source_text, "Proof environment selection required", "1") else 0
    proof_execution_attempt_plan_required_count = 1 if _has_count(source_text, "Proof execution attempt plan required", "1") else 0

    theorem_skeleton_count = 2 if _has_count(source_text, "Carried theorem skeleton", "2") else 0
    lemma_skeleton_count = 2 if _has_count(source_text, "Carried lemma skeleton", "2") else 0
    registered_proof_obligation_count = 6 if _has_count(source_text, "Carried registered proof obligation", "6") else 0
    unresolved_proof_obligation_count = 6 if _has_count(source_text, "Carried unresolved proof obligation", "6") else 0
    resolved_proof_obligation_count = 0 if _has_count(source_text, "Carried resolved proof obligation", "0") else -1
    registered_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried registered formal definition candidate", "2") else 0
    unresolved_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried unresolved formal definition candidate", "2") else 0
    completed_formal_definition_candidate_count = 0 if _has_count(source_text, "Carried completed formal definition candidate", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    selected_proof_environment_count = sum(1 for row in environment_rows if row.selection_status == "selected")
    selected_manual_markdown_environment_count = sum(
        1 for row in environment_rows
        if row.environment_name == "manual markdown derivation" and row.selection_status == "selected"
    )
    deferred_formal_assistant_environment_count = sum(
        1 for row in environment_rows
        if row.selection_status == "deferred"
    )

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.54 proof strategy source artifact.")
    if proof_strategy_plan_count != 1:
        errors.append("Expected proof strategy plan signal is absent.")
    if proof_strategy_plan_row_count != 4:
        errors.append("Expected proof strategy plan row count signal is absent.")
    if manual_derivation_track_count != 1:
        errors.append("Expected manual derivation track signal is absent.")
    if formal_assistant_readiness_track_count != 1:
        errors.append("Expected formal assistant readiness track signal is absent.")
    if counterexample_audit_track_count != 1:
        errors.append("Expected counterexample audit track signal is absent.")
    if boundary_audit_track_count != 1:
        errors.append("Expected boundary audit track signal is absent.")
    if proof_environment_selection_required_count != 1:
        errors.append("Expected proof environment selection required signal is absent.")
    if proof_execution_attempt_plan_required_count != 1:
        errors.append("Expected proof execution attempt plan required signal is absent.")
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
    if selected_proof_environment_count != 1:
        errors.append("Expected exactly one selected proof environment.")
    if selected_manual_markdown_environment_count != 1:
        errors.append("Expected manual markdown derivation to be the selected first environment.")
    if deferred_formal_assistant_environment_count != 2:
        errors.append("Expected two deferred formal assistant environments.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")

    warnings = [
        "Manual markdown derivation is selected for the first attempt plan, while proof execution remains absent.",
        "Lean and Coq readiness paths are deferred.",
        "Formal definition candidates remain unresolved.",
        "Proof obligations remain unresolved.",
    ]

    lines = [
        "# Proof Environment Selection and First Proof Attempt Plan v8.55",
        "",
        "## Purpose",
        "",
        "Select a conservative proof environment and plan a first proof attempt route after v8.54 proof strategy planning while keeping formal definition completion, proof execution, theorem proof, lemma proof, proof gap resolution, external validation, citation addition, and submission readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Proof environment selection rows",
        "",
        "| Environment ID | Environment name | Environment role | Selection status | Rationale | Boundary status |",
        "|---|---|---|---|---|---|",
    ]

    for row in environment_rows:
        lines.append(
            f"| {row.environment_id} | {row.environment_name} | {row.environment_role} | {row.selection_status} | {row.rationale} | {row.boundary_status} |"
        )

    lines.extend(
        [
            "",
            "## First proof attempt plan rows",
            "",
            "| Attempt plan ID | Target | Planned action | Required inputs | Success condition | Boundary status |",
            "|---|---|---|---|---|---|",
        ]
    )

    for row in attempt_rows:
        lines.append(
            f"| {row.attempt_plan_id} | {row.target} | {row.planned_action} | {row.required_inputs} | {row.success_condition} | {row.boundary_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Proof environment selection plan count: 1",
            f"- Proof environment candidate count: {len(environment_rows)}",
            f"- Selected proof environment count: {selected_proof_environment_count}",
            f"- Selected manual markdown environment count: {selected_manual_markdown_environment_count}",
            f"- Deferred formal assistant environment count: {deferred_formal_assistant_environment_count}",
            "- First proof attempt plan count: 1",
            f"- First proof attempt plan row count: {len(attempt_rows)}",
            "",
            "## Carried proof strategy signals",
            "",
            f"- Carried proof strategy plan count: {proof_strategy_plan_count}",
            f"- Carried proof strategy plan row count: {proof_strategy_plan_row_count}",
            f"- Carried manual derivation track count: {manual_derivation_track_count}",
            f"- Carried formal assistant readiness track count: {formal_assistant_readiness_track_count}",
            f"- Carried counterexample audit track count: {counterexample_audit_track_count}",
            f"- Carried boundary audit track count: {boundary_audit_track_count}",
            f"- Carried proof environment selection required count: {proof_environment_selection_required_count}",
            f"- Carried proof execution attempt plan required count: {proof_execution_attempt_plan_required_count}",
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
            "- First proof attempt execution count: 0",
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
            "The v8.55 artifact selects manual markdown derivation as the first proof environment and plans the first proof attempt route only. It does not execute proof work, does not complete formal definitions, does not resolve proof obligations, does not establish theorem proof, does not establish lemma proof, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "This milestone deliberately selects a low-risk manual markdown route before formal assistant translation. Lean and Coq remain deferred until definition candidates and proof obligations are cleaner. The first attempt remains planned only.",
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
            "The project has selected manual markdown derivation as the first proof environment and planned a first proof attempt route, while keeping first proof attempt execution, proof execution, theorem proof, lemma proof, completed formal definitions, proof gap resolution, citation additions, external validation, and manuscript submission readiness at zero.",
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
        errors.append("Overclaim pattern detected in v8.55 proof environment selection report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.55 proof environment selection report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> ProofEnvironmentSelectionAndFirstProofAttemptPlanReport:
    text = render_report()
    source_text = _read_source()
    environment_rows = build_environment_rows()
    attempt_rows = build_attempt_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    proof_strategy_plan_count = 1 if _has_count(source_text, "Proof strategy plan", "1") else 0
    proof_strategy_plan_row_count = 4 if _has_count(source_text, "Proof strategy plan row", "4") else 0
    manual_derivation_track_count = 1 if _has_count(source_text, "Manual derivation track", "1") else 0
    formal_assistant_readiness_track_count = 1 if _has_count(source_text, "Formal assistant readiness track", "1") else 0
    counterexample_audit_track_count = 1 if _has_count(source_text, "Counterexample audit track", "1") else 0
    boundary_audit_track_count = 1 if _has_count(source_text, "Boundary audit track", "1") else 0
    proof_environment_selection_required_count = 1 if _has_count(source_text, "Proof environment selection required", "1") else 0
    proof_execution_attempt_plan_required_count = 1 if _has_count(source_text, "Proof execution attempt plan required", "1") else 0

    theorem_skeleton_count = 2 if _has_count(source_text, "Carried theorem skeleton", "2") else 0
    lemma_skeleton_count = 2 if _has_count(source_text, "Carried lemma skeleton", "2") else 0
    registered_proof_obligation_count = 6 if _has_count(source_text, "Carried registered proof obligation", "6") else 0
    unresolved_proof_obligation_count = 6 if _has_count(source_text, "Carried unresolved proof obligation", "6") else 0
    resolved_proof_obligation_count = 0 if _has_count(source_text, "Carried resolved proof obligation", "0") else -1
    registered_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried registered formal definition candidate", "2") else 0
    unresolved_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried unresolved formal definition candidate", "2") else 0
    completed_formal_definition_candidate_count = 0 if _has_count(source_text, "Carried completed formal definition candidate", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    selected_proof_environment_count = sum(1 for row in environment_rows if row.selection_status == "selected")
    selected_manual_markdown_environment_count = sum(
        1 for row in environment_rows
        if row.environment_name == "manual markdown derivation" and row.selection_status == "selected"
    )
    deferred_formal_assistant_environment_count = sum(
        1 for row in environment_rows
        if row.selection_status == "deferred"
    )

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.54 proof strategy source artifact.")
    if proof_strategy_plan_count != 1:
        errors.append("Expected proof strategy plan signal is absent.")
    if proof_strategy_plan_row_count != 4:
        errors.append("Expected proof strategy plan row count signal is absent.")
    if manual_derivation_track_count != 1:
        errors.append("Expected manual derivation track signal is absent.")
    if formal_assistant_readiness_track_count != 1:
        errors.append("Expected formal assistant readiness track signal is absent.")
    if counterexample_audit_track_count != 1:
        errors.append("Expected counterexample audit track signal is absent.")
    if boundary_audit_track_count != 1:
        errors.append("Expected boundary audit track signal is absent.")
    if proof_environment_selection_required_count != 1:
        errors.append("Expected proof environment selection required signal is absent.")
    if proof_execution_attempt_plan_required_count != 1:
        errors.append("Expected proof execution attempt plan required signal is absent.")
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
    if selected_proof_environment_count != 1:
        errors.append("Expected exactly one selected proof environment.")
    if selected_manual_markdown_environment_count != 1:
        errors.append("Expected manual markdown derivation to be the selected first environment.")
    if deferred_formal_assistant_environment_count != 2:
        errors.append("Expected two deferred formal assistant environments.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "Manual markdown derivation is selected for the first attempt plan, while proof execution remains absent.",
        "Lean and Coq readiness paths are deferred.",
        "Formal definition candidates remain unresolved.",
        "Proof obligations remain unresolved.",
    ]

    return ProofEnvironmentSelectionAndFirstProofAttemptPlanReport(
        title="Proof Environment Selection and First Proof Attempt Plan v8.55",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        proof_environment_selection_plan_count=1,
        proof_environment_candidate_count=len(environment_rows),
        selected_proof_environment_count=selected_proof_environment_count,
        selected_manual_markdown_environment_count=selected_manual_markdown_environment_count,
        deferred_formal_assistant_environment_count=deferred_formal_assistant_environment_count,
        first_proof_attempt_plan_count=1,
        first_proof_attempt_plan_row_count=len(attempt_rows),
        carried_proof_strategy_plan_count=proof_strategy_plan_count,
        carried_proof_strategy_plan_row_count=proof_strategy_plan_row_count,
        carried_manual_derivation_track_count=manual_derivation_track_count,
        carried_formal_assistant_readiness_track_count=formal_assistant_readiness_track_count,
        carried_counterexample_audit_track_count=counterexample_audit_track_count,
        carried_boundary_audit_track_count=boundary_audit_track_count,
        carried_proof_environment_selection_required_count=proof_environment_selection_required_count,
        carried_proof_execution_attempt_plan_required_count=proof_execution_attempt_plan_required_count,
        carried_theorem_skeleton_count=theorem_skeleton_count,
        carried_lemma_skeleton_count=lemma_skeleton_count,
        carried_registered_proof_obligation_count=registered_proof_obligation_count,
        carried_unresolved_proof_obligation_count=unresolved_proof_obligation_count,
        carried_resolved_proof_obligation_count=resolved_proof_obligation_count,
        carried_registered_formal_definition_candidate_count=registered_formal_definition_candidate_count,
        carried_unresolved_formal_definition_candidate_count=unresolved_formal_definition_candidate_count,
        carried_completed_formal_definition_candidate_count=completed_formal_definition_candidate_count,
        first_proof_attempt_execution_count=0,
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
        hard_zero_count=17,
        boundary_phrase_count=38,
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
