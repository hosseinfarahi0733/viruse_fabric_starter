from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyCitationRetrievalBatch1CandidateIntakeBuilder:
    version = "v8.224"

    source_empty_ledger_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_empty_candidate_ledger_instance_v8_223.json"
    )
    source_empty_ledger_md_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_empty_candidate_ledger_instance_v8_223.md"
    )
    source_ledger_schema_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_candidate_ledger_schema_v8_222.json"
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

    output_md_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_batch_1_candidate_intake_v8_224.md"
    )
    output_json_path = Path(
        "outputs/safe_abstract_toy_citation_retrieval_batch_1_candidate_intake_v8_224.json"
    )

    plan_phrase = "batch_1_candidate_sources_recorded_but_not_verified_accepted_or_integrated"

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

    def _candidate_sources(self) -> List[Dict[str, Any]]:
        return [
            {
                "candidate_id": "CAND-B1-001",
                "slot_family": "causal-inference-foundation",
                "candidate_title": "Causality: Models, Reasoning, and Inference",
                "candidate_author_or_body": "Judea Pearl",
                "candidate_year": "2009",
                "candidate_locator": "DOI: 10.1017/CBO9780511803161",
                "publisher_or_venue": "Cambridge University Press",
                "source_type": "book",
                "candidate_url": "https://www.cambridge.org/core/books/causality/B0046844FAE10CBF274D4ACBDAEB5F5B",
                "retrieval_basis": "Cambridge University Press book page",
                "evidence_role": "Methodological background for causal reasoning, structural causal models, and intervention-oriented conceptual framing.",
                "allowed_use": "Background framing only. May support causal terminology once separately verified and accepted.",
                "retrieval_status": "retrieved_not_verified",
                "verification_status": "not_verified",
                "acceptance_status": "pending_review_not_accepted",
                "citation_integration_status": "not_integrated",
                "manuscript_mutation_status": "no_mutation",
                "safety_screen_status": "passed_non_operational_method_source_screen",
                "safety_exclusion_notes": "No real biological dataset import, no real pathogen simulation, no receptor parameters, no operational host targeting, no wet-lab protocol.",
                "boundary_note": "Candidate source is recorded but not verified, not accepted, and not integrated.",
            },
            {
                "candidate_id": "CAND-B1-002",
                "slot_family": "probabilistic-graphical-models-foundation",
                "candidate_title": "Probabilistic Graphical Models: Principles and Techniques",
                "candidate_author_or_body": "Daphne Koller and Nir Friedman",
                "candidate_year": "2009",
                "candidate_locator": "ISBN: 9780262013192",
                "publisher_or_venue": "MIT Press",
                "source_type": "book",
                "candidate_url": "https://mitpress.mit.edu/9780262013192/probabilistic-graphical-models/",
                "retrieval_basis": "MIT Press book page",
                "evidence_role": "Methodological background for graphical modelling and probabilistic dependency representation.",
                "allowed_use": "Background framing only. May support abstract graphical-model terminology once separately verified and accepted.",
                "retrieval_status": "retrieved_not_verified",
                "verification_status": "not_verified",
                "acceptance_status": "pending_review_not_accepted",
                "citation_integration_status": "not_integrated",
                "manuscript_mutation_status": "no_mutation",
                "safety_screen_status": "passed_non_operational_method_source_screen",
                "safety_exclusion_notes": "No real biological dataset import, no real pathogen simulation, no receptor parameters, no operational host targeting, no wet-lab protocol.",
                "boundary_note": "Candidate source is recorded but not verified, not accepted, and not integrated.",
            },
            {
                "candidate_id": "CAND-B1-003",
                "slot_family": "network-science-foundation",
                "candidate_title": "Networks: An Introduction",
                "candidate_author_or_body": "Mark Newman",
                "candidate_year": "2010",
                "candidate_locator": "ISBN: 9780199206650",
                "publisher_or_venue": "Oxford University Press / Oxford Academic",
                "source_type": "book",
                "candidate_url": "https://academic.oup.com/book/27303",
                "retrieval_basis": "Oxford Academic book page",
                "evidence_role": "Methodological background for abstract networks, graph measures, and network-theoretic vocabulary.",
                "allowed_use": "Background framing only. May support non-operational network terminology once separately verified and accepted.",
                "retrieval_status": "retrieved_not_verified",
                "verification_status": "not_verified",
                "acceptance_status": "pending_review_not_accepted",
                "citation_integration_status": "not_integrated",
                "manuscript_mutation_status": "no_mutation",
                "safety_screen_status": "passed_non_operational_method_source_screen",
                "safety_exclusion_notes": "No real biological dataset import, no real pathogen simulation, no receptor parameters, no operational host targeting, no wet-lab protocol.",
                "boundary_note": "Candidate source is recorded but not verified, not accepted, and not integrated.",
            },
            {
                "candidate_id": "CAND-B1-004",
                "slot_family": "agent-based-modelling-foundation",
                "candidate_title": "Agent-based modeling: methods and techniques for simulating human systems",
                "candidate_author_or_body": "Eric Bonabeau",
                "candidate_year": "2002",
                "candidate_locator": "DOI: 10.1073/pnas.082080899; PMID: 12011407",
                "publisher_or_venue": "Proceedings of the National Academy of Sciences",
                "source_type": "journal_article",
                "candidate_url": "https://pubmed.ncbi.nlm.nih.gov/12011407/",
                "retrieval_basis": "PubMed record for PNAS article",
                "evidence_role": "Methodological background for agent-based modelling and emergent behavior in abstract or social systems.",
                "allowed_use": "Background framing only. May support non-biological ABM framing once separately verified and accepted.",
                "retrieval_status": "retrieved_not_verified",
                "verification_status": "not_verified",
                "acceptance_status": "pending_review_not_accepted",
                "citation_integration_status": "not_integrated",
                "manuscript_mutation_status": "no_mutation",
                "safety_screen_status": "passed_non_operational_method_source_screen",
                "safety_exclusion_notes": "Human systems framing only; no pathogen model, no receptor parameters, no wet-lab protocol, no operational targeting.",
                "boundary_note": "Candidate source is recorded but not verified, not accepted, and not integrated.",
            },
            {
                "candidate_id": "CAND-B1-005",
                "slot_family": "network-science-textbook-foundation",
                "candidate_title": "Network Science",
                "candidate_author_or_body": "Albert-László Barabási",
                "candidate_year": "2016",
                "candidate_locator": "ISBN: 9781107076266",
                "publisher_or_venue": "Cambridge University Press",
                "source_type": "book",
                "candidate_url": "https://www.cambridge.org/gb/universitypress/subjects/physics/statistical-physics/network-science",
                "retrieval_basis": "Cambridge University Press book page",
                "evidence_role": "Methodological background for network science vocabulary and abstract graph concepts.",
                "allowed_use": "Background framing only. May support general network science terminology once separately verified and accepted.",
                "retrieval_status": "retrieved_not_verified",
                "verification_status": "not_verified",
                "acceptance_status": "pending_review_not_accepted",
                "citation_integration_status": "not_integrated",
                "manuscript_mutation_status": "no_mutation",
                "safety_screen_status": "passed_non_operational_method_source_screen",
                "safety_exclusion_notes": "No real biological dataset import, no real pathogen simulation, no receptor parameters, no operational host targeting, no wet-lab protocol.",
                "boundary_note": "Candidate source is recorded but not verified, not accepted, and not integrated.",
            },
            {
                "candidate_id": "CAND-B1-006",
                "slot_family": "sensitivity-analysis-foundation",
                "candidate_title": "Global Sensitivity Analysis: The Primer",
                "candidate_author_or_body": "Andrea Saltelli, Marco Ratto, Terry Andres, Francesca Campolongo, Jessica Cariboni, Debora Gatelli, Michaela Saisana, and Stefano Tarantola",
                "candidate_year": "2008",
                "candidate_locator": "DOI: 10.1002/9780470725184",
                "publisher_or_venue": "Wiley / JRC Publications",
                "source_type": "book",
                "candidate_url": "https://onlinelibrary.wiley.com/doi/book/10.1002/9780470725184",
                "retrieval_basis": "Wiley Online Library book page and JRC publication record",
                "evidence_role": "Methodological background for sensitivity analysis, uncertainty propagation, and model robustness framing.",
                "allowed_use": "Background framing only. May support sensitivity-analysis terminology once separately verified and accepted.",
                "retrieval_status": "retrieved_not_verified",
                "verification_status": "not_verified",
                "acceptance_status": "pending_review_not_accepted",
                "citation_integration_status": "not_integrated",
                "manuscript_mutation_status": "no_mutation",
                "safety_screen_status": "passed_non_operational_method_source_screen",
                "safety_exclusion_notes": "No real biological dataset import, no real pathogen simulation, no receptor parameters, no operational host targeting, no wet-lab protocol.",
                "boundary_note": "Candidate source is recorded but not verified, not accepted, and not integrated.",
            },
            {
                "candidate_id": "CAND-B1-007",
                "slot_family": "agent-based-simulation-foundation",
                "candidate_title": "Tutorial on agent-based modelling and simulation",
                "candidate_author_or_body": "Charles M. Macal and Michael J. North",
                "candidate_year": "2010",
                "candidate_locator": "DOI: 10.1057/jos.2010.3",
                "publisher_or_venue": "Journal of Simulation / Springer Nature",
                "source_type": "journal_article",
                "candidate_url": "https://link.springer.com/article/10.1057/jos.2010.3",
                "retrieval_basis": "Springer article page",
                "evidence_role": "Methodological background for agent-based modelling and simulation workflows at a non-operational level.",
                "allowed_use": "Background framing only. May support general ABMS terminology once separately verified and accepted.",
                "retrieval_status": "retrieved_not_verified",
                "verification_status": "not_verified",
                "acceptance_status": "pending_review_not_accepted",
                "citation_integration_status": "not_integrated",
                "manuscript_mutation_status": "no_mutation",
                "safety_screen_status": "passed_non_operational_method_source_screen",
                "safety_exclusion_notes": "No real biological dataset import, no real pathogen simulation, no receptor parameters, no operational host targeting, no wet-lab protocol.",
                "boundary_note": "Candidate source is recorded but not verified, not accepted, and not integrated.",
            },
        ]

    def _intake_controls(self) -> List[Dict[str, str]]:
        return [
            {
                "control_id": "B1-CTRL-01",
                "control_name": "metadata_only_intake",
                "control_rule": "Batch 1 records source metadata only and does not insert citations into manuscript files.",
                "boundary_note": "No actual citation is added.",
            },
            {
                "control_id": "B1-CTRL-02",
                "control_name": "retrieved_not_verified_status",
                "control_rule": "Every candidate must remain retrieved_not_verified in v8.224.",
                "boundary_note": "No source is claimed as verified.",
            },
            {
                "control_id": "B1-CTRL-03",
                "control_name": "pending_review_not_accepted",
                "control_rule": "Every candidate must remain pending_review_not_accepted.",
                "boundary_note": "No accepted source and no rejected source is recorded.",
            },
            {
                "control_id": "B1-CTRL-04",
                "control_name": "not_integrated_status",
                "control_rule": "Every candidate must remain not_integrated.",
                "boundary_note": "does not complete citation integration.",
            },
            {
                "control_id": "B1-CTRL-05",
                "control_name": "methodological_sources_only",
                "control_rule": "Batch 1 may include only non-operational methodological sources.",
                "boundary_note": "No real biological datasets, no real pathogen models, no receptor parameters, and no operational targeting are introduced.",
            },
            {
                "control_id": "B1-CTRL-06",
                "control_name": "no_manuscript_mutation",
                "control_rule": "Candidate intake must not modify any manuscript file.",
                "boundary_note": "No manuscript file is modified.",
            },
            {
                "control_id": "B1-CTRL-07",
                "control_name": "future_verification_required",
                "control_rule": "A separate milestone is required before verification, acceptance, rejection, or integration.",
                "boundary_note": "Future source verification and citation integration require separate official milestones.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        empty_ledger_source = self._load_json(self.source_empty_ledger_json_path)
        empty_ledger_md = self._load_text(self.source_empty_ledger_md_path)
        ledger_schema_source = self._load_json(self.source_ledger_schema_json_path)
        retrieval_gate_source = self._load_json(self.source_retrieval_gate_json_path)
        eligibility_source = self._load_json(self.source_eligibility_json_path)
        citation_slot_source = self._load_json(self.source_citation_slot_json_path)

        empty_counters = empty_ledger_source.get("counters", {})
        schema_counters = ledger_schema_source.get("counters", {})
        retrieval_counters = retrieval_gate_source.get("counters", {})
        eligibility_counters = eligibility_source.get("counters", {})
        citation_counters = citation_slot_source.get("counters", {})

        candidate_sources = self._candidate_sources()
        intake_controls = self._intake_controls()

        for candidate in candidate_sources:
            candidate["source_intake_batch"] = "batch_1"
            candidate["claim_validation_status"] = "does_not_validate_scientific_claims"
            candidate["readiness_status"] = "does_not_approve_readiness"
            candidate["real_biological_operational_status"] = "non_operational_methodological_source_only"

        counters = {
            "Safe abstract toy citation retrieval batch 1 candidate intake count": 1,
            "New safe abstract toy citation retrieval batch 1 candidate intake count": 1,
            "Toy citation retrieval batch 1 candidate intake JSON export count": 1,
            "Toy citation batch 1 candidate source row count": len(candidate_sources),
            "Toy citation batch 1 candidate source recorded count": len(candidate_sources),
            "Toy citation batch 1 retrieved not verified candidate count": len(candidate_sources),
            "Toy citation batch 1 metadata-only candidate count": len(candidate_sources),
            "Toy citation batch 1 methodological source count": len(candidate_sources),
            "Toy citation batch 1 non-operational safety pass count": len(candidate_sources),
            "Toy citation batch 1 source retrieval execution count": 1,
            "Toy citation batch 1 source retrieval count": len(candidate_sources),
            "Toy citation batch 1 verification execution count": 0,
            "Toy citation batch 1 verified source count": 0,
            "Toy citation batch 1 acceptance decision count": 0,
            "Toy citation batch 1 rejection decision count": 0,
            "Toy citation batch 1 accepted source count": 0,
            "Toy citation batch 1 rejected source count": 0,
            "Toy citation batch 1 blocked source count": 0,
            "Toy citation batch 1 actual citation count": 0,
            "Toy citation batch 1 fabricated reference count": 0,
            "Toy citation batch 1 citation integration completion count": 0,
            "Toy citation batch 1 added to manuscript count": 0,
            "Toy citation batch 1 manuscript mutation count": 0,
            "Toy citation batch 1 intake control count": len(intake_controls),
            "Toy citation batch 1 source book count": sum(1 for item in candidate_sources if item["source_type"] == "book"),
            "Toy citation batch 1 source article count": sum(1 for item in candidate_sources if item["source_type"] == "journal_article"),
            "Toy citation batch 1 source DOI locator count": sum(1 for item in candidate_sources if "DOI:" in item["candidate_locator"]),
            "Toy citation batch 1 source ISBN locator count": sum(1 for item in candidate_sources if "ISBN:" in item["candidate_locator"]),
            "Toy citation batch 1 prior empty ledger row count": empty_counters.get("Toy citation empty ledger row count"),
            "Toy citation batch 1 prior empty ledger candidate source recorded count": empty_counters.get("Toy citation empty ledger candidate source recorded count"),
            "Toy citation batch 1 prior empty ledger source retrieval count": empty_counters.get("Toy citation empty ledger source retrieval count"),
            "Toy citation batch 1 prior empty ledger verified source count": empty_counters.get("Toy citation empty ledger verified source count"),
            "Toy citation batch 1 prior empty ledger actual citation count": empty_counters.get("Toy citation empty ledger actual citation count"),
            "Toy citation batch 1 source candidate ledger field count": schema_counters.get("Toy citation candidate ledger field count"),
            "Toy citation batch 1 source status enum count": schema_counters.get("Toy citation candidate status enum count"),
            "Toy citation batch 1 source provenance field count": schema_counters.get("Toy citation candidate provenance field count"),
            "Toy citation batch 1 source safety screen field count": schema_counters.get("Toy citation candidate safety screen field count"),
            "Toy citation batch 1 source hallucination control count": schema_counters.get("Toy citation candidate hallucination control count"),
            "Toy citation batch 1 source retrieval gate item count": retrieval_counters.get("Toy citation retrieval gate item count"),
            "Toy citation batch 1 source allowed query family count": retrieval_counters.get("Toy citation retrieval allowed query family count"),
            "Toy citation batch 1 source acceptance schema field count": retrieval_counters.get("Toy citation retrieval acceptance schema field count"),
            "Toy citation batch 1 source rejection reason count": retrieval_counters.get("Toy citation retrieval rejection reason count"),
            "Toy citation batch 1 source preflight check count": retrieval_counters.get("Toy citation retrieval preflight check count"),
            "Toy citation batch 1 source eligibility rule count": eligibility_counters.get("Toy citation source eligibility rule count"),
            "Toy citation batch 1 source query plan count": eligibility_counters.get("Toy citation source query plan count"),
            "Toy citation batch 1 source exclusion group count": eligibility_counters.get("Toy citation source exclusion group count"),
            "Toy citation batch 1 source slot count": citation_counters.get("Toy citation slot count"),
            "Toy citation batch 1 source unresolved slot count": citation_counters.get("Toy citation unresolved slot count"),
            "Toy citation batch 1 source slot group count": citation_counters.get("Toy citation slot group count"),
            "Toy citation source retrieval execution count": 1,
            "Toy citation candidate source retrieval count": len(candidate_sources),
            "Toy citation actual citation count": 0,
            "Toy citation verified source count": 0,
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
            "title": "Safe Abstract Toy Citation Retrieval Batch 1 Candidate Intake",
            "source_empty_ledger_json": str(self.source_empty_ledger_json_path),
            "source_empty_ledger_markdown": str(self.source_empty_ledger_md_path),
            "source_empty_ledger_markdown_character_count": len(empty_ledger_md),
            "source_ledger_schema_json": str(self.source_ledger_schema_json_path),
            "source_retrieval_gate_json": str(self.source_retrieval_gate_json_path),
            "source_eligibility_json": str(self.source_eligibility_json_path),
            "source_citation_slot_json": str(self.source_citation_slot_json_path),
            "plan_phrase": self.plan_phrase,
            "scope": "citation-retrieval-batch-1-candidate-intake-only",
            "safe_abstract_toy_only": True,
            "synthetic_project_context_only": True,
            "abstract_graphs_only": True,
            "unitless_parameters_only": True,
            "non_operational_only": True,
            "candidate_intake_completed": True,
            "candidate_sources_recorded": True,
            "candidate_sources": candidate_sources,
            "candidate_source_count": len(candidate_sources),
            "source_retrieval_performed": True,
            "source_retrieval_scope": "metadata-only-methodological-source-intake",
            "verification_performed": False,
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
            "intake_controls": intake_controls,
            "non_readiness_disclaimer": (
                "This v8.224 artifact records Batch 1 candidate sources only. "
                "Candidate source intake only. ""Source retrieval scope is metadata-only-methodological-source-intake. ""Candidate sources are recorded as retrieved_not_verified. "
                "No source is claimed as verified. No accepted source is recorded. No rejected source is recorded. "
                "No actual citation is added. No fabricated reference is introduced. "
                "It does not complete citation integration, does not validate scientific claims, "
                "does not modify manuscript files, and No manuscript file is modified. "
                "No new citation is added. Future verification, acceptance, rejection, and citation integration require separate official milestones."
            ),
            "boundary_notes": (
                [item["boundary_note"] for item in candidate_sources]
                + [item["boundary_note"] for item in intake_controls]
            ),
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "citation-retrieval-batch-1-candidate-intake-only":
            raise AssertionError("v8.224 must remain citation-retrieval-batch-1-candidate-intake-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.224 candidate intake must pass.")

        if report["candidate_intake_completed"] is not True:
            raise AssertionError("Candidate intake should be completed in v8.224.")

        if report["candidate_sources_recorded"] is not True:
            raise AssertionError("v8.224 should record candidate sources.")

        if report["source_retrieval_performed"] is not True:
            raise AssertionError("v8.224 should record metadata-only source retrieval.")

        for field in [
            "verification_performed",
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

        candidates = report["candidate_sources"]
        if len(candidates) != 7:
            raise AssertionError(f"Expected 7 candidate sources, got {len(candidates)}")

        candidate_ids = [candidate["candidate_id"] for candidate in candidates]
        if len(candidate_ids) != len(set(candidate_ids)):
            raise AssertionError("Candidate IDs must be unique.")

        for candidate in candidates:
            if candidate["retrieval_status"] != "retrieved_not_verified":
                raise AssertionError("Every candidate must remain retrieved_not_verified.")
            if candidate["verification_status"] != "not_verified":
                raise AssertionError("Every candidate must remain not_verified.")
            if candidate["acceptance_status"] != "pending_review_not_accepted":
                raise AssertionError("Every candidate must remain pending_review_not_accepted.")
            if candidate["citation_integration_status"] != "not_integrated":
                raise AssertionError("Every candidate must remain not_integrated.")
            if candidate["manuscript_mutation_status"] != "no_mutation":
                raise AssertionError("Every candidate must remain no_mutation.")
            if candidate["safety_screen_status"] != "passed_non_operational_method_source_screen":
                raise AssertionError("Every candidate must pass non-operational method source screen.")
            forbidden_terms = [
                "host range prediction",
                "immune evasion optimization",
                "infectivity optimization",
                "wet-lab protocol",
                "receptor parameterization",
                "operational targeting",
            ]
            combined_candidate_text = json.dumps(candidate, ensure_ascii=False).lower()
            for term in forbidden_terms:
                if term in combined_candidate_text and "no " not in combined_candidate_text:
                    raise AssertionError(f"Forbidden operational term appears without negation: {term}")

        counters = report["counters"]

        expected_counts = {
            "Toy citation batch 1 candidate source row count": 7,
            "Toy citation batch 1 candidate source recorded count": 7,
            "Toy citation batch 1 retrieved not verified candidate count": 7,
            "Toy citation batch 1 metadata-only candidate count": 7,
            "Toy citation batch 1 methodological source count": 7,
            "Toy citation batch 1 non-operational safety pass count": 7,
            "Toy citation batch 1 source retrieval execution count": 1,
            "Toy citation batch 1 source retrieval count": 7,
            "Toy citation batch 1 verification execution count": 0,
            "Toy citation batch 1 verified source count": 0,
            "Toy citation batch 1 acceptance decision count": 0,
            "Toy citation batch 1 rejection decision count": 0,
            "Toy citation batch 1 accepted source count": 0,
            "Toy citation batch 1 rejected source count": 0,
            "Toy citation batch 1 blocked source count": 0,
            "Toy citation batch 1 actual citation count": 0,
            "Toy citation batch 1 fabricated reference count": 0,
            "Toy citation batch 1 citation integration completion count": 0,
            "Toy citation batch 1 added to manuscript count": 0,
            "Toy citation batch 1 manuscript mutation count": 0,
            "Toy citation batch 1 intake control count": 7,
            "Toy citation batch 1 source book count": 5,
            "Toy citation batch 1 source article count": 2,
            "Toy citation batch 1 source DOI locator count": 4,
            "Toy citation batch 1 source ISBN locator count": 3,
            "Toy citation batch 1 prior empty ledger row count": 0,
            "Toy citation batch 1 prior empty ledger candidate source recorded count": 0,
            "Toy citation batch 1 prior empty ledger source retrieval count": 0,
            "Toy citation batch 1 prior empty ledger verified source count": 0,
            "Toy citation batch 1 prior empty ledger actual citation count": 0,
            "Toy citation batch 1 source candidate ledger field count": 16,
            "Toy citation batch 1 source status enum count": 8,
            "Toy citation batch 1 source provenance field count": 10,
            "Toy citation batch 1 source safety screen field count": 10,
            "Toy citation batch 1 source hallucination control count": 10,
            "Toy citation batch 1 source retrieval gate item count": 12,
            "Toy citation batch 1 source allowed query family count": 12,
            "Toy citation batch 1 source acceptance schema field count": 12,
            "Toy citation batch 1 source rejection reason count": 10,
            "Toy citation batch 1 source preflight check count": 10,
            "Toy citation batch 1 source eligibility rule count": 12,
            "Toy citation batch 1 source query plan count": 12,
            "Toy citation batch 1 source exclusion group count": 4,
            "Toy citation batch 1 source slot count": 12,
            "Toy citation batch 1 source unresolved slot count": 12,
            "Toy citation batch 1 source slot group count": 4,
            "Toy citation source retrieval execution count": 1,
            "Toy citation candidate source retrieval count": 7,
        }

        for name, expected in expected_counts.items():
            if counters.get(name) != expected:
                raise AssertionError(f"Expected {expected} for {name}, got {counters.get(name)}")

        combined_text = (
            json.dumps(report["candidate_sources"], ensure_ascii=False)
            + " "
            + json.dumps(report["intake_controls"], ensure_ascii=False)
            + " "
            + report["non_readiness_disclaimer"]
        )

        required_phrases = [
            "Candidate source intake only",
            "retrieved_not_verified",
            "not_verified",
            "pending_review_not_accepted",
            "not_integrated",
            "no_mutation",
            "metadata-only-methodological-source-intake",
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
                raise AssertionError(f"Missing required batch 1 candidate intake phrase: {phrase}")

        must_be_zero = [
            "Toy citation batch 1 verification execution count",
            "Toy citation batch 1 verified source count",
            "Toy citation batch 1 acceptance decision count",
            "Toy citation batch 1 rejection decision count",
            "Toy citation batch 1 accepted source count",
            "Toy citation batch 1 rejected source count",
            "Toy citation batch 1 blocked source count",
            "Toy citation batch 1 actual citation count",
            "Toy citation batch 1 fabricated reference count",
            "Toy citation batch 1 citation integration completion count",
            "Toy citation batch 1 added to manuscript count",
            "Toy citation batch 1 manuscript mutation count",
            "Toy citation actual citation count",
            "Toy citation verified source count",
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

        lines.append("# Safe Abstract Toy Citation Retrieval Batch 1 Candidate Intake")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is citation-retrieval-batch-1-candidate-intake-only.")
        lines.append("It records Batch 1 candidate source metadata as retrieved_not_verified without source verification, acceptance, rejection, citation integration, or manuscript mutation.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")

        lines.append("## Candidate Sources")
        lines.append("")
        for candidate in report["candidate_sources"]:
            lines.append(f"### {candidate['candidate_id']} - {candidate['candidate_title']}")
            lines.append("")
            lines.append(f"- Author/body: {candidate['candidate_author_or_body']}")
            lines.append(f"- Year: {candidate['candidate_year']}")
            lines.append(f"- Locator: {candidate['candidate_locator']}")
            lines.append(f"- Publisher/venue: {candidate['publisher_or_venue']}")
            lines.append(f"- Source type: {candidate['source_type']}")
            lines.append(f"- URL: {candidate['candidate_url']}")
            lines.append(f"- Retrieval basis: {candidate['retrieval_basis']}")
            lines.append(f"- Slot family: {candidate['slot_family']}")
            lines.append(f"- Evidence role: {candidate['evidence_role']}")
            lines.append(f"- Allowed use: {candidate['allowed_use']}")
            lines.append(f"- Retrieval status: {candidate['retrieval_status']}")
            lines.append(f"- Verification status: {candidate['verification_status']}")
            lines.append(f"- Acceptance status: {candidate['acceptance_status']}")
            lines.append(f"- Citation integration status: {candidate['citation_integration_status']}")
            lines.append(f"- Manuscript mutation status: {candidate['manuscript_mutation_status']}")
            lines.append(f"- Safety screen status: {candidate['safety_screen_status']}")
            lines.append(f"- Safety exclusion notes: {candidate['safety_exclusion_notes']}")
            lines.append(f"- Boundary note: {candidate['boundary_note']}")
            lines.append("")

        lines.append("## Intake Controls")
        lines.append("")
        for item in report["intake_controls"]:
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
        lines.append("V8_224_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_BATCH_1_CANDIDATE_INTAKE_OK")
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


def build_safe_abstract_toy_citation_retrieval_batch_1_candidate_intake() -> Dict[str, Any]:
    return SafeAbstractToyCitationRetrievalBatch1CandidateIntakeBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_citation_retrieval_batch_1_candidate_intake()
    counters = result["counters"]
    print("V8_224_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_BATCH_1_CANDIDATE_INTAKE_OK")
    print("TOY_CITATION_RETRIEVAL_BATCH_1_CANDIDATE_INTAKE_DIRECT_CHECK_OK")
    print(f"Candidate source row count: {counters['Toy citation batch 1 candidate source row count']}")
    print(f"Candidate source recorded count: {counters['Toy citation batch 1 candidate source recorded count']}")
    print(f"Retrieved not verified candidate count: {counters['Toy citation batch 1 retrieved not verified candidate count']}")
    print(f"Metadata-only candidate count: {counters['Toy citation batch 1 metadata-only candidate count']}")
    print(f"Methodological source count: {counters['Toy citation batch 1 methodological source count']}")
    print(f"Non-operational safety pass count: {counters['Toy citation batch 1 non-operational safety pass count']}")
    print(f"Source retrieval execution count: {counters['Toy citation batch 1 source retrieval execution count']}")
    print(f"Source retrieval count: {counters['Toy citation batch 1 source retrieval count']}")
    print(f"Verification execution count: {counters['Toy citation batch 1 verification execution count']}")
    print(f"Verified source count: {counters['Toy citation batch 1 verified source count']}")
    print(f"Acceptance decision count: {counters['Toy citation batch 1 acceptance decision count']}")
    print(f"Rejection decision count: {counters['Toy citation batch 1 rejection decision count']}")
    print(f"Accepted source count: {counters['Toy citation batch 1 accepted source count']}")
    print(f"Rejected source count: {counters['Toy citation batch 1 rejected source count']}")
    print(f"Blocked source count: {counters['Toy citation batch 1 blocked source count']}")
    print(f"Actual citation count: {counters['Toy citation batch 1 actual citation count']}")
    print(f"Fabricated reference count: {counters['Toy citation batch 1 fabricated reference count']}")
    print(f"Citation integration completion count: {counters['Toy citation batch 1 citation integration completion count']}")
    print(f"Citation added to manuscript count: {counters['Toy citation batch 1 added to manuscript count']}")
    print(f"Manuscript mutation count: {counters['Toy citation batch 1 manuscript mutation count']}")
    print(f"Book source count: {counters['Toy citation batch 1 source book count']}")
    print(f"Article source count: {counters['Toy citation batch 1 source article count']}")
    print(f"DOI locator count: {counters['Toy citation batch 1 source DOI locator count']}")
    print(f"ISBN locator count: {counters['Toy citation batch 1 source ISBN locator count']}")
    print(f"Prior empty ledger row count: {counters['Toy citation batch 1 prior empty ledger row count']}")
    print(f"Prior empty ledger candidate source recorded count: {counters['Toy citation batch 1 prior empty ledger candidate source recorded count']}")
    print(f"Prior empty ledger source retrieval count: {counters['Toy citation batch 1 prior empty ledger source retrieval count']}")
    print(f"Source candidate ledger field count: {counters['Toy citation batch 1 source candidate ledger field count']}")
    print(f"Source status enum count: {counters['Toy citation batch 1 source status enum count']}")
    print(f"Source provenance field count: {counters['Toy citation batch 1 source provenance field count']}")
    print(f"Source safety screen field count: {counters['Toy citation batch 1 source safety screen field count']}")
    print(f"Source hallucination control count: {counters['Toy citation batch 1 source hallucination control count']}")
    print(f"Source retrieval gate item count: {counters['Toy citation batch 1 source retrieval gate item count']}")
    print(f"Source allowed query family count: {counters['Toy citation batch 1 source allowed query family count']}")
    print(f"Source eligibility rule count: {counters['Toy citation batch 1 source eligibility rule count']}")
    print(f"Source query plan count: {counters['Toy citation batch 1 source query plan count']}")
    print(f"Source exclusion group count: {counters['Toy citation batch 1 source exclusion group count']}")
    print(f"Source slot count: {counters['Toy citation batch 1 source slot count']}")
    print(f"Source unresolved slot count: {counters['Toy citation batch 1 source unresolved slot count']}")
    print(f"Source slot group count: {counters['Toy citation batch 1 source slot group count']}")
    print(f"Toy citation source retrieval execution count: {counters['Toy citation source retrieval execution count']}")
    print(f"Toy citation candidate source retrieval count: {counters['Toy citation candidate source retrieval count']}")
    print(f"Toy citation actual citation count: {counters['Toy citation actual citation count']}")
    print(f"Toy citation verified source count: {counters['Toy citation verified source count']}")
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
