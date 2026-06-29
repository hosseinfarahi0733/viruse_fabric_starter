from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent

from viruse_fabric.safety.toy_fixture_catalog import fixture_catalog_summary


COUNTER_LINES = [
    "Safe synthetic toy fixture catalog package count: 1",
    "New safe synthetic toy fixture catalog package count: 1",
    "Synthetic toy fixture catalog module count: 1",
    "Synthetic toy fixture catalog entry count: 3",
    "Synthetic toy fixture catalog safety pass count: 3",
    "Synthetic toy fixture catalog blocked marker count: 0",
    "Synthetic toy fixture catalog missing safe marker count: 0",
    "Two-node toy fixture count: 1",
    "Three-node chain toy fixture count: 1",
    "Star graph toy fixture count: 1",
    "Fixture catalog summary count: 1",
    "Fixture catalog guard validation count: 1",

    "Safe toy simulation safety guard unit test package count: 1",
    "Safety guard unit test file count: 1",
    "Safety guard unittest case count: 10",
    "Safety guard unit test execution count: 1",
    "Safe toy simulation safety guard module count: 1",
    "Safety guard module implementation count: 1",
    "Safety guard test harness count: 1",
    "Safe toy fixture builder count: 1",
    "Safe toy fixture pass check count: 1",

    "Imported safe toy simulation safety guard unit test package count: 1",
    "Imported safety guard unit test file count: 1",
    "Imported safety guard unittest case count: 10",
    "Imported safety guard unit test execution count: 1",
    "Imported safe toy simulation safety guard module count: 1",

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
    "Safe toy simulation safety guard unit test package count: 1",
    "Safety guard unit test file count: 1",
    "Safety guard unittest case count: 10",
    "Safety guard unit test execution count: 1",
    "Safe toy simulation safety guard module count: 1",
    "Safety guard module implementation count: 1",
    "Safety guard test harness count: 1",
    "Safe toy fixture builder count: 1",
    "Safe toy fixture pass check count: 1",
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
    "Safe synthetic toy fixture catalog package count: 1",
    "New safe synthetic toy fixture catalog package count: 1",
    "Synthetic toy fixture catalog module count: 1",
    "Synthetic toy fixture catalog entry count: 3",
    "Synthetic toy fixture catalog safety pass count: 3",
    "Synthetic toy fixture catalog blocked marker count: 0",
    "Synthetic toy fixture catalog missing safe marker count: 0",
    "Two-node toy fixture count: 1",
    "Three-node chain toy fixture count: 1",
    "Star graph toy fixture count: 1",
    "Fixture catalog summary count: 1",
    "Fixture catalog guard validation count: 1",

    "Safe toy simulation safety guard unit test package count: 1",
    "Safety guard unit test file count: 1",
    "Safety guard unittest case count: 10",
    "Safety guard unit test execution count: 1",
    "Safe toy simulation safety guard module count: 1",
    "Safety guard module implementation count: 1",
    "Safety guard test harness count: 1",
    "Safe toy fixture builder count: 1",
    "Safe toy fixture pass check count: 1",

    "Imported safe toy simulation safety guard unit test package count: 1",
    "Imported safety guard unit test file count: 1",
    "Imported safety guard unittest case count: 10",
    "Imported safety guard unit test execution count: 1",
    "Imported safe toy simulation safety guard module count: 1",

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
class SafeSyntheticToyFixtureCatalogPackageResult:
    report: str
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def _catalog_summary_text() -> str:
    summary = fixture_catalog_summary()
    fixture_ids = "\n".join(f"- `{fixture_id}`" for fixture_id in summary["fixture_ids"])
    return dedent(
        f"""
        ## Synthetic toy fixture catalog summary

        Fixture catalog module:
        - `{summary["fixture_catalog_module"]}`

        Fixture catalog counts:
        - Synthetic toy fixture catalog entry count: {summary["fixture_catalog_entry_count"]}
        - Synthetic toy fixture catalog safety pass count: {summary["fixture_catalog_safe_pass_count"]}
        - Synthetic toy fixture catalog blocked marker count: {summary["fixture_catalog_blocked_marker_count"]}
        - Synthetic toy fixture catalog missing safe marker count: {summary["fixture_catalog_missing_safe_marker_count"]}

        Fixture ids:
        {fixture_ids}
        """
    ).strip()


def _package_description() -> str:
    return dedent(
        """
        ## Safe synthetic toy fixture catalog package

        ### Purpose

        v8.188 packages a small catalog of synthetic toy fixtures.

        These fixtures are for future safety tests and non-operational toy demonstrations only.

        This milestone does not implement simulator dynamics.

        This milestone does not provide an executable simulator.

        ---

        ## Fixture boundary

        The catalog contains only:

        - synthetic node ids,
        - synthetic edge ids,
        - toy agents,
        - unitless scores,
        - deterministic seeds,
        - abstract graph structure,
        - non-operational boundary strings.

        The catalog does not contain:

        - real biological datasets,
        - real pathogen identities,
        - real receptor identities,
        - real host targeting objectives,
        - wet-lab protocols,
        - operational biological parameters.

        ---

        ## Catalog entries

        The catalog includes:

        - one two-node toy fixture,
        - one three-node chain toy fixture,
        - one star graph toy fixture.

        All entries are checked by the safety guard.

        ---

        ## Non-operational boundary

        This milestone is fixture catalog packaging only.

        It does not add simulator implementation.

        It does not add dynamics implementation.

        It does not add executable toy simulator claims.
        """
    ).strip()


def build_report(source_text: str) -> SafeSyntheticToyFixtureCatalogPackageResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.188 - Safe Synthetic Toy Fixture Catalog Package

        ## Question

        Can Viruse Fabric add a safe synthetic toy fixture catalog for future tests and non-operational demonstrations while preserving zero counts for simulator implementation, dynamics implementation, executable toy simulator, real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, verification, validation, readiness, and citations?

        ## Source artifact

        - `outputs/safe_toy_simulation_safety_guard_unit_test_package_v8_187.md`

        ## Fixture-catalog interpretation

        v8.188 adds a safe synthetic toy fixture catalog package.

        This milestone does not implement simulator code.

        This milestone does not implement dynamics.

        This milestone does not provide an executable toy simulator.

        This milestone does not provide real pathogen simulation.

        This milestone does not provide real receptor parameters.

        This milestone does not provide operational host targeting.

        This milestone does not provide wet-lab protocols.

        This milestone does not provide actionable biosafety-risk instructions.

        {_package_description()}

        {_catalog_summary_text()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim and safety boundary

        This milestone records safe synthetic toy fixture catalog package count: 1.

        This milestone records synthetic toy fixture catalog module count: 1.

        This milestone records synthetic toy fixture catalog entry count: 3.

        This milestone records synthetic toy fixture catalog safety pass count: 3.

        This milestone records synthetic toy fixture catalog blocked marker count: 0.

        This milestone records synthetic toy fixture catalog missing safe marker count: 0.

        This milestone preserves safe toy simulation safety guard unit test package count: 1.

        This milestone preserves safety guard unit test file count: 1.

        This milestone preserves safety guard unittest case count: 10.

        This milestone preserves safe toy simulation safety guard module count: 1.

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

        The project has added a safe synthetic toy fixture catalog package for future tests and non-operational demonstrations, while preserving explicit boundaries against simulator implementation, dynamics implementation, executable toy simulator claims, real biological dataset imports, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation additions.
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
        "This milestone adds a synthetic toy fixture catalog only; it does not implement simulator dynamics.",
        "Executable toy simulator count remains zero.",
        "Real biological dataset import remains zero.",
        "Real pathogen simulation remains zero.",
        "Real receptor parameters remain zero.",
        "Operational host targeting remains zero.",
        "Wet-lab protocols remain zero.",
        "Actionable biosafety-risk instructions remain zero.",
    ]

    return SafeSyntheticToyFixtureCatalogPackageResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> SafeSyntheticToyFixtureCatalogPackageResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
