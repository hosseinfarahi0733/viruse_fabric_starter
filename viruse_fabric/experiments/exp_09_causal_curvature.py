from __future__ import annotations

from rich.console import Console
from rich.table import Table

from viruse_fabric.causal.intervention import (
    shift_node_space,
    shift_node_time,
)
from viruse_fabric.experiments.exp_01_projection import build_demo_fabric
from viruse_fabric.geometry.causal_curvature import CausalCurvatureAnalyzer
from viruse_fabric.geometry.spacetime_coupling import add_biological_spacetime_couplings

console = Console()


def print_report(title: str, report) -> None:
    console.rule(title)

    console.print(f"Total curvature: {report.total_curvature:.3f}")
    console.print(f"Max curvature: {report.max_curvature:.3f}")
    console.print(f"Curvature entropy: {report.curvature_entropy:.3f}")
    console.print(f"Interpretation: {report.interpretation}")

    dominant = ", ".join(node.node_id for node in report.dominant_nodes) or "none"
    console.print(f"Dominant causal attractors: {dominant}")

    table = Table(title="Node curvature / causal gravity")
    table.add_column("Node")
    table.add_column("Kind")
    table.add_column("Degree")
    table.add_column("Local tension")
    table.add_column("Pressure")
    table.add_column("Curvature")
    table.add_column("Causal gravity")
    table.add_column("Interpretation")

    for node in report.nodes:
        table.add_row(
            node.node_id,
            node.kind,
            str(node.degree),
            f"{node.local_tension:.3f}",
            f"{node.fabric_pressure:.3f}",
            f"{node.curvature:.3f}",
            f"{node.causal_gravity:.3f}",
            node.interpretation,
        )

    console.print(table)


def main() -> None:
    analyzer = CausalCurvatureAnalyzer()

    original = build_demo_fabric()
    coupled = add_biological_spacetime_couplings(original)

    spatial_intervention = shift_node_space(
        coupled,
        "B",
        dx=4.0,
        dy=2.0,
        dz=1.0,
    )

    t2_intervention = shift_node_time(
        coupled,
        "C",
        dt2=-10.0,
    )

    console.rule("Experiment 09: Causal Curvature / Causal Gravity")
    console.print(
        "Question: Which nodes bend the causal fabric by concentrating tension, "
        "pressure, and connectivity?"
    )

    original_report = analyzer.analyze(original)
    coupled_report = analyzer.analyze(coupled)
    spatial_report = analyzer.analyze(spatial_intervention)
    t2_report = analyzer.analyze(t2_intervention)

    print_report("Case 01: Original MVP fabric", original_report)
    print_report("Case 02: Coupled fabric", coupled_report)
    print_report("Case 03: Spatial displacement of B after coupling", spatial_report)
    print_report("Case 04: C shifted earlier on t2 after coupling", t2_report)

    summary = Table(title="Curvature comparison")
    summary.add_column("Case")
    summary.add_column("Total curvature")
    summary.add_column("Entropy")
    summary.add_column("Dominant attractors")

    for name, report in [
        ("original", original_report),
        ("coupled", coupled_report),
        ("B spatial displaced", spatial_report),
        ("C t2 earlier", t2_report),
    ]:
        summary.add_row(
            name,
            f"{report.total_curvature:.3f}",
            f"{report.curvature_entropy:.3f}",
            ", ".join(node.node_id for node in report.dominant_nodes) or "none",
        )

    console.print(summary)

    console.rule("Theory note")
    console.print(
        "Causal gravity is modeled as curvature produced by tension, pressure, and connectivity. "
        "A node with high causal gravity is not simply earlier in time; it organizes nearby paths "
        "inside the fabric."
    )


if __name__ == "__main__":
    main()
