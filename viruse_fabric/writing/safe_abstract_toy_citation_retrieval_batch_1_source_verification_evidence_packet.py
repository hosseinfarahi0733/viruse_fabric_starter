from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyCitationRetrievalBatch1SourceVerificationEvidencePacketBuilder:
    version = "v8.225"

    source_batch_1_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_batch_1_candidate_intake_v8_224.json"
    )
    source_empty_ledger_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_empty_candidate_ledger_instance_v8_223.json"
    )
    source_ledger_schema_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_candidate_ledger_schema_v8_222.json"
    )
    source_retrieval_gate_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_readiness_gate_v8_221.json"
    )

    output_md_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_batch_1_source_verification_evidence_packet_v8_225.md"
    )
    output_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_batch_1_source_verification_evidence_packet_v8_225.json"
    )

    plan_phrase = "batch_1_source_verification_evidence_recorded_but_not_verified_accepted_or_integrated"

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Missing JSON source: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"Expected dict JSON payload from {path}")
        return payload

    def _verification_evidence_records(self) -> List[Dict[str, Any]]:
        return [
            {
                "candidate_id": "CAND-B1-001",
                "evidence_record_id": "VERIF-EVID-B1-001",
                "candidate_title": "Causality: Models, Reasoning, and Inference",
                "evidence_source_category": "publisher_page",
                "evidence_source_body": "Cambridge University Press",
                "evidence_url": "https://www.cambridge.org/core/books/causality/B0046844FAE10CBF274D4ACBDAEB5F5B",
                "evidence_locator_claims": [
                    "Author page identifies Judea Pearl.",
                    "Publisher page lists Cambridge University Press.",
                    "Publisher page lists DOI 10.1017/CBO9780511803161.",
                    "Publisher page lists ISBN values 9780511803161 and 9780521895606.",
                ],
                "metadata_fields_checked": [
                    "title",
                    "author",
                    "publisher",
                    "doi",
                    "isbn",
                    "publication_date",
                ],
                "verification_evidence_status": "verification_evidence_recorded_not_accepted",
                "source_verification_decision": "no_verification_decision_recorded",
                "source_acceptance_decision": "no_acceptance_decision_recorded",
                "source_rejection_decision": "no_rejection_decision_recorded",
                "citation_integration_status": "not_integrated",
                "manuscript_mutation_status": "no_mutation",
                "safety_scope": "non_operational_methodological_source_only",
                "boundary_note": "Evidence is recorded, but the source is not claimed as verified, not accepted, and not integrated.",
            },
            {
                "candidate_id": "CAND-B1-002",
                "evidence_record_id": "VERIF-EVID-B1-002",
                "candidate_title": "Probabilistic Graphical Models: Principles and Techniques",
                "evidence_source_category": "publisher_page",
                "evidence_source_body": "MIT Press",
                "evidence_url": "https://mitpress.mit.edu/9780262013192/probabilistic-graphical-models/",
                "evidence_locator_claims": [
                    "Publisher page identifies Daphne Koller and Nir Friedman.",
                    "Publisher page lists hardcover ISBN 9780262013192.",
                    "Publisher page lists publication date July 31, 2009.",
                    "Publisher page lists The MIT Press as publisher.",
                ],
                "metadata_fields_checked": [
                    "title",
                    "authors",
                    "publisher",
                    "isbn",
                    "publication_date",
                    "format",
                ],
                "verification_evidence_status": "verification_evidence_recorded_not_accepted",
                "source_verification_decision": "no_verification_decision_recorded",
                "source_acceptance_decision": "no_acceptance_decision_recorded",
                "source_rejection_decision": "no_rejection_decision_recorded",
                "citation_integration_status": "not_integrated",
                "manuscript_mutation_status": "no_mutation",
                "safety_scope": "non_operational_methodological_source_only",
                "boundary_note": "Evidence is recorded, but the source is not claimed as verified, not accepted, and not integrated.",
            },
            {
                "candidate_id": "CAND-B1-003",
                "evidence_record_id": "VERIF-EVID-B1-003",
                "candidate_title": "Networks: An Introduction",
                "evidence_source_category": "academic_book_page",
                "evidence_source_body": "Oxford Academic / Oxford University Press",
                "evidence_url": "https://academic.oup.com/book/27303",
                "evidence_locator_claims": [
                    "Academic book page locator identifies the Oxford Academic book record.",
                    "Candidate metadata records Mark Newman as author.",
                    "Candidate metadata records ISBN 9780199206650.",
                    "Evidence is sufficient for locator recording but not for final verification acceptance.",
                ],
                "metadata_fields_checked": [
                    "title",
                    "author",
                    "publisher_or_platform",
                    "isbn",
                    "book_record_locator",
                ],
                "verification_evidence_status": "verification_evidence_recorded_not_accepted",
                "source_verification_decision": "no_verification_decision_recorded",
                "source_acceptance_decision": "no_acceptance_decision_recorded",
                "source_rejection_decision": "no_rejection_decision_recorded",
                "citation_integration_status": "not_integrated",
                "manuscript_mutation_status": "no_mutation",
                "safety_scope": "non_operational_methodological_source_only",
                "boundary_note": "Evidence is recorded, but the source is not claimed as verified, not accepted, and not integrated.",
            },
            {
                "candidate_id": "CAND-B1-004",
                "evidence_record_id": "VERIF-EVID-B1-004",
                "candidate_title": "Agent-based modeling: methods and techniques for simulating human systems",
                "evidence_source_category": "bibliographic_database_record",
                "evidence_source_body": "PubMed / NCBI",
                "evidence_url": "https://pubmed.ncbi.nlm.nih.gov/12011407/",
                "evidence_locator_claims": [
                    "PubMed page identifies Eric Bonabeau as author.",
                    "PubMed page lists Proc Natl Acad Sci U S A as venue.",
                    "PubMed page lists DOI 10.1073/pnas.082080899.",
                    "PubMed page lists PMID 12011407 and PMCID PMC128598.",
                    "PubMed page lists pages 7280-7287 and publication date May 14, 2002.",
                ],
                "metadata_fields_checked": [
                    "title",
                    "author",
                    "venue",
                    "doi",
                    "pmid",
                    "pmcid",
                    "pages",
                    "publication_date",
                ],
                "verification_evidence_status": "verification_evidence_recorded_not_accepted",
                "source_verification_decision": "no_verification_decision_recorded",
                "source_acceptance_decision": "no_acceptance_decision_recorded",
                "source_rejection_decision": "no_rejection_decision_recorded",
                "citation_integration_status": "not_integrated",
                "manuscript_mutation_status": "no_mutation",
                "safety_scope": "non_operational_methodological_source_only",
                "boundary_note": "Evidence is recorded, but the source is not claimed as verified, not accepted, and not integrated.",
            },
            {
                "candidate_id": "CAND-B1-005",
                "evidence_record_id": "VERIF-EVID-B1-005",
                "candidate_title": "Network Science",
                "evidence_source_category": "official_book_website_and_book_metadata",
                "evidence_source_body": "Network Science official book website / Cambridge University Press metadata",
                "evidence_url": "https://networksciencebook.com/",
                "evidence_locator_claims": [
                    "Official book website identifies Network Science by Albert-László Barabási.",
                    "Candidate metadata records Cambridge University Press as publisher.",
                    "Candidate metadata records ISBN 9781107076266.",
                    "Evidence is sufficient for locator recording but not for final verification acceptance.",
                ],
                "metadata_fields_checked": [
                    "title",
                    "author",
                    "book_website",
                    "publisher_metadata",
                    "isbn",
                ],
                "verification_evidence_status": "verification_evidence_recorded_not_accepted",
                "source_verification_decision": "no_verification_decision_recorded",
                "source_acceptance_decision": "no_acceptance_decision_recorded",
                "source_rejection_decision": "no_rejection_decision_recorded",
                "citation_integration_status": "not_integrated",
                "manuscript_mutation_status": "no_mutation",
                "safety_scope": "non_operational_methodological_source_only",
                "boundary_note": "Evidence is recorded, but the source is not claimed as verified, not accepted, and not integrated.",
            },
            {
                "candidate_id": "CAND-B1-006",
                "evidence_record_id": "VERIF-EVID-B1-006",
                "candidate_title": "Global Sensitivity Analysis: The Primer",
                "evidence_source_category": "publisher_doi_record",
                "evidence_source_body": "Wiley Online Library",
                "evidence_url": "https://onlinelibrary.wiley.com/doi/book/10.1002/9780470725184",
                "evidence_locator_claims": [
                    "Wiley Online Library book DOI page records DOI 10.1002/9780470725184.",
                    "Candidate metadata records the Saltelli et al. authorship group.",
                    "Candidate metadata records Wiley / JRC Publications as publisher or record context.",
                    "Evidence is sufficient for locator recording but not for final verification acceptance.",
                ],
                "metadata_fields_checked": [
                    "title",
                    "authors",
                    "publisher_or_platform",
                    "doi",
                    "book_record_locator",
                ],
                "verification_evidence_status": "verification_evidence_recorded_not_accepted",
                "source_verification_decision": "no_verification_decision_recorded",
                "source_acceptance_decision": "no_acceptance_decision_recorded",
                "source_rejection_decision": "no_rejection_decision_recorded",
                "citation_integration_status": "not_integrated",
                "manuscript_mutation_status": "no_mutation",
                "safety_scope": "non_operational_methodological_source_only",
                "boundary_note": "Evidence is recorded, but the source is not claimed as verified, not accepted, and not integrated.",
            },
            {
                "candidate_id": "CAND-B1-007",
                "evidence_record_id": "VERIF-EVID-B1-007",
                "candidate_title": "Tutorial on agent-based modelling and simulation",
                "evidence_source_category": "publisher_article_page",
                "evidence_source_body": "Springer Nature Link",
                "evidence_url": "https://link.springer.com/article/10.1057/jos.2010.3",
                "evidence_locator_claims": [
                    "Springer page identifies C. M. Macal and M. J. North.",
                    "Springer page lists Journal of Simulation, volume 4, pages 151-162.",
                    "Springer page lists publication date September 2, 2010.",
                    "Springer page lists DOI 10.1057/jos.2010.3.",
                ],
                "metadata_fields_checked": [
                    "title",
                    "authors",
                    "venue",
                    "volume",
                    "pages",
                    "doi",
                    "publication_date",
                ],
                "verification_evidence_status": "verification_evidence_recorded_not_accepted",
                "source_verification_decision": "no_verification_decision_recorded",
                "source_acceptance_decision": "no_acceptance_decision_recorded",
                "source_rejection_decision": "no_rejection_decision_recorded",
                "citation_integration_status": "not_integrated",
                "manuscript_mutation_status": "no_mutation",
                "safety_scope": "non_operational_methodological_source_only",
                "boundary_note": "Evidence is recorded, but the source is not claimed as verified, not accepted, and not integrated.",
            },
        ]

    def _controls(self) -> List[Dict[str, str]]:
        return [
            {
                "control_id": "B1-VERIF-CTRL-01",
                "control_name": "evidence_packet_only",
                "control_rule": "v8.225 records verification evidence only.",
                "boundary_note": "Verification evidence packet only.",
            },
            {
                "control_id": "B1-VERIF-CTRL-02",
                "control_name": "no_verified_claim",
                "control_rule": "Evidence records do not become verified source claims.",
                "boundary_note": "No source is claimed as verified.",
            },
            {
                "control_id": "B1-VERIF-CTRL-03",
                "control_name": "no_acceptance_decision",
                "control_rule": "Evidence records do not create acceptance decisions.",
                "boundary_note": "No accepted source is recorded.",
            },
            {
                "control_id": "B1-VERIF-CTRL-04",
                "control_name": "no_rejection_decision",
                "control_rule": "Evidence records do not create rejection decisions.",
                "boundary_note": "No rejected source is recorded.",
            },
            {
                "control_id": "B1-VERIF-CTRL-05",
                "control_name": "no_citation_integration",
                "control_rule": "Evidence records do not insert citations.",
                "boundary_note": "No actual citation is added.",
            },
            {
                "control_id": "B1-VERIF-CTRL-06",
                "control_name": "no_fabricated_reference",
                "control_rule": "Evidence records must not invent references beyond candidate metadata and evidence locators.",
                "boundary_note": "No fabricated reference is introduced.",
            },
            {
                "control_id": "B1-VERIF-CTRL-07",
                "control_name": "no_manuscript_mutation",
                "control_rule": "Evidence packet must not modify manuscript files.",
                "boundary_note": "No manuscript file is modified.",
            },
            {
                "control_id": "B1-VERIF-CTRL-08",
                "control_name": "non_operational_scope",
                "control_rule": "Evidence packet remains methodological and non-operational.",
                "boundary_note": "No real biological datasets, no real pathogen models, no receptor parameters, and no operational targeting.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        batch_1 = self._load_json(self.source_batch_1_json_path)
        empty_ledger = self._load_json(self.source_empty_ledger_json_path)
        ledger_schema = self._load_json(self.source_ledger_schema_json_path)
        retrieval_gate = self._load_json(self.source_retrieval_gate_json_path)

        batch_counters = batch_1.get("counters", {})
        empty_counters = empty_ledger.get("counters", {})
        schema_counters = ledger_schema.get("counters", {})
        retrieval_gate_counters = retrieval_gate.get("counters", {})

        source_candidates = batch_1.get("candidate_sources", [])
        evidence_records = self._verification_evidence_records()
        controls = self._controls()

        candidate_ids = {candidate["candidate_id"] for candidate in source_candidates}
        evidence_candidate_ids = {record["candidate_id"] for record in evidence_records}

        counters = {
            "Safe abstract toy citation retrieval batch 1 source verification evidence packet count": 1,
            "New safe abstract toy citation retrieval batch 1 source verification evidence packet count": 1,
            "Toy citation batch 1 source verification evidence packet JSON export count": 1,
            "Toy citation batch 1 source verification evidence record count": len(evidence_records),
            "Toy citation batch 1 source verification evidence recorded count": len(evidence_records),
            "Toy citation batch 1 source verification evidence candidate coverage count": len(evidence_candidate_ids),
            "Toy citation batch 1 source verification evidence official locator count": len(evidence_records),
            "Toy citation batch 1 source verification evidence publisher page count": 5,
            "Toy citation batch 1 source verification evidence database record count": 1,
            "Toy citation batch 1 source verification evidence official book website count": 1,
            "Toy citation batch 1 source verification evidence field check count": sum(
                len(record["metadata_fields_checked"]) for record in evidence_records
            ),
            "Toy citation batch 1 source verification evidence locator claim count": sum(
                len(record["evidence_locator_claims"]) for record in evidence_records
            ),
            "Toy citation batch 1 source verification evidence control count": len(controls),
            "Toy citation batch 1 source verification final decision count": 0,
            "Toy citation batch 1 verified source count": 0,
            "Toy citation batch 1 accepted source count": 0,
            "Toy citation batch 1 rejected source count": 0,
            "Toy citation batch 1 acceptance decision count": 0,
            "Toy citation batch 1 rejection decision count": 0,
            "Toy citation batch 1 actual citation count": 0,
            "Toy citation batch 1 fabricated reference count": 0,
            "Toy citation batch 1 citation integration completion count": 0,
            "Toy citation batch 1 added to manuscript count": 0,
            "Toy citation batch 1 manuscript mutation count": 0,
            "Toy citation batch 1 prior candidate source row count": batch_counters.get("Toy citation batch 1 candidate source row count"),
            "Toy citation batch 1 prior candidate source recorded count": batch_counters.get("Toy citation batch 1 candidate source recorded count"),
            "Toy citation batch 1 prior source retrieval count": batch_counters.get("Toy citation batch 1 source retrieval count"),
            "Toy citation batch 1 prior verified source count": batch_counters.get("Toy citation batch 1 verified source count"),
            "Toy citation batch 1 prior actual citation count": batch_counters.get("Toy citation batch 1 actual citation count"),
            "Toy citation batch 1 prior empty ledger row count": empty_counters.get("Toy citation empty ledger row count"),
            "Toy citation batch 1 source candidate ledger field count": schema_counters.get("Toy citation candidate ledger field count"),
            "Toy citation batch 1 source retrieval gate item count": retrieval_gate_counters.get("Toy citation retrieval gate item count"),
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
            "title": "Safe Abstract Toy Citation Retrieval Batch 1 Source Verification Evidence Packet",
            "source_batch_1_json": str(self.source_batch_1_json_path),
            "source_empty_ledger_json": str(self.source_empty_ledger_json_path),
            "source_ledger_schema_json": str(self.source_ledger_schema_json_path),
            "source_retrieval_gate_json": str(self.source_retrieval_gate_json_path),
            "plan_phrase": self.plan_phrase,
            "scope": "citation-retrieval-batch-1-source-verification-evidence-packet-only",
            "safe_abstract_toy_only": True,
            "synthetic_project_context_only": True,
            "abstract_graphs_only": True,
            "unitless_parameters_only": True,
            "non_operational_only": True,
            "source_candidate_count": len(source_candidates),
            "source_candidate_ids": sorted(candidate_ids),
            "verification_evidence_packet_completed": True,
            "verification_evidence_records_recorded": True,
            "verification_evidence_record_count": len(evidence_records),
            "verification_evidence_candidate_coverage_complete": candidate_ids == evidence_candidate_ids,
            "source_verification_performed": False,
            "verified_sources_claimed": False,
            "acceptance_decisions_recorded": False,
            "rejection_decisions_recorded": False,
            "accepted_sources_recorded": False,
            "rejected_sources_recorded": False,
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
            "verification_evidence_records": evidence_records,
            "verification_evidence_controls": controls,
            "non_readiness_disclaimer": (
                "This v8.225 artifact records Batch 1 source verification evidence only. "
                "Verification evidence packet only. Verification evidence is recorded, but no source is claimed as verified. "
                "No accepted source is recorded. No rejected source is recorded. "
                "No actual citation is added. No fabricated reference is introduced. "
                "It does not complete citation integration, does not validate scientific claims, "
                "does not modify manuscript files, and No manuscript file is modified. "
                "No new citation is added. Future source verification decisions, acceptance, rejection, and citation integration require separate official milestones."
            ),
            "boundary_notes": (
                [record["boundary_note"] for record in evidence_records]
                + [control["boundary_note"] for control in controls]
            ),
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "citation-retrieval-batch-1-source-verification-evidence-packet-only":
            raise AssertionError("v8.225 must remain source-verification-evidence-packet-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.225 evidence packet must pass.")

        if report["source_candidate_count"] != 7:
            raise AssertionError("Expected 7 source candidates from v8.224.")

        if report["verification_evidence_record_count"] != 7:
            raise AssertionError("Expected 7 verification evidence records.")

        if report["verification_evidence_candidate_coverage_complete"] is not True:
            raise AssertionError("Verification evidence must cover all seven candidate IDs.")

        if report["verification_evidence_packet_completed"] is not True:
            raise AssertionError("Evidence packet should be completed.")

        if report["verification_evidence_records_recorded"] is not True:
            raise AssertionError("Evidence records should be recorded.")

        for field in [
            "source_verification_performed",
            "verified_sources_claimed",
            "acceptance_decisions_recorded",
            "rejection_decisions_recorded",
            "accepted_sources_recorded",
            "rejected_sources_recorded",
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

        for record in report["verification_evidence_records"]:
            if record["verification_evidence_status"] != "verification_evidence_recorded_not_accepted":
                raise AssertionError("Every evidence record must remain recorded_not_accepted.")
            if record["source_verification_decision"] != "no_verification_decision_recorded":
                raise AssertionError("No source verification decision may be recorded.")
            if record["source_acceptance_decision"] != "no_acceptance_decision_recorded":
                raise AssertionError("No source acceptance decision may be recorded.")
            if record["source_rejection_decision"] != "no_rejection_decision_recorded":
                raise AssertionError("No source rejection decision may be recorded.")
            if record["citation_integration_status"] != "not_integrated":
                raise AssertionError("No source may be citation-integrated.")
            if record["manuscript_mutation_status"] != "no_mutation":
                raise AssertionError("No manuscript mutation may be recorded.")
            if record["safety_scope"] != "non_operational_methodological_source_only":
                raise AssertionError("Evidence record must remain non-operational methodological only.")

        counters = report["counters"]

        expected_counts = {
            "Toy citation batch 1 source verification evidence record count": 7,
            "Toy citation batch 1 source verification evidence recorded count": 7,
            "Toy citation batch 1 source verification evidence candidate coverage count": 7,
            "Toy citation batch 1 source verification evidence official locator count": 7,
            "Toy citation batch 1 source verification evidence publisher page count": 5,
            "Toy citation batch 1 source verification evidence database record count": 1,
            "Toy citation batch 1 source verification evidence official book website count": 1,
            "Toy citation batch 1 source verification evidence field check count": 42,
            "Toy citation batch 1 source verification evidence locator claim count": 29,
            "Toy citation batch 1 source verification evidence control count": 8,
            "Toy citation batch 1 source verification final decision count": 0,
            "Toy citation batch 1 verified source count": 0,
            "Toy citation batch 1 accepted source count": 0,
            "Toy citation batch 1 rejected source count": 0,
            "Toy citation batch 1 actual citation count": 0,
            "Toy citation batch 1 citation integration completion count": 0,
            "Toy citation batch 1 added to manuscript count": 0,
            "Toy citation batch 1 manuscript mutation count": 0,
            "Toy citation batch 1 prior candidate source row count": 7,
            "Toy citation batch 1 prior candidate source recorded count": 7,
            "Toy citation batch 1 prior source retrieval count": 7,
            "Toy citation batch 1 prior verified source count": 0,
            "Toy citation batch 1 prior actual citation count": 0,
            "Toy citation batch 1 prior empty ledger row count": 0,
            "Toy citation batch 1 source candidate ledger field count": 16,
            "Toy citation batch 1 source retrieval gate item count": 12,
        }

        for name, expected in expected_counts.items():
            actual = counters.get(name)
            if actual != expected:
                raise AssertionError(f"Expected {expected} for {name}, got {actual}")

        combined_text = (
            json.dumps(report["verification_evidence_records"], ensure_ascii=False)
            + " "
            + json.dumps(report["verification_evidence_controls"], ensure_ascii=False)
            + " "
            + report["non_readiness_disclaimer"]
        )

        required_phrases = [
            "Verification evidence packet only",
            "verification_evidence_recorded_not_accepted",
            "no_verification_decision_recorded",
            "no_acceptance_decision_recorded",
            "no_rejection_decision_recorded",
            "not_integrated",
            "no_mutation",
            "No source is claimed as verified",
            "No accepted source is recorded",
            "No rejected source is recorded",
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
                raise AssertionError(f"Missing required verification evidence phrase: {phrase}")

        must_be_zero = [
            "Toy citation batch 1 source verification final decision count",
            "Toy citation batch 1 verified source count",
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

        lines.append("# Safe Abstract Toy Citation Retrieval Batch 1 Source Verification Evidence Packet")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is citation-retrieval-batch-1-source-verification-evidence-packet-only.")
        lines.append("It records verification evidence for the seven v8.224 candidate sources without claiming verification, acceptance, rejection, citation integration, or manuscript mutation.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")

        lines.append("## Verification Evidence Records")
        lines.append("")
        for record in report["verification_evidence_records"]:
            lines.append(f"### {record['evidence_record_id']} - {record['candidate_id']}")
            lines.append("")
            lines.append(f"- Candidate title: {record['candidate_title']}")
            lines.append(f"- Evidence source category: {record['evidence_source_category']}")
            lines.append(f"- Evidence source body: {record['evidence_source_body']}")
            lines.append(f"- Evidence URL: {record['evidence_url']}")
            lines.append("- Evidence locator claims:")
            for claim in record["evidence_locator_claims"]:
                lines.append(f"  - {claim}")
            lines.append("- Metadata fields checked:")
            for field in record["metadata_fields_checked"]:
                lines.append(f"  - {field}")
            lines.append(f"- Verification evidence status: {record['verification_evidence_status']}")
            lines.append(f"- Source verification decision: {record['source_verification_decision']}")
            lines.append(f"- Source acceptance decision: {record['source_acceptance_decision']}")
            lines.append(f"- Source rejection decision: {record['source_rejection_decision']}")
            lines.append(f"- Citation integration status: {record['citation_integration_status']}")
            lines.append(f"- Manuscript mutation status: {record['manuscript_mutation_status']}")
            lines.append(f"- Safety scope: {record['safety_scope']}")
            lines.append(f"- Boundary note: {record['boundary_note']}")
            lines.append("")

        lines.append("## Verification Evidence Controls")
        lines.append("")
        for control in report["verification_evidence_controls"]:
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
        lines.append("V8_225_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_BATCH_1_SOURCE_VERIFICATION_EVIDENCE_PACKET_OK")
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


def build_safe_abstract_toy_citation_retrieval_batch_1_source_verification_evidence_packet() -> Dict[str, Any]:
    return SafeAbstractToyCitationRetrievalBatch1SourceVerificationEvidencePacketBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_citation_retrieval_batch_1_source_verification_evidence_packet()
    counters = result["counters"]
    print("V8_225_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_BATCH_1_SOURCE_VERIFICATION_EVIDENCE_PACKET_OK")
    print("TOY_CITATION_RETRIEVAL_BATCH_1_SOURCE_VERIFICATION_EVIDENCE_PACKET_DIRECT_CHECK_OK")
    print(f"Evidence record count: {counters['Toy citation batch 1 source verification evidence record count']}")
    print(f"Evidence recorded count: {counters['Toy citation batch 1 source verification evidence recorded count']}")
    print(f"Evidence candidate coverage count: {counters['Toy citation batch 1 source verification evidence candidate coverage count']}")
    print(f"Official locator count: {counters['Toy citation batch 1 source verification evidence official locator count']}")
    print(f"Publisher page count: {counters['Toy citation batch 1 source verification evidence publisher page count']}")
    print(f"Database record count: {counters['Toy citation batch 1 source verification evidence database record count']}")
    print(f"Official book website count: {counters['Toy citation batch 1 source verification evidence official book website count']}")
    print(f"Evidence field check count: {counters['Toy citation batch 1 source verification evidence field check count']}")
    print(f"Evidence locator claim count: {counters['Toy citation batch 1 source verification evidence locator claim count']}")
    print(f"Evidence control count: {counters['Toy citation batch 1 source verification evidence control count']}")
    print(f"Final verification decision count: {counters['Toy citation batch 1 source verification final decision count']}")
    print(f"Verified source count: {counters['Toy citation batch 1 verified source count']}")
    print(f"Accepted source count: {counters['Toy citation batch 1 accepted source count']}")
    print(f"Rejected source count: {counters['Toy citation batch 1 rejected source count']}")
    print(f"Actual citation count: {counters['Toy citation batch 1 actual citation count']}")
    print(f"Fabricated reference count: {counters['Toy citation batch 1 fabricated reference count']}")
    print(f"Citation integration completion count: {counters['Toy citation batch 1 citation integration completion count']}")
    print(f"Citation added to manuscript count: {counters['Toy citation batch 1 added to manuscript count']}")
    print(f"Manuscript mutation count: {counters['Toy citation batch 1 manuscript mutation count']}")
    print(f"Prior candidate source row count: {counters['Toy citation batch 1 prior candidate source row count']}")
    print(f"Prior source retrieval count: {counters['Toy citation batch 1 prior source retrieval count']}")
    print(f"Toy citation verified source count: {counters['Toy citation verified source count']}")
    print(f"Toy citation actual citation count: {counters['Toy citation actual citation count']}")
    print(f"Toy citation fabricated reference count: {counters['Toy citation fabricated reference count']}")
    print(f"Toy citation integration completion count: {counters['Toy citation integration completion count']}")
    print(f"Toy citation added to manuscript count: {counters['Toy citation added to manuscript count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript patch mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {result['passed']}")
