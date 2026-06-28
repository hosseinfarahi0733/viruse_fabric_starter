from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTERS = {
    "controlled_traj_a_definition_completion_execution_count": 1,
    "new_controlled_traj_a_definition_completion_execution_count": 1,
    "traj_a_definition_completion_execution_count": 1,
    "dependent_object_definition_completion_execution_count": 1,
    "definition_completion_execution_count": 1,
    "completion_execution_count": 1,
    "definition_execution_count": 1,
    "new_definition_execution_count": 1,

    "adm_a_definition_completion_count": 1,
    "completed_adm_a_definition_count": 1,
    "c_reg_definition_completion_count": 1,
    "completed_c_reg_definition_count": 1,
    "pi_obs_definition_completion_count": 1,
    "completed_pi_obs_definition_count": 1,
    "m_c_definition_completion_count": 1,
    "completed_m_c_definition_count": 1,
    "r_a_definition_completion_count": 1,
    "completed_r_a_definition_count": 1,
    "traj_a_definition_completion_count": 1,
    "completed_traj_a_definition_count": 1,
    "dependent_object_definition_completion_count": 6,
    "completed_dependent_object_definition_count": 6,
    "all_dependent_object_definition_completion_count": 1,

    "imported_controlled_r_a_definition_completion_execution_count": 1,
    "imported_completed_adm_a_definition_count": 1,
    "imported_completed_c_reg_definition_count": 1,
    "imported_completed_pi_obs_definition_count": 1,
    "imported_completed_m_c_definition_count": 1,
    "imported_completed_r_a_definition_count": 1,
    "imported_dependent_object_definition_completion_count": 5,
    "imported_completed_dependent_object_definition_count": 5,
    "imported_completed_sigma_a_definition_count": 1,
    "imported_completed_formal_definition_count": 1,

    "dependent_object_completion_bundle_integration_count": 0,
    "formalization_complete_count": 0,
    "theorem_candidate_plan_count": 0,
    "new_theorem_proven_count": 0,
    "proof_assistant_verification_count": 0,
    "external_validation_count": 0,
    "independent_experiment_count": 0,
    "manuscript_submission_ready_count": 0,
    "readiness_approval_count": 0,
    "new_citation_added_count": 0,
}


LABEL_OVERRIDES = {
    "controlled_traj_a_definition_completion_execution_count": "Controlled Traj_A definition completion execution count",
    "new_controlled_traj_a_definition_completion_execution_count": "New controlled Traj_A definition completion execution count",
    "traj_a_definition_completion_execution_count": "Traj_A definition completion execution count",
    "dependent_object_definition_completion_execution_count": "Dependent-object definition completion execution count",
    "definition_completion_execution_count": "Definition completion execution count",
    "completion_execution_count": "Completion execution count",
    "definition_execution_count": "Definition execution count",
    "new_definition_execution_count": "New definition execution count",

    "adm_a_definition_completion_count": "Adm_A definition completion count",
    "completed_adm_a_definition_count": "Completed Adm_A definition count",
    "c_reg_definition_completion_count": "C_reg definition completion count",
    "completed_c_reg_definition_count": "Completed C_reg definition count",
    "pi_obs_definition_completion_count": "Pi_obs definition completion count",
    "completed_pi_obs_definition_count": "Completed Pi_obs definition count",
    "m_c_definition_completion_count": "M_c definition completion count",
    "completed_m_c_definition_count": "Completed M_c definition count",
    "r_a_definition_completion_count": "R_A definition completion count",
    "completed_r_a_definition_count": "Completed R_A definition count",
    "traj_a_definition_completion_count": "Traj_A definition completion count",
    "completed_traj_a_definition_count": "Completed Traj_A definition count",
    "dependent_object_definition_completion_count": "Dependent-object definition completion count",
    "completed_dependent_object_definition_count": "Completed dependent-object definition count",
    "all_dependent_object_definition_completion_count": "All dependent-object definition completion count",

    "imported_controlled_r_a_definition_completion_execution_count": "Imported controlled R_A definition completion execution count",
    "imported_completed_adm_a_definition_count": "Imported completed Adm_A definition count",
    "imported_completed_c_reg_definition_count": "Imported completed C_reg definition count",
    "imported_completed_pi_obs_definition_count": "Imported completed Pi_obs definition count",
    "imported_completed_m_c_definition_count": "Imported completed M_c definition count",
    "imported_completed_r_a_definition_count": "Imported completed R_A definition count",
    "imported_dependent_object_definition_completion_count": "Imported dependent-object definition completion count",
    "imported_completed_dependent_object_definition_count": "Imported completed dependent-object definition count",
    "imported_completed_sigma_a_definition_count": "Imported completed Sigma_A definition count",
    "imported_completed_formal_definition_count": "Imported completed formal definition count",

    "dependent_object_completion_bundle_integration_count": "Dependent-object completion bundle integration count",
    "formalization_complete_count": "Formalization complete count",
    "theorem_candidate_plan_count": "Theorem candidate plan count",
    "new_theorem_proven_count": "New theorem proven count",
    "proof_assistant_verification_count": "Proof assistant verification count",
    "external_validation_count": "External validation count",
    "independent_experiment_count": "Independent experiment count",
    "manuscript_submission_ready_count": "Manuscript submission ready count",
    "readiness_approval_count": "Readiness approval count",
    "new_citation_added_count": "New citation added count",
}


REQUIRED_SOURCE_PHRASES = [
    "Controlled R_A definition completion execution count: 1",
    "New controlled R_A definition completion execution count: 1",
    "R_A definition completion execution count: 1",
    "Dependent-object definition completion execution count: 1",
    "Adm_A definition completion count: 1",
    "Completed Adm_A definition count: 1",
    "C_reg definition completion count: 1",
    "Completed C_reg definition count: 1",
    "Pi_obs definition completion count: 1",
    "Completed Pi_obs definition count: 1",
    "M_c definition completion count: 1",
    "Completed M_c definition count: 1",
    "R_A definition completion count: 1",
    "Completed R_A definition count: 1",
    "Dependent-object definition completion count: 5",
    "Completed dependent-object definition count: 5",
    "Traj_A definition completion count: 0",
    "All dependent-object definition completion count: 0",
    "Dependent-object completion bundle integration count: 0",
    "Formalization complete count: 0",
    "Theorem candidate plan count: 0",
    "New theorem proven count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


REQUIRED_REPORT_PHRASES = [
    "Controlled Traj_A definition completion execution count: 1",
    "New controlled Traj_A definition completion execution count: 1",
    "Traj_A definition completion execution count: 1",
    "Dependent-object definition completion execution count: 1",
    "Definition completion execution count: 1",
    "Completion execution count: 1",
    "Definition execution count: 1",
    "New definition execution count: 1",

    "Adm_A definition completion count: 1",
    "Completed Adm_A definition count: 1",
    "C_reg definition completion count: 1",
    "Completed C_reg definition count: 1",
    "Pi_obs definition completion count: 1",
    "Completed Pi_obs definition count: 1",
    "M_c definition completion count: 1",
    "Completed M_c definition count: 1",
    "R_A definition completion count: 1",
    "Completed R_A definition count: 1",
    "Traj_A definition completion count: 1",
    "Completed Traj_A definition count: 1",
    "Dependent-object definition completion count: 6",
    "Completed dependent-object definition count: 6",
    "All dependent-object definition completion count: 1",

    "Imported controlled R_A definition completion execution count: 1",
    "Imported completed Adm_A definition count: 1",
    "Imported completed C_reg definition count: 1",
    "Imported completed Pi_obs definition count: 1",
    "Imported completed M_c definition count: 1",
    "Imported completed R_A definition count: 1",
    "Imported dependent-object definition completion count: 5",
    "Imported completed dependent-object definition count: 5",
    "Imported completed Sigma_A definition count: 1",
    "Imported completed formal definition count: 1",

    "Dependent-object completion bundle integration count: 0",
    "Formalization complete count: 0",
    "Theorem candidate plan count: 0",
    "New theorem proven count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


@dataclass(frozen=True)
class CompletionResult:
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


def _definition_block() -> str:
    return dedent(
        """
        ## Completed formal definition: Traj_A

        Let `Sigma_A` denote the completed formal definition object imported from v8.147.

        Let `Adm_A` denote the completed A-indexed admissibility object imported from v8.149.

        Let `C_reg` denote the completed controlled regularity object imported from v8.150.

        Let `Pi_obs` denote the completed controlled observation projection object imported from v8.151.

        Let `M_c` denote the completed controlled causal mass accounting object imported from v8.152.

        Let `R_A` denote the completed controlled relation object imported from v8.153.

        `Traj_A` is the A-indexed controlled trajectory object that assembles admissible states, regular transitions, observable projections, controlled mass records, and relation membership into finite A-indexed trajectory records without claiming theorem-level reachability, proof assistant verification, empirical validation, or manuscript readiness.

        ### Completed carriers

        Define the admissible carrier:

        `X_A^adm = { x in X_A | Adm_A(x) = admissible }`

        Define the regular transition carrier:

        `T_A^reg = { (x, y, i) in X_A^adm × X_A^adm × I_A | C_reg(x, y, i) = regular }`

        Define the observable carrier:

        `O_A = range(Pi_obs)`

        Define the controlled mass carrier:

        `Q_A^mass = range(M_c)`

        Define the controlled relation carrier:

        `Rel_A = R_A`

        where `X_A` and `I_A` are inherited through the completed `Sigma_A` structure.

        ### Signature

        `Traj_A : Seq(T_A^reg) -> H_A^traj`

        where `H_A^traj` is the A-indexed controlled trajectory record carrier.

        ### Trajectory record form

        For a finite regular transition sequence:

        `tau = ((x_0, x_1, i_0), (x_1, x_2, i_1), ..., (x_{n-1}, x_n, i_{n-1}))`

        `Traj_A(tau) = h_tau in H_A^traj`

        iff all of the following controlled conditions hold:

        1. every state `x_k` satisfies completed `Adm_A`;
        2. every transition `(x_k, x_{k+1}, i_k)` satisfies completed `C_reg`;
        3. every observable record used by the trajectory is produced through completed `Pi_obs`;
        4. every controlled mass record used by the trajectory is produced through completed `M_c`;
        5. every compatibility tuple required by the trajectory is admitted by completed `R_A`;
        6. the trajectory preserves A-indexed structural scope inherited from completed `Sigma_A`;
        7. the trajectory record is finite and explicitly typed in `H_A^traj`;
        8. the trajectory record does not claim reachability completeness, optimality, empirical validation, or proof-level closure.

        ### Reachability and closure boundary

        `Traj_A` is a controlled trajectory record object.

        `Traj_A` does not prove reachability.

        `Traj_A` does not prove uniqueness.

        `Traj_A` does not prove optimality.

        `Traj_A` does not validate empirical trajectories.

        `Traj_A` does not integrate the dependent-object completion bundle.

        `Traj_A` completes the sixth dependent-object definition, but it does not complete full formalization.

        ### Completion boundary

        This definition completes `Traj_A`.

        It preserves completed `Adm_A`.

        It preserves completed `C_reg`.

        It preserves completed `Pi_obs`.

        It preserves completed `M_c`.

        It preserves completed `R_A`.

        It completes the sixth dependent-object definition.

        It records all six dependent-object definitions as completed.

        It does not integrate the dependent-object completion bundle.

        It does not complete full formalization.

        It does not create theorem candidates.

        It does not prove new theorems.

        It does not provide proof assistant verification.

        It does not provide validation.

        It does not make the manuscript ready.
        """
    ).strip()


def _next_steps() -> str:
    return "\n".join(
        [
            "1. Integrate completed dependent-object definitions into a controlled completion bundle.",
            "2. Run a dependency closure boundary audit only after bundle integration, if needed.",
            "3. Plan theorem candidates only after the dependent-object completion bundle exists.",
        ]
    )


def build_report(source_text: str) -> CompletionResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.154 — Controlled Traj_A Definition Completion Execution

        ## Question

        Can Viruse Fabric execute the sixth controlled dependent-object definition completion by completing `Traj_A` after official v8.153 R_A definition completion, while recording all six dependent-object definitions as completed and keeping dependent-object bundle integration, full formalization, theorem candidate planning, theorem proof, proof assistant verification, validation, manuscript readiness, readiness approval, and new citations at zero?

        ## Source artifact

        - `outputs/controlled_r_a_definition_completion_execution_v8_153.md`

        ## Execution interpretation

        v8.154 executes one controlled dependent-object definition completion.

        The newly completed object is `Traj_A`.

        The previously completed dependent objects `Adm_A`, `C_reg`, `Pi_obs`, `M_c`, and `R_A` remain completed.

        This milestone records six completed dependent-object definitions.

        This is an execution milestone, not a planning milestone and not an audit milestone.

        {_definition_block()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone completes exactly one additional dependent-object definition: `Traj_A`.

        This milestone records all six dependent-object definitions as completed.

        This milestone preserves completed `Adm_A`.

        This milestone preserves completed `C_reg`.

        This milestone preserves completed `Pi_obs`.

        This milestone preserves completed `M_c`.

        This milestone preserves completed `R_A`.

        This milestone does not integrate the dependent-object completion bundle.

        This milestone does not complete full formalization.

        This milestone does not create theorem candidates.

        This milestone does not prove new theorems.

        This milestone does not provide proof assistant verification.

        This milestone does not provide external validation.

        This milestone does not provide independent experiments.

        This milestone does not make the manuscript submission ready.

        This milestone does not approve readiness.

        This milestone does not add new citations.

        ## Next steps

        {_next_steps()}

        ## Safe claim

        The project has executed one controlled Traj_A definition completion and records Adm_A, C_reg, Pi_obs, M_c, R_A, and Traj_A as six completed dependent-object definitions while keeping dependent-object completion bundle integration, full formalization completion, theorem candidate planning, theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_phrases = [
        "This milestone integrates the dependent-object completion bundle",
        "This milestone completes full formalization",
        "This milestone creates theorem candidates",
        "This milestone proves new theorems",
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
        "does not integrate",
        "does not complete full formalization",
        "does not create theorem candidates",
        "does not prove",
        "does not provide",
        "does not make",
        "does not approve",
        "does not add",
        "at zero",
        "does not validate",
    ]
    boundary_phrase_count = sum(report.lower().count(item.lower()) for item in boundary_keywords)

    warnings = [
        "This milestone completes Traj_A as the sixth completed dependent object.",
        "All six dependent-object definitions are completed after this execution.",
        "Dependent-object bundle integration remains incomplete.",
        "Full formalization, theorem, proof, validation, readiness approval, and citation claims remain absent.",
    ]

    return CompletionResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> CompletionResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
