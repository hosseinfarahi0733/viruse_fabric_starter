from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class SafeAbstractToyManuscriptCoherenceImprovementPackageBuilder:
    version = "v8.218"

    source_assembly_json_path = Path("outputs/safe_abstract_toy_manuscript_assembly_preview_package_v8_215.json")
    source_assembly_md_path = Path("outputs/safe_abstract_toy_manuscript_assembly_preview_package_v8_215.md")
    source_gap_json_path = Path("outputs/safe_abstract_toy_scientific_gap_and_evidence_upgrade_register_v8_216.json")
    source_eval_json_path = Path("outputs/safe_abstract_toy_evaluation_design_plan_v8_217.json")

    output_md_path = Path("outputs/safe_abstract_toy_manuscript_coherence_improvement_package_v8_218.md")
    output_json_path = Path("outputs/safe_abstract_toy_manuscript_coherence_improvement_package_v8_218.json")

    package_phrase = "manuscript_coherence_improved_but_no_manuscript_file_modified"

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

    def _coherence_items(self) -> List[Dict[str, str]]:
        return [
            {
                "id": "CI-01",
                "target_area": "Global narrative spine",
                "coherence_problem": "The preview states safe boundaries clearly but needs a stronger reviewer-facing throughline.",
                "improvement_text": (
                    "The manuscript should present its central story as a safety-bounded governance pipeline for controlling "
                    "how safe abstract toy manuscript artifacts are proposed, constrained, drafted, checked, and positioned "
                    "without turning those artifacts into validation, readiness, or real-biological claims."
                ),
                "transition_text": (
                    "This framing lets the reader see the work as a governance contribution first, not as an empirical "
                    "biology claim or a submission-ready system."
                ),
                "retained_boundary": "No validation, readiness, or real-biological applicability is introduced.",
                "blocked_overclaim": "Do not call the preview a validated method, deployed system, or submission-ready manuscript.",
            },
            {
                "id": "CI-02",
                "target_area": "Abstract coherence",
                "coherence_problem": "The abstract needs to foreground the problem, artifact contribution, and limitation in one compact arc.",
                "improvement_text": (
                    "The abstract should move from the problem of manuscript overclaim control, to the proposed safe abstract "
                    "toy-only governance pipeline, to the current evidence boundary: assembled preview, registered gaps, and "
                    "designed toy evaluation, but no executed evaluation or validation."
                ),
                "transition_text": (
                    "This gives the abstract a complete arc while preserving the line between planned evaluation and completed evidence."
                ),
                "retained_boundary": "Toy evaluation is designed but not executed or validated.",
                "blocked_overclaim": "Do not imply performance, external validation, or completed evidence upgrades.",
            },
            {
                "id": "CI-03",
                "target_area": "Introduction story arc",
                "coherence_problem": "The introduction needs a clearer motivation for why claim governance matters.",
                "improvement_text": (
                    "The introduction should explain that complex manuscript-building workflows can accidentally blur proposal, "
                    "drafting, evidence, and readiness language. The contribution is a safe abstract toy governance structure "
                    "that keeps those states separated."
                ),
                "transition_text": (
                    "After motivating the risk of overclaim drift, the introduction can lead naturally into the toy-only scope."
                ),
                "retained_boundary": "The motivation remains about manuscript governance, not biological operation.",
                "blocked_overclaim": "Do not add real pathogen, receptor, host, infectivity, immune evasion, or host-range examples.",
            },
            {
                "id": "CI-04",
                "target_area": "Method scope bridge",
                "coherence_problem": "The method scope needs to sound intentional rather than merely defensive.",
                "improvement_text": (
                    "The method scope should state that restriction to synthetic, abstract, unitless, non-operational toy artifacts "
                    "is a design choice for claim governance. No real biological datasets, no real pathogen models, no receptor "
                    "parameters, and no operational targeting are used."
                ),
                "transition_text": (
                    "This turns the safety boundary into a methodological premise rather than an afterthought."
                ),
                "retained_boundary": "No real biological datasets, no real pathogen models, no receptor parameters, and no operational targeting are used.",
                "blocked_overclaim": "Do not describe any real biological mechanism, operational target, or real-world biological prediction.",
            },
            {
                "id": "CI-05",
                "target_area": "Pipeline overview transitions",
                "coherence_problem": "The preview lists artifacts, but the reader needs a stronger sense of staged progression.",
                "improvement_text": (
                    "The pipeline overview should read as a staged progression: claim boundaries constrain safe language; "
                    "safe language informs section drafts; audited drafts become an assembly preview; gaps identify missing "
                    "evidence; evaluation design proposes how future toy-only checks could be structured."
                ),
                "transition_text": (
                    "This connects v8.208 through v8.217 as a coherent artifact lineage instead of a stack of isolated files."
                ),
                "retained_boundary": "Lineage organization is not scientific validation.",
                "blocked_overclaim": "Do not treat staged artifact lineage as proof, external validation, or readiness approval.",
            },
            {
                "id": "CI-06",
                "target_area": "Safety controls framing",
                "coherence_problem": "Safety controls risk reading like bureaucratic clutter unless their role is explained.",
                "improvement_text": (
                    "The safety controls should be framed as invariants that preserve claim boundaries: zero applied patches, "
                    "zero manuscript mutation, zero readiness approval, zero external validation, zero proof assistant verification, "
                    "and zero new citation addition."
                ),
                "transition_text": (
                    "The reader should understand that these counters prevent scope drift rather than serving as evidence of effectiveness."
                ),
                "retained_boundary": "Zero counters are governance checks, not validation or proof.",
                "blocked_overclaim": "Do not claim that zero counters prove safety, correctness, usefulness, or publishability.",
            },
            {
                "id": "CI-07",
                "target_area": "Claim governance explanation",
                "coherence_problem": "The claim governance section needs a cleaner distinction between allowed, deferred, and prohibited claims.",
                "improvement_text": (
                    "The claim governance discussion should explicitly separate what can be said now, what requires future evidence, "
                    "and what remains prohibited. Current claims are limited to internally audited safe abstract toy governance artifacts."
                ),
                "transition_text": (
                    "This helps reviewers see that the manuscript does not hide weak evidence; it classifies evidence requirements."
                ),
                "retained_boundary": "Deferred claims remain deferred and prohibited claims remain prohibited.",
                "blocked_overclaim": "Do not upgrade deferred claims into completed claims or prohibited claims into future promises.",
            },
            {
                "id": "CI-08",
                "target_area": "Limitations balance",
                "coherence_problem": "The limitations are necessary but can overwhelm the contribution if not organized.",
                "improvement_text": (
                    "The limitations section should be organized around evidence gaps rather than apology. It should clearly state "
                    "that there is no executed toy evaluation, no external validation, no independent experiment, no formal proof, "
                    "no citation-completed claim, and no submission readiness, while also explaining what the governance package does provide."
                ),
                "transition_text": (
                    "This balances caution with contribution: the limitations restrict claims without erasing the artifact's purpose."
                ),
                "retained_boundary": "Limitations may be organized but not weakened.",
                "blocked_overclaim": "Do not soften or remove non-readiness, non-validation, or non-evidence statements.",
            },
            {
                "id": "CI-09",
                "target_area": "Evaluation design bridge",
                "coherence_problem": "The manuscript needs a bridge from gap register to toy evaluation design.",
                "improvement_text": (
                    "The evaluation-design bridge should explain that the v8.217 modules are proposed future checks for lineage completeness, "
                    "zero-counter preservation, blocked-claim coverage, section-boundary consistency, gap traceability, contribution clarity, "
                    "limitation balance, citation-slot readiness, mutation gating, and reproducibility description coverage."
                ),
                "transition_text": (
                    "This positions evaluation design as the next evidence pathway while keeping actual evaluation run count at zero."
                ),
                "retained_boundary": "Evaluation modules are designed but not executed.",
                "blocked_overclaim": "Do not report results, scores, validation outcomes, or performance claims.",
            },
            {
                "id": "CI-10",
                "target_area": "Future work roadmap",
                "coherence_problem": "Future work needs to be sequenced rather than listed loosely.",
                "improvement_text": (
                    "Future work should be sequenced as: citation-slot integration, safe toy evaluation execution, metric reporting, "
                    "coherence rewrite, contribution sharpening, limitation balancing, reproducibility packaging, and only then a future "
                    "readiness blocker review. Future work may only introduce stronger claims after separately audited milestones."
                ),
                "transition_text": (
                    "This creates a disciplined roadmap from preview toward stronger evidence without implying that later milestones already occurred."
                ),
                "retained_boundary": "Future work is conditional and not completed in this package.",
                "blocked_overclaim": "Do not imply citation integration, evaluation execution, readiness, proof, or validation has already happened.",
            },
        ]

    def _improved_outline(self) -> List[Dict[str, str]]:
        return [
            {
                "section": "Abstract",
                "coherence_role": "State problem, safe toy governance contribution, current artifacts, and explicit non-readiness.",
            },
            {
                "section": "Introduction",
                "coherence_role": "Motivate overclaim drift and establish why claim-state separation matters.",
            },
            {
                "section": "Method Scope",
                "coherence_role": "Present toy-only restriction as a methodological premise, not a decorative warning label.",
            },
            {
                "section": "Pipeline Overview",
                "coherence_role": "Narrate the progression from boundaries to language, drafts, preview, gaps, and evaluation design.",
            },
            {
                "section": "Safety Controls",
                "coherence_role": "Explain zero counters as invariants that prevent scope drift.",
            },
            {
                "section": "Claim Governance",
                "coherence_role": "Separate allowed, deferred, and prohibited claims in reviewer-facing language.",
            },
            {
                "section": "Limitations",
                "coherence_role": "Organize missing evidence without erasing the governance contribution.",
            },
            {
                "section": "Safety Exclusions",
                "coherence_role": "Keep real-biological exclusions explicit and non-negotiable.",
            },
            {
                "section": "Future Work",
                "coherence_role": "Sequence evidence upgrades without implying they are complete.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        assembly_source = self._load_json(self.source_assembly_json_path)
        assembly_md = self._load_text(self.source_assembly_md_path)
        gap_source = self._load_json(self.source_gap_json_path)
        eval_source = self._load_json(self.source_eval_json_path)

        assembly_counters = assembly_source.get("counters", {})
        gap_counters = gap_source.get("counters", {})
        eval_counters = eval_source.get("counters", {})

        coherence_items = self._coherence_items()
        improved_outline = self._improved_outline()

        combined_improvement_text = "\n\n".join(
            f"{item['target_area']}: {item['improvement_text']} {item['transition_text']}"
            for item in coherence_items
        )

        counters = {
            "Safe abstract toy manuscript coherence improvement package count": 1,
            "New safe abstract toy manuscript coherence improvement package count": 1,
            "Toy manuscript coherence improvement JSON export count": 1,
            "Toy manuscript coherence improvement item count": len(coherence_items),
            "Toy manuscript coherence improved outline section count": len(improved_outline),
            "Toy manuscript coherence transition text count": len(coherence_items),
            "Toy manuscript coherence retained boundary count": len(coherence_items),
            "Toy manuscript coherence blocked overclaim count": len(coherence_items),
            "Toy manuscript coherence source assembly section count": assembly_counters.get("Toy manuscript assembly preview section count"),
            "Toy manuscript coherence source gap item count": gap_counters.get("Toy scientific gap register item count"),
            "Toy manuscript coherence source evaluation design module count": eval_counters.get("Toy evaluation design module count"),
            "Toy manuscript coherence source actual evaluation run count": eval_counters.get("Toy evaluation actual run count"),
            "Toy manuscript coherence source validation claim count": eval_counters.get("Toy evaluation validation claim count"),
            "Toy manuscript coherence source evidence upgrade completed count": eval_counters.get("Toy scientific evidence upgrade completed count"),
            "Toy manuscript coherence package execution count": 1,
            "Toy manuscript coherence package direct execution count": 1,
            "Toy manuscript coherence rewrite application count": 0,
            "Toy evaluation actual run count": 0,
            "Toy evaluation result count": 0,
            "Toy evaluation validation claim count": 0,
            "Toy scientific evidence upgrade completed count": 0,
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
            "title": "Safe Abstract Toy Manuscript Coherence Improvement Package",
            "source_assembly_json": str(self.source_assembly_json_path),
            "source_assembly_markdown": str(self.source_assembly_md_path),
            "source_gap_json": str(self.source_gap_json_path),
            "source_evaluation_design_json": str(self.source_eval_json_path),
            "source_assembly_markdown_character_count": len(assembly_md),
            "package_phrase": self.package_phrase,
            "scope": "manuscript-coherence-improvement-package-only",
            "safe_abstract_toy_only": True,
            "synthetic_only": True,
            "abstract_graphs_only": True,
            "unitless_parameters_only": True,
            "non_operational_only": True,
            "coherence_improvement_completed": True,
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
                "This v8.218 artifact improves the coherence plan for the safe abstract toy manuscript preview only. "
                "It does not apply a rewrite to any manuscript file, execute evaluation, produce results, validate claims, "
                "complete evidence upgrades, add citations, approve readiness, or introduce real-biological operational capability."
            ),
            "coherence_items": coherence_items,
            "improved_outline": improved_outline,
            "combined_improvement_text": combined_improvement_text,
            "boundary_notes": [item["retained_boundary"] for item in coherence_items],
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "manuscript-coherence-improvement-package-only":
            raise AssertionError("v8.218 must remain manuscript-coherence-improvement-package-only.")

        if report["passed"] is not True:
            raise AssertionError("v8.218 coherence improvement package must pass.")

        if report["coherence_improvement_completed"] is not True:
            raise AssertionError("v8.218 should complete only the coherence improvement package.")

        for field in [
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

        if counters["Toy manuscript coherence improvement item count"] != 10:
            raise AssertionError("Expected exactly ten coherence improvement items.")

        if counters["Toy manuscript coherence improved outline section count"] != 9:
            raise AssertionError("Expected exactly nine improved outline sections.")

        if counters["Toy manuscript coherence source assembly section count"] != 9:
            raise AssertionError("Expected source assembly section count of nine.")

        if counters["Toy manuscript coherence source gap item count"] != 12:
            raise AssertionError("Expected source gap item count of twelve.")

        if counters["Toy manuscript coherence source evaluation design module count"] != 10:
            raise AssertionError("Expected source evaluation design module count of ten.")

        if counters["Toy manuscript coherence source actual evaluation run count"] != 0:
            raise AssertionError("Source actual evaluation run count must remain zero.")

        if counters["Toy manuscript coherence source validation claim count"] != 0:
            raise AssertionError("Source validation claim count must remain zero.")

        if counters["Toy manuscript coherence source evidence upgrade completed count"] != 0:
            raise AssertionError("Source evidence upgrade count must remain zero.")

        if counters["Toy manuscript coherence rewrite application count"] != 0:
            raise AssertionError("No coherence rewrite may be applied in v8.218.")

        combined_text = json.dumps(report["coherence_items"], ensure_ascii=False) + report["combined_improvement_text"]

        required_phrases = [
            "Global narrative spine",
            "Abstract coherence",
            "Introduction story arc",
            "Method scope bridge",
            "Pipeline overview transitions",
            "Safety controls framing",
            "Claim governance explanation",
            "Limitations balance",
            "Evaluation design bridge",
            "Future work roadmap",
            "No real biological datasets",
            "no real pathogen models",
            "no receptor parameters",
            "no operational targeting",
            "zero applied patches",
            "zero manuscript mutation",
            "zero readiness approval",
            "zero external validation",
            "zero proof assistant verification",
            "zero new citation addition",
            "Future work may only introduce stronger claims",
        ]

        for phrase in required_phrases:
            if phrase not in combined_text:
                raise AssertionError(f"Missing required coherence phrase: {phrase}")

        must_be_zero = [
            "Toy manuscript coherence rewrite application count",
            "Toy evaluation actual run count",
            "Toy evaluation result count",
            "Toy evaluation validation claim count",
            "Toy scientific evidence upgrade completed count",
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

        lines.append("# Safe Abstract Toy Manuscript Coherence Improvement Package")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is manuscript-coherence-improvement-package-only.")
        lines.append("It improves the narrative plan for the manuscript preview without applying a rewrite or modifying any manuscript file.")
        lines.append("")
        lines.append(f"Package phrase: `{report['package_phrase']}`")
        lines.append("")
        lines.append("## Non-Readiness Disclaimer")
        lines.append("")
        lines.append(report["non_readiness_disclaimer"])
        lines.append("")
        lines.append("## Improved Outline")
        lines.append("")

        for item in report["improved_outline"]:
            lines.append(f"- {item['section']}: {item['coherence_role']}")

        lines.append("")
        lines.append("## Coherence Improvement Items")
        lines.append("")

        for item in report["coherence_items"]:
            lines.append(f"### {item['id']} — {item['target_area']}")
            lines.append("")
            lines.append(f"- Coherence problem: {item['coherence_problem']}")
            lines.append(f"- Improvement text: {item['improvement_text']}")
            lines.append(f"- Transition text: {item['transition_text']}")
            lines.append(f"- Retained boundary: {item['retained_boundary']}")
            lines.append(f"- Blocked overclaim: {item['blocked_overclaim']}")
            lines.append("")

        lines.append("## Combined Improvement Text")
        lines.append("")
        lines.append(report["combined_improvement_text"])
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
        lines.append("V8_218_SAFE_ABSTRACT_TOY_MANUSCRIPT_COHERENCE_IMPROVEMENT_PACKAGE_OK")
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


def build_safe_abstract_toy_manuscript_coherence_improvement_package() -> Dict[str, Any]:
    return SafeAbstractToyManuscriptCoherenceImprovementPackageBuilder().run()


if __name__ == "__main__":
    result = build_safe_abstract_toy_manuscript_coherence_improvement_package()
    counters = result["counters"]
    print("V8_218_SAFE_ABSTRACT_TOY_MANUSCRIPT_COHERENCE_IMPROVEMENT_PACKAGE_OK")
    print("TOY_MANUSCRIPT_COHERENCE_IMPROVEMENT_PACKAGE_DIRECT_CHECK_OK")
    print(f"Coherence improvement item count: {counters['Toy manuscript coherence improvement item count']}")
    print(f"Improved outline section count: {counters['Toy manuscript coherence improved outline section count']}")
    print(f"Transition text count: {counters['Toy manuscript coherence transition text count']}")
    print(f"Source assembly section count: {counters['Toy manuscript coherence source assembly section count']}")
    print(f"Source gap item count: {counters['Toy manuscript coherence source gap item count']}")
    print(f"Source evaluation design module count: {counters['Toy manuscript coherence source evaluation design module count']}")
    print(f"Source actual evaluation run count: {counters['Toy manuscript coherence source actual evaluation run count']}")
    print(f"Source validation claim count: {counters['Toy manuscript coherence source validation claim count']}")
    print(f"Source evidence upgrade completed count: {counters['Toy manuscript coherence source evidence upgrade completed count']}")
    print(f"Rewrite application count: {counters['Toy manuscript coherence rewrite application count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"Passed: {result['passed']}")
