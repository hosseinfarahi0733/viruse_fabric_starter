import VFH2.Product.ProductUpdateRangeCharacterization
import VFH2.Product.ProductRestrictedParamsCurrentBestMainTheorem

/-!
# VF-H2 Restricted Proof Spine After One Product Update

This file connects one-step restricted product stabilization to the current
restricted proof spine.

Scientific role:
- The initial state `x` is arbitrary.
- One concrete `productUpdateState` step produces a fixed state.
- Inactive-insensitive scores are preserved by that update.
- Initial natural score bounds therefore transfer to the updated state.
- The updated state then enters the existing restricted proof spine.

Boundary:
- This result is only for the current `ProductRestrictedParams` model.
- It does not prove unrestricted TTP-VF-H2-004 or the full Viruse Fabric theory.
- It does not remove inactive-insensitivity or natural score-bound assumptions.
- It does not establish empirical validation or nontrivial multi-step dynamics.
-/

namespace VFH2

namespace ProductRestrictedParamsAfterOneUpdateProofSpine

/--
An arbitrary restricted product state enters the current proof spine after one
concrete update, provided its score is inactive-insensitive and initially lies
inside the natural threshold window.
-/
theorem restrictedParams_after_one_update_to_currentBestMainTheorem
    (p : ProductRestrictedParams)
    (x : p.State)
    (productScore : p.State → Int)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hScoreInactive :
      ProductRestrictedParamsActiveInsensitiveScore.productScoreInactiveInsensitive
        p productScore)
    (hBaseLowerNatural :
      thresholdLo ≤ productScore x)
    (hBaseUpperNatural :
      productScore x ≤ thresholdHi) :
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
      p
      (productUpdateState p x)
      (productUpdateState p)
      productScore
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
        p
        (productUpdateState p x)
        (productUpdateState p))
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
        p
        (productUpdateState p x)
        (productUpdateState p)
        productScore)
      (ProductFixedSet p (productUpdateState p x))
      thresholdLo
      thresholdHi
      hThreshold := by
  have hScorePreserved :
      productScore (productUpdateState p x) = productScore x := by
    exact
      ProductRestrictedParamsActiveInsensitiveScore.productUpdateState_scorePreservingPolicy_of_inactiveInsensitive
        p
        productScore
        hScoreInactive
        x

  exact
    ProductRestrictedParamsCurrentBestMainTheorem.restrictedParams_currentBestMainTheorem
      p
      (productUpdateState p x)
      productScore
      thresholdLo
      thresholdHi
      hThreshold
      hScoreInactive
      (productUpdateState_ProductFixedSet p x)
      (by
        rw [hScorePreserved]
        exact hBaseLowerNatural)
      (by
        rw [hScorePreserved]
        exact hBaseUpperNatural)

end ProductRestrictedParamsAfterOneUpdateProofSpine

end VFH2
