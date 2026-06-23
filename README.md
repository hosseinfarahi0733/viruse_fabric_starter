# Viruse Fabric Starter

A tiny starting implementation for the **Unified Causal Fabric** idea:

> Causality is not a chain; it is a geometry of constraints.

This starter is intentionally abstract and safe. It does **not** model real pathogens or give biological operational details. It demonstrates:

- 3 space + 3 model-time coordinates
- event nodes in a fabric
- constraints between events
- FabricEnergy
- CausalMass by node deletion
- observer projection into a one-time narrative
- apparent past recontextualization

## Install

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e .
```

## Run

```bash
python -m viruse_fabric.experiments.exp_01_projection
```

Outputs:

- console report
- `outputs/projection_timeline.png`
- `outputs/causal_mass.png`

## Project logic

- `EventNode`: node in 6D fabric `(x,y,z,t1,t2,t3)`
- `Constraint`: compatibility/necessity relation between two nodes
- `Fabric`: stores nodes and constraints
- `FabricEnergy`: penalty for violated constraints and instability
- `CausalMass`: energy change when a node is removed
- `ObserverProjection`: compresses 3 model-times into one perceived time

## Next theory steps

1. Add nonlinear constraint tensors.
2. Add curvature-like causal mass fields.
3. Add several observer projections.
4. Add a critical engine that warns against false cause claims.
5. Turn experiments into book sections.
