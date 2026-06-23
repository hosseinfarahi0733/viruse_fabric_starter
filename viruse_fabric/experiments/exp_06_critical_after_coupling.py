from __future__ import annotations

from rich.console import Console
from rich.table import Table

from viruse_fabric.causal.counterfactual import counterfactual_delete
from viruse_fabric.causal.intervention import (
    compare_intervention,
    shift_node_space,
    shift_node_time,
)
from viruse_fabric.engines.critical_engine import CriticalEngine
from viruse_fabric.experiments.exp_01_projection import build_demo_fabric
from viruse_fabric.geometry.spacetime_coupling import add_biological_spacetime_couplings

console = Console()


def build_coupled_intervention_results(fabric):
    return [
        compare_intervention(
            name="C_t2_earlier_with_coupling",
            description="Move regulatory recontextualization earlier on t2 after coupling.",
            base=fabric,
            intervened=shift_node_time(fabric, "C", dt2=-10.0),
        ),
        compare_intervention(
            name="D_t3_earlier_with_coupling",
            description="Move hereditary stabilization earlier on t3 after coupling.",
            base=fabric,
            intervened=shift_node_time(fabric, "D", dt3=-9.0),
        ),
        compare_intervention(
            name="B_spatial_displaced_with_coupling",
            description="Move B away in physical space after biological space-time coupling.",
            base=fabric,
            intervened=shift_node_space(fabric, "B", dx=4.0, dy=2.0, dz=1.0),
        ),
    ]


def main() -> None:
    base_fabric = build_demo_fabric()
    coupled_fabric = add_biological_spacetime_couplings(base_fabric)

    counterfactual_results = [
        counterfactual_delete(coupled_fabric, node_id)
        for node_id in coupled_fabric.nodes
    ]

    intervention_results = build_coupled_intervention_results(coupled_fabric)

    engine = CriticalEngine()
    engine.evaluate_counterfactuals(counterfactual_results)
    engine.evaluate_interventions(intervention_results)
    engine.evaluate_model_balance(intervention_results=intervention_results)

    console.rule("Experiment 06: Critical Review After Space-Time Coupling")
    console.print(
        "Question: Did biological space-time coupling reduce earlier critical warnings?"
    )

    intervention_table = Table(title="Coupled intervention summary")
    intervention_table.add_column("Intervention")
    intervention_table.add_column("ΔEnergy")
    intervention_table.add_column("Projection distance")
    intervention_table.add_column("Interpretation")

    for result in intervention_results:
        intervention_table.add_row(
            result.name,
            f"{result.energy_delta:.3f}",
            f"{result.projection_distance:.3f}",
            result.interpretation,
        )

    console.print(intervention_table)

    findings_table = Table(title="Critical findings after coupling")
    findings_table.add_column("Code")
    findings_table.add_column("Severity")
    findings_table.add_column("Title")
    findings_table.add_column("Evidence")
    findings_table.add_column("Recommendation")

    for finding in engine.findings:
        findings_table.add_row(
            finding.code,
            finding.severity,
            finding.title,
            finding.evidence,
            finding.recommendation,
        )

    console.print(findings_table)

    console.rule("Critical verdict after coupling")
    console.print(f"Score: {engine.summary_score():.1f}")
    console.print(f"Verdict: {engine.verdict()}")

    console.rule("Theory note")
    console.print(
        "Adding space-time coupling should reduce weak-space warnings, "
        "but it may reveal a new issue: projection order alone hides deep fabric changes."
    )


if __name__ == "__main__":
    main()
