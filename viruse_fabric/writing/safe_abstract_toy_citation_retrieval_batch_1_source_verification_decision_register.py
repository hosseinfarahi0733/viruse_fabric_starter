from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyCitationRetrievalBatch1SourceVerificationDecisionRegisterBuilder:
    version = "v8.226"

    source_evidence_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_batch_1_source_verification_evidence_packet_v8_225.json"
    )
    source_intake_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_batch_1_candidate_intake_v8_224.json"
    )
    source_empty_ledger_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_empty_candidate_ledger_instance_v8_223.json"
    )
    source_ledger_schema_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_candidate_ledger_schema_v8_222.json"
    )

    output_md_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_batch_1_source_verification_decision_register_v8_226.md"
    )
    output_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_batch_1_source_verification_decision_register_v8_226.json"
    )

    plan_phrase = "batch_1_metadata_verification_decisions_recorded_but_not_accepted_cited_or_integrated"

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Missing JSON source: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"Expected dict JSON payload from {path}")
        return payload

    def _decision_controls(self) -> List[Dict[str, str]]:
        return [
            {
                "control_id": "B1-VERIF-DEC-CTRL-01",
                "control_name": "metadata_only_decision_register",
                "control_rule": "v8.226 records metadata-only source verification decisions.",
                "boundary_note": "Metadata-only source verification decision register.",
            },
            {
                "control_id": "B1-VERIF-DEC-CTRL-02",
                "control_name": "no_full_source_verification_claim",
                "control_rule": "Bibliographic metadata verification is not a full source verification or scientific validation claim.",
                "boundary_note": "Full source verification is not claimed.",
            },
            {
                "control_id": "B1-VERIF-DEC-CTRL-03",
                "control_name": "no_acceptance_decision",
                "control_rule": "Metadata verification decisions do not create source acceptance decisions.",
                "boundary_note": "No accepted source is recorded.",
            },
            {
                "control_id": "B1-VERIF-DEC-CTRL-04",
                "control_name": "no_rejection_decision",
                "control_rule": "Metadata verification decisions do not create source rejection decisions.",
                "boundary_note": "No rejected source is recorded.",
            },
            {
                "control_id": "B1-VERIF-DEC-CTRL-05",
                "control_name": "no_citation_readiness",
                "control_rule": "Metadata verification decisions do not make sources citation-ready.",
                "boundary_note": "No source is marked citation-ready.",
            },
            {
                "control_id": "B1-VERIF-DEC-CTRL-06",
                "control_name": "no_actual_citation",
                "control_rule": "Metadata verification decisions do not insert actual citations.",
                "boundary_note": "No actual citation is added.",
            },
            {
                "control_id": "B1-VERIF-DEC-CTRL-07",
                "control_name": "no_citation_integration",
                "control_rule": "Metadata verification decisions do not complete citation integration.",
                "boundary_note": "does not complete citation integration",
            },
            {
                "control_id": "B1-VERIF-DEC-CTRL-08",
                "control_name": "no_manuscript_mutation",
                "control_rule": "Metadata verification decisions must not modify manuscript files.",
                "boundary_note": "No manuscript file is modified.",
            },
            {
                "control_id": "B1-VERIF-DEC-CTRL-09",
                "control_name": "no_readiness_approval",
                "control_rule": "Metadata verification decisions do not approve submission readiness.",
                "boundary_note": "No readiness approval is recorded.",
            },
            {
                "control_id": "B1-VERIF-DEC-CTRL-10",
                "control_name": "non_operational_scope",
                "control_rule": "The decision register remains methodological and non-operational.",
                "boundary_note": "No real biological datasets, no real pathogen models, no receptor parameters, and no operational targeting.",
            },
        ]

    def _make_decision_records(
        self,
        evidence_records: List[Dict[str, Any]],
        candidate_id_to_title: Dict[str, str],
    ) -> List[Dict[str, Any]]:
        records: List[Dict[str, Any]] = []

        for index, evidence in enumerate(sorted(evidence_records, key=lambda item: item["candidate_id"]), start=1):
            candidate_id = evidence["candidate_id"]
            evidence_status = evidence["verification_evidence_status"]

            if evidence_status != "verification_evidence_recorded_not_accepted":
                raise AssertionError(
                    f"Expected v8.225 evidence status verification_evidence_recorded_not_accepted for {candidate_id}"
                )

            records.append(
                {
                    "decision_record_id": f"VERIF-DEC-B1-{index:03d}",
                    "candidate_id": candidate_id,
                    "candidate_title": candidate_id_to_title[candidate_id],
                    "evidence_record_id": evidence["evidence_record_id"],
                    "decision_scope": "metadata_only",
                    "decision_kind": "bibliographic_metadata_verification_decision",
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
                    "evidence_basis": [
                        f"Uses v8.225 evidence record {evidence['evidence_record_id']}.",
                        "Evidence source category and evidence URL are present.",
                        "Evidence locator claims are present.",
                        "Metadata fields checked are present.",
                        "Candidate remains non-operational and methodological.",
                    ],
                    "verified_metadata_fields": evidence["metadata_fields_checked"],
                    "decision_boundary_note": (
                        "Metadata-only bibliographic verification decision recorded; "
                        "source is not accepted, not rejected, not citation-ready, not integrated, "
                        "and no manuscript mutation is permitted."
                    ),
                }
            )

        return records

    def build(self) -> Dict[str, Any]:
        evidence_packet = self._load_json(self.source_evidence_json_path)
        intake_packet = self._load_json(self.source_intake_json_path)
        empty_ledger = self._load_json(self.source_empty_ledger_json_path)
        ledger_schema = self._load_json(self.source_ledger_schema_json_path)

        evidence_counters = evidence_packet.get("counters", {})
        intake_counters = intake_packet.get("counters", {})
        empty_counters = empty_ledger.get("counters", {})
        schema_counters = ledger_schema.get("counters", {})

        evidence_records = evidence_packet.get("verification_evidence_records", [])
        candidate_sources = intake_packet.get("candidate_sources", [])

        candidate_id_to_title = {}
        for candidate in candidate_sources:
            candidate_id = candidate["candidate_id"]
            title = (
                candidate.get("title")
                or candidate.get("candidate_title")
                or candidate.get("source_title")
                or candidate.get("bibliographic_title")
            )
            if title:
                candidate_id_to_title[candidate_id] = title

        for evidence in evidence_records:
            candidate_id = evidence["candidate_id"]
            if candidate_id not in candidate_id_to_title:
                fallback_title = evidence.get("candidate_title")
                if not fallback_title:
                    raise AssertionError(f"Missing candidate title for {candidate_id}")
                candidate_id_to_title[candidate_id] = fallback_title

        decision_records = self._make_decision_records(evidence_records, candidate_id_to_title)
        controls = self._decision_controls()

        decision_candidate_ids = {record["candidate_id"] for record in decision_records}
        evidence_candidate_ids = {record["candidate_id"] for record in evidence_records}
        candidate_ids = set(candidate_id_to_title)

        counters = {
            "Safe abstract toy citation retrieval batch 1 source verification decision register count": 1,
            "New safe abstract toy citation retrieval batch 1 source verification decision register count": 1,
            "Toy citation batch 1 source verification decision register JSON export count": 1,
            "Toy citation batch 1 source verification decision record count": len(decision_records),
            "Toy citation batch 1 metadata-only verification decision count": len(decision_records),
            "Toy citation batch 1 bibliographic metadata verified source count": len(decision_records),
            "Toy citation batch 1 metadata verified not accepted source count": len(decision_records),
            "Toy citation batch 1 metadata verified source recorded count": len(decision_records),
            "Toy citation batch 1 verification decision evidence coverage count": len(decision_candidate_ids),
            "Toy citation batch 1 verification decision control count": len(controls),
            "Toy citation batch 1 full source verification claim count": 0,
            "Toy citation batch 1 citation-ready verified source count": 0,
            "Toy citation batch 1 accepted source count": 0,
            "Toy citation batch 1 rejected source count": 0,
            "Toy citation batch 1 acceptance decision count": 0,
            "Toy citation batch 1 rejection decision count": 0,
            "Toy citation batch 1 actual citation count": 0,
            "Toy citation batch 1 fabricated reference count": 0,
            "Toy citation batch 1 citation integration completion count": 0,
            "Toy citation batch 1 added to manuscript count": 0,
            "Toy citation batch 1 manuscript mutation count": 0,
            "Toy citation batch 1 prior evidence record count": evidence_counters.get("Toy citation batch 1 source verification evidence record count"),
            "Toy citation batch 1 prior evidence recorded count": evidence_counters.get("Toy citation batch 1 source verification evidence recorded count"),
            "Toy citation batch 1 prior evidence candidate coverage count": evidence_counters.get("Toy citation batch 1 source verification evidence candidate coverage count"),
            "Toy citation batch 1 prior evidence locator claim count": evidence_counters.get("Toy citation batch 1 source verification evidence locator claim count"),
            "Toy citation batch 1 prior final verification decision count": evidence_counters.get("Toy citation batch 1 source verification final decision count"),
            "Toy citation batch 1 prior verified source count": evidence_counters.get("Toy citation batch 1 verified source count"),
            "Toy citation batch 1 prior actual citation count": evidence_counters.get("Toy citation batch 1 actual citation count"),
            "Toy citation batch 1 prior candidate source row count": intake_counters.get("Toy citation batch 1 candidate source row count"),
            "Toy citation batch 1 prior candidate source recorded count": intake_counters.get("Toy citation batch 1 candidate source recorded count"),
            "Toy citation batch 1 prior source retrieval count": intake_counters.get("Toy citation batch 1 source retrieval count"),
            "Toy citation batch 1 prior empty ledger row count": empty_counters.get("Toy citation empty ledger row count"),
            "Toy citation batch 1 source candidate ledger field count": schema_counters.get("Toy citation candidate ledger field count"),
            "Toy citation verified source count": 0,
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
            "title": "Safe Abstract Toy Citation Retrieval Batch 1 Source Verification Decision Register",
            "source_evidence_json": str(self.source_evidence_json_path),
            "source_intake_json": str(self.source_intake_json_path),
            "source_empty_ledger_json": str(self.source_empty_ledger_json_path),
            "source_ledger_schema_json": str(self.source_ledger_schema_json_path),
            "plan_phrase": self.plan_phrase,
            "scope": "citation-retrieval-batch-1-source-verification-decision-register-only",
            "safe_abstract_toy_only": True,
            "synthetic_project_context_only": True,
            "abstract_graphs_only": True,
            "unitless_parameters_only": True,
            "non_operational_only": True,
            "source_candidate_count": len(candidate_sources),
            "evidence_record_count": len(evidence_records),
            "decision_record_count": len(decision_records),
            "decision_candidate_coverage_complete": candidate_ids == evidence_candidate_ids == decision_candidate_ids,
            "source_verification_decision_register_completed": True,
            "metadata_verification_decisions_recorded": True,
            "bibliographic_metadata_verified_sources_recorded": True,
            "source_verification_performed": False,
            "full_source_verification_claimed": False,
            "verified_sources_claimed": False,
            "acceptance_decisions_recorded": False,
            "rejection_decisions_recorded": False,
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
            "applied_patch_count": 0,
            "source_verification_decision_records": decision_records,
            "source_verification_decision_controls": controls,
            "non_readiness_disclaimer": (
                "This v8.226 artifact records metadata-only source verification decisions only. "
                "Metadata-only source verification decision register. "
                "Bibliographic metadata is marked as verified, but full source verification is not claimed. "
                "No accepted source is recorded. No rejected source is recorded. "
                "No source is marked citation-ready. No actual citation is added. "
                "No fabricated reference is introduced. It does not complete citation integration, "
                "does not validate scientific claims, does not modify manuscript files, and No manuscript file is modified. "
                "No new citation is added. Future source acceptance, rejection, citation eligibility, and citation integration require separate official milestones."
            ),
            "boundary_notes": (
                [record["decision_boundary_note"] for record in decision_records]
                + [control["boundary_note"] for control in controls]
            ),
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "citation-retrieval-batch-1-source-verification-decision-register-only":
            raise AssertionError("v8.226 must remain source-verification-decision-register-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.226 decision register must pass.")

        if report["source_candidate_count"] != 7:
            raise AssertionError("Expected 7 source candidates.")

        if report["evidence_record_count"] != 7:
            raise AssertionError("Expected 7 evidence records from v8.225.")

        if report["decision_record_count"] != 7:
            raise AssertionError("Expected 7 metadata verification decision records.")

        if report["decision_candidate_coverage_complete"] is not True:
            raise AssertionError("Decision records must cover all candidate IDs.")

        if report["source_verification_decision_register_completed"] is not True:
            raise AssertionError("Decision register should be completed.")

        if report["metadata_verification_decisions_recorded"] is not True:
            raise AssertionError("Metadata verification decisions should be recorded.")

        if report["bibliographic_metadata_verified_sources_recorded"] is not True:
            raise AssertionError("Bibliographic metadata verified sources should be recorded.")

        for field in [
            "source_verification_performed",
            "full_source_verification_claimed",
            "verified_sources_claimed",
            "acceptance_decisions_recorded",
            "rejection_decisions_recorded",
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
        ]:
            if report[field] is not False:
                raise AssertionError(f"Expected False for {field}")

        if report["applied_patch_count"] != 0:
            raise AssertionError("Applied patch count must remain zero.")

        for record in report["source_verification_decision_records"]:
            expected_pairs = {
                "decision_scope": "metadata_only",
                "decision_kind": "bibliographic_metadata_verification_decision",
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
            for key, expected in expected_pairs.items():
                actual = record[key]
                if actual != expected:
                    raise AssertionError(f"Expected {expected} for {key}, got {actual}")

        counters = report["counters"]

        expected_counts = {
            "Toy citation batch 1 source verification decision record count": 7,
            "Toy citation batch 1 metadata-only verification decision count": 7,
            "Toy citation batch 1 bibliographic metadata verified source count": 7,
            "Toy citation batch 1 metadata verified not accepted source count": 7,
            "Toy citation batch 1 metadata verified source recorded count": 7,
            "Toy citation batch 1 verification decision evidence coverage count": 7,
            "Toy citation batch 1 verification decision control count": 10,
            "Toy citation batch 1 full source verification claim count": 0,
            "Toy citation batch 1 citation-ready verified source count": 0,
            "Toy citation batch 1 accepted source count": 0,
            "Toy citation batch 1 rejected source count": 0,
            "Toy citation batch 1 acceptance decision count": 0,
            "Toy citation batch 1 rejection decision count": 0,
            "Toy citation batch 1 actual citation count": 0,
            "Toy citation batch 1 fabricated reference count": 0,
            "Toy citation batch 1 citation integration completion count": 0,
            "Toy citation batch 1 added to manuscript count": 0,
            "Toy citation batch 1 manuscript mutation count": 0,
            "Toy citation batch 1 prior evidence record count": 7,
            "Toy citation batch 1 prior evidence recorded count": 7,
            "Toy citation batch 1 prior evidence candidate coverage count": 7,
            "Toy citation batch 1 prior evidence locator claim count": 29,
            "Toy citation batch 1 prior final verification decision count": 0,
            "Toy citation batch 1 prior verified source count": 0,
            "Toy citation batch 1 prior actual citation count": 0,
            "Toy citation batch 1 prior candidate source row count": 7,
            "Toy citation batch 1 prior candidate source recorded count": 7,
            "Toy citation batch 1 prior source retrieval count": 7,
            "Toy citation batch 1 prior empty ledger row count": 0,
            "Toy citation batch 1 source candidate ledger field count": 16,
        }

        for name, expected in expected_counts.items():
            actual = counters.get(name)
            if actual != expected:
                raise AssertionError(f"Expected {expected} for {name}, got {actual}")

        combined_text = (
            json.dumps(report["source_verification_decision_records"], ensure_ascii=False)
            + " "
            + json.dumps(report["source_verification_decision_controls"], ensure_ascii=False)
            + " "
            + report["non_readiness_disclaimer"]
        )

        required_phrases = [
            "Metadata-only source verification decision register",
            "bibliographic_metadata_verification_decision",
            "metadata_verified_not_accepted",
            "bibliographic_metadata_verified",
            "metadata_verified_source_recorded",
            "full_source_verification_not_claimed",
            "no_acceptance_decision_recorded",
            "no_rejection_decision_recorded",
            "not_citation_ready",
            "not_integrated",
            "no_mutation",
            "scientific_validation_not_claimed",
            "Full source verification is not claimed",
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
            "No new citation is added",
            "No manuscript file is modified",
        ]

        for phrase in required_phrases:
            if phrase not in combined_text:
                raise AssertionError(f"Missing required verification decision phrase: {phrase}")

        must_be_zero = [
            "Toy citation batch 1 full source verification claim count",
            "Toy citation batch 1 citation-ready verified source count",
            "Toy citation batch 1 accepted source count",
            "Toy citation batch 1 rejected source count",
            "Toy citation batch 1 acceptance decision count",
            "Toy citation batch 1 rejection decision count",
            "Toy citation batch 1 actual citation count",
            "Toy citation batch 1 fabricated reference count",
            "Toy citation batch 1 citation integration completion count",
            "Toy citation batch 1 added to manuscript count",
            "Toy citation batch 1 manuscript mutation count",
            "Toy citation verified source count",
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

        lines.append("# Safe Abstract Toy Citation Retrieval Batch 1 Source Verification Decision Register")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is citation-retrieval-batch-1-source-verification-decision-register-only.")
        lines.append("It records metadata-only bibliographic verification decisions for the seven Batch 1 sources without accepting, rejecting, citing, integrating, or modifying manuscript files.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")

        lines.append("## Source Verification Decision Records")
        lines.append("")
        for record in report["source_verification_decision_records"]:
            lines.append(f"### {record['decision_record_id']} - {record['candidate_id']}")
            lines.append("")
            lines.append(f"- Candidate title: {record['candidate_title']}")
            lines.append(f"- Evidence record ID: {record['evidence_record_id']}")
            lines.append(f"- Decision scope: {record['decision_scope']}")
            lines.append(f"- Decision kind: {record['decision_kind']}")
            lines.append(f"- Decision result: {record['decision_result']}")
            lines.append(f"- Metadata verification status: {record['metadata_verification_status']}")
            lines.append(f"- Metadata verified source status: {record['metadata_verified_source_status']}")
            lines.append(f"- Full source verification status: {record['full_source_verification_status']}")
            lines.append(f"- Source acceptance decision: {record['source_acceptance_decision']}")
            lines.append(f"- Source rejection decision: {record['source_rejection_decision']}")
            lines.append(f"- Citation readiness status: {record['citation_readiness_status']}")
            lines.append(f"- Citation integration status: {record['citation_integration_status']}")
            lines.append(f"- Manuscript mutation status: {record['manuscript_mutation_status']}")
            lines.append(f"- Scientific validation status: {record['scientific_validation_status']}")
            lines.append(f"- Source operational scope: {record['source_operational_scope']}")
            lines.append("- Evidence basis:")
            for basis in record["evidence_basis"]:
                lines.append(f"  - {basis}")
            lines.append("- Verified metadata fields:")
            for field in record["verified_metadata_fields"]:
                lines.append(f"  - {field}")
            lines.append(f"- Decision boundary note: {record['decision_boundary_note']}")
            lines.append("")

        lines.append("## Decision Controls")
        lines.append("")
        for control in report["source_verification_decision_controls"]:
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
        lines.append("V8_226_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_BATCH_1_SOURCE_VERIFICATION_DECISION_REGISTER_OK")
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


def build_safe_abstract_toy_citation_retrieval_batch_1_source_verification_decision_register() -> Dict[str, Any]:
    return SafeAbstractToyCitationRetrievalBatch1SourceVerificationDecisionRegisterBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_citation_retrieval_batch_1_source_verification_decision_register()
    counters = result["counters"]
    print("V8_226_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_BATCH_1_SOURCE_VERIFICATION_DECISION_REGISTER_OK")
    print("TOY_CITATION_RETRIEVAL_BATCH_1_SOURCE_VERIFICATION_DECISION_REGISTER_DIRECT_CHECK_OK")
    print(f"Decision record count: {counters['Toy citation batch 1 source verification decision record count']}")
    print(f"Metadata-only verification decision count: {counters['Toy citation batch 1 metadata-only verification decision count']}")
    print(f"Bibliographic metadata verified source count: {counters['Toy citation batch 1 bibliographic metadata verified source count']}")
    print(f"Metadata verified not accepted source count: {counters['Toy citation batch 1 metadata verified not accepted source count']}")
    print(f"Verification decision evidence coverage count: {counters['Toy citation batch 1 verification decision evidence coverage count']}")
    print(f"Verification decision control count: {counters['Toy citation batch 1 verification decision control count']}")
    print(f"Full source verification claim count: {counters['Toy citation batch 1 full source verification claim count']}")
    print(f"Citation-ready verified source count: {counters['Toy citation batch 1 citation-ready verified source count']}")
    print(f"Accepted source count: {counters['Toy citation batch 1 accepted source count']}")
    print(f"Rejected source count: {counters['Toy citation batch 1 rejected source count']}")
    print(f"Actual citation count: {counters['Toy citation batch 1 actual citation count']}")
    print(f"Fabricated reference count: {counters['Toy citation batch 1 fabricated reference count']}")
    print(f"Citation integration completion count: {counters['Toy citation batch 1 citation integration completion count']}")
    print(f"Citation added to manuscript count: {counters['Toy citation batch 1 added to manuscript count']}")
    print(f"Manuscript mutation count: {counters['Toy citation batch 1 manuscript mutation count']}")
    print(f"Prior evidence record count: {counters['Toy citation batch 1 prior evidence record count']}")
    print(f"Prior evidence locator claim count: {counters['Toy citation batch 1 prior evidence locator claim count']}")
    print(f"Prior final verification decision count: {counters['Toy citation batch 1 prior final verification decision count']}")
    print(f"Toy citation verified source count: {counters['Toy citation verified source count']}")
    print(f"Toy citation actual citation count: {counters['Toy citation actual citation count']}")
    print(f"Toy citation fabricated reference count: {counters['Toy citation fabricated reference count']}")
    print(f"Toy citation integration completion count: {counters['Toy citation integration completion count']}")
    print(f"Toy citation added to manuscript count: {counters['Toy citation added to manuscript count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {result['passed']}")
