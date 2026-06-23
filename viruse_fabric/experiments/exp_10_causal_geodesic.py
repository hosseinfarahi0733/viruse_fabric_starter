from __future__ import annotations

from rich.console import Console
from rich.table import Table

from viruse_fabric.causal.intervention import (
    shift_node_space,
    shift_node_time,
)
from viruse_fabric.experiments.exp_01_projection import build_demo_fabric
from viruse_fabric.geometry.causal_geodesic import CausalGeodesicAnalyzer
from viruse_fabric.geometry.spacetime_coupling import add_biological_spacetime_couplings

console = Console()


def print_edge_table(title: str, geodesic) -> None:
    table = Table(title=title)
    table.add_column("Edge")
    table.add_column("Kind")
    table.add_column("Raw penalty")
    table.add_column("Gravity pull")
    table.add_column("Final cost")

    for edge in geodesic.edges:
        table.add_row(
            f"{edge.source} → {edge.target}",
            edge.kind,
            f"{edge.raw_penalty:.3f}",
            f"{edge.gravity_pull:.3f}",
            f"{edge.final_cost:.3f}",
        )

    console.print(table)


def main() -> None:
    analyzer = CausalGeodesicAnalyzer(attraction_strength=0.65)

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
        analyzer.compare("original", original, source="A", target="E"),
        analyzer.compare("coupled", coupled, source="A", target="E"),
        analyzer.compare("B_spatial_displaced", b_spatial, source="A", target="E"),
        analyzer.compare("C_t2_earlier", c_t2, source="A", target="E"),
    ]

    console.rule("Experiment 10: Causal Geodesic / Path Bending")
    console.print(
        "Question: Do causal paths bend toward low-cost, high-gravity routes through the fabric?"
    )

    summary = Table(title="Causal geodesic comparison")
    summary.add_column("Case")
    summary.add_column("Path")
    summary.add_column("Total cost")
    summary.add_column("Raw penalty")
    summary.add_column("Gravity pull")
    summary.add_column("Dominant attractors")
    summary.add_column("Total curvature")
    summary.add_column("Interpretation")

    for case in cases:
        geodesic = case.geodesic
        summary.add_row(
            case.name,
            geodesic.path_label,
            f"{geodesic.total_cost:.3f}",
            f"{geodesic.total_raw_penalty:.3f}",
            f"{geodesic.total_gravity_pull:.3f}",
            ", ".join(case.dominant_attractors) or "none",
            f"{case.total_curvature:.3f}",
            geodesic.interpretation,
        )

    console.print(summary)

    for case in cases:
        print_edge_table(
            f"Edges for {case.name}: {case.geodesic.path_label}",
            case.geodesic,
        )

    console.rule("Theory note")
    console.print(
        "A causal path is not simply the first visible chain of events. "
        "It is the route where constraint cost and causal gravity combine. "
        "This gives a first computational model of apparent targeting: "
        "paths that are cheaper and more gravitationally supported become more observable."
    )


if __name__ == "__main__":
    main()
