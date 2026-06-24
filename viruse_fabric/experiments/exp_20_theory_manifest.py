from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.theory_manifest import TheoryManifestExporter


REQUIRED_SECTIONS = (
    "## Core Claim",
    "## What the Project Explains",
    "## What the Project Does Not Claim",
    "## Computational Evidence So Far",
    "## Conceptual Boundary",
    "## Biological Safety Boundary",
    "## Why This Is Not Just Metaphor",
    "## Open Weak Points",
    "## Next Research Questions",
)


REQUIRED_BOUNDARY_PHRASES = (
    "does not currently claim empirical proof",
    "non-operational",
    "real pathogens",
    "real hosts",
    "laboratory protocols",
    "actionable biological procedures",
)


def main() -> None:
    print("Experiment 20: Theory Manifest")
    print("Question: Can the project state its claims, limits, evidence, and weak points directly?")

    exporter = TheoryManifestExporter()
    result = exporter.export()

    path = Path(result.output_path)
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    missing_sections = [section for section in REQUIRED_SECTIONS if section not in text]
    missing_boundary_phrases = [
        phrase for phrase in REQUIRED_BOUNDARY_PHRASES if phrase not in text
    ]

    overindented_lines = [
        index
        for index, line in enumerate(lines, 1)
        if line.startswith("            ")
    ]

    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path}")
    print(f"Section count: {result.section_count}")
    print(f"Claim count: {result.claim_count}")
    print(f"Weak point count: {result.weak_point_count}")
    print(f"Word count: {result.word_count}")
    print(f"Missing sections: {len(missing_sections)}")
    print(f"Missing boundary phrases: {len(missing_boundary_phrases)}")
    print(f"Overindented lines: {len(overindented_lines)}")
    print(f"Interpretation: {result.interpretation}")

    if missing_sections:
        print("Missing required sections:")
        for section in missing_sections:
            print(f"- {section}")

    if missing_boundary_phrases:
        print("Missing required boundary phrases:")
        for phrase in missing_boundary_phrases:
            print(f"- {phrase}")

    if overindented_lines:
        print("Overindented line numbers:")
        for line_number in overindented_lines[:20]:
            print(f"- {line_number}")

    if missing_sections or missing_boundary_phrases or overindented_lines:
        raise SystemExit(1)

    print("Experiment 20 completed successfully.")


if __name__ == "__main__":
    main()
