# VF-H2 v16.1.0 — Restricted Score-Preserving Policy Instantiation

## Status

This milestone reduces blocker B2 from v16.0.0.

It does not prove that every product update preserves score.

It provides concrete sufficient conditions under which the score-preserving update policy used by the frozen proof spine is instantiated.

## Instantiated policy

The v16.0 frozen theorem required:

```text
restrictedParamsScorePreservingUpdatePolicy
```

v16.1 proves this policy from either:

```text
restrictedParamsIdentityLikeUpdate
```

meaning:

```text
∀ y : p.State, productUpdate y = y
```

or:

```text
restrictedParamsScoreKeyPreservingUpdateCondition
```

meaning that score factors through a key and update preserves that key.

## Main theorem surface

```lean
VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_identityLikeUpdate_to_scorePreservingPolicy
VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_scoreKeyPreservingUpdateCondition_to_scorePreservingPolicy
VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedProofSpine_rawEqualities_and_identityLikeUpdate_to_updatedBounds
VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedProofSpine_rawEqualities_and_scoreKeyCondition_to_updatedBounds
```

## Proven

The following sufficient policy instantiations are Lean-checked:

```text
identity-like update implies score-preserving policy
score-key preserving update condition implies score-preserving policy
```

and each can be connected to the v16.0 frozen proof spine.

## Still assumed

The current branch still assumes:

```text
base strong bridge inputs
raw typed/product update-score equalities
thresholdLo ≤ thresholdHi
```

For the score-key branch, it also assumes the score-key factorization and key-preservation condition.

## Not claimed

This milestone does not claim:

```text
all productUpdate functions are identity-like
all productUpdate functions preserve a score key
the score-key condition has been derived from productUpdate internals
base strong bridge inputs have been discharged
full VF-H2 theorem
unrestricted theorem
biological validation
empirical validation
submission-ready manuscript
```

## Remaining blockers

After v16.1.0, the strongest remaining blockers are:

```text
B1: discharge or justify base strong bridge inputs
B3: instantiate raw typed/product update-score equalities from concrete typedUpdate/typedScore definitions
```
