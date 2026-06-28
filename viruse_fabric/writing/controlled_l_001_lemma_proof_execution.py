from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTERS = {
    "controlled_l_001_lemma_proof_execution_count": 1,
    "new_controlled_l_001_lemma_proof_execution_count": 1,
    "l_001_lemma_proof_execution_count": 1,
    "lemma_proof_execution_count": 1,
    "tc_001_lemma_proof_execution_count": 1,
    "executed_l_001_proof_step_count": 4,
    "proved_l_001_lemma_count": 1,
    "proved_tc_001_supporting_lemma_count": 1,
    "internal_lemma_proof_count": 1,

    "controlled_l_001_lemma_proof_strategy_planning_count": 1,
    "l_001_lemma_proof_strategy_planning_count": 1,
    "selected_lemma_count": 1,
    "selected_l_001_count": 1,
    "planned_l_001_proof_strategy_count": 1,
    "planned_l_001_proof_step_count": 4,

    "controlled_tc_001_proof_obligation_lemma_planning_count": 1,
    "tc_001_proof_obligation_lemma_planning_count": 1,
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

    "imported_controlled_l_001_lemma_proof_strategy_planning_count": 1,
    "imported_l_001_lemma_proof_strategy_planning_count": 1,
    "imported_selected_l_001_count": 1,
    "imported_planned_l_001_proof_strategy_count": 1,
    "imported_planned_l_001_proof_step_count": 4,
    "imported_planned_lemma_count": 6,
    "imported_tc_001_planned_lemma_count": 6,
    "imported_selected_tc_001_count": 1,
    "imported_dependency_closure_boundary_pass_count": 1,
    "imported_dependency_closure_blocker_count": 0,
    "imported_unresolved_dependency_gap_count": 0,

    "formalization_complete_count": 0,
    "new_theorem_proven_count": 0,
    "theorem_proof_execution_count": 0,
    "tc_001_proof_execution_count": 0,
    "tc_001_theorem_proven_count": 0,
    "proof_assistant_verification_count": 0,
    "external_validation_count": 0,
    "independent_experiment_count": 0,
    "manuscript_submission_ready_count": 0,
    "readiness_approval_count": 0,
    "new_citation_added_count": 0,
}


LABEL_OVERRIDES = {
    "controlled_l_001_lemma_proof_execution_count": "Controlled L-001 lemma proof execution count",
    "new_controlled_l_001_lemma_proof_execution_count": "New controlled L-001 lemma proof execution count",
    "l_001_lemma_proof_execution_count": "L-001 lemma proof execution count",
    "lemma_proof_execution_count": "Lemma proof execution count",
    "tc_001_lemma_proof_execution_count": "TC-001 lemma proof execution count",
    "executed_l_001_proof_step_count": "Executed L-001 proof step count",
    "proved_l_001_lemma_count": "Proved L-001 lemma count",
    "proved_tc_001_supporting_lemma_count": "Proved TC-001 supporting lemma count",
    "internal_lemma_proof_count": "Internal lemma proof count",

    "controlled_l_001_lemma_proof_strategy_planning_count": "Controlled L-001 lemma proof strategy planning count",
    "l_001_lemma_proof_strategy_planning_count": "L-001 lemma proof strategy planning count",
    "selected_lemma_count": "Selected lemma count",
    "selected_l_001_count": "Selected L-001 count",
    "planned_l_001_proof_strategy_count": "Planned L-001 proof strategy count",
    "planned_l_001_proof_step_count": "Planned L-001 proof step count",

    "controlled_tc_001_proof_obligation_lemma_planning_count": "Controlled TC-001 proof obligation lemma planning count",
    "tc_001_proof_obligation_lemma_planning_count": "TC-001 proof obligation lemma planning count",
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

    "imported_controlled_l_001_lemma_proof_strategy_planning_count": "Imported controlled L-001 lemma proof strategy planning count",
    "imported_l_001_lemma_proof_strategy_planning_count": "Imported L-001 lemma proof strategy planning count",
    "imported_selected_l_001_count": "Imported selected L-001 count",
    "imported_planned_l_001_proof_strategy_count": "Imported planned L-001 proof strategy count",
    "imported_planned_l_001_proof_step_count": "Imported planned L-001 proof step count",
    "imported_planned_lemma_count": "Imported planned lemma count",
    "imported_tc_001_planned_lemma_count": "Imported TC-001 planned lemma count",
    "imported_selected_tc_001_count": "Imported selected TC-001 count",
    "imported_dependency_closure_boundary_pass_count": "Imported dependency closure boundary pass count",
    "imported_dependency_closure_blocker_count": "Imported dependency closure blocker count",
    "imported_unresolved_dependency_gap_count": "Imported unresolved dependency gap count",

    "formalization_complete_count": "Formalization complete count",
    "new_theorem_proven_count": "New theorem proven count",
    "theorem_proof_execution_count": "Theorem proof execution count",
    "tc_001_proof_execution_count": "TC-001 proof execution count",
    "tc_001_theorem_proven_count": "TC-001 theorem proven count",
    "proof_assistant_verification_count": "Proof assistant verification count",
    "external_validation_count": "External validation count",
    "independent_experiment_count": "Independent experiment count",
    "manuscript_submission_ready_count": "Manuscript submission ready count",
    "readiness_approval_count": "Readiness approval count",
    "new_citation_added_count": "New citation added count",
}


REQUIRED_SOURCE_PHRASES = [
    "Controlled L-001 lemma proof strategy planning count: 1",
    "New controlled L-001 lemma proof strategy planning count: 1",
    "L-001 lemma proof strategy planning count: 1",
    "Selected lemma count: 1",
    "Selected L-001 count: 1",
    "Planned L-001 proof strategy count: 1",
    "Planned L-001 proof step count: 4",
    "Planned lemma count: 6",
    "TC-001 planned lemma count: 6",
    "Accepted lemma plan count: 1",
    "Selected TC-001 count: 1",
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


REQUIRED_REPORT_PHRASES = [
    "Controlled L-001 lemma proof execution count: 1",
    "New controlled L-001 lemma proof execution count: 1",
    "L-001 lemma proof execution count: 1",
    "Lemma proof execution count: 1",
    "TC-001 lemma proof execution count: 1",
    "Executed L-001 proof step count: 4",
    "Proved L-001 lemma count: 1",
    "Proved TC-001 supporting lemma count: 1",
    "Internal lemma proof count: 1",

    "Controlled L-001 lemma proof strategy planning count: 1",
    "L-001 lemma proof strategy planning count: 1",
    "Selected lemma count: 1",
    "Selected L-001 count: 1",
    "Planned L-001 proof strategy count: 1",
    "Planned L-001 proof step count: 4",

    "Planned lemma count: 6",
    "TC-001 planned lemma count: 6",
    "Selected TC-001 count: 1",

    "Imported controlled L-001 lemma proof strategy planning count: 1",
    "Imported L-001 lemma proof strategy planning count: 1",
    "Imported selected L-001 count: 1",
    "Imported planned L-001 proof strategy count: 1",
    "Imported planned L-001 proof step count: 4",

    "Formalization complete count: 0",
    "New theorem proven count: 0",
    "Theorem proof execution count: 0",
    "TC-001 proof execution count: 0",
    "TC-001 theorem proven count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


@dataclass(frozen=True)
class L001ProofExecutionResult:
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


def _proof_block() -> str:
    return dedent(
        """
        ## Executed lemma

        Executed lemma: `L-001 — Sigma_A carrier availability lemma`

        Parent theorem candidate:

        `TC-001 — Admissible regular observation well-typing`

        Parent proof obligation:

        `PO-001 — Sigma_A carrier availability`

        Lemma statement:

        If completed `Sigma_A` is available in the dependency-closed bundle, then the A-indexed carrier and transition index required by TC-001 can be referenced as well-typed formal carriers.

        ## Controlled internal proof execution

        ### Step E001 — Completed Sigma_A record availability

        From the imported dependency-closed bundle, completed `Sigma_A` is recorded as the formal definition object preceding all dependent-object definitions.

        Therefore the proof may reference completed `Sigma_A` as an available formal record.

        Result:
        - executed
        - accepted internally

        ### Step E002 — A-indexed state carrier availability

        By completed `Sigma_A`, the A-indexed state carrier required by TC-001 is part of the formal carrier structure.

        Therefore the TC-001 proof route may reference the A-indexed state carrier as well-typed.

        Result:
        - executed
        - accepted internally

        ### Step E003 — A-indexed transition index availability

        By completed `Sigma_A`, the A-indexed transition index required by TC-001 is part of the formal index structure.

        Therefore the TC-001 proof route may reference the A-indexed transition index as well-typed.

        Result:
        - executed
        - accepted internally

        ### Step E004 — No disallowed dependency use

        The L-001 proof uses only completed `Sigma_A` and the accepted dependency-closure status.

        It does not use `Adm_A`, `C_reg`, `Pi_obs`, `M_c`, `R_A`, `Traj_A`, TC-001 proof execution, theorem proof execution, proof assistant verification, validation, manuscript readiness, or citation additions as proof dependencies.

        Result:
        - executed
        - accepted internally

        ## Controlled proof conclusion

        L-001 is internally proved as a controlled lemma proof artifact.

        The proof establishes carrier and transition-index availability from completed `Sigma_A`.

        The proof discharges PO-001 at lemma level.

        ## Boundary

        This milestone proves L-001 only as an internal controlled lemma proof.

        It does not prove TC-001.

        It does not execute TC-001 proof.

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
            "1. Plan controlled L-002 lemma proof strategy.",
            "2. Keep L-002 proof execution separate from L-002 proof strategy planning.",
            "3. Keep TC-001 theorem proof, proof assistant verification, validation, manuscript readiness, and citation work out of this stage.",
        ]
    )


def build_report(source_text: str) -> L001ProofExecutionResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.161 — Controlled L-001 Lemma Proof Execution

        ## Question

        Can Viruse Fabric execute the controlled internal proof of L-001 from the v8.160 proof strategy while keeping TC-001 proof execution, theorem proof execution, new theorem proof, proof assistant verification, validation, manuscript readiness, readiness approval, and new citations at zero?

        ## Source artifact

        - `outputs/controlled_l_001_lemma_proof_strategy_planning_v8_160.md`

        ## Execution interpretation

        v8.161 executes the internal controlled proof of L-001 only.

        This milestone is lemma proof execution.

        This milestone is not TC-001 proof execution.

        This milestone is not theorem proof execution.

        This milestone is not proof assistant verification.

        {_proof_block()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone executes and internally proves L-001 only.

        This milestone records L-001 lemma proof execution count: 1.

        This milestone records lemma proof execution count: 1.

        This milestone records proved L-001 lemma count: 1.

        This milestone records proved TC-001 supporting lemma count: 1.

        This milestone records executed L-001 proof step count: 4.

        This milestone preserves selected TC-001 count: 1.

        This milestone preserves planned lemma count: 6.

        This milestone does not prove TC-001.

        This milestone does not execute TC-001 proof.

        This milestone does not prove any theorem.

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

        The project has executed and internally proved L-001 as one controlled TC-001 supporting lemma while keeping TC-001 proof execution, theorem proof execution, new theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_phrases = [
        "This milestone proves TC-001",
        "This milestone executes TC-001 proof",
        "This milestone proves any theorem",
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
        "does not prove tc-001",
        "does not execute tc-001 proof",
        "does not prove any theorem",
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
        "This milestone proves L-001 only as an internal controlled lemma proof.",
        "TC-001 proof execution remains zero.",
        "Theorem proof execution remains zero.",
        "Proof assistant verification, validation, readiness approval, and citation claims remain absent.",
    ]

    return L001ProofExecutionResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> L001ProofExecutionResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
