# C12 - Active-Insensitive Score Preservation Impact Audit

## Objective

Record the scientific impact of C12 and C12.1.

C12 introduced active-insensitive score semantics.
C12.1 routed that semantics into the restricted proof spine for the concrete product update.

## Verified commits

d216dfc - Derive score preservation from active-insensitive score
449b9e6 - Route active-insensitive score to restricted proof spine

## Scientific result

Before C12, score preservation was available only as an abstract policy assumption or score-key condition.

After C12, for the concrete update productUpdateState p, score preservation is derivable from a semantic condition on productScore.

The semantic condition is that productScore is inactive-insensitive: if two states agree on inactive-coordinate values, then they have the same score.

Since productUpdateState preserves inactive-coordinate values, inactive-insensitive scores are preserved by productUpdateState.

## Assumption impact

A1 - Score Preservation
Status: partially discharged.

The old abstract obligation was pointwise score preservation:
for every y, productScore (productUpdate y) = productScore y.

The new C12 route proves this obligation for productUpdateState p from active-insensitive score semantics.

This is not a full unconditional discharge of A1.
It is a conditional semantic derivation for a meaningful class of scores.

A2 - ProductFixedSet
Status: still undischarged.

A3 - Natural base bounds
Status: still undischarged.

## Main new theorem route

ProductRestrictedParamsActiveInsensitiveScore.productUpdateState_scorePreservingPolicy_of_inactiveInsensitive

ProductRestrictedParamsActiveInsensitiveProofSpine.restrictedParams_activeInsensitiveScore_naturalBase_to_restrictedProofSpineTarget

## Overclaim policy

Allowed claim:
Score preservation is derived for concrete productUpdateState p under active-insensitive score semantics.

Forbidden claims:
- all score preservation is discharged
- ProductFixedSet is discharged
- natural base bounds are discharged
- VF-H2 is fully proved
- the model is submission-ready

## Tag assessment

A scientific tag is justified after this audit because C12 performs real partial assumption reduction for A1.

Recommended tag: v17.5.0

Reason: partial discharge of score preservation for concrete productUpdateState under active-insensitive score semantics.
