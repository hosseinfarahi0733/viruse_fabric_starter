# VF-H2 Main Theorem

## Current best front-door theorem

ProductRestrictedParamsCurrentBestMainTheorem.restrictedParams_currentBestMainTheorem

## Informal statement

For the concrete update productUpdateState p, if the score is inactive-insensitive, the state is fixed on the active set, and the base score lies in the natural threshold window, then the restricted proof-spine target holds.

## Formal route

Inputs:
- p : ProductRestrictedParams
- x : p.State
- productScore : p.State -> Int
- thresholdLo thresholdHi : Int
- hThreshold : thresholdLo <= thresholdHi
- hScoreInactive : productScoreInactiveInsensitive p productScore
- hFixedSet : ProductFixedSet p x
- hBaseLowerNatural : thresholdLo <= productScore x
- hBaseUpperNatural : productScore x <= thresholdHi

Conclusion:
- restrictedProofSpineTarget for p, x, productUpdateState p, productScore, ProductFixedSet p x, and the threshold window.

## Scientific status

This is the cleanest current theorem after v17.5.0.

It uses the C12 active-insensitive score route, so it avoids the abstract score-key preservation premise for the concrete update.

It still depends on ProductFixedSet p x and natural base bounds.

Therefore, the project is still a conditional proof framework, not an unconditional full VF-H2 proof.

## Remaining proof debt

- A2: derive or justify ProductFixedSet p x.
- A3: derive or justify natural base bounds.
