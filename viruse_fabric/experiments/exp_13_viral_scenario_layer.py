from __future__ import annotations

from rich.console import Console
from rich.table import Table

from viruse_fabric.biology.apparent_targeting import ApparentTargetingAnalyzer
from viruse_fabric.biology.viral_scenarios import build_viral_pattern_scenarios
from viruse_fabric.geometry.attractor_classifier import AttractorTypeClassifier
from viruse_fabric.geometry.causal_curvature import CausalCurvatureAnalyzer

console = Console()


def warning_from_roles(*, tension_wells: list[str], strained_gateways: list[str], score: float) -> str:
    if tension_wells:
        return "crisis-dominated route; apparent targeting collapses"
    if strained_gateways:
        return "structured but costly route; targeting remains weak"
    if score >= 75:
        return "coherent route; high apparent targeting"
    if score >= 50:
        return "partial route coherence"
    return "weak route coherence"


def main() -> None:
    targeting_analyzer = ApparentTargetingAnalyzer()
    classifier = AttractorTypeClassifier()
    curvature_analyzer = CausalCurvatureAnalyzer()

    scenarios = build_viral_pattern_scenarios()

    console.rule("Experiment 13: Viral Pattern Scenario Layer")
    console.print(
        "Question: Can the abstract fabric be read as safe viral-pattern scenarios "
        "without assigning intention or using real pathogen parameters?"
    )

    summary = Table(title="Viral-pattern scenario summary")
    summary.add_column("Scenario")
    summary.add_column("Path")
    summary.add_column("Targeting score")
    summary.add_column("Targeting interpretation")
    summary.add_column("Constructive")
    summary.add_column("Tension wells")
    summary.add_column("Strained gateways")
    summary.add_column("Dominant curvature")
    summary.add_column("Warning")

    details = Table(title="Scenario readings")
    details.add_column("Scenario")
    details.add_column("Biological-facing reading")
    details.add_column("Abstract question")
    details.add_column("Expected mechanism")
    details.add_column("Safety note")

    node_table = Table(title="Node role dictionary")
    node_table.add_column("Node")
    node_table.add_column("Event label")
    node_table.add_column("Biological-facing role")
    node_table.add_column("Safe abstraction")

    role_source = scenarios[0].fabric
    for node_id in ["A", "B", "C", "D", "E"]:
        node = role_source.nodes[node_id]
        node_table.add_row(
            node_id,
            str(node.state.get("event", node.label)),
            str(node.state.get("biological_role", "")),
            str(node.state.get("safe_abstraction", "")),
        )

    for scenario in scenarios:
        targeting = targeting_analyzer.analyze(
            scenario.fabric,
            case_name=scenario.name,
        )
        classification = classifier.classify(
            scenario.fabric,
            case_name=scenario.name,
        )
        curvature = curvature_analyzer.analyze(scenario.fabric)

        dominant = ", ".join(
            node.node_id for node in curvature.dominant_nodes
        ) or "none"

        warning = warning_from_roles(
            tension_wells=classification.tension_wells,
            strained_gateways=classification.strained_gateways,
            score=targeting.score,
        )

        summary.add_row(
            scenario.name,
            " → ".join(targeting.path),
            f"{targeting.score:.2f}",
            targeting.interpretation,
            ", ".join(classification.constructive_nodes) or "none",
            ", ".join(classification.tension_wells) or "none",
            ", ".join(classification.strained_gateways) or "none",
            dominant,
            warning,
        )

        details.add_row(
            scenario.name,
            scenario.biological_reading,
            scenario.abstract_question,
            scenario.expected_mechanism,
            scenario.safety_note,
        )

    console.print(node_table)
    console.print(summary)
    console.print(details)

    console.rule("Theory note")
    console.print(
        "The viral-pattern layer does not make the model biologically operational. "
        "It translates abstract causal roles into safe biological-facing language. "
        "Apparent targeting remains a property of route coherence, constructive attractors, "
        "and constraint filtering, not viral intention."
    )


if __name__ == "__main__":
    main()
