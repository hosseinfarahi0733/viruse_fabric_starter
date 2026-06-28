from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTERS = {
    "controlled_pi_obs_definition_completion_execution_count": 1,
    "new_controlled_pi_obs_definition_completion_execution_count": 1,
    "pi_obs_definition_completion_execution_count": 1,
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
    "dependent_object_definition_completion_count": 3,
    "completed_dependent_object_definition_count": 3,

    "imported_controlled_c_reg_definition_completion_execution_count": 1,
    "imported_completed_adm_a_definition_count": 1,
    "imported_completed_c_reg_definition_count": 1,
    "imported_dependent_object_definition_completion_count": 2,
    "imported_completed_dependent_object_definition_count": 2,
    "imported_completed_sigma_a_definition_count": 1,
    "imported_completed_formal_definition_count": 1,

    "m_c_definition_completion_count": 0,
    "r_a_definition_completion_count": 0,
    "traj_a_definition_completion_count": 0,

    "all_dependent_object_definition_completion_count": 0,
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
    "controlled_pi_obs_definition_completion_execution_count": "Controlled Pi_obs definition completion execution count",
    "new_controlled_pi_obs_definition_completion_execution_count": "New controlled Pi_obs definition completion execution count",
    "pi_obs_definition_completion_execution_count": "Pi_obs definition completion execution count",
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
    "dependent_object_definition_completion_count": "Dependent-object definition completion count",
    "completed_dependent_object_definition_count": "Completed dependent-object definition count",

    "imported_controlled_c_reg_definition_completion_execution_count": "Imported controlled C_reg definition completion execution count",
    "imported_completed_adm_a_definition_count": "Imported completed Adm_A definition count",
    "imported_completed_c_reg_definition_count": "Imported completed C_reg definition count",
    "imported_dependent_object_definition_completion_count": "Imported dependent-object definition completion count",
    "imported_completed_dependent_object_definition_count": "Imported completed dependent-object definition count",
    "imported_completed_sigma_a_definition_count": "Imported completed Sigma_A definition count",
    "imported_completed_formal_definition_count": "Imported completed formal definition count",

    "m_c_definition_completion_count": "M_c definition completion count",
    "r_a_definition_completion_count": "R_A definition completion count",
    "traj_a_definition_completion_count": "Traj_A definition completion count",

    "all_dependent_object_definition_completion_count": "All dependent-object definition completion count",
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
    "Controlled C_reg definition completion execution count: 1",
    "New controlled C_reg definition completion execution count: 1",
    "C_reg definition completion execution count: 1",
    "Dependent-object definition completion execution count: 1",
    "Adm_A definition completion count: 1",
    "Completed Adm_A definition count: 1",
    "C_reg definition completion count: 1",
    "Completed C_reg definition count: 1",
    "Dependent-object definition completion count: 2",
    "Completed dependent-object definition count: 2",
    "Pi_obs definition completion count: 0",
    "M_c definition completion count: 0",
    "R_A definition completion count: 0",
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
    "Controlled Pi_obs definition completion execution count: 1",
    "New controlled Pi_obs definition completion execution count: 1",
    "Pi_obs definition completion execution count: 1",
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
    "Dependent-object definition completion count: 3",
    "Completed dependent-object definition count: 3",

    "Imported controlled C_reg definition completion execution count: 1",
    "Imported completed Adm_A definition count: 1",
    "Imported completed C_reg definition count: 1",
    "Imported dependent-object definition completion count: 2",
    "Imported completed dependent-object definition count: 2",
    "Imported completed Sigma_A definition count: 1",
    "Imported completed formal definition count: 1",

    "M_c definition completion count: 0",
    "R_A definition completion count: 0",
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
        ## Completed formal definition: Pi_obs

        Let `Sigma_A` denote the completed formal definition object imported from v8.147.

        Let `Adm_A` denote the completed A-indexed admissibility object imported from v8.149.

        Let `C_reg` denote the completed controlled regularity object imported from v8.150.

        `Pi_obs` is the controlled observation projection object that maps admissible and regular A-indexed states or transitions into observable representations without claiming empirical validation.

        ### Admissible and regular carrier

        Define the admissible carrier:

        `X_A^adm = { x in X_A | Adm_A(x) = admissible }`

        Define the regular transition carrier:

        `T_A^reg = { (x, y, i) in X_A^adm × X_A^adm × I_A | C_reg(x, y, i) = regular }`

        where `X_A` and `I_A` are inherited through the completed `Sigma_A` structure.

        ### Signature

        `Pi_obs : X_A^adm ∪ T_A^reg -> O_A`

        where `O_A` is the A-indexed observable representation carrier.

        ### Projection form

        For an admissible state `x in X_A^adm`:

        `Pi_obs(x) = o_x in O_A`

        For a regular transition `(x, y, i) in T_A^reg`:

        `Pi_obs(x, y, i) = o_{x,y,i} in O_A`

        iff all of the following controlled conditions hold:

        1. the input is typed over completed `Sigma_A`;
        2. state inputs satisfy completed `Adm_A`;
        3. transition inputs satisfy completed `C_reg`;
        4. the projection target lies in the declared A-indexed observation carrier `O_A`;
        5. the projection records observable structure without claiming full recovery of hidden structure;
        6. the projection preserves an explicit loss boundary;
        7. the projection remains eligible for later `M_c`, `R_A`, and `Traj_A` completion without implying that those objects are already complete.

        ### Loss boundary

        `Pi_obs` is not an inverse map.

        `Pi_obs` does not claim that every hidden structural component in `Sigma_A` is observable.

        `Pi_obs` only records controlled observable representations for admissible states and regular transitions.

        ### Completion boundary

        This definition completes `Pi_obs` only.

        It preserves completed `Adm_A`.

        It preserves completed `C_reg`.

        It does not complete `M_c`.

        It does not complete `R_A`.

        It does not complete `Traj_A`.

        It does not complete all dependent objects.

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
            "1. Execute controlled M_c definition completion.",
            "2. Execute controlled R_A definition completion.",
            "3. Execute controlled Traj_A definition completion.",
            "4. Integrate completed dependent-object definitions into a bundle only after all six completions exist.",
            "5. Plan theorem candidates only after the dependent-object completion bundle exists.",
        ]
    )


def build_report(source_text: str) -> CompletionResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.151 — Controlled Pi_obs Definition Completion Execution

        ## Question

        Can Viruse Fabric execute the third controlled dependent-object definition completion by completing `Pi_obs` after official v8.150 C_reg definition completion, while keeping M_c, R_A, Traj_A, all-dependent-object completion, bundle integration, full formalization, theorem candidate planning, theorem proof, proof assistant verification, validation, manuscript readiness, readiness approval, and new citations at zero?

        ## Source artifact

        - `outputs/controlled_c_reg_definition_completion_execution_v8_150.md`

        ## Execution interpretation

        v8.151 executes one controlled dependent-object definition completion.

        The newly completed object is `Pi_obs`.

        The previously completed dependent objects `Adm_A` and `C_reg` remain completed.

        This is an execution milestone, not a planning milestone and not an audit milestone.

        {_definition_block()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone completes exactly one additional dependent-object definition: `Pi_obs`.

        This milestone preserves completed `Adm_A`.

        This milestone preserves completed `C_reg`.

        This milestone does not complete `M_c`.

        This milestone does not complete `R_A`.

        This milestone does not complete `Traj_A`.

        This milestone does not complete all dependent objects.

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

        The project has executed one controlled Pi_obs definition completion and records Adm_A, C_reg, and Pi_obs as three completed dependent-object definitions while keeping M_c, R_A, Traj_A, all-dependent-object completion, dependent-object bundle integration, full formalization completion, theorem candidate planning, theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_phrases = [
        "This milestone completes `M_c`",
        "This milestone completes `R_A`",
        "This milestone completes `Traj_A`",
        "This milestone completes all dependent objects",
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
        "does not complete",
        "does not integrate",
        "does not create theorem candidates",
        "does not prove",
        "does not provide",
        "does not make",
        "does not approve",
        "does not add",
        "at zero",
        "not an inverse map",
    ]
    boundary_phrase_count = sum(report.lower().count(item.lower()) for item in boundary_keywords)

    warnings = [
        "This milestone completes Pi_obs only as the third completed dependent object.",
        "M_c, R_A, and Traj_A remain uncompleted.",
        "All-dependent-object completion and bundle integration remain incomplete.",
        "Theorem, proof, validation, readiness approval, and citation claims remain absent.",
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
