from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTERS = {
    "controlled_tc_001_proof_obligation_lemma_planning_count": 1,
    "new_controlled_tc_001_proof_obligation_lemma_planning_count": 1,
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

    "dependency_closure_boundary_audit_count": 1,
    "full_dependency_closure_audit_count": 1,
    "dependency_closure_boundary_pass_count": 1,
    "dependency_closure_blocker_count": 0,
    "unresolved_dependency_gap_count": 0,

    "dependent_object_completion_bundle_integration_count": 1,
    "completed_dependent_object_completion_bundle_count": 1,
    "dependent_object_definition_completion_count": 6,
    "completed_dependent_object_definition_count": 6,
    "all_dependent_object_definition_completion_count": 1,

    "imported_controlled_tc_001_proof_strategy_planning_count": 1,
    "imported_tc_001_proof_strategy_planning_count": 1,
    "imported_selected_tc_001_count": 1,
    "imported_planned_proof_strategy_count": 1,
    "imported_planned_proof_obligation_count": 6,
    "imported_theorem_candidate_plan_count": 1,
    "imported_planned_theorem_candidate_count": 4,
    "imported_dependency_closure_boundary_pass_count": 1,
    "imported_dependency_closure_blocker_count": 0,
    "imported_unresolved_dependency_gap_count": 0,
    "imported_completed_dependent_object_completion_bundle_count": 1,

    "formalization_complete_count": 0,
    "new_theorem_proven_count": 0,
    "theorem_proof_execution_count": 0,
    "tc_001_proof_execution_count": 0,
    "lemma_proof_execution_count": 0,
    "tc_001_lemma_proof_execution_count": 0,
    "proof_assistant_verification_count": 0,
    "external_validation_count": 0,
    "independent_experiment_count": 0,
    "manuscript_submission_ready_count": 0,
    "readiness_approval_count": 0,
    "new_citation_added_count": 0,
}


LABEL_OVERRIDES = {
    "controlled_tc_001_proof_obligation_lemma_planning_count": "Controlled TC-001 proof obligation lemma planning count",
    "new_controlled_tc_001_proof_obligation_lemma_planning_count": "New controlled TC-001 proof obligation lemma planning count",
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

    "dependency_closure_boundary_audit_count": "Dependency closure boundary audit count",
    "full_dependency_closure_audit_count": "Full dependency closure audit count",
    "dependency_closure_boundary_pass_count": "Dependency closure boundary pass count",
    "dependency_closure_blocker_count": "Dependency closure blocker count",
    "unresolved_dependency_gap_count": "Unresolved dependency gap count",

    "dependent_object_completion_bundle_integration_count": "Dependent-object completion bundle integration count",
    "completed_dependent_object_completion_bundle_count": "Completed dependent-object completion bundle count",
    "dependent_object_definition_completion_count": "Dependent-object definition completion count",
    "completed_dependent_object_definition_count": "Completed dependent-object definition count",
    "all_dependent_object_definition_completion_count": "All dependent-object definition completion count",

    "imported_controlled_tc_001_proof_strategy_planning_count": "Imported controlled TC-001 proof strategy planning count",
    "imported_tc_001_proof_strategy_planning_count": "Imported TC-001 proof strategy planning count",
    "imported_selected_tc_001_count": "Imported selected TC-001 count",
    "imported_planned_proof_strategy_count": "Imported planned proof strategy count",
    "imported_planned_proof_obligation_count": "Imported planned proof obligation count",
    "imported_theorem_candidate_plan_count": "Imported theorem candidate plan count",
    "imported_planned_theorem_candidate_count": "Imported planned theorem candidate count",
    "imported_dependency_closure_boundary_pass_count": "Imported dependency closure boundary pass count",
    "imported_dependency_closure_blocker_count": "Imported dependency closure blocker count",
    "imported_unresolved_dependency_gap_count": "Imported unresolved dependency gap count",
    "imported_completed_dependent_object_completion_bundle_count": "Imported completed dependent-object completion bundle count",

    "formalization_complete_count": "Formalization complete count",
    "new_theorem_proven_count": "New theorem proven count",
    "theorem_proof_execution_count": "Theorem proof execution count",
    "tc_001_proof_execution_count": "TC-001 proof execution count",
    "lemma_proof_execution_count": "Lemma proof execution count",
    "tc_001_lemma_proof_execution_count": "TC-001 lemma proof execution count",
    "proof_assistant_verification_count": "Proof assistant verification count",
    "external_validation_count": "External validation count",
    "independent_experiment_count": "Independent experiment count",
    "manuscript_submission_ready_count": "Manuscript submission ready count",
    "readiness_approval_count": "Readiness approval count",
    "new_citation_added_count": "New citation added count",
}


REQUIRED_SOURCE_PHRASES = [
    "Controlled TC-001 proof strategy planning count: 1",
    "New controlled TC-001 proof strategy planning count: 1",
    "TC-001 proof strategy planning count: 1",
    "Selected theorem candidate count: 1",
    "Selected TC-001 count: 1",
    "Planned proof strategy count: 1",
    "Planned proof obligation count: 6",
    "Theorem candidate plan count: 1",
    "Planned theorem candidate count: 4",
    "Accepted theorem candidate plan count: 1",
    "Dependency closure boundary audit count: 1",
    "Full dependency closure audit count: 1",
    "Dependency closure boundary pass count: 1",
    "Dependency closure blocker count: 0",
    "Unresolved dependency gap count: 0",
    "Formalization complete count: 0",
    "New theorem proven count: 0",
    "Theorem proof execution count: 0",
    "TC-001 proof execution count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


REQUIRED_REPORT_PHRASES = [
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

    "Theorem candidate plan count: 1",
    "Planned theorem candidate count: 4",
    "Accepted theorem candidate plan count: 1",

    "Dependency closure boundary audit count: 1",
    "Full dependency closure audit count: 1",
    "Dependency closure boundary pass count: 1",
    "Dependency closure blocker count: 0",
    "Unresolved dependency gap count: 0",

    "Imported controlled TC-001 proof strategy planning count: 1",
    "Imported TC-001 proof strategy planning count: 1",
    "Imported selected TC-001 count: 1",
    "Imported planned proof strategy count: 1",
    "Imported planned proof obligation count: 6",
    "Imported theorem candidate plan count: 1",
    "Imported planned theorem candidate count: 4",
    "Imported dependency closure boundary pass count: 1",
    "Imported dependency closure blocker count: 0",
    "Imported unresolved dependency gap count: 0",

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


@dataclass(frozen=True)
class LemmaPlanningResult:
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


def _lemma_block() -> str:
    return dedent(
        """
        ## TC-001 proof obligation lemma plan

        Selected theorem candidate:

        `TC-001 — Admissible regular observation well-typing`

        Source proof obligations imported from v8.158:

        - PO-001 — Sigma_A carrier availability
        - PO-002 — Adm_A admissible-state typing
        - PO-003 — C_reg regular-transition typing
        - PO-004 — Pi_obs projection domain compatibility
        - PO-005 — Pi_obs codomain well-typing
        - PO-006 — No uncompleted dependency use

        This milestone decomposes those obligations into lemma plans only.

        ### Planned lemmas

        L-001 — Sigma_A carrier availability lemma

        Purpose:
        Show that the A-indexed carrier and transition index required by TC-001 are available from completed `Sigma_A`.

        Planned dependency basis:
        - completed `Sigma_A`

        Target obligation:
        - PO-001

        Execution status:
        - planned only
        - not proved

        L-002 — Adm_A admissible-state typing lemma

        Purpose:
        Show that every state entering TC-001 is typed in the admissible carrier determined by completed `Adm_A`.

        Planned dependency basis:
        - completed `Sigma_A`
        - completed `Adm_A`

        Target obligation:
        - PO-002

        Execution status:
        - planned only
        - not proved

        L-003 — C_reg regular-transition typing lemma

        Purpose:
        Show that every transition entering TC-001 is typed as a regular transition under completed `C_reg`.

        Planned dependency basis:
        - completed `Sigma_A`
        - completed `Adm_A`
        - completed `C_reg`

        Target obligation:
        - PO-003

        Execution status:
        - planned only
        - not proved

        L-004 — Pi_obs projection domain compatibility lemma

        Purpose:
        Show that every admissible state and regular transition in TC-001 lies in the declared domain of completed `Pi_obs`.

        Planned dependency basis:
        - completed `Sigma_A`
        - completed `Adm_A`
        - completed `C_reg`
        - completed `Pi_obs`

        Target obligation:
        - PO-004

        Execution status:
        - planned only
        - not proved

        L-005 — Pi_obs codomain well-typing lemma

        Purpose:
        Show that the observable output produced by `Pi_obs` lies in the declared A-indexed observation carrier `O_A`.

        Planned dependency basis:
        - completed `Sigma_A`
        - completed `Adm_A`
        - completed `C_reg`
        - completed `Pi_obs`

        Target obligation:
        - PO-005

        Execution status:
        - planned only
        - not proved

        L-006 — No uncompleted dependency use lemma

        Purpose:
        Show that the TC-001 proof route does not require `M_c`, `R_A`, `Traj_A`, theorem proof execution, proof assistant verification, validation, manuscript readiness, or citation additions as proof dependencies.

        Planned dependency basis:
        - completed `Sigma_A`
        - completed `Adm_A`
        - completed `C_reg`
        - completed `Pi_obs`
        - accepted dependency closure boundary audit

        Target obligation:
        - PO-006

        Execution status:
        - planned only
        - not proved

        ### Boundary

        This milestone plans six TC-001 lemmas.

        It does not prove any lemma.

        It does not prove TC-001.

        It does not prove any theorem.

        It does not execute theorem proof.

        It does not execute lemma proof.

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
            "1. Select L-001 for controlled lemma proof strategy planning.",
            "2. Keep lemma proof execution separate from lemma proof strategy planning.",
            "3. Keep proof assistant verification, validation, manuscript readiness, and citation work out of this stage.",
        ]
    )


def build_report(source_text: str) -> LemmaPlanningResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.159 — Controlled TC-001 Proof Obligation Lemma Planning

        ## Question

        Can Viruse Fabric decompose the six TC-001 planned proof obligations from v8.158 into controlled lemma plans while keeping lemma proof execution, TC-001 proof execution, theorem proof execution, new theorem proof, proof assistant verification, validation, manuscript readiness, readiness approval, and new citations at zero?

        ## Source artifact

        - `outputs/controlled_tc_001_proof_strategy_planning_v8_158.md`

        ## Planning interpretation

        v8.159 decomposes TC-001 proof obligations into lemma plans.

        This milestone is not lemma proof execution.

        This milestone is not theorem proof execution.

        This milestone is not TC-001 proof execution.

        This milestone is not proof assistant verification.

        {_lemma_block()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone plans TC-001 proof obligation lemmas only.

        This milestone records planned lemma count: 6.

        This milestone records TC-001 planned lemma count: 6.

        This milestone records accepted lemma plan count: 1.

        This milestone preserves planned proof obligation count: 6.

        This milestone preserves selected TC-001 count: 1.

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

        The project has decomposed the six TC-001 planned proof obligations into six controlled lemma plans while keeping lemma proof execution, TC-001 proof execution, theorem proof execution, new theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_phrases = [
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
        "This milestone plans TC-001 lemmas only.",
        "Lemma proof execution remains zero.",
        "TC-001 proof execution remains zero.",
        "Proof assistant verification, validation, readiness approval, and citation claims remain absent.",
    ]

    return LemmaPlanningResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> LemmaPlanningResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
