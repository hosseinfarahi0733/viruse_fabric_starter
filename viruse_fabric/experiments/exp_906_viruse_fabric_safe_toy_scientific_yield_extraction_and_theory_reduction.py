from __future__ import annotations

import json
from pathlib import Path

from viruse_fabric.writing.viruse_fabric_safe_toy_scientific_yield_extraction_and_theory_reduction import (
    ViruseFabricSafeToyScientificYieldExtractionAndTheoryReductionBuilder,
)


def main() -> None:
    builder = ViruseFabricSafeToyScientificYieldExtractionAndTheoryReductionBuilder()
    report = builder.run()

    counters = report["counters"]
    summary = report["scientific_yield_summary"]
    core = report["reduced_theory_core"]
    hypothesis_table = report["hypothesis_yield_table"]
    mechanism_table = report["mechanism_status_table"]
    allowed_claims = report["allowed_claims_register"]
    forbidden_claims = report["forbidden_claims_register"]
    next_requirements = report["next_evidence_requirements"]

    assert report["passed"] is True
    assert report["scope"] == "safe-toy-scientific-yield-extraction-and-theory-reduction-only"
    assert report["plan_phrase"] == "v9_6_safe_toy_scientific_yield_extraction_and_theory_reduction_without_validation_or_readiness"

    for field in [
        "safe_abstract_toy_only",
        "scientific_yield_extracted",
        "theory_reduction_performed",
        "reduced_theory_core_identified",
    ]:
        assert report[field] is True, f"Expected True for {field}"

    for field in [
        "validation_claim_made",
        "readiness_approval_recorded",
        "manuscript_file_modified",
        "manuscript_mutation",
        "new_citation_added",
    ]:
        assert report[field] is False, f"Expected False for {field}"

    assert summary["summary_id"] == "V9-6-SCIENTIFIC-YIELD-SUMMARY-001"
    assert summary["yield_type"] == "narrow_safe_toy_signal"
    assert summary["primary_signal"] == "ledger_effect_size"
    assert summary["primary_supported_hypothesis"] == "VF-H2"
    assert summary["not_falsified_toy_hypothesis_count"] == 1
    assert summary["unresolved_or_unsupported_hypothesis_count"] == 3
    assert summary["strongest_safe_toy_divergence"]["baseline_id"] == "VF-BASE-A"
    assert summary["strongest_safe_toy_divergence"]["absolute_delta_total"] == 3.077813
    assert summary["weakest_safe_toy_divergence"]["absolute_delta_total"] == 0.0
    assert summary["readiness_gate_decision"] == "not_ready_for_manuscript_submission"

    assert core["core_id"] == "V9-6-REDUCED-CORE-001"
    assert core["core_name"] == "memory-ledger-driven toy dynamics"
    assert core["retained_mechanism"] == "memory_ledger"
    assert core["retained_hypothesis"] == "VF-H2"
    assert set(core["demoted_or_unresolved_hypotheses"]) == {"VF-H1", "VF-H3", "VF-H4"}
    assert "broader theory remains a framework" in core["core_statement"]
    assert "not a validated theory" in core["core_statement"]

    assert len(hypothesis_table) == 4

    hypothesis_by_id = {item["hypothesis_id"]: item for item in hypothesis_table}

    assert hypothesis_by_id["VF-H1"]["source_toy_verdict"] == "falsified_or_unresolved_in_this_safe_toy_audit"
    assert hypothesis_by_id["VF-H2"]["source_toy_verdict"] == "not_falsified_in_this_safe_toy_audit"
    assert hypothesis_by_id["VF-H3"]["source_toy_verdict"] == "falsified_or_unresolved_in_this_safe_toy_audit"
    assert hypothesis_by_id["VF-H4"]["source_toy_verdict"] == "falsified_or_unresolved_in_this_safe_toy_audit"

    assert hypothesis_by_id["VF-H1"]["selected_delta_total"] == 0.0
    assert hypothesis_by_id["VF-H2"]["selected_delta_total"] == 3.0
    assert hypothesis_by_id["VF-H3"]["selected_delta_total"] == 0.0
    assert hypothesis_by_id["VF-H4"]["selected_delta_total"] == 0.0

    assert hypothesis_by_id["VF-H2"]["yield_status"] == "not_falsified_in_current_safe_toy_audit"
    for hypothesis_id in ["VF-H1", "VF-H3", "VF-H4"]:
        assert hypothesis_by_id[hypothesis_id]["yield_status"] == "unresolved_or_unsupported_in_current_safe_toy_audit"

    assert len(mechanism_table) == 4
    mechanism_by_name = {item["mechanism_name"]: item for item in mechanism_table}
    assert mechanism_by_name["memory_ledger"]["current_status"] == "retained_as_reduced_toy_core"
    assert mechanism_by_name["memory_ledger"]["linked_hypothesis"] == "VF-H2"

    for mechanism_name in [
        "multi_layer_constraint_path_shift",
        "causal_mass_delayed_effect",
        "three_time_layer_predictive_difference",
    ]:
        assert mechanism_by_name[mechanism_name]["current_status"] == "unresolved_or_unsupported"

    assert len(allowed_claims) == 5
    assert len(forbidden_claims) == 8
    assert len(next_requirements) == 5

    allowed_text = " ".join(item["claim_text"] for item in allowed_claims)
    forbidden_text = " ".join(item["forbidden_claim"] for item in forbidden_claims)

    assert "memory-ledger component produces the clearest measurable divergence" in allowed_text
    assert "memory-ledger-driven toy dynamics" in allowed_text
    assert "multi-layer constraint, causal-mass, and three-time-layer mechanisms remain unresolved" in allowed_text
    assert "full Viruse Fabric theory is validated" in forbidden_text
    assert "causal-mass mechanism is supported" in forbidden_text
    assert "three-time-layer mechanism is supported" in forbidden_text
    assert "multi-layer constraint path-shift mechanism is supported" in forbidden_text
    assert "manuscript submission ready" in forbidden_text
    assert "empirical evidence" in forbidden_text
    assert "real biological systems" in forbidden_text

    expected_counts = {
        "V9 scientific yield extraction artifact count": 1,
        "V9 scientific yield extraction count": 1,
        "V9 theory reduction count": 1,
        "V9 reduced theory core count": 1,
        "V9 hypothesis yield table count": 1,
        "V9 hypothesis yield record count": 4,
        "V9 not-falsified toy hypothesis count": 1,
        "V9 unresolved or unsupported toy hypothesis count": 3,
        "V9 mechanism status table count": 1,
        "V9 mechanism status record count": 4,
        "V9 allowed claims register count": 1,
        "V9 allowed claim count": 5,
        "V9 forbidden claims register count": 1,
        "V9 forbidden claim count": 8,
        "V9 next evidence requirement table count": 1,
        "V9 next evidence requirement count": 5,
        "V9 source reframed hypothesis count": 4,
        "V9 source formal results report count": 1,
        "V9 source falsification audit execution count": 1,
        "V9 source toy falsification audit record count": 4,
        "V9 source manuscript readiness denial count": 1,
        "V9 source manuscript readiness approval count": 0,
        "V9 theory validation claim count": 0,
        "V9 manuscript readiness claim count": 0,
        "V9 manuscript readiness approval count": 0,
    }

    for name, expected in expected_counts.items():
        actual = counters.get(name)
        assert actual == expected, f"Expected {expected} for {name}, got {actual}"

    must_be_zero = [
        "V9 theory validation claim count",
        "V9 manuscript readiness claim count",
        "V9 manuscript readiness approval count",
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

    required_phrases = [
        "memory-ledger-driven toy dynamics",
        "Only VF-H2 is not-falsified",
        "VF-H1, VF-H3, and VF-H4 remain unresolved",
        "allowed claims",
        "forbidden claims",
        "not empirical evidence",
        "not external validation",
        "not independent validation",
        "not manuscript readiness",
        "not a theory validation claim",
        "No validation claim is made",
        "No manuscript readiness claim is made",
        "No readiness approval is recorded",
        "No manuscript file is modified",
        "No citation is added",
        "No external validation is performed",
        "No independent experiment is performed",
        "No real biological datasets",
        "no real pathogen models",
        "no receptor parameters",
        "no operational targeting",
        "no wet-lab protocol",
        "no infectivity optimization",
        "no immune evasion optimization",
        "no host range prediction",
    ]

    for phrase in required_phrases:
        assert phrase in combined_text, f"Missing required phrase: {phrase}"

    print("V9_6_VIRUSE_FABRIC_SAFE_TOY_SCIENTIFIC_YIELD_EXTRACTION_AND_THEORY_REDUCTION_OK")
    print("VIRUSE_FABRIC_SAFE_TOY_SCIENTIFIC_YIELD_EXTRACTION_AND_THEORY_REDUCTION_DIRECT_CHECK_OK")
    print(f"Primary supported hypothesis: {summary['primary_supported_hypothesis']}")
    print(f"Primary signal: {summary['primary_signal']}")
    print(f"Reduced theory core: {core['core_name']}")
    print(f"Scientific yield extraction count: {counters['V9 scientific yield extraction count']}")
    print(f"Theory reduction count: {counters['V9 theory reduction count']}")
    print(f"Reduced theory core count: {counters['V9 reduced theory core count']}")
    print(f"Hypothesis yield record count: {counters['V9 hypothesis yield record count']}")
    print(f"Not-falsified toy hypothesis count: {counters['V9 not-falsified toy hypothesis count']}")
    print(f"Unresolved or unsupported toy hypothesis count: {counters['V9 unresolved or unsupported toy hypothesis count']}")
    print(f"Allowed claim count: {counters['V9 allowed claim count']}")
    print(f"Forbidden claim count: {counters['V9 forbidden claim count']}")
    print(f"Theory validation claim count: {counters['V9 theory validation claim count']}")
    print(f"Manuscript readiness claim count: {counters['V9 manuscript readiness claim count']}")
    print(f"External validation count: {counters['External validation count']}")
    print(f"Independent experiment count: {counters['Independent experiment count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {report['passed']}")


if __name__ == "__main__":
    main()
