from __future__ import annotations

import json

from viruse_fabric.writing.viruse_fabric_abstract_simulation_reframing import (
    ViruseFabricAbstractSimulationReframingBuilder,
)


def main() -> None:
    builder = ViruseFabricAbstractSimulationReframingBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "abstract-simulation-reframing-only"
    assert report["plan_phrase"] == "v9_0_abstract_simulation_reframing_without_simulation_execution"

    for field in [
        "safe_abstract_toy_only",
        "formal_reframing_only",
        "simulatable_theory_reframed",
        "falsifiable_hypotheses_declared",
        "simulation_specification_deferred_to_v9_1",
        "v8_line_frozen",
        "post_v8_pivot_to_simulation_backed_theory",
    ]:
        assert report[field] is True, f"Expected True for {field}"

    for field in [
        "simulation_engine_created",
        "simulation_run_performed",
        "baseline_comparison_performed",
        "results_reported",
        "falsification_audit_executed",
        "validation_claim_made",
        "readiness_approval_recorded",
        "manuscript_file_modified",
        "manuscript_mutation",
        "new_citation_added",
    ]:
        assert report[field] is False, f"Expected False for {field}"

    assert len(report["model_objects"]) == 8
    assert len(report["state_variables"]) == 12
    assert len(report["reframed_hypotheses"]) == 4
    assert len(report["baseline_plan"]) == 5
    assert len(report["metric_proposals"]) == 8
    assert len(report["falsification_rules"]) == 6
    assert len(report["safety_boundaries"]) == 10
    assert len(report["roadmap"]) == 5

    expected_hypotheses = {
        "VF-H1",
        "VF-H2",
        "VF-H3",
        "VF-H4",
    }
    assert {item["hypothesis_id"] for item in report["reframed_hypotheses"]} == expected_hypotheses

    expected_baselines = {
        "VF-BASE-A",
        "VF-BASE-B",
        "VF-BASE-C",
        "VF-BASE-D",
        "VF-BASE-E",
    }
    assert {item["baseline_id"] for item in report["baseline_plan"]} == expected_baselines

    expected_counts = {
        "V9 abstract simulation reframing artifact count": 1,
        "V9 theory reframing record count": 1,
        "V9 simulatable model object definition count": 8,
        "V9 state variable definition count": 12,
        "V9 reframed hypothesis count": 4,
        "V9 baseline plan count": 5,
        "V9 metric proposal count": 8,
        "V9 falsification rule count": 6,
        "V9 safety boundary count": 10,
        "V9 roadmap milestone count": 5,
        "V9 abstract simulation reframing completed count": 1,
        "V9 detailed simulation specification completed count": 0,
        "V9 simulation engine implementation count": 0,
        "V9 simulation execution count": 0,
        "V9 baseline comparison execution count": 0,
        "V9 results report count": 0,
        "V9 falsification audit execution count": 0,
        "V9 theory validation claim count": 0,
        "Toy simulation engine created count": 0,
        "Toy simulation actual run count": 0,
        "Toy simulation result count": 0,
        "Toy baseline comparison execution count": 0,
        "Toy falsification audit execution count": 0,
        "Toy citation batch 1 accepted source count": 7,
        "Toy citation batch 1 accepted methodological source pool count": 7,
        "Toy citation batch 1 accepted not citation-ready source count": 7,
        "Toy citation batch 1 citation-ready source count": 0,
        "Toy citation batch 1 actual citation count": 0,
        "Toy citation batch 1 citation integration completion count": 0,
        "Toy citation batch 1 manuscript mutation count": 0,
    }

    for name, expected in expected_counts.items():
        actual = counters.get(name)
        assert actual == expected, f"Expected {expected} for {name}, got {actual}"

    must_be_zero = [
        "V9 detailed simulation specification completed count",
        "V9 simulation engine implementation count",
        "V9 simulation execution count",
        "V9 baseline comparison execution count",
        "V9 results report count",
        "V9 falsification audit execution count",
        "V9 theory validation claim count",
        "Toy simulation engine created count",
        "Toy simulation actual run count",
        "Toy simulation result count",
        "Toy baseline comparison execution count",
        "Toy falsification audit execution count",
        "Toy evaluation actual run count",
        "Toy evaluation result count",
        "Toy evaluation validation claim count",
        "Toy scientific evidence upgrade completed count",
        "Toy manuscript coherence rewrite application count",
        "Toy manuscript patch application checklist completion count",
        "Toy manuscript patch application checklist execution count",
        "Toy manuscript patch application permission count",
        "Toy manuscript patch application applied patch count",
        "Toy manuscript patch application manuscript file modified count",
        "Toy manuscript patch application manuscript mutation count",
        "Toy citation citation-ready source count",
        "Toy citation actual citation count",
        "Toy citation fabricated reference count",
        "Toy citation integration completion count",
        "Toy citation added to manuscript count",
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

    combined_text = json.dumps(report, ensure_ascii=False)

    for phrase in [
        "Abstract simulation reframing only",
        "No simulation engine is created",
        "No simulation run is performed",
        "No baseline comparison is executed",
        "No results are reported",
        "No falsification audit is executed",
        "No validation claim is made",
        "Viruse Fabric is reframed as a safe abstract toy model",
        "formal, simulatable, and falsifiable theory frame",
        "safe abstract toy model over graph-based symbolic pattern packets",
        "local and global constraints",
        "causal-mass scoring",
        "memory-ledger path dependence",
        "t1/t2/t3 time-layered state",
        "No manuscript file is modified",
        "No citation is added",
        "No real biological datasets",
        "no real pathogen models",
        "no receptor parameters",
        "no operational targeting",
    ]:
        assert phrase in combined_text, f"Missing required phrase: {phrase}"

    print("V9_0_VIRUSE_FABRIC_ABSTRACT_SIMULATION_REFRAMING_OK")
    print("VIRUSE_FABRIC_ABSTRACT_SIMULATION_REFRAMING_DIRECT_CHECK_OK")
    print(f"Model object definition count: {counters['V9 simulatable model object definition count']}")
    print(f"State variable definition count: {counters['V9 state variable definition count']}")
    print(f"Reframed hypothesis count: {counters['V9 reframed hypothesis count']}")
    print(f"Baseline plan count: {counters['V9 baseline plan count']}")
    print(f"Metric proposal count: {counters['V9 metric proposal count']}")
    print(f"Falsification rule count: {counters['V9 falsification rule count']}")
    print(f"Safety boundary count: {counters['V9 safety boundary count']}")
    print(f"Roadmap milestone count: {counters['V9 roadmap milestone count']}")
    print(f"Simulation engine implementation count: {counters['V9 simulation engine implementation count']}")
    print(f"Simulation execution count: {counters['V9 simulation execution count']}")
    print(f"Baseline comparison execution count: {counters['V9 baseline comparison execution count']}")
    print(f"Results report count: {counters['V9 results report count']}")
    print(f"Falsification audit execution count: {counters['V9 falsification audit execution count']}")
    print(f"Theory validation claim count: {counters['V9 theory validation claim count']}")
    print(f"Toy simulation actual run count: {counters['Toy simulation actual run count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {report['passed']}")


if __name__ == "__main__":
    main()
