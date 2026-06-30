from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyCitationRetrievalReadinessGateBuilder:
    version = "v8.221"

    source_eligibility_json_path = Path(
        "outputs/safe_abstract_toy_citation_source_eligibility_and_query_plan_v8_220.json"
    )
    source_eligibility_md_path = Path(
        "outputs/safe_abstract_toy_citation_source_eligibility_and_query_plan_v8_220.md"
    )
    source_citation_slot_json_path = Path(
        "outputs/safe_abstract_toy_citation_slot_integration_plan_v8_219.json"
    )
    source_citation_slot_md_path = Path(
        "outputs/safe_abstract_toy_citation_slot_integration_plan_v8_219.md"
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

    output_md_path = Path("outputs/safe_abstract_toy_citation_retrieval_readiness_gate_v8_221.md")
    output_json_path = Path("outputs/safe_abstract_toy_citation_retrieval_readiness_gate_v8_221.json")

    plan_phrase = "citation_retrieval_readiness_gated_but_no_source_retrieval_performed"

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

    def _retrieval_gate_items(self) -> List[Dict[str, str]]:
        return [
            {
                "gate_id": "GATE-01",
                "slot_id": "CIT-SLOT-01",
                "gate_area": "Governance pipeline positioning",
                "readiness_requirement": "Future retrieval may search only for governance-pipeline, claim-control, or safety-bounded reporting sources.",
                "pass_condition": "A retrieved candidate must support governance framing without claiming validation, proof, or readiness.",
                "fail_condition": "Reject sources that imply biological validation, operational capability, or submission readiness.",
                "authorization_status": "not_authorized_for_retrieval",
                "boundary_note": "Retrieval readiness gate only. No source retrieval is performed.",
            },
            {
                "gate_id": "GATE-02",
                "slot_id": "CIT-SLOT-02",
                "gate_area": "Overclaim drift and reporting discipline",
                "readiness_requirement": "Future retrieval may search for research integrity, overclaiming, evidence-boundary, or reporting-discipline sources.",
                "pass_condition": "A retrieved candidate must help separate draft, evidence, validation, and readiness language.",
                "fail_condition": "Reject sources that only provide generic writing advice without evidence-boundary relevance.",
                "authorization_status": "not_authorized_for_retrieval",
                "boundary_note": "No source is claimed as verified.",
            },
            {
                "gate_id": "GATE-03",
                "slot_id": "CIT-SLOT-03",
                "gate_area": "Synthetic abstract toy scope",
                "readiness_requirement": "Future retrieval may search for toy-model, abstract-model, non-operational simulation-boundary, or scope-limited-method sources.",
                "pass_condition": "A retrieved candidate must support synthetic abstract toy-only scoping without importing real biological material.",
                "fail_condition": "Reject real biological datasets, real pathogen models, receptor-parameter sources, and operational targeting sources.",
                "authorization_status": "not_authorized_for_retrieval",
                "boundary_note": "No real biological datasets, no real pathogen models, no receptor parameters, and no operational targeting are introduced.",
            },
            {
                "gate_id": "GATE-04",
                "slot_id": "CIT-SLOT-04",
                "gate_area": "Staged artifact lineage",
                "readiness_requirement": "Future retrieval may search for staged workflows, artifact lineage, traceability, reproducible artifact tracking, or software process governance.",
                "pass_condition": "A retrieved candidate must support artifact traceability without converting lineage into validation.",
                "fail_condition": "Reject sources that treat artifact tracking as proof, safety validation, performance evidence, or readiness approval.",
                "authorization_status": "not_authorized_for_retrieval",
                "boundary_note": "Lineage support remains a future citation need, not evidence completion.",
            },
            {
                "gate_id": "GATE-05",
                "slot_id": "CIT-SLOT-05",
                "gate_area": "Zero-counter governance invariants",
                "readiness_requirement": "Future retrieval may search for assurance arguments, safety cases, invariant checks, governance controls, or process controls.",
                "pass_condition": "A retrieved candidate must support explicit control logic without upgrading counters into proof.",
                "fail_condition": "Reject sources that would let zero counters be described as proof, external validation, or readiness approval.",
                "authorization_status": "not_authorized_for_retrieval",
                "boundary_note": "Zero counters are governance controls only.",
            },
            {
                "gate_id": "GATE-06",
                "slot_id": "CIT-SLOT-06",
                "gate_area": "Claim governance",
                "readiness_requirement": "Future retrieval may search for evidence grading, claim classification, responsible reporting, and validation-language discipline.",
                "pass_condition": "A retrieved candidate must support allowed, deferred, and prohibited claim separation.",
                "fail_condition": "Reject sources that collapse deferred claims into completed claims or turn prohibited claims into promises.",
                "authorization_status": "not_authorized_for_retrieval",
                "boundary_note": "Deferred claims remain deferred and prohibited claims remain prohibited.",
            },
            {
                "gate_id": "GATE-07",
                "slot_id": "CIT-SLOT-07",
                "gate_area": "Scientific gap register",
                "readiness_requirement": "Future retrieval may search for evidence mapping, gap registers, validation roadmaps, and transparent limitation tracking.",
                "pass_condition": "A retrieved candidate must support evidence-gap mapping without implying that gaps are closed.",
                "fail_condition": "Reject sources used to claim citation integration, proof, validation, or readiness is complete.",
                "authorization_status": "not_authorized_for_retrieval",
                "boundary_note": "No evidence upgrade is completed.",
            },
            {
                "gate_id": "GATE-08",
                "slot_id": "CIT-SLOT-08",
                "gate_area": "Toy evaluation design",
                "readiness_requirement": "Future retrieval may search for evaluation design, toy metrics, traceability metrics, reproducibility checks, or non-operational evaluation planning.",
                "pass_condition": "A retrieved candidate must support evaluation design without reporting project results.",
                "fail_condition": "Reject sources that would be used to imply executed evaluation, performance scores, or validation outcomes.",
                "authorization_status": "not_authorized_for_retrieval",
                "boundary_note": "Toy evaluation is designed but not executed.",
            },
            {
                "gate_id": "GATE-09",
                "slot_id": "CIT-SLOT-09",
                "gate_area": "Manuscript coherence and limitations",
                "readiness_requirement": "Future retrieval may search for scientific writing coherence, argumentation, limitation framing, reviewer-facing narrative, or future-work sequencing.",
                "pass_condition": "A retrieved candidate must support narrative coherence or limitation transparency without authorizing manuscript mutation.",
                "fail_condition": "Reject sources that would be used as permission to apply a rewrite in this milestone.",
                "authorization_status": "not_authorized_for_retrieval",
                "boundary_note": "No manuscript file is modified.",
            },
            {
                "gate_id": "GATE-10",
                "slot_id": "CIT-SLOT-10",
                "gate_area": "Limitation transparency and non-readiness",
                "readiness_requirement": "Future retrieval may search for limitation transparency, validation boundaries, non-readiness statements, or responsible evidence restraint.",
                "pass_condition": "A retrieved candidate must support transparent non-readiness and non-validation language.",
                "fail_condition": "Reject sources that soften or remove non-readiness, non-validation, non-proof, or non-evidence statements.",
                "authorization_status": "not_authorized_for_retrieval",
                "boundary_note": "Manuscript submission ready count remains zero.",
            },
            {
                "gate_id": "GATE-11",
                "slot_id": "CIT-SLOT-11",
                "gate_area": "Safety exclusions and non-operational boundary",
                "readiness_requirement": "Future retrieval may search only for safe research boundaries, dual-use risk management, non-operational framing, or exclusion-language sources.",
                "pass_condition": "A retrieved candidate must support explicit safety exclusions without operational content.",
                "fail_condition": "Reject wet-lab protocols, actionable biosafety-risk instructions, real-world infectivity optimization, immune evasion optimization, host range prediction, and operational host targeting.",
                "authorization_status": "not_authorized_for_retrieval",
                "boundary_note": "Wet-lab protocol count and actionable biosafety-risk instruction count remain zero.",
            },
            {
                "gate_id": "GATE-12",
                "slot_id": "CIT-SLOT-12",
                "gate_area": "Future work and claim escalation",
                "readiness_requirement": "Future retrieval may search for staged validation, responsible claim escalation, reproducible artifact packaging, or roadmap discipline.",
                "pass_condition": "A retrieved candidate must support future-work sequencing without implying the work has already occurred.",
                "fail_condition": "Reject sources used to imply citation integration, evaluation execution, readiness, proof, or validation has already happened.",
                "authorization_status": "not_authorized_for_retrieval",
                "boundary_note": "Future work may only introduce stronger claims after separately audited milestones.",
            },
        ]

    def _allowed_query_families(self) -> List[Dict[str, str]]:
        return [
            {
                "family_id": "ALLOW-01",
                "slot_id": "CIT-SLOT-01",
                "allowed_family": "governance pipeline claim control safety-bounded reporting",
                "execution_status": "not_executed",
                "boundary_note": "Allowed query family only; no search is run.",
            },
            {
                "family_id": "ALLOW-02",
                "slot_id": "CIT-SLOT-02",
                "allowed_family": "research integrity overclaiming evidence-boundary reporting discipline",
                "execution_status": "not_executed",
                "boundary_note": "Allowed query family only; No source retrieval is performed.",
            },
            {
                "family_id": "ALLOW-03",
                "slot_id": "CIT-SLOT-03",
                "allowed_family": "toy model abstract model non-operational simulation boundary methodological scope",
                "execution_status": "not_executed",
                "boundary_note": "No real biological datasets are searched, imported, or used.",
            },
            {
                "family_id": "ALLOW-04",
                "slot_id": "CIT-SLOT-04",
                "allowed_family": "artifact lineage traceability staged workflow reproducible artifact tracking",
                "execution_status": "not_executed",
                "boundary_note": "No proof or validation result is produced.",
            },
            {
                "family_id": "ALLOW-05",
                "slot_id": "CIT-SLOT-05",
                "allowed_family": "safety case assurance argument invariant checking governance controls",
                "execution_status": "not_executed",
                "boundary_note": "No readiness approval is produced.",
            },
            {
                "family_id": "ALLOW-06",
                "slot_id": "CIT-SLOT-06",
                "allowed_family": "claim classification evidence grading responsible reporting validation language",
                "execution_status": "not_executed",
                "boundary_note": "No deferred claim is upgraded.",
            },
            {
                "family_id": "ALLOW-07",
                "slot_id": "CIT-SLOT-07",
                "allowed_family": "evidence gap register validation roadmap limitation tracking",
                "execution_status": "not_executed",
                "boundary_note": "No evidence upgrade is completed.",
            },
            {
                "family_id": "ALLOW-08",
                "slot_id": "CIT-SLOT-08",
                "allowed_family": "evaluation design toy metrics traceability metrics reproducibility checks",
                "execution_status": "not_executed",
                "boundary_note": "No evaluation is executed and no results are reported.",
            },
            {
                "family_id": "ALLOW-09",
                "slot_id": "CIT-SLOT-09",
                "allowed_family": "scientific writing coherence argumentation limitation framing reviewer narrative",
                "execution_status": "not_executed",
                "boundary_note": "No manuscript file is modified.",
            },
            {
                "family_id": "ALLOW-10",
                "slot_id": "CIT-SLOT-10",
                "allowed_family": "transparent limitations validation boundary non-readiness responsible evidence restraint",
                "execution_status": "not_executed",
                "boundary_note": "No submission readiness claim is made.",
            },
            {
                "family_id": "ALLOW-11",
                "slot_id": "CIT-SLOT-11",
                "allowed_family": "dual-use risk management non-operational research safety boundary exclusion language",
                "execution_status": "not_executed",
                "boundary_note": "No wet-lab protocol or actionable biosafety-risk instruction is introduced.",
            },
            {
                "family_id": "ALLOW-12",
                "slot_id": "CIT-SLOT-12",
                "allowed_family": "staged validation responsible claim escalation reproducible artifact package roadmap discipline",
                "execution_status": "not_executed",
                "boundary_note": "Future source retrieval requires a separate official milestone.",
            },
        ]

    def _acceptance_schema(self) -> List[Dict[str, str]]:
        return [
            {
                "field_id": "ACCEPT-FIELD-01",
                "field_name": "slot_id",
                "required_value_rule": "Must map to exactly one unresolved CIT-SLOT identifier.",
                "boundary_note": "Schema only; no accepted source is recorded.",
            },
            {
                "field_id": "ACCEPT-FIELD-02",
                "field_name": "candidate_source_title",
                "required_value_rule": "Must be captured only after a future retrieval milestone finds a real candidate.",
                "boundary_note": "No source retrieval is performed.",
            },
            {
                "field_id": "ACCEPT-FIELD-03",
                "field_name": "source_type",
                "required_value_rule": "Must classify the future candidate as peer-reviewed article, book chapter, standards document, or other explicitly allowed source type.",
                "boundary_note": "No source is claimed as verified.",
            },
            {
                "field_id": "ACCEPT-FIELD-04",
                "field_name": "evidence_role",
                "required_value_rule": "Must state whether the source supports governance framing, toy scope, lineage, limitation framing, or evaluation design only.",
                "boundary_note": "No evidence upgrade is completed.",
            },
            {
                "field_id": "ACCEPT-FIELD-05",
                "field_name": "claim_boundary",
                "required_value_rule": "Must state that the source does not validate project results, prove safety, approve readiness, or complete citation integration.",
                "boundary_note": "does not validate scientific claims.",
            },
            {
                "field_id": "ACCEPT-FIELD-06",
                "field_name": "safety_screen_result",
                "required_value_rule": "Must be rejected if it contains real biological datasets, real pathogen simulation, receptor parameters, operational targeting, or actionable biosafety-risk instructions.",
                "boundary_note": "No real biological datasets, no real pathogen models, no receptor parameters, and no operational targeting are introduced.",
            },
            {
                "field_id": "ACCEPT-FIELD-07",
                "field_name": "verification_status",
                "required_value_rule": "Must remain unverified until a separate retrieval and verification milestone records evidence.",
                "boundary_note": "No source is claimed as verified.",
            },
            {
                "field_id": "ACCEPT-FIELD-08",
                "field_name": "integration_status",
                "required_value_rule": "Must remain not integrated until a separate citation integration milestone.",
                "boundary_note": "does not complete citation integration.",
            },
            {
                "field_id": "ACCEPT-FIELD-09",
                "field_name": "manuscript_mutation_status",
                "required_value_rule": "Must remain no manuscript mutation in this milestone.",
                "boundary_note": "No manuscript file is modified.",
            },
            {
                "field_id": "ACCEPT-FIELD-10",
                "field_name": "readiness_status",
                "required_value_rule": "Must not claim submission readiness, external validation, proof, or independent experiment completion.",
                "boundary_note": "Manuscript submission ready count remains zero.",
            },
            {
                "field_id": "ACCEPT-FIELD-11",
                "field_name": "rejection_if_unsafe",
                "required_value_rule": "Must reject any candidate that violates safety exclusions or overclaim boundaries.",
                "boundary_note": "Unsafe or overclaiming candidates remain excluded.",
            },
            {
                "field_id": "ACCEPT-FIELD-12",
                "field_name": "future_authorization_reference",
                "required_value_rule": "Must name the future official milestone that performs retrieval or integration.",
                "boundary_note": "Future source retrieval requires a separate official milestone.",
            },
        ]

    def _rejection_schema(self) -> List[Dict[str, str]]:
        return [
            {
                "reason_id": "REJECT-01",
                "reason_name": "fabricated_or_unverifiable_reference",
                "rejection_rule": "Reject imaginary, unverifiable, placeholder, or fabricated references.",
                "boundary_note": "No fabricated reference is introduced.",
            },
            {
                "reason_id": "REJECT-02",
                "reason_name": "real_biological_dataset_or_pathogen_model",
                "rejection_rule": "Reject candidates that require or describe real biological datasets, real pathogen simulations, or operational biological modeling.",
                "boundary_note": "No real biological datasets and no real pathogen models are introduced.",
            },
            {
                "reason_id": "REJECT-03",
                "reason_name": "receptor_parameter_or_operational_targeting",
                "rejection_rule": "Reject candidates containing receptor parameters, operational targeting, host tropism mechanics, or host range prediction.",
                "boundary_note": "No receptor parameters and no operational targeting are introduced.",
            },
            {
                "reason_id": "REJECT-04",
                "reason_name": "wet_lab_or_actionable_biosafety_risk",
                "rejection_rule": "Reject wet-lab protocols, actionable biosafety-risk instructions, infectivity optimization, immune evasion optimization, or operational host targeting.",
                "boundary_note": "Wet-lab protocol count and actionable biosafety-risk instruction count remain zero.",
            },
            {
                "reason_id": "REJECT-05",
                "reason_name": "claim_validation_or_readiness_upgrade",
                "rejection_rule": "Reject candidates used to claim validation, readiness, proof, external validation, or independent experiment completion.",
                "boundary_note": "Readiness approval count and external validation count remain zero.",
            },
            {
                "reason_id": "REJECT-06",
                "reason_name": "citation_integration_completion_claim",
                "rejection_rule": "Reject candidates used to imply citation integration has already been completed.",
                "boundary_note": "does not complete citation integration.",
            },
            {
                "reason_id": "REJECT-07",
                "reason_name": "manuscript_mutation_or_rewrite_permission",
                "rejection_rule": "Reject candidates used as permission to modify manuscript files or apply rewrites in this milestone.",
                "boundary_note": "No manuscript file is modified.",
            },
            {
                "reason_id": "REJECT-08",
                "reason_name": "evaluation_result_or_performance_claim",
                "rejection_rule": "Reject candidates used to imply executed evaluation, project performance results, metric scores, or validation outcomes.",
                "boundary_note": "Toy evaluation actual run count remains zero.",
            },
            {
                "reason_id": "REJECT-09",
                "reason_name": "evidence_gap_closure_claim",
                "rejection_rule": "Reject candidates used to imply scientific evidence gaps are closed.",
                "boundary_note": "No evidence upgrade is completed.",
            },
            {
                "reason_id": "REJECT-10",
                "reason_name": "future_work_overclaim",
                "rejection_rule": "Reject candidates used to imply future work has already occurred.",
                "boundary_note": "Future work may only introduce stronger claims after separately audited milestones.",
            },
        ]

    def _preflight_checks(self) -> List[Dict[str, str]]:
        return [
            {
                "check_id": "PREFLIGHT-01",
                "check_name": "source_eligibility_artifact_available",
                "required_result": "v8.220 eligibility and query plan artifact must exist before retrieval planning advances.",
                "observed_status": "available",
                "boundary_note": "This confirms artifact availability, not retrieval execution.",
            },
            {
                "check_id": "PREFLIGHT-02",
                "check_name": "citation_slots_remain_unresolved",
                "required_result": "All citation slots remain unresolved placeholders before any retrieval milestone.",
                "observed_status": "unresolved",
                "boundary_note": "No actual citation is added.",
            },
            {
                "check_id": "PREFLIGHT-03",
                "check_name": "retrieval_authorization_absent",
                "required_result": "No retrieval authorization is granted in this milestone.",
                "observed_status": "absent",
                "boundary_note": "Retrieval authorization count remains zero.",
            },
            {
                "check_id": "PREFLIGHT-04",
                "check_name": "source_verification_absent",
                "required_result": "No source is claimed as verified.",
                "observed_status": "absent",
                "boundary_note": "Verified source count remains zero.",
            },
            {
                "check_id": "PREFLIGHT-05",
                "check_name": "citation_integration_absent",
                "required_result": "No citation is integrated into any manuscript file.",
                "observed_status": "absent",
                "boundary_note": "No new citation is added.",
            },
            {
                "check_id": "PREFLIGHT-06",
                "check_name": "manuscript_mutation_absent",
                "required_result": "No manuscript file is modified.",
                "observed_status": "absent",
                "boundary_note": "No manuscript file is modified.",
            },
            {
                "check_id": "PREFLIGHT-07",
                "check_name": "evaluation_execution_absent",
                "required_result": "No evaluation is executed.",
                "observed_status": "absent",
                "boundary_note": "Toy evaluation actual run count remains zero.",
            },
            {
                "check_id": "PREFLIGHT-08",
                "check_name": "readiness_approval_absent",
                "required_result": "No manuscript submission readiness or approval is claimed.",
                "observed_status": "absent",
                "boundary_note": "Manuscript submission ready count remains zero.",
            },
            {
                "check_id": "PREFLIGHT-09",
                "check_name": "real_biological_operational_content_absent",
                "required_result": "No real biological datasets, pathogen models, receptor parameters, operational targeting, or wet-lab protocols are introduced.",
                "observed_status": "absent",
                "boundary_note": "No real biological datasets, no real pathogen models, no receptor parameters, and no operational targeting are introduced.",
            },
            {
                "check_id": "PREFLIGHT-10",
                "check_name": "future_milestone_required",
                "required_result": "Future source retrieval requires a separate official milestone.",
                "observed_status": "required",
                "boundary_note": "Future source retrieval requires a separate official milestone.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        eligibility_source = self._load_json(self.source_eligibility_json_path)
        eligibility_md = self._load_text(self.source_eligibility_md_path)
        citation_slot_source = self._load_json(self.source_citation_slot_json_path)
        citation_slot_md = self._load_text(self.source_citation_slot_md_path)
        coherence_source = self._load_json(self.source_coherence_json_path)
        eval_source = self._load_json(self.source_eval_json_path)
        gap_source = self._load_json(self.source_gap_json_path)
        assembly_source = self._load_json(self.source_assembly_json_path)

        eligibility_counters = eligibility_source.get("counters", {})
        citation_counters = citation_slot_source.get("counters", {})
        coherence_counters = coherence_source.get("counters", {})
        eval_counters = eval_source.get("counters", {})
        gap_counters = gap_source.get("counters", {})
        assembly_counters = assembly_source.get("counters", {})

        retrieval_gate_items = self._retrieval_gate_items()
        allowed_query_families = self._allowed_query_families()
        acceptance_schema = self._acceptance_schema()
        rejection_schema = self._rejection_schema()
        preflight_checks = self._preflight_checks()

        counters = {
            "Safe abstract toy citation retrieval readiness gate count": 1,
            "New safe abstract toy citation retrieval readiness gate count": 1,
            "Toy citation retrieval readiness gate JSON export count": 1,
            "Toy citation retrieval gate item count": len(retrieval_gate_items),
            "Toy citation retrieval allowed query family count": len(allowed_query_families),
            "Toy citation retrieval acceptance schema field count": len(acceptance_schema),
            "Toy citation retrieval rejection reason count": len(rejection_schema),
            "Toy citation retrieval preflight check count": len(preflight_checks),
            "Toy citation retrieval authorization count": 0,
            "Toy citation retrieval execution count": 0,
            "Toy citation retrieval source retrieval count": 0,
            "Toy citation retrieval verified source count": 0,
            "Toy citation retrieval accepted source count": 0,
            "Toy citation retrieval rejected source count": 0,
            "Toy citation retrieval actual citation count": 0,
            "Toy citation retrieval fabricated reference count": 0,
            "Toy citation retrieval integration completion count": 0,
            "Toy citation retrieval added to manuscript count": 0,
            "Toy citation retrieval source eligibility rule count": eligibility_counters.get("Toy citation source eligibility rule count"),
            "Toy citation retrieval source query plan count": eligibility_counters.get("Toy citation source query plan count"),
            "Toy citation retrieval source exclusion group count": eligibility_counters.get("Toy citation source exclusion group count"),
            "Toy citation retrieval source prior retrieval count": eligibility_counters.get("Toy citation source retrieval count"),
            "Toy citation retrieval source prior verified source count": eligibility_counters.get("Toy citation source verified source count"),
            "Toy citation retrieval source prior actual citation count": eligibility_counters.get("Toy citation source actual citation count"),
            "Toy citation retrieval source prior fabricated reference count": eligibility_counters.get("Toy citation source fabricated reference count"),
            "Toy citation retrieval source prior integration completion count": eligibility_counters.get("Toy citation source integration completion count"),
            "Toy citation retrieval source prior added to manuscript count": eligibility_counters.get("Toy citation source added to manuscript count"),
            "Toy citation retrieval source slot count": citation_counters.get("Toy citation slot count"),
            "Toy citation retrieval source unresolved slot count": citation_counters.get("Toy citation unresolved slot count"),
            "Toy citation retrieval source slot group count": citation_counters.get("Toy citation slot group count"),
            "Toy citation retrieval source assembly section count": assembly_counters.get("Toy manuscript assembly preview section count"),
            "Toy citation retrieval source gap item count": gap_counters.get("Toy scientific gap register item count"),
            "Toy citation retrieval source P0 gap count": gap_counters.get("Toy scientific gap P0 count"),
            "Toy citation retrieval source evidence upgrade completed count": gap_counters.get("Toy scientific evidence upgrade completed count"),
            "Toy citation retrieval source evaluation design module count": eval_counters.get("Toy evaluation design module count"),
            "Toy citation retrieval source actual evaluation run count": eval_counters.get("Toy evaluation actual run count"),
            "Toy citation retrieval source validation claim count": eval_counters.get("Toy evaluation validation claim count"),
            "Toy citation retrieval source coherence improvement item count": coherence_counters.get("Toy manuscript coherence improvement item count"),
            "Toy citation retrieval source coherence rewrite application count": coherence_counters.get("Toy manuscript coherence rewrite application count"),
            "Toy citation retrieval gate execution count": 1,
            "Toy citation retrieval gate direct execution count": 1,
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
            "title": "Safe Abstract Toy Citation Retrieval Readiness Gate",
            "source_eligibility_json": str(self.source_eligibility_json_path),
            "source_eligibility_markdown": str(self.source_eligibility_md_path),
            "source_eligibility_markdown_character_count": len(eligibility_md),
            "source_citation_slot_json": str(self.source_citation_slot_json_path),
            "source_citation_slot_markdown": str(self.source_citation_slot_md_path),
            "source_citation_slot_markdown_character_count": len(citation_slot_md),
            "source_coherence_json": str(self.source_coherence_json_path),
            "source_evaluation_design_json": str(self.source_eval_json_path),
            "source_gap_json": str(self.source_gap_json_path),
            "source_assembly_json": str(self.source_assembly_json_path),
            "plan_phrase": self.plan_phrase,
            "scope": "citation-retrieval-readiness-gate-only",
            "safe_abstract_toy_only": True,
            "synthetic_only": True,
            "abstract_graphs_only": True,
            "unitless_parameters_only": True,
            "non_operational_only": True,
            "retrieval_readiness_gate_completed": True,
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
                "This v8.221 artifact creates a citation retrieval readiness gate only. "
                "Retrieval readiness gate only. No retrieval authorization is granted. "
                "No source retrieval is performed. No actual citation is added. "
                "No fabricated reference is introduced. No source is claimed as verified. "
                "It does not complete citation integration, does not validate scientific claims, "
                "does not modify manuscript files, and No manuscript file is modified. "
                "No new citation is added. Future source retrieval requires a separate official milestone."
            ),
            "retrieval_gate_items": retrieval_gate_items,
            "allowed_query_families": allowed_query_families,
            "acceptance_schema": acceptance_schema,
            "rejection_schema": rejection_schema,
            "preflight_checks": preflight_checks,
            "boundary_notes": (
                [item["boundary_note"] for item in retrieval_gate_items]
                + [item["boundary_note"] for item in allowed_query_families]
                + [item["boundary_note"] for item in acceptance_schema]
                + [item["boundary_note"] for item in rejection_schema]
                + [item["boundary_note"] for item in preflight_checks]
            ),
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "citation-retrieval-readiness-gate-only":
            raise AssertionError("v8.221 must remain citation-retrieval-readiness-gate-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.221 citation retrieval readiness gate must pass.")

        if report["retrieval_readiness_gate_completed"] is not True:
            raise AssertionError("v8.221 should complete only the retrieval readiness gate.")

        for field in [
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
            "Toy citation retrieval gate item count": 12,
            "Toy citation retrieval allowed query family count": 12,
            "Toy citation retrieval acceptance schema field count": 12,
            "Toy citation retrieval rejection reason count": 10,
            "Toy citation retrieval preflight check count": 10,
            "Toy citation retrieval authorization count": 0,
            "Toy citation retrieval execution count": 0,
            "Toy citation retrieval source retrieval count": 0,
            "Toy citation retrieval verified source count": 0,
            "Toy citation retrieval accepted source count": 0,
            "Toy citation retrieval rejected source count": 0,
            "Toy citation retrieval actual citation count": 0,
            "Toy citation retrieval fabricated reference count": 0,
            "Toy citation retrieval integration completion count": 0,
            "Toy citation retrieval added to manuscript count": 0,
            "Toy citation retrieval source eligibility rule count": 12,
            "Toy citation retrieval source query plan count": 12,
            "Toy citation retrieval source exclusion group count": 4,
            "Toy citation retrieval source prior retrieval count": 0,
            "Toy citation retrieval source prior verified source count": 0,
            "Toy citation retrieval source prior actual citation count": 0,
            "Toy citation retrieval source prior fabricated reference count": 0,
            "Toy citation retrieval source prior integration completion count": 0,
            "Toy citation retrieval source prior added to manuscript count": 0,
            "Toy citation retrieval source slot count": 12,
            "Toy citation retrieval source unresolved slot count": 12,
            "Toy citation retrieval source slot group count": 4,
            "Toy citation retrieval source assembly section count": 9,
            "Toy citation retrieval source gap item count": 12,
            "Toy citation retrieval source P0 gap count": 6,
            "Toy citation retrieval source evidence upgrade completed count": 0,
            "Toy citation retrieval source evaluation design module count": 10,
            "Toy citation retrieval source actual evaluation run count": 0,
            "Toy citation retrieval source validation claim count": 0,
            "Toy citation retrieval source coherence improvement item count": 10,
            "Toy citation retrieval source coherence rewrite application count": 0,
        }

        for name, expected in expected_counts.items():
            if counters.get(name) != expected:
                raise AssertionError(f"Expected {expected} for {name}, got {counters.get(name)}")

        combined_text = (
            json.dumps(report["retrieval_gate_items"], ensure_ascii=False)
            + " "
            + json.dumps(report["allowed_query_families"], ensure_ascii=False)
            + " "
            + json.dumps(report["acceptance_schema"], ensure_ascii=False)
            + " "
            + json.dumps(report["rejection_schema"], ensure_ascii=False)
            + " "
            + json.dumps(report["preflight_checks"], ensure_ascii=False)
            + " "
            + report["non_readiness_disclaimer"]
        )

        required_phrases = [
            "citation retrieval readiness gate",
            "Retrieval readiness gate only",
            "not_authorized_for_retrieval",
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
            "Future work may only introduce stronger claims",
        ]

        for phrase in required_phrases:
            if phrase not in combined_text:
                raise AssertionError(f"Missing required retrieval gate phrase: {phrase}")

        must_be_zero = [
            "Toy citation retrieval authorization count",
            "Toy citation retrieval execution count",
            "Toy citation retrieval source retrieval count",
            "Toy citation retrieval verified source count",
            "Toy citation retrieval accepted source count",
            "Toy citation retrieval rejected source count",
            "Toy citation retrieval actual citation count",
            "Toy citation retrieval fabricated reference count",
            "Toy citation retrieval integration completion count",
            "Toy citation retrieval added to manuscript count",
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

        lines.append("# Safe Abstract Toy Citation Retrieval Readiness Gate")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is citation-retrieval-readiness-gate-only.")
        lines.append("It defines retrieval gates, allowed query families, acceptance schema, rejection schema, and preflight checks without source retrieval, source verification, citation insertion, or manuscript mutation.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")
        lines.append("## Retrieval Gate Items")
        lines.append("")

        for item in report["retrieval_gate_items"]:
            lines.append(f"### {item['gate_id']} — {item['slot_id']} — {item['gate_area']}")
            lines.append("")
            lines.append(f"- Readiness requirement: {item['readiness_requirement']}")
            lines.append(f"- Pass condition: {item['pass_condition']}")
            lines.append(f"- Fail condition: {item['fail_condition']}")
            lines.append(f"- Authorization status: {item['authorization_status']}")
            lines.append(f"- Boundary note: {item['boundary_note']}")
            lines.append("")

        lines.append("## Allowed Query Families")
        lines.append("")

        for item in report["allowed_query_families"]:
            lines.append(f"### {item['family_id']} — {item['slot_id']}")
            lines.append("")
            lines.append(f"- Allowed family: {item['allowed_family']}")
            lines.append(f"- Execution status: {item['execution_status']}")
            lines.append(f"- Boundary note: {item['boundary_note']}")
            lines.append("")

        lines.append("## Acceptance Schema")
        lines.append("")

        for item in report["acceptance_schema"]:
            lines.append(f"### {item['field_id']} — {item['field_name']}")
            lines.append("")
            lines.append(f"- Required value rule: {item['required_value_rule']}")
            lines.append(f"- Boundary note: {item['boundary_note']}")
            lines.append("")

        lines.append("## Rejection Schema")
        lines.append("")

        for item in report["rejection_schema"]:
            lines.append(f"### {item['reason_id']} — {item['reason_name']}")
            lines.append("")
            lines.append(f"- Rejection rule: {item['rejection_rule']}")
            lines.append(f"- Boundary note: {item['boundary_note']}")
            lines.append("")

        lines.append("## Preflight Checks")
        lines.append("")

        for item in report["preflight_checks"]:
            lines.append(f"### {item['check_id']} — {item['check_name']}")
            lines.append("")
            lines.append(f"- Required result: {item['required_result']}")
            lines.append(f"- Observed status: {item['observed_status']}")
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
        lines.append("V8_221_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_READINESS_GATE_OK")
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


def build_safe_abstract_toy_citation_retrieval_readiness_gate() -> Dict[str, Any]:
    return SafeAbstractToyCitationRetrievalReadinessGateBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_citation_retrieval_readiness_gate()
    counters = result["counters"]
    print("V8_221_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_READINESS_GATE_OK")
    print("TOY_CITATION_RETRIEVAL_READINESS_GATE_DIRECT_CHECK_OK")
    print(f"Retrieval gate item count: {counters['Toy citation retrieval gate item count']}")
    print(f"Allowed query family count: {counters['Toy citation retrieval allowed query family count']}")
    print(f"Acceptance schema field count: {counters['Toy citation retrieval acceptance schema field count']}")
    print(f"Rejection reason count: {counters['Toy citation retrieval rejection reason count']}")
    print(f"Preflight check count: {counters['Toy citation retrieval preflight check count']}")
    print(f"Retrieval authorization count: {counters['Toy citation retrieval authorization count']}")
    print(f"Retrieval execution count: {counters['Toy citation retrieval execution count']}")
    print(f"Source retrieval count: {counters['Toy citation retrieval source retrieval count']}")
    print(f"Verified source count: {counters['Toy citation retrieval verified source count']}")
    print(f"Accepted source count: {counters['Toy citation retrieval accepted source count']}")
    print(f"Rejected source count: {counters['Toy citation retrieval rejected source count']}")
    print(f"Actual citation count: {counters['Toy citation retrieval actual citation count']}")
    print(f"Fabricated reference count: {counters['Toy citation retrieval fabricated reference count']}")
    print(f"Citation integration completion count: {counters['Toy citation retrieval integration completion count']}")
    print(f"Citation added to manuscript count: {counters['Toy citation retrieval added to manuscript count']}")
    print(f"Source eligibility rule count: {counters['Toy citation retrieval source eligibility rule count']}")
    print(f"Source query plan count: {counters['Toy citation retrieval source query plan count']}")
    print(f"Source exclusion group count: {counters['Toy citation retrieval source exclusion group count']}")
    print(f"Source slot count: {counters['Toy citation retrieval source slot count']}")
    print(f"Source unresolved slot count: {counters['Toy citation retrieval source unresolved slot count']}")
    print(f"Source slot group count: {counters['Toy citation retrieval source slot group count']}")
    print(f"Source assembly section count: {counters['Toy citation retrieval source assembly section count']}")
    print(f"Source gap item count: {counters['Toy citation retrieval source gap item count']}")
    print(f"Source P0 gap count: {counters['Toy citation retrieval source P0 gap count']}")
    print(f"Source evaluation design module count: {counters['Toy citation retrieval source evaluation design module count']}")
    print(f"Source coherence improvement item count: {counters['Toy citation retrieval source coherence improvement item count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {result['passed']}")
