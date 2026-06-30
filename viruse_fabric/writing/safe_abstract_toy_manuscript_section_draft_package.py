from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyManuscriptSectionDraftPackageBuilder:
    version = "v8.213"

    source_md_path = Path("outputs/safe_abstract_toy_manuscript_claim_language_placement_plan_audit_v8_212.md")
    source_json_path = Path("outputs/safe_abstract_toy_manuscript_claim_language_placement_plan_audit_v8_212.json")

    output_md_path = Path("outputs/safe_abstract_toy_manuscript_section_draft_package_v8_213.md")
    output_json_path = Path("outputs/safe_abstract_toy_manuscript_section_draft_package_v8_213.json")

    package_phrase = "safe_section_drafts_packaged_but_no_manuscript_patch_applied"

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

    def _draft_items(self) -> List[Dict[str, str]]:
        return [
            {
                "id": "SD-01",
                "manuscript_section": "Abstract",
                "draft_role": "bounded contribution sentence",
                "draft_text": (
                    "This work presents an internally audited, safety-bounded, safe abstract toy-only governance "
                    "pipeline for organizing manuscript patch decisions, claim boundaries, safe claim language, "
                    "and planned placement of that language."
                ),
                "usage_boundary": "Use only as a governance contribution statement.",
                "blocked_expansion": "Do not add validation, performance, biological realism, or submission readiness.",
            },
            {
                "id": "SD-02",
                "manuscript_section": "Introduction",
                "draft_role": "problem and contribution framing",
                "draft_text": (
                    "The central contribution is a controlled governance layer for safe abstract toy manuscript "
                    "development: it records decision lineage, separates allowed from deferred and prohibited claims, "
                    "and packages audited wording before any manuscript modification is authorized."
                ),
                "usage_boundary": "Use for framing the contribution without implying empirical success.",
                "blocked_expansion": "Do not claim the framework has been scientifically validated.",
            },
            {
                "id": "SD-03",
                "manuscript_section": "Method Scope",
                "draft_role": "scope limiter",
                "draft_text": (
                    "All artifacts in this lineage are synthetic, abstract, unitless, non-operational, and toy-only. "
                    "The lineage does not import real biological datasets, use real receptor parameters, simulate real pathogens, "
                    "or support operational biological targeting."
                ),
                "usage_boundary": "Use to define the safe abstract toy-only boundary.",
                "blocked_expansion": "Do not add real biological examples, parameters, datasets, or host-targeting language.",
            },
            {
                "id": "SD-04",
                "manuscript_section": "Pipeline Overview",
                "draft_role": "artifact lineage description",
                "draft_text": (
                    "The staged lineage proceeds through proposal, dry-run, structural gate, plan, checklist, audit, "
                    "decision ledger, finding register, consistency audit, claim boundary registration, claim language "
                    "packaging, claim language audit, placement planning, and placement-plan audit."
                ),
                "usage_boundary": "Use as artifact history only.",
                "blocked_expansion": "Do not state that manuscript patches have been applied.",
            },
            {
                "id": "SD-05",
                "manuscript_section": "Safety Controls",
                "draft_role": "zero-counter safety statement",
                "draft_text": (
                    "The internal safety counters preserve zero application permission, zero checklist execution, "
                    "zero applied patches, zero manuscript mutation, zero readiness approval, zero external validation, "
                    "zero proof assistant verification, zero new citation addition, and zero real-biological operational capability."
                ),
                "usage_boundary": "Use as a boundary-control statement, not as scientific evidence.",
                "blocked_expansion": "Do not treat zero counters as validation or proof.",
            },
            {
                "id": "SD-06",
                "manuscript_section": "Claim Governance",
                "draft_role": "allowed/deferred/prohibited claim separation",
                "draft_text": (
                    "The claim governance layer classifies manuscript wording into currently allowed, deferred, "
                    "and prohibited families, preventing governance descriptions from drifting into readiness, validation, "
                    "or real-biological operational claims."
                ),
                "usage_boundary": "Use to explain claim discipline.",
                "blocked_expansion": "Do not present claim classification as approval to submit.",
            },
            {
                "id": "SD-07",
                "manuscript_section": "Limitations",
                "draft_role": "evidence boundary",
                "draft_text": (
                    "The current evidence base does not establish external validation, independent experimental support, "
                    "formal proof, citation-completed claims, applied manuscript patches, or manuscript submission readiness."
                ),
                "usage_boundary": "Use unchanged until future audited evidence exists.",
                "blocked_expansion": "Do not weaken this limitation without a future official evidence-upgrade milestone.",
            },
            {
                "id": "SD-08",
                "manuscript_section": "Safety Exclusions",
                "draft_role": "real-bio non-claim",
                "draft_text": (
                    "The framework does not model real pathogens, real receptors, operational host targeting, "
                    "infectivity optimization, immune evasion, host-range prediction, wet-lab protocols, or actionable "
                    "biosafety-risk procedures."
                ),
                "usage_boundary": "Use as explicit exclusion language.",
                "blocked_expansion": "Do not add operational biological mechanisms or procedures.",
            },
            {
                "id": "SD-09",
                "manuscript_section": "Future Work",
                "draft_role": "conditional evidence-upgrade pathway",
                "draft_text": (
                    "Future work may only introduce stronger claims after separately audited milestones for safe manuscript "
                    "patch application, citation integration, non-operational toy evaluation, proof pathway, or submission "
                    "readiness review."
                ),
                "usage_boundary": "Use to describe conditional future work only.",
                "blocked_expansion": "Do not imply that future milestones have already occurred.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        source = self._load_source_json()
        source_md = self._load_source_md()
        drafts = self._draft_items()

        source_counters = source.get("counters", {})
        source_pass_count = source_counters.get("Toy manuscript claim language placement plan audit pass count")
        source_failure_count = source_counters.get("Toy manuscript claim language placement plan audit failure count")

        counters = {
            "Safe abstract toy manuscript section draft package count": 1,
            "New safe abstract toy manuscript section draft package count": 1,
            "Toy manuscript section draft package JSON export count": 1,
            "Toy manuscript section draft package item count": len(drafts),
            "Toy manuscript section draft package source audit pass count": source_pass_count,
            "Toy manuscript section draft package source audit failure count": source_failure_count,
            "Toy manuscript section draft package execution count": 1,
            "Toy manuscript section draft package direct execution count": 1,
            "Toy manuscript section draft package non-readiness disclaimer count": 1,
            "Toy manuscript section draft package boundary note count": len(drafts),
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
            "title": "Safe Abstract Toy Manuscript Section Draft Package",
            "source_markdown": str(self.source_md_path),
            "source_json": str(self.source_json_path),
            "source_markdown_character_count": len(source_md),
            "package_phrase": self.package_phrase,
            "scope": "section-draft-package-only",
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
                "This v8.213 artifact packages safe section draft text only. It does not complete checklist items, "
                "execute checklist steps, grant application permission, apply manuscript patches, modify manuscript "
                "files, approve readiness, establish submission readiness, validate scientific claims, add citations, "
                "or add real-biological operational capability."
            ),
            "section_draft_items": drafts,
            "boundary_notes": [item["usage_boundary"] for item in drafts],
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "section-draft-package-only":
            raise AssertionError("v8.213 must remain section-draft-package-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.213 section draft package must pass.")

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

        if counters["Toy manuscript section draft package item count"] != 9:
            raise AssertionError("Expected exactly nine section draft items.")

        if counters["Toy manuscript section draft package source audit pass count"] != 10:
            raise AssertionError("Expected source audit pass count of ten.")

        if counters["Toy manuscript section draft package source audit failure count"] != 0:
            raise AssertionError("Expected source audit failure count of zero.")

        required_phrases = [
            "synthetic, abstract, unitless, non-operational",
            "does not import real biological datasets",
            "does not model real pathogens",
            "zero applied patches",
            "does not establish external validation",
            "Future work may only introduce stronger claims",
        ]

        combined = " ".join(item["draft_text"] for item in report["section_draft_items"])
        for phrase in required_phrases:
            if phrase not in combined:
                raise AssertionError(f"Missing required safe phrase: {phrase}")

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

        lines.append("# Safe Abstract Toy Manuscript Section Draft Package")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is section-draft-package-only.")
        lines.append("It packages safe draft text for manuscript sections without applying, authorizing, completing, or executing any manuscript patch workflow.")
        lines.append("")
        lines.append(f"Package phrase: `{report['package_phrase']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")
        lines.append("## Section Draft Items")
        lines.append("")

        for item in report["section_draft_items"]:
            lines.append(f"### {item['id']}")
            lines.append("")
            lines.append(f"- Manuscript section: {item['manuscript_section']}")
            lines.append(f"- Draft role: {item['draft_role']}")
            lines.append(f"- Draft text: {item['draft_text']}")
            lines.append(f"- Usage boundary: {item['usage_boundary']}")
            lines.append(f"- Blocked expansion: {item['blocked_expansion']}")
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
        lines.append("V8_213_SAFE_ABSTRACT_TOY_MANUSCRIPT_SECTION_DRAFT_PACKAGE_OK")
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


def build_safe_abstract_toy_manuscript_section_draft_package() -> Dict[str, Any]:
    return SafeAbstractToyManuscriptSectionDraftPackageBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_manuscript_section_draft_package()
    counters = result["counters"]
    print("V8_213_SAFE_ABSTRACT_TOY_MANUSCRIPT_SECTION_DRAFT_PACKAGE_OK")
    print("TOY_MANUSCRIPT_SECTION_DRAFT_PACKAGE_DIRECT_CHECK_OK")
    print(f"Section draft item count: {counters['Toy manuscript section draft package item count']}")
    print(f"Source audit pass count: {counters['Toy manuscript section draft package source audit pass count']}")
    print(f"Source audit failure count: {counters['Toy manuscript section draft package source audit failure count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"Passed: {result['passed']}")
