import VFH2.Product.ProductRestrictedParamsFixedStateConstruction
import VFH2.Product.ProductLedger

namespace VFH2
namespace ProductRestrictedParamsInactiveCoordScore

/--
C25 coordinate score candidate.

This score reads the value of a single product coordinate and converts it to `Int`.

It is not claimed to be nonconstant in all parameter settings. Its formal value
is that its range can be derived from the existing product-coordinate bound.

Inactive-insensitivity is kept as a separate hypothesis in the proof-spine route,
because C24 showed that direct ledger-style scores must not be assumed to be
inactive-insensitive without proof.
-/
def inactiveCoordScore
    (p : VFH2.ProductRestrictedParams)
    (i : VFH2.ProductIndex p.d) :
    p.State → Int :=
  fun x => Int.ofNat ((x i).val)

/--
The coordinate score is always inside the natural product range `[0, p.n]`.

This discharges the C23 `ScoreRangeCertificate` target for the concrete coordinate
score.
-/
theorem inactiveCoordScore_range_zero_top
    (p : VFH2.ProductRestrictedParams)
    (i : VFH2.ProductIndex p.d) :
    VFH2.ProductRestrictedParamsFixedStateConstruction.ScoreRangeCertificate
      p
      (inactiveCoordScore p i)
      0
      (Int.ofNat p.n) := by
  constructor
  · intro y
    dsimp [inactiveCoordScore]
    exact Int.natCast_nonneg ((y i).val)
  · intro y
    dsimp [inactiveCoordScore]
    have hNat : (y i).val ≤ p.n :=
      VFH2.productLedger_coordinate_val_le_top p y i
    exact_mod_cast hNat

/--
C25 route from the concrete coordinate score to the constructed fixed-state
proof-spine target.

The range certificate and threshold proof are derived. The remaining score-side
condition is exactly inactive-insensitivity of this coordinate score.
-/
theorem restrictedParams_inactiveCoordScore_fixedProductState_to_currentBestMainTheorem
    (p : VFH2.ProductRestrictedParams)
    (i : VFH2.ProductIndex p.d)
    (hScoreInactive :
      VFH2.ProductRestrictedParamsActiveInsensitiveScore.productScoreInactiveInsensitive
        p
        (inactiveCoordScore p i)) :
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget p
      (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p)
      (VFH2.productUpdateState p)
      (inactiveCoordScore p i)
      (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p
        (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p)
        (VFH2.productUpdateState p))
      (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p
        (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p)
        (VFH2.productUpdateState p)
        (inactiveCoordScore p i))
      (VFH2.ProductFixedSet p
        (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p))
      0
      (Int.ofNat p.n)
      (Int.natCast_nonneg p.n) := by
  exact
    VFH2.ProductRestrictedParamsFixedStateConstruction.restrictedParams_scoreRangeCertificate_fixedProductState_to_currentBestMainTheorem
      p
      (inactiveCoordScore p i)
      0
      (Int.ofNat p.n)
      (Int.natCast_nonneg p.n)
      hScoreInactive
      (inactiveCoordScore_range_zero_top p i)

end ProductRestrictedParamsInactiveCoordScore
end VFH2
