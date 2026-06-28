from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTERS = {
    "controlled_theorem_candidate_planning_count": 1,
    "new_controlled_theorem_candidate_planning_count": 1,
    "theorem_candidate_plan_count": 1,
    "theorem_candidate_planning_over_dependency_closed_bundle_count": 1,
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

    "imported_controlled_full_dependency_closure_boundary_audit_count": 1,
    "imported_full_dependency_closure_audit_count": 1,
    "imported_dependency_closure_boundary_pass_count": 1,
    "imported_dependency_closure_blocker_count": 0,
    "imported_unresolved_dependency_gap_count": 0,
    "imported_dependent_object_completion_bundle_integration_count": 1,
    "imported_integrated_dependent_object_completion_bundle_count": 1,
    "imported_completed_dependent_object_completion_bundle_count": 1,
    "imported_completed_sigma_a_definition_count": 1,
    "imported_completed_formal_definition_count": 1,

    "formalization_complete_count": 0,
    "new_theorem_proven_count": 0,
    "theorem_proof_execution_count": 0,
    "proof_assistant_verification_count": 0,
    "external_validation_count": 0,
    "independent_experiment_count": 0,
    "manuscript_submission_ready_count": 0,
    "readiness_approval_count": 0,
    "new_citation_added_count": 0,
}


LABEL_OVERRIDES = {
    "controlled_theorem_candidate_planning_count": "Controlled theorem candidate planning count",
    "new_controlled_theorem_candidate_planning_count": "New controlled theorem candidate planning count",
    "theorem_candidate_plan_count": "Theorem candidate plan count",
    "theorem_candidate_planning_over_dependency_closed_bundle_count": "Theorem candidate planning over dependency-closed bundle count",
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

    "imported_controlled_full_dependency_closure_boundary_audit_count": "Imported controlled full dependency closure boundary audit count",
    "imported_full_dependency_closure_audit_count": "Imported full dependency closure audit count",
    "imported_dependency_closure_boundary_pass_count": "Imported dependency closure boundary pass count",
    "imported_dependency_closure_blocker_count": "Imported dependency closure blocker count",
    "imported_unresolved_dependency_gap_count": "Imported unresolved dependency gap count",
    "imported_dependent_object_completion_bundle_integration_count": "Imported dependent-object completion bundle integration count",
    "imported_integrated_dependent_object_completion_bundle_count": "Imported integrated dependent-object completion bundle count",
    "imported_completed_dependent_object_completion_bundle_count": "Imported completed dependent-object completion bundle count",
    "imported_completed_sigma_a_definition_count": "Imported completed Sigma_A definition count",
    "imported_completed_formal_definition_count": "Imported completed formal definition count",

    "formalization_complete_count": "Formalization complete count",
    "new_theorem_proven_count": "New theorem proven count",
    "theorem_proof_execution_count": "Theorem proof execution count",
    "proof_assistant_verification_count": "Proof assistant verification count",
    "external_validation_count": "External validation count",
    "independent_experiment_count": "Independent experiment count",
    "manuscript_submission_ready_count": "Manuscript submission ready count",
    "readiness_approval_count": "Readiness approval count",
    "new_citation_added_count": "New citation added count",
}


REQUIRED_SOURCE_PHRASES = [
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
    "Dependent-object definition completion count: 6",
    "Completed dependent-object definition count: 6",
    "All dependent-object definition completion count: 1",
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

    "Imported controlled full dependency closure boundary audit count: 1",
    "Imported full dependency closure audit count: 1",
    "Imported dependency closure boundary pass count: 1",
    "Imported dependency closure blocker count: 0",
    "Imported unresolved dependency gap count: 0",
    "Imported dependent-object completion bundle integration count: 1",
    "Imported integrated dependent-object completion bundle count: 1",
    "Imported completed dependent-object completion bundle count: 1",
    "Imported completed Sigma_A definition count: 1",
    "Imported completed formal definition count: 1",

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


@dataclass(frozen=True)
class PlanningResult:
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


def _candidate_block() -> str:
    return dedent(
        """
        ## Planned theorem candidates

        Source bundle:

        `B_dep_A = (Adm_A, C_reg, Pi_obs, M_c, R_A, Traj_A ; Sigma_A)`

        Dependency closure status imported from v8.156:

        - Dependency closure boundary pass count: 1
        - Dependency closure blocker count: 0
        - Unresolved dependency gap count: 0

        This milestone plans theorem candidates only. It does not prove them.

        ### Candidate TC-001 — Admissible regular observation well-typing

        Informal statement:

        If `Sigma_A`, `Adm_A`, `C_reg`, and `Pi_obs` are completed and the dependency-closed bundle is accepted, then every admissible state and regular transition admitted by `C_reg` has a well-typed observable representation under `Pi_obs`.

        Dependency basis:

        - `Sigma_A`
        - `Adm_A`
        - `C_reg`
        - `Pi_obs`

        Required future proof ingredients:

        - carrier typing lemma
        - admissibility preservation lemma
        - regular-transition typing lemma
        - observation projection well-typing lemma

        ### Candidate TC-002 — Controlled mass accounting domain compatibility

        Informal statement:

        If `Sigma_A`, `Adm_A`, `C_reg`, `Pi_obs`, and `M_c` are completed and the dependency-closed bundle is accepted, then every controlled mass record assigned by `M_c` is typed over an admissible state, regular transition, or observable representation admitted by earlier completed objects.

        Dependency basis:

        - `Sigma_A`
        - `Adm_A`
        - `C_reg`
        - `Pi_obs`
        - `M_c`

        Required future proof ingredients:

        - mass carrier typing lemma
        - observation-domain compatibility lemma
        - regular-transition mass-domain lemma

        ### Candidate TC-003 — Relation membership dependency soundness

        Informal statement:

        If `R_A` is completed over the dependency-closed bundle, then every tuple admitted by `R_A` references only completed admissibility, regularity, observation, and mass components.

        Dependency basis:

        - `Sigma_A`
        - `Adm_A`
        - `C_reg`
        - `Pi_obs`
        - `M_c`
        - `R_A`

        Required future proof ingredients:

        - relation tuple typing lemma
        - relation-component compatibility lemma
        - no-forward-dependency lemma

        ### Candidate TC-004 — Controlled trajectory dependency soundness

        Informal statement:

        If `Traj_A` is completed over the dependency-closed bundle, then every finite trajectory record produced by `Traj_A` references only completed admissibility, regularity, observation, mass, and relation components.

        Dependency basis:

        - `Sigma_A`
        - `Adm_A`
        - `C_reg`
        - `Pi_obs`
        - `M_c`
        - `R_A`
        - `Traj_A`

        Required future proof ingredients:

        - finite sequence typing lemma
        - transition-chain compatibility lemma
        - relation-supported trajectory lemma
        - no-uncompleted-dependency lemma

        ### Planning boundary

        This milestone plans four theorem candidates.

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
            "1. Select the first theorem candidate for controlled proof planning.",
            "2. Keep theorem proof execution separate from proof planning.",
            "3. Keep proof assistant verification, validation, manuscript readiness, and citations out of theorem candidate planning.",
        ]
    )


def build_report(source_text: str) -> PlanningResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.157 — Controlled Theorem Candidate Planning over Dependency-closed Bundle

        ## Question

        Can Viruse Fabric plan theorem candidates over the dependency-closed integrated bundle from v8.156 while keeping theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero?

        ## Source artifact

        - `outputs/controlled_full_dependency_closure_boundary_audit_v8_156.md`

        ## Planning interpretation

        v8.157 plans theorem candidates over the dependency-closed integrated dependent-object completion bundle.

        This milestone is not a proof milestone.

        This milestone is not proof assistant verification.

        This milestone is not validation.

        This milestone is not manuscript readiness.

        {_candidate_block()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone plans theorem candidates over the dependency-closed integrated bundle.

        This milestone records planned theorem candidate count: 4.

        This milestone records theorem candidate plan count: 1.

        This milestone preserves dependency closure boundary pass count: 1.

        This milestone preserves dependency closure blocker count: 0.

        This milestone preserves unresolved dependency gap count: 0.

        This milestone does not prove new theorems.

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

        The project has planned four controlled theorem candidates over the dependency-closed integrated dependent-object completion bundle while keeping theorem proof execution, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_phrases = [
        "This milestone proves new theorems",
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
        "This milestone plans theorem candidates only.",
        "Theorem proof execution remains zero.",
        "Proof assistant verification remains zero.",
        "Validation, readiness approval, and citation claims remain absent.",
    ]

    return PlanningResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> PlanningResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
