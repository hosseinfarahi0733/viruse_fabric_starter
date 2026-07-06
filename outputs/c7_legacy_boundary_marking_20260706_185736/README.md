# C7 Legacy Boundary Marking

## Purpose

This audit marks the boundary between the post-v17.4 natural main route and the old legacy strong/collapsing routes.

## Main route after v17.4

```text
FullNaturalProofSpine
naturalBase_to_restrictedProofSpineTarget
```

## Legacy route indicators

```text
hEffectBase
hTypedUpdate
hBaseScore
hUpdatedScore
thresholdHi ≤ baseEffect
baseEffect ≤ thresholdLo
thresholdHi ≤ productScore x
productScore x ≤ thresholdLo
canonicalBaseEffect
canonicalRaw_to_restrictedProofSpineTarget
components_to_restrictedProofSpineTarget
```

## Interpretation

Legacy routes may remain in the repository for historical and dependency reasons.

They should not be used as the main scientific route after v17.4.0.

No file should be deleted until dependency-level safety is established.
