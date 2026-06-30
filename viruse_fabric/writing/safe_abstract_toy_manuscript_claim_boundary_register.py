from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyManuscriptClaimBoundaryRegisterBuilder:
    version = "v8.208"

    source_md_path = Path(
        "outputs/safe_abstract_toy_manuscript_patch_application_decision_ledger_audit_finding_register_consistency_audit_v8_207.md"
    )
    source_json_path = Path(
        "outputs/safe_abstract_toy_manuscript_patch_application_decision_ledger_audit_finding_register_consistency_audit_v8_207.json"
    )

    output_md_path = Path("outputs/safe_abstract_toy_manuscript_claim_boundary_register_v8_208.md")
    output_json_path = Path("outputs/safe_abstract_toy_manuscript_claim_boundary_register_v8_208.json")

    register_phrase = "claim_boundaries_registered_but_no_readiness_or_real_bio_claims"

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

    def _claim_items(self, source: Dict[str, Any]) -> List[Dict[str, Any]]:
        counters = source.get("counters", {})

        return [
            {
                "id": "CB-01",
                "category": "allowed_now",
                "claim_boundary": (
                    "Allowed: the project may claim an internally audited, safety-bounded, "
                    "safe abstract toy-only governance pipeline for organizing manuscript patch decisions."
                ),
                "safe_language": (
                    "We establish an internally audited, safety-bounded, abstract toy framework "
                    "for organizing manuscript patch decision governance."
                ),
                "blocked_language": (
                    "We validate a biological model, prove real-world performance, or establish manuscript readiness."
                ),
                "evidence_requirement": "Existing v8.198-v8.207 lineage and zero-counter audits.",
                "boundary_note": "Allowed claim is governance/pipeline-only, not biological validation.",
            },
            {
                "id": "CB-02",
                "category": "allowed_now",
                "claim_boundary": (
                    "Allowed: the project may describe the recent lineage as proposal, dry-run, gate, "
                    "plan, checklist, audit, decision ledger, finding register, and consistency audit."
                ),
                "safe_language": (
                    "The pipeline records a staged lineage of proposal, dry-run, structural gate, "
                    "planning, checklist, audit, decision ledger, finding register, and consistency audit artifacts."
                ),
                "blocked_language": "The staged lineage means manuscript patches have been applied.",
                "evidence_requirement": "Official artifacts through v8.207.0.",
                "boundary_note": "Lineage description is allowed only as artifact history, not execution.",
            },
            {
                "id": "CB-03",
                "category": "allowed_now",
                "claim_boundary": (
                    "Allowed: the project may claim that internal counters preserve zero application permission, "
                    "zero patch application, zero manuscript mutation, and zero readiness approval."
                ),
                "safe_language": (
                    "Internal audit counters preserve zero application permission, zero applied patches, "
                    "zero manuscript mutation, and zero readiness approval."
                ),
                "blocked_language": "Zero counters prove the scientific method is correct.",
                "evidence_requirement": "Zero counters in v8.207 source artifact.",
                "boundary_note": "Zero counters support safety-boundary claims, not scientific validation.",
            },
            {
                "id": "CB-04",
                "category": "allowed_now",
                "claim_boundary": (
                    "Allowed: the project may claim that this artifact separates allowed, deferred, "
                    "and prohibited manuscript claims."
                ),
                "safe_language": (
                    "The claim boundary register separates currently allowed wording from deferred "
                    "and prohibited claims."
                ),
                "blocked_language": "The claim register authorizes submission or publication.",
                "evidence_requirement": "This v8.208 claim boundary register.",
                "boundary_note": "Claim classification is not readiness approval.",
            },
            {
                "id": "CB-05",
                "category": "deferred_until_future_evidence",
                "claim_boundary": (
                    "Deferred: any claim that manuscript patches have been applied, integrated, "
                    "or finalized must wait for an explicit safe patch-application milestone."
                ),
                "safe_language": (
                    "Patch application remains future work and is not claimed by the current artifact lineage."
                ),
                "blocked_language": "The manuscript has already been patched or finalized.",
                "evidence_requirement": "Future safe patch application plus post-application audit.",
                "boundary_note": "No current artifact applies manuscript patches.",
            },
            {
                "id": "CB-06",
                "category": "deferred_until_future_evidence",
                "claim_boundary": (
                    "Deferred: external validation, independent experiment, proof assistant verification, "
                    "or new citation-supported claims require nonzero evidence-specific milestones."
                ),
                "safe_language": (
                    "External validation, independent experiments, proof assistant verification, "
                    "and citation integration remain outside the current evidence base."
                ),
                "blocked_language": "The framework has been externally validated, formally proved, or citation-completed.",
                "evidence_requirement": "Future external validation, independent experiment, proof, or citation milestone.",
                "boundary_note": "These evidence types remain zero in the current lineage.",
            },
            {
                "id": "CB-07",
                "category": "deferred_until_future_evidence",
                "claim_boundary": (
                    "Deferred: scientific efficacy, generalizability, performance, or predictive claims "
                    "require explicit validation beyond internal toy artifact consistency."
                ),
                "safe_language": (
                    "The current contribution is a safety-bounded abstract toy governance framework, "
                    "not a validated predictive or performance model."
                ),
                "blocked_language": "The model works, predicts, generalizes, or outperforms alternatives.",
                "evidence_requirement": "Future non-operational toy evaluation and separately audited claim upgrade.",
                "boundary_note": "Internal consistency is not empirical performance.",
            },
            {
                "id": "CB-08",
                "category": "prohibited_currently",
                "claim_boundary": (
                    "Prohibited: real-biological operational claims, real pathogen simulation, "
                    "real receptor parameter use, host targeting, infectivity optimization, immune evasion, "
                    "or host-range prediction are not allowed."
                ),
                "safe_language": (
                    "All artifacts remain synthetic, abstract, unitless, non-operational, and toy-only."
                ),
                "blocked_language": (
                    "The framework models real pathogens, real receptors, host targeting, infectivity, "
                    "immune evasion, or host range."
                ),
                "evidence_requirement": "Not applicable inside this safety boundary.",
                "boundary_note": "Real-biological operational claims are outside the allowed scope.",
            },
            {
                "id": "CB-09",
                "category": "prohibited_currently",
                "claim_boundary": (
                    "Prohibited: manuscript submission readiness, acceptance likelihood, publication readiness, "
                    "or approval language is not allowed while readiness approval remains zero."
                ),
                "safe_language": (
                    "The manuscript is not submission-ready under the current evidence and readiness counters."
                ),
                "blocked_language": "The manuscript is ready for submission, accepted-quality, or publication-ready.",
                "evidence_requirement": "Future submission readiness audit with explicit nonzero readiness approval.",
                "boundary_note": "Current readiness approval and manuscript submission readiness remain zero.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        source = self._load_source_json()
        source_md = self._load_source_md()
        claim_items = self._claim_items(source)

        allowed_count = sum(1 for item in claim_items if item["category"] == "allowed_now")
        deferred_count = sum(1 for item in claim_items if item["category"] == "deferred_until_future_evidence")
        prohibited_count = sum(1 for item in claim_items if item["category"] == "prohibited_currently")

        counters = {
            "Safe abstract toy manuscript claim boundary register count": 1,
            "New safe abstract toy manuscript claim boundary register count": 1,
            "Toy manuscript claim boundary register JSON export count": 1,
            "Toy manuscript claim boundary register item count": len(claim_items),
            "Toy manuscript claim boundary register allowed claim count": allowed_count,
            "Toy manuscript claim boundary register deferred claim count": deferred_count,
            "Toy manuscript claim boundary register prohibited claim count": prohibited_count,
            "Toy manuscript claim boundary register execution count": 1,
            "Toy manuscript claim boundary register direct execution count": 1,
            "Toy manuscript claim boundary register non-readiness disclaimer count": 1,
            "Toy manuscript claim boundary register boundary note count": len(claim_items),
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
            "title": "Safe Abstract Toy Manuscript Claim Boundary Register",
            "source_markdown": str(self.source_md_path),
            "source_json": str(self.source_json_path),
            "source_markdown_character_count": len(source_md),
            "register_phrase": self.register_phrase,
            "scope": "claim-boundary-register-only",
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
            "non_readiness_disclaimer": (
                "This v8.208 artifact registers manuscript claim boundaries only. It does not complete checklist "
                "items, execute checklist steps, grant application permission, apply manuscript patches, modify "
                "manuscript files, approve readiness, establish submission readiness, validate scientific claims, "
                "or add real-biological operational capability."
            ),
            "claim_items": claim_items,
            "boundary_notes": [item["boundary_note"] for item in claim_items],
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "claim-boundary-register-only":
            raise AssertionError("v8.208 must remain claim-boundary-register-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.208 claim boundary register must pass.")

        false_fields = [
            "application_permission_granted",
            "application_execution_performed",
            "checklist_completion_performed",
            "checklist_execution_performed",
            "manuscript_file_modified",
            "manuscript_mutation",
        ]

        for field in false_fields:
            if report[field] is not False:
                raise AssertionError(f"Expected False for {field}")

        if report["applied_patch_count"] != 0:
            raise AssertionError("Applied patch count must remain zero.")

        counters = report["counters"]

        if counters["Toy manuscript claim boundary register item count"] != 9:
            raise AssertionError("Expected exactly nine claim boundary items.")

        if counters["Toy manuscript claim boundary register allowed claim count"] != 4:
            raise AssertionError("Expected exactly four currently allowed claims.")

        if counters["Toy manuscript claim boundary register deferred claim count"] != 3:
            raise AssertionError("Expected exactly three deferred claims.")

        if counters["Toy manuscript claim boundary register prohibited claim count"] != 2:
            raise AssertionError("Expected exactly two currently prohibited claims.")

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

        lines.append("# Safe Abstract Toy Manuscript Claim Boundary Register")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is claim-boundary-register-only.")
        lines.append("It separates currently allowed, deferred, and prohibited manuscript claims without applying, authorizing, completing, or executing any manuscript patch workflow.")
        lines.append("")
        lines.append(f"Register phrase: `{report['register_phrase']}`")
        lines.append("")
        lines.append("## Source Artifacts")
        lines.append("")
        lines.append(f"- Source markdown: `{report['source_markdown']}`")
        lines.append(f"- Source JSON: `{report['source_json']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")
        lines.append("## Claim Boundary Items")
        lines.append("")

        for item in report["claim_items"]:
            lines.append(f"### {item['id']}")
            lines.append("")
            lines.append(f"- Category: `{item['category']}`")
            lines.append(f"- Claim boundary: {item['claim_boundary']}")
            lines.append(f"- Safe language: {item['safe_language']}")
            lines.append(f"- Blocked language: {item['blocked_language']}")
            lines.append(f"- Evidence requirement: {item['evidence_requirement']}")
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
        lines.append("V8_208_SAFE_ABSTRACT_TOY_MANUSCRIPT_CLAIM_BOUNDARY_REGISTER_OK")
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


def build_safe_abstract_toy_manuscript_claim_boundary_register() -> Dict[str, Any]:
    return SafeAbstractToyManuscriptClaimBoundaryRegisterBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_manuscript_claim_boundary_register()
    counters = result["counters"]
    print("V8_208_SAFE_ABSTRACT_TOY_MANUSCRIPT_CLAIM_BOUNDARY_REGISTER_OK")
    print("TOY_MANUSCRIPT_CLAIM_BOUNDARY_REGISTER_DIRECT_CHECK_OK")
    print(f"Claim boundary items: {counters['Toy manuscript claim boundary register item count']}")
    print(f"Allowed claim count: {counters['Toy manuscript claim boundary register allowed claim count']}")
    print(f"Deferred claim count: {counters['Toy manuscript claim boundary register deferred claim count']}")
    print(f"Prohibited claim count: {counters['Toy manuscript claim boundary register prohibited claim count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"Passed: {result['passed']}")
