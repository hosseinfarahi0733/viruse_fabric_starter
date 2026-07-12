import VFH2.Product.ProductTrajectoryStationarity
import VFH2.Product.ProductRestrictedParamsAfterOneUpdateProofSpine

/-!
# VF-H2 Restricted Proof Spine Along the Product Trajectory

This file returns the finite-time trajectory results to the current restricted
proof target.

Scientific result:
- Under the same semantic score assumptions used by the after-one-update proof,
  the restricted proof-spine target holds at trajectory time `t` exactly when
  the initial state is fixed or `t` is positive.
- Therefore every positive trajectory time enters the current restricted proof
  spine.
- For an initially fixed state, the target already holds at time zero.
- For an initially nonfixed state, time zero is excluded and every positive time
  satisfies the target.

This is a temporal characterization of the actual restricted proof target,
rather than another standalone trajectory property.

Boundary:
- The result remains restricted to `ProductRestrictedParams`.
- It retains inactive-insensitive score semantics and initial natural score
  bounds.
- It does not prove unrestricted TTP-VF-H2-004 or the full Viruse Fabric theory.
- It is not empirical or biological validation.
-/

namespace VFH2

namespace ProductRestrictedParamsTrajectoryProofSpineCharacterization

/--
The current restricted proof-spine target instantiated at product trajectory
time `t`.
-/
def restrictedParamsTrajectoryProofSpineAt
    (p : ProductRestrictedParams)
    (x : p.State)
    (productScore : p.State → Int)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (t : Nat) : Prop :=
  ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p
    (productUpdateTrajectory p x t)
    (productUpdateState p)
    productScore
    (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
      p
      (productUpdateTrajectory p x t)
      (productUpdateState p))
    (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
      p
      (productUpdateTrajectory p x t)
      (productUpdateState p)
      productScore)
    (ProductFixedSet p (productUpdateTrajectory p x t))
    thresholdLo
    thresholdHi
    hThreshold

/--
Exact temporal characterization of the current restricted proof-spine target.

Under inactive-insensitive score semantics and initial natural score bounds, the
target holds at time `t` exactly when the initial state is fixed or `t` is
positive.
-/
theorem restrictedParams_trajectoryProofSpineAt_iff_initialFixed_or_pos
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
      productScore x ≤ thresholdHi)
    (t : Nat) :
    restrictedParamsTrajectoryProofSpineAt
        p x productScore thresholdLo thresholdHi hThreshold t
      ↔
    ProductFixedSet p x ∨ 0 < t := by
  constructor

  · intro hTarget

    unfold restrictedParamsTrajectoryProofSpineAt at hTarget

    have hBaseTarget :
        ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
          p
          (productUpdateTrajectory p x t)
          (productUpdateState p)
          productScore
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
            p
            (productUpdateTrajectory p x t)
            (productUpdateState p))
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
            p
            (productUpdateTrajectory p x t)
            (productUpdateState p)
            productScore)
          (ProductFixedSet p (productUpdateTrajectory p x t))
          thresholdLo
          thresholdHi
          hThreshold :=
      ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParams_policyEndToEnd_baseTarget_projection
        p
        (productUpdateTrajectory p x t)
        (productUpdateState p)
        productScore
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          (productUpdateTrajectory p x t)
          (productUpdateState p))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          (productUpdateTrajectory p x t)
          (productUpdateState p)
          productScore)
        (ProductFixedSet p (productUpdateTrajectory p x t))
        thresholdLo
        thresholdHi
        hThreshold
        hTarget

    have hWindow :
        ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindow
          p
          (productUpdateTrajectory p x t)
          productScore
          (ProductFixedSet p (productUpdateTrajectory p x t))
          thresholdLo
          thresholdHi :=
      ProductRestrictedParamsScoreWindow.restrictedParams_baseScoreWindowTarget_window_projection
        p
        (productUpdateTrajectory p x t)
        (productUpdateState p)
        productScore
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          (productUpdateTrajectory p x t)
          (productUpdateState p))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          (productUpdateTrajectory p x t)
          (productUpdateState p)
          productScore)
        (ProductFixedSet p (productUpdateTrajectory p x t))
        thresholdLo
        thresholdHi
        hThreshold
        hBaseTarget

    have hLower :
        ProductBridgeGeneralization.genericBridgeTarget
          (ProductFixedSet p (productUpdateTrajectory p x t))
          (thresholdLo ≤ productScore (productUpdateTrajectory p x t)) :=
      ProductRestrictedParamsScoreWindow.restrictedParams_baseScoreWindow_lower_projection
        p
        (productUpdateTrajectory p x t)
        productScore
        (ProductFixedSet p (productUpdateTrajectory p x t))
        thresholdLo
        thresholdHi
        hWindow

    have hFixedAt :
        ProductFixedSet p (productUpdateTrajectory p x t) := by
      unfold ProductBridgeGeneralization.genericBridgeTarget at hLower
      exact hLower.1

    exact
      (productTrajectoryStationaryFrom_iff_initialFixed_or_pos
        p x t).1
        ((productTrajectoryStationaryFrom_iff_fixedAt
          p x t).2 hFixedAt)

  · intro hTime

    rcases hTime with hInitialFixed | htPositive

    · unfold restrictedParamsTrajectoryProofSpineAt

      rw [
        productUpdateTrajectory_eq_initial_of_fixed
          p x hInitialFixed t
      ]

      exact
        ProductRestrictedParamsCurrentBestMainTheorem.restrictedParams_currentBestMainTheorem
          p
          x
          productScore
          thresholdLo
          thresholdHi
          hThreshold
          hScoreInactive
          hInitialFixed
          hBaseLowerNatural
          hBaseUpperNatural

    · unfold restrictedParamsTrajectoryProofSpineAt

      rw [
        productUpdateTrajectory_eq_one_step_of_pos
          p x t htPositive
      ]

      exact
        ProductRestrictedParamsAfterOneUpdateProofSpine.restrictedParams_after_one_update_to_currentBestMainTheorem
          p
          x
          productScore
          thresholdLo
          thresholdHi
          hThreshold
          hScoreInactive
          hBaseLowerNatural
          hBaseUpperNatural

/--
Every positive trajectory time enters the current restricted proof spine.
-/
theorem restrictedParams_positiveTrajectory_to_currentBestMainTheorem
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
      productScore x ≤ thresholdHi)
    (t : Nat)
    (htPositive : 0 < t) :
    restrictedParamsTrajectoryProofSpineAt
      p x productScore thresholdLo thresholdHi hThreshold t := by
  exact
    (restrictedParams_trajectoryProofSpineAt_iff_initialFixed_or_pos
      p
      x
      productScore
      thresholdLo
      thresholdHi
      hThreshold
      hScoreInactive
      hBaseLowerNatural
      hBaseUpperNatural
      t).2
      (Or.inr htPositive)

end ProductRestrictedParamsTrajectoryProofSpineCharacterization

end VFH2
