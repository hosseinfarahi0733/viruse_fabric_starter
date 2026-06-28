from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTERS = {
    "controlled_adm_a_definition_completion_execution_count": 1,
    "new_controlled_adm_a_definition_completion_execution_count": 1,
    "adm_a_definition_completion_execution_count": 1,
    "dependent_object_definition_completion_execution_count": 1,
    "definition_completion_execution_count": 1,
    "completion_execution_count": 1,
    "definition_execution_count": 1,
    "new_definition_execution_count": 1,

    "adm_a_definition_completion_count": 1,
    "completed_adm_a_definition_count": 1,
    "dependent_object_definition_completion_count": 1,
    "completed_dependent_object_definition_count": 1,

    "imported_dependent_object_definition_completion_planning_count": 1,
    "imported_planned_dependent_object_count": 6,
    "imported_completed_sigma_a_definition_count": 1,
    "imported_completed_formal_definition_count": 1,

    "c_reg_definition_completion_count": 0,
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
    "controlled_adm_a_definition_completion_execution_count": "Controlled Adm_A definition completion execution count",
    "new_controlled_adm_a_definition_completion_execution_count": "New controlled Adm_A definition completion execution count",
    "adm_a_definition_completion_execution_count": "Adm_A definition completion execution count",
    "dependent_object_definition_completion_execution_count": "Dependent-object definition completion execution count",
    "definition_completion_execution_count": "Definition completion execution count",
    "completion_execution_count": "Completion execution count",
    "definition_execution_count": "Definition execution count",
    "new_definition_execution_count": "New definition execution count",

    "adm_a_definition_completion_count": "Adm_A definition completion count",
    "completed_adm_a_definition_count": "Completed Adm_A definition count",
    "dependent_object_definition_completion_count": "Dependent-object definition completion count",
    "completed_dependent_object_definition_count": "Completed dependent-object definition count",

    "imported_dependent_object_definition_completion_planning_count": "Imported dependent-object definition completion planning count",
    "imported_planned_dependent_object_count": "Imported planned dependent-object count",
    "imported_completed_sigma_a_definition_count": "Imported completed Sigma_A definition count",
    "imported_completed_formal_definition_count": "Imported completed formal definition count",

    "c_reg_definition_completion_count": "C_reg definition completion count",
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
    "Dependent-object definition completion planning count: 1",
    "New dependent-object definition completion planning count: 1",
    "Dependent-object completion plan count: 1",
    "Dependent-object completion planning row count: 6",
    "Planned dependent-object count: 6",
    "Planned Adm_A definition completion count: 1",
    "Planned C_reg definition completion count: 1",
    "Planned Pi_obs definition completion count: 1",
    "Planned M_c definition completion count: 1",
    "Planned R_A definition completion count: 1",
    "Planned Traj_A definition completion count: 1",
    "Imported completed Sigma_A definition count: 1",
    "Imported completed formal definition count: 1",
    "Dependent-object definition completion count: 0",
    "Adm_A definition completion count: 0",
    "C_reg definition completion count: 0",
    "Pi_obs definition completion count: 0",
    "M_c definition completion count: 0",
    "R_A definition completion count: 0",
    "Traj_A definition completion count: 0",
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
    "Controlled Adm_A definition completion execution count: 1",
    "New controlled Adm_A definition completion execution count: 1",
    "Adm_A definition completion execution count: 1",
    "Dependent-object definition completion execution count: 1",
    "Definition completion execution count: 1",
    "Completion execution count: 1",
    "Definition execution count: 1",
    "New definition execution count: 1",

    "Adm_A definition completion count: 1",
    "Completed Adm_A definition count: 1",
    "Dependent-object definition completion count: 1",
    "Completed dependent-object definition count: 1",

    "Imported dependent-object definition completion planning count: 1",
    "Imported planned dependent-object count: 6",
    "Imported completed Sigma_A definition count: 1",
    "Imported completed formal definition count: 1",

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
        ## Completed formal definition: Adm_A

        Let `Sigma_A` denote the completed formal definition object imported from v8.147.

        `Adm_A` is the A-indexed admissibility object that filters candidate structural states before they may participate in regularity, observation, causal mass, relation, or trajectory construction.

        ### Signature

        `Adm_A : X_A -> {admissible, rejected}`

        where `X_A` is the candidate A-indexed state carrier inherited through completed `Sigma_A`.

        ### Predicate form

        For a candidate state `x in X_A`:

        `Adm_A(x) = admissible`

        iff all of the following controlled conditions hold:

        1. `x` is typed over the completed `Sigma_A` carrier.
        2. `x` preserves the A-indexed structural scope declared by `Sigma_A`.
        3. `x` respects the time-index compatibility boundary of `Sigma_A`.
        4. `x` does not violate the local admissibility exclusions inherited from the dependent-object draft bundle.
        5. `x` remains eligible for later `C_reg`, `Pi_obs`, `M_c`, `R_A`, and `Traj_A` completion without implying that those objects are already complete.

        Otherwise:

        `Adm_A(x) = rejected`

        ### Completion boundary

        This definition completes `Adm_A` only.

        It does not complete `C_reg`.

        It does not complete `Pi_obs`.

        It does not complete `M_c`.

        It does not complete `R_A`.

        It does not complete `Traj_A`.

        It does not complete the dependent-object bundle.

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
            "1. Execute controlled C_reg definition completion.",
            "2. Execute controlled Pi_obs definition completion.",
            "3. Execute controlled M_c definition completion.",
            "4. Execute controlled R_A definition completion.",
            "5. Execute controlled Traj_A definition completion.",
            "6. Integrate completed dependent-object definitions into a bundle only after all six completions exist.",
            "7. Plan theorem candidates only after the dependent-object completion bundle exists.",
        ]
    )


def build_report(source_text: str) -> CompletionResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.149 — Controlled Adm_A Definition Completion Execution

        ## Question

        Can Viruse Fabric execute the first controlled dependent-object definition completion by completing `Adm_A` after official v8.148 dependent-object definition completion planning, while keeping the remaining dependent-object completions, full formalization, theorem candidate planning, theorem proof, proof assistant verification, validation, manuscript readiness, readiness approval, and new citations at zero?

        ## Source artifact

        - `outputs/dependent_object_definition_completion_planning_v8_148.md`

        ## Execution interpretation

        v8.149 executes one controlled dependent-object definition completion.

        The completed object is `Adm_A`.

        This is an execution milestone, not a planning milestone and not an audit milestone.

        {_definition_block()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone completes exactly one dependent-object definition: `Adm_A`.

        This milestone does not complete `C_reg`.

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

        The project has executed one controlled Adm_A definition completion and recorded Adm_A as one completed dependent-object definition while keeping C_reg, Pi_obs, M_c, R_A, Traj_A, all-dependent-object completion, dependent-object bundle integration, full formalization completion, theorem candidate planning, theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_phrases = [
        "This milestone completes `C_reg`",
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
        "This milestone completes Adm_A only.",
        "C_reg, Pi_obs, M_c, R_A, and Traj_A remain uncompleted.",
        "Full formalization remains incomplete.",
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
