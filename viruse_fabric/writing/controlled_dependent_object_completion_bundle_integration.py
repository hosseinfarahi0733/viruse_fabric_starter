from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTERS = {
    "controlled_dependent_object_completion_bundle_integration_count": 1,
    "new_controlled_dependent_object_completion_bundle_integration_count": 1,
    "dependent_object_completion_bundle_integration_count": 1,
    "integrated_dependent_object_completion_bundle_count": 1,
    "completed_dependent_object_completion_bundle_count": 1,

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

    "imported_controlled_traj_a_definition_completion_execution_count": 1,
    "imported_completed_adm_a_definition_count": 1,
    "imported_completed_c_reg_definition_count": 1,
    "imported_completed_pi_obs_definition_count": 1,
    "imported_completed_m_c_definition_count": 1,
    "imported_completed_r_a_definition_count": 1,
    "imported_completed_traj_a_definition_count": 1,
    "imported_dependent_object_definition_completion_count": 6,
    "imported_completed_dependent_object_definition_count": 6,
    "imported_all_dependent_object_definition_completion_count": 1,
    "imported_completed_sigma_a_definition_count": 1,
    "imported_completed_formal_definition_count": 1,

    "full_dependency_closure_audit_count": 0,
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
    "controlled_dependent_object_completion_bundle_integration_count": "Controlled dependent-object completion bundle integration count",
    "new_controlled_dependent_object_completion_bundle_integration_count": "New controlled dependent-object completion bundle integration count",
    "dependent_object_completion_bundle_integration_count": "Dependent-object completion bundle integration count",
    "integrated_dependent_object_completion_bundle_count": "Integrated dependent-object completion bundle count",
    "completed_dependent_object_completion_bundle_count": "Completed dependent-object completion bundle count",

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

    "imported_controlled_traj_a_definition_completion_execution_count": "Imported controlled Traj_A definition completion execution count",
    "imported_completed_adm_a_definition_count": "Imported completed Adm_A definition count",
    "imported_completed_c_reg_definition_count": "Imported completed C_reg definition count",
    "imported_completed_pi_obs_definition_count": "Imported completed Pi_obs definition count",
    "imported_completed_m_c_definition_count": "Imported completed M_c definition count",
    "imported_completed_r_a_definition_count": "Imported completed R_A definition count",
    "imported_completed_traj_a_definition_count": "Imported completed Traj_A definition count",
    "imported_dependent_object_definition_completion_count": "Imported dependent-object definition completion count",
    "imported_completed_dependent_object_definition_count": "Imported completed dependent-object definition count",
    "imported_all_dependent_object_definition_completion_count": "Imported all dependent-object definition completion count",
    "imported_completed_sigma_a_definition_count": "Imported completed Sigma_A definition count",
    "imported_completed_formal_definition_count": "Imported completed formal definition count",

    "full_dependency_closure_audit_count": "Full dependency closure audit count",
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
    "Controlled Traj_A definition completion execution count: 1",
    "New controlled Traj_A definition completion execution count: 1",
    "Traj_A definition completion execution count: 1",
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
    "Traj_A definition completion count: 1",
    "Completed Traj_A definition count: 1",
    "Dependent-object definition completion count: 6",
    "Completed dependent-object definition count: 6",
    "All dependent-object definition completion count: 1",
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
    "Controlled dependent-object completion bundle integration count: 1",
    "New controlled dependent-object completion bundle integration count: 1",
    "Dependent-object completion bundle integration count: 1",
    "Integrated dependent-object completion bundle count: 1",
    "Completed dependent-object completion bundle count: 1",

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

    "Imported controlled Traj_A definition completion execution count: 1",
    "Imported completed Adm_A definition count: 1",
    "Imported completed C_reg definition count: 1",
    "Imported completed Pi_obs definition count: 1",
    "Imported completed M_c definition count: 1",
    "Imported completed R_A definition count: 1",
    "Imported completed Traj_A definition count: 1",
    "Imported dependent-object definition completion count: 6",
    "Imported completed dependent-object definition count: 6",
    "Imported all dependent-object definition completion count: 1",
    "Imported completed Sigma_A definition count: 1",
    "Imported completed formal definition count: 1",

    "Full dependency closure audit count: 0",
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
class IntegrationResult:
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


def _bundle_block() -> str:
    return dedent(
        """
        ## Integrated dependent-object completion bundle

        Let `Sigma_A` denote the completed formal definition object imported from v8.147.

        Let the completed dependent-object definitions be:

        - `Adm_A`
        - `C_reg`
        - `Pi_obs`
        - `M_c`
        - `R_A`
        - `Traj_A`

        v8.155 integrates these six completed dependent-object definitions into the controlled bundle:

        `B_dep_A = (Adm_A, C_reg, Pi_obs, M_c, R_A, Traj_A ; Sigma_A)`

        ### Bundle membership conditions

        `B_dep_A` is a valid completed dependent-object bundle iff all of the following controlled conditions hold:

        1. `Sigma_A` is recorded as a completed formal definition object.
        2. `Adm_A` is recorded as a completed dependent-object definition.
        3. `C_reg` is recorded as a completed dependent-object definition.
        4. `Pi_obs` is recorded as a completed dependent-object definition.
        5. `M_c` is recorded as a completed dependent-object definition.
        6. `R_A` is recorded as a completed dependent-object definition.
        7. `Traj_A` is recorded as a completed dependent-object definition.
        8. The dependency order is preserved:
           `Sigma_A -> Adm_A -> C_reg -> Pi_obs -> M_c -> R_A -> Traj_A`.
        9. The bundle records dependency compatibility without claiming theorem-level closure.
        10. The bundle remains eligible for later dependency closure audit and theorem candidate planning.

        ### Integration boundary

        This milestone integrates the completed dependent-object definitions into one controlled completion bundle.

        It does not run a full dependency closure audit.

        It does not complete full formalization.

        It does not create theorem candidates.

        It does not prove new theorems.

        It does not provide proof assistant verification.

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
            "1. Run one full dependency closure boundary audit, only if needed, over the integrated bundle.",
            "2. Plan theorem candidates only after dependency closure is accepted.",
            "3. Keep proof, validation, manuscript readiness, and citation work out of this milestone.",
        ]
    )


def build_report(source_text: str) -> IntegrationResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.155 — Controlled Dependent-object Completion Bundle Integration

        ## Question

        Can Viruse Fabric integrate the six completed dependent-object definitions into one controlled dependent-object completion bundle after official v8.154 Traj_A completion, while keeping full dependency closure audit, full formalization, theorem candidate planning, theorem proof, proof assistant verification, validation, manuscript readiness, readiness approval, and new citations at zero?

        ## Source artifact

        - `outputs/controlled_traj_a_definition_completion_execution_v8_154.md`

        ## Integration interpretation

        v8.155 integrates six already-completed dependent-object definitions.

        This milestone is not a new dependent-object definition completion.

        This milestone is not a theorem candidate plan.

        This milestone is not a proof milestone.

        This milestone is not a validation milestone.

        {_bundle_block()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone integrates the completed dependent-object definitions into one controlled completion bundle.

        This milestone preserves completed `Adm_A`.

        This milestone preserves completed `C_reg`.

        This milestone preserves completed `Pi_obs`.

        This milestone preserves completed `M_c`.

        This milestone preserves completed `R_A`.

        This milestone preserves completed `Traj_A`.

        This milestone does not run a full dependency closure audit.

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

        The project has integrated the six completed dependent-object definitions into one controlled dependent-object completion bundle while keeping full dependency closure audit, full formalization completion, theorem candidate planning, theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_phrases = [
        "This milestone runs a full dependency closure audit",
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
        "does not run",
        "does not complete full formalization",
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
        "This milestone integrates the completed dependent-object bundle only.",
        "Full dependency closure audit remains unexecuted.",
        "Full formalization remains incomplete.",
        "Theorem, proof, validation, readiness approval, and citation claims remain absent.",
    ]

    return IntegrationResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> IntegrationResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
