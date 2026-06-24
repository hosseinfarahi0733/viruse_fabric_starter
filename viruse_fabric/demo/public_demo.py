from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class DemoArtifact:
    name: str
    path: str
    artifact_type: str
    purpose: str
    required: bool = True


@dataclass(frozen=True)
class DemoMilestone:
    version: str
    title: str
    summary: str
    experiment_module: str
    main_output: str


@dataclass(frozen=True)
class PublicDemoReport:
    title: str
    output_path: str
    milestone_count: int
    artifact_count: int
    missing_required_count: int
    passed: bool
    interpretation: str


class PublicDemoPackage:
    title = "Viruse Fabric Public Demo Package v2.3"

    milestones: tuple[DemoMilestone, ...] = (
        DemoMilestone(
            version="v1.7.0",
            title="English Theory Chapter Exporter",
            summary="Exports an English manuscript-facing theory chapter from simulation results.",
            experiment_module="viruse_fabric.experiments.exp_17_theory_chapter_exporter",
            main_output="outputs/theory_chapter_v1_7.md",
        ),
        DemoMilestone(
            version="v1.8.0",
            title="Persian Theory Chapter Exporter",
            summary="Exports a Persian theory chapter with safe conceptual boundaries.",
            experiment_module="viruse_fabric.experiments.exp_18_persian_theory_chapter_exporter",
            main_output="outputs/theory_chapter_fa_v1_8.md",
        ),
        DemoMilestone(
            version="v1.9.0",
            title="Bilingual Quality Audit",
            summary="Adds a bilingual glossary and an automated quality gate for manuscript outputs.",
            experiment_module="viruse_fabric.experiments.exp_19_bilingual_quality_audit",
            main_output="outputs/bilingual_quality_report_v1_9.md",
        ),
        DemoMilestone(
            version="v2.0.0",
            title="Theory Manifest",
            summary="States the theory claims, limits, evidence, safety boundary, and open weak points.",
            experiment_module="viruse_fabric.experiments.exp_20_theory_manifest",
            main_output="outputs/theory_manifest_v2_0.md",
        ),
        DemoMilestone(
            version="v2.1.0",
            title="Visual Explanation Layer",
            summary="Renders a diagram and report connecting paths, attractors, targeting, and observer misreading.",
            experiment_module="viruse_fabric.experiments.exp_21_visual_explanation",
            main_output="outputs/visual_explanation_report_v2_1.md",
        ),
        DemoMilestone(
            version="v2.2.0",
            title="Scenario Stress Tests",
            summary="Checks whether the model rejects broken scenarios without flattening valid ones.",
            experiment_module="viruse_fabric.experiments.exp_22_scenario_stress_tests",
            main_output="outputs/scenario_stress_report_v2_2.md",
        ),
        DemoMilestone(
            version="v2.3.0",
            title="Public Demo Package",
            summary="Provides a public-facing entry point for milestones, outputs, safety boundary, and current limits.",
            experiment_module="viruse_fabric.experiments.exp_23_public_demo_package",
            main_output="outputs/public_demo_report_v2_3.md",
        ),
    )

    artifacts: tuple[DemoArtifact, ...] = (
        DemoArtifact(
            name="English theory chapter",
            path="outputs/theory_chapter_v1_7.md",
            artifact_type="markdown",
            purpose="English manuscript-facing theory output.",
        ),
        DemoArtifact(
            name="Persian theory chapter",
            path="outputs/theory_chapter_fa_v1_8.md",
            artifact_type="markdown",
            purpose="Persian manuscript-facing theory output.",
        ),
        DemoArtifact(
            name="Bilingual quality report",
            path="outputs/bilingual_quality_report_v1_9.md",
            artifact_type="markdown",
            purpose="Quality gate report for Persian chapter and glossary.",
        ),
        DemoArtifact(
            name="Theory manifest",
            path="outputs/theory_manifest_v2_0.md",
            artifact_type="markdown",
            purpose="Boundary document for claims, evidence, limits, and weaknesses.",
        ),
        DemoArtifact(
            name="Visual explanation diagram",
            path="outputs/fabric_diagram_v2_1.png",
            artifact_type="image",
            purpose="Diagram of route structure, attractor roles, and disrupted paths.",
        ),
        DemoArtifact(
            name="Visual explanation report",
            path="outputs/visual_explanation_report_v2_1.md",
            artifact_type="markdown",
            purpose="Report explaining the visual layer.",
        ),
        DemoArtifact(
            name="Scenario stress report",
            path="outputs/scenario_stress_report_v2_2.md",
            artifact_type="markdown",
            purpose="Internal stress-test report.",
        ),
        DemoArtifact(
            name="Theory log",
            path="notes/theory_log.md",
            artifact_type="markdown",
            purpose="Versioned theoretical development log.",
        ),
    )

    safety_boundary = (
        "This project is conceptual and non-operational. It does not provide real pathogens, "
        "real hosts, doses, receptors, laboratory protocols, executable biological procedures, "
        "or deployable interventions."
    )

    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path or Path("outputs/public_demo_report_v2_3.md")

    def build(self) -> PublicDemoReport:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        markdown = self.render_markdown()
        self.output_path.write_text(markdown, encoding="utf-8")

        missing_required_count = len(self.missing_required_artifacts())

        return PublicDemoReport(
            title=self.title,
            output_path=str(self.output_path),
            milestone_count=len(self.milestones),
            artifact_count=len(self.artifacts),
            missing_required_count=missing_required_count,
            passed=missing_required_count == 0,
            interpretation=(
                "The project now has a public-facing demo package that explains how to inspect "
                "its milestones, outputs, safety boundary, and current limits."
            ),
        )

    def missing_required_artifacts(self) -> tuple[DemoArtifact, ...]:
        missing = [
            artifact
            for artifact in self.artifacts
            if artifact.required and not Path(artifact.path).exists()
        ]
        return tuple(missing)

    def artifact_size(self, artifact: DemoArtifact) -> int:
        path = Path(artifact.path)
        if not path.exists():
            return 0
        return path.stat().st_size

    def render_markdown(self) -> str:
        missing = self.missing_required_artifacts()

        lines = [
            f"# {self.title}",
            "",
            "## What this demo is",
            "",
            (
                "This report is a public entry point for Viruse Fabric. "
                "It summarizes the current milestones, generated artifacts, safety boundary, "
                "and recommended inspection order."
            ),
            "",
            "Viruse Fabric's current core claim is:",
            "",
            "> Causality is not a chain; it is a geometry of constraints.",
            "",
            "> علیت زنجیره نیست؛ هندسه‌ی قیود است.",
            "",
            "## Recommended inspection order",
            "",
            "1. Read `outputs/theory_manifest_v2_0.md`.",
            "2. Read `outputs/scenario_stress_report_v2_2.md`.",
            "3. Open `outputs/fabric_diagram_v2_1.png`.",
            "4. Read `outputs/visual_explanation_report_v2_1.md`.",
            "5. Inspect `outputs/theory_chapter_fa_v1_8.md` or `outputs/theory_chapter_v1_7.md`.",
            "6. Check `notes/theory_log.md` for version history.",
            "",
            "## Milestones",
            "",
            "| Version | Title | Experiment | Main output | Summary |",
            "|---|---|---|---|---|",
        ]

        for milestone in self.milestones:
            lines.append(
                f"| {milestone.version} | {milestone.title} | "
                f"`python -m {milestone.experiment_module}` | "
                f"`{milestone.main_output}` | {milestone.summary} |"
            )

        lines.extend(
            [
                "",
                "## Artifacts",
                "",
                "| Artifact | Type | Path | Size bytes | Purpose |",
                "|---|---|---|---:|---|",
            ]
        )

        for artifact in self.artifacts:
            lines.append(
                f"| {artifact.name} | {artifact.artifact_type} | "
                f"`{artifact.path}` | {self.artifact_size(artifact)} | {artifact.purpose} |"
            )

        lines.extend(
            [
                "",
                "## Missing required artifacts",
                "",
            ]
        )

        if not missing:
            lines.append("No missing required artifacts.")
        else:
            for artifact in missing:
                lines.append(f"- `{artifact.path}`")

        lines.extend(
            [
                "",
                "## Safety boundary",
                "",
                self.safety_boundary,
                "",
                "## What this project does not yet prove",
                "",
                "- It does not provide external empirical validation yet.",
                "- It does not prove that the current formulas are final.",
                "- It does not predict real biological outcomes.",
                "- It does not convert abstract biological language into executable biological procedure.",
                "- It does not claim that apparent targeting is real intention.",
                "",
                "## Demo commands",
                "",
                "```bash",
                "python -m viruse_fabric.experiments.exp_20_theory_manifest",
                "python -m viruse_fabric.experiments.exp_21_visual_explanation",
                "python -m viruse_fabric.experiments.exp_22_scenario_stress_tests",
                "```",
                "",
                "## Interpretation",
                "",
                (
                    "The project is currently strongest as a conceptual-computational theory-building system. "
                    "Its next weakness is public readability: a new reader still needs guidance. "
                    "This demo package is the first entry point that reduces that friction."
                ),
                "",
            ]
        )

        return "\n".join(lines)

    def word_count(self, text: str) -> int:
        return len([part for part in re.split(r"\s+", text.strip()) if part])
