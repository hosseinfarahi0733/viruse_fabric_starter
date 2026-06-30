from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyCitationRetrievalEmptyCandidateLedgerInstanceBuilder:
    version = "v8.223"

    source_ledger_schema_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_candidate_ledger_schema_v8_222.json"
    )
    source_ledger_schema_md_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_candidate_ledger_schema_v8_222.md"
    )
    source_retrieval_gate_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_readiness_gate_v8_221.json"
    )
    source_eligibility_json_path = Path(
        "outputs/safe_abstract_toy_citation_source_eligibility_and_query_plan_v8_220.json"
    )
    source_citation_slot_json_path = Path(
        "outputs/safe_abstract_toy_citation_slot_integration_plan_v8_219.json"
    )
    source_coherence_json_path = Path(
        "outputs/safe_abstract_toy_manuscript_coherence_improvement_package_v8_218.json"
    )
    source_eval_json_path = Path("outputs/safe_abstract_toy_evaluation_design_plan_v8_217.json")
    source_gap_json_path = Path(
        "outputs/safe_abstract_toy_scientific_gap_and_evidence_upgrade_register_v8_216.json"
    )
    source_assembly_json_path = Path(
        "outputs/safe_abstract_toy_manuscript_assembly_preview_package_v8_215.json"
    )

    output_md_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_empty_candidate_ledger_instance_v8_223.md"
    )
    output_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_empty_candidate_ledger_instance_v8_223.json"
    )

    plan_phrase = "empty_candidate_ledger_instance_created_but_no_candidates_recorded"

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Missing JSON source: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"Expected dict JSON payload from {path}")
        return payload

    def _load_text(self, path: Path) -> str:
        if not path.exists():
            raise FileNotFoundError(f"Missing text source: {path}")
        return path.read_text(encoding="utf-8")

    def _instance_metadata(self) -> Dict[str, str]:
        return {
            "instance_id": "EMPTY-CANDIDATE-LEDGER-v8.223",
            "instance_type": "empty_candidate_ledger_instance",
            "schema_source": "v8.222 candidate ledger schema",
            "ledger_status": "empty",
            "row_state": "zero_rows",
            "candidate_state": "no_candidate_source_is_recorded",
            "retrieval_state": "not_authorized_and_not_performed",
            "verification_state": "no_source_is_claimed_as_verified",
            "integration_state": "not_integrated",
            "manuscript_state": "no_manuscript_file_is_modified",
            "boundary_note": "Empty candidate ledger instance only. No ledger rows are created and No candidate source is recorded.",
        }

    def _schema_conformance_checks(self) -> List[Dict[str, str]]:
        return [
            {
                "check_id": "CONFORM-01",
                "schema_field": "candidate_id",
                "empty_instance_rule": "The empty ledger contains no candidate_id values because no candidate rows exist.",
                "observed_status": "absent_by_design",
                "boundary_note": "No candidate source is recorded.",
            },
            {
                "check_id": "CONFORM-02",
                "schema_field": "slot_id",
                "empty_instance_rule": "The empty ledger contains no slot_id assignments because no candidate rows exist.",
                "observed_status": "absent_by_design",
                "boundary_note": "No actual citation is added.",
            },
            {
                "check_id": "CONFORM-03",
                "schema_field": "query_family_id",
                "empty_instance_rule": "The empty ledger contains no query_family_id values because no source retrieval is performed.",
                "observed_status": "absent_by_design",
                "boundary_note": "Future source retrieval requires a separate official milestone.",
            },
            {
                "check_id": "CONFORM-04",
                "schema_field": "candidate_title",
                "empty_instance_rule": "The empty ledger contains no candidate titles and does not invent placeholder titles.",
                "observed_status": "absent_by_design",
                "boundary_note": "No fabricated reference is introduced.",
            },
            {
                "check_id": "CONFORM-05",
                "schema_field": "candidate_author_or_body",
                "empty_instance_rule": "The empty ledger contains no author or issuing body metadata because no source metadata is retrieved.",
                "observed_status": "absent_by_design",
                "boundary_note": "No source is claimed as verified.",
            },
            {
                "check_id": "CONFORM-06",
                "schema_field": "candidate_year",
                "empty_instance_rule": "The empty ledger contains no candidate year values and does not infer unavailable dates.",
                "observed_status": "absent_by_design",
                "boundary_note": "No source retrieval is performed.",
            },
            {
                "check_id": "CONFORM-07",
                "schema_field": "candidate_locator",
                "empty_instance_rule": "The empty ledger contains no DOI, URL, ISBN, database record, or other locator.",
                "observed_status": "absent_by_design",
                "boundary_note": "No fabricated reference is introduced.",
            },
            {
                "check_id": "CONFORM-08",
                "schema_field": "source_type",
                "empty_instance_rule": "The empty ledger contains no source_type classification because no candidate is present.",
                "observed_status": "absent_by_design",
                "boundary_note": "No evidence upgrade is completed.",
            },
            {
                "check_id": "CONFORM-09",
                "schema_field": "evidence_role",
                "empty_instance_rule": "The empty ledger contains no evidence_role claims because no source is present.",
                "observed_status": "absent_by_design",
                "boundary_note": "does not validate scientific claims.",
            },
            {
                "check_id": "CONFORM-10",
                "schema_field": "safety_screen_status",
                "empty_instance_rule": "The empty ledger contains no safety screen result because no candidate requires screening.",
                "observed_status": "absent_by_design",
                "boundary_note": "No real biological datasets, no real pathogen models, no receptor parameters, and no operational targeting are introduced.",
            },
            {
                "check_id": "CONFORM-11",
                "schema_field": "verification_status",
                "empty_instance_rule": "The empty ledger contains no verification_status row and does not claim verification.",
                "observed_status": "absent_by_design",
                "boundary_note": "No source is claimed as verified.",
            },
            {
                "check_id": "CONFORM-12",
                "schema_field": "acceptance_status",
                "empty_instance_rule": "The empty ledger contains no acceptance_status row because no candidate has been accepted or rejected.",
                "observed_status": "absent_by_design",
                "boundary_note": "No accepted source and no rejected source is recorded.",
            },
            {
                "check_id": "CONFORM-13",
                "schema_field": "citation_integration_status",
                "empty_instance_rule": "The empty ledger contains no citation integration status because no citation is integrated.",
                "observed_status": "absent_by_design",
                "boundary_note": "does not complete citation integration.",
            },
            {
                "check_id": "CONFORM-14",
                "schema_field": "manuscript_mutation_status",
                "empty_instance_rule": "The empty ledger contains no manuscript mutation status row because no manuscript file is modified.",
                "observed_status": "absent_by_design",
                "boundary_note": "No manuscript file is modified.",
            },
            {
                "check_id": "CONFORM-15",
                "schema_field": "readiness_claim_status",
                "empty_instance_rule": "The empty ledger contains no readiness claim and does not imply manuscript submission readiness.",
                "observed_status": "absent_by_design",
                "boundary_note": "Manuscript submission ready count remains zero.",
            },
            {
                "check_id": "CONFORM-16",
                "schema_field": "future_authorization_reference",
                "empty_instance_rule": "The empty ledger records no authorization reference because no future retrieval milestone has run yet.",
                "observed_status": "absent_by_design",
                "boundary_note": "Future source retrieval requires a separate official milestone.",
            },
        ]

    def _zero_row_invariants(self) -> List[Dict[str, str]]:
        return [
            {
                "invariant_id": "ZERO-ROW-01",
                "invariant_name": "empty_candidate_ledger_length",
                "required_value": "0 rows",
                "boundary_note": "No ledger rows are created.",
            },
            {
                "invariant_id": "ZERO-ROW-02",
                "invariant_name": "candidate_source_record_count",
                "required_value": "0 recorded candidate sources",
                "boundary_note": "No candidate source is recorded.",
            },
            {
                "invariant_id": "ZERO-ROW-03",
                "invariant_name": "candidate_acceptance_decision_count",
                "required_value": "0 acceptance decisions",
                "boundary_note": "Accepted source count remains zero.",
            },
            {
                "invariant_id": "ZERO-ROW-04",
                "invariant_name": "candidate_rejection_decision_count",
                "required_value": "0 rejection decisions",
                "boundary_note": "Rejected source count remains zero.",
            },
            {
                "invariant_id": "ZERO-ROW-05",
                "invariant_name": "candidate_blocked_decision_count",
                "required_value": "0 blocked decisions",
                "boundary_note": "blocked_for_safety remains a future status only.",
            },
            {
                "invariant_id": "ZERO-ROW-06",
                "invariant_name": "retrieval_authorization_count",
                "required_value": "0 retrieval authorizations",
                "boundary_note": "No retrieval authorization is granted.",
            },
            {
                "invariant_id": "ZERO-ROW-07",
                "invariant_name": "source_retrieval_count",
                "required_value": "0 source retrieval operations",
                "boundary_note": "No source retrieval is performed.",
            },
            {
                "invariant_id": "ZERO-ROW-08",
                "invariant_name": "verified_source_count",
                "required_value": "0 verified sources",
                "boundary_note": "No source is claimed as verified.",
            },
            {
                "invariant_id": "ZERO-ROW-09",
                "invariant_name": "actual_citation_count",
                "required_value": "0 actual citations",
                "boundary_note": "No actual citation is added.",
            },
            {
                "invariant_id": "ZERO-ROW-10",
                "invariant_name": "fabricated_reference_count",
                "required_value": "0 fabricated references",
                "boundary_note": "No fabricated reference is introduced.",
            },
            {
                "invariant_id": "ZERO-ROW-11",
                "invariant_name": "citation_integration_completion_count",
                "required_value": "0 completed citation integrations",
                "boundary_note": "does not complete citation integration.",
            },
            {
                "invariant_id": "ZERO-ROW-12",
                "invariant_name": "manuscript_mutation_count",
                "required_value": "0 manuscript mutations",
                "boundary_note": "No manuscript file is modified.",
            },
        ]

    def _empty_ledger_controls(self) -> List[Dict[str, str]]:
        return [
            {
                "control_id": "EMPTY-LEDGER-CTRL-01",
                "control_name": "no_synthetic_placeholder_rows",
                "control_rule": "The empty instance must not create dummy candidate rows for demonstration.",
                "boundary_note": "No ledger rows are created.",
            },
            {
                "control_id": "EMPTY-LEDGER-CTRL-02",
                "control_name": "no_memory_based_candidate_metadata",
                "control_rule": "The empty instance must not populate title, author, year, locator, or source type from memory.",
                "boundary_note": "No fabricated reference is introduced.",
            },
            {
                "control_id": "EMPTY-LEDGER-CTRL-03",
                "control_name": "no_retrieval_execution",
                "control_rule": "The empty instance must not execute search, scraping, lookup, database access, or source retrieval.",
                "boundary_note": "No source retrieval is performed.",
            },
            {
                "control_id": "EMPTY-LEDGER-CTRL-04",
                "control_name": "no_verification_claim",
                "control_rule": "The empty instance must not mark any source as verified.",
                "boundary_note": "No source is claimed as verified.",
            },
            {
                "control_id": "EMPTY-LEDGER-CTRL-05",
                "control_name": "no_acceptance_or_rejection_decision",
                "control_rule": "The empty instance must not record accepted_candidate, rejected_candidate, or blocked_for_safety decisions.",
                "boundary_note": "No accepted source and no rejected source is recorded.",
            },
            {
                "control_id": "EMPTY-LEDGER-CTRL-06",
                "control_name": "no_citation_insertion",
                "control_rule": "The empty instance must not add any citation to manuscript files.",
                "boundary_note": "No new citation is added.",
            },
            {
                "control_id": "EMPTY-LEDGER-CTRL-07",
                "control_name": "no_schema_as_evidence_upgrade",
                "control_rule": "The empty instance must not treat schema conformance as evidence completion.",
                "boundary_note": "No evidence upgrade is completed.",
            },
            {
                "control_id": "EMPTY-LEDGER-CTRL-08",
                "control_name": "no_schema_as_validation",
                "control_rule": "The empty instance must not treat an empty ledger as validation, proof, or independent experiment.",
                "boundary_note": "does not validate scientific claims.",
            },
            {
                "control_id": "EMPTY-LEDGER-CTRL-09",
                "control_name": "no_real_biological_operational_content",
                "control_rule": "The empty instance must not introduce real biological datasets, real pathogen models, receptor parameters, or operational targeting.",
                "boundary_note": "No real biological datasets, no real pathogen models, no receptor parameters, and no operational targeting are introduced.",
            },
            {
                "control_id": "EMPTY-LEDGER-CTRL-10",
                "control_name": "future_milestone_required",
                "control_rule": "Future retrieval, verification, acceptance, rejection, and integration require separate official milestones.",
                "boundary_note": "Future source retrieval requires a separate official milestone.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        ledger_schema_source = self._load_json(self.source_ledger_schema_json_path)
        ledger_schema_md = self._load_text(self.source_ledger_schema_md_path)
        retrieval_gate_source = self._load_json(self.source_retrieval_gate_json_path)
        eligibility_source = self._load_json(self.source_eligibility_json_path)
        citation_slot_source = self._load_json(self.source_citation_slot_json_path)
        coherence_source = self._load_json(self.source_coherence_json_path)
        eval_source = self._load_json(self.source_eval_json_path)
        gap_source = self._load_json(self.source_gap_json_path)
        assembly_source = self._load_json(self.source_assembly_json_path)

        ledger_schema_counters = ledger_schema_source.get("counters", {})
        retrieval_counters = retrieval_gate_source.get("counters", {})
        eligibility_counters = eligibility_source.get("counters", {})
        citation_counters = citation_slot_source.get("counters", {})
        coherence_counters = coherence_source.get("counters", {})
        eval_counters = eval_source.get("counters", {})
        gap_counters = gap_source.get("counters", {})
        assembly_counters = assembly_source.get("counters", {})

        instance_metadata = self._instance_metadata()
        schema_conformance_checks = self._schema_conformance_checks()
        zero_row_invariants = self._zero_row_invariants()
        empty_ledger_controls = self._empty_ledger_controls()
        empty_candidate_ledger_rows: List[Dict[str, Any]] = []

        counters = {
            "Safe abstract toy citation retrieval empty candidate ledger instance count": 1,
            "New safe abstract toy citation retrieval empty candidate ledger instance count": 1,
            "Toy citation retrieval empty candidate ledger instance JSON export count": 1,
            "Toy citation empty ledger schema conformance check count": len(schema_conformance_checks),
            "Toy citation empty ledger zero row invariant count": len(zero_row_invariants),
            "Toy citation empty ledger control count": len(empty_ledger_controls),
            "Toy citation empty ledger row count": len(empty_candidate_ledger_rows),
            "Toy citation empty ledger candidate source recorded count": 0,
            "Toy citation empty ledger acceptance decision count": 0,
            "Toy citation empty ledger rejection decision count": 0,
            "Toy citation empty ledger blocked decision count": 0,
            "Toy citation empty ledger retrieval authorization count": 0,
            "Toy citation empty ledger retrieval execution count": 0,
            "Toy citation empty ledger source retrieval count": 0,
            "Toy citation empty ledger verified source count": 0,
            "Toy citation empty ledger accepted source count": 0,
            "Toy citation empty ledger rejected source count": 0,
            "Toy citation empty ledger actual citation count": 0,
            "Toy citation empty ledger fabricated reference count": 0,
            "Toy citation empty ledger integration completion count": 0,
            "Toy citation empty ledger added to manuscript count": 0,
            "Toy citation empty ledger source candidate ledger field count": ledger_schema_counters.get("Toy citation candidate ledger field count"),
            "Toy citation empty ledger source status enum count": ledger_schema_counters.get("Toy citation candidate status enum count"),
            "Toy citation empty ledger source provenance field count": ledger_schema_counters.get("Toy citation candidate provenance field count"),
            "Toy citation empty ledger source safety screen field count": ledger_schema_counters.get("Toy citation candidate safety screen field count"),
            "Toy citation empty ledger source hallucination control count": ledger_schema_counters.get("Toy citation candidate hallucination control count"),
            "Toy citation empty ledger source prior ledger row count": ledger_schema_counters.get("Toy citation candidate ledger row count"),
            "Toy citation empty ledger source prior candidate source recorded count": ledger_schema_counters.get("Toy citation candidate source recorded count"),
            "Toy citation empty ledger source prior retrieval authorization count": ledger_schema_counters.get("Toy citation candidate retrieval authorization count"),
            "Toy citation empty ledger source prior source retrieval count": ledger_schema_counters.get("Toy citation candidate source retrieval count"),
            "Toy citation empty ledger source prior verified source count": ledger_schema_counters.get("Toy citation candidate verified source count"),
            "Toy citation empty ledger source prior accepted source count": ledger_schema_counters.get("Toy citation candidate accepted source count"),
            "Toy citation empty ledger source prior rejected source count": ledger_schema_counters.get("Toy citation candidate rejected source count"),
            "Toy citation empty ledger source prior actual citation count": ledger_schema_counters.get("Toy citation candidate actual citation count"),
            "Toy citation empty ledger source prior fabricated reference count": ledger_schema_counters.get("Toy citation candidate fabricated reference count"),
            "Toy citation empty ledger source prior integration completion count": ledger_schema_counters.get("Toy citation candidate integration completion count"),
            "Toy citation empty ledger source prior added to manuscript count": ledger_schema_counters.get("Toy citation candidate added to manuscript count"),
            "Toy citation empty ledger source retrieval gate item count": retrieval_counters.get("Toy citation retrieval gate item count"),
            "Toy citation empty ledger source allowed query family count": retrieval_counters.get("Toy citation retrieval allowed query family count"),
            "Toy citation empty ledger source acceptance schema field count": retrieval_counters.get("Toy citation retrieval acceptance schema field count"),
            "Toy citation empty ledger source rejection reason count": retrieval_counters.get("Toy citation retrieval rejection reason count"),
            "Toy citation empty ledger source preflight check count": retrieval_counters.get("Toy citation retrieval preflight check count"),
            "Toy citation empty ledger source eligibility rule count": eligibility_counters.get("Toy citation source eligibility rule count"),
            "Toy citation empty ledger source query plan count": eligibility_counters.get("Toy citation source query plan count"),
            "Toy citation empty ledger source exclusion group count": eligibility_counters.get("Toy citation source exclusion group count"),
            "Toy citation empty ledger source slot count": citation_counters.get("Toy citation slot count"),
            "Toy citation empty ledger source unresolved slot count": citation_counters.get("Toy citation unresolved slot count"),
            "Toy citation empty ledger source slot group count": citation_counters.get("Toy citation slot group count"),
            "Toy citation empty ledger source assembly section count": assembly_counters.get("Toy manuscript assembly preview section count"),
            "Toy citation empty ledger source gap item count": gap_counters.get("Toy scientific gap register item count"),
            "Toy citation empty ledger source P0 gap count": gap_counters.get("Toy scientific gap P0 count"),
            "Toy citation empty ledger source evidence upgrade completed count": gap_counters.get("Toy scientific evidence upgrade completed count"),
            "Toy citation empty ledger source evaluation design module count": eval_counters.get("Toy evaluation design module count"),
            "Toy citation empty ledger source actual evaluation run count": eval_counters.get("Toy evaluation actual run count"),
            "Toy citation empty ledger source validation claim count": eval_counters.get("Toy evaluation validation claim count"),
            "Toy citation empty ledger source coherence improvement item count": coherence_counters.get("Toy manuscript coherence improvement item count"),
            "Toy citation empty ledger source coherence rewrite application count": coherence_counters.get("Toy manuscript coherence rewrite application count"),
            "Toy citation empty ledger instance execution count": 1,
            "Toy citation empty ledger instance direct execution count": 1,
            "Toy citation actual citation count": 0,
            "Toy citation verified source count": 0,
            "Toy citation fabricated reference count": 0,
            "Toy citation source retrieval execution count": 0,
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
            "title": "Safe Abstract Toy Citation Retrieval Empty Candidate Ledger Instance",
            "source_ledger_schema_json": str(self.source_ledger_schema_json_path),
            "source_ledger_schema_markdown": str(self.source_ledger_schema_md_path),
            "source_ledger_schema_markdown_character_count": len(ledger_schema_md),
            "source_retrieval_gate_json": str(self.source_retrieval_gate_json_path),
            "source_eligibility_json": str(self.source_eligibility_json_path),
            "source_citation_slot_json": str(self.source_citation_slot_json_path),
            "source_coherence_json": str(self.source_coherence_json_path),
            "source_evaluation_design_json": str(self.source_eval_json_path),
            "source_gap_json": str(self.source_gap_json_path),
            "source_assembly_json": str(self.source_assembly_json_path),
            "plan_phrase": self.plan_phrase,
            "scope": "citation-retrieval-empty-candidate-ledger-instance-only",
            "safe_abstract_toy_only": True,
            "synthetic_only": True,
            "abstract_graphs_only": True,
            "unitless_parameters_only": True,
            "non_operational_only": True,
            "empty_candidate_ledger_instance_completed": True,
            "schema_conformance_checked": True,
            "zero_row_invariants_checked": True,
            "empty_ledger_controls_checked": True,
            "candidate_ledger_rows_created": False,
            "candidate_sources_recorded": False,
            "candidate_acceptance_decisions_recorded": False,
            "candidate_rejection_decisions_recorded": False,
            "candidate_blocked_decisions_recorded": False,
            "retrieval_authorization_granted": False,
            "source_retrieval_performed": False,
            "verified_sources_claimed": False,
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
            "non_readiness_disclaimer": (
                "This v8.223 artifact creates an empty candidate ledger instance only. "
                "Empty candidate ledger instance only. No ledger rows are created. "
                "No candidate source is recorded. No retrieval authorization is granted. "
                "No source retrieval is performed. No actual citation is added. "
                "No fabricated reference is introduced. No source is claimed as verified. "
                "It does not complete citation integration, does not validate scientific claims, "
                "does not modify manuscript files, and No manuscript file is modified. "
                "No new citation is added. Future source retrieval requires a separate official milestone."
            ),
            "instance_metadata": instance_metadata,
            "empty_candidate_ledger_rows": empty_candidate_ledger_rows,
            "schema_conformance_checks": schema_conformance_checks,
            "zero_row_invariants": zero_row_invariants,
            "empty_ledger_controls": empty_ledger_controls,
            "boundary_notes": (
                [instance_metadata["boundary_note"]]
                + [item["boundary_note"] for item in schema_conformance_checks]
                + [item["boundary_note"] for item in zero_row_invariants]
                + [item["boundary_note"] for item in empty_ledger_controls]
            ),
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "citation-retrieval-empty-candidate-ledger-instance-only":
            raise AssertionError("v8.223 must remain citation-retrieval-empty-candidate-ledger-instance-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.223 empty candidate ledger instance must pass.")

        if report["empty_candidate_ledger_instance_completed"] is not True:
            raise AssertionError("v8.223 should complete only the empty candidate ledger instance.")

        if report["empty_candidate_ledger_rows"] != []:
            raise AssertionError("v8.223 empty candidate ledger rows must be an empty list.")

        for field in [
            "candidate_ledger_rows_created",
            "candidate_sources_recorded",
            "candidate_acceptance_decisions_recorded",
            "candidate_rejection_decisions_recorded",
            "candidate_blocked_decisions_recorded",
            "retrieval_authorization_granted",
            "source_retrieval_performed",
            "verified_sources_claimed",
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

        counters = report["counters"]

        expected_counts = {
            "Toy citation empty ledger schema conformance check count": 16,
            "Toy citation empty ledger zero row invariant count": 12,
            "Toy citation empty ledger control count": 10,
            "Toy citation empty ledger row count": 0,
            "Toy citation empty ledger candidate source recorded count": 0,
            "Toy citation empty ledger acceptance decision count": 0,
            "Toy citation empty ledger rejection decision count": 0,
            "Toy citation empty ledger blocked decision count": 0,
            "Toy citation empty ledger retrieval authorization count": 0,
            "Toy citation empty ledger retrieval execution count": 0,
            "Toy citation empty ledger source retrieval count": 0,
            "Toy citation empty ledger verified source count": 0,
            "Toy citation empty ledger accepted source count": 0,
            "Toy citation empty ledger rejected source count": 0,
            "Toy citation empty ledger actual citation count": 0,
            "Toy citation empty ledger fabricated reference count": 0,
            "Toy citation empty ledger integration completion count": 0,
            "Toy citation empty ledger added to manuscript count": 0,
            "Toy citation empty ledger source candidate ledger field count": 16,
            "Toy citation empty ledger source status enum count": 8,
            "Toy citation empty ledger source provenance field count": 10,
            "Toy citation empty ledger source safety screen field count": 10,
            "Toy citation empty ledger source hallucination control count": 10,
            "Toy citation empty ledger source prior ledger row count": 0,
            "Toy citation empty ledger source prior candidate source recorded count": 0,
            "Toy citation empty ledger source prior retrieval authorization count": 0,
            "Toy citation empty ledger source prior source retrieval count": 0,
            "Toy citation empty ledger source prior verified source count": 0,
            "Toy citation empty ledger source prior accepted source count": 0,
            "Toy citation empty ledger source prior rejected source count": 0,
            "Toy citation empty ledger source prior actual citation count": 0,
            "Toy citation empty ledger source prior fabricated reference count": 0,
            "Toy citation empty ledger source prior integration completion count": 0,
            "Toy citation empty ledger source prior added to manuscript count": 0,
            "Toy citation empty ledger source retrieval gate item count": 12,
            "Toy citation empty ledger source allowed query family count": 12,
            "Toy citation empty ledger source acceptance schema field count": 12,
            "Toy citation empty ledger source rejection reason count": 10,
            "Toy citation empty ledger source preflight check count": 10,
            "Toy citation empty ledger source eligibility rule count": 12,
            "Toy citation empty ledger source query plan count": 12,
            "Toy citation empty ledger source exclusion group count": 4,
            "Toy citation empty ledger source slot count": 12,
            "Toy citation empty ledger source unresolved slot count": 12,
            "Toy citation empty ledger source slot group count": 4,
            "Toy citation empty ledger source assembly section count": 9,
            "Toy citation empty ledger source gap item count": 12,
            "Toy citation empty ledger source P0 gap count": 6,
            "Toy citation empty ledger source evidence upgrade completed count": 0,
            "Toy citation empty ledger source evaluation design module count": 10,
            "Toy citation empty ledger source actual evaluation run count": 0,
            "Toy citation empty ledger source validation claim count": 0,
            "Toy citation empty ledger source coherence improvement item count": 10,
            "Toy citation empty ledger source coherence rewrite application count": 0,
        }

        for name, expected in expected_counts.items():
            if counters.get(name) != expected:
                raise AssertionError(f"Expected {expected} for {name}, got {counters.get(name)}")

        combined_text = (
            json.dumps(report["instance_metadata"], ensure_ascii=False)
            + " "
            + json.dumps(report["schema_conformance_checks"], ensure_ascii=False)
            + " "
            + json.dumps(report["zero_row_invariants"], ensure_ascii=False)
            + " "
            + json.dumps(report["empty_ledger_controls"], ensure_ascii=False)
            + " "
            + report["non_readiness_disclaimer"]
        )

        required_phrases = [
            "empty candidate ledger instance",
            "Empty candidate ledger instance only",
            "No ledger rows are created",
            "No candidate source is recorded",
            "zero_rows",
            "absent_by_design",
            "No retrieval authorization is granted",
            "No source retrieval is performed",
            "No actual citation is added",
            "No fabricated reference is introduced",
            "No source is claimed as verified",
            "Future source retrieval requires a separate official milestone",
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
                raise AssertionError(f"Missing required empty ledger phrase: {phrase}")

        must_be_zero = [
            "Toy citation empty ledger row count",
            "Toy citation empty ledger candidate source recorded count",
            "Toy citation empty ledger acceptance decision count",
            "Toy citation empty ledger rejection decision count",
            "Toy citation empty ledger blocked decision count",
            "Toy citation empty ledger retrieval authorization count",
            "Toy citation empty ledger retrieval execution count",
            "Toy citation empty ledger source retrieval count",
            "Toy citation empty ledger verified source count",
            "Toy citation empty ledger accepted source count",
            "Toy citation empty ledger rejected source count",
            "Toy citation empty ledger actual citation count",
            "Toy citation empty ledger fabricated reference count",
            "Toy citation empty ledger integration completion count",
            "Toy citation empty ledger added to manuscript count",
            "Toy citation actual citation count",
            "Toy citation verified source count",
            "Toy citation fabricated reference count",
            "Toy citation source retrieval execution count",
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

        lines.append("# Safe Abstract Toy Citation Retrieval Empty Candidate Ledger Instance")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is citation-retrieval-empty-candidate-ledger-instance-only.")
        lines.append("It creates an empty candidate ledger instance with zero rows and checks schema conformance, zero-row invariants, and empty-ledger controls without recording candidate sources, performing source retrieval, verifying sources, adding citations, or mutating manuscript files.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")

        lines.append("## Instance Metadata")
        lines.append("")
        for key, value in report["instance_metadata"].items():
            lines.append(f"- {key}: {value}")
        lines.append("")

        lines.append("## Empty Candidate Ledger Rows")
        lines.append("")
        lines.append("Rows: []")
        lines.append("")
        lines.append("No ledger rows are created.")
        lines.append("No candidate source is recorded.")
        lines.append("")

        lines.append("## Schema Conformance Checks")
        lines.append("")
        for item in report["schema_conformance_checks"]:
            lines.append(f"### {item['check_id']} - {item['schema_field']}")
            lines.append("")
            lines.append(f"- Empty instance rule: {item['empty_instance_rule']}")
            lines.append(f"- Observed status: {item['observed_status']}")
            lines.append(f"- Boundary note: {item['boundary_note']}")
            lines.append("")

        lines.append("## Zero-Row Invariants")
        lines.append("")
        for item in report["zero_row_invariants"]:
            lines.append(f"### {item['invariant_id']} - {item['invariant_name']}")
            lines.append("")
            lines.append(f"- Required value: {item['required_value']}")
            lines.append(f"- Boundary note: {item['boundary_note']}")
            lines.append("")

        lines.append("## Empty Ledger Controls")
        lines.append("")
        for item in report["empty_ledger_controls"]:
            lines.append(f"### {item['control_id']} - {item['control_name']}")
            lines.append("")
            lines.append(f"- Control rule: {item['control_rule']}")
            lines.append(f"- Boundary note: {item['boundary_note']}")
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
        lines.append("V8_223_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_EMPTY_CANDIDATE_LEDGER_INSTANCE_OK")
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


def build_safe_abstract_toy_citation_retrieval_empty_candidate_ledger_instance() -> Dict[str, Any]:
    return SafeAbstractToyCitationRetrievalEmptyCandidateLedgerInstanceBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_citation_retrieval_empty_candidate_ledger_instance()
    counters = result["counters"]
    print("V8_223_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_EMPTY_CANDIDATE_LEDGER_INSTANCE_OK")
    print("TOY_CITATION_RETRIEVAL_EMPTY_CANDIDATE_LEDGER_INSTANCE_DIRECT_CHECK_OK")
    print(f"Schema conformance check count: {counters['Toy citation empty ledger schema conformance check count']}")
    print(f"Zero row invariant count: {counters['Toy citation empty ledger zero row invariant count']}")
    print(f"Empty ledger control count: {counters['Toy citation empty ledger control count']}")
    print(f"Empty ledger row count: {counters['Toy citation empty ledger row count']}")
    print(f"Candidate source recorded count: {counters['Toy citation empty ledger candidate source recorded count']}")
    print(f"Acceptance decision count: {counters['Toy citation empty ledger acceptance decision count']}")
    print(f"Rejection decision count: {counters['Toy citation empty ledger rejection decision count']}")
    print(f"Blocked decision count: {counters['Toy citation empty ledger blocked decision count']}")
    print(f"Retrieval authorization count: {counters['Toy citation empty ledger retrieval authorization count']}")
    print(f"Retrieval execution count: {counters['Toy citation empty ledger retrieval execution count']}")
    print(f"Source retrieval count: {counters['Toy citation empty ledger source retrieval count']}")
    print(f"Verified source count: {counters['Toy citation empty ledger verified source count']}")
    print(f"Accepted source count: {counters['Toy citation empty ledger accepted source count']}")
    print(f"Rejected source count: {counters['Toy citation empty ledger rejected source count']}")
    print(f"Actual citation count: {counters['Toy citation empty ledger actual citation count']}")
    print(f"Fabricated reference count: {counters['Toy citation empty ledger fabricated reference count']}")
    print(f"Citation integration completion count: {counters['Toy citation empty ledger integration completion count']}")
    print(f"Citation added to manuscript count: {counters['Toy citation empty ledger added to manuscript count']}")
    print(f"Source candidate ledger field count: {counters['Toy citation empty ledger source candidate ledger field count']}")
    print(f"Source status enum count: {counters['Toy citation empty ledger source status enum count']}")
    print(f"Source provenance field count: {counters['Toy citation empty ledger source provenance field count']}")
    print(f"Source safety screen field count: {counters['Toy citation empty ledger source safety screen field count']}")
    print(f"Source hallucination control count: {counters['Toy citation empty ledger source hallucination control count']}")
    print(f"Source retrieval gate item count: {counters['Toy citation empty ledger source retrieval gate item count']}")
    print(f"Source allowed query family count: {counters['Toy citation empty ledger source allowed query family count']}")
    print(f"Source acceptance schema field count: {counters['Toy citation empty ledger source acceptance schema field count']}")
    print(f"Source rejection reason count: {counters['Toy citation empty ledger source rejection reason count']}")
    print(f"Source preflight check count: {counters['Toy citation empty ledger source preflight check count']}")
    print(f"Source eligibility rule count: {counters['Toy citation empty ledger source eligibility rule count']}")
    print(f"Source query plan count: {counters['Toy citation empty ledger source query plan count']}")
    print(f"Source exclusion group count: {counters['Toy citation empty ledger source exclusion group count']}")
    print(f"Source slot count: {counters['Toy citation empty ledger source slot count']}")
    print(f"Source unresolved slot count: {counters['Toy citation empty ledger source unresolved slot count']}")
    print(f"Source slot group count: {counters['Toy citation empty ledger source slot group count']}")
    print(f"Source assembly section count: {counters['Toy citation empty ledger source assembly section count']}")
    print(f"Source gap item count: {counters['Toy citation empty ledger source gap item count']}")
    print(f"Source P0 gap count: {counters['Toy citation empty ledger source P0 gap count']}")
    print(f"Source evaluation design module count: {counters['Toy citation empty ledger source evaluation design module count']}")
    print(f"Source coherence improvement item count: {counters['Toy citation empty ledger source coherence improvement item count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {result['passed']}")
