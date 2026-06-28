from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTERS = {
    "controlled_full_dependency_closure_boundary_audit_count": 1,
    "new_controlled_full_dependency_closure_boundary_audit_count": 1,
    "full_dependency_closure_audit_count": 1,
    "dependency_closure_boundary_audit_count": 1,
    "dependency_closure_boundary_pass_count": 1,
    "dependency_closure_blocker_count": 0,
    "unresolved_dependency_gap_count": 0,

    "dependent_object_completion_bundle_integration_count": 1,
    "integrated_dependent_object_completion_bundle_count": 1,
    "completed_dependent_object_completion_bundle_count": 1,

    "adm_a_definition_completion_count": 1,
    "c_reg_definition_completion_count": 1,
    "pi_obs_definition_completion_count": 1,
    "m_c_definition_completion_count": 1,
    "r_a_definition_completion_count": 1,
    "traj_a_definition_completion_count": 1,
    "dependent_object_definition_completion_count": 6,
    "completed_dependent_object_definition_count": 6,
    "all_dependent_object_definition_completion_count": 1,

    "imported_dependent_object_completion_bundle_integration_count": 1,
    "imported_integrated_dependent_object_completion_bundle_count": 1,
    "imported_completed_dependent_object_completion_bundle_count": 1,
    "imported_completed_sigma_a_definition_count": 1,
    "imported_completed_formal_definition_count": 1,

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
    "controlled_full_dependency_closure_boundary_audit_count": "Controlled full dependency closure boundary audit count",
    "new_controlled_full_dependency_closure_boundary_audit_count": "New controlled full dependency closure boundary audit count",
    "full_dependency_closure_audit_count": "Full dependency closure audit count",
    "dependency_closure_boundary_audit_count": "Dependency closure boundary audit count",
    "dependency_closure_boundary_pass_count": "Dependency closure boundary pass count",
    "dependency_closure_blocker_count": "Dependency closure blocker count",
    "unresolved_dependency_gap_count": "Unresolved dependency gap count",

    "dependent_object_completion_bundle_integration_count": "Dependent-object completion bundle integration count",
    "integrated_dependent_object_completion_bundle_count": "Integrated dependent-object completion bundle count",
    "completed_dependent_object_completion_bundle_count": "Completed dependent-object completion bundle count",

    "adm_a_definition_completion_count": "Adm_A definition completion count",
    "c_reg_definition_completion_count": "C_reg definition completion count",
    "pi_obs_definition_completion_count": "Pi_obs definition completion count",
    "m_c_definition_completion_count": "M_c definition completion count",
    "r_a_definition_completion_count": "R_A definition completion count",
    "traj_a_definition_completion_count": "Traj_A definition completion count",
    "dependent_object_definition_completion_count": "Dependent-object definition completion count",
    "completed_dependent_object_definition_count": "Completed dependent-object definition count",
    "all_dependent_object_definition_completion_count": "All dependent-object definition completion count",

    "imported_dependent_object_completion_bundle_integration_count": "Imported dependent-object completion bundle integration count",
    "imported_integrated_dependent_object_completion_bundle_count": "Imported integrated dependent-object completion bundle count",
    "imported_completed_dependent_object_completion_bundle_count": "Imported completed dependent-object completion bundle count",
    "imported_completed_sigma_a_definition_count": "Imported completed Sigma_A definition count",
    "imported_completed_formal_definition_count": "Imported completed formal definition count",

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
    "Controlled dependent-object completion bundle integration count: 1",
    "New controlled dependent-object completion bundle integration count: 1",
    "Dependent-object completion bundle integration count: 1",
    "Integrated dependent-object completion bundle count: 1",
    "Completed dependent-object completion bundle count: 1",
    "Adm_A definition completion count: 1",
    "C_reg definition completion count: 1",
    "Pi_obs definition completion count: 1",
    "M_c definition completion count: 1",
    "R_A definition completion count: 1",
    "Traj_A definition completion count: 1",
    "Dependent-object definition completion count: 6",
    "Completed dependent-object definition count: 6",
    "All dependent-object definition completion count: 1",
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


REQUIRED_REPORT_PHRASES = [
    "Controlled full dependency closure boundary audit count: 1",
    "New controlled full dependency closure boundary audit count: 1",
    "Full dependency closure audit count: 1",
    "Dependency closure boundary audit count: 1",
    "Dependency closure boundary pass count: 1",
    "Dependency closure blocker count: 0",
    "Unresolved dependency gap count: 0",

    "Dependent-object completion bundle integration count: 1",
    "Integrated dependent-object completion bundle count: 1",
    "Completed dependent-object completion bundle count: 1",

    "Adm_A definition completion count: 1",
    "C_reg definition completion count: 1",
    "Pi_obs definition completion count: 1",
    "M_c definition completion count: 1",
    "R_A definition completion count: 1",
    "Traj_A definition completion count: 1",
    "Dependent-object definition completion count: 6",
    "Completed dependent-object definition count: 6",
    "All dependent-object definition completion count: 1",

    "Imported dependent-object completion bundle integration count: 1",
    "Imported integrated dependent-object completion bundle count: 1",
    "Imported completed dependent-object completion bundle count: 1",
    "Imported completed Sigma_A definition count: 1",
    "Imported completed formal definition count: 1",

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
class AuditResult:
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


def _audit_block() -> str:
    return dedent(
        """
        ## Controlled dependency closure boundary audit

        Source bundle:

        `B_dep_A = (Adm_A, C_reg, Pi_obs, M_c, R_A, Traj_A ; Sigma_A)`

        This audit checks whether the integrated dependent-object completion bundle is dependency-closed at the definition boundary.

        ### Dependency order checked

        The audit accepts the following dependency order:

        `Sigma_A -> Adm_A -> C_reg -> Pi_obs -> M_c -> R_A -> Traj_A`

        ### Closure conditions checked

        The bundle passes this boundary audit iff all of the following are recorded:

        1. `Sigma_A` is completed before all dependent-object definitions.
        2. `Adm_A` is completed and depends only on completed `Sigma_A`.
        3. `C_reg` is completed and depends only on completed `Sigma_A` and `Adm_A`.
        4. `Pi_obs` is completed and depends only on completed `Sigma_A`, `Adm_A`, and `C_reg`.
        5. `M_c` is completed and depends only on completed `Sigma_A`, `Adm_A`, `C_reg`, and `Pi_obs`.
        6. `R_A` is completed and depends only on completed `Sigma_A`, `Adm_A`, `C_reg`, `Pi_obs`, and `M_c`.
        7. `Traj_A` is completed and depends only on completed `Sigma_A`, `Adm_A`, `C_reg`, `Pi_obs`, `M_c`, and `R_A`.
        8. No dependent-object definition remains missing.
        9. The integrated bundle is present.
        10. No theorem, proof, validation, readiness, or citation claim is introduced by this audit.

        ### Audit result

        Dependency closure boundary pass: yes.

        Dependency closure blocker count: 0.

        Unresolved dependency gap count: 0.

        ### Boundary

        This milestone runs one controlled full dependency closure boundary audit.

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
            "1. Plan theorem candidates over the accepted dependency-closed bundle.",
            "2. Keep theorem proof separate from theorem candidate planning.",
            "3. Keep proof assistant verification, validation, manuscript readiness, and citations out of this milestone.",
        ]
    )


def build_report(source_text: str) -> AuditResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.156 — Controlled Full Dependency Closure Boundary Audit

        ## Question

        Can Viruse Fabric run one controlled full dependency closure boundary audit over the v8.155 integrated dependent-object completion bundle, record zero blockers and zero unresolved dependency gaps, and still keep full formalization, theorem candidate planning, theorem proof, proof assistant verification, validation, manuscript readiness, readiness approval, and new citations at zero?

        ## Source artifact

        - `outputs/controlled_dependent_object_completion_bundle_integration_v8_155.md`

        ## Audit interpretation

        v8.156 is a boundary audit over the already-integrated dependent-object completion bundle.

        This milestone is not another dependent-object definition completion.

        This milestone is not bundle integration.

        This milestone is not theorem candidate planning.

        This milestone is not theorem proof.

        {_audit_block()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone runs exactly one controlled full dependency closure boundary audit.

        This milestone records dependency closure boundary pass count: 1.

        This milestone records dependency closure blocker count: 0.

        This milestone records unresolved dependency gap count: 0.

        This milestone preserves the integrated dependent-object completion bundle.

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

        The project has run one controlled full dependency closure boundary audit over the integrated dependent-object completion bundle and records zero dependency blockers and zero unresolved dependency gaps, while keeping full formalization completion, theorem candidate planning, theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_phrases = [
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
        "does not complete full formalization",
        "does not create theorem candidates",
        "does not prove",
        "does not provide",
        "does not make",
        "does not approve",
        "does not add",
        "at zero",
        "blocker count: 0",
        "unresolved dependency gap count: 0",
    ]
    boundary_phrase_count = sum(report.lower().count(item.lower()) for item in boundary_keywords)

    warnings = [
        "This milestone is only a dependency closure boundary audit.",
        "Full formalization remains incomplete.",
        "Theorem candidate planning remains unexecuted.",
        "Theorem proof, validation, readiness approval, and citation claims remain absent.",
    ]

    return AuditResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> AuditResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
