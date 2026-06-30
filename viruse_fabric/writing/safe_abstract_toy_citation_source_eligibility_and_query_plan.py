from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyCitationSourceEligibilityAndQueryPlanBuilder:
    version = "v8.220"

    source_citation_slot_json_path = Path("outputs/safe_abstract_toy_citation_slot_integration_plan_v8_219.json")
    source_citation_slot_md_path = Path("outputs/safe_abstract_toy_citation_slot_integration_plan_v8_219.md")
    source_coherence_json_path = Path("outputs/safe_abstract_toy_manuscript_coherence_improvement_package_v8_218.json")
    source_eval_json_path = Path("outputs/safe_abstract_toy_evaluation_design_plan_v8_217.json")
    source_gap_json_path = Path("outputs/safe_abstract_toy_scientific_gap_and_evidence_upgrade_register_v8_216.json")
    source_assembly_json_path = Path("outputs/safe_abstract_toy_manuscript_assembly_preview_package_v8_215.json")

    output_md_path = Path("outputs/safe_abstract_toy_citation_source_eligibility_and_query_plan_v8_220.md")
    output_json_path = Path("outputs/safe_abstract_toy_citation_source_eligibility_and_query_plan_v8_220.json")

    plan_phrase = "citation_source_eligibility_and_queries_planned_but_no_source_retrieval_performed"

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

    def _eligibility_rules(self) -> List[Dict[str, str]]:
        return [
            {
                "rule_id": "ELIG-01",
                "slot_id": "CIT-SLOT-01",
                "manuscript_area": "Abstract",
                "eligible_source_profile": "Peer-reviewed conceptual or methodological source on governance pipelines, claim control, research workflow governance, or safety-bounded reporting.",
                "minimum_acceptance_rule": "A future source must directly support governance-pipeline positioning without implying biological validation or submission readiness.",
                "exclusion_rule": "Exclude editorials without method relevance, unverifiable webpages, fabricated references, and sources that imply real-biological operational capability.",
                "status": "planned eligibility rule only",
                "boundary_note": "No source retrieval is performed and No actual citation is added.",
            },
            {
                "rule_id": "ELIG-02",
                "slot_id": "CIT-SLOT-02",
                "manuscript_area": "Introduction",
                "eligible_source_profile": "Peer-reviewed source on overclaiming, research integrity, reporting discipline, reproducibility language, or evidence-boundary management.",
                "minimum_acceptance_rule": "A future source must help justify why proposal, draft, evidence, validation, and readiness language should remain separated.",
                "exclusion_rule": "Exclude sources that only discuss generic writing advice without evidence-boundary or integrity relevance.",
                "status": "planned eligibility rule only",
                "boundary_note": "No source is claimed as verified.",
            },
            {
                "rule_id": "ELIG-03",
                "slot_id": "CIT-SLOT-03",
                "manuscript_area": "Method Scope",
                "eligible_source_profile": "Methodological source on toy models, abstract models, simulation boundaries, non-operational evaluation design, or scope-limited research artifacts.",
                "minimum_acceptance_rule": "A future source must support the legitimacy of synthetic, abstract, unitless, non-operational toy-only scoping.",
                "exclusion_rule": "Exclude real biological datasets, real pathogen models, receptor-parameter sources, and operational targeting sources.",
                "status": "planned eligibility rule only",
                "boundary_note": "No real biological datasets, no real pathogen models, no receptor parameters, and no operational targeting are introduced.",
            },
            {
                "rule_id": "ELIG-04",
                "slot_id": "CIT-SLOT-04",
                "manuscript_area": "Pipeline Overview",
                "eligible_source_profile": "Source on staged workflows, artifact lineage, traceability, software process governance, or reproducible artifact tracking.",
                "minimum_acceptance_rule": "A future source must support staged artifact lineage or traceability without converting lineage into validation.",
                "exclusion_rule": "Exclude sources that claim artifact lineage alone proves correctness, safety, performance, or readiness.",
                "status": "planned eligibility rule only",
                "boundary_note": "Lineage support remains a citation need, not evidence completion.",
            },
            {
                "rule_id": "ELIG-05",
                "slot_id": "CIT-SLOT-05",
                "manuscript_area": "Safety Controls",
                "eligible_source_profile": "Source on safety cases, assurance arguments, invariant checking, governance controls, or zero-counter style control checks.",
                "minimum_acceptance_rule": "A future source must support the use of explicit invariants or assurance-style control logic.",
                "exclusion_rule": "Exclude sources that would allow zero counters to be described as proof, external validation, or readiness approval.",
                "status": "planned eligibility rule only",
                "boundary_note": "Zero counters are governance controls only.",
            },
            {
                "rule_id": "ELIG-06",
                "slot_id": "CIT-SLOT-06",
                "manuscript_area": "Claim Governance",
                "eligible_source_profile": "Source on evidence grading, claim classification, responsible reporting, validation language, or research integrity.",
                "minimum_acceptance_rule": "A future source must support the separation of allowed, deferred, and prohibited claims.",
                "exclusion_rule": "Exclude sources that collapse deferred claims into completed claims or turn prohibited claims into promises.",
                "status": "planned eligibility rule only",
                "boundary_note": "Deferred claims remain deferred and prohibited claims remain prohibited.",
            },
            {
                "rule_id": "ELIG-07",
                "slot_id": "CIT-SLOT-07",
                "manuscript_area": "Scientific Gap Register",
                "eligible_source_profile": "Source on evidence mapping, gap registers, validation planning, roadmap discipline, or transparent limitation tracking.",
                "minimum_acceptance_rule": "A future source must support gap mapping or evidence-roadmap framing without implying gap closure.",
                "exclusion_rule": "Exclude sources used to claim that citation integration, proof, validation, or readiness is already complete.",
                "status": "planned eligibility rule only",
                "boundary_note": "No evidence upgrade is completed.",
            },
            {
                "rule_id": "ELIG-08",
                "slot_id": "CIT-SLOT-08",
                "manuscript_area": "Evaluation Design",
                "eligible_source_profile": "Source on evaluation design, toy metrics, traceability metrics, reproducibility checks, or planned non-operational evaluation.",
                "minimum_acceptance_rule": "A future source must support evaluation design or metric planning without reporting results.",
                "exclusion_rule": "Exclude sources that would be used to imply executed evaluation, performance, scores, or validation outcomes.",
                "status": "planned eligibility rule only",
                "boundary_note": "Toy evaluation is designed but not executed.",
            },
            {
                "rule_id": "ELIG-09",
                "slot_id": "CIT-SLOT-09",
                "manuscript_area": "Coherence Improvement",
                "eligible_source_profile": "Source on scientific writing structure, argumentation, reviewer-facing narrative, coherence, transparent limitation framing, or future-work sequencing.",
                "minimum_acceptance_rule": "A future source must support narrative coherence or limitation framing without authorizing manuscript mutation.",
                "exclusion_rule": "Exclude sources that would be used as permission to apply a rewrite in this milestone.",
                "status": "planned eligibility rule only",
                "boundary_note": "No manuscript file is modified.",
            },
            {
                "rule_id": "ELIG-10",
                "slot_id": "CIT-SLOT-10",
                "manuscript_area": "Limitations",
                "eligible_source_profile": "Source on limitation transparency, validation boundaries, non-readiness statements, or responsible evidence restraint.",
                "minimum_acceptance_rule": "A future source must support transparent non-readiness and non-validation language.",
                "exclusion_rule": "Exclude sources that soften or remove non-readiness, non-validation, non-proof, or non-evidence statements.",
                "status": "planned eligibility rule only",
                "boundary_note": "Manuscript submission ready count remains zero.",
            },
            {
                "rule_id": "ELIG-11",
                "slot_id": "CIT-SLOT-11",
                "manuscript_area": "Safety Exclusions",
                "eligible_source_profile": "Source on safe research boundaries, dual-use risk management, non-operational research framing, or safety exclusion language.",
                "minimum_acceptance_rule": "A future source must support the need for explicit exclusions without introducing operational content.",
                "exclusion_rule": "Exclude sources containing wet-lab protocols, actionable biosafety-risk instructions, real-world infectivity optimization, immune evasion optimization, or host range prediction.",
                "status": "planned eligibility rule only",
                "boundary_note": "Wet-lab protocol count and actionable biosafety-risk instruction count remain zero.",
            },
            {
                "rule_id": "ELIG-12",
                "slot_id": "CIT-SLOT-12",
                "manuscript_area": "Future Work",
                "eligible_source_profile": "Source on staged validation, responsible claim escalation, reproducible artifact packages, or roadmap discipline.",
                "minimum_acceptance_rule": "A future source must support sequencing of future work without implying future work has already occurred.",
                "exclusion_rule": "Exclude sources used to imply citation integration, evaluation execution, readiness, proof, or validation has already happened.",
                "status": "planned eligibility rule only",
                "boundary_note": "Future work may only introduce stronger claims after separately audited milestones.",
            },
        ]

    def _query_plans(self) -> List[Dict[str, str]]:
        return [
            {
                "query_id": "QUERY-01",
                "slot_id": "CIT-SLOT-01",
                "query_family": "Governance pipeline positioning",
                "planned_query_template": "research workflow governance claim control safety bounded reporting methodological pipeline",
                "execution_status": "not_executed",
                "boundary_note": "Query plans are planned search instructions only.",
            },
            {
                "query_id": "QUERY-02",
                "slot_id": "CIT-SLOT-02",
                "query_family": "Overclaim drift and reporting discipline",
                "planned_query_template": "scientific overclaiming research integrity reporting discipline evidence boundary language",
                "execution_status": "not_executed",
                "boundary_note": "No source retrieval is performed.",
            },
            {
                "query_id": "QUERY-03",
                "slot_id": "CIT-SLOT-03",
                "query_family": "Synthetic abstract toy scope",
                "planned_query_template": "toy model abstraction non operational simulation boundary methodological scope",
                "execution_status": "not_executed",
                "boundary_note": "No real biological datasets are searched, imported, or used.",
            },
            {
                "query_id": "QUERY-04",
                "slot_id": "CIT-SLOT-04",
                "query_family": "Staged artifact lineage",
                "planned_query_template": "artifact lineage traceability staged workflow reproducible research artifact tracking",
                "execution_status": "not_executed",
                "boundary_note": "No proof or validation result is produced.",
            },
            {
                "query_id": "QUERY-05",
                "slot_id": "CIT-SLOT-05",
                "query_family": "Zero-counter governance invariants",
                "planned_query_template": "invariant checking safety case assurance argument governance control software process",
                "execution_status": "not_executed",
                "boundary_note": "No readiness approval is produced.",
            },
            {
                "query_id": "QUERY-06",
                "slot_id": "CIT-SLOT-06",
                "query_family": "Allowed deferred prohibited claim classification",
                "planned_query_template": "claim classification evidence grading responsible reporting validation language deferred claims",
                "execution_status": "not_executed",
                "boundary_note": "No deferred claim is upgraded.",
            },
            {
                "query_id": "QUERY-07",
                "slot_id": "CIT-SLOT-07",
                "query_family": "Evidence gap register and roadmap",
                "planned_query_template": "evidence gap register validation roadmap limitation tracking responsible research planning",
                "execution_status": "not_executed",
                "boundary_note": "No evidence upgrade is completed.",
            },
            {
                "query_id": "QUERY-08",
                "slot_id": "CIT-SLOT-08",
                "query_family": "Toy evaluation design and metrics",
                "planned_query_template": "evaluation design toy metrics traceability metrics reproducibility checks non operational evaluation",
                "execution_status": "not_executed",
                "boundary_note": "No evaluation is executed and no results are reported.",
            },
            {
                "query_id": "QUERY-09",
                "slot_id": "CIT-SLOT-09",
                "query_family": "Manuscript coherence and limitation framing",
                "planned_query_template": "scientific writing coherence argumentation limitation framing reviewer narrative future work sequence",
                "execution_status": "not_executed",
                "boundary_note": "No manuscript file is modified.",
            },
            {
                "query_id": "QUERY-10",
                "slot_id": "CIT-SLOT-10",
                "query_family": "Limitation transparency and non-readiness",
                "planned_query_template": "transparent limitations validation boundary non readiness responsible evidence restraint",
                "execution_status": "not_executed",
                "boundary_note": "No submission readiness claim is made.",
            },
            {
                "query_id": "QUERY-11",
                "slot_id": "CIT-SLOT-11",
                "query_family": "Safety exclusions and non-operational boundary",
                "planned_query_template": "dual use risk management non operational research safety boundary exclusion language",
                "execution_status": "not_executed",
                "boundary_note": "No wet-lab protocol or actionable biosafety-risk instruction is introduced.",
            },
            {
                "query_id": "QUERY-12",
                "slot_id": "CIT-SLOT-12",
                "query_family": "Staged future work and claim escalation",
                "planned_query_template": "staged validation responsible claim escalation reproducible artifact package roadmap discipline",
                "execution_status": "not_executed",
                "boundary_note": "Future source retrieval requires a separate official milestone.",
            },
        ]

    def _exclusion_groups(self) -> List[Dict[str, str]]:
        return [
            {
                "group_id": "EXCL-01",
                "group_name": "No fabricated or unverifiable references",
                "excluded_material": "Fabricated references, unverifiable claims, imaginary DOI records, unsourced source claims, and unreviewed placeholder references.",
                "boundary_note": "No fabricated reference is introduced and No source is claimed as verified.",
            },
            {
                "group_id": "EXCL-02",
                "group_name": "No citation integration or manuscript mutation",
                "excluded_material": "Actual citation insertion, citation integration completion, source retrieval execution, manuscript rewrite application, and manuscript file mutation.",
                "boundary_note": "No new citation is added and No manuscript file is modified.",
            },
            {
                "group_id": "EXCL-03",
                "group_name": "No validation, readiness, proof, or evidence upgrade",
                "excluded_material": "Validation claims, readiness approval, proof assistant verification, independent experiment claims, external validation, and evidence upgrade completion.",
                "boundary_note": "does not complete citation integration and does not validate scientific claims.",
            },
            {
                "group_id": "EXCL-04",
                "group_name": "No real-biological operational content",
                "excluded_material": "Real biological datasets, real pathogen simulation, receptor parameters, operational targeting, wet-lab protocols, actionable biosafety-risk instructions, real-world infectivity optimization, immune evasion optimization, and host range prediction.",
                "boundary_note": "No real biological datasets, no real pathogen models, no receptor parameters, and no operational targeting are introduced.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        citation_slot_source = self._load_json(self.source_citation_slot_json_path)
        citation_slot_md = self._load_text(self.source_citation_slot_md_path)
        coherence_source = self._load_json(self.source_coherence_json_path)
        eval_source = self._load_json(self.source_eval_json_path)
        gap_source = self._load_json(self.source_gap_json_path)
        assembly_source = self._load_json(self.source_assembly_json_path)

        citation_counters = citation_slot_source.get("counters", {})
        coherence_counters = coherence_source.get("counters", {})
        eval_counters = eval_source.get("counters", {})
        gap_counters = gap_source.get("counters", {})
        assembly_counters = assembly_source.get("counters", {})

        eligibility_rules = self._eligibility_rules()
        query_plans = self._query_plans()
        exclusion_groups = self._exclusion_groups()

        counters = {
            "Safe abstract toy citation source eligibility and query plan count": 1,
            "New safe abstract toy citation source eligibility and query plan count": 1,
            "Toy citation source eligibility and query plan JSON export count": 1,
            "Toy citation source eligibility rule count": len(eligibility_rules),
            "Toy citation source query plan count": len(query_plans),
            "Toy citation source exclusion group count": len(exclusion_groups),
            "Toy citation source retrieval count": 0,
            "Toy citation source verified source count": 0,
            "Toy citation source accepted source count": 0,
            "Toy citation source rejected source count": 0,
            "Toy citation source actual citation count": 0,
            "Toy citation source fabricated reference count": 0,
            "Toy citation source integration completion count": 0,
            "Toy citation source added to manuscript count": 0,
            "Toy citation source source slot count": citation_counters.get("Toy citation slot count"),
            "Toy citation source unresolved slot count": citation_counters.get("Toy citation unresolved slot count"),
            "Toy citation source slot group count": citation_counters.get("Toy citation slot group count"),
            "Toy citation source prior actual citation count": citation_counters.get("Toy citation actual citation count"),
            "Toy citation source prior verified source count": citation_counters.get("Toy citation verified source count"),
            "Toy citation source prior fabricated reference count": citation_counters.get("Toy citation fabricated reference count"),
            "Toy citation source prior source retrieval count": citation_counters.get("Toy citation source retrieval count"),
            "Toy citation source prior integration completion count": citation_counters.get("Toy citation integration completion count"),
            "Toy citation source prior citation added to manuscript count": citation_counters.get("Toy citation added to manuscript count"),
            "Toy citation source source assembly section count": assembly_counters.get("Toy manuscript assembly preview section count"),
            "Toy citation source source gap item count": gap_counters.get("Toy scientific gap register item count"),
            "Toy citation source source P0 gap count": gap_counters.get("Toy scientific gap P0 count"),
            "Toy citation source source evidence upgrade completed count": gap_counters.get("Toy scientific evidence upgrade completed count"),
            "Toy citation source source evaluation design module count": eval_counters.get("Toy evaluation design module count"),
            "Toy citation source source actual evaluation run count": eval_counters.get("Toy evaluation actual run count"),
            "Toy citation source source validation claim count": eval_counters.get("Toy evaluation validation claim count"),
            "Toy citation source source coherence improvement item count": coherence_counters.get("Toy manuscript coherence improvement item count"),
            "Toy citation source source coherence rewrite application count": coherence_counters.get("Toy manuscript coherence rewrite application count"),
            "Toy citation source eligibility plan execution count": 1,
            "Toy citation source eligibility plan direct execution count": 1,
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
            "title": "Safe Abstract Toy Citation Source Eligibility and Query Plan",
            "source_citation_slot_json": str(self.source_citation_slot_json_path),
            "source_citation_slot_markdown": str(self.source_citation_slot_md_path),
            "source_citation_slot_markdown_character_count": len(citation_slot_md),
            "source_coherence_json": str(self.source_coherence_json_path),
            "source_evaluation_design_json": str(self.source_eval_json_path),
            "source_gap_json": str(self.source_gap_json_path),
            "source_assembly_json": str(self.source_assembly_json_path),
            "plan_phrase": self.plan_phrase,
            "scope": "citation-source-eligibility-and-query-plan-only",
            "safe_abstract_toy_only": True,
            "synthetic_only": True,
            "abstract_graphs_only": True,
            "unitless_parameters_only": True,
            "non_operational_only": True,
            "citation_source_eligibility_plan_completed": True,
            "query_plan_completed": True,
            "source_retrieval_performed": False,
            "verified_sources_claimed": False,
            "accepted_sources_recorded": False,
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
                "This v8.220 artifact creates a citation source eligibility and query plan only. "
                "No source retrieval is performed. No actual citation is added. No fabricated reference is introduced. "
                "No source is claimed as verified. It does not complete citation integration, does not validate scientific claims, "
                "does not modify manuscript files, and No manuscript file is modified. No new citation is added. "
                "Future source retrieval requires a separate official milestone."
            ),
            "eligibility_rules": eligibility_rules,
            "query_plans": query_plans,
            "exclusion_groups": exclusion_groups,
            "boundary_notes": [item["boundary_note"] for item in eligibility_rules] + [item["boundary_note"] for item in exclusion_groups],
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "citation-source-eligibility-and-query-plan-only":
            raise AssertionError("v8.220 must remain citation-source-eligibility-and-query-plan-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.220 citation source eligibility and query plan must pass.")

        if report["citation_source_eligibility_plan_completed"] is not True:
            raise AssertionError("v8.220 should complete only the eligibility plan.")

        if report["query_plan_completed"] is not True:
            raise AssertionError("v8.220 should complete only the query plan.")

        for field in [
            "source_retrieval_performed",
            "verified_sources_claimed",
            "accepted_sources_recorded",
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
            "Toy citation source eligibility rule count": 12,
            "Toy citation source query plan count": 12,
            "Toy citation source exclusion group count": 4,
            "Toy citation source retrieval count": 0,
            "Toy citation source verified source count": 0,
            "Toy citation source accepted source count": 0,
            "Toy citation source rejected source count": 0,
            "Toy citation source actual citation count": 0,
            "Toy citation source fabricated reference count": 0,
            "Toy citation source integration completion count": 0,
            "Toy citation source added to manuscript count": 0,
            "Toy citation source source slot count": 12,
            "Toy citation source unresolved slot count": 12,
            "Toy citation source slot group count": 4,
            "Toy citation source prior actual citation count": 0,
            "Toy citation source prior verified source count": 0,
            "Toy citation source prior fabricated reference count": 0,
            "Toy citation source prior source retrieval count": 0,
            "Toy citation source prior integration completion count": 0,
            "Toy citation source prior citation added to manuscript count": 0,
            "Toy citation source source assembly section count": 9,
            "Toy citation source source gap item count": 12,
            "Toy citation source source P0 gap count": 6,
            "Toy citation source source evidence upgrade completed count": 0,
            "Toy citation source source evaluation design module count": 10,
            "Toy citation source source actual evaluation run count": 0,
            "Toy citation source source validation claim count": 0,
            "Toy citation source source coherence improvement item count": 10,
            "Toy citation source source coherence rewrite application count": 0,
        }

        for name, expected in expected_counts.items():
            if counters.get(name) != expected:
                raise AssertionError(f"Expected {expected} for {name}, got {counters.get(name)}")

        combined_text = (
            json.dumps(report["eligibility_rules"], ensure_ascii=False)
            + " "
            + json.dumps(report["query_plans"], ensure_ascii=False)
            + " "
            + json.dumps(report["exclusion_groups"], ensure_ascii=False)
            + " "
            + report["non_readiness_disclaimer"]
        )

        required_phrases = [
            "citation source eligibility and query plan",
            "planned eligibility rule only",
            "Query plans are planned search instructions only",
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
            "Future work may only introduce stronger claims",
        ]

        for phrase in required_phrases:
            if phrase not in combined_text:
                raise AssertionError(f"Missing required eligibility/query phrase: {phrase}")

        must_be_zero = [
            "Toy citation source retrieval count",
            "Toy citation source verified source count",
            "Toy citation source accepted source count",
            "Toy citation source rejected source count",
            "Toy citation source actual citation count",
            "Toy citation source fabricated reference count",
            "Toy citation source integration completion count",
            "Toy citation source added to manuscript count",
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

        lines.append("# Safe Abstract Toy Citation Source Eligibility and Query Plan")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is citation-source-eligibility-and-query-plan-only.")
        lines.append("It plans eligibility rules and query templates without source retrieval, source verification, citation insertion, or manuscript mutation.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")
        lines.append("## Eligibility Rules")
        lines.append("")

        for item in report["eligibility_rules"]:
            lines.append(f"### {item['rule_id']} — {item['slot_id']} — {item['manuscript_area']}")
            lines.append("")
            lines.append(f"- Eligible source profile: {item['eligible_source_profile']}")
            lines.append(f"- Minimum acceptance rule: {item['minimum_acceptance_rule']}")
            lines.append(f"- Exclusion rule: {item['exclusion_rule']}")
            lines.append(f"- Status: {item['status']}")
            lines.append(f"- Boundary note: {item['boundary_note']}")
            lines.append("")

        lines.append("## Query Plans")
        lines.append("")

        for item in report["query_plans"]:
            lines.append(f"### {item['query_id']} — {item['slot_id']} — {item['query_family']}")
            lines.append("")
            lines.append(f"- Planned query template: {item['planned_query_template']}")
            lines.append(f"- Execution status: {item['execution_status']}")
            lines.append(f"- Boundary note: {item['boundary_note']}")
            lines.append("")

        lines.append("## Exclusion Groups")
        lines.append("")

        for item in report["exclusion_groups"]:
            lines.append(f"### {item['group_id']} — {item['group_name']}")
            lines.append("")
            lines.append(f"- Excluded material: {item['excluded_material']}")
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
        lines.append("V8_220_SAFE_ABSTRACT_TOY_CITATION_SOURCE_ELIGIBILITY_AND_QUERY_PLAN_OK")
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


def build_safe_abstract_toy_citation_source_eligibility_and_query_plan() -> Dict[str, Any]:
    return SafeAbstractToyCitationSourceEligibilityAndQueryPlanBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_citation_source_eligibility_and_query_plan()
    counters = result["counters"]
    print("V8_220_SAFE_ABSTRACT_TOY_CITATION_SOURCE_ELIGIBILITY_AND_QUERY_PLAN_OK")
    print("TOY_CITATION_SOURCE_ELIGIBILITY_AND_QUERY_PLAN_DIRECT_CHECK_OK")
    print(f"Eligibility rule count: {counters['Toy citation source eligibility rule count']}")
    print(f"Query plan count: {counters['Toy citation source query plan count']}")
    print(f"Exclusion group count: {counters['Toy citation source exclusion group count']}")
    print(f"Source retrieval count: {counters['Toy citation source retrieval count']}")
    print(f"Verified source count: {counters['Toy citation source verified source count']}")
    print(f"Accepted source count: {counters['Toy citation source accepted source count']}")
    print(f"Actual citation count: {counters['Toy citation source actual citation count']}")
    print(f"Fabricated reference count: {counters['Toy citation source fabricated reference count']}")
    print(f"Citation integration completion count: {counters['Toy citation source integration completion count']}")
    print(f"Citation added to manuscript count: {counters['Toy citation source added to manuscript count']}")
    print(f"Source slot count: {counters['Toy citation source source slot count']}")
    print(f"Source unresolved slot count: {counters['Toy citation source unresolved slot count']}")
    print(f"Source slot group count: {counters['Toy citation source slot group count']}")
    print(f"Source assembly section count: {counters['Toy citation source source assembly section count']}")
    print(f"Source gap item count: {counters['Toy citation source source gap item count']}")
    print(f"Source P0 gap count: {counters['Toy citation source source P0 gap count']}")
    print(f"Source evaluation design module count: {counters['Toy citation source source evaluation design module count']}")
    print(f"Source coherence improvement item count: {counters['Toy citation source source coherence improvement item count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {result['passed']}")
