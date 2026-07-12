import VFH2.Product.ProductRestrictedParamsAfterOneUpdateProofSpine
import VFH2.Product.ProductRestrictedParamsInactiveCoordScore

/-!
# VF-H2 Inactive-Coordinate Score After One Product Update

This file specializes the after-one-update restricted proof-spine theorem to
the concrete score obtained from an inactive product coordinate.

Scientific role:
- The initial product state is arbitrary.
- The score is selected from an inactive coordinate.
- Inactive-insensitivity is derived from the inactive-index proof.
- Natural score bounds `[0, p.n]` are derived from the coordinate range.
- After one concrete product update, the resulting fixed state enters the
  restricted proof spine.

Boundary:
- This result is only for the current `ProductRestrictedParams` model.
- It still requires an inactive product coordinate.
- It does not prove unrestricted TTP-VF-H2-004 or the full Viruse Fabric theory.
- It does not establish empirical validation or nontrivial multi-step dynamics.
-/

namespace VFH2

namespace ProductRestrictedParamsInactiveCoordAfterOneUpdateProofSpine

/--
For any inactive coordinate, its natural coordinate score sends every initial
state into the current restricted proof spine after one concrete product
update, with no additional score-side assumptions.
-/
theorem restrictedParams_inactiveCoordScore_after_one_update_to_currentBestMainTheorem
    (p : ProductRestrictedParams)
    (x : p.State)
    (i : ProductIndex p.d)
    (hi : ¬ i ∈ p.active) :
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
      p
      (productUpdateState p x)
      (productUpdateState p)
      (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore p i)
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
        p
        (productUpdateState p x)
        (productUpdateState p))
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
        p
        (productUpdateState p x)
        (productUpdateState p)
        (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore p i))
      (ProductFixedSet p (productUpdateState p x))
      0
      (Int.ofNat p.n)
      (Int.natCast_nonneg p.n) := by
  have hInactive :
      ProductRestrictedParamsActiveInsensitiveScore.productScoreInactiveInsensitive
        p
        (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore p i) :=
    ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore_inactiveInsensitive_of_inactive_index
      p
      i
      hi

  have hRange :
      ProductRestrictedParamsFixedStateConstruction.ScoreRangeCertificate
        p
        (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore p i)
        0
        (Int.ofNat p.n) :=
    ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore_range_zero_top
      p
      i

  exact
    ProductRestrictedParamsAfterOneUpdateProofSpine.restrictedParams_after_one_update_to_currentBestMainTheorem
      p
      x
      (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore p i)
      0
      (Int.ofNat p.n)
      (Int.natCast_nonneg p.n)
      hInactive
      (hRange.lower x)
      (hRange.upper x)

end ProductRestrictedParamsInactiveCoordAfterOneUpdateProofSpine

end VFH2
