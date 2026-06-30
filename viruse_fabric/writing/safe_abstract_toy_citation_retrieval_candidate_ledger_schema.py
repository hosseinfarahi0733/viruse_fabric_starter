from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyCitationRetrievalCandidateLedgerSchemaBuilder:
    version = "v8.222"

    source_retrieval_gate_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_readiness_gate_v8_221.json"
    )
    source_retrieval_gate_md_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_readiness_gate_v8_221.md"
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
        "outputs/safe_abstract_toy_citation_retrieval_candidate_ledger_schema_v8_222.md"
    )
    output_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_candidate_ledger_schema_v8_222.json"
    )

    plan_phrase = "citation_retrieval_candidate_ledger_schema_created_but_no_candidates_recorded"

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

    def _ledger_fields(self) -> List[Dict[str, str]]:
        return [
            {
                "field_id": "LEDGER-FIELD-01",
                "field_name": "candidate_id",
                "field_purpose": "Stable identifier for a future retrieval candidate.",
                "required_rule": "Must remain empty until a separate source retrieval milestone creates a real candidate.",
                "boundary_note": "Candidate ledger schema only. No candidate source is recorded.",
            },
            {
                "field_id": "LEDGER-FIELD-02",
                "field_name": "slot_id",
                "field_purpose": "Maps a future candidate to exactly one unresolved citation slot.",
                "required_rule": "Must reference one CIT-SLOT identifier from the unresolved slot list.",
                "boundary_note": "No actual citation is added.",
            },
            {
                "field_id": "LEDGER-FIELD-03",
                "field_name": "query_family_id",
                "field_purpose": "Links a future candidate to an allowed query family from the retrieval gate.",
                "required_rule": "Must use an allowed query family and must not introduce a new unreviewed search family.",
                "boundary_note": "Future source retrieval requires a separate official milestone.",
            },
            {
                "field_id": "LEDGER-FIELD-04",
                "field_name": "candidate_title",
                "field_purpose": "Stores the title of a future retrieved candidate source.",
                "required_rule": "Must not be filled from memory, guesswork, placeholder text, or fabricated references.",
                "boundary_note": "No fabricated reference is introduced.",
            },
            {
                "field_id": "LEDGER-FIELD-05",
                "field_name": "candidate_author_or_body",
                "field_purpose": "Stores authorship or issuing body after future retrieval.",
                "required_rule": "Must remain empty until source metadata is retrieved and separately checked.",
                "boundary_note": "No source is claimed as verified.",
            },
            {
                "field_id": "LEDGER-FIELD-06",
                "field_name": "candidate_year",
                "field_purpose": "Stores candidate publication year after future retrieval.",
                "required_rule": "Must not be inferred when unavailable.",
                "boundary_note": "No source retrieval is performed.",
            },
            {
                "field_id": "LEDGER-FIELD-07",
                "field_name": "candidate_locator",
                "field_purpose": "Stores DOI, URL, database record, ISBN, or stable locator after future retrieval.",
                "required_rule": "Must reject imaginary DOI records, unverifiable URLs, and placeholder locators.",
                "boundary_note": "No fabricated reference is introduced.",
            },
            {
                "field_id": "LEDGER-FIELD-08",
                "field_name": "source_type",
                "field_purpose": "Classifies future source type.",
                "required_rule": "Allowed values must remain within the source type enum and must not imply validation by type alone.",
                "boundary_note": "No evidence upgrade is completed.",
            },
            {
                "field_id": "LEDGER-FIELD-09",
                "field_name": "evidence_role",
                "field_purpose": "States the narrow role the future source may support.",
                "required_rule": "Must not support project result validation, performance claims, readiness approval, or proof.",
                "boundary_note": "does not validate scientific claims.",
            },
            {
                "field_id": "LEDGER-FIELD-10",
                "field_name": "safety_screen_status",
                "field_purpose": "Records whether a future candidate passes safety exclusion screening.",
                "required_rule": "Must reject real biological datasets, real pathogen models, receptor parameters, operational targeting, wet-lab protocols, and actionable biosafety-risk instructions.",
                "boundary_note": "No real biological datasets, no real pathogen models, no receptor parameters, and no operational targeting are introduced.",
            },
            {
                "field_id": "LEDGER-FIELD-11",
                "field_name": "verification_status",
                "field_purpose": "Records verification state after a future verification milestone.",
                "required_rule": "Must remain not_verified in this milestone.",
                "boundary_note": "No source is claimed as verified.",
            },
            {
                "field_id": "LEDGER-FIELD-12",
                "field_name": "acceptance_status",
                "field_purpose": "Records whether a future candidate is pending, accepted, rejected, or blocked.",
                "required_rule": "Must remain not_recorded in this milestone because no candidate exists.",
                "boundary_note": "No accepted source and no rejected source is recorded.",
            },
            {
                "field_id": "LEDGER-FIELD-13",
                "field_name": "citation_integration_status",
                "field_purpose": "Records whether a future verified source has been integrated into a manuscript citation slot.",
                "required_rule": "Must remain not_integrated in this milestone.",
                "boundary_note": "does not complete citation integration.",
            },
            {
                "field_id": "LEDGER-FIELD-14",
                "field_name": "manuscript_mutation_status",
                "field_purpose": "Records whether a manuscript file was changed.",
                "required_rule": "Must remain no_mutation in this milestone.",
                "boundary_note": "No manuscript file is modified.",
            },
            {
                "field_id": "LEDGER-FIELD-15",
                "field_name": "readiness_claim_status",
                "field_purpose": "Records whether a candidate is being misused to imply readiness.",
                "required_rule": "Must remain no_readiness_claim in this milestone.",
                "boundary_note": "Manuscript submission ready count remains zero.",
            },
            {
                "field_id": "LEDGER-FIELD-16",
                "field_name": "future_authorization_reference",
                "field_purpose": "Stores the future official milestone that authorizes retrieval, verification, or integration.",
                "required_rule": "Must state that future source retrieval requires a separate official milestone.",
                "boundary_note": "Future source retrieval requires a separate official milestone.",
            },
        ]

    def _status_enums(self) -> List[Dict[str, str]]:
        return [
            {
                "enum_id": "STATUS-01",
                "enum_name": "not_recorded",
                "allowed_use": "Default state for candidate fields in v8.222 because no candidate source is recorded.",
                "boundary_note": "No candidate source is recorded.",
            },
            {
                "enum_id": "STATUS-02",
                "enum_name": "pending_future_retrieval",
                "allowed_use": "May describe a future ledger row only after retrieval authorization exists.",
                "boundary_note": "No retrieval authorization is granted.",
            },
            {
                "enum_id": "STATUS-03",
                "enum_name": "retrieved_not_verified",
                "allowed_use": "Reserved for a future retrieval milestone only.",
                "boundary_note": "No source retrieval is performed.",
            },
            {
                "enum_id": "STATUS-04",
                "enum_name": "verified_not_integrated",
                "allowed_use": "Reserved for a future verification milestone only.",
                "boundary_note": "No source is claimed as verified.",
            },
            {
                "enum_id": "STATUS-05",
                "enum_name": "accepted_candidate",
                "allowed_use": "Reserved for future accepted candidate records after retrieval and screening.",
                "boundary_note": "Accepted source count remains zero.",
            },
            {
                "enum_id": "STATUS-06",
                "enum_name": "rejected_candidate",
                "allowed_use": "Reserved for future rejected candidate records after retrieval and screening.",
                "boundary_note": "Rejected source count remains zero.",
            },
            {
                "enum_id": "STATUS-07",
                "enum_name": "blocked_for_safety",
                "allowed_use": "Reserved for future candidates that violate safety exclusions.",
                "boundary_note": "Wet-lab protocol count and actionable biosafety-risk instruction count remain zero.",
            },
            {
                "enum_id": "STATUS-08",
                "enum_name": "not_integrated",
                "allowed_use": "Default citation integration state in v8.222.",
                "boundary_note": "No new citation is added and does not complete citation integration.",
            },
        ]

    def _provenance_fields(self) -> List[Dict[str, str]]:
        return [
            {
                "provenance_id": "PROV-01",
                "field_name": "retrieval_milestone_id",
                "required_rule": "Must name the future official milestone that performed source retrieval.",
                "boundary_note": "Future source retrieval requires a separate official milestone.",
            },
            {
                "provenance_id": "PROV-02",
                "field_name": "retrieval_query_used",
                "required_rule": "Must match an allowed query family and must not be invented after the fact.",
                "boundary_note": "No source retrieval is performed.",
            },
            {
                "provenance_id": "PROV-03",
                "field_name": "retrieval_database_or_index",
                "required_rule": "Must identify the future database, index, publisher site, or stable discovery location.",
                "boundary_note": "No source is claimed as verified.",
            },
            {
                "provenance_id": "PROV-04",
                "field_name": "retrieval_timestamp",
                "required_rule": "Must be recorded only when a future retrieval action actually occurs.",
                "boundary_note": "Retrieval execution count remains zero.",
            },
            {
                "provenance_id": "PROV-05",
                "field_name": "metadata_capture_method",
                "required_rule": "Must state how title, author, year, and locator were captured.",
                "boundary_note": "No candidate source is recorded.",
            },
            {
                "provenance_id": "PROV-06",
                "field_name": "verification_method",
                "required_rule": "Must remain not_verified until a future verification step checks the source.",
                "boundary_note": "No source is claimed as verified.",
            },
            {
                "provenance_id": "PROV-07",
                "field_name": "safety_screen_method",
                "required_rule": "Must record how safety exclusions were checked in a future milestone.",
                "boundary_note": "No real biological datasets and no real pathogen models are introduced.",
            },
            {
                "provenance_id": "PROV-08",
                "field_name": "claim_boundary_review",
                "required_rule": "Must confirm that a future candidate is not used to validate results or claim readiness.",
                "boundary_note": "does not validate scientific claims.",
            },
            {
                "provenance_id": "PROV-09",
                "field_name": "integration_milestone_id",
                "required_rule": "Must name the future official milestone that integrates a citation.",
                "boundary_note": "does not complete citation integration.",
            },
            {
                "provenance_id": "PROV-10",
                "field_name": "audit_trail_note",
                "required_rule": "Must preserve a plain-language audit note for why a future candidate was accepted, rejected, or blocked.",
                "boundary_note": "No accepted source and no rejected source is recorded.",
            },
        ]

    def _safety_screen_fields(self) -> List[Dict[str, str]]:
        return [
            {
                "screen_id": "SCREEN-01",
                "screen_name": "real_biological_dataset_screen",
                "screen_rule": "Reject candidate if it requires importing, analyzing, or operationalizing real biological datasets.",
                "boundary_note": "Real biological dataset import count remains zero.",
            },
            {
                "screen_id": "SCREEN-02",
                "screen_name": "real_pathogen_model_screen",
                "screen_rule": "Reject candidate if it introduces real pathogen simulation or operational biological modeling.",
                "boundary_note": "Real pathogen simulation count remains zero.",
            },
            {
                "screen_id": "SCREEN-03",
                "screen_name": "receptor_parameter_screen",
                "screen_rule": "Reject candidate if it introduces receptor parameters or real receptor mechanics.",
                "boundary_note": "Real receptor parameter count remains zero.",
            },
            {
                "screen_id": "SCREEN-04",
                "screen_name": "operational_targeting_screen",
                "screen_rule": "Reject candidate if it supports operational targeting, host tropism prediction, or host range prediction.",
                "boundary_note": "Operational host targeting count and real host range prediction count remain zero.",
            },
            {
                "screen_id": "SCREEN-05",
                "screen_name": "wet_lab_protocol_screen",
                "screen_rule": "Reject candidate if it contains wet-lab protocols or actionable experimental instructions.",
                "boundary_note": "Wet-lab protocol count remains zero.",
            },
            {
                "screen_id": "SCREEN-06",
                "screen_name": "biosafety_risk_instruction_screen",
                "screen_rule": "Reject candidate if it enables actionable biosafety-risk instructions.",
                "boundary_note": "Actionable biosafety-risk instruction count remains zero.",
            },
            {
                "screen_id": "SCREEN-07",
                "screen_name": "infectivity_optimization_screen",
                "screen_rule": "Reject candidate if it supports real-world infectivity optimization.",
                "boundary_note": "Real-world infectivity optimization count remains zero.",
            },
            {
                "screen_id": "SCREEN-08",
                "screen_name": "immune_evasion_screen",
                "screen_rule": "Reject candidate if it supports immune evasion optimization.",
                "boundary_note": "Immune evasion optimization count remains zero.",
            },
            {
                "screen_id": "SCREEN-09",
                "screen_name": "overclaim_screen",
                "screen_rule": "Reject candidate if it is used to imply validation, proof, readiness, evidence-gap closure, or evaluation results.",
                "boundary_note": "External validation count, proof assistant verification count, and readiness approval count remain zero.",
            },
            {
                "screen_id": "SCREEN-10",
                "screen_name": "manuscript_mutation_screen",
                "screen_rule": "Reject any use of a candidate as permission to mutate manuscript files in this milestone.",
                "boundary_note": "No manuscript file is modified.",
            },
        ]

    def _hallucination_controls(self) -> List[Dict[str, str]]:
        return [
            {
                "control_id": "HALLUCINATION-01",
                "control_name": "no_memory_based_reference_creation",
                "control_rule": "Never create candidate metadata from memory or model recall.",
                "boundary_note": "No fabricated reference is introduced.",
            },
            {
                "control_id": "HALLUCINATION-02",
                "control_name": "no_placeholder_to_reference_upgrade",
                "control_rule": "Never convert a placeholder citation slot into a reference without retrieval evidence.",
                "boundary_note": "No actual citation is added.",
            },
            {
                "control_id": "HALLUCINATION-03",
                "control_name": "locator_required_for_future_candidate",
                "control_rule": "A future candidate must have a stable locator or explicit reason for rejection.",
                "boundary_note": "No candidate source is recorded.",
            },
            {
                "control_id": "HALLUCINATION-04",
                "control_name": "verification_separate_from_retrieval",
                "control_rule": "Retrieval alone must not be treated as source verification.",
                "boundary_note": "No source is claimed as verified.",
            },
            {
                "control_id": "HALLUCINATION-05",
                "control_name": "acceptance_separate_from_verification",
                "control_rule": "Verification alone must not be treated as acceptance for citation integration.",
                "boundary_note": "Accepted source count remains zero.",
            },
            {
                "control_id": "HALLUCINATION-06",
                "control_name": "integration_separate_from_acceptance",
                "control_rule": "Acceptance alone must not modify manuscript files.",
                "boundary_note": "No manuscript file is modified.",
            },
            {
                "control_id": "HALLUCINATION-07",
                "control_name": "no_retroactive_source_claims",
                "control_rule": "Do not claim earlier milestones retrieved or verified sources.",
                "boundary_note": "Source retrieval count and verified source count remain zero.",
            },
            {
                "control_id": "HALLUCINATION-08",
                "control_name": "no_readiness_from_citation_presence",
                "control_rule": "Even future citations must not imply submission readiness by themselves.",
                "boundary_note": "Manuscript submission ready count remains zero.",
            },
            {
                "control_id": "HALLUCINATION-09",
                "control_name": "no_evidence_upgrade_from_schema",
                "control_rule": "A schema does not close evidence gaps or validate scientific claims.",
                "boundary_note": "No evidence upgrade is completed.",
            },
            {
                "control_id": "HALLUCINATION-10",
                "control_name": "future_authorization_required",
                "control_rule": "Future retrieval, verification, and integration require separate official milestones.",
                "boundary_note": "Future source retrieval requires a separate official milestone.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        retrieval_gate_source = self._load_json(self.source_retrieval_gate_json_path)
        retrieval_gate_md = self._load_text(self.source_retrieval_gate_md_path)
        eligibility_source = self._load_json(self.source_eligibility_json_path)
        citation_slot_source = self._load_json(self.source_citation_slot_json_path)
        coherence_source = self._load_json(self.source_coherence_json_path)
        eval_source = self._load_json(self.source_eval_json_path)
        gap_source = self._load_json(self.source_gap_json_path)
        assembly_source = self._load_json(self.source_assembly_json_path)

        retrieval_counters = retrieval_gate_source.get("counters", {})
        eligibility_counters = eligibility_source.get("counters", {})
        citation_counters = citation_slot_source.get("counters", {})
        coherence_counters = coherence_source.get("counters", {})
        eval_counters = eval_source.get("counters", {})
        gap_counters = gap_source.get("counters", {})
        assembly_counters = assembly_source.get("counters", {})

        ledger_fields = self._ledger_fields()
        status_enums = self._status_enums()
        provenance_fields = self._provenance_fields()
        safety_screen_fields = self._safety_screen_fields()
        hallucination_controls = self._hallucination_controls()

        counters = {
            "Safe abstract toy citation retrieval candidate ledger schema count": 1,
            "New safe abstract toy citation retrieval candidate ledger schema count": 1,
            "Toy citation retrieval candidate ledger schema JSON export count": 1,
            "Toy citation candidate ledger field count": len(ledger_fields),
            "Toy citation candidate status enum count": len(status_enums),
            "Toy citation candidate provenance field count": len(provenance_fields),
            "Toy citation candidate safety screen field count": len(safety_screen_fields),
            "Toy citation candidate hallucination control count": len(hallucination_controls),
            "Toy citation candidate ledger row count": 0,
            "Toy citation candidate source recorded count": 0,
            "Toy citation candidate acceptance decision count": 0,
            "Toy citation candidate rejection decision count": 0,
            "Toy citation candidate blocked decision count": 0,
            "Toy citation candidate retrieval authorization count": 0,
            "Toy citation candidate retrieval execution count": 0,
            "Toy citation candidate source retrieval count": 0,
            "Toy citation candidate verified source count": 0,
            "Toy citation candidate accepted source count": 0,
            "Toy citation candidate rejected source count": 0,
            "Toy citation candidate actual citation count": 0,
            "Toy citation candidate fabricated reference count": 0,
            "Toy citation candidate integration completion count": 0,
            "Toy citation candidate added to manuscript count": 0,
            "Toy citation candidate source retrieval gate item count": retrieval_counters.get("Toy citation retrieval gate item count"),
            "Toy citation candidate source allowed query family count": retrieval_counters.get("Toy citation retrieval allowed query family count"),
            "Toy citation candidate source acceptance schema field count": retrieval_counters.get("Toy citation retrieval acceptance schema field count"),
            "Toy citation candidate source rejection reason count": retrieval_counters.get("Toy citation retrieval rejection reason count"),
            "Toy citation candidate source preflight check count": retrieval_counters.get("Toy citation retrieval preflight check count"),
            "Toy citation candidate source prior retrieval authorization count": retrieval_counters.get("Toy citation retrieval authorization count"),
            "Toy citation candidate source prior retrieval execution count": retrieval_counters.get("Toy citation retrieval execution count"),
            "Toy citation candidate source prior source retrieval count": retrieval_counters.get("Toy citation retrieval source retrieval count"),
            "Toy citation candidate source prior verified source count": retrieval_counters.get("Toy citation retrieval verified source count"),
            "Toy citation candidate source prior accepted source count": retrieval_counters.get("Toy citation retrieval accepted source count"),
            "Toy citation candidate source prior rejected source count": retrieval_counters.get("Toy citation retrieval rejected source count"),
            "Toy citation candidate source prior actual citation count": retrieval_counters.get("Toy citation retrieval actual citation count"),
            "Toy citation candidate source prior fabricated reference count": retrieval_counters.get("Toy citation retrieval fabricated reference count"),
            "Toy citation candidate source prior integration completion count": retrieval_counters.get("Toy citation retrieval integration completion count"),
            "Toy citation candidate source prior added to manuscript count": retrieval_counters.get("Toy citation retrieval added to manuscript count"),
            "Toy citation candidate source eligibility rule count": eligibility_counters.get("Toy citation source eligibility rule count"),
            "Toy citation candidate source query plan count": eligibility_counters.get("Toy citation source query plan count"),
            "Toy citation candidate source exclusion group count": eligibility_counters.get("Toy citation source exclusion group count"),
            "Toy citation candidate source slot count": citation_counters.get("Toy citation slot count"),
            "Toy citation candidate source unresolved slot count": citation_counters.get("Toy citation unresolved slot count"),
            "Toy citation candidate source slot group count": citation_counters.get("Toy citation slot group count"),
            "Toy citation candidate source assembly section count": assembly_counters.get("Toy manuscript assembly preview section count"),
            "Toy citation candidate source gap item count": gap_counters.get("Toy scientific gap register item count"),
            "Toy citation candidate source P0 gap count": gap_counters.get("Toy scientific gap P0 count"),
            "Toy citation candidate source evidence upgrade completed count": gap_counters.get("Toy scientific evidence upgrade completed count"),
            "Toy citation candidate source evaluation design module count": eval_counters.get("Toy evaluation design module count"),
            "Toy citation candidate source actual evaluation run count": eval_counters.get("Toy evaluation actual run count"),
            "Toy citation candidate source validation claim count": eval_counters.get("Toy evaluation validation claim count"),
            "Toy citation candidate source coherence improvement item count": coherence_counters.get("Toy manuscript coherence improvement item count"),
            "Toy citation candidate source coherence rewrite application count": coherence_counters.get("Toy manuscript coherence rewrite application count"),
            "Toy citation candidate ledger schema execution count": 1,
            "Toy citation candidate ledger schema direct execution count": 1,
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
            "title": "Safe Abstract Toy Citation Retrieval Candidate Ledger Schema",
            "source_retrieval_gate_json": str(self.source_retrieval_gate_json_path),
            "source_retrieval_gate_markdown": str(self.source_retrieval_gate_md_path),
            "source_retrieval_gate_markdown_character_count": len(retrieval_gate_md),
            "source_eligibility_json": str(self.source_eligibility_json_path),
            "source_citation_slot_json": str(self.source_citation_slot_json_path),
            "source_coherence_json": str(self.source_coherence_json_path),
            "source_evaluation_design_json": str(self.source_eval_json_path),
            "source_gap_json": str(self.source_gap_json_path),
            "source_assembly_json": str(self.source_assembly_json_path),
            "plan_phrase": self.plan_phrase,
            "scope": "citation-retrieval-candidate-ledger-schema-only",
            "safe_abstract_toy_only": True,
            "synthetic_only": True,
            "abstract_graphs_only": True,
            "unitless_parameters_only": True,
            "non_operational_only": True,
            "candidate_ledger_schema_completed": True,
            "candidate_ledger_rows_created": False,
            "candidate_sources_recorded": False,
            "candidate_acceptance_decisions_recorded": False,
            "candidate_rejection_decisions_recorded": False,
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
                "This v8.222 artifact creates a citation retrieval candidate ledger schema only. "
                "Candidate ledger schema only. No candidate source is recorded. "
                "No retrieval authorization is granted. No source retrieval is performed. "
                "No actual citation is added. No fabricated reference is introduced. "
                "No source is claimed as verified. It does not complete citation integration, "
                "does not validate scientific claims, does not modify manuscript files, and No manuscript file is modified. "
                "No new citation is added. Future source retrieval requires a separate official milestone."
            ),
            "ledger_fields": ledger_fields,
            "status_enums": status_enums,
            "provenance_fields": provenance_fields,
            "safety_screen_fields": safety_screen_fields,
            "hallucination_controls": hallucination_controls,
            "boundary_notes": (
                [item["boundary_note"] for item in ledger_fields]
                + [item["boundary_note"] for item in status_enums]
                + [item["boundary_note"] for item in provenance_fields]
                + [item["boundary_note"] for item in safety_screen_fields]
                + [item["boundary_note"] for item in hallucination_controls]
            ),
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "citation-retrieval-candidate-ledger-schema-only":
            raise AssertionError("v8.222 must remain citation-retrieval-candidate-ledger-schema-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.222 candidate ledger schema must pass.")

        if report["candidate_ledger_schema_completed"] is not True:
            raise AssertionError("v8.222 should complete only the candidate ledger schema.")

        for field in [
            "candidate_ledger_rows_created",
            "candidate_sources_recorded",
            "candidate_acceptance_decisions_recorded",
            "candidate_rejection_decisions_recorded",
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
            "Toy citation candidate ledger field count": 16,
            "Toy citation candidate status enum count": 8,
            "Toy citation candidate provenance field count": 10,
            "Toy citation candidate safety screen field count": 10,
            "Toy citation candidate hallucination control count": 10,
            "Toy citation candidate ledger row count": 0,
            "Toy citation candidate source recorded count": 0,
            "Toy citation candidate acceptance decision count": 0,
            "Toy citation candidate rejection decision count": 0,
            "Toy citation candidate blocked decision count": 0,
            "Toy citation candidate retrieval authorization count": 0,
            "Toy citation candidate retrieval execution count": 0,
            "Toy citation candidate source retrieval count": 0,
            "Toy citation candidate verified source count": 0,
            "Toy citation candidate accepted source count": 0,
            "Toy citation candidate rejected source count": 0,
            "Toy citation candidate actual citation count": 0,
            "Toy citation candidate fabricated reference count": 0,
            "Toy citation candidate integration completion count": 0,
            "Toy citation candidate added to manuscript count": 0,
            "Toy citation candidate source retrieval gate item count": 12,
            "Toy citation candidate source allowed query family count": 12,
            "Toy citation candidate source acceptance schema field count": 12,
            "Toy citation candidate source rejection reason count": 10,
            "Toy citation candidate source preflight check count": 10,
            "Toy citation candidate source prior retrieval authorization count": 0,
            "Toy citation candidate source prior retrieval execution count": 0,
            "Toy citation candidate source prior source retrieval count": 0,
            "Toy citation candidate source prior verified source count": 0,
            "Toy citation candidate source prior accepted source count": 0,
            "Toy citation candidate source prior rejected source count": 0,
            "Toy citation candidate source prior actual citation count": 0,
            "Toy citation candidate source prior fabricated reference count": 0,
            "Toy citation candidate source prior integration completion count": 0,
            "Toy citation candidate source prior added to manuscript count": 0,
            "Toy citation candidate source eligibility rule count": 12,
            "Toy citation candidate source query plan count": 12,
            "Toy citation candidate source exclusion group count": 4,
            "Toy citation candidate source slot count": 12,
            "Toy citation candidate source unresolved slot count": 12,
            "Toy citation candidate source slot group count": 4,
            "Toy citation candidate source assembly section count": 9,
            "Toy citation candidate source gap item count": 12,
            "Toy citation candidate source P0 gap count": 6,
            "Toy citation candidate source evidence upgrade completed count": 0,
            "Toy citation candidate source evaluation design module count": 10,
            "Toy citation candidate source actual evaluation run count": 0,
            "Toy citation candidate source validation claim count": 0,
            "Toy citation candidate source coherence improvement item count": 10,
            "Toy citation candidate source coherence rewrite application count": 0,
        }

        for name, expected in expected_counts.items():
            if counters.get(name) != expected:
                raise AssertionError(f"Expected {expected} for {name}, got {counters.get(name)}")

        combined_text = (
            json.dumps(report["ledger_fields"], ensure_ascii=False)
            + " "
            + json.dumps(report["status_enums"], ensure_ascii=False)
            + " "
            + json.dumps(report["provenance_fields"], ensure_ascii=False)
            + " "
            + json.dumps(report["safety_screen_fields"], ensure_ascii=False)
            + " "
            + json.dumps(report["hallucination_controls"], ensure_ascii=False)
            + " "
            + report["non_readiness_disclaimer"]
        )

        required_phrases = [
            "citation retrieval candidate ledger schema",
            "Candidate ledger schema only",
            "No candidate source is recorded",
            "not_recorded",
            "pending_future_retrieval",
            "accepted_candidate",
            "rejected_candidate",
            "blocked_for_safety",
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
                raise AssertionError(f"Missing required candidate ledger phrase: {phrase}")

        must_be_zero = [
            "Toy citation candidate ledger row count",
            "Toy citation candidate source recorded count",
            "Toy citation candidate acceptance decision count",
            "Toy citation candidate rejection decision count",
            "Toy citation candidate blocked decision count",
            "Toy citation candidate retrieval authorization count",
            "Toy citation candidate retrieval execution count",
            "Toy citation candidate source retrieval count",
            "Toy citation candidate verified source count",
            "Toy citation candidate accepted source count",
            "Toy citation candidate rejected source count",
            "Toy citation candidate actual citation count",
            "Toy citation candidate fabricated reference count",
            "Toy citation candidate integration completion count",
            "Toy citation candidate added to manuscript count",
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

        lines.append("# Safe Abstract Toy Citation Retrieval Candidate Ledger Schema")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is citation-retrieval-candidate-ledger-schema-only.")
        lines.append("It defines candidate ledger fields, status enums, provenance fields, safety screen fields, and hallucination controls without recording candidate sources, performing source retrieval, verifying sources, adding citations, or mutating manuscript files.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")

        lines.append("## Ledger Fields")
        lines.append("")
        for item in report["ledger_fields"]:
            lines.append(f"### {item['field_id']} — {item['field_name']}")
            lines.append("")
            lines.append(f"- Purpose: {item['field_purpose']}")
            lines.append(f"- Required rule: {item['required_rule']}")
            lines.append(f"- Boundary note: {item['boundary_note']}")
            lines.append("")

        lines.append("## Status Enums")
        lines.append("")
        for item in report["status_enums"]:
            lines.append(f"### {item['enum_id']} — {item['enum_name']}")
            lines.append("")
            lines.append(f"- Allowed use: {item['allowed_use']}")
            lines.append(f"- Boundary note: {item['boundary_note']}")
            lines.append("")

        lines.append("## Provenance Fields")
        lines.append("")
        for item in report["provenance_fields"]:
            lines.append(f"### {item['provenance_id']} — {item['field_name']}")
            lines.append("")
            lines.append(f"- Required rule: {item['required_rule']}")
            lines.append(f"- Boundary note: {item['boundary_note']}")
            lines.append("")

        lines.append("## Safety Screen Fields")
        lines.append("")
        for item in report["safety_screen_fields"]:
            lines.append(f"### {item['screen_id']} — {item['screen_name']}")
            lines.append("")
            lines.append(f"- Screen rule: {item['screen_rule']}")
            lines.append(f"- Boundary note: {item['boundary_note']}")
            lines.append("")

        lines.append("## Hallucination Controls")
        lines.append("")
        for item in report["hallucination_controls"]:
            lines.append(f"### {item['control_id']} — {item['control_name']}")
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
        lines.append("V8_222_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_CANDIDATE_LEDGER_SCHEMA_OK")
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


def build_safe_abstract_toy_citation_retrieval_candidate_ledger_schema() -> Dict[str, Any]:
    return SafeAbstractToyCitationRetrievalCandidateLedgerSchemaBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_citation_retrieval_candidate_ledger_schema()
    counters = result["counters"]
    print("V8_222_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_CANDIDATE_LEDGER_SCHEMA_OK")
    print("TOY_CITATION_RETRIEVAL_CANDIDATE_LEDGER_SCHEMA_DIRECT_CHECK_OK")
    print(f"Candidate ledger field count: {counters['Toy citation candidate ledger field count']}")
    print(f"Candidate status enum count: {counters['Toy citation candidate status enum count']}")
    print(f"Candidate provenance field count: {counters['Toy citation candidate provenance field count']}")
    print(f"Candidate safety screen field count: {counters['Toy citation candidate safety screen field count']}")
    print(f"Candidate hallucination control count: {counters['Toy citation candidate hallucination control count']}")
    print(f"Candidate ledger row count: {counters['Toy citation candidate ledger row count']}")
    print(f"Candidate source recorded count: {counters['Toy citation candidate source recorded count']}")
    print(f"Candidate acceptance decision count: {counters['Toy citation candidate acceptance decision count']}")
    print(f"Candidate rejection decision count: {counters['Toy citation candidate rejection decision count']}")
    print(f"Candidate blocked decision count: {counters['Toy citation candidate blocked decision count']}")
    print(f"Retrieval authorization count: {counters['Toy citation candidate retrieval authorization count']}")
    print(f"Retrieval execution count: {counters['Toy citation candidate retrieval execution count']}")
    print(f"Source retrieval count: {counters['Toy citation candidate source retrieval count']}")
    print(f"Verified source count: {counters['Toy citation candidate verified source count']}")
    print(f"Accepted source count: {counters['Toy citation candidate accepted source count']}")
    print(f"Rejected source count: {counters['Toy citation candidate rejected source count']}")
    print(f"Actual citation count: {counters['Toy citation candidate actual citation count']}")
    print(f"Fabricated reference count: {counters['Toy citation candidate fabricated reference count']}")
    print(f"Citation integration completion count: {counters['Toy citation candidate integration completion count']}")
    print(f"Citation added to manuscript count: {counters['Toy citation candidate added to manuscript count']}")
    print(f"Source retrieval gate item count: {counters['Toy citation candidate source retrieval gate item count']}")
    print(f"Source allowed query family count: {counters['Toy citation candidate source allowed query family count']}")
    print(f"Source acceptance schema field count: {counters['Toy citation candidate source acceptance schema field count']}")
    print(f"Source rejection reason count: {counters['Toy citation candidate source rejection reason count']}")
    print(f"Source preflight check count: {counters['Toy citation candidate source preflight check count']}")
    print(f"Source eligibility rule count: {counters['Toy citation candidate source eligibility rule count']}")
    print(f"Source query plan count: {counters['Toy citation candidate source query plan count']}")
    print(f"Source exclusion group count: {counters['Toy citation candidate source exclusion group count']}")
    print(f"Source slot count: {counters['Toy citation candidate source slot count']}")
    print(f"Source unresolved slot count: {counters['Toy citation candidate source unresolved slot count']}")
    print(f"Source slot group count: {counters['Toy citation candidate source slot group count']}")
    print(f"Source assembly section count: {counters['Toy citation candidate source assembly section count']}")
    print(f"Source gap item count: {counters['Toy citation candidate source gap item count']}")
    print(f"Source P0 gap count: {counters['Toy citation candidate source P0 gap count']}")
    print(f"Source evaluation design module count: {counters['Toy citation candidate source evaluation design module count']}")
    print(f"Source coherence improvement item count: {counters['Toy citation candidate source coherence improvement item count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {result['passed']}")
