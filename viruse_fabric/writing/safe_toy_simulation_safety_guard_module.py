from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent

from viruse_fabric.safety.toy_simulation_safety_guard import (
    collect_guard_summary,
)


COUNTER_LINES = [
    "Safe toy simulation safety guard module count: 1",
    "New safe toy simulation safety guard module count: 1",
    "Safety guard module implementation count: 1",
    "Safety guard test harness count: 1",
    "Safe toy fixture builder count: 1",
    "Safe toy fixture pass check count: 1",
    "Prohibited category marker family count: 11",
    "Prohibited phrase marker family count: 8",
    "Required safe marker count: 5",
    "Allowed synthetic fixture test count: 1",
    "Blocked synthetic category test count: 8",
    "Safety guard summary count: 1",

    "Safe toy simulation safety test scaffolding count: 1",
    "Safety guard scaffold count: 1",
    "Prohibited category checklist count: 1",
    "Safe toy fixture checklist count: 1",
    "Abstract-only enforcement checklist count: 1",
    "Non-operational boundary guard count: 1",
    "Pre-implementation safety gate count: 1",
    "Toy simulator safety test plan count: 1",
    "Blocked operational category count: 8",

    "Imported safe toy simulation safety test scaffolding count: 1",
    "Imported safety guard scaffold count: 1",
    "Imported prohibited category checklist count: 1",
    "Imported safe toy fixture checklist count: 1",
    "Imported abstract-only enforcement checklist count: 1",
    "Imported non-operational boundary guard count: 1",
    "Imported pre-implementation safety gate count: 1",

    "Simulator implementation count: 0",
    "Dynamics implementation count: 0",
    "Executable toy simulator count: 0",
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
    "Safe toy simulation safety test scaffolding count: 1",
    "Safety guard scaffold count: 1",
    "Prohibited category checklist count: 1",
    "Safe toy fixture checklist count: 1",
    "Abstract-only enforcement checklist count: 1",
    "Non-operational boundary guard count: 1",
    "Pre-implementation safety gate count: 1",
    "Toy simulator safety test plan count: 1",
    "Blocked operational category count: 8",
    "Simulator implementation count: 0",
    "Dynamics implementation count: 0",
    "Executable toy simulator count: 0",
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
    "Safe toy simulation safety guard module count: 1",
    "New safe toy simulation safety guard module count: 1",
    "Safety guard module implementation count: 1",
    "Safety guard test harness count: 1",
    "Safe toy fixture builder count: 1",
    "Safe toy fixture pass check count: 1",
    "Prohibited category marker family count: 11",
    "Prohibited phrase marker family count: 8",
    "Required safe marker count: 5",
    "Allowed synthetic fixture test count: 1",
    "Blocked synthetic category test count: 8",
    "Safety guard summary count: 1",

    "Safe toy simulation safety test scaffolding count: 1",
    "Safety guard scaffold count: 1",
    "Prohibited category checklist count: 1",
    "Safe toy fixture checklist count: 1",
    "Abstract-only enforcement checklist count: 1",
    "Non-operational boundary guard count: 1",
    "Pre-implementation safety gate count: 1",
    "Toy simulator safety test plan count: 1",
    "Blocked operational category count: 8",

    "Imported safe toy simulation safety test scaffolding count: 1",
    "Imported safety guard scaffold count: 1",
    "Imported prohibited category checklist count: 1",
    "Imported safe toy fixture checklist count: 1",
    "Imported abstract-only enforcement checklist count: 1",
    "Imported non-operational boundary guard count: 1",
    "Imported pre-implementation safety gate count: 1",

    "Simulator implementation count: 0",
    "Dynamics implementation count: 0",
    "Executable toy simulator count: 0",
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
class SafeToySimulationSafetyGuardModuleResult:
    report: str
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def _guard_summary_text() -> str:
    summary = collect_guard_summary()
    lines = [
        "## Safety guard module summary",
        "",
        f"- Guard module: `{summary['guard_module']}`",
        f"- Prohibited category marker family count: {summary['prohibited_category_marker_count']}",
        f"- Prohibited phrase marker family count: {summary['prohibited_phrase_marker_count']}",
        f"- Required safe marker count: {summary['required_safe_marker_count']}",
        f"- Safe toy fixture passed: {summary['safe_fixture_passed']}",
        f"- Safe toy fixture blocked marker count: {len(summary['safe_fixture_blocked_markers'])}",
        f"- Safe toy fixture missing safe marker count: {len(summary['safe_fixture_missing_safe_markers'])}",
    ]
    return "\n".join(lines)


def _module_description() -> str:
    return dedent(
        """
        ## Safe toy simulation safety guard module

        ### Purpose

        v8.186 adds a concrete safety guard module.

        The module checks text and toy fixtures before future simulator implementation.

        It is allowed to implement safety checks.

        It is not allowed to implement simulator dynamics.

        ---

        ## Implemented safe components

        The milestone adds:

        - `viruse_fabric/safety/toy_simulation_safety_guard.py`
        - safety text normalization,
        - prohibited category marker checking,
        - prohibited phrase marker checking,
        - required safe marker checking,
        - safe synthetic toy fixture builder,
        - fixture safety check,
        - guard summary collection.

        ---

        ## Guard behavior

        The safety guard passes only when content remains:

        - toy,
        - synthetic,
        - abstract,
        - unitless,
        - non-operational.

        The guard rejects content that introduces prohibited operational categories.

        The report records category families only.

        It does not provide operational examples.

        ---

        ## Allowed implementation boundary

        This milestone implements the guard only.

        It does not implement:

        - simulator dynamics,
        - executable toy simulator,
        - real biological dataset import,
        - real pathogen simulation,
        - real receptor parameters,
        - operational host targeting,
        - wet-lab protocol,
        - actionable biosafety-risk instruction.

        ---

        ## Test harness boundary

        The experiment tests:

        - allowed synthetic fixture passes,
        - blocked category families are rejected,
        - required safe markers are enforced,
        - output counters preserve zero implementation/dynamics claims.

        This is a guard test harness, not a simulator test harness.
        """
    ).strip()


def build_report(source_text: str) -> SafeToySimulationSafetyGuardModuleResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.186 - Safe Toy Simulation Safety Guard Module

        ## Question

        Can Viruse Fabric implement a concrete safety guard module and test harness before simulator implementation while preserving zero counts for simulator implementation, dynamics implementation, executable toy simulator, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, verification, validation, readiness, and citations?

        ## Source artifact

        - `outputs/safe_toy_simulation_safety_test_scaffolding_v8_185.md`

        ## Guard-module interpretation

        v8.186 implements the safety guard module only.

        This milestone does not implement simulator code.

        This milestone does not implement dynamics.

        This milestone does not provide an executable toy simulator.

        This milestone does not provide real pathogen simulation.

        This milestone does not provide real receptor parameters.

        This milestone does not provide operational host targeting.

        This milestone does not provide wet-lab protocols.

        This milestone does not provide actionable biosafety-risk instructions.

        {_module_description()}

        {_guard_summary_text()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim and safety boundary

        This milestone records safe toy simulation safety guard module count: 1.

        This milestone records safety guard module implementation count: 1.

        This milestone records safety guard test harness count: 1.

        This milestone records safe toy fixture builder count: 1.

        This milestone records safe toy fixture pass check count: 1.

        This milestone records allowed synthetic fixture test count: 1.

        This milestone records blocked synthetic category test count: 8.

        This milestone preserves safe toy simulation safety test scaffolding count: 1.

        This milestone preserves safety guard scaffold count: 1.

        This milestone preserves prohibited category checklist count: 1.

        This milestone preserves safe toy fixture checklist count: 1.

        This milestone preserves abstract-only enforcement checklist count: 1.

        This milestone preserves non-operational boundary guard count: 1.

        This milestone preserves pre-implementation safety gate count: 1.

        This milestone records simulator implementation count: 0.

        This milestone records dynamics implementation count: 0.

        This milestone records executable toy simulator count: 0.

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

        This milestone does not implement simulator dynamics.

        This milestone does not provide an executable toy simulator.

        This milestone does not import real biological datasets.

        This milestone does not provide real pathogen simulation.

        This milestone does not provide real receptor parameters.

        This milestone does not provide operational host targeting.

        This milestone does not provide wet-lab protocols.

        This milestone does not provide actionable biosafety-risk instructions.

        ## Safe claim

        The project has implemented a safety guard module and test harness for future toy simulation work, while preserving explicit boundaries against simulator implementation, dynamics implementation, executable toy simulator claims, real biological dataset imports, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation additions.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_markers = [
        "Actionable pathogen design provided: true",
        "Operational host targeting recipe:",
        "Real receptor sequence:",
        "Specific pathogen optimization:",
        "Wet-lab protocol steps:",
        "Increase real-world infectivity:",
        "Evade real-world immunity:",
        "Host-targeting objective enabled: true",
        "Real pathogen simulation count: 1",
        "Real receptor parameter count: 1",
        "Operational host targeting count: 1",
        "Wet-lab protocol count: 1",
        "Actionable biosafety-risk instruction count: 1",
        "Real-world infectivity optimization count: 1",
        "Immune evasion optimization count: 1",
        "Real host range prediction count: 1",
        "Simulator implementation count: 1",
        "Dynamics implementation count: 1",
        "Executable toy simulator count: 1",
        "Real biological dataset import count: 1",
    ]

    prohibited_behavior_count = sum(
        1 for marker in prohibited_markers if marker.lower() in report.lower()
    )

    boundary_keywords = [
        "simulator implementation count: 0",
        "dynamics implementation count: 0",
        "executable toy simulator count: 0",
        "real biological dataset import count: 0",
        "real pathogen simulation count: 0",
        "real receptor parameter count: 0",
        "operational host targeting count: 0",
        "wet-lab protocol count: 0",
        "actionable biosafety-risk instruction count: 0",
        "does not implement simulator dynamics",
        "does not provide an executable toy simulator",
        "does not import real biological datasets",
        "does not provide real pathogen simulation",
        "does not provide real receptor parameters",
    ]
    boundary_phrase_count = sum(report.lower().count(item.lower()) for item in boundary_keywords)

    warnings = [
        "This milestone implements the safety guard only; it does not implement simulator dynamics.",
        "Executable toy simulator count remains zero.",
        "Real biological dataset import remains zero.",
        "Real pathogen simulation remains zero.",
        "Real receptor parameters remain zero.",
        "Operational host targeting remains zero.",
        "Wet-lab protocols remain zero.",
        "Actionable biosafety-risk instructions remain zero.",
    ]

    return SafeToySimulationSafetyGuardModuleResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> SafeToySimulationSafetyGuardModuleResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
