from __future__ import annotations

from rich.console import Console
from rich.table import Table

from viruse_fabric.causal.counterfactual import counterfactual_delete
from viruse_fabric.causal.intervention import (
    compare_intervention,
    scale_constraint_weight,
    shift_node_space,
    shift_node_time,
)
from viruse_fabric.engines.critical_engine import CriticalEngine
from viruse_fabric.experiments.exp_01_projection import build_demo_fabric

console = Console()


def build_intervention_results(fabric):
    return [
        compare_intervention(
            name="C_t2_earlier",
            description="Move regulatory recontextualization earlier on t2.",
            base=fabric,
            intervened=shift_node_time(fabric, "C", dt2=-10.0),
        ),
        compare_intervention(
            name="D_t3_earlier",
            description="Move hereditary stabilization earlier on t3.",
            base=fabric,
            intervened=shift_node_time(fabric, "D", dt3=-9.0),
        ),
        compare_intervention(
            name="A_D_tension_weaker",
            description="Weaken the long A→D tension constraint.",
            base=fabric,
            intervened=scale_constraint_weight(
                fabric,
                source="A",
                target="D",
                kind="tension",
                factor=0.20,
            ),
        ),
        compare_intervention(
            name="B_spatial_displaced",
            description="Move B away in physical space without changing time.",
            base=fabric,
            intervened=shift_node_space(fabric, "B", dx=4.0, dy=2.0, dz=1.0),
        ),
    ]


def main() -> None:
    fabric = build_demo_fabric()

    counterfactual_results = [
        counterfactual_delete(fabric, node_id)
        for node_id in fabric.nodes
    ]

    intervention_results = build_intervention_results(fabric)

    engine = CriticalEngine()
    engine.evaluate_counterfactuals(counterfactual_results)
    engine.evaluate_interventions(intervention_results)
    engine.evaluate_model_balance(intervention_results=intervention_results)

    console.rule("Experiment 04: Critical Engine")
    console.print(
        "Question: Can the simulator criticize its own causal interpretations?"
    )

    table = Table(title="Critical findings")
    table.add_column("Code")
    table.add_column("Severity")
    table.add_column("Title")
    table.add_column("Evidence")
    table.add_column("Recommendation")

    for finding in engine.findings:
        table.add_row(
            finding.code,
            finding.severity,
            finding.title,
            finding.evidence,
            finding.recommendation,
        )

    console.print(table)

    console.rule("Critical verdict")
    console.print(f"Score: {engine.summary_score():.1f}")
    console.print(f"Verdict: {engine.verdict()}")

    console.rule("Theory note")
    console.print(
        "A serious theory should not only produce explanations. "
        "It should produce warnings about when its explanations may be artifacts of the model."
    )


if __name__ == "__main__":
    main()
