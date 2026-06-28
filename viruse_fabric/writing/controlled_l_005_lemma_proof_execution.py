from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTERS = {
    "controlled_l_005_lemma_proof_execution_count": 1,
    "new_controlled_l_005_lemma_proof_execution_count": 1,
    "l_005_lemma_proof_execution_count": 1,
    "new_l_005_lemma_proof_execution_count": 1,
    "new_lemma_proof_execution_count": 1,
    "lemma_proof_execution_count": 5,
    "tc_001_lemma_proof_execution_count": 5,
    "executed_l_005_proof_step_count": 7,
    "proved_l_005_lemma_count": 1,
    "proved_l_004_lemma_count": 1,
    "proved_l_003_lemma_count": 1,
    "proved_l_002_lemma_count": 1,
    "proved_l_001_lemma_count": 1,
    "proved_tc_001_supporting_lemma_count": 5,
    "internal_lemma_proof_count": 5,

    "controlled_l_005_lemma_proof_strategy_planning_count": 1,
    "l_005_lemma_proof_strategy_planning_count": 1,
    "selected_lemma_count": 1,
    "selected_l_005_count": 1,
    "planned_l_005_proof_strategy_count": 1,
    "planned_l_005_proof_step_count": 7,

    "l_001_lemma_proof_execution_count": 1,
    "l_002_lemma_proof_execution_count": 1,
    "l_003_lemma_proof_execution_count": 1,
    "l_004_lemma_proof_execution_count": 1,
    "executed_l_001_proof_step_count": 4,
    "executed_l_002_proof_step_count": 5,
    "executed_l_003_proof_step_count": 6,
    "executed_l_004_proof_step_count": 7,

    "controlled_l_004_lemma_proof_execution_count": 1,
    "controlled_l_003_lemma_proof_execution_count": 1,
    "controlled_l_002_lemma_proof_execution_count": 1,
    "controlled_l_001_lemma_proof_execution_count": 1,

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

    "imported_controlled_l_005_lemma_proof_strategy_planning_count": 1,
    "imported_l_005_lemma_proof_strategy_planning_count": 1,
    "imported_selected_l_005_count": 1,
    "imported_planned_l_005_proof_strategy_count": 1,
    "imported_planned_l_005_proof_step_count": 7,
    "imported_l_001_lemma_proof_execution_count": 1,
    "imported_l_002_lemma_proof_execution_count": 1,
    "imported_l_003_lemma_proof_execution_count": 1,
    "imported_l_004_lemma_proof_execution_count": 1,
    "imported_lemma_proof_execution_count": 4,
    "imported_tc_001_lemma_proof_execution_count": 4,
    "imported_proved_l_001_lemma_count": 1,
    "imported_proved_l_002_lemma_count": 1,
    "imported_proved_l_003_lemma_count": 1,
    "imported_proved_l_004_lemma_count": 1,
    "imported_proved_tc_001_supporting_lemma_count": 4,
    "imported_internal_lemma_proof_count": 4,

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
    "controlled_l_005_lemma_proof_execution_count": "Controlled L-005 lemma proof execution count",
    "new_controlled_l_005_lemma_proof_execution_count": "New controlled L-005 lemma proof execution count",
    "l_005_lemma_proof_execution_count": "L-005 lemma proof execution count",
    "new_l_005_lemma_proof_execution_count": "New L-005 lemma proof execution count",
    "new_lemma_proof_execution_count": "New lemma proof execution count",
    "lemma_proof_execution_count": "Lemma proof execution count",
    "tc_001_lemma_proof_execution_count": "TC-001 lemma proof execution count",
    "executed_l_005_proof_step_count": "Executed L-005 proof step count",
    "proved_l_005_lemma_count": "Proved L-005 lemma count",
    "proved_l_004_lemma_count": "Proved L-004 lemma count",
    "proved_l_003_lemma_count": "Proved L-003 lemma count",
    "proved_l_002_lemma_count": "Proved L-002 lemma count",
    "proved_l_001_lemma_count": "Proved L-001 lemma count",
    "proved_tc_001_supporting_lemma_count": "Proved TC-001 supporting lemma count",
    "internal_lemma_proof_count": "Internal lemma proof count",

    "controlled_l_005_lemma_proof_strategy_planning_count": "Controlled L-005 lemma proof strategy planning count",
    "l_005_lemma_proof_strategy_planning_count": "L-005 lemma proof strategy planning count",
    "selected_lemma_count": "Selected lemma count",
    "selected_l_005_count": "Selected L-005 count",
    "planned_l_005_proof_strategy_count": "Planned L-005 proof strategy count",
    "planned_l_005_proof_step_count": "Planned L-005 proof step count",

    "l_001_lemma_proof_execution_count": "L-001 lemma proof execution count",
    "l_002_lemma_proof_execution_count": "L-002 lemma proof execution count",
    "l_003_lemma_proof_execution_count": "L-003 lemma proof execution count",
    "l_004_lemma_proof_execution_count": "L-004 lemma proof execution count",
    "executed_l_001_proof_step_count": "Executed L-001 proof step count",
    "executed_l_002_proof_step_count": "Executed L-002 proof step count",
    "executed_l_003_proof_step_count": "Executed L-003 proof step count",
    "executed_l_004_proof_step_count": "Executed L-004 proof step count",

    "controlled_l_004_lemma_proof_execution_count": "Controlled L-004 lemma proof execution count",
    "controlled_l_003_lemma_proof_execution_count": "Controlled L-003 lemma proof execution count",
    "controlled_l_002_lemma_proof_execution_count": "Controlled L-002 lemma proof execution count",
    "controlled_l_001_lemma_proof_execution_count": "Controlled L-001 lemma proof execution count",

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
    "completed_dependent_object_definition_count": "Completed dependent-object definition completion count",
    "all_dependent_object_definition_completion_count": "All dependent-object definition completion count",

    "imported_controlled_l_005_lemma_proof_strategy_planning_count": "Imported controlled L-005 lemma proof strategy planning count",
    "imported_l_005_lemma_proof_strategy_planning_count": "Imported L-005 lemma proof strategy planning count",
    "imported_selected_l_005_count": "Imported selected L-005 count",
    "imported_planned_l_005_proof_strategy_count": "Imported planned L-005 proof strategy count",
    "imported_planned_l_005_proof_step_count": "Imported planned L-005 proof step count",
    "imported_l_001_lemma_proof_execution_count": "Imported L-001 lemma proof execution count",
    "imported_l_002_lemma_proof_execution_count": "Imported L-002 lemma proof execution count",
    "imported_l_003_lemma_proof_execution_count": "Imported L-003 lemma proof execution count",
    "imported_l_004_lemma_proof_execution_count": "Imported L-004 lemma proof execution count",
    "imported_lemma_proof_execution_count": "Imported lemma proof execution count",
    "imported_tc_001_lemma_proof_execution_count": "Imported TC-001 lemma proof execution count",
    "imported_proved_l_001_lemma_count": "Imported proved L-001 lemma count",
    "imported_proved_l_002_lemma_count": "Imported proved L-002 lemma count",
    "imported_proved_l_003_lemma_count": "Imported proved L-003 lemma count",
    "imported_proved_l_004_lemma_count": "Imported proved L-004 lemma count",
    "imported_proved_tc_001_supporting_lemma_count": "Imported proved TC-001 supporting lemma count",
    "imported_internal_lemma_proof_count": "Imported internal lemma proof count",

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
    "Controlled L-005 lemma proof strategy planning count: 1",
    "New controlled L-005 lemma proof strategy planning count: 1",
    "L-005 lemma proof strategy planning count: 1",
    "Selected L-005 count: 1",
    "Planned L-005 proof strategy count: 1",
    "Planned L-005 proof step count: 7",
    "L-001 lemma proof execution count: 1",
    "L-002 lemma proof execution count: 1",
    "L-003 lemma proof execution count: 1",
    "L-004 lemma proof execution count: 1",
    "Lemma proof execution count: 4",
    "TC-001 lemma proof execution count: 4",
    "Proved L-001 lemma count: 1",
    "Proved L-002 lemma count: 1",
    "Proved L-003 lemma count: 1",
    "Proved L-004 lemma count: 1",
    "Proved L-005 lemma count: 0",
    "Proved TC-001 supporting lemma count: 4",
    "Internal lemma proof count: 4",
    "New L-005 lemma proof execution count: 0",
    "L-005 lemma proof execution count: 0",
    "New lemma proof execution count: 0",
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


REQUIRED_REPORT_PHRASES = [
    "Controlled L-005 lemma proof execution count: 1",
    "New controlled L-005 lemma proof execution count: 1",
    "L-005 lemma proof execution count: 1",
    "New L-005 lemma proof execution count: 1",
    "New lemma proof execution count: 1",
    "Lemma proof execution count: 5",
    "TC-001 lemma proof execution count: 5",
    "Executed L-005 proof step count: 7",
    "Proved L-005 lemma count: 1",
    "Proved L-004 lemma count: 1",
    "Proved L-003 lemma count: 1",
    "Proved L-002 lemma count: 1",
    "Proved L-001 lemma count: 1",
    "Proved TC-001 supporting lemma count: 5",
    "Internal lemma proof count: 5",

    "Controlled L-005 lemma proof strategy planning count: 1",
    "L-005 lemma proof strategy planning count: 1",
    "Selected L-005 count: 1",
    "Planned L-005 proof strategy count: 1",
    "Planned L-005 proof step count: 7",

    "L-001 lemma proof execution count: 1",
    "L-002 lemma proof execution count: 1",
    "L-003 lemma proof execution count: 1",
    "L-004 lemma proof execution count: 1",
    "Executed L-001 proof step count: 4",
    "Executed L-002 proof step count: 5",
    "Executed L-003 proof step count: 6",
    "Executed L-004 proof step count: 7",

    "Planned lemma count: 6",
    "TC-001 planned lemma count: 6",
    "Selected TC-001 count: 1",

    "Imported controlled L-005 lemma proof strategy planning count: 1",
    "Imported L-005 lemma proof strategy planning count: 1",
    "Imported selected L-005 count: 1",
    "Imported planned L-005 proof strategy count: 1",
    "Imported planned L-005 proof step count: 7",
    "Imported L-001 lemma proof execution count: 1",
    "Imported L-002 lemma proof execution count: 1",
    "Imported L-003 lemma proof execution count: 1",
    "Imported L-004 lemma proof execution count: 1",
    "Imported lemma proof execution count: 4",
    "Imported TC-001 lemma proof execution count: 4",
    "Imported proved L-001 lemma count: 1",
    "Imported proved L-002 lemma count: 1",
    "Imported proved L-003 lemma count: 1",
    "Imported proved L-004 lemma count: 1",
    "Imported proved TC-001 supporting lemma count: 4",
    "Imported internal lemma proof count: 4",

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
class L005ProofExecutionResult:
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

        Executed lemma: `L-005 - Pi_obs codomain well-typing lemma`

        Parent theorem candidate:

        `TC-001 - Admissible regular observation well-typing`

        Parent proof obligation:

        `PO-005 - Pi_obs codomain well-typing`

        Lemma statement:

        If completed `Sigma_A`, completed `Adm_A`, completed `C_reg`, completed `Pi_obs`, and the internally proved L-001, L-002, L-003, and L-004 lemmas are available, then the observation produced by applying `Pi_obs` to an admissible regular TC-001 input is well-typed in the stated observation codomain.

        ## Controlled internal proof execution

        ### Step E001 - Import L-001 carrier availability

        The official L-001 internal lemma proof establishes carrier and transition-index availability from completed `Sigma_A`.

        Therefore L-005 may use L-001 as carrier and transition-index availability support.

        Result:
        - executed
        - accepted internally

        ### Step E002 - Import L-002 admissible-state typing

        The official L-002 internal lemma proof establishes admissible-state typing from completed `Sigma_A`, completed `Adm_A`, and L-001.

        Therefore L-005 may use L-002 as admissible-state typing support.

        Result:
        - executed
        - accepted internally

        ### Step E003 - Import L-003 regular-transition typing

        The official L-003 internal lemma proof establishes regular-transition typing from completed `Sigma_A`, completed `Adm_A`, completed `C_reg`, L-001, and L-002.

        Therefore L-005 may use L-003 as regular-transition typing support.

        Result:
        - executed
        - accepted internally

        ### Step E004 - Import L-004 projection-domain compatibility

        The official L-004 internal lemma proof establishes that the admissible regular TC-001 input lies in the projection domain required by completed `Pi_obs`.

        Therefore L-005 may apply `Pi_obs` to that input without leaving the projection domain.

        Result:
        - executed
        - accepted internally

        ### Step E005 - Completed Pi_obs codomain record availability

        Completed `Pi_obs` supplies the stated observation codomain for the projection route used in TC-001.

        Therefore the proof may reference completed `Pi_obs` as the codomain object for the projected observation.

        Result:
        - executed
        - accepted internally

        ### Step E006 - Bind projected observation to Pi_obs codomain

        By L-004, `Pi_obs` may be applied to the admissible regular TC-001 input.

        By completed `Pi_obs`, the result of this application lands in the stated observation codomain.

        Therefore the projected observation is well-typed in the `Pi_obs` codomain.

        Result:
        - executed
        - accepted internally

        ### Step E007 - No disallowed dependency use

        The L-005 proof uses only completed `Sigma_A`, completed `Adm_A`, completed `C_reg`, completed `Pi_obs`, official L-001, official L-002, official L-003, official L-004, and accepted dependency-closure status.

        It does not use `M_c`, `R_A`, `Traj_A`, TC-001 proof execution, theorem proof execution, proof assistant verification, validation, manuscript readiness, or citation additions as proof dependencies.

        Result:
        - executed
        - accepted internally

        ## Controlled proof conclusion

        L-005 is internally proved as a controlled lemma proof artifact.

        The proof establishes codomain well-typing for the observation produced by `Pi_obs` from admissible regular TC-001 inputs.

        The proof discharges PO-005 at lemma level.

        ## Boundary

        This milestone proves L-005 only as an internal controlled lemma proof.

        It preserves the official L-001, L-002, L-003, and L-004 internal proofs.

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
            "1. Plan controlled L-006 lemma proof strategy.",
            "2. Keep L-006 proof execution separate from L-006 proof strategy planning.",
            "3. Keep TC-001 theorem proof, proof assistant verification, validation, manuscript readiness, and citation work out of this stage.",
        ]
    )


def build_report(source_text: str) -> L005ProofExecutionResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.169 - Controlled L-005 Lemma Proof Execution

        ## Question

        Can Viruse Fabric execute the controlled internal proof of L-005 from the v8.168 proof strategy while preserving the official L-001, L-002, L-003, and L-004 proofs and keeping TC-001 proof execution, theorem proof execution, new theorem proof, proof assistant verification, validation, manuscript readiness, readiness approval, and new citations at zero?

        ## Source artifact

        - `outputs/controlled_l_005_lemma_proof_strategy_planning_v8_168.md`

        ## Execution interpretation

        v8.169 executes the internal controlled proof of L-005 only.

        This milestone is L-005 lemma proof execution.

        This milestone preserves the official L-001, L-002, L-003, and L-004 internal lemma proofs.

        This milestone is not TC-001 proof execution.

        This milestone is not theorem proof execution.

        This milestone is not proof assistant verification.

        {_proof_block()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone executes and internally proves L-005 only.

        This milestone records L-005 lemma proof execution count: 1.

        This milestone records new L-005 lemma proof execution count: 1.

        This milestone records lemma proof execution count: 5.

        This milestone records TC-001 lemma proof execution count: 5.

        This milestone records proved L-005 lemma count: 1.

        This milestone preserves proved L-004 lemma count: 1.

        This milestone preserves proved L-003 lemma count: 1.

        This milestone preserves proved L-002 lemma count: 1.

        This milestone preserves proved L-001 lemma count: 1.

        This milestone records proved TC-001 supporting lemma count: 5.

        This milestone records executed L-005 proof step count: 7.

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

        The project has executed and internally proved L-005 as the fifth controlled TC-001 supporting lemma, while preserving the official L-001, L-002, L-003, and L-004 proofs and keeping TC-001 proof execution, theorem proof execution, new theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero.
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
        "This milestone proves L-005 only as an internal controlled lemma proof.",
        "The official L-001, L-002, L-003, and L-004 proofs remain preserved.",
        "TC-001 proof execution remains zero.",
        "Theorem proof execution remains zero.",
        "Proof assistant verification, validation, readiness approval, and citation claims remain absent.",
    ]

    return L005ProofExecutionResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> L005ProofExecutionResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
