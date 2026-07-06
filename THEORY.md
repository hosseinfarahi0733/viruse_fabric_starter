# VF-H2 / Viruse Fabric — Theory Boundary after v17.4.0

## Status

The current formal milestone is `v17.4.0`.

The established theorem-level achievement is:

```text
The full restricted proof-spine target can be constructed from natural base interval assumptions,
under fixedness and score-preserving policy routes.
```

Main theorem surface:

```lean
VFH2.ProductRestrictedParamsFullNaturalProofSpine.restrictedParams_scoreKeyCondition_naturalBase_to_restrictedProofSpineTarget
```

Sanity / weak identity-like route:

```lean
VFH2.ProductRestrictedParamsFullNaturalProofSpine.restrictedParams_identityLikeUpdate_naturalBase_to_restrictedProofSpineTarget
```

## What the theory currently proves

The project currently proves a restricted formal proof-spine construction.

The proof-spine is no longer dependent on the old strong/collapsing base-window assumptions for the main route. Instead, the main v17.4 route uses the natural interval shape:

```lean
thresholdLo ≤ productScore x
productScore x ≤ thresholdHi
```

under:

```lean
hThreshold : thresholdLo ≤ thresholdHi
hFixed : fixed
restrictedParamsScoreKeyPreservingUpdateCondition
```

## What the theory does not yet prove

The project does not yet prove full VF-H2.

The following are not derived internally:

```text
- hFixed
- score-key preservation from domain dynamics
- natural base interval source
- domain semantics
- empirical validation
- manuscript readiness
```

## Intended scientific interpretation

The current formal development should be interpreted as a restricted formal spine.

It shows that, if a natural base score interval is available, and if fixedness and score-preserving policy assumptions hold, then the restricted proof-spine target can be constructed.

This is valuable because it removes the old collapsing score-window route from the main path.

## Current main route

```text
natural base interval
+ fixedness
+ score-key preserving update condition
→ natural updated bounds
→ full restricted proof-spine target
```

## Non-main route

The identity-like route remains a sanity route only.

It should not be presented as the scientific route because it does not explain why realistic domain updates preserve the relevant score keys.

## Next theory objective

The next scientific objective is not to add wrapper theorems.

The next scientific objective is:

```text
derive, remove, or sharply classify one fundamental assumption.
```

Priority assumptions:

```text
1. score-key preservation
2. hFixed
3. source of natural base interval
4. domain semantics
```
