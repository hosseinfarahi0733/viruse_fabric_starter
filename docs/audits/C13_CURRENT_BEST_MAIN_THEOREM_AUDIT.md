# C13 - Current Best Main Theorem Front Door Audit

## Objective

Record the scientific and architectural role of C13.

C13 introduces a reviewer-facing front-door theorem for the current best post-v17.5.0 route.

## Commit

fa75b9f - Add current best main theorem front door

## Main theorem

ProductRestrictedParamsCurrentBestMainTheorem.restrictedParams_currentBestMainTheorem

## Scientific role

C13 packages the current best theorem route into a clean front-door statement.

It specializes the update to concrete productUpdateState p.

It uses active-insensitive score semantics instead of abstract score-key preservation.

It specializes fixedness to the concrete semantic predicate ProductFixedSet p x.

It still assumes ProductFixedSet p x and natural base bounds.

## Assumption impact

Reduced assumptions: none newly reduced by C13.

C13 relies on the v17.5.0 / C12 reduction route for A1.

Remaining assumptions:
- A2: ProductFixedSet p x remains undischarged.
- A3: natural base bounds remain undischarged.

## Correct claim

The current best main theorem proves the restricted proof-spine target for concrete productUpdateState p under active-insensitive score semantics, ProductFixedSet p x, and natural base bounds.

## Forbidden claims

- C13 does not discharge ProductFixedSet.
- C13 does not discharge natural base bounds.
- C13 does not prove VF-H2 unconditionally.
- C13 is not a new scientific tag milestone.

## Tag policy

No tag is justified for C13.

Reason: C13 improves exposition and theorem discoverability, but does not reduce a new fundamental assumption.

Last scientific tag remains v17.5.0.
