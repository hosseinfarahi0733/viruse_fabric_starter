from __future__ import annotations

from viruse_fabric.writing.persian_theory_chapter_exporter import (
    PersianTheoryChapterExporter,
)


def main() -> None:
    print("Experiment 18: Persian Theory Chapter Exporter")
    print("Question: Can the simulator export a Persian theory chapter from its results?")

    exporter = PersianTheoryChapterExporter()
    result = exporter.export()

    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path}")
    print(f"Scenario count: {result.scenario_count}")
    print(f"Safety status: {result.safety_status}")
    print(f"Total findings: {result.total_findings}")
    print(f"Word count: {result.word_count}")
    print(f"Interpretation: {result.interpretation}")
    print("Theory note: The Persian exporter converts computational results into a Persian chapter draft.")


if __name__ == "__main__":
    main()
