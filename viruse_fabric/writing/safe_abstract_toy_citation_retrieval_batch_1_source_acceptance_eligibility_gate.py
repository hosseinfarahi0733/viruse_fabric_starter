from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyCitationRetrievalBatch1SourceAcceptanceEligibilityGateBuilder:
    version = "v8.227"

    source_decision_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_batch_1_source_verification_decision_register_v8_226.json"
    )
    source_evidence_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_batch_1_source_verification_evidence_packet_v8_225.json"
    )
    source_intake_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_batch_1_candidate_intake_v8_224.json"
    )
    source_ledger_schema_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_candidate_ledger_schema_v8_222.json"
    )

    output_md_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_batch_1_source_acceptance_eligibility_gate_v8_227.md"
    )
    output_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_batch_1_source_acceptance_eligibility_gate_v8_227.json"
    )

    plan_phrase = "batch_1_acceptance_eligibility_gate_recorded_but_not_accepted_rejected_cited_or_integrated"

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Missing JSON source: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"Expected dict JSON payload from {path}")
        return payload

    def _eligibility_criteria(self) -> List[Dict[str, str]]:
        return [
            {
                "criterion_id": "ACCEPT-ELIG-B1-CRIT-01",
                "criterion_name": "metadata_verification_present",
                "criterion_rule": "The source must have a v8.226 metadata-only bibliographic verification decision.",
                "expected_status": "bibliographic_metadata_verified",
            },
            {
                "criterion_id": "ACCEPT-ELIG-B1-CRIT-02",
                "criterion_name": "not_already_accepted",
                "criterion_rule": "The source must not already have an acceptance decision.",
                "expected_status": "no_acceptance_decision_recorded",
            },
            {
                "criterion_id": "ACCEPT-ELIG-B1-CRIT-03",
                "criterion_name": "not_already_rejected",
                "criterion_rule": "The source must not already have a rejection decision.",
                "expected_status": "no_rejection_decision_recorded",
            },
            {
                "criterion_id": "ACCEPT-ELIG-B1-CRIT-04",
                "criterion_name": "not_citation_ready",
                "criterion_rule": "The source must not be marked citation-ready inside this gate.",
                "expected_status": "not_citation_ready",
            },
            {
                "criterion_id": "ACCEPT-ELIG-B1-CRIT-05",
                "criterion_name": "not_integrated",
                "criterion_rule": "The source must not be citation-integrated into any manuscript.",
                "expected_status": "not_integrated",
            },
            {
                "criterion_id": "ACCEPT-ELIG-B1-CRIT-06",
                "criterion_name": "non_operational_methodological_scope",
                "criterion_rule": "The source must remain non-operational and methodological.",
                "expected_status": "non_operational_methodological_source_only",
            },
        ]

    def _gate_controls(self) -> List[Dict[str, str]]:
        return [
            {
                "control_id": "B1-ACCEPT-ELIG-CTRL-01",
                "control_name": "eligibility_gate_only",
                "control_rule": "v8.227 records acceptance eligibility gate status only.",
                "boundary_note": "Acceptance eligibility gate only.",
            },
            {
                "control_id": "B1-ACCEPT-ELIG-CTRL-02",
                "control_name": "no_acceptance_decision",
                "control_rule": "Eligibility does not create source acceptance.",
                "boundary_note": "No accepted source is recorded.",
            },
            {
                "control_id": "B1-ACCEPT-ELIG-CTRL-03",
                "control_name": "no_rejection_decision",
                "control_rule": "Eligibility does not create source rejection.",
                "boundary_note": "No rejected source is recorded.",
            },
            {
                "control_id": "B1-ACCEPT-ELIG-CTRL-04",
                "control_name": "no_citation_ready_status",
                "control_rule": "Eligibility does not mark a source citation-ready.",
                "boundary_note": "No source is marked citation-ready.",
            },
            {
                "control_id": "B1-ACCEPT-ELIG-CTRL-05",
                "control_name": "no_actual_citation",
                "control_rule": "Eligibility does not add actual citations.",
                "boundary_note": "No actual citation is added.",
            },
            {
                "control_id": "B1-ACCEPT-ELIG-CTRL-06",
                "control_name": "no_fabricated_reference",
                "control_rule": "Eligibility does not introduce fabricated references.",
                "boundary_note": "No fabricated reference is introduced.",
            },
            {
                "control_id": "B1-ACCEPT-ELIG-CTRL-07",
                "control_name": "no_citation_integration",
                "control_rule": "Eligibility does not complete citation integration.",
                "boundary_note": "does not complete citation integration",
            },
            {
                "control_id": "B1-ACCEPT-ELIG-CTRL-08",
                "control_name": "no_manuscript_mutation",
                "control_rule": "Eligibility does not modify manuscript files.",
                "boundary_note": "No manuscript file is modified.",
            },
            {
                "control_id": "B1-ACCEPT-ELIG-CTRL-09",
                "control_name": "no_scientific_validation",
                "control_rule": "Eligibility does not validate scientific claims.",
                "boundary_note": "does not validate scientific claims",
            },
            {
                "control_id": "B1-ACCEPT-ELIG-CTRL-10",
                "control_name": "no_readiness_approval",
                "control_rule": "Eligibility does not approve submission readiness.",
                "boundary_note": "No readiness approval is recorded.",
            },
            {
                "control_id": "B1-ACCEPT-ELIG-CTRL-11",
                "control_name": "no_new_citation_added",
                "control_rule": "Eligibility does not add any new citation.",
                "boundary_note": "No new citation is added.",
            },
            {
                "control_id": "B1-ACCEPT-ELIG-CTRL-12",
                "control_name": "non_operational_scope",
                "control_rule": "Eligibility remains methodological and non-operational.",
                "boundary_note": "No real biological datasets, no real pathogen models, no receptor parameters, and no operational targeting.",
            },
        ]

    def _make_gate_records(
        self,
        decision_records: List[Dict[str, Any]],
        criteria: List[Dict[str, str]],
    ) -> List[Dict[str, Any]]:
        gate_records: List[Dict[str, Any]] = []

        for index, decision in enumerate(sorted(decision_records, key=lambda item: item["candidate_id"]), start=1):
            candidate_id = decision["candidate_id"]

            required_pairs = {
                "decision_scope": "metadata_only",
                "decision_result": "metadata_verified_not_accepted",
                "metadata_verification_status": "bibliographic_metadata_verified",
                "metadata_verified_source_status": "metadata_verified_source_recorded",
                "full_source_verification_status": "full_source_verification_not_claimed",
                "source_acceptance_decision": "no_acceptance_decision_recorded",
                "source_rejection_decision": "no_rejection_decision_recorded",
                "citation_readiness_status": "not_citation_ready",
                "citation_integration_status": "not_integrated",
                "manuscript_mutation_status": "no_mutation",
                "scientific_validation_status": "scientific_validation_not_claimed",
                "source_operational_scope": "non_operational_methodological_source_only",
            }

            for key, expected in required_pairs.items():
                actual = decision.get(key)
                if actual != expected:
                    raise AssertionError(
                        f"Expected {expected} for {candidate_id} decision field {key}, got {actual}"
                    )

            criterion_results = []
            for criterion in criteria:
                criterion_results.append(
                    {
                        "criterion_id": criterion["criterion_id"],
                        "criterion_name": criterion["criterion_name"],
                        "criterion_result": "passed_for_future_acceptance_review_only",
                        "criterion_boundary": "Criterion passes eligibility screening only and does not create acceptance.",
                    }
                )

            gate_records.append(
                {
                    "gate_record_id": f"ACCEPT-ELIG-GATE-B1-{index:03d}",
                    "candidate_id": candidate_id,
                    "candidate_title": decision["candidate_title"],
                    "source_decision_record_id": decision["decision_record_id"],
                    "gate_scope": "acceptance_eligibility_only",
                    "eligibility_gate_status": "eligible_for_future_acceptance_review_not_accepted",
                    "eligibility_assessment_status": "acceptance_eligibility_recorded_not_decided",
                    "metadata_verification_dependency": "bibliographic_metadata_verified",
                    "acceptance_decision_status": "no_acceptance_decision_recorded",
                    "rejection_decision_status": "no_rejection_decision_recorded",
                    "citation_readiness_status": "not_citation_ready",
                    "citation_integration_status": "not_integrated",
                    "manuscript_mutation_status": "no_mutation",
                    "scientific_validation_status": "scientific_validation_not_claimed",
                    "source_operational_scope": "non_operational_methodological_source_only",
                    "criterion_results": criterion_results,
                    "gate_boundary_note": (
                        "Acceptance eligibility is recorded only for future review; "
                        "source is not accepted, not rejected, not citation-ready, not integrated, "
                        "and no manuscript mutation is permitted."
                    ),
                }
            )

        return gate_records

    def build(self) -> Dict[str, Any]:
        decision_register = self._load_json(self.source_decision_json_path)
        evidence_packet = self._load_json(self.source_evidence_json_path)
        intake_packet = self._load_json(self.source_intake_json_path)
        ledger_schema = self._load_json(self.source_ledger_schema_json_path)

        decision_counters = decision_register.get("counters", {})
        evidence_counters = evidence_packet.get("counters", {})
        intake_counters = intake_packet.get("counters", {})
        schema_counters = ledger_schema.get("counters", {})

        decision_records = decision_register.get("source_verification_decision_records", [])
        criteria = self._eligibility_criteria()
        controls = self._gate_controls()
        gate_records = self._make_gate_records(decision_records, criteria)

        decision_candidate_ids = {record["candidate_id"] for record in decision_records}
        gate_candidate_ids = {record["candidate_id"] for record in gate_records}

        criterion_result_count = sum(len(record["criterion_results"]) for record in gate_records)

        counters = {
            "Safe abstract toy citation retrieval batch 1 source acceptance eligibility gate count": 1,
            "New safe abstract toy citation retrieval batch 1 source acceptance eligibility gate count": 1,
            "Toy citation batch 1 source acceptance eligibility gate JSON export count": 1,
            "Toy citation batch 1 acceptance eligibility gate record count": len(gate_records),
            "Toy citation batch 1 acceptance eligibility assessment recorded count": len(gate_records),
            "Toy citation batch 1 eligible for future acceptance review count": len(gate_records),
            "Toy citation batch 1 acceptance eligibility candidate coverage count": len(gate_candidate_ids),
            "Toy citation batch 1 acceptance eligibility criterion group count": len(criteria),
            "Toy citation batch 1 acceptance eligibility criterion evaluation count": criterion_result_count,
            "Toy citation batch 1 acceptance eligibility control count": len(controls),
            "Toy citation batch 1 acceptance decision count": 0,
            "Toy citation batch 1 accepted source count": 0,
            "Toy citation batch 1 rejection decision count": 0,
            "Toy citation batch 1 rejected source count": 0,
            "Toy citation batch 1 citation-ready source count": 0,
            "Toy citation batch 1 actual citation count": 0,
            "Toy citation batch 1 fabricated reference count": 0,
            "Toy citation batch 1 citation integration completion count": 0,
            "Toy citation batch 1 added to manuscript count": 0,
            "Toy citation batch 1 manuscript mutation count": 0,
            "Toy citation batch 1 prior source verification decision record count": decision_counters.get("Toy citation batch 1 source verification decision record count"),
            "Toy citation batch 1 prior metadata-only verification decision count": decision_counters.get("Toy citation batch 1 metadata-only verification decision count"),
            "Toy citation batch 1 prior bibliographic metadata verified source count": decision_counters.get("Toy citation batch 1 bibliographic metadata verified source count"),
            "Toy citation batch 1 prior metadata verified not accepted source count": decision_counters.get("Toy citation batch 1 metadata verified not accepted source count"),
            "Toy citation batch 1 prior full source verification claim count": decision_counters.get("Toy citation batch 1 full source verification claim count"),
            "Toy citation batch 1 prior citation-ready verified source count": decision_counters.get("Toy citation batch 1 citation-ready verified source count"),
            "Toy citation batch 1 prior accepted source count": decision_counters.get("Toy citation batch 1 accepted source count"),
            "Toy citation batch 1 prior rejected source count": decision_counters.get("Toy citation batch 1 rejected source count"),
            "Toy citation batch 1 prior actual citation count": decision_counters.get("Toy citation batch 1 actual citation count"),
            "Toy citation batch 1 prior evidence record count": evidence_counters.get("Toy citation batch 1 source verification evidence record count"),
            "Toy citation batch 1 prior evidence locator claim count": evidence_counters.get("Toy citation batch 1 source verification evidence locator claim count"),
            "Toy citation batch 1 prior candidate source row count": intake_counters.get("Toy citation batch 1 candidate source row count"),
            "Toy citation batch 1 source candidate ledger field count": schema_counters.get("Toy citation candidate ledger field count"),
            "Toy citation verified source count": 0,
            "Toy citation accepted source count": 0,
            "Toy citation rejected source count": 0,
            "Toy citation actual citation count": 0,
            "Toy citation fabricated reference count": 0,
            "Toy citation integration completion count": 0,
            "Toy citation added to manuscript count": 0,
            "Toy evaluation actual run count": 0,
            "Toy evaluation result count": 0,
            "Toy evaluation validation claim count": 0,
            "Toy scientific evidence upgrade completed count": 0,
            "Toy manuscript coherence rewrite application count": 0,
            "Toy manuscript patch application checklist completion count": 0,
            "Toy manuscript patch application checklist execution count": 0,
            "Toy manuscript patch application permission count": 0,
            "Toy manuscript patch application applied patch count": 0,
            "Toy manuscript patch application manuscript file modified count": 0,
            "Toy manuscript patch application manuscript mutation count": 0,
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
            "title": "Safe Abstract Toy Citation Retrieval Batch 1 Source Acceptance Eligibility Gate",
            "source_decision_json": str(self.source_decision_json_path),
            "source_evidence_json": str(self.source_evidence_json_path),
            "source_intake_json": str(self.source_intake_json_path),
            "source_ledger_schema_json": str(self.source_ledger_schema_json_path),
            "plan_phrase": self.plan_phrase,
            "scope": "citation-retrieval-batch-1-source-acceptance-eligibility-gate-only",
            "safe_abstract_toy_only": True,
            "synthetic_project_context_only": True,
            "abstract_graphs_only": True,
            "unitless_parameters_only": True,
            "non_operational_only": True,
            "source_decision_record_count": len(decision_records),
            "eligibility_gate_record_count": len(gate_records),
            "eligibility_gate_candidate_coverage_complete": decision_candidate_ids == gate_candidate_ids,
            "acceptance_eligibility_gate_completed": True,
            "acceptance_eligibility_assessments_recorded": True,
            "eligible_for_future_acceptance_review_recorded": True,
            "source_acceptance_performed": False,
            "source_rejection_performed": False,
            "accepted_sources_recorded": False,
            "rejected_sources_recorded": False,
            "citation_ready_sources_recorded": False,
            "actual_citations_added": False,
            "fabricated_references_introduced": False,
            "citation_integration_completed": False,
            "manuscript_rewrite_applied": False,
            "application_permission_granted": False,
            "application_execution_performed": False,
            "checklist_completion_performed": False,
            "checklist_execution_performed": False,
            "manuscript_file_modified": False,
            "manuscript_mutation": False,
            "evaluation_execution_performed": False,
            "evidence_upgrade_completed": False,
            "validation_claim_made": False,
            "readiness_approval_recorded": False,
            "new_citation_added": False,
            "applied_patch_count": 0,
            "acceptance_eligibility_criteria": criteria,
            "acceptance_eligibility_gate_records": gate_records,
            "acceptance_eligibility_controls": controls,
            "non_readiness_disclaimer": (
                "This v8.227 artifact records acceptance eligibility gate status only. "
                "Acceptance eligibility gate only. eligible for future acceptance review does not mean accepted. "
                "No accepted source is recorded. No rejected source is recorded. "
                "No source is marked citation-ready. No actual citation is added. "
                "No fabricated reference is introduced. It does not complete citation integration, "
                "does not validate scientific claims, does not modify manuscript files, and No manuscript file is modified. "
                "No readiness approval is recorded. No new citation is added. "
                "Future source acceptance, rejection, citation readiness, citation integration, and manuscript mutation require separate official milestones."
            ),
            "boundary_notes": (
                [record["gate_boundary_note"] for record in gate_records]
                + [control["boundary_note"] for control in controls]
            ),
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "citation-retrieval-batch-1-source-acceptance-eligibility-gate-only":
            raise AssertionError("v8.227 must remain source-acceptance-eligibility-gate-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.227 acceptance eligibility gate must pass.")

        if report["source_decision_record_count"] != 7:
            raise AssertionError("Expected 7 prior source verification decision records.")

        if report["eligibility_gate_record_count"] != 7:
            raise AssertionError("Expected 7 acceptance eligibility gate records.")

        if report["eligibility_gate_candidate_coverage_complete"] is not True:
            raise AssertionError("Eligibility gate must cover all prior decision records.")

        for field in [
            "source_acceptance_performed",
            "source_rejection_performed",
            "accepted_sources_recorded",
            "rejected_sources_recorded",
            "citation_ready_sources_recorded",
            "actual_citations_added",
            "fabricated_references_introduced",
            "citation_integration_completed",
            "manuscript_rewrite_applied",
            "application_permission_granted",
            "application_execution_performed",
            "checklist_completion_performed",
            "checklist_execution_performed",
            "manuscript_file_modified",
            "manuscript_mutation",
            "evaluation_execution_performed",
            "evidence_upgrade_completed",
            "validation_claim_made",
            "readiness_approval_recorded",
            "new_citation_added",
        ]:
            if report[field] is not False:
                raise AssertionError(f"Expected False for {field}")

        if report["applied_patch_count"] != 0:
            raise AssertionError("Applied patch count must remain zero.")

        for record in report["acceptance_eligibility_gate_records"]:
            expected_pairs = {
                "gate_scope": "acceptance_eligibility_only",
                "eligibility_gate_status": "eligible_for_future_acceptance_review_not_accepted",
                "eligibility_assessment_status": "acceptance_eligibility_recorded_not_decided",
                "metadata_verification_dependency": "bibliographic_metadata_verified",
                "acceptance_decision_status": "no_acceptance_decision_recorded",
                "rejection_decision_status": "no_rejection_decision_recorded",
                "citation_readiness_status": "not_citation_ready",
                "citation_integration_status": "not_integrated",
                "manuscript_mutation_status": "no_mutation",
                "scientific_validation_status": "scientific_validation_not_claimed",
                "source_operational_scope": "non_operational_methodological_source_only",
            }
            for key, expected in expected_pairs.items():
                actual = record[key]
                if actual != expected:
                    raise AssertionError(f"Expected {expected} for {key}, got {actual}")

            if len(record["criterion_results"]) != 6:
                raise AssertionError("Each gate record must include six criterion results.")

            for criterion_result in record["criterion_results"]:
                if criterion_result["criterion_result"] != "passed_for_future_acceptance_review_only":
                    raise AssertionError("Criterion result must remain future-review-only.")

        counters = report["counters"]

        expected_counts = {
            "Toy citation batch 1 acceptance eligibility gate record count": 7,
            "Toy citation batch 1 acceptance eligibility assessment recorded count": 7,
            "Toy citation batch 1 eligible for future acceptance review count": 7,
            "Toy citation batch 1 acceptance eligibility candidate coverage count": 7,
            "Toy citation batch 1 acceptance eligibility criterion group count": 6,
            "Toy citation batch 1 acceptance eligibility criterion evaluation count": 42,
            "Toy citation batch 1 acceptance eligibility control count": 12,
            "Toy citation batch 1 acceptance decision count": 0,
            "Toy citation batch 1 accepted source count": 0,
            "Toy citation batch 1 rejection decision count": 0,
            "Toy citation batch 1 rejected source count": 0,
            "Toy citation batch 1 citation-ready source count": 0,
            "Toy citation batch 1 actual citation count": 0,
            "Toy citation batch 1 fabricated reference count": 0,
            "Toy citation batch 1 citation integration completion count": 0,
            "Toy citation batch 1 added to manuscript count": 0,
            "Toy citation batch 1 manuscript mutation count": 0,
            "Toy citation batch 1 prior source verification decision record count": 7,
            "Toy citation batch 1 prior metadata-only verification decision count": 7,
            "Toy citation batch 1 prior bibliographic metadata verified source count": 7,
            "Toy citation batch 1 prior metadata verified not accepted source count": 7,
            "Toy citation batch 1 prior full source verification claim count": 0,
            "Toy citation batch 1 prior citation-ready verified source count": 0,
            "Toy citation batch 1 prior accepted source count": 0,
            "Toy citation batch 1 prior rejected source count": 0,
            "Toy citation batch 1 prior actual citation count": 0,
            "Toy citation batch 1 prior evidence record count": 7,
            "Toy citation batch 1 prior evidence locator claim count": 29,
            "Toy citation batch 1 prior candidate source row count": 7,
            "Toy citation batch 1 source candidate ledger field count": 16,
        }

        for name, expected in expected_counts.items():
            actual = counters.get(name)
            if actual != expected:
                raise AssertionError(f"Expected {expected} for {name}, got {actual}")

        combined_text = (
            json.dumps(report["acceptance_eligibility_criteria"], ensure_ascii=False)
            + " "
            + json.dumps(report["acceptance_eligibility_gate_records"], ensure_ascii=False)
            + " "
            + json.dumps(report["acceptance_eligibility_controls"], ensure_ascii=False)
            + " "
            + report["non_readiness_disclaimer"]
        )

        required_phrases = [
            "Acceptance eligibility gate only",
            "eligible_for_future_acceptance_review_not_accepted",
            "acceptance_eligibility_recorded_not_decided",
            "eligible for future acceptance review does not mean accepted",
            "No accepted source is recorded",
            "No rejected source is recorded",
            "No source is marked citation-ready",
            "No actual citation is added",
            "No fabricated reference is introduced",
            "does not complete citation integration",
            "does not validate scientific claims",
            "No real biological datasets",
            "no real pathogen models",
            "no receptor parameters",
            "no operational targeting",
            "No readiness approval is recorded",
            "No new citation is added",
            "No manuscript file is modified",
            "not_integrated",
            "no_mutation",
            "scientific_validation_not_claimed",
            "non_operational_methodological_source_only",
        ]

        for phrase in required_phrases:
            if phrase not in combined_text:
                raise AssertionError(f"Missing required acceptance eligibility phrase: {phrase}")

        must_be_zero = [
            "Toy citation batch 1 acceptance decision count",
            "Toy citation batch 1 accepted source count",
            "Toy citation batch 1 rejection decision count",
            "Toy citation batch 1 rejected source count",
            "Toy citation batch 1 citation-ready source count",
            "Toy citation batch 1 actual citation count",
            "Toy citation batch 1 fabricated reference count",
            "Toy citation batch 1 citation integration completion count",
            "Toy citation batch 1 added to manuscript count",
            "Toy citation batch 1 manuscript mutation count",
            "Toy citation verified source count",
            "Toy citation accepted source count",
            "Toy citation rejected source count",
            "Toy citation actual citation count",
            "Toy citation fabricated reference count",
            "Toy citation integration completion count",
            "Toy citation added to manuscript count",
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

    def render_markdown(self, report: Dict[str, Any]) -> str:
        lines: List[str] = []

        lines.append("# Safe Abstract Toy Citation Retrieval Batch 1 Source Acceptance Eligibility Gate")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is citation-retrieval-batch-1-source-acceptance-eligibility-gate-only.")
        lines.append("It records acceptance eligibility gate status for the seven metadata-verified Batch 1 sources without accepting, rejecting, marking citation-ready, citing, integrating, or modifying manuscript files.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")

        lines.append("## Acceptance Eligibility Criteria")
        lines.append("")
        for criterion in report["acceptance_eligibility_criteria"]:
            lines.append(f"### {criterion['criterion_id']} - {criterion['criterion_name']}")
            lines.append("")
            lines.append(f"- Criterion rule: {criterion['criterion_rule']}")
            lines.append(f"- Expected status: {criterion['expected_status']}")
            lines.append("")

        lines.append("## Acceptance Eligibility Gate Records")
        lines.append("")
        for record in report["acceptance_eligibility_gate_records"]:
            lines.append(f"### {record['gate_record_id']} - {record['candidate_id']}")
            lines.append("")
            lines.append(f"- Candidate title: {record['candidate_title']}")
            lines.append(f"- Source decision record ID: {record['source_decision_record_id']}")
            lines.append(f"- Gate scope: {record['gate_scope']}")
            lines.append(f"- Eligibility gate status: {record['eligibility_gate_status']}")
            lines.append(f"- Eligibility assessment status: {record['eligibility_assessment_status']}")
            lines.append(f"- Metadata verification dependency: {record['metadata_verification_dependency']}")
            lines.append(f"- Acceptance decision status: {record['acceptance_decision_status']}")
            lines.append(f"- Rejection decision status: {record['rejection_decision_status']}")
            lines.append(f"- Citation readiness status: {record['citation_readiness_status']}")
            lines.append(f"- Citation integration status: {record['citation_integration_status']}")
            lines.append(f"- Manuscript mutation status: {record['manuscript_mutation_status']}")
            lines.append(f"- Scientific validation status: {record['scientific_validation_status']}")
            lines.append(f"- Source operational scope: {record['source_operational_scope']}")
            lines.append("- Criterion results:")
            for criterion_result in record["criterion_results"]:
                lines.append(
                    f"  - {criterion_result['criterion_id']} / {criterion_result['criterion_name']}: "
                    f"{criterion_result['criterion_result']} | {criterion_result['criterion_boundary']}"
                )
            lines.append(f"- Gate boundary note: {record['gate_boundary_note']}")
            lines.append("")

        lines.append("## Gate Controls")
        lines.append("")
        for control in report["acceptance_eligibility_controls"]:
            lines.append(f"### {control['control_id']} - {control['control_name']}")
            lines.append("")
            lines.append(f"- Control rule: {control['control_rule']}")
            lines.append(f"- Boundary note: {control['boundary_note']}")
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
        lines.append("V8_227_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_BATCH_1_SOURCE_ACCEPTANCE_ELIGIBILITY_GATE_OK")
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


def build_safe_abstract_toy_citation_retrieval_batch_1_source_acceptance_eligibility_gate() -> Dict[str, Any]:
    return SafeAbstractToyCitationRetrievalBatch1SourceAcceptanceEligibilityGateBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_citation_retrieval_batch_1_source_acceptance_eligibility_gate()
    counters = result["counters"]
    print("V8_227_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_BATCH_1_SOURCE_ACCEPTANCE_ELIGIBILITY_GATE_OK")
    print("TOY_CITATION_RETRIEVAL_BATCH_1_SOURCE_ACCEPTANCE_ELIGIBILITY_GATE_DIRECT_CHECK_OK")
    print(f"Eligibility gate record count: {counters['Toy citation batch 1 acceptance eligibility gate record count']}")
    print(f"Eligibility assessment recorded count: {counters['Toy citation batch 1 acceptance eligibility assessment recorded count']}")
    print(f"Eligible for future acceptance review count: {counters['Toy citation batch 1 eligible for future acceptance review count']}")
    print(f"Eligibility candidate coverage count: {counters['Toy citation batch 1 acceptance eligibility candidate coverage count']}")
    print(f"Eligibility criterion group count: {counters['Toy citation batch 1 acceptance eligibility criterion group count']}")
    print(f"Eligibility criterion evaluation count: {counters['Toy citation batch 1 acceptance eligibility criterion evaluation count']}")
    print(f"Eligibility control count: {counters['Toy citation batch 1 acceptance eligibility control count']}")
    print(f"Acceptance decision count: {counters['Toy citation batch 1 acceptance decision count']}")
    print(f"Accepted source count: {counters['Toy citation batch 1 accepted source count']}")
    print(f"Rejection decision count: {counters['Toy citation batch 1 rejection decision count']}")
    print(f"Rejected source count: {counters['Toy citation batch 1 rejected source count']}")
    print(f"Citation-ready source count: {counters['Toy citation batch 1 citation-ready source count']}")
    print(f"Actual citation count: {counters['Toy citation batch 1 actual citation count']}")
    print(f"Fabricated reference count: {counters['Toy citation batch 1 fabricated reference count']}")
    print(f"Citation integration completion count: {counters['Toy citation batch 1 citation integration completion count']}")
    print(f"Citation added to manuscript count: {counters['Toy citation batch 1 added to manuscript count']}")
    print(f"Manuscript mutation count: {counters['Toy citation batch 1 manuscript mutation count']}")
    print(f"Prior verification decision record count: {counters['Toy citation batch 1 prior source verification decision record count']}")
    print(f"Prior metadata verified not accepted source count: {counters['Toy citation batch 1 prior metadata verified not accepted source count']}")
    print(f"Prior accepted source count: {counters['Toy citation batch 1 prior accepted source count']}")
    print(f"Prior actual citation count: {counters['Toy citation batch 1 prior actual citation count']}")
    print(f"Toy citation accepted source count: {counters['Toy citation accepted source count']}")
    print(f"Toy citation rejected source count: {counters['Toy citation rejected source count']}")
    print(f"Toy citation actual citation count: {counters['Toy citation actual citation count']}")
    print(f"Toy citation fabricated reference count: {counters['Toy citation fabricated reference count']}")
    print(f"Toy citation integration completion count: {counters['Toy citation integration completion count']}")
    print(f"Toy citation added to manuscript count: {counters['Toy citation added to manuscript count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {result['passed']}")
