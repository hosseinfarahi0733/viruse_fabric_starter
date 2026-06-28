from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTERS = {
    "controlled_l_001_lemma_proof_strategy_planning_count": 1,
    "new_controlled_l_001_lemma_proof_strategy_planning_count": 1,
    "l_001_lemma_proof_strategy_planning_count": 1,
    "selected_lemma_count": 1,
    "selected_l_001_count": 1,
    "planned_l_001_proof_strategy_count": 1,
    "planned_l_001_proof_step_count": 4,

    "controlled_tc_001_proof_obligation_lemma_planning_count": 1,
    "tc_001_proof_obligation_lemma_planning_count": 1,
    "proof_obligation_lemma_planning_count": 1,
    "planned_proof_obligation_count": 6,
    "planned_lemma_count": 6,
    "tc_001_planned_lemma_count": 6,
    "accepted_lemma_plan_count": 1,

    "selected_theorem_candidate_count": 1,
    "selected_tc_001_count": 1,
    "planned_proof_strategy_count": 1,
    "tc_001_proof_strategy_planning_count": 1,

    "theorem_candidate_plan_count": 1,
    "planned_theorem_candidate_count": 4,
    "accepted_theorem_candidate_plan_count": 1,

    "dependency_closure_boundary_pass_count": 1,
    "dependency_closure_blocker_count": 0,
    "unresolved_dependency_gap_count": 0,

    "dependent_object_completion_bundle_integration_count": 1,
    "completed_dependent_object_completion_bundle_count": 1,
    "dependent_object_definition_completion_count": 6,
    "completed_dependent_object_definition_count": 6,
    "all_dependent_object_definition_completion_count": 1,

    "imported_controlled_tc_001_proof_obligation_lemma_planning_count": 1,
    "imported_tc_001_proof_obligation_lemma_planning_count": 1,
    "imported_planned_proof_obligation_count": 6,
    "imported_planned_lemma_count": 6,
    "imported_tc_001_planned_lemma_count": 6,
    "imported_accepted_lemma_plan_count": 1,
    "imported_selected_tc_001_count": 1,
    "imported_tc_001_proof_strategy_planning_count": 1,
    "imported_dependency_closure_boundary_pass_count": 1,
    "imported_dependency_closure_blocker_count": 0,
    "imported_unresolved_dependency_gap_count": 0,

    "formalization_complete_count": 0,
    "new_theorem_proven_count": 0,
    "theorem_proof_execution_count": 0,
    "tc_001_proof_execution_count": 0,
    "lemma_proof_execution_count": 0,
    "l_001_lemma_proof_execution_count": 0,
    "tc_001_lemma_proof_execution_count": 0,
    "proof_assistant_verification_count": 0,
    "external_validation_count": 0,
    "independent_experiment_count": 0,
    "manuscript_submission_ready_count": 0,
    "readiness_approval_count": 0,
    "new_citation_added_count": 0,
}


LABEL_OVERRIDES = {
    "controlled_l_001_lemma_proof_strategy_planning_count": "Controlled L-001 lemma proof strategy planning count",
    "new_controlled_l_001_lemma_proof_strategy_planning_count": "New controlled L-001 lemma proof strategy planning count",
    "l_001_lemma_proof_strategy_planning_count": "L-001 lemma proof strategy planning count",
    "selected_lemma_count": "Selected lemma count",
    "selected_l_001_count": "Selected L-001 count",
    "planned_l_001_proof_strategy_count": "Planned L-001 proof strategy count",
    "planned_l_001_proof_step_count": "Planned L-001 proof step count",

    "controlled_tc_001_proof_obligation_lemma_planning_count": "Controlled TC-001 proof obligation lemma planning count",
    "tc_001_proof_obligation_lemma_planning_count": "TC-001 proof obligation lemma planning count",
    "proof_obligation_lemma_planning_count": "Proof obligation lemma planning count",
    "planned_proof_obligation_count": "Planned proof obligation count",
    "planned_lemma_count": "Planned lemma count",
    "tc_001_planned_lemma_count": "TC-001 planned lemma count",
    "accepted_lemma_plan_count": "Accepted lemma plan count",

    "selected_theorem_candidate_count": "Selected theorem candidate count",
    "selected_tc_001_count": "Selected TC-001 count",
    "planned_proof_strategy_count": "Planned proof strategy count",
    "tc_001_proof_strategy_planning_count": "TC-001 proof strategy planning count",

    "theorem_candidate_plan_count": "Theorem candidate plan count",
    "planned_theorem_candidate_count": "Planned theorem candidate count",
    "accepted_theorem_candidate_plan_count": "Accepted theorem candidate plan count",

    "dependency_closure_boundary_pass_count": "Dependency closure boundary pass count",
    "dependency_closure_blocker_count": "Dependency closure blocker count",
    "unresolved_dependency_gap_count": "Unresolved dependency gap count",

    "dependent_object_completion_bundle_integration_count": "Dependent-object completion bundle integration count",
    "completed_dependent_object_completion_bundle_count": "Completed dependent-object completion bundle count",
    "dependent_object_definition_completion_count": "Dependent-object definition completion count",
    "completed_dependent_object_definition_count": "Completed dependent-object definition count",
    "all_dependent_object_definition_completion_count": "All dependent-object definition completion count",

    "imported_controlled_tc_001_proof_obligation_lemma_planning_count": "Imported controlled TC-001 proof obligation lemma planning count",
    "imported_tc_001_proof_obligation_lemma_planning_count": "Imported TC-001 proof obligation lemma planning count",
    "imported_planned_proof_obligation_count": "Imported planned proof obligation count",
    "imported_planned_lemma_count": "Imported planned lemma count",
    "imported_tc_001_planned_lemma_count": "Imported TC-001 planned lemma count",
    "imported_accepted_lemma_plan_count": "Imported accepted lemma plan count",
    "imported_selected_tc_001_count": "Imported selected TC-001 count",
    "imported_tc_001_proof_strategy_planning_count": "Imported TC-001 proof strategy planning count",
    "imported_dependency_closure_boundary_pass_count": "Imported dependency closure boundary pass count",
    "imported_dependency_closure_blocker_count": "Imported dependency closure blocker count",
    "imported_unresolved_dependency_gap_count": "Imported unresolved dependency gap count",

    "formalization_complete_count": "Formalization complete count",
    "new_theorem_proven_count": "New theorem proven count",
    "theorem_proof_execution_count": "Theorem proof execution count",
    "tc_001_proof_execution_count": "TC-001 proof execution count",
    "lemma_proof_execution_count": "Lemma proof execution count",
    "l_001_lemma_proof_execution_count": "L-001 lemma proof execution count",
    "tc_001_lemma_proof_execution_count": "TC-001 lemma proof execution count",
    "proof_assistant_verification_count": "Proof assistant verification count",
    "external_validation_count": "External validation count",
    "independent_experiment_count": "Independent experiment count",
    "manuscript_submission_ready_count": "Manuscript submission ready count",
    "readiness_approval_count": "Readiness approval count",
    "new_citation_added_count": "New citation added count",
}


REQUIRED_SOURCE_PHRASES = [
    "Controlled TC-001 proof obligation lemma planning count: 1",
    "New controlled TC-001 proof obligation lemma planning count: 1",
    "TC-001 proof obligation lemma planning count: 1",
    "Proof obligation lemma planning count: 1",
    "Planned proof obligation count: 6",
    "Planned lemma count: 6",
    "TC-001 planned lemma count: 6",
    "Accepted lemma plan count: 1",
    "Selected theorem candidate count: 1",
    "Selected TC-001 count: 1",
    "Planned proof strategy count: 1",
    "TC-001 proof strategy planning count: 1",
    "Formalization complete count: 0",
    "New theorem proven count: 0",
    "Theorem proof execution count: 0",
    "TC-001 proof execution count: 0",
    "Lemma proof execution count: 0",
    "TC-001 lemma proof execution count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


REQUIRED_REPORT_PHRASES = [
    "Controlled L-001 lemma proof strategy planning count: 1",
    "New controlled L-001 lemma proof strategy planning count: 1",
    "L-001 lemma proof strategy planning count: 1",
    "Selected lemma count: 1",
    "Selected L-001 count: 1",
    "Planned L-001 proof strategy count: 1",
    "Planned L-001 proof step count: 4",

    "Controlled TC-001 proof obligation lemma planning count: 1",
    "TC-001 proof obligation lemma planning count: 1",
    "Proof obligation lemma planning count: 1",
    "Planned proof obligation count: 6",
    "Planned lemma count: 6",
    "TC-001 planned lemma count: 6",
    "Accepted lemma plan count: 1",

    "Selected theorem candidate count: 1",
    "Selected TC-001 count: 1",
    "Planned proof strategy count: 1",
    "TC-001 proof strategy planning count: 1",

    "Theorem candidate plan count: 1",
    "Planned theorem candidate count: 4",
    "Accepted theorem candidate plan count: 1",

    "Dependency closure boundary pass count: 1",
    "Dependency closure blocker count: 0",
    "Unresolved dependency gap count: 0",

    "Imported controlled TC-001 proof obligation lemma planning count: 1",
    "Imported TC-001 proof obligation lemma planning count: 1",
    "Imported planned proof obligation count: 6",
    "Imported planned lemma count: 6",
    "Imported TC-001 planned lemma count: 6",
    "Imported accepted lemma plan count: 1",
    "Imported selected TC-001 count: 1",
    "Imported TC-001 proof strategy planning count: 1",

    "Formalization complete count: 0",
    "New theorem proven count: 0",
    "Theorem proof execution count: 0",
    "TC-001 proof execution count: 0",
    "Lemma proof execution count: 0",
    "L-001 lemma proof execution count: 0",
    "TC-001 lemma proof execution count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


@dataclass(frozen=True)
class L001ProofStrategyResult:
    report: str
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _label(key: str) -> str:
    if key in LABEL_OVERRIDES:
        return LABEL_OVERRIDES[key]
    return key.replace("_", " ").capitalize()


def _counter_lines() -> str:
    return "\n".join(f"- {_label(key)}: {value}" for key, value in COUNTERS.items())


def _strategy_block() -> str:
    return dedent(
        """
        ## Selected lemma

        Selected lemma: `L-001 — Sigma_A carrier availability lemma`

        Parent theorem candidate:

        `TC-001 — Admissible regular observation well-typing`

        Parent proof obligation:

        `PO-001 — Sigma_A carrier availability`

        Target lemma statement, planned only:

        If completed `Sigma_A` is available in the dependency-closed bundle, then the A-indexed carrier and transition index required by TC-001 can be referenced as well-typed formal carriers.

        This milestone plans the proof strategy only. It does not prove L-001.

        ## Controlled proof strategy for L-001

        ### Allowed dependency basis

        The strategy may use only:

        - completed `Sigma_A`;
        - accepted dependency closure boundary status;
        - v8.159 L-001 lemma plan;
        - no theorem proof execution;
        - no proof assistant verification;
        - no validation artifact;
        - no manuscript readiness artifact;
        - no citation addition.

        ### Planned proof steps

        L001-S01 — Identify completed Sigma_A record

        Purpose:
        Establish that completed `Sigma_A` is the only required formal object for L-001 carrier availability.

        Status:
        - planned only
        - not executed

        L001-S02 — Extract A-indexed state carrier

        Purpose:
        Plan the route for referencing the A-indexed state carrier from completed `Sigma_A`.

        Status:
        - planned only
        - not executed

        L001-S03 — Extract A-indexed transition index

        Purpose:
        Plan the route for referencing the A-indexed transition index from completed `Sigma_A`.

        Status:
        - planned only
        - not executed

        L001-S04 — Check no disallowed dependency enters L-001

        Purpose:
        Ensure the future L-001 proof route does not depend on `Adm_A`, `C_reg`, `Pi_obs`, `M_c`, `R_A`, `Traj_A`, TC-001 proof execution, proof assistant verification, validation, manuscript readiness, or citation additions.

        Status:
        - planned only
        - not executed

        ### Boundary

        This milestone plans a proof strategy for L-001.

        It does not prove L-001.

        It does not execute L-001 proof.

        It does not prove any lemma.

        It does not execute lemma proof.

        It does not prove TC-001.

        It does not execute TC-001 proof.

        It does not prove new theorems.

        It does not execute theorem proof.

        It does not provide proof assistant verification.

        It does not complete full formalization.

        It does not provide external validation.

        It does not provide independent experiments.

        It does not make the manuscript ready.

        It does not approve readiness.

        It does not add new citations.
        """
    ).strip()


def _next_steps() -> str:
    return "\n".join(
        [
            "1. Execute controlled L-001 lemma proof only after this strategy is official.",
            "2. Keep proof assistant verification separate from internal lemma proof execution.",
            "3. Keep validation, manuscript readiness, and citation work out of L-001 proof execution.",
        ]
    )


def build_report(source_text: str) -> L001ProofStrategyResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.160 — Controlled L-001 Lemma Proof Strategy Planning

        ## Question

        Can Viruse Fabric select L-001 from the v8.159 TC-001 lemma plan and produce a controlled proof strategy for L-001 while keeping L-001 proof execution, lemma proof execution, TC-001 proof execution, theorem proof execution, new theorem proof, proof assistant verification, validation, manuscript readiness, readiness approval, and new citations at zero?

        ## Source artifact

        - `outputs/controlled_tc_001_proof_obligation_lemma_planning_v8_159.md`

        ## Planning interpretation

        v8.160 selects L-001 and plans a controlled proof strategy for it.

        This milestone is not L-001 proof execution.

        This milestone is not lemma proof execution.

        This milestone is not TC-001 proof execution.

        This milestone is not proof assistant verification.

        {_strategy_block()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone plans the proof strategy for L-001 only.

        This milestone records selected lemma count: 1.

        This milestone records selected L-001 count: 1.

        This milestone records planned L-001 proof strategy count: 1.

        This milestone records planned L-001 proof step count: 4.

        This milestone preserves planned lemma count: 6.

        This milestone preserves TC-001 planned lemma count: 6.

        This milestone does not prove L-001.

        This milestone does not execute L-001 proof.

        This milestone does not prove any lemma.

        This milestone does not execute lemma proof.

        This milestone does not prove TC-001.

        This milestone does not execute TC-001 proof.

        This milestone does not prove new theorems.

        This milestone does not execute theorem proof.

        This milestone does not provide proof assistant verification.

        This milestone does not complete full formalization.

        This milestone does not provide external validation.

        This milestone does not provide independent experiments.

        This milestone does not make the manuscript submission ready.

        This milestone does not approve readiness.

        This milestone does not add new citations.

        ## Next steps

        {_next_steps()}

        ## Safe claim

        The project has selected L-001 and planned a controlled proof strategy with four planned proof steps while keeping L-001 proof execution, lemma proof execution, TC-001 proof execution, theorem proof execution, new theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_phrases = [
        "This milestone proves L-001",
        "This milestone executes L-001 proof",
        "This milestone proves any lemma",
        "This milestone executes lemma proof",
        "This milestone proves TC-001",
        "This milestone executes TC-001 proof",
        "This milestone proves new theorems",
        "This milestone executes theorem proof",
        "This milestone provides proof assistant verification",
        "This milestone provides external validation",
        "This milestone provides independent experiments",
        "This milestone makes the manuscript submission ready",
        "This milestone approves readiness",
        "This milestone adds new citations",
    ]

    prohibited_behavior_count = sum(
        1 for phrase in prohibited_phrases if phrase.lower() in report.lower()
    )

    boundary_keywords = [
        "does not prove",
        "does not execute l-001 proof",
        "does not execute lemma proof",
        "does not execute tc-001 proof",
        "does not execute theorem proof",
        "does not provide",
        "does not complete full formalization",
        "does not make",
        "does not approve",
        "does not add",
        "at zero",
    ]
    boundary_phrase_count = sum(report.lower().count(item.lower()) for item in boundary_keywords)

    warnings = [
        "This milestone plans L-001 proof strategy only.",
        "L-001 proof execution remains zero.",
        "Lemma proof execution remains zero.",
        "Proof assistant verification, validation, readiness approval, and citation claims remain absent.",
    ]

    return L001ProofStrategyResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> L001ProofStrategyResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
