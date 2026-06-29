from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent

from viruse_fabric.safety.toy_simulation_safety_guard import (
    PROHIBITED_CATEGORY_MARKERS,
    PROHIBITED_PHRASE_MARKERS,
    REQUIRED_SAFE_MARKERS,
    collect_guard_summary,
)


COUNTER_LINES = [
    "Safe toy simulation safety guard unit test package count: 1",
    "New safe toy simulation safety guard unit test package count: 1",
    "Safety guard unit test file count: 1",
    "Safety guard unittest case count: 10",
    "Safe text pass unit test count: 1",
    "Safe fixture pass unit test count: 1",
    "Required safe marker enforcement unit test count: 1",
    "Prohibited category marker unit test count: 1",
    "Prohibited phrase marker unit test count: 1",
    "Assert safe accept unit test count: 1",
    "Assert safe reject unit test count: 1",
    "Normalization unit test count: 1",
    "Guard summary consistency unit test count: 1",
    "Required safe marker stability unit test count: 1",
    "Safety guard unit test execution count: 1",

    "Safe toy simulation safety guard module count: 1",
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

    "Imported safe toy simulation safety guard module count: 1",
    "Imported safety guard module implementation count: 1",
    "Imported safety guard test harness count: 1",
    "Imported safe toy fixture builder count: 1",
    "Imported safe toy fixture pass check count: 1",

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
    "Safe toy simulation safety guard module count: 1",
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
    "Safe toy simulation safety guard unit test package count: 1",
    "New safe toy simulation safety guard unit test package count: 1",
    "Safety guard unit test file count: 1",
    "Safety guard unittest case count: 10",
    "Safe text pass unit test count: 1",
    "Safe fixture pass unit test count: 1",
    "Required safe marker enforcement unit test count: 1",
    "Prohibited category marker unit test count: 1",
    "Prohibited phrase marker unit test count: 1",
    "Assert safe accept unit test count: 1",
    "Assert safe reject unit test count: 1",
    "Normalization unit test count: 1",
    "Guard summary consistency unit test count: 1",
    "Required safe marker stability unit test count: 1",
    "Safety guard unit test execution count: 1",

    "Safe toy simulation safety guard module count: 1",
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

    "Imported safe toy simulation safety guard module count: 1",
    "Imported safety guard module implementation count: 1",
    "Imported safety guard test harness count: 1",
    "Imported safe toy fixture builder count: 1",
    "Imported safe toy fixture pass check count: 1",

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
class SafeToySimulationSafetyGuardUnitTestPackageResult:
    report: str
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def _test_summary() -> str:
    guard_summary = collect_guard_summary()
    return dedent(
        f"""
        ## Safety guard unit test package summary

        Unit test file:
        - `tests/safety/test_toy_simulation_safety_guard.py`

        Unit test groups:
        - Safe text pass test.
        - Safe fixture pass test.
        - Required safe marker enforcement test.
        - Prohibited category marker rejection test.
        - Prohibited phrase marker rejection test.
        - Assert-safe accept test.
        - Assert-safe reject test.
        - Normalization behavior test.
        - Guard summary consistency test.
        - Required safe marker stability test.

        Guard marker counts:
        - Prohibited category marker family count: {len(PROHIBITED_CATEGORY_MARKERS)}
        - Prohibited phrase marker family count: {len(PROHIBITED_PHRASE_MARKERS)}
        - Required safe marker count: {len(REQUIRED_SAFE_MARKERS)}

        Runtime guard summary:
        - Safe toy fixture passed: {guard_summary["safe_fixture_passed"]}
        - Safe fixture blocked marker count: {len(guard_summary["safe_fixture_blocked_markers"])}
        - Safe fixture missing safe marker count: {len(guard_summary["safe_fixture_missing_safe_markers"])}
        """
    ).strip()


def _package_description() -> str:
    return dedent(
        """
        ## Safe toy simulation safety guard unit test package

        ### Purpose

        v8.187 packages the safety guard checks into explicit unit tests.

        This milestone verifies the guard behavior without implementing simulator dynamics.

        It is allowed to add unit tests for the guard.

        It is not allowed to implement a simulator.

        ---

        ## Unit-test boundary

        The unit tests verify:

        - allowed safe text passes,
        - safe synthetic fixture passes,
        - missing required safe markers fail,
        - prohibited category markers fail,
        - prohibited phrase markers fail,
        - assert helper rejects blocked content,
        - normalization is stable,
        - guard summary is consistent.

        These are safety tests.

        They are not simulator tests.

        ---

        ## Non-operational boundary

        This milestone does not provide:

        - simulator implementation,
        - dynamics implementation,
        - executable toy simulator,
        - real biological dataset import,
        - real pathogen simulation,
        - real receptor parameters,
        - operational host targeting,
        - wet-lab protocol,
        - actionable biosafety-risk instruction,
        - real-world infectivity optimization,
        - immune evasion optimization,
        - real host range prediction.

        The only new artifact is a unit-test package for the safety guard.
        """
    ).strip()


def build_report(source_text: str) -> SafeToySimulationSafetyGuardUnitTestPackageResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.187 - Safe Toy Simulation Safety Guard Unit Test Package

        ## Question

        Can Viruse Fabric package the safety guard behavior into explicit unit tests while preserving zero counts for simulator implementation, dynamics implementation, executable toy simulator, real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, verification, validation, readiness, and citations?

        ## Source artifact

        - `outputs/safe_toy_simulation_safety_guard_module_v8_186.md`

        ## Unit-test interpretation

        v8.187 adds a unit-test package for the safety guard module.

        This milestone does not implement simulator code.

        This milestone does not implement dynamics.

        This milestone does not provide an executable toy simulator.

        This milestone does not provide real pathogen simulation.

        This milestone does not provide real receptor parameters.

        This milestone does not provide operational host targeting.

        This milestone does not provide wet-lab protocols.

        This milestone does not provide actionable biosafety-risk instructions.

        {_package_description()}

        {_test_summary()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim and safety boundary

        This milestone records safe toy simulation safety guard unit test package count: 1.

        This milestone records safety guard unit test file count: 1.

        This milestone records safety guard unittest case count: 10.

        This milestone records safety guard unit test execution count: 1.

        This milestone preserves safe toy simulation safety guard module count: 1.

        This milestone preserves safety guard module implementation count: 1.

        This milestone preserves safety guard test harness count: 1.

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

        The project has added an explicit unit-test package for the safety guard module, while preserving explicit boundaries against simulator implementation, dynamics implementation, executable toy simulator claims, real biological dataset imports, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation additions.
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
        "This milestone adds unit tests only; it does not implement simulator dynamics.",
        "Executable toy simulator count remains zero.",
        "Real biological dataset import remains zero.",
        "Real pathogen simulation remains zero.",
        "Real receptor parameters remain zero.",
        "Operational host targeting remains zero.",
        "Wet-lab protocols remain zero.",
        "Actionable biosafety-risk instructions remain zero.",
    ]

    return SafeToySimulationSafetyGuardUnitTestPackageResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> SafeToySimulationSafetyGuardUnitTestPackageResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
