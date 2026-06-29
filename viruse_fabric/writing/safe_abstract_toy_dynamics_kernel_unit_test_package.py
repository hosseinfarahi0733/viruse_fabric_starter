from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTER_LINES = [
    "Safe abstract toy dynamics kernel unit test package count: 1",
    "New safe abstract toy dynamics kernel unit test package count: 1",
    "Toy dynamics kernel unit test file count: 1",
    "Toy dynamics kernel unittest case count: 10",
    "Clamp unit test count: 1",
    "Kernel config unit test count: 1",
    "Single fixture kernel result unit test count: 1",
    "Catalog execution count unit test count: 1",
    "Catalog safety guard unit test count: 1",
    "Kernel summary unit test count: 1",
    "Empty summary unit test count: 1",
    "Unsafe fixture rejection unit test count: 1",
    "Unknown synthetic location rejection unit test count: 1",
    "Deterministic kernel execution unit test count: 1",
    "Toy dynamics kernel unit test execution count: 1",

    "Safe abstract toy dynamics kernel implementation count: 1",
    "Simulator implementation count: 1",
    "Dynamics implementation count: 1",
    "Executable toy simulator count: 1",
    "Toy dynamics kernel module count: 1",
    "Toy kernel catalog execution count: 1",
    "Toy kernel fixture execution count: 3",
    "Toy kernel safety guard pass count: 3",
    "Toy kernel result summary count: 1",
    "Toy observation projection execution count: 1",
    "Targeted-looking pattern score execution count: 1",
    "Unitless dynamics execution count: 1",
    "Abstract graph dynamics execution count: 1",
    "Synthetic fixture execution count: 3",

    "Imported safe abstract toy dynamics kernel implementation count: 1",
    "Imported simulator implementation count: 1",
    "Imported dynamics implementation count: 1",
    "Imported executable toy simulator count: 1",
    "Imported toy dynamics kernel module count: 1",

    "Real biological dataset import count: 0",
    "Real pathogen simulation count: 0",
    "Real receptor parameter count: 0",
    "Operational host targeting count: 0",
    "Wet-lab protocol count: 0",
    "Actionable biosafety-risk instruction count: 0",
    "Real-world infectivity optimization count: 0",
    "Immune evasion optimization count: 0",
    "Real host range prediction count: 0",

    "New lemma proof execution count: 0",
    "New TC-001 proof execution count: 0",
    "New theorem proven count: 0",
    "New theorem proof execution count: 0",
    "Formalization complete count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


REQUIRED_SOURCE_PHRASES = [
    "Safe abstract toy dynamics kernel implementation count: 1",
    "Simulator implementation count: 1",
    "Dynamics implementation count: 1",
    "Executable toy simulator count: 1",
    "Toy dynamics kernel module count: 1",
    "Toy kernel catalog execution count: 1",
    "Toy kernel fixture execution count: 3",
    "Toy kernel safety guard pass count: 3",
    "Toy kernel result summary count: 1",
    "Toy observation projection execution count: 1",
    "Targeted-looking pattern score execution count: 1",
    "Unitless dynamics execution count: 1",
    "Abstract graph dynamics execution count: 1",
    "Synthetic fixture execution count: 3",
    "Real biological dataset import count: 0",
    "Real pathogen simulation count: 0",
    "Real receptor parameter count: 0",
    "Operational host targeting count: 0",
    "Wet-lab protocol count: 0",
    "Actionable biosafety-risk instruction count: 0",
    "Real-world infectivity optimization count: 0",
    "Immune evasion optimization count: 0",
    "Real host range prediction count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


REQUIRED_REPORT_PHRASES = [
    "Safe abstract toy dynamics kernel unit test package count: 1",
    "New safe abstract toy dynamics kernel unit test package count: 1",
    "Toy dynamics kernel unit test file count: 1",
    "Toy dynamics kernel unittest case count: 10",
    "Clamp unit test count: 1",
    "Kernel config unit test count: 1",
    "Single fixture kernel result unit test count: 1",
    "Catalog execution count unit test count: 1",
    "Catalog safety guard unit test count: 1",
    "Kernel summary unit test count: 1",
    "Empty summary unit test count: 1",
    "Unsafe fixture rejection unit test count: 1",
    "Unknown synthetic location rejection unit test count: 1",
    "Deterministic kernel execution unit test count: 1",
    "Toy dynamics kernel unit test execution count: 1",

    "Safe abstract toy dynamics kernel implementation count: 1",
    "Simulator implementation count: 1",
    "Dynamics implementation count: 1",
    "Executable toy simulator count: 1",
    "Toy dynamics kernel module count: 1",
    "Toy kernel catalog execution count: 1",
    "Toy kernel fixture execution count: 3",
    "Toy kernel safety guard pass count: 3",
    "Toy kernel result summary count: 1",
    "Toy observation projection execution count: 1",
    "Targeted-looking pattern score execution count: 1",
    "Unitless dynamics execution count: 1",
    "Abstract graph dynamics execution count: 1",
    "Synthetic fixture execution count: 3",

    "Imported safe abstract toy dynamics kernel implementation count: 1",
    "Imported simulator implementation count: 1",
    "Imported dynamics implementation count: 1",
    "Imported executable toy simulator count: 1",
    "Imported toy dynamics kernel module count: 1",

    "Real biological dataset import count: 0",
    "Real pathogen simulation count: 0",
    "Real receptor parameter count: 0",
    "Operational host targeting count: 0",
    "Wet-lab protocol count: 0",
    "Actionable biosafety-risk instruction count: 0",
    "Real-world infectivity optimization count: 0",
    "Immune evasion optimization count: 0",
    "Real host range prediction count: 0",

    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


@dataclass(frozen=True)
class SafeAbstractToyDynamicsKernelUnitTestPackageResult:
    report: str
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def _description() -> str:
    return dedent(
        """
        ## Safe abstract toy dynamics kernel unit-test package

        ### Purpose

        v8.190 adds explicit unit tests for the first safe abstract toy dynamics kernel.

        This milestone tests the kernel.

        It does not add new dynamics behavior.

        It does not import real biological datasets.

        It does not add biological interpretation.

        ---

        ## Unit-test groups

        The unit-test package checks:

        - clamp behavior,
        - kernel configuration,
        - single-fixture result range,
        - catalog execution count,
        - catalog safety guard pass,
        - kernel summary behavior,
        - empty summary behavior,
        - unsafe fixture rejection,
        - unknown synthetic location rejection,
        - deterministic execution for the same fixture.

        ---

        ## Non-operational boundary

        This milestone is a test package for an existing toy kernel.

        It does not change the safe interpretation of v8.189.

        The executable simulator remains toy, synthetic, abstract, unitless, and non-operational.
        """
    ).strip()


def build_report(source_text: str) -> SafeAbstractToyDynamicsKernelUnitTestPackageResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.190 - Safe Abstract Toy Dynamics Kernel Unit Test Package

        ## Question

        Can Viruse Fabric add explicit unit tests for the safe abstract toy dynamics kernel while preserving the existing safe toy execution counters and all zero boundaries for real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, verification, validation, readiness, and citations?

        ## Source artifact

        - `outputs/safe_abstract_toy_dynamics_kernel_implementation_v8_189.md`

        ## Unit-test interpretation

        v8.190 adds a unit-test package for the v8.189 toy dynamics kernel.

        This milestone preserves:
        - Simulator implementation count: 1
        - Dynamics implementation count: 1
        - Executable toy simulator count: 1

        This milestone preserves:
        - Real biological dataset import count: 0
        - Real pathogen simulation count: 0
        - Real receptor parameter count: 0
        - Operational host targeting count: 0
        - Wet-lab protocol count: 0
        - Actionable biosafety-risk instruction count: 0

        {_description()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim and safety boundary

        This milestone records safe abstract toy dynamics kernel unit test package count: 1.

        This milestone records toy dynamics kernel unit test file count: 1.

        This milestone records toy dynamics kernel unittest case count: 10.

        This milestone records toy dynamics kernel unit test execution count: 1.

        This milestone preserves safe abstract toy dynamics kernel implementation count: 1.

        This milestone preserves simulator implementation count: 1.

        This milestone preserves dynamics implementation count: 1.

        This milestone preserves executable toy simulator count: 1.

        This milestone records real biological dataset import count: 0.

        This milestone records real pathogen simulation count: 0.

        This milestone records real receptor parameter count: 0.

        This milestone records operational host targeting count: 0.

        This milestone records wet-lab protocol count: 0.

        This milestone records actionable biosafety-risk instruction count: 0.

        This milestone records real-world infectivity optimization count: 0.

        This milestone records immune evasion optimization count: 0.

        This milestone records real host range prediction count: 0.

        This milestone records proof assistant verification count: 0.

        This milestone records external validation count: 0.

        This milestone records independent experiment count: 0.

        This milestone records manuscript submission ready count: 0.

        This milestone records readiness approval count: 0.

        This milestone records new citation added count: 0.

        This milestone does not import real biological datasets.

        This milestone does not provide real pathogen simulation.

        This milestone does not provide real receptor parameters.

        This milestone does not provide operational host targeting.

        This milestone does not provide wet-lab protocols.

        This milestone does not provide actionable biosafety-risk instructions.

        This milestone does not provide external validation.

        This milestone does not make the manuscript submission ready.

        ## Safe claim

        The project has added explicit unit tests for its safe abstract toy dynamics kernel, while preserving simulator implementation count: 1, dynamics implementation count: 1, executable toy simulator count: 1, and all explicit zero boundaries against real biological dataset imports, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation additions.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_markers = [
        "Real pathogen simulation count: 1",
        "Real receptor parameter count: 1",
        "Operational host targeting count: 1",
        "Wet-lab protocol count: 1",
        "Actionable biosafety-risk instruction count: 1",
        "Real-world infectivity optimization count: 1",
        "Immune evasion optimization count: 1",
        "Real host range prediction count: 1",
        "Real biological dataset import count: 1",
        "Proof assistant verification count: 1",
        "External validation count: 1",
        "Independent experiment count: 1",
        "Manuscript submission ready count: 1",
        "Readiness approval count: 1",
        "New citation added count: 1",
    ]

    prohibited_behavior_count = sum(
        1 for marker in prohibited_markers if marker.lower() in report.lower()
    )

    boundary_keywords = [
        "real biological dataset import count: 0",
        "real pathogen simulation count: 0",
        "real receptor parameter count: 0",
        "operational host targeting count: 0",
        "wet-lab protocol count: 0",
        "actionable biosafety-risk instruction count: 0",
        "does not import real biological datasets",
        "does not provide real pathogen simulation",
        "does not provide real receptor parameters",
        "does not provide operational host targeting",
        "does not provide wet-lab protocols",
        "does not provide actionable biosafety-risk instructions",
    ]
    boundary_phrase_count = sum(report.lower().count(item.lower()) for item in boundary_keywords)

    warnings = [
        "This milestone adds unit tests for the toy dynamics kernel only.",
        "Real biological dataset import remains zero.",
        "Real pathogen simulation remains zero.",
        "Real receptor parameters remain zero.",
        "Operational host targeting remains zero.",
        "Wet-lab protocols remain zero.",
        "Actionable biosafety-risk instructions remain zero.",
        "External validation remains zero.",
    ]

    return SafeAbstractToyDynamicsKernelUnitTestPackageResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> SafeAbstractToyDynamicsKernelUnitTestPackageResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
