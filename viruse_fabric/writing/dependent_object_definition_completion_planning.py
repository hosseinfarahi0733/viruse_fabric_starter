from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


DEPENDENT_OBJECTS = [
    {
        "name": "Adm_A",
        "role": "admissibility operator for candidate A-indexed structural states",
        "completion_target": "turn draft admissibility constraints into a closed formal definition with explicit domain, codomain, admissibility predicate, failure boundary, and dependency on Sigma_A",
        "must_preserve_zero": "must not claim theorem proof, validation, or full formalization",
    },
    {
        "name": "C_reg",
        "role": "regularity constraint family governing controlled admissible transitions",
        "completion_target": "turn draft regularity clauses into a closed formal definition with regularity predicate, scope, excluded cases, and dependency on completed Sigma_A",
        "must_preserve_zero": "must not claim proof assistant verification or external validation",
    },
    {
        "name": "Pi_obs",
        "role": "observation projection object for accessible traces and observable evidence",
        "completion_target": "turn draft observation projection into a closed formal definition with input space, output space, projection semantics, loss boundary, and dependency on Sigma_A",
        "must_preserve_zero": "must not claim empirical validation or manuscript readiness",
    },
    {
        "name": "M_c",
        "role": "controlled causal mass object used for structured mass accounting",
        "completion_target": "turn draft causal mass accounting into a closed formal definition with carrier, measure-like accounting rule, conservation/exclusion boundary, and dependency on Sigma_A",
        "must_preserve_zero": "must not claim new theorem proof from mass accounting",
    },
    {
        "name": "R_A",
        "role": "A-indexed relation object connecting admissible states, observations, and transitions",
        "completion_target": "turn draft relation clauses into a closed formal definition with relation signature, admissible pairs, failure cases, and dependency on Sigma_A plus dependent objects",
        "must_preserve_zero": "must not claim closure of the entire framework",
    },
    {
        "name": "Traj_A",
        "role": "A-indexed trajectory object for admissible time-indexed paths",
        "completion_target": "turn draft trajectory shell into a closed formal definition with temporal indexing, transition compatibility, observation compatibility, and dependency on Sigma_A",
        "must_preserve_zero": "must not claim proof, validation, or readiness",
    },
]


COUNTERS = {
    "dependent_object_definition_completion_planning_count": 1,
    "new_dependent_object_definition_completion_planning_count": 1,
    "dependent_object_completion_plan_count": 1,
    "dependent_object_completion_planning_row_count": 6,
    "planned_dependent_object_count": 6,
    "planned_adm_a_definition_completion_count": 1,
    "planned_c_reg_definition_completion_count": 1,
    "planned_pi_obs_definition_completion_count": 1,
    "planned_m_c_definition_completion_count": 1,
    "planned_r_a_definition_completion_count": 1,
    "planned_traj_a_definition_completion_count": 1,
    "imported_completed_sigma_a_definition_count": 1,
    "imported_completed_formal_definition_count": 1,

    "dependent_object_definition_completion_count": 0,
    "adm_a_definition_completion_count": 0,
    "c_reg_definition_completion_count": 0,
    "pi_obs_definition_completion_count": 0,
    "m_c_definition_completion_count": 0,
    "r_a_definition_completion_count": 0,
    "traj_a_definition_completion_count": 0,
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
    "dependent_object_definition_completion_planning_count": "Dependent-object definition completion planning count",
    "new_dependent_object_definition_completion_planning_count": "New dependent-object definition completion planning count",
    "dependent_object_completion_plan_count": "Dependent-object completion plan count",
    "dependent_object_completion_planning_row_count": "Dependent-object completion planning row count",
    "planned_dependent_object_count": "Planned dependent-object count",

    "planned_adm_a_definition_completion_count": "Planned Adm_A definition completion count",
    "planned_c_reg_definition_completion_count": "Planned C_reg definition completion count",
    "planned_pi_obs_definition_completion_count": "Planned Pi_obs definition completion count",
    "planned_m_c_definition_completion_count": "Planned M_c definition completion count",
    "planned_r_a_definition_completion_count": "Planned R_A definition completion count",
    "planned_traj_a_definition_completion_count": "Planned Traj_A definition completion count",

    "imported_completed_sigma_a_definition_count": "Imported completed Sigma_A definition count",
    "imported_completed_formal_definition_count": "Imported completed formal definition count",

    "dependent_object_definition_completion_count": "Dependent-object definition completion count",
    "adm_a_definition_completion_count": "Adm_A definition completion count",
    "c_reg_definition_completion_count": "C_reg definition completion count",
    "pi_obs_definition_completion_count": "Pi_obs definition completion count",
    "m_c_definition_completion_count": "M_c definition completion count",
    "r_a_definition_completion_count": "R_A definition completion count",
    "traj_a_definition_completion_count": "Traj_A definition completion count",

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
    "Controlled Sigma_A definition completion execution count: 1",
    "Sigma_A definition completion execution count: 1",
    "Completed Sigma_A definition count: 1",
    "Completed formal definition count: 1",
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


PROHIBITED_BEHAVIOR_PHRASES = [
    "this milestone completes Adm_A",
    "this milestone completes C_reg",
    "this milestone completes Pi_obs",
    "this milestone completes M_c",
    "this milestone completes R_A",
    "this milestone completes Traj_A",
    "this milestone completes all dependent objects",
    "this milestone completes full formalization",
    "this milestone proves",
    "proof assistant verified",
    "externally validated",
    "manuscript is ready",
    "readiness approved",
    "new citations added",
]


@dataclass(frozen=True)
class PlanResult:
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


def _planning_table() -> str:
    lines = [
        "| Object | Current status | v8.148 planning target | Completion gate | Boundary preserved |",
        "|---|---:|---|---|---|",
    ]
    for item in DEPENDENT_OBJECTS:
        lines.append(
            f"| `{item['name']}` | draft exists, completion count remains 0 | "
            f"{item['completion_target']} | future execution only | {item['must_preserve_zero']} |"
        )
    return "\n".join(lines)


def _next_steps() -> str:
    return "\n".join(
        [
            "1. Execute Adm_A definition completion in a controlled milestone.",
            "2. Execute C_reg definition completion in a controlled milestone.",
            "3. Execute Pi_obs definition completion in a controlled milestone.",
            "4. Execute M_c definition completion in a controlled milestone.",
            "5. Execute R_A definition completion in a controlled milestone.",
            "6. Execute Traj_A definition completion in a controlled milestone.",
            "7. Integrate completed dependent-object definitions into a completion bundle.",
            "8. Only after dependent-object completion bundle integration, plan theorem candidates.",
        ]
    )


def build_report(source_text: str) -> PlanResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.148 — Dependent-object Definition Completion Planning

        ## Question

        Can Viruse Fabric plan the next controlled dependent-object definition completion sequence after the official v8.147 Sigma_A definition completion, while keeping actual dependent-object completion, full formalization, theorem candidate planning, theorem proof, proof assistant verification, validation, manuscript readiness, readiness approval, and new citations at zero?

        ## Source artifact

        - `outputs/controlled_sigma_a_definition_completion_execution_v8_147.md`

        ## Planning interpretation

        v8.147 officially records Sigma_A as one completed formal definition object.

        v8.148 does not complete any dependent-object definition.

        v8.148 only creates the controlled plan for future dependent-object definition completion.

        The six dependent objects are planned as separate completion targets because each one has its own signature, scope, dependency boundary, and failure boundary.

        ## Planned dependent-object definition completion sequence

        {_planning_table()}

        ## Execution gates for future milestones

        Each future dependent-object completion milestone must satisfy these gates:

        1. The object must declare its formal role relative to completed Sigma_A.
        2. The object must specify domain and codomain or equivalent formal carrier.
        3. The object must specify admissibility, regularity, projection, mass, relation, or trajectory semantics without importing proof claims.
        4. The object must preserve zero theorem, proof, validation, readiness, and citation counters.
        5. The object must state its failure boundary.
        6. The object must state which prior artifacts it imports.
        7. The object must avoid claiming full formalization.
        8. The object must leave theorem candidate planning at zero.

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone is a planning milestone.

        This milestone does not complete Adm_A.

        This milestone does not complete C_reg.

        This milestone does not complete Pi_obs.

        This milestone does not complete M_c.

        This milestone does not complete R_A.

        This milestone does not complete Traj_A.

        This milestone does not complete all dependent objects.

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

        The project has planned the controlled dependent-object definition completion sequence after official Sigma_A definition completion while keeping actual dependent-object completion, full formalization completion, theorem candidate planning, theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_behavior_count = sum(
        1 for phrase in PROHIBITED_BEHAVIOR_PHRASES
        if phrase.lower() in report.lower()
    )

    boundary_keywords = [
        "does not complete",
        "does not create theorem candidates",
        "does not prove",
        "does not provide",
        "does not make",
        "does not approve",
        "does not add",
        "at zero",
        "completion count remains 0",
    ]
    boundary_phrase_count = sum(report.lower().count(item.lower()) for item in boundary_keywords)

    warnings = [
        "This milestone plans future dependent-object definition completion only.",
        "Dependent-object definitions remain uncompleted.",
        "Full formalization remains incomplete.",
        "Theorem, proof, validation, readiness approval, and citation claims remain absent.",
    ]

    return PlanResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> PlanResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
