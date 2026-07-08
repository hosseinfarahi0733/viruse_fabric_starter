import VFH2.Product.ProductRestrictedParamsBoundedScore

/-!
# C16 — Fixed-state construction

This file constructs a concrete product state that satisfies `ProductFixedSet`.

Scientific role:
- It does not prove that every state is fixed.
- It does not derive `ProductFixedSet p x` for arbitrary `x`.
- It constructs a canonical fixed state by assigning `p.topCoord` everywhere.
- Since `p.topCoord.val = p.n`, this state satisfies `ProductFixedSet`.
- It then connects the constructed fixed state to the C15 constant-score theorem.

Assumption impact:
- A2 is partially discharged for constructed fixed states.
- A3 remains partially discharged through the C15 constant-score route.
- Arbitrary-state fixedness remains undischarged.
-/

namespace VFH2

namespace ProductRestrictedParamsFixedStateConstruction

/--
Canonical fixed product state.

Every coordinate is set to `p.topCoord`.
-/
def fixedProductState
    (p : ProductRestrictedParams) : p.State :=
  fun _ => p.topCoord

/--
The canonical fixed product state is fixed on the active set.
-/
theorem fixedProductState_ProductFixedSet
    (p : ProductRestrictedParams) :
    ProductFixedSet p (fixedProductState p) := by
  intro i hi
  unfold fixedProductState
  exact ProductRestrictedParams.topCoord_val p

/--
The product update leaves the canonical fixed state value-equivalent pointwise.
-/
theorem productUpdateState_fixedProductState_val_eq
    (p : ProductRestrictedParams) :
    ∀ i : ProductIndex p.d,
      (productUpdateState p (fixedProductState p) i).val =
        (fixedProductState p i).val := by
  exact
    productUpdateState_val_eq_of_fixed
      (p := p)
      (x := fixedProductState p)
      (fixedProductState_ProductFixedSet p)

/--
Constant-score proof-spine theorem for the canonical fixed state.

This theorem removes the explicit `ProductFixedSet` assumption by using the
constructed fixed state.
-/
theorem restrictedParams_constantScore_fixedProductState_to_currentBestMainTheorem
    (p : ProductRestrictedParams)
    (c thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hLo : thresholdLo ≤ c)
    (hHi : c ≤ thresholdHi) :
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
      p (fixedProductState p) (productUpdateState p)
      (ProductRestrictedParamsBoundedScore.constantProductScore p c)
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
        p (fixedProductState p) (productUpdateState p))
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
        p (fixedProductState p) (productUpdateState p)
        (ProductRestrictedParamsBoundedScore.constantProductScore p c))
      (ProductFixedSet p (fixedProductState p))
      thresholdLo thresholdHi hThreshold := by
  exact
    ProductRestrictedParamsBoundedScore.restrictedParams_constantScore_to_currentBestMainTheorem
      p (fixedProductState p)
      c thresholdLo thresholdHi hThreshold
      hLo hHi
      (fixedProductState_ProductFixedSet p)

end ProductRestrictedParamsFixedStateConstruction

end VFH2

namespace VFH2
namespace ProductRestrictedParamsFixedStateConstruction

/--
C19 generalizes the v17.7.0 constructed fixed-state route.

Instead of using only the constant score `constantProductScore p c`, this theorem
uses the constructed state `fixedProductState p` with an arbitrary product score,
provided the score is inactive-insensitive and globally bounded by the threshold
interval.

This preserves the constructed-state contribution of v17.7.0 while removing the
constant-score restriction.
-/
theorem restrictedParams_boundedInactiveScore_fixedProductState_to_currentBestMainTheorem
    (p : VFH2.ProductRestrictedParams)
    (productScore : p.State → Int)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hScoreInactive :
      VFH2.ProductRestrictedParamsActiveInsensitiveScore.productScoreInactiveInsensitive p productScore)
    (hScoreBounded :
      VFH2.ProductRestrictedParamsBoundedScore.productScoreBoundedBy p productScore thresholdLo thresholdHi) :
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget p
      (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p)
      (VFH2.productUpdateState p)
      productScore
      (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p
        (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p)
        (VFH2.productUpdateState p))
      (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p
        (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p)
        (VFH2.productUpdateState p)
        productScore)
      (VFH2.ProductFixedSet p
        (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p))
      thresholdLo
      thresholdHi
      hThreshold := by
  have hBounds :=
    hScoreBounded
      (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p)
  exact
    VFH2.ProductRestrictedParamsCurrentBestMainTheorem.restrictedParams_currentBestMainTheorem
      p
      (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p)
      productScore
      thresholdLo
      thresholdHi
      hThreshold
      hScoreInactive
      (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState_ProductFixedSet p)
      hBounds.1
      hBounds.2

end ProductRestrictedParamsFixedStateConstruction
end VFH2
