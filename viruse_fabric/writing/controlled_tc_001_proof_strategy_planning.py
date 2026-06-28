from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTERS = {
    "controlled_tc_001_proof_strategy_planning_count": 1,
    "new_controlled_tc_001_proof_strategy_planning_count": 1,
    "tc_001_proof_strategy_planning_count": 1,
    "selected_theorem_candidate_count": 1,
    "selected_tc_001_count": 1,
    "planned_proof_strategy_count": 1,
    "planned_proof_obligation_count": 6,

    "theorem_candidate_plan_count": 1,
    "planned_theorem_candidate_count": 4,
    "accepted_theorem_candidate_plan_count": 1,

    "dependency_closure_boundary_audit_count": 1,
    "full_dependency_closure_audit_count": 1,
    "dependency_closure_boundary_pass_count": 1,
    "dependency_closure_blocker_count": 0,
    "unresolved_dependency_gap_count": 0,

    "dependent_object_completion_bundle_integration_count": 1,
    "integrated_dependent_object_completion_bundle_count": 1,
    "completed_dependent_object_completion_bundle_count": 1,

    "dependent_object_definition_completion_count": 6,
    "completed_dependent_object_definition_count": 6,
    "all_dependent_object_definition_completion_count": 1,

    "imported_controlled_theorem_candidate_planning_count": 1,
    "imported_theorem_candidate_plan_count": 1,
    "imported_planned_theorem_candidate_count": 4,
    "imported_accepted_theorem_candidate_plan_count": 1,
    "imported_dependency_closure_boundary_pass_count": 1,
    "imported_dependency_closure_blocker_count": 0,
    "imported_unresolved_dependency_gap_count": 0,
    "imported_dependent_object_completion_bundle_integration_count": 1,
    "imported_completed_dependent_object_completion_bundle_count": 1,
    "imported_completed_sigma_a_definition_count": 1,
    "imported_completed_formal_definition_count": 1,

    "formalization_complete_count": 0,
    "new_theorem_proven_count": 0,
    "theorem_proof_execution_count": 0,
    "tc_001_proof_execution_count": 0,
    "proof_assistant_verification_count": 0,
    "external_validation_count": 0,
    "independent_experiment_count": 0,
    "manuscript_submission_ready_count": 0,
    "readiness_approval_count": 0,
    "new_citation_added_count": 0,
}


LABEL_OVERRIDES = {
    "controlled_tc_001_proof_strategy_planning_count": "Controlled TC-001 proof strategy planning count",
    "new_controlled_tc_001_proof_strategy_planning_count": "New controlled TC-001 proof strategy planning count",
    "tc_001_proof_strategy_planning_count": "TC-001 proof strategy planning count",
    "selected_theorem_candidate_count": "Selected theorem candidate count",
    "selected_tc_001_count": "Selected TC-001 count",
    "planned_proof_strategy_count": "Planned proof strategy count",
    "planned_proof_obligation_count": "Planned proof obligation count",

    "theorem_candidate_plan_count": "Theorem candidate plan count",
    "planned_theorem_candidate_count": "Planned theorem candidate count",
    "accepted_theorem_candidate_plan_count": "Accepted theorem candidate plan count",

    "dependency_closure_boundary_audit_count": "Dependency closure boundary audit count",
    "full_dependency_closure_audit_count": "Full dependency closure audit count",
    "dependency_closure_boundary_pass_count": "Dependency closure boundary pass count",
    "dependency_closure_blocker_count": "Dependency closure blocker count",
    "unresolved_dependency_gap_count": "Unresolved dependency gap count",

    "dependent_object_completion_bundle_integration_count": "Dependent-object completion bundle integration count",
    "integrated_dependent_object_completion_bundle_count": "Integrated dependent-object completion bundle count",
    "completed_dependent_object_completion_bundle_count": "Completed dependent-object completion bundle count",

    "dependent_object_definition_completion_count": "Dependent-object definition completion count",
    "completed_dependent_object_definition_count": "Completed dependent-object definition count",
    "all_dependent_object_definition_completion_count": "All dependent-object definition completion count",

    "imported_controlled_theorem_candidate_planning_count": "Imported controlled theorem candidate planning count",
    "imported_theorem_candidate_plan_count": "Imported theorem candidate plan count",
    "imported_planned_theorem_candidate_count": "Imported planned theorem candidate count",
    "imported_accepted_theorem_candidate_plan_count": "Imported accepted theorem candidate plan count",
    "imported_dependency_closure_boundary_pass_count": "Imported dependency closure boundary pass count",
    "imported_dependency_closure_blocker_count": "Imported dependency closure blocker count",
    "imported_unresolved_dependency_gap_count": "Imported unresolved dependency gap count",
    "imported_dependent_object_completion_bundle_integration_count": "Imported dependent-object completion bundle integration count",
    "imported_completed_dependent_object_completion_bundle_count": "Imported completed dependent-object completion bundle count",
    "imported_completed_sigma_a_definition_count": "Imported completed Sigma_A definition count",
    "imported_completed_formal_definition_count": "Imported completed formal definition count",

    "formalization_complete_count": "Formalization complete count",
    "new_theorem_proven_count": "New theorem proven count",
    "theorem_proof_execution_count": "Theorem proof execution count",
    "tc_001_proof_execution_count": "TC-001 proof execution count",
    "proof_assistant_verification_count": "Proof assistant verification count",
    "external_validation_count": "External validation count",
    "independent_experiment_count": "Independent experiment count",
    "manuscript_submission_ready_count": "Manuscript submission ready count",
    "readiness_approval_count": "Readiness approval count",
    "new_citation_added_count": "New citation added count",
}


REQUIRED_SOURCE_PHRASES = [
    "Controlled theorem candidate planning count: 1",
    "New controlled theorem candidate planning count: 1",
    "Theorem candidate plan count: 1",
    "Theorem candidate planning over dependency-closed bundle count: 1",
    "Planned theorem candidate count: 4",
    "Accepted theorem candidate plan count: 1",
    "Dependency closure boundary audit count: 1",
    "Full dependency closure audit count: 1",
    "Dependency closure boundary pass count: 1",
    "Dependency closure blocker count: 0",
    "Unresolved dependency gap count: 0",
    "Dependent-object completion bundle integration count: 1",
    "Integrated dependent-object completion bundle count: 1",
    "Completed dependent-object completion bundle count: 1",
    "Dependent-object definition completion count: 6",
    "Completed dependent-object definition count: 6",
    "All dependent-object definition completion count: 1",
    "Formalization complete count: 0",
    "New theorem proven count: 0",
    "Theorem proof execution count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


REQUIRED_REPORT_PHRASES = [
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

    "Dependent-object completion bundle integration count: 1",
    "Integrated dependent-object completion bundle count: 1",
    "Completed dependent-object completion bundle count: 1",

    "Dependent-object definition completion count: 6",
    "Completed dependent-object definition count: 6",
    "All dependent-object definition completion count: 1",

    "Imported controlled theorem candidate planning count: 1",
    "Imported theorem candidate plan count: 1",
    "Imported planned theorem candidate count: 4",
    "Imported accepted theorem candidate plan count: 1",
    "Imported dependency closure boundary pass count: 1",
    "Imported dependency closure blocker count: 0",
    "Imported unresolved dependency gap count: 0",
    "Imported dependent-object completion bundle integration count: 1",
    "Imported completed dependent-object completion bundle count: 1",
    "Imported completed Sigma_A definition count: 1",
    "Imported completed formal definition count: 1",

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


@dataclass(frozen=True)
class ProofStrategyResult:
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
        ## Selected theorem candidate

        Selected candidate: `TC-001 — Admissible regular observation well-typing`

        Informal target statement:

        If `Sigma_A`, `Adm_A`, `C_reg`, and `Pi_obs` are completed and the dependency-closed bundle is accepted, then every admissible state and regular transition admitted by `C_reg` has a well-typed observable representation under `Pi_obs`.

        This milestone plans the proof strategy only. It does not prove TC-001.

        ## Controlled proof strategy for TC-001

        ### Proof basis

        The strategy may use only the following already-recorded objects and milestones:

        - completed `Sigma_A`;
        - completed `Adm_A`;
        - completed `C_reg`;
        - completed `Pi_obs`;
        - integrated dependent-object completion bundle;
        - accepted dependency closure boundary audit;
        - theorem candidate plan from v8.157.

        ### Planned proof obligations

        PO-001 — Sigma_A carrier availability

        Show that the relevant A-indexed carrier and transition index are available from completed `Sigma_A`.

        PO-002 — Adm_A admissible-state typing

        Show that every state entering TC-001 is typed in the admissible carrier determined by completed `Adm_A`.

        PO-003 — C_reg regular-transition typing

        Show that every transition entering TC-001 is typed as a regular transition under completed `C_reg`.

        PO-004 — Pi_obs projection domain compatibility

        Show that every admissible state and regular transition in TC-001 lies in the declared domain of completed `Pi_obs`.

        PO-005 — Pi_obs codomain well-typing

        Show that the observable output produced by `Pi_obs` lies in the declared A-indexed observation carrier `O_A`.

        PO-006 — No uncompleted dependency use

        Show that TC-001 proof strategy does not use `M_c`, `R_A`, `Traj_A`, theorem proof execution, proof assistant verification, validation, manuscript readiness, or citation additions as proof dependencies.

        ### Strategy order

        1. Establish `Sigma_A` carrier availability.
        2. Establish admissible-state typing via `Adm_A`.
        3. Establish regular-transition typing via `C_reg`.
        4. Establish projection domain compatibility via `Pi_obs`.
        5. Establish observable codomain well-typing.
        6. Check no uncompleted or disallowed dependency enters the proof route.

        ### Boundary

        This milestone plans a proof strategy for TC-001.

        It does not prove TC-001.

        It does not prove any theorem.

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
            "1. Decompose TC-001 proof obligations into controlled lemma plans.",
            "2. Keep proof execution separate from proof obligation decomposition.",
            "3. Keep proof assistant verification, validation, manuscript readiness, and citation work out of this stage.",
        ]
    )


def build_report(source_text: str) -> ProofStrategyResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.158 — Controlled TC-001 Proof Strategy Planning

        ## Question

        Can Viruse Fabric select TC-001 from the v8.157 theorem candidate plan and produce a controlled proof strategy for TC-001 while keeping theorem proof execution, new theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero?

        ## Source artifact

        - `outputs/controlled_theorem_candidate_planning_over_dependency_closed_bundle_v8_157.md`

        ## Planning interpretation

        v8.158 selects TC-001 and plans a controlled proof strategy for it.

        This milestone is not theorem proof execution.

        This milestone is not proof assistant verification.

        This milestone is not validation.

        This milestone is not manuscript readiness.

        {_strategy_block()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone plans the proof strategy for TC-001 only.

        This milestone records selected theorem candidate count: 1.

        This milestone records selected TC-001 count: 1.

        This milestone records planned proof strategy count: 1.

        This milestone records planned proof obligation count: 6.

        This milestone preserves theorem candidate plan count: 1.

        This milestone preserves planned theorem candidate count: 4.

        This milestone preserves dependency closure boundary pass count: 1.

        This milestone preserves dependency closure blocker count: 0.

        This milestone preserves unresolved dependency gap count: 0.

        This milestone does not prove new theorems.

        This milestone does not execute theorem proof.

        This milestone does not prove TC-001.

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

        The project has selected TC-001 and planned a controlled proof strategy with six planned proof obligations while keeping theorem proof execution, new theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_phrases = [
        "This milestone proves new theorems",
        "This milestone executes theorem proof",
        "This milestone proves TC-001",
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
        "does not execute theorem proof",
        "does not provide",
        "does not complete full formalization",
        "does not make",
        "does not approve",
        "does not add",
        "at zero",
        "blocker count: 0",
        "unresolved dependency gap count: 0",
    ]
    boundary_phrase_count = sum(report.lower().count(item.lower()) for item in boundary_keywords)

    warnings = [
        "This milestone plans TC-001 proof strategy only.",
        "Theorem proof execution remains zero.",
        "TC-001 proof execution remains zero.",
        "Proof assistant verification, validation, readiness approval, and citation claims remain absent.",
    ]

    return ProofStrategyResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> ProofStrategyResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
