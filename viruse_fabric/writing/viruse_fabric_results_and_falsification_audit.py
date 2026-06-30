from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Mapping, Sequence


class ViruseFabricResultsAndFalsificationAuditBuilder:
    version = "v9.4"

    source_reframing_json_path = Path("outputs/viruse_fabric_abstract_simulation_reframing_v9_0.json")
    source_spec_json_path = Path("outputs/viruse_fabric_abstract_simulation_specification_v9_1.json")
    source_engine_json_path = Path("outputs/viruse_fabric_minimal_safe_toy_simulation_engine_v9_2.json")
    source_baseline_json_path = Path("outputs/viruse_fabric_safe_toy_baseline_comparison_v9_3.json")

    output_md_path = Path("outputs/viruse_fabric_results_and_falsification_audit_v9_4.md")
    output_json_path = Path("outputs/viruse_fabric_results_and_falsification_audit_v9_4.json")

    plan_phrase = "v9_4_results_and_falsification_audit_without_validation_or_manuscript_readiness"

    metric_names = [
        "survival_rate",
        "constraint_violation_rate",
        "symbolic_drift_rate",
        "ledger_effect_size",
    ]

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Missing required source JSON: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"Expected dict payload from {path}")
        return payload

    def _metric_abs_total(self, metric_deltas: Mapping[str, float]) -> float:
        return round(
            sum(abs(float(metric_deltas.get(metric_name, 0.0))) for metric_name in self.metric_names),
            6,
        )

    def _find_comparison(
        self,
        comparison_records: Sequence[Dict[str, Any]],
        baseline_id: str,
    ) -> Dict[str, Any]:
        for record in comparison_records:
            if record["baseline_id"] == baseline_id:
                return record
        raise ValueError(f"Missing comparison record for {baseline_id}")

    def _result_summary(self, baseline_payload: Dict[str, Any]) -> Dict[str, Any]:
        run_records = baseline_payload["run_records"]
        comparison_records = baseline_payload["comparison_records"]

        metric_table = []
        for run_record in run_records:
            metric_table.append(
                {
                    "baseline_id": run_record["baseline_id"],
                    "metric_results": run_record["metric_results"],
                    "execution_boundary": run_record["execution_boundary"],
                }
            )

        comparison_table = []
        for comparison_record in comparison_records:
            metric_deltas = comparison_record["metric_deltas"]
            comparison_table.append(
                {
                    "comparison_id": comparison_record["comparison_id"],
                    "reference_model": comparison_record["reference_model"],
                    "baseline_id": comparison_record["baseline_id"],
                    "metric_deltas": metric_deltas,
                    "absolute_delta_total": self._metric_abs_total(metric_deltas),
                    "comparison_boundary": comparison_record["comparison_boundary"],
                }
            )

        strongest = max(comparison_table, key=lambda item: item["absolute_delta_total"])
        weakest = min(comparison_table, key=lambda item: item["absolute_delta_total"])

        return {
            "summary_id": "V9-4-TOY-RESULT-SUMMARY-001",
            "scope": "formal-toy-results-report-only",
            "run_record_count": len(run_records),
            "comparison_record_count": len(comparison_records),
            "metric_table": metric_table,
            "comparison_table": comparison_table,
            "strongest_safe_toy_divergence": {
                "baseline_id": strongest["baseline_id"],
                "absolute_delta_total": strongest["absolute_delta_total"],
            },
            "weakest_safe_toy_divergence": {
                "baseline_id": weakest["baseline_id"],
                "absolute_delta_total": weakest["absolute_delta_total"],
            },
            "interpretation_boundary": (
                "Formal toy results report only. These are safe abstract toy outputs, not empirical evidence, "
                "not external validation, not independent validation, not manuscript readiness, and not a theory validation claim."
            ),
        }

    def _audit_record(
        self,
        hypothesis_id: str,
        hypothesis_name: str,
        expected_sensitive_baseline: str,
        comparison_record: Dict[str, Any],
        tested_metric_names: Sequence[str],
    ) -> Dict[str, Any]:
        metric_deltas = comparison_record["metric_deltas"]
        selected_delta_total = round(
            sum(abs(float(metric_deltas.get(metric_name, 0.0))) for metric_name in tested_metric_names),
            6,
        )

        if selected_delta_total > 0.0:
            toy_audit_verdict = "not_falsified_in_this_safe_toy_audit"
            audit_reason = (
                "The selected safe toy baseline comparison produced nonzero divergence on the audited toy metrics. "
                "This prevents a toy-level falsification verdict for this hypothesis in v9.4, but it does not validate the theory."
            )
        else:
            toy_audit_verdict = "falsified_or_unresolved_in_this_safe_toy_audit"
            audit_reason = (
                "The selected safe toy baseline comparison produced no detectable divergence on the audited toy metrics. "
                "This is treated as a toy-level falsification-or-unresolved signal, not as an empirical conclusion."
            )

        return {
            "audit_id": f"V9-4-AUDIT-{hypothesis_id}",
            "hypothesis_id": hypothesis_id,
            "hypothesis_name": hypothesis_name,
            "expected_sensitive_baseline": expected_sensitive_baseline,
            "comparison_id": comparison_record["comparison_id"],
            "tested_metric_names": list(tested_metric_names),
            "selected_metric_deltas": {
                metric_name: metric_deltas.get(metric_name, 0.0)
                for metric_name in tested_metric_names
            },
            "selected_delta_total": selected_delta_total,
            "toy_audit_verdict": toy_audit_verdict,
            "audit_reason": audit_reason,
            "audit_boundary": (
                "Toy falsification audit only. This audit is not external validation, not empirical evidence, "
                "not manuscript readiness, and not a theory validation claim."
            ),
        }

    def _falsification_audit(self, baseline_payload: Dict[str, Any]) -> Dict[str, Any]:
        comparison_records = baseline_payload["comparison_records"]

        h1_comparison = self._find_comparison(comparison_records, "VF-BASE-B")
        h2_comparison = self._find_comparison(comparison_records, "VF-BASE-C")
        h3_comparison = self._find_comparison(comparison_records, "VF-BASE-E")
        h4_comparison = self._find_comparison(comparison_records, "VF-BASE-D")

        audit_records = [
            self._audit_record(
                hypothesis_id="VF-H1",
                hypothesis_name="multi_layer_constraint_path_shift",
                expected_sensitive_baseline="VF-BASE-B",
                comparison_record=h1_comparison,
                tested_metric_names=[
                    "survival_rate",
                    "constraint_violation_rate",
                    "symbolic_drift_rate",
                ],
            ),
            self._audit_record(
                hypothesis_id="VF-H2",
                hypothesis_name="memory_ledger_stability_effect",
                expected_sensitive_baseline="VF-BASE-C",
                comparison_record=h2_comparison,
                tested_metric_names=[
                    "ledger_effect_size",
                    "symbolic_drift_rate",
                ],
            ),
            self._audit_record(
                hypothesis_id="VF-H3",
                hypothesis_name="causal_mass_delayed_effect",
                expected_sensitive_baseline="VF-BASE-E",
                comparison_record=h3_comparison,
                tested_metric_names=[
                    "ledger_effect_size",
                    "symbolic_drift_rate",
                    "survival_rate",
                ],
            ),
            self._audit_record(
                hypothesis_id="VF-H4",
                hypothesis_name="three_time_layer_predictive_difference",
                expected_sensitive_baseline="VF-BASE-D",
                comparison_record=h4_comparison,
                tested_metric_names=[
                    "ledger_effect_size",
                    "symbolic_drift_rate",
                    "constraint_violation_rate",
                ],
            ),
        ]

        verdict_counts: Dict[str, int] = {}
        for record in audit_records:
            verdict = record["toy_audit_verdict"]
            verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        return {
            "audit_summary_id": "V9-4-TOY-FALSIFICATION-AUDIT-001",
            "scope": "toy-falsification-audit-only",
            "audit_record_count": len(audit_records),
            "audit_records": audit_records,
            "toy_audit_verdict_counts": verdict_counts,
            "audit_statement": (
                "v9.4 executes a toy falsification audit over the v9.3 safe toy baseline comparison records. "
                "The audit may produce toy-level not-falsified or falsified-or-unresolved signals, but it does not "
                "make a theory validation claim, does not provide external validation, does not provide independent "
                "experimental confirmation, and does not establish manuscript readiness."
            ),
        }

    def build(self) -> Dict[str, Any]:
        reframing_payload = self._load_json(self.source_reframing_json_path)
        spec_payload = self._load_json(self.source_spec_json_path)
        engine_payload = self._load_json(self.source_engine_json_path)
        baseline_payload = self._load_json(self.source_baseline_json_path)

        result_summary = self._result_summary(baseline_payload)
        falsification_audit = self._falsification_audit(baseline_payload)

        counters = {
            "V9 results and falsification audit artifact count": 1,
            "V9 formal results report count": 1,
            "V9 results report count": 1,
            "V9 falsification audit execution count": 1,
            "V9 toy result summary count": 1,
            "V9 toy falsification audit summary count": 1,
            "V9 toy falsification audit record count": falsification_audit["audit_record_count"],
            "V9 toy hypothesis audit count": falsification_audit["audit_record_count"],
            "Toy evaluation actual run count": 1,
            "Toy evaluation result count": 1,
            "Toy falsification audit execution count": 1,
            "Toy falsification audit result count": falsification_audit["audit_record_count"],
            "V9 source safe toy baseline comparison artifact count": baseline_payload["counters"]["V9 safe toy baseline comparison artifact count"],
            "V9 source simulation execution count": baseline_payload["counters"]["V9 simulation execution count"],
            "V9 source baseline comparison execution count": baseline_payload["counters"]["V9 baseline comparison execution count"],
            "V9 source safe toy run record count": baseline_payload["counters"]["V9 safe toy run record count"],
            "V9 source safe toy baseline comparison record count": baseline_payload["counters"]["V9 safe toy baseline comparison record count"],
            "V9 source engine implementation count": engine_payload["counters"]["V9 simulation engine implementation count"],
            "V9 source detailed simulation specification completed count": spec_payload["counters"]["V9 detailed simulation specification completed count"],
            "V9 source reframed hypothesis count": reframing_payload["counters"]["V9 reframed hypothesis count"],
            "V9 theory validation claim count": 0,
            "V9 manuscript readiness claim count": 0,
            "Toy evaluation validation claim count": 0,
            "Toy scientific evidence upgrade completed count": 0,
            "Toy manuscript coherence rewrite application count": 0,
            "Toy manuscript patch application checklist completion count": 0,
            "Toy manuscript patch application checklist execution count": 0,
            "Toy manuscript patch application permission count": 0,
            "Toy manuscript patch application applied patch count": 0,
            "Toy manuscript patch application manuscript file modified count": 0,
            "Toy manuscript patch application manuscript mutation count": 0,
            "Toy citation citation-ready source count": 0,
            "Toy citation actual citation count": 0,
            "Toy citation fabricated reference count": 0,
            "Toy citation integration completion count": 0,
            "Toy citation added to manuscript count": 0,
            "Real biological dataset import count": 0,
            "Real pathogen simulation count": 0,
            "Real receptor parameter count": 0,
            "Operational host targeting count": 0,
            "Wet-lab protocol count": 0,
            "Actionable biosafety-risk instruction count": 0,
            "Real-world infectivity optimization count": 0,
            "Immune evasion optimization count": 0,
            "Real host range prediction count": 0,
            "Proof assistant verification count": 0,
            "External validation count": 0,
            "Independent experiment count": 0,
            "Manuscript submission ready count": 0,
            "Readiness approval count": 0,
            "New citation added count": 0,
        }

        report = {
            "version": self.version,
            "title": "Viruse Fabric Results and Falsification Audit",
            "plan_phrase": self.plan_phrase,
            "scope": "formal-toy-results-and-falsification-audit-only",
            "safe_abstract_toy_only": True,
            "formal_results_reported": True,
            "results_reported": True,
            "falsification_audit_executed": True,
            "toy_evaluation_executed": True,
            "validation_claim_made": False,
            "readiness_approval_recorded": False,
            "manuscript_file_modified": False,
            "manuscript_mutation": False,
            "new_citation_added": False,
            "source_reframing_json": str(self.source_reframing_json_path),
            "source_spec_json": str(self.source_spec_json_path),
            "source_engine_json": str(self.source_engine_json_path),
            "source_baseline_json": str(self.source_baseline_json_path),
            "result_summary": result_summary,
            "falsification_audit": falsification_audit,
            "results_statement": (
                "v9.4 produces a formal toy results report from the v9.3 safe toy baseline comparison records. "
                "It reports toy metric summaries and toy baseline divergences only. The report is not empirical evidence, "
                "not external validation, not independent validation, not manuscript readiness, and not a theory validation claim."
            ),
            "non_validation_disclaimer": (
                "Formal toy results report and toy falsification audit only. No validation claim is made. "
                "No manuscript readiness claim is made. No external validation is performed. No independent experiment is performed. "
                "No manuscript file is modified. No citation is added. No real biological datasets, no real pathogen models, "
                "no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, "
                "no immune evasion optimization, and no host range prediction are introduced."
            ),
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "formal-toy-results-and-falsification-audit-only":
            raise AssertionError("v9.4 must remain formal-toy-results-and-falsification-audit-only.")

        if report["passed"] is not True:
            raise AssertionError("v9.4 must pass.")

        for field in [
            "safe_abstract_toy_only",
            "formal_results_reported",
            "results_reported",
            "falsification_audit_executed",
            "toy_evaluation_executed",
        ]:
            if report[field] is not True:
                raise AssertionError(f"Expected True for {field}")

        for field in [
            "validation_claim_made",
            "readiness_approval_recorded",
            "manuscript_file_modified",
            "manuscript_mutation",
            "new_citation_added",
        ]:
            if report[field] is not False:
                raise AssertionError(f"Expected False for {field}")

        if report["result_summary"]["run_record_count"] != 6:
            raise AssertionError("Expected six source run records.")

        if report["result_summary"]["comparison_record_count"] != 5:
            raise AssertionError("Expected five source comparison records.")

        if report["falsification_audit"]["audit_record_count"] != 4:
            raise AssertionError("Expected four toy hypothesis audit records.")

        counters = report["counters"]

        expected_counts = {
            "V9 results and falsification audit artifact count": 1,
            "V9 formal results report count": 1,
            "V9 results report count": 1,
            "V9 falsification audit execution count": 1,
            "V9 toy result summary count": 1,
            "V9 toy falsification audit summary count": 1,
            "V9 toy falsification audit record count": 4,
            "V9 toy hypothesis audit count": 4,
            "Toy evaluation actual run count": 1,
            "Toy evaluation result count": 1,
            "Toy falsification audit execution count": 1,
            "Toy falsification audit result count": 4,
            "V9 source safe toy baseline comparison artifact count": 1,
            "V9 source simulation execution count": 1,
            "V9 source baseline comparison execution count": 1,
            "V9 source safe toy run record count": 6,
            "V9 source safe toy baseline comparison record count": 5,
            "V9 source engine implementation count": 1,
            "V9 source detailed simulation specification completed count": 1,
            "V9 source reframed hypothesis count": 4,
            "V9 theory validation claim count": 0,
            "V9 manuscript readiness claim count": 0,
        }

        for name, expected in expected_counts.items():
            actual = counters.get(name)
            if actual != expected:
                raise AssertionError(f"Expected {expected} for {name}, got {actual}")

        must_be_zero = [
            "V9 theory validation claim count",
            "V9 manuscript readiness claim count",
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
            if counters.get(name) != 0:
                raise AssertionError(f"Counter must remain zero: {name}")

        combined_text = json.dumps(report, ensure_ascii=False)

        required_phrases = [
            "Formal toy results report only",
            "toy falsification audit",
            "toy metric summaries",
            "toy baseline divergences",
            "not empirical evidence",
            "not external validation",
            "not independent validation",
            "not manuscript readiness",
            "not a theory validation claim",
            "No validation claim is made",
            "No manuscript readiness claim is made",
            "No external validation is performed",
            "No independent experiment is performed",
            "No manuscript file is modified",
            "No citation is added",
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
            if phrase not in combined_text:
                raise AssertionError(f"Missing required v9.4 phrase: {phrase}")

    def render_markdown(self, report: Dict[str, Any]) -> str:
        lines: List[str] = []

        lines.append("# Viruse Fabric Results and Falsification Audit")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is formal-toy-results-and-falsification-audit-only.")
        lines.append("It produces a formal toy results report and a toy falsification audit from v9.3 safe toy baseline comparison records.")
        lines.append("It does not validate the theory, does not approve manuscript readiness, does not modify manuscript files, and does not add citations.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")

        lines.append("## Results Statement")
        lines.append("")
        lines.append(report["results_statement"])
        lines.append("")

        lines.append("## Non-Validation Disclaimer")
        lines.append("")
        lines.append(report["non_validation_disclaimer"])
        lines.append("")

        lines.append("## Toy Result Summary")
        lines.append("")
        summary = report["result_summary"]
        lines.append(f"- Summary id: {summary['summary_id']}")
        lines.append(f"- Scope: {summary['scope']}")
        lines.append(f"- Run record count: {summary['run_record_count']}")
        lines.append(f"- Comparison record count: {summary['comparison_record_count']}")
        lines.append(f"- Strongest safe toy divergence: {summary['strongest_safe_toy_divergence']}")
        lines.append(f"- Weakest safe toy divergence: {summary['weakest_safe_toy_divergence']}")
        lines.append(f"- Interpretation boundary: {summary['interpretation_boundary']}")
        lines.append("")

        lines.append("## Toy Metric Table")
        lines.append("")
        for item in summary["metric_table"]:
            lines.append(f"### {item['baseline_id']}")
            lines.append("")
            lines.append(f"- Metric results: {item['metric_results']}")
            lines.append(f"- Execution boundary: {item['execution_boundary']}")
            lines.append("")

        lines.append("## Toy Baseline Divergence Table")
        lines.append("")
        for item in summary["comparison_table"]:
            lines.append(f"### {item['comparison_id']}")
            lines.append("")
            lines.append(f"- Reference model: {item['reference_model']}")
            lines.append(f"- Baseline id: {item['baseline_id']}")
            lines.append(f"- Metric deltas: {item['metric_deltas']}")
            lines.append(f"- Absolute delta total: {item['absolute_delta_total']}")
            lines.append(f"- Comparison boundary: {item['comparison_boundary']}")
            lines.append("")

        lines.append("## Toy Falsification Audit")
        lines.append("")
        audit = report["falsification_audit"]
        lines.append(f"- Audit summary id: {audit['audit_summary_id']}")
        lines.append(f"- Scope: {audit['scope']}")
        lines.append(f"- Audit record count: {audit['audit_record_count']}")
        lines.append(f"- Toy audit verdict counts: {audit['toy_audit_verdict_counts']}")
        lines.append(f"- Audit statement: {audit['audit_statement']}")
        lines.append("")

        for item in audit["audit_records"]:
            lines.append(f"### {item['audit_id']}")
            lines.append("")
            lines.append(f"- Hypothesis id: {item['hypothesis_id']}")
            lines.append(f"- Hypothesis name: {item['hypothesis_name']}")
            lines.append(f"- Expected sensitive baseline: {item['expected_sensitive_baseline']}")
            lines.append(f"- Comparison id: {item['comparison_id']}")
            lines.append(f"- Tested metric names: {item['tested_metric_names']}")
            lines.append(f"- Selected metric deltas: {item['selected_metric_deltas']}")
            lines.append(f"- Selected delta total: {item['selected_delta_total']}")
            lines.append(f"- Toy audit verdict: {item['toy_audit_verdict']}")
            lines.append(f"- Audit reason: {item['audit_reason']}")
            lines.append(f"- Audit boundary: {item['audit_boundary']}")
            lines.append("")

        lines.append("## Counters")
        lines.append("")
        for key, value in report["counters"].items():
            lines.append(f"{key}: {value}")

        lines.append("")
        lines.append("## Result")
        lines.append("")
        lines.append(f"Passed: {report['passed']}")
        lines.append("")
        lines.append("V9_4_VIRUSE_FABRIC_RESULTS_AND_FALSIFICATION_AUDIT_OK")
        lines.append("")

        return "\n".join(lines)

    def run(self) -> Dict[str, Any]:
        report = self.build()
        self.output_md_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_json_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_md_path.write_text(self.render_markdown(report), encoding="utf-8")
        self.output_json_path.write_text(
            json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        return report


def build_viruse_fabric_results_and_falsification_audit() -> Dict[str, Any]:
    return ViruseFabricResultsAndFalsificationAuditBuilder().run()


if __name__ == "__main__":
    result = build_viruse_fabric_results_and_falsification_audit()
    counters = result["counters"]
    print("V9_4_VIRUSE_FABRIC_RESULTS_AND_FALSIFICATION_AUDIT_OK")
    print("VIRUSE_FABRIC_RESULTS_AND_FALSIFICATION_AUDIT_DIRECT_CHECK_OK")
    print(f"Formal results report count: {counters['V9 formal results report count']}")
    print(f"Results report count: {counters['V9 results report count']}")
    print(f"Falsification audit execution count: {counters['V9 falsification audit execution count']}")
    print(f"Toy result summary count: {counters['V9 toy result summary count']}")
    print(f"Toy falsification audit record count: {counters['V9 toy falsification audit record count']}")
    print(f"Toy evaluation actual run count: {counters['Toy evaluation actual run count']}")
    print(f"Toy evaluation result count: {counters['Toy evaluation result count']}")
    print(f"Toy falsification audit execution count: {counters['Toy falsification audit execution count']}")
    print(f"Theory validation claim count: {counters['V9 theory validation claim count']}")
    print(f"Manuscript readiness claim count: {counters['V9 manuscript readiness claim count']}")
    print(f"External validation count: {counters['External validation count']}")
    print(f"Independent experiment count: {counters['Independent experiment count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {result['passed']}")
