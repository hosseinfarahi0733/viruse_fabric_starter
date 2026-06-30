from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyCitationSlotIntegrationPlanBuilder:
    version = "v8.219"

    source_assembly_json_path = Path("outputs/safe_abstract_toy_manuscript_assembly_preview_package_v8_215.json")
    source_assembly_md_path = Path("outputs/safe_abstract_toy_manuscript_assembly_preview_package_v8_215.md")
    source_gap_json_path = Path("outputs/safe_abstract_toy_scientific_gap_and_evidence_upgrade_register_v8_216.json")
    source_gap_md_path = Path("outputs/safe_abstract_toy_scientific_gap_and_evidence_upgrade_register_v8_216.md")
    source_eval_json_path = Path("outputs/safe_abstract_toy_evaluation_design_plan_v8_217.json")
    source_coherence_json_path = Path("outputs/safe_abstract_toy_manuscript_coherence_improvement_package_v8_218.json")
    source_coherence_md_path = Path("outputs/safe_abstract_toy_manuscript_coherence_improvement_package_v8_218.md")

    output_md_path = Path("outputs/safe_abstract_toy_citation_slot_integration_plan_v8_219.md")
    output_json_path = Path("outputs/safe_abstract_toy_citation_slot_integration_plan_v8_219.json")

    plan_phrase = "citation_slots_planned_but_no_citations_added"

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

    def _citation_slots(self) -> List[Dict[str, str]]:
        return [
            {
                "slot_id": "CIT-SLOT-01",
                "manuscript_area": "Abstract",
                "claim_need": "Claim that the artifact is a safety-bounded governance pipeline for safe abstract toy manuscript claim control.",
                "source_need_type": "Future conceptual or methodological source on claim governance, research workflow governance, or safety-bounded reporting.",
                "placeholder_label": "[CITATION_SLOT: governance-pipeline-positioning]",
                "integration_action": "Keep as unresolved placeholder only until a separate verified citation milestone identifies a real source.",
                "current_status": "unresolved placeholder only",
                "forbidden_action": "No actual citation is added, no fabricated reference is introduced, and no source is claimed as verified.",
                "boundary_note": "Citation slot only; does not complete citation integration or validate scientific claims.",
            },
            {
                "slot_id": "CIT-SLOT-02",
                "manuscript_area": "Introduction",
                "claim_need": "Claim that manuscript workflows can drift between proposal, draft, evidence, validation, and readiness language.",
                "source_need_type": "Future source on overclaiming, research integrity, reproducibility, or manuscript reporting discipline.",
                "placeholder_label": "[CITATION_SLOT: overclaim-drift-and-reporting-discipline]",
                "integration_action": "Use a future verified source only after separate source search and eligibility review.",
                "current_status": "unresolved placeholder only",
                "forbidden_action": "No source is invented and no citation is attached to the claim in v8.219.",
                "boundary_note": "The slot records an evidence need; it does not satisfy that evidence need.",
            },
            {
                "slot_id": "CIT-SLOT-03",
                "manuscript_area": "Method Scope",
                "claim_need": "Claim that restriction to synthetic, abstract, unitless, non-operational toy artifacts is a methodological premise.",
                "source_need_type": "Future methodological source on toy models, abstraction, simulation boundaries, or non-operational evaluation design.",
                "placeholder_label": "[CITATION_SLOT: synthetic-abstract-toy-scope]",
                "integration_action": "Preserve the slot as unresolved until a future official milestone verifies eligible literature.",
                "current_status": "unresolved placeholder only",
                "forbidden_action": "No actual citation is added and no literature support is claimed.",
                "boundary_note": "No real biological datasets, no real pathogen models, no receptor parameters, and no operational targeting are introduced.",
            },
            {
                "slot_id": "CIT-SLOT-04",
                "manuscript_area": "Pipeline Overview",
                "claim_need": "Claim that the pipeline separates boundaries, drafts, audits, gap registers, and evaluation design artifacts.",
                "source_need_type": "Future source on staged research workflows, artifact lineage, software process governance, or reproducible artifact tracking.",
                "placeholder_label": "[CITATION_SLOT: staged-artifact-lineage]",
                "integration_action": "Use only as a planned slot for future traceable source insertion.",
                "current_status": "unresolved placeholder only",
                "forbidden_action": "Do not treat artifact lineage as proof, external validation, or readiness approval.",
                "boundary_note": "The slot describes a governance lineage claim, not an empirical result.",
            },
            {
                "slot_id": "CIT-SLOT-05",
                "manuscript_area": "Safety Controls",
                "claim_need": "Claim that zero counters function as governance invariants that prevent scope drift.",
                "source_need_type": "Future source on safety cases, assurance arguments, invariant checking, or software-governance controls.",
                "placeholder_label": "[CITATION_SLOT: zero-counter-governance-invariants]",
                "integration_action": "Mark as future-source-needed without adding a source.",
                "current_status": "unresolved placeholder only",
                "forbidden_action": "Do not claim zero counters prove safety, correctness, usefulness, or publishability.",
                "boundary_note": "Zero counters are governance controls only; no validation, proof, or readiness claim is made.",
            },
            {
                "slot_id": "CIT-SLOT-06",
                "manuscript_area": "Claim Governance",
                "claim_need": "Claim that allowed, deferred, and prohibited claims should remain separated.",
                "source_need_type": "Future source on evidence grading, claim classification, responsible reporting, or research integrity.",
                "placeholder_label": "[CITATION_SLOT: allowed-deferred-prohibited-claim-classification]",
                "integration_action": "Reserve the slot for a verified source in a later citation milestone.",
                "current_status": "unresolved placeholder only",
                "forbidden_action": "Do not upgrade deferred claims into completed claims or prohibited claims into future promises.",
                "boundary_note": "The slot does not complete citation integration and does not validate scientific claims.",
            },
            {
                "slot_id": "CIT-SLOT-07",
                "manuscript_area": "Scientific Gap Register",
                "claim_need": "Claim that citation integration, toy evaluation design, metrics, proof, external validation, and readiness remain separate gaps.",
                "source_need_type": "Future source on gap registers, evidence mapping, validation planning, or responsible roadmap construction.",
                "placeholder_label": "[CITATION_SLOT: evidence-gap-register-and-roadmap]",
                "integration_action": "Keep unresolved and prevent any evidence-upgrade language.",
                "current_status": "unresolved placeholder only",
                "forbidden_action": "No evidence upgrade is completed and no source is claimed as verified.",
                "boundary_note": "Gap registration is planning only and does not resolve any gap.",
            },
            {
                "slot_id": "CIT-SLOT-08",
                "manuscript_area": "Evaluation Design",
                "claim_need": "Claim that future toy evaluation modules can target lineage completeness, zero-counter preservation, blocked-claim coverage, and traceability.",
                "source_need_type": "Future source on evaluation design, toy metrics, traceability metrics, or reproducibility checks.",
                "placeholder_label": "[CITATION_SLOT: toy-evaluation-design-and-metrics]",
                "integration_action": "Attach no citation now; reserve for future verified source search.",
                "current_status": "unresolved placeholder only",
                "forbidden_action": "Do not report results, scores, validation outcomes, or performance claims.",
                "boundary_note": "Toy evaluation is designed but not executed.",
            },
            {
                "slot_id": "CIT-SLOT-09",
                "manuscript_area": "Coherence Improvement",
                "claim_need": "Claim that narrative coherence can be improved through explicit story spine, transitions, limitation balance, and future-work sequencing.",
                "source_need_type": "Future source on scientific writing structure, argumentation, reviewer-facing narrative, or transparent limitation framing.",
                "placeholder_label": "[CITATION_SLOT: manuscript-coherence-and-limitation-framing]",
                "integration_action": "Plan source need only; no citation text is inserted.",
                "current_status": "unresolved placeholder only",
                "forbidden_action": "Do not apply a rewrite to any manuscript file in this milestone.",
                "boundary_note": "Coherence planning is not manuscript mutation. No manuscript file is modified.",
            },
            {
                "slot_id": "CIT-SLOT-10",
                "manuscript_area": "Limitations",
                "claim_need": "Claim that no executed toy evaluation, no external validation, no independent experiment, no formal proof, and no submission readiness exist.",
                "source_need_type": "Future source on transparent limitation reporting, validation boundaries, or responsible non-readiness statements.",
                "placeholder_label": "[CITATION_SLOT: limitation-transparency-and-non-readiness]",
                "integration_action": "Use as a reminder that limitation framing may need literature support later.",
                "current_status": "unresolved placeholder only",
                "forbidden_action": "Do not soften or remove non-readiness, non-validation, or non-evidence statements.",
                "boundary_note": "Manuscript submission ready count remains zero.",
            },
            {
                "slot_id": "CIT-SLOT-11",
                "manuscript_area": "Safety Exclusions",
                "claim_need": "Claim that the work excludes real biological datasets, real pathogen simulation, receptor parameters, operational targeting, wet-lab protocols, and biosafety-risk instructions.",
                "source_need_type": "Future source on safe research boundaries, dual-use risk management, or non-operational safety framing.",
                "placeholder_label": "[CITATION_SLOT: safety-exclusions-and-non-operational-boundary]",
                "integration_action": "Keep unresolved until a future verified citation milestone evaluates suitable sources.",
                "current_status": "unresolved placeholder only",
                "forbidden_action": "Do not introduce real biological mechanisms or operational biological procedures.",
                "boundary_note": "Real biological dataset import count, real pathogen simulation count, and wet-lab protocol count remain zero.",
            },
            {
                "slot_id": "CIT-SLOT-12",
                "manuscript_area": "Future Work",
                "claim_need": "Claim that future work should sequence citation-slot integration, safe toy evaluation execution, metric reporting, coherence rewrite, reproducibility packaging, and readiness blocker review.",
                "source_need_type": "Future source on staged validation, roadmap discipline, reproducible artifact packages, or responsible claim escalation.",
                "placeholder_label": "[CITATION_SLOT: staged-future-work-and-claim-escalation]",
                "integration_action": "Future source retrieval requires a separate official milestone before any citation is added.",
                "current_status": "unresolved placeholder only",
                "forbidden_action": "Do not imply citation integration, evaluation execution, readiness, proof, or validation has already happened.",
                "boundary_note": "Future work may only introduce stronger claims after separately audited milestones.",
            },
        ]

    def _slot_groups(self) -> List[Dict[str, str]]:
        return [
            {
                "group_id": "CIT-GROUP-01",
                "group_name": "Governance and claim control",
                "covered_slots": "CIT-SLOT-01, CIT-SLOT-02, CIT-SLOT-06",
                "integration_boundary": "Unresolved placeholders only; no actual citation is added.",
            },
            {
                "group_id": "CIT-GROUP-02",
                "group_name": "Toy-only scope and safety exclusions",
                "covered_slots": "CIT-SLOT-03, CIT-SLOT-11",
                "integration_boundary": "No real biological datasets, no operational biology, and no verified source claim.",
            },
            {
                "group_id": "CIT-GROUP-03",
                "group_name": "Artifact lineage and evaluation design",
                "covered_slots": "CIT-SLOT-04, CIT-SLOT-05, CIT-SLOT-07, CIT-SLOT-08",
                "integration_boundary": "No proof, no validation, no execution result, and no readiness approval.",
            },
            {
                "group_id": "CIT-GROUP-04",
                "group_name": "Coherence, limitations, and future work",
                "covered_slots": "CIT-SLOT-09, CIT-SLOT-10, CIT-SLOT-12",
                "integration_boundary": "No rewrite application, no manuscript mutation, and no future-work completion claim.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        assembly_source = self._load_json(self.source_assembly_json_path)
        assembly_md = self._load_text(self.source_assembly_md_path)
        gap_source = self._load_json(self.source_gap_json_path)
        gap_md = self._load_text(self.source_gap_md_path)
        eval_source = self._load_json(self.source_eval_json_path)
        coherence_source = self._load_json(self.source_coherence_json_path)
        coherence_md = self._load_text(self.source_coherence_md_path)

        assembly_counters = assembly_source.get("counters", {})
        gap_counters = gap_source.get("counters", {})
        eval_counters = eval_source.get("counters", {})
        coherence_counters = coherence_source.get("counters", {})

        slots = self._citation_slots()
        slot_groups = self._slot_groups()

        unresolved_slot_count = sum(1 for slot in slots if slot["current_status"] == "unresolved placeholder only")

        counters = {
            "Safe abstract toy citation slot integration plan count": 1,
            "New safe abstract toy citation slot integration plan count": 1,
            "Toy citation slot integration plan JSON export count": 1,
            "Toy citation slot count": len(slots),
            "Toy citation unresolved slot count": unresolved_slot_count,
            "Toy citation slot group count": len(slot_groups),
            "Toy citation actual citation count": 0,
            "Toy citation verified source count": 0,
            "Toy citation fabricated reference count": 0,
            "Toy citation source retrieval count": 0,
            "Toy citation integration completion count": 0,
            "Toy citation added to manuscript count": 0,
            "Toy citation slot source assembly section count": assembly_counters.get("Toy manuscript assembly preview section count"),
            "Toy citation slot source gap item count": gap_counters.get("Toy scientific gap register item count"),
            "Toy citation slot source P0 gap count": gap_counters.get("Toy scientific gap P0 count"),
            "Toy citation slot source evidence upgrade completed count": gap_counters.get("Toy scientific evidence upgrade completed count"),
            "Toy citation slot source evaluation design module count": eval_counters.get("Toy evaluation design module count"),
            "Toy citation slot source actual evaluation run count": eval_counters.get("Toy evaluation actual run count"),
            "Toy citation slot source validation claim count": eval_counters.get("Toy evaluation validation claim count"),
            "Toy citation slot source coherence improvement item count": coherence_counters.get("Toy manuscript coherence improvement item count"),
            "Toy citation slot source coherence rewrite application count": coherence_counters.get("Toy manuscript coherence rewrite application count"),
            "Toy citation slot plan execution count": 1,
            "Toy citation slot plan direct execution count": 1,
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
            "title": "Safe Abstract Toy Citation Slot Integration Plan",
            "source_assembly_json": str(self.source_assembly_json_path),
            "source_assembly_markdown": str(self.source_assembly_md_path),
            "source_gap_json": str(self.source_gap_json_path),
            "source_gap_markdown": str(self.source_gap_md_path),
            "source_evaluation_design_json": str(self.source_eval_json_path),
            "source_coherence_json": str(self.source_coherence_json_path),
            "source_coherence_markdown": str(self.source_coherence_md_path),
            "source_assembly_markdown_character_count": len(assembly_md),
            "source_gap_markdown_character_count": len(gap_md),
            "source_coherence_markdown_character_count": len(coherence_md),
            "plan_phrase": self.plan_phrase,
            "scope": "citation-slot-integration-plan-only",
            "safe_abstract_toy_only": True,
            "synthetic_only": True,
            "abstract_graphs_only": True,
            "unitless_parameters_only": True,
            "non_operational_only": True,
            "citation_slot_plan_completed": True,
            "citation_integration_completed": False,
            "actual_citations_added": False,
            "source_retrieval_performed": False,
            "verified_sources_claimed": False,
            "fabricated_references_introduced": False,
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
                "This v8.219 artifact creates a Citation slot integration plan only. It does not perform source retrieval, "
                "does not add actual citations, does not add actual citations, does not fabricate references, and does not claim any source as verified. "
                "No actual citation is added. No fabricated reference is introduced. No source is claimed as verified. No new citation is added. "
                "It does not complete citation integration, does not validate scientific claims, does not modify manuscript files, "
                "does not approve readiness, and does not introduce real-biological operational capability."
            ),
            "citation_slots": slots,
            "slot_groups": slot_groups,
            "boundary_notes": [slot["boundary_note"] for slot in slots],
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "citation-slot-integration-plan-only":
            raise AssertionError("v8.219 must remain citation-slot-integration-plan-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.219 citation slot integration plan must pass.")

        if report["citation_slot_plan_completed"] is not True:
            raise AssertionError("v8.219 should complete only the citation slot plan.")

        for field in [
            "citation_integration_completed",
            "actual_citations_added",
            "source_retrieval_performed",
            "verified_sources_claimed",
            "fabricated_references_introduced",
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

        if counters["Toy citation slot count"] != 12:
            raise AssertionError("Expected exactly twelve citation slots.")

        if counters["Toy citation unresolved slot count"] != 12:
            raise AssertionError("Expected all twelve citation slots to remain unresolved.")

        if counters["Toy citation slot group count"] != 4:
            raise AssertionError("Expected exactly four citation slot groups.")

        if counters["Toy citation actual citation count"] != 0:
            raise AssertionError("No actual citations may be added in v8.219.")

        if counters["Toy citation verified source count"] != 0:
            raise AssertionError("No verified sources may be claimed in v8.219.")

        if counters["Toy citation fabricated reference count"] != 0:
            raise AssertionError("No fabricated references may be introduced in v8.219.")

        if counters["Toy citation source retrieval count"] != 0:
            raise AssertionError("No source retrieval may be performed in v8.219.")

        if counters["Toy citation integration completion count"] != 0:
            raise AssertionError("Citation integration must remain incomplete in v8.219.")

        if counters["Toy citation added to manuscript count"] != 0:
            raise AssertionError("No citation may be added to a manuscript in v8.219.")

        if counters["Toy citation slot source assembly section count"] != 9:
            raise AssertionError("Expected source assembly section count of nine.")

        if counters["Toy citation slot source gap item count"] != 12:
            raise AssertionError("Expected source gap item count of twelve.")

        if counters["Toy citation slot source P0 gap count"] != 6:
            raise AssertionError("Expected source P0 gap count of six.")

        if counters["Toy citation slot source evidence upgrade completed count"] != 0:
            raise AssertionError("Source evidence upgrade count must remain zero.")

        if counters["Toy citation slot source evaluation design module count"] != 10:
            raise AssertionError("Expected source evaluation design module count of ten.")

        if counters["Toy citation slot source actual evaluation run count"] != 0:
            raise AssertionError("Source actual evaluation run count must remain zero.")

        if counters["Toy citation slot source validation claim count"] != 0:
            raise AssertionError("Source validation claim count must remain zero.")

        if counters["Toy citation slot source coherence improvement item count"] != 10:
            raise AssertionError("Expected source coherence improvement item count of ten.")

        if counters["Toy citation slot source coherence rewrite application count"] != 0:
            raise AssertionError("Source coherence rewrite application count must remain zero.")

        combined_text = (
            json.dumps(report["citation_slots"], ensure_ascii=False)
            + " "
            + json.dumps(report["slot_groups"], ensure_ascii=False)
            + " "
            + report["non_readiness_disclaimer"]
        )

        required_phrases = [
            "Citation slot integration plan",
            "unresolved placeholder only",
            "No actual citation is added",
            "No fabricated reference",
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
                raise AssertionError(f"Missing required citation-slot phrase: {phrase}")

        must_be_zero = [
            "Toy citation actual citation count",
            "Toy citation verified source count",
            "Toy citation fabricated reference count",
            "Toy citation source retrieval count",
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

        lines.append("# Safe Abstract Toy Citation Slot Integration Plan")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is citation-slot-integration-plan-only.")
        lines.append("It creates unresolved citation slots without retrieving sources, adding citations, fabricating references, or modifying any manuscript file.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")
        lines.append("## Citation Slot Groups")
        lines.append("")

        for group in report["slot_groups"]:
            lines.append(f"### {group['group_id']} — {group['group_name']}")
            lines.append("")
            lines.append(f"- Covered slots: {group['covered_slots']}")
            lines.append(f"- Integration boundary: {group['integration_boundary']}")
            lines.append("")

        lines.append("## Citation Slots")
        lines.append("")

        for slot in report["citation_slots"]:
            lines.append(f"### {slot['slot_id']} — {slot['manuscript_area']}")
            lines.append("")
            lines.append(f"- Claim need: {slot['claim_need']}")
            lines.append(f"- Source need type: {slot['source_need_type']}")
            lines.append(f"- Placeholder label: {slot['placeholder_label']}")
            lines.append(f"- Integration action: {slot['integration_action']}")
            lines.append(f"- Current status: {slot['current_status']}")
            lines.append(f"- Forbidden action: {slot['forbidden_action']}")
            lines.append(f"- Boundary note: {slot['boundary_note']}")
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
        lines.append("V8_219_SAFE_ABSTRACT_TOY_CITATION_SLOT_INTEGRATION_PLAN_OK")
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


def build_safe_abstract_toy_citation_slot_integration_plan() -> Dict[str, Any]:
    return SafeAbstractToyCitationSlotIntegrationPlanBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_citation_slot_integration_plan()
    counters = result["counters"]
    print("V8_219_SAFE_ABSTRACT_TOY_CITATION_SLOT_INTEGRATION_PLAN_OK")
    print("TOY_CITATION_SLOT_INTEGRATION_PLAN_DIRECT_CHECK_OK")
    print(f"Citation slot count: {counters['Toy citation slot count']}")
    print(f"Unresolved citation slot count: {counters['Toy citation unresolved slot count']}")
    print(f"Citation slot group count: {counters['Toy citation slot group count']}")
    print(f"Actual citation count: {counters['Toy citation actual citation count']}")
    print(f"Verified source count: {counters['Toy citation verified source count']}")
    print(f"Fabricated reference count: {counters['Toy citation fabricated reference count']}")
    print(f"Source retrieval count: {counters['Toy citation source retrieval count']}")
    print(f"Citation integration completion count: {counters['Toy citation integration completion count']}")
    print(f"Citation added to manuscript count: {counters['Toy citation added to manuscript count']}")
    print(f"Source assembly section count: {counters['Toy citation slot source assembly section count']}")
    print(f"Source gap item count: {counters['Toy citation slot source gap item count']}")
    print(f"Source P0 gap count: {counters['Toy citation slot source P0 gap count']}")
    print(f"Source evaluation design module count: {counters['Toy citation slot source evaluation design module count']}")
    print(f"Source coherence improvement item count: {counters['Toy citation slot source coherence improvement item count']}")
    print(f"Source coherence rewrite application count: {counters['Toy citation slot source coherence rewrite application count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {result['passed']}")
