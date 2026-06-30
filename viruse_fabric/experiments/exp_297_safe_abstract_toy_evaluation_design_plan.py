from __future__ import annotations

from viruse_fabric.writing.safe_abstract_toy_evaluation_design_plan import (
    SafeAbstractToyEvaluationDesignPlanBuilder,
)


def main() -> None:
    builder = SafeAbstractToyEvaluationDesignPlanBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "toy-evaluation-design-plan-only"
    assert report["plan_phrase"] == "toy_evaluation_design_planned_but_not_executed_or_validated"

    assert report["evaluation_design_completed"] is True
    assert report["evaluation_execution_performed"] is False
    assert report["evidence_upgrade_completed"] is False
    assert report["validation_claim_made"] is False

    assert report["application_permission_granted"] is False
    assert report["application_execution_performed"] is False
    assert report["checklist_completion_performed"] is False
    assert report["checklist_execution_performed"] is False
    assert report["manuscript_file_modified"] is False
    assert report["manuscript_mutation"] is False
    assert report["applied_patch_count"] == 0

    assert counters["Toy evaluation design module count"] == 10
    assert counters["Toy evaluation design metric definition count"] == 10
    assert counters["Toy evaluation design gap link count"] == 9
    assert counters["Toy evaluation design source assembly section count"] == 9
    assert counters["Toy evaluation design source gap item count"] == 12
    assert counters["Toy evaluation design source P0 gap count"] == 6
    assert counters["Toy evaluation design source P1 gap count"] == 4
    assert counters["Toy evaluation design source evidence upgrade completed count"] == 0

    assert counters["Toy evaluation actual run count"] == 0
    assert counters["Toy evaluation result count"] == 0
    assert counters["Toy evaluation validation claim count"] == 0
    assert counters["Toy scientific evidence upgrade completed count"] == 0

    module_text = " ".join(
        item["module_family"]
        + " "
        + item["toy_input_type"]
        + " "
        + item["metric_definition"]
        + " "
        + item["blocked_interpretation"]
        + " "
        + item["safety_boundary"]
        for item in report["evaluation_modules"]
    )

    for phrase in [
        "Artifact lineage completeness",
        "Zero-counter preservation",
        "Blocked-claim coverage",
        "Section-boundary consistency",
        "Gap-to-evaluation traceability",
        "Contribution clarity rubric",
        "Limitation balance rubric",
        "Citation-slot readiness design",
        "Manuscript mutation gate design",
        "Reproducibility description design",
        "Synthetic artifact metadata records only",
        "Unitless fraction",
        "No real biological datasets",
        "no real pathogen models",
        "no receptor parameters",
        "no operational targeting",
        "No new citation is added",
        "No manuscript file is modified",
        "wet-lab protocols",
    ]:
        assert phrase in module_text, f"Missing module phrase: {phrase}"

    must_be_zero = [
        "Toy evaluation actual run count",
        "Toy evaluation result count",
        "Toy evaluation validation claim count",
        "Toy scientific evidence upgrade completed count",
        "Toy manuscript patch application checklist completion count",
        "Toy manuscript patch application checklist execution count",
        "Toy manuscript patch application permission count",
        "Toy manuscript patch application applied patch count",
        "Toy manuscript patch application manuscript file modified count",
        "Toy manuscript patch application manuscript mutation count",
        "Real biological dataset import count",
        "Real pathogen simulation count",
        "Real receptor parameter count",
        "Operational host targeting count",
        "Wet-lab protocol count",
        "Actionable biosafety-risk instruction count",
        "Real-world infectivity optimization count",
        "Immune evasion optimization count",
        "Real host range prediction count",
        "Proof assistant verification count",
        "External validation count",
        "Independent experiment count",
        "Manuscript submission ready count",
        "Readiness approval count",
        "New citation added count",
    ]

    for name in must_be_zero:
        assert counters[name] == 0, f"Expected zero counter for {name}, got {counters[name]}"

    print("V8_217_SAFE_ABSTRACT_TOY_EVALUATION_DESIGN_PLAN_OK")
    print("TOY_EVALUATION_DESIGN_PLAN_DIRECT_CHECK_OK")
    print(f"Evaluation design module count: {counters['Toy evaluation design module count']}")
    print(f"Evaluation metric definition count: {counters['Toy evaluation design metric definition count']}")
    print(f"Evaluation gap link count: {counters['Toy evaluation design gap link count']}")
    print(f"Source assembly section count: {counters['Toy evaluation design source assembly section count']}")
    print(f"Source gap item count: {counters['Toy evaluation design source gap item count']}")
    print(f"Source P0 gap count: {counters['Toy evaluation design source P0 gap count']}")
    print(f"Source P1 gap count: {counters['Toy evaluation design source P1 gap count']}")
    print(f"Actual evaluation run count: {counters['Toy evaluation actual run count']}")
    print(f"Evaluation result count: {counters['Toy evaluation result count']}")
    print(f"Validation claim count: {counters['Toy evaluation validation claim count']}")
    print(f"Evidence upgrade completed count: {counters['Toy scientific evidence upgrade completed count']}")
    print(f"Checklist completion count: {counters['Toy manuscript patch application checklist completion count']}")
    print(f"Checklist execution count: {counters['Toy manuscript patch application checklist execution count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"External validation count: {counters['External validation count']}")
    print(f"Independent experiment count: {counters['Independent experiment count']}")
    print(f"Proof assistant verification count: {counters['Proof assistant verification count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {report['passed']}")


if __name__ == "__main__":
    main()
