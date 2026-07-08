import VFH2.Product.ProductRestrictedParamsCurrentBestMainTheorem

/-!
# C15 — Bounded score construction

This file introduces a bounded-score interface for the current best theorem.

Scientific role:
- It does not pretend to discharge natural bounds unconditionally.
- It replaces pointwise base-bound assumptions at a chosen state `x` with a
  semantic/global score condition.
- It proves that the global bounded-score condition implies the base bounds
  required by the current best theorem.
- It also provides a small concrete score construction: constant scores.
- Constant scores are inactive-insensitive and bounded whenever the constant
  lies inside the threshold interval.

Boundary:
- `productScoreBoundedBy` is still an assumption when used abstractly.
- The constant-score route is a genuine construction, but mathematically simple.
- This file does not discharge ProductFixedSet.
- This file does not prove all product scores are bounded.
- This file should not receive a tag before an impact audit.
-/

namespace VFH2

namespace ProductRestrictedParamsBoundedScore

/--
A product score is bounded by a threshold interval when every state receives a
score inside that interval.
-/
def productScoreBoundedBy
    (p : ProductRestrictedParams)
    (productScore : p.State → Int)
    (thresholdLo thresholdHi : Int) : Prop :=
  ∀ y : p.State,
    thresholdLo ≤ productScore y ∧ productScore y ≤ thresholdHi

/--
A bounded score gives the lower natural base bound at any chosen state.
-/
theorem productScoreBoundedBy_baseLower
    (p : ProductRestrictedParams)
    (productScore : p.State → Int)
    (thresholdLo thresholdHi : Int)
    (x : p.State)
    (hBounded : productScoreBoundedBy p productScore thresholdLo thresholdHi) :
    thresholdLo ≤ productScore x := by
  exact (hBounded x).1

/--
A bounded score gives the upper natural base bound at any chosen state.
-/
theorem productScoreBoundedBy_baseUpper
    (p : ProductRestrictedParams)
    (productScore : p.State → Int)
    (thresholdLo thresholdHi : Int)
    (x : p.State)
    (hBounded : productScoreBoundedBy p productScore thresholdLo thresholdHi) :
    productScore x ≤ thresholdHi := by
  exact (hBounded x).2

/--
A bounded score gives both natural base bounds at any chosen state.
-/
theorem productScoreBoundedBy_baseBounds
    (p : ProductRestrictedParams)
    (productScore : p.State → Int)
    (thresholdLo thresholdHi : Int)
    (x : p.State)
    (hBounded : productScoreBoundedBy p productScore thresholdLo thresholdHi) :
    thresholdLo ≤ productScore x ∧ productScore x ≤ thresholdHi := by
  exact hBounded x

/--
Current best theorem, but with the two pointwise natural base-bound assumptions
replaced by a global bounded-score condition.
-/
theorem restrictedParams_boundedScore_to_currentBestMainTheorem
    (p : ProductRestrictedParams)
    (x : p.State)
    (productScore : p.State → Int)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hScoreInactive :
      ProductRestrictedParamsActiveInsensitiveScore.productScoreInactiveInsensitive
        p productScore)
    (hScoreBounded :
      productScoreBoundedBy p productScore thresholdLo thresholdHi)
    (hFixedSet : ProductFixedSet p x) :
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
      p x (productUpdateState p) productScore
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
        p x (productUpdateState p))
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
        p x (productUpdateState p) productScore)
      (ProductFixedSet p x) thresholdLo thresholdHi hThreshold := by
  exact
    ProductRestrictedParamsCurrentBestMainTheorem.restrictedParams_currentBestMainTheorem
      p x productScore thresholdLo thresholdHi hThreshold
      hScoreInactive hFixedSet
      (productScoreBoundedBy_baseLower
        p productScore thresholdLo thresholdHi x hScoreBounded)
      (productScoreBoundedBy_baseUpper
        p productScore thresholdLo thresholdHi x hScoreBounded)

/--
A simple concrete score construction: every state receives the same integer.
-/
def constantProductScore
    (p : ProductRestrictedParams)
    (c : Int) : p.State → Int :=
  fun _ => c

/--
Constant scores are inactive-insensitive.
-/
theorem constantProductScore_inactiveInsensitive
    (p : ProductRestrictedParams)
    (c : Int) :
    ProductRestrictedParamsActiveInsensitiveScore.productScoreInactiveInsensitive
      p (constantProductScore p c) := by
  intro x y hInactiveEq
  rfl

/--
A constant score is bounded whenever the constant is inside the threshold
interval.
-/
theorem constantProductScore_boundedBy
    (p : ProductRestrictedParams)
    (c thresholdLo thresholdHi : Int)
    (hLo : thresholdLo ≤ c)
    (hHi : c ≤ thresholdHi) :
    productScoreBoundedBy
      p (constantProductScore p c) thresholdLo thresholdHi := by
  intro y
  exact ⟨hLo, hHi⟩

/--
Concrete constant-score front-door theorem.

This removes both pointwise natural base-bound assumptions and the
active-insensitive-score assumption for the special case of constant scores.

It still assumes ProductFixedSet.
-/
theorem restrictedParams_constantScore_to_currentBestMainTheorem
    (p : ProductRestrictedParams)
    (x : p.State)
    (c thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hLo : thresholdLo ≤ c)
    (hHi : c ≤ thresholdHi)
    (hFixedSet : ProductFixedSet p x) :
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
      p x (productUpdateState p) (constantProductScore p c)
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
        p x (productUpdateState p))
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
        p x (productUpdateState p) (constantProductScore p c))
      (ProductFixedSet p x) thresholdLo thresholdHi hThreshold := by
  exact
    restrictedParams_boundedScore_to_currentBestMainTheorem
      p x (constantProductScore p c)
      thresholdLo thresholdHi hThreshold
      (constantProductScore_inactiveInsensitive p c)
      (constantProductScore_boundedBy p c thresholdLo thresholdHi hLo hHi)
      hFixedSet

end ProductRestrictedParamsBoundedScore

end VFH2
