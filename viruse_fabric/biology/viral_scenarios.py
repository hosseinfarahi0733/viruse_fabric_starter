from __future__ import annotations

from dataclasses import dataclass
import copy

from viruse_fabric.core.fabric import Fabric
from viruse_fabric.causal.intervention import shift_node_space, shift_node_time
from viruse_fabric.experiments.exp_01_projection import build_demo_fabric
from viruse_fabric.geometry.spacetime_coupling import add_biological_spacetime_couplings


@dataclass
class ViralPatternScenario:
    name: str
    fabric: Fabric
    biological_reading: str
    abstract_question: str
    expected_mechanism: str
    safety_note: str


NODE_ANNOTATIONS = {
    "A": {
        "event": "exposure / boundary contact",
        "biological_role": "contact-like physical boundary event",
        "safe_abstraction": "a non-operational contact proxy",
    },
    "B": {
        "event": "compatibility transition",
        "biological_role": "receptor-like compatibility or cell-state transition",
        "safe_abstraction": "an abstract compatibility gate, not a real receptor model",
    },
    "C": {
        "event": "regulatory context shift",
        "biological_role": "information-context reorganization",
        "safe_abstraction": "an abstract regulatory shift, not a molecular protocol",
    },
    "D": {
        "event": "persistence stabilization",
        "biological_role": "hereditary or persistence-like stabilization",
        "safe_abstraction": "a stability proxy, not a replication mechanism",
    },
    "E": {
        "event": "observer-visible outcome",
        "biological_role": "observable phenotype-like projection",
        "safe_abstraction": "a visible endpoint proxy",
    },
}


def annotate_viral_pattern(fabric: Fabric, *, scenario_name: str) -> Fabric:
    """Attach safe biological-facing labels to an abstract fabric.

    This layer is deliberately non-operational:
    it does not model real pathogens, protocols, doses, hosts, or lab actions.
    It only makes the abstract causal roles easier to read.
    """

    f = copy.deepcopy(fabric)

    for node_id, annotation in NODE_ANNOTATIONS.items():
        if node_id not in f.nodes:
            continue

        node = f.nodes[node_id]
        node.state.update(annotation)
        node.state["scenario"] = scenario_name
        node.label = annotation["event"]

    return f


def build_viral_pattern_scenarios() -> list[ViralPatternScenario]:
    baseline = annotate_viral_pattern(
        build_demo_fabric(),
        scenario_name="abstract_baseline",
    )

    coupled = annotate_viral_pattern(
        add_biological_spacetime_couplings(build_demo_fabric()),
        scenario_name="coherent_viral_pattern",
    )

    spatial_break = annotate_viral_pattern(
        shift_node_space(
            add_biological_spacetime_couplings(build_demo_fabric()),
            "B",
            dx=4.0,
            dy=2.0,
            dz=1.0,
        ),
        scenario_name="spatial_context_break",
    )

    regulatory_time_break = annotate_viral_pattern(
        shift_node_time(
            add_biological_spacetime_couplings(build_demo_fabric()),
            "C",
            dt2=-10.0,
        ),
        scenario_name="regulatory_time_disruption",
    )

    return [
        ViralPatternScenario(
            name="abstract_baseline",
            fabric=baseline,
            biological_reading=(
                "A weakly organized abstract viral-pattern baseline. "
                "The path has structure, but it passes through a costly strained gateway."
            ),
            abstract_question=(
                "What does the system look like before biological space-time coupling is made coherent?"
            ),
            expected_mechanism="strained gateway rather than stable targeting",
            safety_note="Conceptual model only; not a real pathogen or host model.",
        ),
        ViralPatternScenario(
            name="coherent_viral_pattern",
            fabric=coupled,
            biological_reading=(
                "A coherent abstract viral-pattern route where compatibility, regulation, "
                "stabilization, and visible outcome align."
            ),
            abstract_question=(
                "Can a coherent constraint fabric make a route look target-like without intention?"
            ),
            expected_mechanism="high apparent targeting through constructive attractor support",
            safety_note="Safe abstraction; no actionable biological parameters.",
        ),
        ViralPatternScenario(
            name="spatial_context_break",
            fabric=spatial_break,
            biological_reading=(
                "A disrupted compatibility-context scenario. The compatibility-like node becomes "
                "a high-tension attractor that the geodesic avoids."
            ),
            abstract_question=(
                "What happens when the compatibility transition becomes spatially incoherent?"
            ),
            expected_mechanism="tension well formation and route avoidance",
            safety_note="Safe abstraction; spatial displacement is mathematical, not biological.",
        ),
        ViralPatternScenario(
            name="regulatory_time_disruption",
            fabric=regulatory_time_break,
            biological_reading=(
                "A disrupted regulatory-time scenario. The information-context node becomes "
                "a high-tension attractor rather than a stable route."
            ),
            abstract_question=(
                "What happens when regulatory timing becomes incoherent with the rest of the fabric?"
            ),
            expected_mechanism="regulatory tension well and loss of apparent targeting",
            safety_note="Safe abstraction; timing is model-time, not a biological intervention.",
        ),
    ]
