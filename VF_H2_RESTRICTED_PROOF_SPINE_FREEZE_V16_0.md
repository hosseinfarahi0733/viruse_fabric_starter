# VF-H2 v16.0.0 — Restricted Proof Spine Freeze and Audit

## Status

This file freezes the restricted proof spine verified through:

```text
v15.0.0 … v15.9.0
```

The freeze point is:

```text
base tag: v15.9.0
expected HEAD: 48f38a6
new tag: v16.0.0
```

## Main frozen theorem surface

The citeable Lean surface for the current restricted proof spine is:

```lean
VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpine_rawEqualities_to_target
VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpine_rawEqualities_to_updatedBounds
VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpine_rawEqualities_to_updatedLower
VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpine_rawEqualities_to_updatedUpper
```

## Frozen result

The frozen restricted result proves:

```text
raw typed/product update-score equalities over ProductStateTransport.productToTyped
+ baseEffect = productScore x
+ base strong bridge inputs
+ restrictedParamsScorePreservingUpdatePolicy
+ thresholdLo ≤ thresholdHi

→ base and updated score-window target
→ thresholdLo ≤ productScore (productUpdate x)
→ productScore (productUpdate x) ≤ thresholdHi
```

## Proven

The following have Lean-checked support in the v15 proof spine:

```text
restricted params bridge core pivot
restricted params update-score bridge
restricted params update-score transport
restricted params update-score bound
score-effect binding
score-window construction
score-window preservation
score-preserving update transfer
score-preservation policy discharge
policy end-to-end score-window theorem
```

## Still assumed

The current frozen result still assumes:

```text
base strong bridge inputs
restrictedParamsScorePreservingUpdatePolicy
raw typed/product update-score equalities
thresholdLo ≤ thresholdHi
```

These are explicit inputs to the frozen theorem surface.

## Not claimed

The freeze does not claim:

```text
the score-preserving policy is true for every productUpdate
base strong bridge inputs have been discharged
full VF-H2 theorem
unrestricted theorem
biological validation
empirical validation
submission-ready manuscript
```

## Remaining blockers

The two main blockers after v16.0.0 are:

```text
B1: discharge or justify base strong bridge inputs
B2: derive or instantiate restrictedParamsScorePreservingUpdatePolicy from concrete productUpdate/productScore behavior
```

## Recommended next proof work

After the freeze, theorem work should resume only if it reduces one of the two blockers:

```text
v16.1.0 — restricted score-preserving policy instantiation
or
v16.1.0 — restricted base strong bridge discharge
```

No new decorative target layer should be accepted.
