from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyScientificGapAndEvidenceUpgradeRegisterBuilder:
    version = "v8.216"

    source_md_path = Path("outputs/safe_abstract_toy_manuscript_assembly_preview_package_v8_215.md")
    source_json_path = Path("outputs/safe_abstract_toy_manuscript_assembly_preview_package_v8_215.json")

    output_md_path = Path("outputs/safe_abstract_toy_scientific_gap_and_evidence_upgrade_register_v8_216.md")
    output_json_path = Path("outputs/safe_abstract_toy_scientific_gap_and_evidence_upgrade_register_v8_216.json")

    register_phrase = "scientific_gaps_registered_but_no_evidence_upgrade_completed"

    def _load_source_json(self) -> Dict[str, Any]:
        if not self.source_json_path.exists():
            raise FileNotFoundError(f"Missing source JSON: {self.source_json_path}")
        payload = json.loads(self.source_json_path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("Source JSON must be a dict.")
        return payload

    def _load_source_md(self) -> str:
        if not self.source_md_path.exists():
            raise FileNotFoundError(f"Missing source markdown: {self.source_md_path}")
        return self.source_md_path.read_text(encoding="utf-8")

    def _gap_items(self) -> List[Dict[str, Any]]:
        return [
            {
                "id": "SG-01",
                "gap_family": "Citation integration",
                "priority": "P0",
                "current_gap": "The manuscript preview has no integrated real citation support.",
                "required_future_milestone": "Create and audit a citation slot integration plan using verified sources before adding citation-supported claims.",
                "blocked_claim_until_resolved": "citation-completed claims",
                "safe_allowed_now": "State only that citation integration remains future work.",
                "evidence_upgrade_completed": False,
                "boundary_note": "No new citation is added by this register.",
            },
            {
                "id": "SG-02",
                "gap_family": "Synthetic toy evaluation design",
                "priority": "P0",
                "current_gap": "The manuscript preview describes governance artifacts but lacks a designed non-operational toy evaluation.",
                "required_future_milestone": "Define a synthetic, abstract, unitless, non-operational toy evaluation design.",
                "blocked_claim_until_resolved": "evaluation-supported internal performance or utility claims",
                "safe_allowed_now": "State only that toy evaluation remains unexecuted.",
                "evidence_upgrade_completed": False,
                "boundary_note": "No real biological data, pathogen simulation, receptor parameter, or host targeting may be introduced.",
            },
            {
                "id": "SG-03",
                "gap_family": "Toy evaluation metrics",
                "priority": "P1",
                "current_gap": "No abstract metrics are yet defined for evaluating lineage consistency, boundary preservation, or overclaim prevention.",
                "required_future_milestone": "Define toy-only metrics for governance lineage completeness, zero-counter preservation, blocked-claim coverage, and section coherence.",
                "blocked_claim_until_resolved": "metric-supported claims",
                "safe_allowed_now": "State only that metrics are planned, not executed.",
                "evidence_upgrade_completed": False,
                "boundary_note": "Metrics must remain abstract and unitless.",
            },
            {
                "id": "SG-04",
                "gap_family": "Coherence and narrative",
                "priority": "P0",
                "current_gap": "The preview is readable but still assembled from section drafts, so narrative flow and reviewer-facing story need sharpening.",
                "required_future_milestone": "Create a manuscript coherence improvement package focused on story, transitions, contribution clarity, and limitation balance.",
                "blocked_claim_until_resolved": "coherent manuscript candidate",
                "safe_allowed_now": "State only that a preview exists, not a polished manuscript.",
                "evidence_upgrade_completed": False,
                "boundary_note": "Coherence work must not soften safety exclusions.",
            },
            {
                "id": "SG-05",
                "gap_family": "Contribution sharpening",
                "priority": "P0",
                "current_gap": "The contribution is safe but still framed broadly as governance; the precise research contribution needs sharper positioning.",
                "required_future_milestone": "Create a contribution sharpening package that distinguishes artifact lineage, claim governance, and manuscript patch control.",
                "blocked_claim_until_resolved": "strong contribution framing",
                "safe_allowed_now": "State only the current safe governance contribution.",
                "evidence_upgrade_completed": False,
                "boundary_note": "Contribution language must not imply validation, proof, readiness, or real-biological applicability.",
            },
            {
                "id": "SG-06",
                "gap_family": "Related work positioning",
                "priority": "P1",
                "current_gap": "The preview lacks a related-work bridge to manuscript governance, safety-bounded workflows, claim control, and evaluation methodology.",
                "required_future_milestone": "Create a related-work slot plan with citation families and no fabricated references.",
                "blocked_claim_until_resolved": "literature-positioned manuscript",
                "safe_allowed_now": "State only that related-work integration is incomplete.",
                "evidence_upgrade_completed": False,
                "boundary_note": "No fake citation or unsupported literature claim may be introduced.",
            },
            {
                "id": "SG-07",
                "gap_family": "Limitations balance",
                "priority": "P1",
                "current_gap": "The limitations are accurate but may dominate the manuscript unless balanced with clear safe contributions.",
                "required_future_milestone": "Create a limitation-balance package that preserves all exclusions while clarifying what the toy governance contribution does provide.",
                "blocked_claim_until_resolved": "reviewer-balanced limitations section",
                "safe_allowed_now": "Keep limitations explicit and unsmoothed.",
                "evidence_upgrade_completed": False,
                "boundary_note": "Limitations may be organized but not weakened.",
            },
            {
                "id": "SG-08",
                "gap_family": "Proof pathway",
                "priority": "P2",
                "current_gap": "No formal proof or proof assistant verification exists.",
                "required_future_milestone": "Create a proof pathway plan for possible future formalization of toy invariants.",
                "blocked_claim_until_resolved": "formally proved claims",
                "safe_allowed_now": "State only that proof assistant verification count remains zero.",
                "evidence_upgrade_completed": False,
                "boundary_note": "No proof claim may be made until a future official proof milestone exists.",
            },
            {
                "id": "SG-09",
                "gap_family": "External validation",
                "priority": "P3",
                "current_gap": "No external validation exists and none should be implied.",
                "required_future_milestone": "Define a future external-review or replication pathway only after toy evaluation and citation integration mature.",
                "blocked_claim_until_resolved": "externally validated claims",
                "safe_allowed_now": "State only that external validation count remains zero.",
                "evidence_upgrade_completed": False,
                "boundary_note": "External validation is not completed or approximated here.",
            },
            {
                "id": "SG-10",
                "gap_family": "Submission readiness",
                "priority": "P0",
                "current_gap": "The project has no submission readiness approval.",
                "required_future_milestone": "Create a future readiness blocker register after citation, toy evaluation, coherence, and contribution sharpening milestones.",
                "blocked_claim_until_resolved": "submission-ready manuscript",
                "safe_allowed_now": "State only that manuscript submission ready count remains zero.",
                "evidence_upgrade_completed": False,
                "boundary_note": "This register does not approve submission readiness.",
            },
            {
                "id": "SG-11",
                "gap_family": "Reproducibility package",
                "priority": "P1",
                "current_gap": "The manuscript preview does not yet include a concise reproducibility description for safe toy artifact generation.",
                "required_future_milestone": "Create a reproducibility description package limited to safe abstract toy artifact generation and validation scripts.",
                "blocked_claim_until_resolved": "reproducible artifact package claim",
                "safe_allowed_now": "State only that reproducibility packaging remains incomplete.",
                "evidence_upgrade_completed": False,
                "boundary_note": "Reproducibility must not include real biological workflows or operational instructions.",
            },
            {
                "id": "SG-12",
                "gap_family": "Manuscript mutation gate",
                "priority": "P0",
                "current_gap": "No manuscript file has been modified and no patch application permission has been granted.",
                "required_future_milestone": "Create a controlled manuscript mutation authorization plan only after the preview, gaps, toy evaluation design, and citation slots are stable.",
                "blocked_claim_until_resolved": "applied manuscript patch claims",
                "safe_allowed_now": "State only that the preview exists and manuscript mutation count remains zero.",
                "evidence_upgrade_completed": False,
                "boundary_note": "This register grants no permission to modify manuscript files.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        source = self._load_source_json()
        source_md = self._load_source_md()
        source_counters = source.get("counters", {})
        gaps = self._gap_items()

        p0_count = sum(1 for item in gaps if item["priority"] == "P0")
        p1_count = sum(1 for item in gaps if item["priority"] == "P1")
        p2_count = sum(1 for item in gaps if item["priority"] == "P2")
        p3_count = sum(1 for item in gaps if item["priority"] == "P3")
        evidence_upgrade_completed_count = sum(1 for item in gaps if item["evidence_upgrade_completed"])

        counters = {
            "Safe abstract toy scientific gap and evidence upgrade register count": 1,
            "New safe abstract toy scientific gap and evidence upgrade register count": 1,
            "Toy scientific gap and evidence upgrade register JSON export count": 1,
            "Toy scientific gap register item count": len(gaps),
            "Toy scientific gap P0 count": p0_count,
            "Toy scientific gap P1 count": p1_count,
            "Toy scientific gap P2 count": p2_count,
            "Toy scientific gap P3 count": p3_count,
            "Toy scientific evidence upgrade completed count": evidence_upgrade_completed_count,
            "Toy scientific gap register source assembly section count": source_counters.get("Toy manuscript assembly preview section count"),
            "Toy scientific gap register source audit pass count": source_counters.get("Toy manuscript assembly preview source audit pass count"),
            "Toy scientific gap register source audit failure count": source_counters.get("Toy manuscript assembly preview source audit failure count"),
            "Toy scientific gap register execution count": 1,
            "Toy scientific gap register direct execution count": 1,
            "Toy scientific gap register non-readiness disclaimer count": 1,
            "Toy scientific gap register boundary note count": len(gaps),
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
            "title": "Safe Abstract Toy Scientific Gap and Evidence Upgrade Register",
            "source_markdown": str(self.source_md_path),
            "source_json": str(self.source_json_path),
            "source_markdown_character_count": len(source_md),
            "register_phrase": self.register_phrase,
            "scope": "scientific-gap-and-evidence-upgrade-register-only",
            "safe_abstract_toy_only": True,
            "synthetic_only": True,
            "abstract_graphs_only": True,
            "unitless_parameters_only": True,
            "non_operational_only": True,
            "application_permission_granted": False,
            "application_execution_performed": False,
            "checklist_completion_performed": False,
            "checklist_execution_performed": False,
            "manuscript_file_modified": False,
            "manuscript_mutation": False,
            "applied_patch_count": 0,
            "evidence_upgrade_completed": False,
            "non_readiness_disclaimer": (
                "This v8.216 artifact registers scientific gaps and future evidence-upgrade requirements only. "
                "It does not complete checklist items, execute checklist steps, grant application permission, apply "
                "manuscript patches, modify manuscript files, approve readiness, establish submission readiness, "
                "validate scientific claims, add citations, complete evidence upgrades, or add real-biological operational capability."
            ),
            "gap_items": gaps,
            "boundary_notes": [item["boundary_note"] for item in gaps],
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "scientific-gap-and-evidence-upgrade-register-only":
            raise AssertionError("v8.216 must remain scientific-gap-and-evidence-upgrade-register-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.216 gap register must pass.")

        for field in [
            "application_permission_granted",
            "application_execution_performed",
            "checklist_completion_performed",
            "checklist_execution_performed",
            "manuscript_file_modified",
            "manuscript_mutation",
            "evidence_upgrade_completed",
        ]:
            if report[field] is not False:
                raise AssertionError(f"Expected False for {field}")

        if report["applied_patch_count"] != 0:
            raise AssertionError("Applied patch count must remain zero.")

        counters = report["counters"]

        if counters["Toy scientific gap register item count"] != 12:
            raise AssertionError("Expected exactly twelve scientific gap items.")

        if counters["Toy scientific gap P0 count"] != 6:
            raise AssertionError("Expected exactly six P0 gaps.")

        if counters["Toy scientific gap P1 count"] != 4:
            raise AssertionError("Expected exactly four P1 gaps.")

        if counters["Toy scientific gap P2 count"] != 1:
            raise AssertionError("Expected exactly one P2 gap.")

        if counters["Toy scientific gap P3 count"] != 1:
            raise AssertionError("Expected exactly one P3 gap.")

        if counters["Toy scientific evidence upgrade completed count"] != 0:
            raise AssertionError("No evidence upgrade may be completed in v8.216.")

        if counters["Toy scientific gap register source assembly section count"] != 9:
            raise AssertionError("Expected source assembly section count of nine.")

        if counters["Toy scientific gap register source audit pass count"] != 11:
            raise AssertionError("Expected source audit pass count of eleven.")

        if counters["Toy scientific gap register source audit failure count"] != 0:
            raise AssertionError("Expected source audit failure count of zero.")

        gap_text = json.dumps(report["gap_items"], ensure_ascii=False)

        required_gap_phrases = [
            "Citation integration",
            "Synthetic toy evaluation design",
            "Toy evaluation metrics",
            "Coherence and narrative",
            "Contribution sharpening",
            "Related work positioning",
            "Limitations balance",
            "Proof pathway",
            "External validation",
            "Submission readiness",
            "Reproducibility package",
            "Manuscript mutation gate",
            "does not approve submission readiness",
            "No new citation is added",
            "No real biological data, pathogen simulation, receptor parameter, or host targeting may be introduced",
        ]

        for phrase in required_gap_phrases:
            if phrase not in gap_text:
                raise AssertionError(f"Missing required gap phrase: {phrase}")

        must_be_zero = [
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

        lines.append("# Safe Abstract Toy Scientific Gap and Evidence Upgrade Register")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is scientific-gap-and-evidence-upgrade-register-only.")
        lines.append("It registers scientific gaps and future evidence-upgrade requirements without completing any evidence upgrade or modifying any manuscript file.")
        lines.append("")
        lines.append(f"Register phrase: `{report['register_phrase']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")
        lines.append("## Gap Items")
        lines.append("")

        for item in report["gap_items"]:
            lines.append(f"### {item['id']} — {item['gap_family']}")
            lines.append("")
            lines.append(f"- Priority: {item['priority']}")
            lines.append(f"- Current gap: {item['current_gap']}")
            lines.append(f"- Required future milestone: {item['required_future_milestone']}")
            lines.append(f"- Blocked claim until resolved: {item['blocked_claim_until_resolved']}")
            lines.append(f"- Safe allowed now: {item['safe_allowed_now']}")
            lines.append(f"- Evidence upgrade completed: {item['evidence_upgrade_completed']}")
            lines.append(f"- Boundary note: {item['boundary_note']}")
            lines.append("")

        lines.append("## Priority Summary")
        lines.append("")
        lines.append(f"- P0 gaps: {report['counters']['Toy scientific gap P0 count']}")
        lines.append(f"- P1 gaps: {report['counters']['Toy scientific gap P1 count']}")
        lines.append(f"- P2 gaps: {report['counters']['Toy scientific gap P2 count']}")
        lines.append(f"- P3 gaps: {report['counters']['Toy scientific gap P3 count']}")
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
        lines.append("V8_216_SAFE_ABSTRACT_TOY_SCIENTIFIC_GAP_AND_EVIDENCE_UPGRADE_REGISTER_OK")
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


def build_safe_abstract_toy_scientific_gap_and_evidence_upgrade_register() -> Dict[str, Any]:
    return SafeAbstractToyScientificGapAndEvidenceUpgradeRegisterBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_scientific_gap_and_evidence_upgrade_register()
    counters = result["counters"]
    print("V8_216_SAFE_ABSTRACT_TOY_SCIENTIFIC_GAP_AND_EVIDENCE_UPGRADE_REGISTER_OK")
    print("TOY_SCIENTIFIC_GAP_AND_EVIDENCE_UPGRADE_REGISTER_DIRECT_CHECK_OK")
    print(f"Gap item count: {counters['Toy scientific gap register item count']}")
    print(f"P0 count: {counters['Toy scientific gap P0 count']}")
    print(f"P1 count: {counters['Toy scientific gap P1 count']}")
    print(f"P2 count: {counters['Toy scientific gap P2 count']}")
    print(f"P3 count: {counters['Toy scientific gap P3 count']}")
    print(f"Evidence upgrade completed count: {counters['Toy scientific evidence upgrade completed count']}")
    print(f"Source assembly section count: {counters['Toy scientific gap register source assembly section count']}")
    print(f"Source audit pass count: {counters['Toy scientific gap register source audit pass count']}")
    print(f"Source audit failure count: {counters['Toy scientific gap register source audit failure count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"Passed: {result['passed']}")
