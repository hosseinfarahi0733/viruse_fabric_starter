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

namespace VFH2
namespace ProductRestrictedParamsInactiveCoordScore

/--
C26 discharges the inactive-insensitivity obligation for `inactiveCoordScore`
under the exact inactive-index condition.

The definition of `productScoreInactiveInsensitive` requires equality of the score
whenever two states agree on every inactive coordinate. Since `inactiveCoordScore`
reads only coordinate `i`, the score is inactive-insensitive whenever `i` is not
in the active coordinate set.
-/
theorem inactiveCoordScore_inactiveInsensitive_of_inactive_index
    (p : VFH2.ProductRestrictedParams)
    (i : VFH2.ProductIndex p.d)
    (hi : ¬ i ∈ p.active) :
    VFH2.ProductRestrictedParamsActiveInsensitiveScore.productScoreInactiveInsensitive
      p
      (inactiveCoordScore p i) := by
  intro x y hInactiveEq
  dsimp [inactiveCoordScore]
  exact congrArg Int.ofNat (hInactiveEq i hi)

/--
C26 closes the remaining C25 score-side hypothesis for inactive coordinates.

For any coordinate `i` outside the active set, the coordinate score has:
1. derived inactive-insensitivity;
2. derived range bounds from C25;
3. a route into the constructed fixed-state proof spine.
-/
theorem restrictedParams_inactiveCoordScore_inactiveIndex_fixedProductState_to_currentBestMainTheorem
    (p : VFH2.ProductRestrictedParams)
    (i : VFH2.ProductIndex p.d)
    (hi : ¬ i ∈ p.active) :
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
    restrictedParams_inactiveCoordScore_fixedProductState_to_currentBestMainTheorem
      p
      i
      (inactiveCoordScore_inactiveInsensitive_of_inactive_index p i hi)

end ProductRestrictedParamsInactiveCoordScore
end VFH2

namespace VFH2
namespace ProductRestrictedParamsInactiveCoordScore

/--
C27 packages the exact remaining coordinate-side data needed by C26.

An `InactiveIndexCertificate p` provides a product coordinate together with a proof
that this coordinate is outside the active set. This is the smallest parameter-side
certificate needed to close the `inactiveCoordScore` route from C26.
-/
structure InactiveIndexCertificate
    (p : VFH2.ProductRestrictedParams) : Type where
  i : VFH2.ProductIndex p.d
  inactive : ¬ i ∈ p.active

/--
The coordinate score selected by an inactive-index certificate.
-/
def inactiveIndexCertificateScore
    (p : VFH2.ProductRestrictedParams)
    (cert : InactiveIndexCertificate p) :
    p.State → Int :=
  inactiveCoordScore p cert.i

/--
An inactive-index certificate supplies the inactive-insensitivity proof for its
associated coordinate score.
-/
theorem InactiveIndexCertificate.score_inactiveInsensitive
    (p : VFH2.ProductRestrictedParams)
    (cert : InactiveIndexCertificate p) :
    VFH2.ProductRestrictedParamsActiveInsensitiveScore.productScoreInactiveInsensitive
      p
      (inactiveIndexCertificateScore p cert) := by
  dsimp [inactiveIndexCertificateScore]
  exact inactiveCoordScore_inactiveInsensitive_of_inactive_index
    p
    cert.i
    cert.inactive

/--
An inactive-index certificate supplies the range certificate for its associated
coordinate score.
-/
theorem InactiveIndexCertificate.score_range_zero_top
    (p : VFH2.ProductRestrictedParams)
    (cert : InactiveIndexCertificate p) :
    VFH2.ProductRestrictedParamsFixedStateConstruction.ScoreRangeCertificate
      p
      (inactiveIndexCertificateScore p cert)
      0
      (Int.ofNat p.n) := by
  dsimp [inactiveIndexCertificateScore]
  exact inactiveCoordScore_range_zero_top p cert.i

/--
C27 packages the C26 inactive-coordinate route behind an inactive-index
certificate.

This theorem removes the need to pass a raw coordinate and inactive-membership
proof separately. The proof-spine target follows from the certificate-selected
coordinate score.
-/
theorem restrictedParams_inactiveIndexCertificate_fixedProductState_to_currentBestMainTheorem
    (p : VFH2.ProductRestrictedParams)
    (cert : InactiveIndexCertificate p) :
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget p
      (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p)
      (VFH2.productUpdateState p)
      (inactiveIndexCertificateScore p cert)
      (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p
        (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p)
        (VFH2.productUpdateState p))
      (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p
        (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p)
        (VFH2.productUpdateState p)
        (inactiveIndexCertificateScore p cert))
      (VFH2.ProductFixedSet p
        (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p))
      0
      (Int.ofNat p.n)
      (Int.natCast_nonneg p.n) := by
  dsimp [inactiveIndexCertificateScore]
  exact
    restrictedParams_inactiveCoordScore_inactiveIndex_fixedProductState_to_currentBestMainTheorem
      p
      cert.i
      cert.inactive

end ProductRestrictedParamsInactiveCoordScore
end VFH2

namespace VFH2
namespace ProductRestrictedParamsInactiveCoordScore

/--
C28 constructs an inactive-index certificate from the minimal non-coverage
condition.

This does not claim that an inactive coordinate exists unconditionally. It says
that if the active list does not cover every coordinate, then the witness can be
packaged as an `InactiveIndexCertificate`.

The definition is noncomputable because it extracts a witness from an existential
proof.
-/
noncomputable def InactiveIndexCertificate.of_exists_inactive
    (p : VFH2.ProductRestrictedParams)
    (hExists : ∃ i : VFH2.ProductIndex p.d, ¬ i ∈ p.active) :
    InactiveIndexCertificate p :=
  {
    i := Classical.choose hExists
    inactive := Classical.choose_spec hExists
  }

/--
The minimal non-coverage condition supplies a certificate-selected coordinate
score and therefore closes the C27 proof-spine route.
-/
theorem restrictedParams_existsInactiveIndex_fixedProductState_to_currentBestMainTheorem
    (p : VFH2.ProductRestrictedParams)
    (hExists : ∃ i : VFH2.ProductIndex p.d, ¬ i ∈ p.active) :
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget p
      (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p)
      (VFH2.productUpdateState p)
      (inactiveIndexCertificateScore p
        (InactiveIndexCertificate.of_exists_inactive p hExists))
      (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p
        (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p)
        (VFH2.productUpdateState p))
      (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p
        (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p)
        (VFH2.productUpdateState p)
        (inactiveIndexCertificateScore p
          (InactiveIndexCertificate.of_exists_inactive p hExists)))
      (VFH2.ProductFixedSet p
        (VFH2.ProductRestrictedParamsFixedStateConstruction.fixedProductState p))
      0
      (Int.ofNat p.n)
      (Int.natCast_nonneg p.n) := by
  exact
    restrictedParams_inactiveIndexCertificate_fixedProductState_to_currentBestMainTheorem
      p
      (InactiveIndexCertificate.of_exists_inactive p hExists)

end ProductRestrictedParamsInactiveCoordScore
end VFH2
