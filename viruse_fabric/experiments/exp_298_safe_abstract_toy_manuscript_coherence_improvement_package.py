from __future__ import annotations

import json

from viruse_fabric.writing.safe_abstract_toy_manuscript_coherence_improvement_package import (
    SafeAbstractToyManuscriptCoherenceImprovementPackageBuilder,
)


def main() -> None:
    builder = SafeAbstractToyManuscriptCoherenceImprovementPackageBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "manuscript-coherence-improvement-package-only"
    assert report["package_phrase"] == "manuscript_coherence_improved_but_no_manuscript_file_modified"

    assert report["coherence_improvement_completed"] is True
    assert report["manuscript_rewrite_applied"] is False

    assert report["application_permission_granted"] is False
    assert report["application_execution_performed"] is False
    assert report["checklist_completion_performed"] is False
    assert report["checklist_execution_performed"] is False
    assert report["manuscript_file_modified"] is False
    assert report["manuscript_mutation"] is False
    assert report["evaluation_execution_performed"] is False
    assert report["evidence_upgrade_completed"] is False
    assert report["validation_claim_made"] is False
    assert report["applied_patch_count"] == 0

    assert counters["Toy manuscript coherence improvement item count"] == 10
    assert counters["Toy manuscript coherence improved outline section count"] == 9
    assert counters["Toy manuscript coherence transition text count"] == 10
    assert counters["Toy manuscript coherence retained boundary count"] == 10
    assert counters["Toy manuscript coherence blocked overclaim count"] == 10

    assert counters["Toy manuscript coherence source assembly section count"] == 9
    assert counters["Toy manuscript coherence source gap item count"] == 12
    assert counters["Toy manuscript coherence source evaluation design module count"] == 10
    assert counters["Toy manuscript coherence source actual evaluation run count"] == 0
    assert counters["Toy manuscript coherence source validation claim count"] == 0
    assert counters["Toy manuscript coherence source evidence upgrade completed count"] == 0

    assert counters["Toy manuscript coherence rewrite application count"] == 0
    assert counters["Toy evaluation actual run count"] == 0
    assert counters["Toy evaluation result count"] == 0
    assert counters["Toy evaluation validation claim count"] == 0
    assert counters["Toy scientific evidence upgrade completed count"] == 0

    combined_text = (
        json.dumps(report["coherence_items"], ensure_ascii=False)
        + " "
        + json.dumps(report["improved_outline"], ensure_ascii=False)
        + " "
        + report["combined_improvement_text"]
    )

    for phrase in [
        "Global narrative spine",
        "Abstract coherence",
        "Introduction story arc",
        "Method scope bridge",
        "Pipeline overview transitions",
        "Safety controls framing",
        "Claim governance explanation",
        "Limitations balance",
        "Evaluation design bridge",
        "Future work roadmap",
        "No real biological datasets",
        "no real pathogen models",
        "no receptor parameters",
        "no operational targeting",
        "zero applied patches",
        "zero manuscript mutation",
        "zero readiness approval",
        "zero external validation",
        "zero proof assistant verification",
        "zero new citation addition",
        "Future work may only introduce stronger claims",
    ]:
        assert phrase in combined_text, f"Missing coherence phrase: {phrase}"

    must_be_zero = [
        "Toy manuscript coherence rewrite application count",
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

    print("V8_218_SAFE_ABSTRACT_TOY_MANUSCRIPT_COHERENCE_IMPROVEMENT_PACKAGE_OK")
    print("TOY_MANUSCRIPT_COHERENCE_IMPROVEMENT_PACKAGE_DIRECT_CHECK_OK")
    print(f"Coherence improvement item count: {counters['Toy manuscript coherence improvement item count']}")
    print(f"Improved outline section count: {counters['Toy manuscript coherence improved outline section count']}")
    print(f"Transition text count: {counters['Toy manuscript coherence transition text count']}")
    print(f"Retained boundary count: {counters['Toy manuscript coherence retained boundary count']}")
    print(f"Blocked overclaim count: {counters['Toy manuscript coherence blocked overclaim count']}")
    print(f"Source assembly section count: {counters['Toy manuscript coherence source assembly section count']}")
    print(f"Source gap item count: {counters['Toy manuscript coherence source gap item count']}")
    print(f"Source evaluation design module count: {counters['Toy manuscript coherence source evaluation design module count']}")
    print(f"Source actual evaluation run count: {counters['Toy manuscript coherence source actual evaluation run count']}")
    print(f"Source validation claim count: {counters['Toy manuscript coherence source validation claim count']}")
    print(f"Source evidence upgrade completed count: {counters['Toy manuscript coherence source evidence upgrade completed count']}")
    print(f"Rewrite application count: {counters['Toy manuscript coherence rewrite application count']}")
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
