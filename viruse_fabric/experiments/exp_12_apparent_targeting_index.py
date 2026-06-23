from __future__ import annotations

from rich.console import Console
from rich.table import Table

from viruse_fabric.biology.apparent_targeting import ApparentTargetingAnalyzer
from viruse_fabric.causal.intervention import (
    shift_node_space,
    shift_node_time,
)
from viruse_fabric.experiments.exp_01_projection import build_demo_fabric
from viruse_fabric.geometry.spacetime_coupling import add_biological_spacetime_couplings

console = Console()


def main() -> None:
    analyzer = ApparentTargetingAnalyzer()

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
        analyzer.analyze(original, case_name="original"),
        analyzer.analyze(coupled, case_name="coupled"),
        analyzer.analyze(b_spatial, case_name="B_spatial_displaced"),
        analyzer.analyze(c_t2, case_name="C_t2_earlier"),
    ]

    console.rule("Experiment 12: Apparent Targeting Index")
    console.print(
        "Question: When does a causal path appear target-like without assigning intention?"
    )

    table = Table(title="Apparent targeting index")
    table.add_column("Case")
    table.add_column("Path")
    table.add_column("Score")
    table.add_column("Constructive")
    table.add_column("Coverage")
    table.add_column("Gravity alignment")
    table.add_column("Cost efficiency")
    table.add_column("Tension penalty")
    table.add_column("Strained penalty")
    table.add_column("Interpretation")

    for result in cases:
        table.add_row(
            result.case_name,
            " → ".join(result.path),
            f"{result.score:.2f}",
            f"{result.constructive_support:.3f}",
            f"{result.path_coverage:.3f}",
            f"{result.gravity_alignment:.3f}",
            f"{result.cost_efficiency:.3f}",
            f"{result.tension_well_penalty:.3f}",
            f"{result.strained_gateway_penalty:.3f}",
            result.interpretation,
        )

    console.print(table)

    detail = Table(title="Targeting mechanism details")
    detail.add_column("Case")
    detail.add_column("Constructive nodes")
    detail.add_column("Tension wells")
    detail.add_column("Strained gateways")
    detail.add_column("Explanation")

    for result in cases:
        detail.add_row(
            result.case_name,
            ", ".join(result.constructive_nodes) or "none",
            ", ".join(result.tension_wells) or "none",
            ", ".join(result.strained_gateways) or "none",
            result.explanation,
        )

    console.print(detail)

    console.rule("Theory note")
    console.print(
        "Apparent targeting is modeled as route coherence through constructive attractors, "
        "not as intention. A path may look target-like when fabric constraints make it coherent, "
        "efficient, and observable."
    )


if __name__ == "__main__":
    main()
