from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyManuscriptClaimLanguagePackageBuilder:
    version = "v8.209"

    source_md_path = Path("outputs/safe_abstract_toy_manuscript_claim_boundary_register_v8_208.md")
    source_json_path = Path("outputs/safe_abstract_toy_manuscript_claim_boundary_register_v8_208.json")

    output_md_path = Path("outputs/safe_abstract_toy_manuscript_claim_language_package_v8_209.md")
    output_json_path = Path("outputs/safe_abstract_toy_manuscript_claim_language_package_v8_209.json")

    package_phrase = "safe_claim_language_packaged_but_no_readiness_or_real_bio_claims"

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

    def _safe_language_items(self) -> List[Dict[str, str]]:
        return [
            {
                "id": "SL-01",
                "section": "contribution",
                "language": (
                    "This work establishes an internally audited, safety-bounded, safe abstract toy-only "
                    "governance pipeline for organizing manuscript patch decisions and claim boundaries."
                ),
                "use_context": "Contribution paragraph.",
                "boundary_note": "Governance-only claim; no validation or readiness claim.",
            },
            {
                "id": "SL-02",
                "section": "method_scope",
                "language": (
                    "The pipeline operates only on synthetic, abstract, unitless, non-operational toy artifacts."
                ),
                "use_context": "Scope or methods boundary paragraph.",
                "boundary_note": "Explicitly excludes real-biological operation.",
            },
            {
                "id": "SL-03",
                "section": "artifact_lineage",
                "language": (
                    "The staged artifact lineage includes proposal, dry-run, structural gate, plan, checklist, "
                    "audit, decision ledger, finding register, consistency audit, and claim boundary registration."
                ),
                "use_context": "Pipeline overview.",
                "boundary_note": "Lineage description only; no patch application claim.",
            },
            {
                "id": "SL-04",
                "section": "safety_controls",
                "language": (
                    "Internal counters preserve zero application permission, zero applied patches, zero manuscript "
                    "mutation, zero readiness approval, and zero real-biological operational capability."
                ),
                "use_context": "Safety-control paragraph.",
                "boundary_note": "Safety-boundary claim only.",
            },
            {
                "id": "SL-05",
                "section": "claim_governance",
                "language": (
                    "The claim boundary register separates currently allowed manuscript wording from deferred "
                    "and prohibited claims."
                ),
                "use_context": "Claim governance paragraph.",
                "boundary_note": "Claim classification is not submission approval.",
            },
            {
                "id": "SL-06",
                "section": "limitations",
                "language": (
                    "The current evidence base does not establish external validation, independent experimental "
                    "support, proof assistant verification, citation-completed claims, or manuscript submission readiness."
                ),
                "use_context": "Limitations paragraph.",
                "boundary_note": "Keeps validation/proof/citation/readiness at zero.",
            },
            {
                "id": "SL-07",
                "section": "non_claims",
                "language": (
                    "The framework does not model real pathogens, real receptors, operational host targeting, "
                    "infectivity optimization, immune evasion, or host-range prediction."
                ),
                "use_context": "Safety exclusion paragraph.",
                "boundary_note": "Explicit prohibited real-biological claim exclusion.",
            },
            {
                "id": "SL-08",
                "section": "future_work",
                "language": (
                    "Future work must separately audit any safe manuscript patch application, citation integration, "
                    "toy evaluation, proof pathway, or submission readiness upgrade before stronger claims are introduced."
                ),
                "use_context": "Future work paragraph.",
                "boundary_note": "Future evidence requirement only.",
            },
        ]

    def _blocked_language_items(self) -> List[Dict[str, str]]:
        return [
            {"id": "BL-01", "blocked_language": "The manuscript is ready for submission.", "reason": "Readiness approval and manuscript submission ready counters remain zero."},
            {"id": "BL-02", "blocked_language": "The method has been externally validated.", "reason": "External validation count remains zero."},
            {"id": "BL-03", "blocked_language": "The framework has been independently experimentally verified.", "reason": "Independent experiment count remains zero."},
            {"id": "BL-04", "blocked_language": "The method is formally proved.", "reason": "Proof assistant verification count remains zero."},
            {"id": "BL-05", "blocked_language": "The manuscript includes new citation-supported claims.", "reason": "New citation added count remains zero."},
            {"id": "BL-06", "blocked_language": "The manuscript patches have been applied.", "reason": "Applied patch and manuscript mutation counters remain zero."},
            {"id": "BL-07", "blocked_language": "The framework models real pathogens or real receptors.", "reason": "Real biological dataset, pathogen simulation, and receptor parameter counters remain zero."},
            {"id": "BL-08", "blocked_language": "The framework predicts host range or operational host targeting.", "reason": "Operational host targeting and real host range prediction counters remain zero."},
            {"id": "BL-09", "blocked_language": "The framework optimizes infectivity or immune evasion.", "reason": "Real-world infectivity optimization and immune evasion optimization counters remain zero."},
        ]

    def build(self) -> Dict[str, Any]:
        source = self._load_source_json()
        source_md = self._load_source_md()

        safe_items = self._safe_language_items()
        blocked_items = self._blocked_language_items()
        source_counters = source.get("counters", {})

        counters = {
            "Safe abstract toy manuscript claim language package count": 1,
            "New safe abstract toy manuscript claim language package count": 1,
            "Toy manuscript claim language package JSON export count": 1,
            "Toy manuscript claim language package safe language item count": len(safe_items),
            "Toy manuscript claim language package blocked language item count": len(blocked_items),
            "Toy manuscript claim language package source allowed claim count": source_counters.get("Toy manuscript claim boundary register allowed claim count"),
            "Toy manuscript claim language package source deferred claim count": source_counters.get("Toy manuscript claim boundary register deferred claim count"),
            "Toy manuscript claim language package source prohibited claim count": source_counters.get("Toy manuscript claim boundary register prohibited claim count"),
            "Toy manuscript claim language package execution count": 1,
            "Toy manuscript claim language package direct execution count": 1,
            "Toy manuscript claim language package non-readiness disclaimer count": 1,
            "Toy manuscript claim language package boundary note count": len(safe_items),
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
            "title": "Safe Abstract Toy Manuscript Claim Language Package",
            "source_markdown": str(self.source_md_path),
            "source_json": str(self.source_json_path),
            "source_markdown_character_count": len(source_md),
            "package_phrase": self.package_phrase,
            "scope": "claim-language-package-only",
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
                "This v8.209 artifact packages safe manuscript claim language only. It does not complete "
                "checklist items, execute checklist steps, grant application permission, apply manuscript patches, "
                "modify manuscript files, approve readiness, establish submission readiness, validate scientific "
                "claims, add citations, or add real-biological operational capability."
            ),
            "safe_language_items": safe_items,
            "blocked_language_items": blocked_items,
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "claim-language-package-only":
            raise AssertionError("v8.209 must remain claim-language-package-only.")
        if report["passed"] is not True:
            raise AssertionError("v8.209 claim language package must pass.")

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

        expected_nonzero = {
            "Toy manuscript claim language package safe language item count": 8,
            "Toy manuscript claim language package blocked language item count": 9,
            "Toy manuscript claim language package source allowed claim count": 4,
            "Toy manuscript claim language package source deferred claim count": 3,
            "Toy manuscript claim language package source prohibited claim count": 2,
        }

        for key, expected in expected_nonzero.items():
            if counters.get(key) != expected:
                raise AssertionError(f"Expected {expected} for {key}, got {counters.get(key)}")

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

        lines.append("# Safe Abstract Toy Manuscript Claim Language Package")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is claim-language-package-only.")
        lines.append("It packages safe manuscript wording derived from the v8.208 claim boundary register without applying, authorizing, completing, or executing any manuscript patch workflow.")
        lines.append("")
        lines.append(f"Package phrase: `{report['package_phrase']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")
        lines.append("## Safe Language Items")
        lines.append("")

        for item in report["safe_language_items"]:
            lines.append(f"### {item['id']}")
            lines.append("")
            lines.append(f"- Section: `{item['section']}`")
            lines.append(f"- Language: {item['language']}")
            lines.append(f"- Use context: {item['use_context']}")
            lines.append(f"- Boundary note: {item['boundary_note']}")
            lines.append("")

        lines.append("## Blocked Language Items")
        lines.append("")

        for item in report["blocked_language_items"]:
            lines.append(f"### {item['id']}")
            lines.append("")
            lines.append(f"- Blocked language: {item['blocked_language']}")
            lines.append(f"- Reason: {item['reason']}")
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
        lines.append("V8_209_SAFE_ABSTRACT_TOY_MANUSCRIPT_CLAIM_LANGUAGE_PACKAGE_OK")
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


def build_safe_abstract_toy_manuscript_claim_language_package() -> Dict[str, Any]:
    return SafeAbstractToyManuscriptClaimLanguagePackageBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_manuscript_claim_language_package()
    counters = result["counters"]
    print("V8_209_SAFE_ABSTRACT_TOY_MANUSCRIPT_CLAIM_LANGUAGE_PACKAGE_OK")
    print("TOY_MANUSCRIPT_CLAIM_LANGUAGE_PACKAGE_DIRECT_CHECK_OK")
    print(f"Safe language item count: {counters['Toy manuscript claim language package safe language item count']}")
    print(f"Blocked language item count: {counters['Toy manuscript claim language package blocked language item count']}")
    print(f"Source allowed claim count: {counters['Toy manuscript claim language package source allowed claim count']}")
    print(f"Source deferred claim count: {counters['Toy manuscript claim language package source deferred claim count']}")
    print(f"Source prohibited claim count: {counters['Toy manuscript claim language package source prohibited claim count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"Passed: {result['passed']}")
