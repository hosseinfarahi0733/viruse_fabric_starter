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
