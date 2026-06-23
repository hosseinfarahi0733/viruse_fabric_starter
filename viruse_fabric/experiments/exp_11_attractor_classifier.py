from __future__ import annotations

from rich.console import Console
from rich.table import Table

from viruse_fabric.causal.intervention import (
    shift_node_space,
    shift_node_time,
)
from viruse_fabric.experiments.exp_01_projection import build_demo_fabric
from viruse_fabric.geometry.attractor_classifier import AttractorTypeClassifier
from viruse_fabric.geometry.spacetime_coupling import add_biological_spacetime_couplings

console = Console()


def print_report(report) -> None:
    console.rule(f"Case: {report.case_name}")
    console.print(f"Geodesic path: {' → '.join(report.geodesic_path)}")
    console.print(
        f"Dominant attractors by curvature: {', '.join(report.dominant_attractors) or 'none'}"
    )
    console.print(f"Interpretation: {report.interpretation}")

    table = Table(title="Attractor type classification")
    table.add_column("Node")
    table.add_column("Kind")
    table.add_column("Type")
    table.add_column("In path")
    table.add_column("Path index")
    table.add_column("Gravity")
    table.add_column("Gravity ratio")
    table.add_column("Path cost")
    table.add_column("Explanation")

    for item in report.classifications:
        table.add_row(
            item.node_id,
            item.kind,
            item.attractor_type,
            "yes" if item.in_geodesic else "no",
            "" if item.path_index is None else str(item.path_index),
            f"{item.causal_gravity:.3f}",
            f"{item.gravity_ratio:.3f}",
            f"{item.incident_path_cost:.3f}",
            item.explanation,
        )

    console.print(table)


def main() -> None:
    classifier = AttractorTypeClassifier()

    original = build_demo_fabric()
    coupled = add_biological_spacetime_couplings(original)

    b_spatial = shift_node_space(
        coupled,
        "B",
        dx=4.0,
        dy=2.0,
        dz=1.0,
    )

    c_t2 = shift_node_time(
        coupled,
        "C",
        dt2=-10.0,
    )

    cases = [
        classifier.classify(original, case_name="original"),
        classifier.classify(coupled, case_name="coupled"),
        classifier.classify(b_spatial, case_name="B_spatial_displaced"),
        classifier.classify(c_t2, case_name="C_t2_earlier"),
    ]

    console.rule("Experiment 11: Attractor Type Classifier")
    console.print(
        "Question: Are dominant causal attractors constructive path organizers, "
        "strained gateways, or avoided tension wells?"
    )

    for report in cases:
        print_report(report)

    summary = Table(title="Attractor role summary")
    summary.add_column("Case")
    summary.add_column("Path")
    summary.add_column("Constructive")
    summary.add_column("Tension wells")
    summary.add_column("Strained gateways")
    summary.add_column("Interpretation")

    for report in cases:
        summary.add_row(
            report.case_name,
            " → ".join(report.geodesic_path),
            ", ".join(report.constructive_nodes) or "none",
            ", ".join(report.tension_wells) or "none",
            ", ".join(report.strained_gateways) or "none",
            report.interpretation,
        )

    console.print(summary)

    console.rule("Theory note")
    console.print(
        "Not every causal attractor is a destination. "
        "Some attractors organize stable routes; others become crisis centers that geodesics avoid. "
        "This distinction is essential for modeling apparent viral targeting without assigning intention."
    )


if __name__ == "__main__":
    main()
