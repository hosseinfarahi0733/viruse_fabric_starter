# Viruse Fabric / VFH2

## C133 semantic recovery

C133 restores the original constraint-geometry program with an explicit claim
boundary. The verified recovery layer treats `past`, `present`, and `future` as
three ordered **causal epochs**, not three physical time dimensions. It adds:

- a deterministic tri-temporal structural model;
- surgical downstream interventions;
- a no-retrocausality theorem;
- evidence-relative candidate pasts and strict observer recontextualization;
- a computable rectangle defect exactly characterized by the earlier
  adjacent-chain factorization theorem;
- an independent Python oracle with exhaustive Boolean fixtures.

Run the complete C133 verification with:

```bash
bash scripts/verify_c133.sh
```

See `docs/c133/SEMANTIC_CONTRACT_FA_EN.md` and
`docs/c133/CLAIM_BOUNDARY.md` before interpreting the results.

## Legacy conceptual prototype

A tiny starting implementation for the **Unified Causal Fabric** idea:

> Causality is not a chain; it is a geometry of constraints.

This starter is intentionally abstract and safe. It does **not** model real
pathogens or give biological operational details. The following objects are
legacy exploratory heuristics, not validated physical or causal quantities:

- 3 space + 3 legacy model-time coordinates
- event nodes in a fabric
- constraints between events
- a heuristic `FabricEnergy` loss
- a heuristic `CausalMass` node-deletion score
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

## Legacy project logic

- `EventNode`: node in 6D fabric `(x,y,z,t1,t2,t3)`
- `Constraint`: compatibility/necessity relation between two nodes
- `Fabric`: stores nodes and constraints
- `FabricEnergy`: legacy penalty for violated constraints and instability
- `CausalMass`: legacy deletion score; not a physical mass or causal estimand
- `ObserverProjection`: compresses 3 model-times into one perceived time

## Historical theory notes

These historical directions are retained for provenance. C133 supersedes them
as the active scientific route: semantics first, then preregistered public-data
validation, and only then stronger physical or biological interpretation.
