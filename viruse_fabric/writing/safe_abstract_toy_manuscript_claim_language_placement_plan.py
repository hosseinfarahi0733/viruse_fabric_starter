from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyManuscriptClaimLanguagePlacementPlanBuilder:
    version = "v8.211"

    source_md_path = Path("outputs/safe_abstract_toy_manuscript_claim_language_package_audit_v8_210.md")
    source_json_path = Path("outputs/safe_abstract_toy_manuscript_claim_language_package_audit_v8_210.json")

    output_md_path = Path("outputs/safe_abstract_toy_manuscript_claim_language_placement_plan_v8_211.md")
    output_json_path = Path("outputs/safe_abstract_toy_manuscript_claim_language_placement_plan_v8_211.json")

    plan_phrase = "safe_claim_language_placement_planned_but_no_manuscript_patch_applied"

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

    def _placement_items(self) -> List[Dict[str, str]]:
        return [
            {
                "id": "PL-01",
                "manuscript_section": "Abstract",
                "placement_role": "one-sentence contribution boundary",
                "safe_language": (
                    "This work establishes an internally audited, safety-bounded, safe abstract toy-only "
                    "governance pipeline for organizing manuscript patch decisions and claim boundaries."
                ),
                "blocked_expansion": "Do not claim validation, performance, biological realism, or submission readiness.",
                "boundary_note": "Abstract placement must remain governance-only.",
            },
            {
                "id": "PL-02",
                "manuscript_section": "Introduction",
                "placement_role": "problem framing and contribution scope",
                "safe_language": (
                    "The contribution is limited to safe abstract toy governance of manuscript patch decisions, "
                    "claim boundaries, and safe claim language."
                ),
                "blocked_expansion": "Do not convert the governance contribution into a scientific efficacy claim.",
                "boundary_note": "Introduction wording must not imply empirical proof.",
            },
            {
                "id": "PL-03",
                "manuscript_section": "Method Scope",
                "placement_role": "scope limiter",
                "safe_language": (
                    "The pipeline operates only on synthetic, abstract, unitless, non-operational toy artifacts."
                ),
                "blocked_expansion": "Do not mention real biological datasets, real receptors, pathogens, or host targeting.",
                "boundary_note": "Method scope must explicitly exclude real-biological operation.",
            },
            {
                "id": "PL-04",
                "manuscript_section": "Pipeline Overview",
                "placement_role": "artifact lineage description",
                "safe_language": (
                    "The staged artifact lineage includes proposal, dry-run, structural gate, plan, checklist, "
                    "audit, decision ledger, finding register, consistency audit, claim boundary registration, "
                    "claim language packaging, and claim language audit."
                ),
                "blocked_expansion": "Do not state that manuscript patches have been applied.",
                "boundary_note": "Lineage placement is descriptive only.",
            },
            {
                "id": "PL-05",
                "manuscript_section": "Safety Controls",
                "placement_role": "zero-counter safety statement",
                "safe_language": (
                    "Internal counters preserve zero application permission, zero applied patches, zero manuscript "
                    "mutation, zero readiness approval, and zero real-biological operational capability."
                ),
                "blocked_expansion": "Do not treat zero counters as scientific validation.",
                "boundary_note": "Safety counters support boundary control only.",
            },
            {
                "id": "PL-06",
                "manuscript_section": "Claim Governance",
                "placement_role": "allowed/deferred/prohibited claim separation",
                "safe_language": (
                    "The claim governance layer separates currently allowed manuscript wording from deferred "
                    "and prohibited claims."
                ),
                "blocked_expansion": "Do not present claim classification as submission approval.",
                "boundary_note": "Claim governance is not readiness certification.",
            },
            {
                "id": "PL-07",
                "manuscript_section": "Limitations",
                "placement_role": "evidence boundary",
                "safe_language": (
                    "The current evidence base does not establish external validation, independent experimental "
                    "support, proof assistant verification, citation-completed claims, or manuscript submission readiness."
                ),
                "blocked_expansion": "Do not soften or remove this limitation until audited evidence exists.",
                "boundary_note": "Limitations must preserve all zero evidence-upgrade counters.",
            },
            {
                "id": "PL-08",
                "manuscript_section": "Safety Exclusions",
                "placement_role": "real-bio non-claim",
                "safe_language": (
                    "The framework does not model real pathogens, real receptors, operational host targeting, "
                    "infectivity optimization, immune evasion, or host-range prediction."
                ),
                "blocked_expansion": "Do not add operational biological examples or parameters.",
                "boundary_note": "Safety exclusions must remain explicit.",
            },
            {
                "id": "PL-09",
                "manuscript_section": "Future Work",
                "placement_role": "evidence upgrade pathway",
                "safe_language": (
                    "Future work must separately audit any safe manuscript patch application, citation integration, "
                    "toy evaluation, proof pathway, or submission readiness upgrade before stronger claims are introduced."
                ),
                "blocked_expansion": "Do not imply those future milestones have already occurred.",
                "boundary_note": "Future work is conditional, not accomplished.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        source = self._load_source_json()
        source_md = self._load_source_md()
        placements = self._placement_items()

        source_counters = source.get("counters", {})
        source_pass_count = source_counters.get("Toy manuscript claim language package audit pass count")
        source_failure_count = source_counters.get("Toy manuscript claim language package audit failure count")

        counters = {
            "Safe abstract toy manuscript claim language placement plan count": 1,
            "New safe abstract toy manuscript claim language placement plan count": 1,
            "Toy manuscript claim language placement plan JSON export count": 1,
            "Toy manuscript claim language placement plan item count": len(placements),
            "Toy manuscript claim language placement plan source audit pass count": source_pass_count,
            "Toy manuscript claim language placement plan source audit failure count": source_failure_count,
            "Toy manuscript claim language placement plan execution count": 1,
            "Toy manuscript claim language placement plan direct execution count": 1,
            "Toy manuscript claim language placement plan non-readiness disclaimer count": 1,
            "Toy manuscript claim language placement plan boundary note count": len(placements),
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
            "title": "Safe Abstract Toy Manuscript Claim Language Placement Plan",
            "source_markdown": str(self.source_md_path),
            "source_json": str(self.source_json_path),
            "source_markdown_character_count": len(source_md),
            "plan_phrase": self.plan_phrase,
            "scope": "claim-language-placement-plan-only",
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
                "This v8.211 artifact plans safe placement of audited claim language only. It does not complete "
                "checklist items, execute checklist steps, grant application permission, apply manuscript patches, "
                "modify manuscript files, approve readiness, establish submission readiness, validate scientific "
                "claims, add citations, or add real-biological operational capability."
            ),
            "placement_items": placements,
            "boundary_notes": [item["boundary_note"] for item in placements],
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "claim-language-placement-plan-only":
            raise AssertionError("v8.211 must remain claim-language-placement-plan-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.211 placement plan must pass.")

        for field in [
            "application_permission_granted",
            "application_execution_performed",
            "checklist_completion_performed",
            "checklist_execution_performed",
            "manuscript_file_modified",
            "manuscript_mutation",
        ]:
            if report[field] is not False:
                raise AssertionError(f"Expected False for {field}")

        if report["applied_patch_count"] != 0:
            raise AssertionError("Applied patch count must remain zero.")

        counters = report["counters"]

        if counters["Toy manuscript claim language placement plan item count"] != 9:
            raise AssertionError("Expected exactly nine placement items.")

        if counters["Toy manuscript claim language placement plan source audit pass count"] != 10:
            raise AssertionError("Expected source audit pass count of ten.")

        if counters["Toy manuscript claim language placement plan source audit failure count"] != 0:
            raise AssertionError("Expected source audit failure count of zero.")

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

        lines.append("# Safe Abstract Toy Manuscript Claim Language Placement Plan")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is claim-language-placement-plan-only.")
        lines.append("It plans where audited safe claim language may be placed in a manuscript without applying, authorizing, completing, or executing any manuscript patch workflow.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")
        lines.append("## Placement Items")
        lines.append("")

        for item in report["placement_items"]:
            lines.append(f"### {item['id']}")
            lines.append("")
            lines.append(f"- Manuscript section: {item['manuscript_section']}")
            lines.append(f"- Placement role: {item['placement_role']}")
            lines.append(f"- Safe language: {item['safe_language']}")
            lines.append(f"- Blocked expansion: {item['blocked_expansion']}")
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
        lines.append("V8_211_SAFE_ABSTRACT_TOY_MANUSCRIPT_CLAIM_LANGUAGE_PLACEMENT_PLAN_OK")
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


def build_safe_abstract_toy_manuscript_claim_language_placement_plan() -> Dict[str, Any]:
    return SafeAbstractToyManuscriptClaimLanguagePlacementPlanBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_manuscript_claim_language_placement_plan()
    counters = result["counters"]
    print("V8_211_SAFE_ABSTRACT_TOY_MANUSCRIPT_CLAIM_LANGUAGE_PLACEMENT_PLAN_OK")
    print("TOY_MANUSCRIPT_CLAIM_LANGUAGE_PLACEMENT_PLAN_DIRECT_CHECK_OK")
    print(f"Placement item count: {counters['Toy manuscript claim language placement plan item count']}")
    print(f"Source audit pass count: {counters['Toy manuscript claim language placement plan source audit pass count']}")
    print(f"Source audit failure count: {counters['Toy manuscript claim language placement plan source audit failure count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"Passed: {result['passed']}")
