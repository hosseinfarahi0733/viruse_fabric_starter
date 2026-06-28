from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTERS = {
    "controlled_c_reg_definition_completion_execution_count": 1,
    "new_controlled_c_reg_definition_completion_execution_count": 1,
    "c_reg_definition_completion_execution_count": 1,
    "dependent_object_definition_completion_execution_count": 1,
    "definition_completion_execution_count": 1,
    "completion_execution_count": 1,
    "definition_execution_count": 1,
    "new_definition_execution_count": 1,

    "adm_a_definition_completion_count": 1,
    "completed_adm_a_definition_count": 1,
    "c_reg_definition_completion_count": 1,
    "completed_c_reg_definition_count": 1,
    "dependent_object_definition_completion_count": 2,
    "completed_dependent_object_definition_count": 2,

    "imported_controlled_adm_a_definition_completion_execution_count": 1,
    "imported_completed_adm_a_definition_count": 1,
    "imported_dependent_object_definition_completion_count": 1,
    "imported_completed_dependent_object_definition_count": 1,
    "imported_completed_sigma_a_definition_count": 1,
    "imported_completed_formal_definition_count": 1,

    "pi_obs_definition_completion_count": 0,
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
    "controlled_c_reg_definition_completion_execution_count": "Controlled C_reg definition completion execution count",
    "new_controlled_c_reg_definition_completion_execution_count": "New controlled C_reg definition completion execution count",
    "c_reg_definition_completion_execution_count": "C_reg definition completion execution count",
    "dependent_object_definition_completion_execution_count": "Dependent-object definition completion execution count",
    "definition_completion_execution_count": "Definition completion execution count",
    "completion_execution_count": "Completion execution count",
    "definition_execution_count": "Definition execution count",
    "new_definition_execution_count": "New definition execution count",

    "adm_a_definition_completion_count": "Adm_A definition completion count",
    "completed_adm_a_definition_count": "Completed Adm_A definition count",
    "c_reg_definition_completion_count": "C_reg definition completion count",
    "completed_c_reg_definition_count": "Completed C_reg definition count",
    "dependent_object_definition_completion_count": "Dependent-object definition completion count",
    "completed_dependent_object_definition_count": "Completed dependent-object definition count",

    "imported_controlled_adm_a_definition_completion_execution_count": "Imported controlled Adm_A definition completion execution count",
    "imported_completed_adm_a_definition_count": "Imported completed Adm_A definition count",
    "imported_dependent_object_definition_completion_count": "Imported dependent-object definition completion count",
    "imported_completed_dependent_object_definition_count": "Imported completed dependent-object definition count",
    "imported_completed_sigma_a_definition_count": "Imported completed Sigma_A definition count",
    "imported_completed_formal_definition_count": "Imported completed formal definition count",

    "pi_obs_definition_completion_count": "Pi_obs definition completion count",
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
    "Controlled Adm_A definition completion execution count: 1",
    "New controlled Adm_A definition completion execution count: 1",
    "Adm_A definition completion execution count: 1",
    "Dependent-object definition completion execution count: 1",
    "Adm_A definition completion count: 1",
    "Completed Adm_A definition count: 1",
    "Dependent-object definition completion count: 1",
    "Completed dependent-object definition count: 1",
    "C_reg definition completion count: 0",
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
    "Controlled C_reg definition completion execution count: 1",
    "New controlled C_reg definition completion execution count: 1",
    "C_reg definition completion execution count: 1",
    "Dependent-object definition completion execution count: 1",
    "Definition completion execution count: 1",
    "Completion execution count: 1",
    "Definition execution count: 1",
    "New definition execution count: 1",

    "Adm_A definition completion count: 1",
    "Completed Adm_A definition count: 1",
    "C_reg definition completion count: 1",
    "Completed C_reg definition count: 1",
    "Dependent-object definition completion count: 2",
    "Completed dependent-object definition count: 2",

    "Imported controlled Adm_A definition completion execution count: 1",
    "Imported completed Adm_A definition count: 1",
    "Imported dependent-object definition completion count: 1",
    "Imported completed dependent-object definition count: 1",
    "Imported completed Sigma_A definition count: 1",
    "Imported completed formal definition count: 1",

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
        ## Completed formal definition: C_reg

        Let `Sigma_A` denote the completed formal definition object imported from v8.147.

        Let `Adm_A` denote the completed A-indexed admissibility object imported from v8.149.

        `C_reg` is the controlled regularity constraint family that evaluates whether an admissible A-indexed transition is regular enough to be eligible for later observation, causal mass, relation, and trajectory construction.

        ### Admissible carrier

        Define the admissible carrier:

        `X_A^adm = { x in X_A | Adm_A(x) = admissible }`

        where `X_A` is the candidate A-indexed state carrier inherited through completed `Sigma_A`.

        ### Signature

        `C_reg : X_A^adm × X_A^adm × I_A -> {regular, rejected}`

        where `I_A` is the A-indexed transition or time-compatibility index inherited from the completed `Sigma_A` structure.

        ### Predicate form

        For candidate admissible states `x, y in X_A^adm` and transition index `i in I_A`:

        `C_reg(x, y, i) = regular`

        iff all of the following controlled conditions hold:

        1. `x` and `y` are typed over the completed `Sigma_A` carrier.
        2. `Adm_A(x) = admissible`.
        3. `Adm_A(y) = admissible`.
        4. `i` respects the time-index compatibility boundary inherited from `Sigma_A`.
        5. the transition from `x` to `y` preserves the declared A-indexed structural scope.
        6. the transition does not introduce a forbidden discontinuity relative to the controlled dependent-object draft bundle.
        7. the transition remains eligible for later `Pi_obs`, `M_c`, `R_A`, and `Traj_A` completion without implying that those objects are already complete.

        Otherwise:

        `C_reg(x, y, i) = rejected`

        ### Completion boundary

        This definition completes `C_reg` only.

        It preserves completed `Adm_A`.

        It does not complete `Pi_obs`.

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
            "1. Execute controlled Pi_obs definition completion.",
            "2. Execute controlled M_c definition completion.",
            "3. Execute controlled R_A definition completion.",
            "4. Execute controlled Traj_A definition completion.",
            "5. Integrate completed dependent-object definitions into a bundle only after all six completions exist.",
            "6. Plan theorem candidates only after the dependent-object completion bundle exists.",
        ]
    )


def build_report(source_text: str) -> CompletionResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.150 — Controlled C_reg Definition Completion Execution

        ## Question

        Can Viruse Fabric execute the second controlled dependent-object definition completion by completing `C_reg` after official v8.149 Adm_A definition completion, while keeping Pi_obs, M_c, R_A, Traj_A, all-dependent-object completion, bundle integration, full formalization, theorem candidate planning, theorem proof, proof assistant verification, validation, manuscript readiness, readiness approval, and new citations at zero?

        ## Source artifact

        - `outputs/controlled_adm_a_definition_completion_execution_v8_149.md`

        ## Execution interpretation

        v8.150 executes one controlled dependent-object definition completion.

        The newly completed object is `C_reg`.

        The previously completed dependent object `Adm_A` remains completed.

        This is an execution milestone, not a planning milestone and not an audit milestone.

        {_definition_block()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone completes exactly one additional dependent-object definition: `C_reg`.

        This milestone preserves completed `Adm_A`.

        This milestone does not complete `Pi_obs`.

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

        The project has executed one controlled C_reg definition completion and records Adm_A and C_reg as two completed dependent-object definitions while keeping Pi_obs, M_c, R_A, Traj_A, all-dependent-object completion, dependent-object bundle integration, full formalization completion, theorem candidate planning, theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_phrases = [
        "This milestone completes `Pi_obs`",
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
    ]
    boundary_phrase_count = sum(report.lower().count(item.lower()) for item in boundary_keywords)

    warnings = [
        "This milestone completes C_reg only as the second completed dependent object.",
        "Pi_obs, M_c, R_A, and Traj_A remain uncompleted.",
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
