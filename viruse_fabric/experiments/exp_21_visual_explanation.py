from __future__ import annotations

from pathlib import Path

from viruse_fabric.visualization.fabric_diagram import FabricDiagramRenderer


REQUIRED_REPORT_PHRASES = (
    "computed paths",
    "apparent targeting",
    "observer misreading",
    "constructive attractor",
    "tension well",
    "non-operational",
    "real pathogens",
    "laboratory protocols",
    "executable interventions",
)


def main() -> None:
    print("Experiment 21: Visual Explanation")
    print("Question: Can the project render a visual explanation tied to paths, scores, and attractor roles?")

    renderer = FabricDiagramRenderer()
    result = renderer.render()

    image_path = Path(result.image_path)
    report_path = Path(result.report_path)
    report_text = report_path.read_text(encoding="utf-8")

    missing_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES
        if phrase not in report_text
    ]

    image_exists = image_path.exists()
    report_exists = report_path.exists()
    image_size = image_path.stat().st_size if image_exists else 0
    report_size = report_path.stat().st_size if report_exists else 0

    print(f"Title: {result.title}")
    print(f"Image path: {result.image_path}")
    print(f"Report path: {result.report_path}")
    print(f"Scenario count: {result.scenario_count}")
    print(f"Node count: {result.node_count}")
    print(f"Edge count: {result.edge_count}")
    print(f"Image exists: {image_exists}")
    print(f"Image size: {image_size}")
    print(f"Report exists: {report_exists}")
    print(f"Report size: {report_size}")
    print(f"Missing required report phrases: {len(missing_phrases)}")
    print(f"Visual complexity: {renderer.approximate_visual_complexity():.3f}")
    print(f"Interpretation: {result.interpretation}")

    if missing_phrases:
        print("Missing phrases:")
        for phrase in missing_phrases:
            print(f"- {phrase}")

    if not image_exists or image_size <= 0:
        raise SystemExit("visual diagram image was not generated")

    if not report_exists or report_size <= 0:
        raise SystemExit("visual explanation report was not generated")

    if missing_phrases:
        raise SystemExit(1)

    print("Experiment 21 completed successfully.")


if __name__ == "__main__":
    main()
