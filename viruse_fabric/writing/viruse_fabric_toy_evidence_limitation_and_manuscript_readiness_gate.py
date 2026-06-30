from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class ViruseFabricToyEvidenceLimitationAndManuscriptReadinessGateBuilder:
    version = "v9.5"

    source_reframing_json_path = Path("outputs/viruse_fabric_abstract_simulation_reframing_v9_0.json")
    source_spec_json_path = Path("outputs/viruse_fabric_abstract_simulation_specification_v9_1.json")
    source_engine_json_path = Path("outputs/viruse_fabric_minimal_safe_toy_simulation_engine_v9_2.json")
    source_baseline_json_path = Path("outputs/viruse_fabric_safe_toy_baseline_comparison_v9_3.json")
    source_audit_json_path = Path("outputs/viruse_fabric_results_and_falsification_audit_v9_4.json")

    output_md_path = Path("outputs/viruse_fabric_toy_evidence_limitation_and_manuscript_readiness_gate_v9_5.md")
    output_json_path = Path("outputs/viruse_fabric_toy_evidence_limitation_and_manuscript_readiness_gate_v9_5.json")

    plan_phrase = "v9_5_toy_evidence_limitation_and_manuscript_readiness_gate_without_submission_approval"

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Missing required source JSON: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"Expected dict payload from {path}")
        return payload

    def _toy_evidence_summary(
        self,
        reframing_payload: Dict[str, Any],
        spec_payload: Dict[str, Any],
        engine_payload: Dict[str, Any],
        baseline_payload: Dict[str, Any],
        audit_payload: Dict[str, Any],
    ) -> Dict[str, Any]:
        reframing_counters = reframing_payload["counters"]
        spec_counters = spec_payload["counters"]
        engine_counters = engine_payload["counters"]
        baseline_counters = baseline_payload["counters"]
        audit_counters = audit_payload["counters"]

        return {
            "summary_id": "V9-5-TOY-EVIDENCE-SUMMARY-001",
            "safe_abstract_toy_only": True,
            "reframed_hypothesis_count": reframing_counters["V9 reframed hypothesis count"],
            "detailed_specification_completed_count": spec_counters["V9 detailed simulation specification completed count"],
            "engine_implementation_count": engine_counters["V9 simulation engine implementation count"],
            "safe_toy_simulation_execution_count": baseline_counters["V9 simulation execution count"],
            "safe_toy_baseline_comparison_execution_count": baseline_counters["V9 baseline comparison execution count"],
            "safe_toy_run_record_count": baseline_counters["V9 safe toy run record count"],
            "safe_toy_baseline_comparison_record_count": baseline_counters["V9 safe toy baseline comparison record count"],
            "formal_toy_results_report_count": audit_counters["V9 formal results report count"],
            "toy_falsification_audit_execution_count": audit_counters["V9 falsification audit execution count"],
            "toy_falsification_audit_record_count": audit_counters["V9 toy falsification audit record count"],
            "evidence_boundary": (
                "Toy evidence exists only inside the safe abstract toy setting. It is not empirical evidence, "
                "not external validation, not independent validation, not a theory validation claim, "
                "not manuscript readiness, and not submission readiness."
            ),
        }

    def _limitation_register(self) -> List[Dict[str, Any]]:
        return [
            {
                "limitation_id": "V9-5-LIMIT-001",
                "name": "toy_only_evidence_boundary",
                "blocking": True,
                "description": (
                    "The available evidence is safe abstract toy evidence only and cannot be treated as empirical "
                    "or real-world validation."
                ),
            },
            {
                "limitation_id": "V9-5-LIMIT-002",
                "name": "no_external_validation",
                "blocking": True,
                "description": "No external validation has been performed.",
            },
            {
                "limitation_id": "V9-5-LIMIT-003",
                "name": "no_independent_experiment",
                "blocking": True,
                "description": "No independent experiment has been performed.",
            },
            {
                "limitation_id": "V9-5-LIMIT-004",
                "name": "no_proof_assistant_verification",
                "blocking": True,
                "description": "No proof assistant verification has been performed.",
            },
            {
                "limitation_id": "V9-5-LIMIT-005",
                "name": "no_citation_integration",
                "blocking": True,
                "description": "No citation integration has been completed and no citation has been added to manuscript text.",
            },
            {
                "limitation_id": "V9-5-LIMIT-006",
                "name": "no_manuscript_mutation",
                "blocking": True,
                "description": "No manuscript file has been modified, patched, or made submission-ready.",
            },
            {
                "limitation_id": "V9-5-LIMIT-007",
                "name": "no_real_biological_validation",
                "blocking": True,
                "description": (
                    "No real biological dataset, real pathogen simulation, receptor parameter, operational targeting, "
                    "wet-lab protocol, infectivity optimization, immune evasion optimization, or host range prediction "
                    "has been introduced."
                ),
            },
            {
                "limitation_id": "V9-5-LIMIT-008",
                "name": "no_theory_validation_claim",
                "blocking": True,
                "description": "The toy audit does not validate the theory.",
            },
        ]

    def _readiness_gate(
        self,
        limitation_register: List[Dict[str, Any]],
        audit_payload: Dict[str, Any],
    ) -> Dict[str, Any]:
        blocking_items = [item for item in limitation_register if item["blocking"]]
        audit_counters = audit_payload["counters"]

        hard_requirements = [
            {
                "requirement_id": "V9-5-GATE-REQ-001",
                "name": "formal_toy_results_available",
                "required_value": 1,
                "actual_value": audit_counters["V9 formal results report count"],
                "passed": audit_counters["V9 formal results report count"] == 1,
            },
            {
                "requirement_id": "V9-5-GATE-REQ-002",
                "name": "toy_falsification_audit_available",
                "required_value": 1,
                "actual_value": audit_counters["V9 falsification audit execution count"],
                "passed": audit_counters["V9 falsification audit execution count"] == 1,
            },
            {
                "requirement_id": "V9-5-GATE-REQ-003",
                "name": "external_validation_available",
                "required_value": 1,
                "actual_value": audit_counters["External validation count"],
                "passed": False,
            },
            {
                "requirement_id": "V9-5-GATE-REQ-004",
                "name": "independent_experiment_available",
                "required_value": 1,
                "actual_value": audit_counters["Independent experiment count"],
                "passed": False,
            },
            {
                "requirement_id": "V9-5-GATE-REQ-005",
                "name": "citation_integration_available",
                "required_value": 1,
                "actual_value": audit_counters["Toy citation integration completion count"],
                "passed": False,
            },
            {
                "requirement_id": "V9-5-GATE-REQ-006",
                "name": "manuscript_mutation_available",
                "required_value": 1,
                "actual_value": audit_counters["Toy manuscript patch application manuscript mutation count"],
                "passed": False,
            },
            {
                "requirement_id": "V9-5-GATE-REQ-007",
                "name": "readiness_approval_available",
                "required_value": 1,
                "actual_value": audit_counters["Readiness approval count"],
                "passed": False,
            },
        ]

        passed_count = sum(1 for item in hard_requirements if item["passed"])
        failed_count = len(hard_requirements) - passed_count

        return {
            "gate_id": "V9-5-MANUSCRIPT-READINESS-GATE-001",
            "gate_scope": "toy-evidence-limitation-and-readiness-denial-only",
            "gate_decision": "not_ready_for_manuscript_submission",
            "approval_recorded": False,
            "submission_ready": False,
            "theory_validation_claim_made": False,
            "hard_requirement_count": len(hard_requirements),
            "hard_requirement_passed_count": passed_count,
            "hard_requirement_failed_count": failed_count,
            "blocking_limitation_count": len(blocking_items),
            "hard_requirements": hard_requirements,
            "blocking_limitations": blocking_items,
            "decision_reason": (
                "The project has safe toy evidence, a formal toy results report, and a toy falsification audit, "
                "but it lacks external validation, independent experiment, proof assistant verification, citation integration, "
                "manuscript mutation, and readiness approval. Therefore manuscript submission readiness is denied."
            ),
        }

    def build(self) -> Dict[str, Any]:
        reframing_payload = self._load_json(self.source_reframing_json_path)
        spec_payload = self._load_json(self.source_spec_json_path)
        engine_payload = self._load_json(self.source_engine_json_path)
        baseline_payload = self._load_json(self.source_baseline_json_path)
        audit_payload = self._load_json(self.source_audit_json_path)

        toy_evidence_summary = self._toy_evidence_summary(
            reframing_payload=reframing_payload,
            spec_payload=spec_payload,
            engine_payload=engine_payload,
            baseline_payload=baseline_payload,
            audit_payload=audit_payload,
        )
        limitation_register = self._limitation_register()
        readiness_gate = self._readiness_gate(
            limitation_register=limitation_register,
            audit_payload=audit_payload,
        )

        counters = {
            "V9 toy evidence limitation and readiness gate artifact count": 1,
            "V9 toy evidence limitation analysis count": 1,
            "V9 manuscript readiness gate execution count": 1,
            "V9 manuscript readiness denial count": 1,
            "V9 manuscript readiness approval count": 0,
            "V9 readiness hard requirement count": readiness_gate["hard_requirement_count"],
            "V9 readiness hard requirement passed count": readiness_gate["hard_requirement_passed_count"],
            "V9 readiness hard requirement failed count": readiness_gate["hard_requirement_failed_count"],
            "V9 blocking evidence limitation count": readiness_gate["blocking_limitation_count"],
            "V9 source formal results report count": audit_payload["counters"]["V9 formal results report count"],
            "V9 source results report count": audit_payload["counters"]["V9 results report count"],
            "V9 source falsification audit execution count": audit_payload["counters"]["V9 falsification audit execution count"],
            "V9 source toy result summary count": audit_payload["counters"]["V9 toy result summary count"],
            "V9 source toy falsification audit record count": audit_payload["counters"]["V9 toy falsification audit record count"],
            "V9 source theory validation claim count": audit_payload["counters"]["V9 theory validation claim count"],
            "V9 source manuscript readiness claim count": audit_payload["counters"]["V9 manuscript readiness claim count"],
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
            "title": "Viruse Fabric Toy Evidence Limitation and Manuscript Readiness Gate",
            "plan_phrase": self.plan_phrase,
            "scope": "toy-evidence-limitation-and-manuscript-readiness-gate-only",
            "safe_abstract_toy_only": True,
            "toy_evidence_limitation_analysis_performed": True,
            "manuscript_readiness_gate_executed": True,
            "manuscript_readiness_denied": True,
            "manuscript_readiness_approved": False,
            "submission_ready": False,
            "validation_claim_made": False,
            "readiness_approval_recorded": False,
            "manuscript_file_modified": False,
            "manuscript_mutation": False,
            "new_citation_added": False,
            "source_reframing_json": str(self.source_reframing_json_path),
            "source_spec_json": str(self.source_spec_json_path),
            "source_engine_json": str(self.source_engine_json_path),
            "source_baseline_json": str(self.source_baseline_json_path),
            "source_audit_json": str(self.source_audit_json_path),
            "toy_evidence_summary": toy_evidence_summary,
            "limitation_register": limitation_register,
            "readiness_gate": readiness_gate,
            "gate_statement": (
                "v9.5 executes a toy evidence limitation analysis and manuscript readiness gate. "
                "The gate denies manuscript submission readiness because the project remains toy-only and lacks external validation, "
                "independent experiment, proof assistant verification, citation integration, manuscript mutation, and readiness approval."
            ),
            "non_validation_disclaimer": (
                "Toy evidence limitation and readiness gate only. No validation claim is made. "
                "No manuscript readiness claim is made. No submission readiness approval is recorded. "
                "No external validation is performed. No independent experiment is performed. "
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
        if report["scope"] != "toy-evidence-limitation-and-manuscript-readiness-gate-only":
            raise AssertionError("v9.5 must remain toy-evidence-limitation-and-manuscript-readiness-gate-only.")

        if report["passed"] is not True:
            raise AssertionError("v9.5 must pass.")

        for field in [
            "safe_abstract_toy_only",
            "toy_evidence_limitation_analysis_performed",
            "manuscript_readiness_gate_executed",
            "manuscript_readiness_denied",
        ]:
            if report[field] is not True:
                raise AssertionError(f"Expected True for {field}")

        for field in [
            "manuscript_readiness_approved",
            "submission_ready",
            "validation_claim_made",
            "readiness_approval_recorded",
            "manuscript_file_modified",
            "manuscript_mutation",
            "new_citation_added",
        ]:
            if report[field] is not False:
                raise AssertionError(f"Expected False for {field}")

        gate = report["readiness_gate"]
        if gate["gate_decision"] != "not_ready_for_manuscript_submission":
            raise AssertionError("v9.5 gate must deny manuscript submission readiness.")

        if gate["approval_recorded"] is not False:
            raise AssertionError("v9.5 must not record readiness approval.")

        if gate["submission_ready"] is not False:
            raise AssertionError("v9.5 must not mark submission readiness.")

        if gate["theory_validation_claim_made"] is not False:
            raise AssertionError("v9.5 must not make a theory validation claim.")

        if gate["hard_requirement_count"] != 7:
            raise AssertionError("Expected seven hard readiness requirements.")

        if gate["hard_requirement_passed_count"] != 2:
            raise AssertionError("Expected only two hard requirements to pass: toy results and toy audit.")

        if gate["hard_requirement_failed_count"] != 5:
            raise AssertionError("Expected five hard readiness requirements to fail.")

        if gate["blocking_limitation_count"] != 8:
            raise AssertionError("Expected eight blocking evidence limitations.")

        counters = report["counters"]

        expected_counts = {
            "V9 toy evidence limitation and readiness gate artifact count": 1,
            "V9 toy evidence limitation analysis count": 1,
            "V9 manuscript readiness gate execution count": 1,
            "V9 manuscript readiness denial count": 1,
            "V9 manuscript readiness approval count": 0,
            "V9 readiness hard requirement count": 7,
            "V9 readiness hard requirement passed count": 2,
            "V9 readiness hard requirement failed count": 5,
            "V9 blocking evidence limitation count": 8,
            "V9 source formal results report count": 1,
            "V9 source results report count": 1,
            "V9 source falsification audit execution count": 1,
            "V9 source toy result summary count": 1,
            "V9 source toy falsification audit record count": 4,
            "V9 source theory validation claim count": 0,
            "V9 source manuscript readiness claim count": 0,
            "V9 theory validation claim count": 0,
            "V9 manuscript readiness claim count": 0,
        }

        for name, expected in expected_counts.items():
            actual = counters.get(name)
            if actual != expected:
                raise AssertionError(f"Expected {expected} for {name}, got {actual}")

        must_be_zero = [
            "V9 manuscript readiness approval count",
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
            "toy evidence limitation analysis",
            "manuscript readiness gate",
            "not_ready_for_manuscript_submission",
            "denies manuscript submission readiness",
            "toy-only",
            "lacks external validation",
            "independent experiment",
            "proof assistant verification",
            "citation integration",
            "manuscript mutation",
            "readiness approval",
            "No validation claim is made",
            "No manuscript readiness claim is made",
            "No submission readiness approval is recorded",
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
                raise AssertionError(f"Missing required v9.5 phrase: {phrase}")

    def render_markdown(self, report: Dict[str, Any]) -> str:
        lines: List[str] = []

        lines.append("# Viruse Fabric Toy Evidence Limitation and Manuscript Readiness Gate")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is toy-evidence-limitation-and-manuscript-readiness-gate-only.")
        lines.append("It analyzes the limitations of the v9.4 toy evidence and executes a manuscript readiness gate.")
        lines.append("The gate decision is not_ready_for_manuscript_submission.")
        lines.append("It does not validate the theory, does not approve manuscript readiness, does not modify manuscript files, and does not add citations.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")

        lines.append("## Gate Statement")
        lines.append("")
        lines.append(report["gate_statement"])
        lines.append("")

        lines.append("## Non-Validation Disclaimer")
        lines.append("")
        lines.append(report["non_validation_disclaimer"])
        lines.append("")

        lines.append("## Toy Evidence Summary")
        lines.append("")
        for key, value in report["toy_evidence_summary"].items():
            lines.append(f"- {key}: {value}")
        lines.append("")

        lines.append("## Limitation Register")
        lines.append("")
        for item in report["limitation_register"]:
            lines.append(f"### {item['limitation_id']} - {item['name']}")
            lines.append("")
            lines.append(f"- Blocking: {item['blocking']}")
            lines.append(f"- Description: {item['description']}")
            lines.append("")

        lines.append("## Manuscript Readiness Gate")
        lines.append("")
        gate = report["readiness_gate"]
        lines.append(f"- Gate id: {gate['gate_id']}")
        lines.append(f"- Gate scope: {gate['gate_scope']}")
        lines.append(f"- Gate decision: {gate['gate_decision']}")
        lines.append(f"- Approval recorded: {gate['approval_recorded']}")
        lines.append(f"- Submission ready: {gate['submission_ready']}")
        lines.append(f"- Theory validation claim made: {gate['theory_validation_claim_made']}")
        lines.append(f"- Hard requirement count: {gate['hard_requirement_count']}")
        lines.append(f"- Hard requirement passed count: {gate['hard_requirement_passed_count']}")
        lines.append(f"- Hard requirement failed count: {gate['hard_requirement_failed_count']}")
        lines.append(f"- Blocking limitation count: {gate['blocking_limitation_count']}")
        lines.append(f"- Decision reason: {gate['decision_reason']}")
        lines.append("")

        lines.append("## Gate Requirements")
        lines.append("")
        for item in gate["hard_requirements"]:
            lines.append(f"### {item['requirement_id']} - {item['name']}")
            lines.append("")
            lines.append(f"- Required value: {item['required_value']}")
            lines.append(f"- Actual value: {item['actual_value']}")
            lines.append(f"- Passed: {item['passed']}")
            lines.append("")

        lines.append("## Blocking Limitations")
        lines.append("")
        for item in gate["blocking_limitations"]:
            lines.append(f"- {item['limitation_id']}: {item['name']}")

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
        lines.append("V9_5_VIRUSE_FABRIC_TOY_EVIDENCE_LIMITATION_AND_MANUSCRIPT_READINESS_GATE_OK")
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


def build_viruse_fabric_toy_evidence_limitation_and_manuscript_readiness_gate() -> Dict[str, Any]:
    return ViruseFabricToyEvidenceLimitationAndManuscriptReadinessGateBuilder().run()


if __name__ == "__main__":
    result = build_viruse_fabric_toy_evidence_limitation_and_manuscript_readiness_gate()
    counters = result["counters"]
    gate = result["readiness_gate"]
    print("V9_5_VIRUSE_FABRIC_TOY_EVIDENCE_LIMITATION_AND_MANUSCRIPT_READINESS_GATE_OK")
    print("VIRUSE_FABRIC_TOY_EVIDENCE_LIMITATION_AND_MANUSCRIPT_READINESS_GATE_DIRECT_CHECK_OK")
    print(f"Toy evidence limitation analysis count: {counters['V9 toy evidence limitation analysis count']}")
    print(f"Manuscript readiness gate execution count: {counters['V9 manuscript readiness gate execution count']}")
    print(f"Manuscript readiness denial count: {counters['V9 manuscript readiness denial count']}")
    print(f"Manuscript readiness approval count: {counters['V9 manuscript readiness approval count']}")
    print(f"Hard requirement count: {counters['V9 readiness hard requirement count']}")
    print(f"Hard requirement passed count: {counters['V9 readiness hard requirement passed count']}")
    print(f"Hard requirement failed count: {counters['V9 readiness hard requirement failed count']}")
    print(f"Blocking evidence limitation count: {counters['V9 blocking evidence limitation count']}")
    print(f"Gate decision: {gate['gate_decision']}")
    print(f"Submission ready: {gate['submission_ready']}")
    print(f"Approval recorded: {gate['approval_recorded']}")
    print(f"Theory validation claim count: {counters['V9 theory validation claim count']}")
    print(f"Manuscript readiness claim count: {counters['V9 manuscript readiness claim count']}")
    print(f"External validation count: {counters['External validation count']}")
    print(f"Independent experiment count: {counters['Independent experiment count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {result['passed']}")
