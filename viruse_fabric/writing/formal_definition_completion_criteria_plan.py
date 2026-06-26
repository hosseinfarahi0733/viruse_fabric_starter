"""Build the v8.9 formal definition completion criteria plan artifact.

This milestone plans criteria for future formal definition completion. It does
not complete formal definitions, execute definitions, execute a proof, prove a
theorem, prove a lemma, complete formalization, approve readiness, or make the
manuscript submission-ready.
"""

from __future__ import annotations

from pathlib import Path


OUTPUT_PATH = Path("outputs/formal_definition_completion_criteria_plan_v8_9.md")

SOURCE_ARTIFACT_COUNT = 39

REQUIRED_SOURCE_PATHS = [
    Path("outputs/formal_definition_skeleton_audit_v8_8.md"),
]

CRITERIA_ROWS = [
    {
        "id": "FDCCP-ROW-0001",
        "source_audit": "FDSA-ROW-0001",
        "definition_target": "constraint_geometry",
        "criteria_type": "object_relation_boundary_criteria",
        "criteria_focus": "future completion must specify objects, constraint relations, admissible transformations, boundary conditions, and failure cases",
        "status": "criteria_planned_not_completed",
    },
    {
        "id": "FDCCP-ROW-0002",
        "source_audit": "FDSA-ROW-0002",
        "definition_target": "attractor_concentration",
        "criteria_type": "measure_condition_interpretation_criteria",
        "criteria_focus": "future completion must specify concentration measures, attractor conditions, thresholds, and non-teleological interpretation limits",
        "status": "criteria_planned_not_completed",
    },
    {
        "id": "FDCCP-ROW-0003",
        "source_audit": "FDSA-ROW-0003",
        "definition_target": "path_compatibility",
        "criteria_type": "admissible_path_exclusion_criteria",
        "criteria_focus": "future completion must specify admissible paths, exclusion rules, compatibility predicates, and counterexample handling",
        "status": "criteria_planned_not_completed",
    },
    {
        "id": "FDCCP-ROW-0004",
        "source_audit": "FDSA-ROW-0004",
        "definition_target": "observer_projection",
        "criteria_type": "projection_mapping_boundary_criteria",
        "criteria_focus": "future completion must specify observer mapping, projection limits, apparent-purpose language boundaries, and overclaim controls",
        "status": "criteria_planned_not_completed",
    },
]

HARD_ZERO_FIELDS = [
    "formal_definition_completed_count: 0",
    "formal_definition_execution_count: 0",
    "formal_mathematical_proof_count: 0",
    "proof_execution_count: 0",
    "theorem_proven_count: 0",
    "lemma_proven_count: 0",
    "formalization_complete_count: 0",
    "proof_gap_resolution_count: 0",
    "manuscript_submission_ready_count: 0",
    "readiness_approval_count: 0",
    "independent_experiment_count: 0",
    "external_validation_count: 0",
    "new_citation_added_count: 0",
]

BOUNDARY_PHRASES = [
    "formal definition completion criteria plan exists",
    "formal definition completion does not exist",
    "formal definition execution does not exist",
    "formal mathematical proof does not exist",
    "proof execution does not exist",
    "theorem proven count remains zero",
    "lemma proven count remains zero",
    "formalization complete count remains zero",
    "proof gap resolution does not exist",
    "manuscript submission-ready status does not exist",
    "readiness approval does not exist",
    "new citation additions remain zero",
    "CAND-0003 remains conditional hold",
    "research prototype with internal validation",
]

PROHIBITED_BEHAVIORS = [
    "Do not claim completed formal definitions.",
    "Do not claim formal definition execution.",
    "Do not claim a formal mathematical proof.",
    "Do not claim proof execution.",
    "Do not claim a theorem is proven.",
    "Do not claim a lemma is proven.",
    "Do not claim formalization completeness.",
    "Do not claim proof gap resolution.",
    "Do not claim submission readiness.",
    "Do not claim readiness approval.",
    "Do not claim independent experiment.",
    "Do not claim external validation.",
    "Do not claim biological prediction.",
    "Do not add new citation records.",
    "Do not call criteria a completed definition.",
]

NEXT_STEPS = [
    "Plan a formal definition execution readiness gate in a future milestone.",
    "Keep all definition targets criteria-planned-not-completed.",
    "Separate criteria planning from definition completion.",
    "Require failure cases before any completed definition claim.",
    "Keep manuscript status not submission-ready.",
    "Keep project claims bounded to internal validation.",
    "Do not add citations without a dedicated source-retention milestone.",
    "Do not execute formal definitions inside this criteria-plan milestone.",
]


def _prefixed_list(items: list[str], prefix: str) -> str:
    return "\n".join(f"- {prefix}: {item}" for item in items)


def _criteria_row_block(row: dict[str, str]) -> str:
    return "\n".join(
        [
            f"### {row['id']}",
            "",
            f"source_audit: {row['source_audit']}",
            f"definition_target: {row['definition_target']}",
            f"criteria_type: {row['criteria_type']}",
            f"criteria_focus: {row['criteria_focus']}",
            f"status: {row['status']}",
            "completion_criteria_planned: yes",
            "formal_definition_completed: no",
            "formal_definition_executed: no",
            "proof_executed: no",
            "formal_mathematical_proof: no",
            "theorem_proven: no",
            "lemma_proven: no",
            "formalization_complete: no",
            "proof_gap_resolved: no",
            "manuscript_submission_ready: no",
            "readiness_approval: no",
            "new_citation_added: no",
            "",
            "Interpretation:",
            "This row plans criteria for future formal definition completion only. It does not complete a formal definition, execute a definition, execute a proof, prove a theorem, prove a lemma, complete formalization, or approve manuscript submission readiness.",
        ]
    )


def build_report() -> str:
    rows = "\n\n".join(_criteria_row_block(row) for row in CRITERIA_ROWS)

    report = f"""# Formal Definition Completion Criteria Plan v8.9

Experiment: 89
Milestone: v8.9 — Formal Definition Completion Criteria Plan
Status: research prototype with internal validation

## Question

Can Viruse Fabric plan formal definition completion criteria from the v8.8 definition skeleton audit while keeping completed formal definitions, definition execution, proof execution, formal mathematical proof, theorem proof, lemma proof, formalization completion, readiness approval, manuscript submission readiness, and new citation additions at zero?

## Answer

Yes. This artifact plans completion criteria for four formal definition targets. It creates criteria only. It does not complete formal definitions and does not execute formal definition construction.

formal_definition_completion_criteria_plan_count: 1
definition_completion_criteria_row_count: 4
definition_skeleton_audit_source_row_count: 4
formal_definition_completed_count: 0
formal_definition_execution_count: 0
formal_mathematical_proof_count: 0
proof_execution_count: 0
theorem_proven_count: 0
lemma_proven_count: 0
formalization_complete_count: 0
proof_gap_resolution_count: 0
manuscript_submission_ready_count: 0
readiness_approval_count: 0
independent_experiment_count: 0
external_validation_count: 0
new_citation_added_count: 0
CAND_0003_conditional_hold_count: 1

## Required Source Artifact

Required source artifact count: {SOURCE_ARTIFACT_COUNT}

{REQUIRED_SOURCE_PATHS[0]}

## Formal Definition Completion Criteria Rows

{rows}

## Hard Zero Fields

{_prefixed_list(HARD_ZERO_FIELDS, "hard_zero")}

## Boundary Phrases

{_prefixed_list(BOUNDARY_PHRASES, "boundary_phrase")}

## Prohibited Behaviors

{_prefixed_list(PROHIBITED_BEHAVIORS, "prohibited_behavior")}

## Next Steps

{_prefixed_list(NEXT_STEPS, "next_step")}

## CAND-0003 Boundary

CAND-0003 remains conditional hold.
CAND-0003 remains outside retained rows, citation rows, marker rows, revision rows, package rows, readiness rows, decision rows, gap-resolution rows, formal-proof rows, proof-skeleton execution rows, completed-definition rows, and formal-definition execution rows.

## Interpretation

The v8.9 artifact plans four formal definition completion criteria rows from the v8.8 definition skeleton audit. The plan is intentionally non-executing and non-completing. It preserves the formal definition gap and the formal proof gap.

The correct project status after this artifact is:
Viruse Fabric is a research prototype with internal validation that includes a formal definition completion criteria plan.

## Still Disallowed

completed formal definitions
formal definition execution
proven theory
formal mathematical proof
proof execution
theorem proven
lemma proven
formalization complete
resolved proof gap
independent experiment
external validation
biological prediction
clinical relevance
laboratory guidance
operational readiness
submission-ready manuscript
readiness approval
accepted scientific theory
final paper
peer-reviewed manuscript
venue acceptance
"""

    return report


def write_report(path: Path = OUTPUT_PATH) -> str:
    report = build_report()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report, encoding="utf-8")
    return report


def main() -> None:
    write_report()
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
