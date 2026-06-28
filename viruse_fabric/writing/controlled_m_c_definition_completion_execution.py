from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTERS = {
    "controlled_m_c_definition_completion_execution_count": 1,
    "new_controlled_m_c_definition_completion_execution_count": 1,
    "m_c_definition_completion_execution_count": 1,
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
    "dependent_object_definition_completion_count": 4,
    "completed_dependent_object_definition_count": 4,

    "imported_controlled_pi_obs_definition_completion_execution_count": 1,
    "imported_completed_adm_a_definition_count": 1,
    "imported_completed_c_reg_definition_count": 1,
    "imported_completed_pi_obs_definition_count": 1,
    "imported_dependent_object_definition_completion_count": 3,
    "imported_completed_dependent_object_definition_count": 3,
    "imported_completed_sigma_a_definition_count": 1,
    "imported_completed_formal_definition_count": 1,

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
    "controlled_m_c_definition_completion_execution_count": "Controlled M_c definition completion execution count",
    "new_controlled_m_c_definition_completion_execution_count": "New controlled M_c definition completion execution count",
    "m_c_definition_completion_execution_count": "M_c definition completion execution count",
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
    "dependent_object_definition_completion_count": "Dependent-object definition completion count",
    "completed_dependent_object_definition_count": "Completed dependent-object definition count",

    "imported_controlled_pi_obs_definition_completion_execution_count": "Imported controlled Pi_obs definition completion execution count",
    "imported_completed_adm_a_definition_count": "Imported completed Adm_A definition count",
    "imported_completed_c_reg_definition_count": "Imported completed C_reg definition count",
    "imported_completed_pi_obs_definition_count": "Imported completed Pi_obs definition count",
    "imported_dependent_object_definition_completion_count": "Imported dependent-object definition completion count",
    "imported_completed_dependent_object_definition_count": "Imported completed dependent-object definition count",
    "imported_completed_sigma_a_definition_count": "Imported completed Sigma_A definition count",
    "imported_completed_formal_definition_count": "Imported completed formal definition count",

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
    "Controlled Pi_obs definition completion execution count: 1",
    "New controlled Pi_obs definition completion execution count: 1",
    "Pi_obs definition completion execution count: 1",
    "Dependent-object definition completion execution count: 1",
    "Adm_A definition completion count: 1",
    "Completed Adm_A definition count: 1",
    "C_reg definition completion count: 1",
    "Completed C_reg definition count: 1",
    "Pi_obs definition completion count: 1",
    "Completed Pi_obs definition count: 1",
    "Dependent-object definition completion count: 3",
    "Completed dependent-object definition count: 3",
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
    "Controlled M_c definition completion execution count: 1",
    "New controlled M_c definition completion execution count: 1",
    "M_c definition completion execution count: 1",
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
    "Dependent-object definition completion count: 4",
    "Completed dependent-object definition count: 4",

    "Imported controlled Pi_obs definition completion execution count: 1",
    "Imported completed Adm_A definition count: 1",
    "Imported completed C_reg definition count: 1",
    "Imported completed Pi_obs definition count: 1",
    "Imported dependent-object definition completion count: 3",
    "Imported completed dependent-object definition count: 3",
    "Imported completed Sigma_A definition count: 1",
    "Imported completed formal definition count: 1",

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
        ## Completed formal definition: M_c

        Let `Sigma_A` denote the completed formal definition object imported from v8.147.

        Let `Adm_A` denote the completed A-indexed admissibility object imported from v8.149.

        Let `C_reg` denote the completed controlled regularity object imported from v8.150.

        Let `Pi_obs` denote the completed controlled observation projection object imported from v8.151.

        `M_c` is the controlled causal mass accounting object that assigns structured mass records to admissible states, regular transitions, and their observable projections without claiming empirical validation or theorem proof.

        ### Admissible, regular, and observable carriers

        Define the admissible carrier:

        `X_A^adm = { x in X_A | Adm_A(x) = admissible }`

        Define the regular transition carrier:

        `T_A^reg = { (x, y, i) in X_A^adm × X_A^adm × I_A | C_reg(x, y, i) = regular }`

        Define the observable carrier:

        `O_A = range(Pi_obs)`

        where `X_A` and `I_A` are inherited through the completed `Sigma_A` structure.

        ### Signature

        `M_c : X_A^adm ∪ T_A^reg ∪ O_A -> Q_A^mass`

        where `Q_A^mass` is the A-indexed controlled causal mass accounting carrier.

        ### Accounting form

        For an admissible state `x in X_A^adm`:

        `M_c(x) = q_x in Q_A^mass`

        For a regular transition `(x, y, i) in T_A^reg`:

        `M_c(x, y, i) = q_{x,y,i} in Q_A^mass`

        For an observable representation `o in O_A`:

        `M_c(o) = q_o in Q_A^mass`

        iff all of the following controlled conditions hold:

        1. state inputs satisfy completed `Adm_A`;
        2. transition inputs satisfy completed `C_reg`;
        3. observable inputs are produced through completed `Pi_obs`;
        4. every assigned mass record is typed in `Q_A^mass`;
        5. mass records preserve A-indexed structural scope inherited from completed `Sigma_A`;
        6. mass accounting is descriptive and controlled, not a theorem of conservation;
        7. mass accounting remains eligible for later `R_A` and `Traj_A` completion without implying that those objects are already complete.

        ### Conservation and exclusion boundary

        `M_c` is a controlled accounting object.

        `M_c` does not prove conservation.

        `M_c` does not validate empirical causal mass.

        `M_c` does not claim that observable mass records recover hidden causal structure.

        `M_c` only records structured accounting over completed admissibility, regularity, and observation carriers.

        ### Completion boundary

        This definition completes `M_c` only.

        It preserves completed `Adm_A`.

        It preserves completed `C_reg`.

        It preserves completed `Pi_obs`.

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
            "1. Execute controlled R_A definition completion.",
            "2. Execute controlled Traj_A definition completion.",
            "3. Integrate completed dependent-object definitions into a bundle only after all six completions exist.",
            "4. Plan theorem candidates only after the dependent-object completion bundle exists.",
        ]
    )


def build_report(source_text: str) -> CompletionResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.152 — Controlled M_c Definition Completion Execution

        ## Question

        Can Viruse Fabric execute the fourth controlled dependent-object definition completion by completing `M_c` after official v8.151 Pi_obs definition completion, while keeping R_A, Traj_A, all-dependent-object completion, bundle integration, full formalization, theorem candidate planning, theorem proof, proof assistant verification, validation, manuscript readiness, readiness approval, and new citations at zero?

        ## Source artifact

        - `outputs/controlled_pi_obs_definition_completion_execution_v8_151.md`

        ## Execution interpretation

        v8.152 executes one controlled dependent-object definition completion.

        The newly completed object is `M_c`.

        The previously completed dependent objects `Adm_A`, `C_reg`, and `Pi_obs` remain completed.

        This is an execution milestone, not a planning milestone and not an audit milestone.

        {_definition_block()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone completes exactly one additional dependent-object definition: `M_c`.

        This milestone preserves completed `Adm_A`.

        This milestone preserves completed `C_reg`.

        This milestone preserves completed `Pi_obs`.

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

        The project has executed one controlled M_c definition completion and records Adm_A, C_reg, Pi_obs, and M_c as four completed dependent-object definitions while keeping R_A, Traj_A, all-dependent-object completion, dependent-object bundle integration, full formalization completion, theorem candidate planning, theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_phrases = [
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
        "does not validate",
        "does not claim",
    ]
    boundary_phrase_count = sum(report.lower().count(item.lower()) for item in boundary_keywords)

    warnings = [
        "This milestone completes M_c only as the fourth completed dependent object.",
        "R_A and Traj_A remain uncompleted.",
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
