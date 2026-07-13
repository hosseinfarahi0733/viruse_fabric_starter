import VFH2.Product.ProductRestrictedParamsTrajectoryProofSpineCharacterization
import VFH2.Product.ProductRestrictedParamsPreferredAfterOneUpdateProofSpine

/-!
# VF-H2 Preferred Restricted Proof Spine Along the Product Trajectory

This file specializes the temporal restricted proof-spine characterization to
the preferred restricted-parameter construction.

Scientific result:
- Parameters enter only through the preferred front door.
- An inactive-index certificate is derived from preferred active noncoverage.
- The inactive-coordinate score is selected from that derived certificate.
- Inactive-insensitive score semantics are derived.
- Natural score bounds `[0, p.n]` are derived.
- The restricted proof-spine target at trajectory time `t` holds exactly when
  the initial state is fixed or `t` is positive.

Thus the temporal proof-spine result requires no explicit score function,
inactive-index hypothesis, score-insensitivity hypothesis, or score-bound
hypotheses.

Architecture:
- Raw erase-construction declarations are not used.
- Compatibility declarations are not used.
- The route passes through the preferred front door and the established
  trajectory proof-spine characterization.

Boundary:
- The result remains restricted to `ProductRestrictedParams`.
- It does not prove unrestricted TTP-VF-H2-004 or the full Viruse Fabric theory.
- It is not empirical or biological validation.
-/

namespace VFH2

namespace ProductRestrictedParamsPreferredTrajectoryProofSpineCharacterization

/--
For preferred restricted parameters, the current restricted proof-spine target
holds at trajectory time `t` exactly when the initial state is fixed or `t` is
positive.

The inactive coordinate, score, inactive-insensitivity, natural score bounds,
and threshold order are all derived.
-/
theorem restrictedParams_preferredParams_trajectoryProofSpineAt_iff_initialFixed_or_pos
    (n d : Nat)
    (missing : ProductIndex d)
    (x :
      (ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing).State)
    (t : Nat) :
    let p :=
      ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing
    let cert :=
      ProductRestrictedParamsPreferredAfterOneUpdateProofSpine.preferredInactiveIndexCertificate
        n d missing
    ProductRestrictedParamsTrajectoryProofSpineCharacterization.restrictedParamsTrajectoryProofSpineAt
        p
        x
        (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
          p cert.i)
        0
        (Int.ofNat p.n)
        (Int.natCast_nonneg p.n)
        t
      ↔
    ProductFixedSet p x ∨ 0 < t := by
  dsimp only

  let p :=
    ProductRestrictedParamsPreferredFrontDoor.preferredParams
      n d missing

  let cert :=
    ProductRestrictedParamsPreferredAfterOneUpdateProofSpine.preferredInactiveIndexCertificate
      n d missing

  change
    ProductRestrictedParamsTrajectoryProofSpineCharacterization.restrictedParamsTrajectoryProofSpineAt
        p
        x
        (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
          p cert.i)
        0
        (Int.ofNat p.n)
        (Int.natCast_nonneg p.n)
        t
      ↔
    ProductFixedSet p x ∨ 0 < t

  have hInactive :
      ProductRestrictedParamsActiveInsensitiveScore.productScoreInactiveInsensitive
        p
        (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
          p cert.i) :=
    ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore_inactiveInsensitive_of_inactive_index
      p
      cert.i
      cert.inactive

  have hRange :
      ProductRestrictedParamsFixedStateConstruction.ScoreRangeCertificate
        p
        (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
          p cert.i)
        0
        (Int.ofNat p.n) :=
    ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore_range_zero_top
      p
      cert.i

  exact
    ProductRestrictedParamsTrajectoryProofSpineCharacterization.restrictedParams_trajectoryProofSpineAt_iff_initialFixed_or_pos
      p
      x
      (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
        p cert.i)
      0
      (Int.ofNat p.n)
      (Int.natCast_nonneg p.n)
      hInactive
      (hRange.lower x)
      (hRange.upper x)
      t

/--
Every positive trajectory time for preferred parameters enters the current
restricted proof spine, with all score-side conditions derived.
-/
theorem restrictedParams_preferredParams_positiveTrajectory_to_currentBestMainTheorem
    (n d : Nat)
    (missing : ProductIndex d)
    (x :
      (ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing).State)
    (t : Nat)
    (htPositive : 0 < t) :
    let p :=
      ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing
    let cert :=
      ProductRestrictedParamsPreferredAfterOneUpdateProofSpine.preferredInactiveIndexCertificate
        n d missing
    ProductRestrictedParamsTrajectoryProofSpineCharacterization.restrictedParamsTrajectoryProofSpineAt
      p
      x
      (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
        p cert.i)
      0
      (Int.ofNat p.n)
      (Int.natCast_nonneg p.n)
      t := by
  dsimp only

  exact
    (restrictedParams_preferredParams_trajectoryProofSpineAt_iff_initialFixed_or_pos
      n d missing x t).2
      (Or.inr htPositive)

end ProductRestrictedParamsPreferredTrajectoryProofSpineCharacterization

end VFH2
