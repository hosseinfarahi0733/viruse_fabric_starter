from __future__ import annotations

import json
from pathlib import Path

from viruse_fabric.writing.viruse_fabric_safe_toy_parameter_sweep_and_null_control_stress_test import (
    ViruseFabricSafeToyParameterSweepAndNullControlStressTestBuilder,
)


def main() -> None:
    builder = ViruseFabricSafeToyParameterSweepAndNullControlStressTestBuilder()
    report = builder.run()

    counters = report["counters"]
    parameter_summary = report["parameter_boundary_summary"]
    null_summary = report["null_control_summary"]
    decision_gate = report["decision_gate"]

    assert report["passed"] is True
    assert report["scope"] == "safe-toy-parameter-sweep-boundary-and-null-control-decision-gate-only"
    assert report["plan_phrase"] == "v9_8_safe_toy_parameter_sweep_and_null_control_stress_test_without_validation_or_readiness"

    assert report["safe_abstract_toy_only"] is True
    assert report["decision_gate_executed"] is True
    assert report["parameter_sweep_boundary_checked"] is True
    assert report["null_control_executed"] is True

    assert report["validation_claim_made"] is False
    assert report["readiness_approval_recorded"] is False
    assert report["manuscript_file_modified"] is False
    assert report["manuscript_mutation"] is False
    assert report["new_citation_added"] is False

    assert report["primary_hypothesis_under_stress"] == "VF-H2"
    assert report["primary_signal_under_stress"] == "ledger_effect_size"
    assert report["reduced_toy_core_under_stress"] == "memory-ledger-driven toy dynamics"

    assert len(report["parameter_boundary_records"]) == 6
    assert len(report["null_control_records"]) == 4
    assert len(report["null_control_run_records"]) == 8
    assert len(report["non_upgrade_records"]) == 3
    assert {item["hypothesis_id"] for item in report["non_upgrade_records"]} == {"VF-H1", "VF-H3", "VF-H4"}
    assert all(item["status_after_v9_8"] == "not_upgraded" for item in report["non_upgrade_records"])

    assert parameter_summary["candidate_parameter_count"] == 6
    assert parameter_summary["blocked_candidate_count"] + parameter_summary["accepted_candidate_count"] == 6
    assert parameter_summary["parameter_sweep_boundary_verdict"] in {
        "parameter_sweep_blocked_by_engine_spec_boundary",
        "parameter_sweep_partially_blocked_by_engine_spec_boundary",
        "parameter_sweep_allowed_by_engine_spec_boundary",
    }

    assert null_summary["null_control_count"] == 4
    assert null_summary["null_control_leak_count"] + null_summary["null_control_no_leak_count"] == 4
    assert null_summary["null_control_verdict"] in {
        "no_null_control_leak_detected",
        "null_control_leak_detected",
    }

    assert decision_gate["decision"] in {
        "stop_claims_and_debug_null_control_leak",
        "stop_claim_expansion_and_redesign_engine_before_more_toy_evidence",
        "parameter_sweep_possible_but_requires_explicit_execution_before_claim_expansion",
    }

    assert decision_gate["next_allowed_action"] in {
        "engine_debugging_only",
        "engine_redesign_or_limited_technical_note",
        "run_real_parameter_sweep_or_stop",
    }

    assert counters["V9 decision gate artifact count"] == 1
    assert counters["V9 parameter sweep boundary check count"] == 1
    assert counters["V9 candidate parameter mutation count"] == 6
    assert counters["V9 null-control execution count"] == 1
    assert counters["V9 null-control config count"] == 4
    assert counters["V9 null-control run record count"] == 8
    assert counters["V9 null-control comparison record count"] == 4
    assert counters["V9 decision gate count"] == 1
    assert counters["V9 non-upgraded hypothesis record count"] == 3

    assert counters["V9 blocked parameter mutation count"] == parameter_summary["blocked_candidate_count"]
    assert counters["V9 accepted parameter mutation count"] == parameter_summary["accepted_candidate_count"]
    assert counters["V9 null-control leak count"] == null_summary["null_control_leak_count"]
    assert counters["V9 null-control no-leak count"] == null_summary["null_control_no_leak_count"]

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
        "decision gate",
        "parameter_sweep_blocked_by_engine_spec_boundary",
        "safe toy parameter sweep",
        "null-control stress test",
        "memory-ledger-driven toy dynamics",
        "ledger_effect_size",
        "VF-H2",
        "VF-H1",
        "VF-H3",
        "VF-H4",
        "not_upgraded",
        "stop_v9_loop",
        "engine_redesign_or_limited_technical_note",
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

    print("V9_8_VIRUSE_FABRIC_DECISION_GATE_PARAMETER_BOUNDARY_AND_NULL_CONTROL_OK")
    print("VIRUSE_FABRIC_DECISION_GATE_PARAMETER_BOUNDARY_AND_NULL_CONTROL_DIRECT_CHECK_OK")
    print(f"Primary hypothesis under stress: {report['primary_hypothesis_under_stress']}")
    print(f"Primary signal under stress: {report['primary_signal_under_stress']}")
    print(f"Reduced toy core under stress: {report['reduced_toy_core_under_stress']}")
    print(f"Candidate parameter count: {parameter_summary['candidate_parameter_count']}")
    print(f"Blocked candidate count: {parameter_summary['blocked_candidate_count']}")
    print(f"Accepted candidate count: {parameter_summary['accepted_candidate_count']}")
    print(f"Parameter sweep boundary verdict: {parameter_summary['parameter_sweep_boundary_verdict']}")
    print(f"Null-control count: {null_summary['null_control_count']}")
    print(f"Null-control leak count: {null_summary['null_control_leak_count']}")
    print(f"Null-control verdict: {null_summary['null_control_verdict']}")
    print(f"Decision: {decision_gate['decision']}")
    print(f"Next allowed action: {decision_gate['next_allowed_action']}")
    print(f"Loop guard verdict: {decision_gate['loop_guard_verdict']}")
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
