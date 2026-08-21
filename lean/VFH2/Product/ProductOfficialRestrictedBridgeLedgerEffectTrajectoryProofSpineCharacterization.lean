import VFH2.Product.ProductOfficialRestrictedBridgeWellFormedDynamicalEquivalence
import VFH2.Product.ProductRestrictedParamsLedgerEffectProofSpineCharacterization

/-!
# Official Ledger-Effect Trajectory Proof-Spine Characterization

This module applies the concrete Product ledger-effect proof-spine
characterization to every time slice of every official well-formed restricted
trajectory.  The canonical decoder transports the official list state into the
typed Product model, while the score is the official ledger effect pulled back
along canonical state serialization.  The frozen proof-spine target with exact
zero score window then holds precisely when the original official state was
fixed or time is positive.

Boundary:
- This connects only the two current restricted formalizations.
- The score is the existing official `RestrictedBridge.ledgerEffectR` pulled
  back to Product states; the update is the existing `productUpdateState`.
- This transports the existing Product proof spine rather than introducing an
  official-native proof-spine definition.
- No score-preservation, score-bound, or initial-fixedness assumption is added.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
-/

namespace VFH2
namespace ProductOfficialRestrictedBridgeLedgerEffectTrajectoryProofSpineCharacterization

open ProductOfficialRestrictedBridgeStateTransport
open ProductOfficialRestrictedBridgeStateSpaceEquivalence
open ProductOfficialRestrictedBridgeParameterSpaceEquivalence
open ProductOfficialRestrictedBridgeLedgerStateSpaceEquivalence
open ProductOfficialRestrictedBridgeWellFormedDynamicalEquivalence

private theorem officialRestrictedParams_productParamsOfOfficialWellFormed_eq_params
    (wp : RestrictedBridge.WellFormedRestrictedParams) :
    officialRestrictedParams
        (productParamsOfOfficialWellFormed wp) =
      wp.params := by
  exact congrArg
    RestrictedBridge.WellFormedRestrictedParams.params
    (officialWellFormedRestrictedParams_productParamsOfOfficialWellFormed wp)

private theorem productFixedSet_productStateOfOfficialWellFormedState_iff_inFixedSetR
    (wp : RestrictedBridge.WellFormedRestrictedParams)
    (y : RestrictedBridge.State)
    (hspace :
      RestrictedBridge.inRestrictedStateSpace wp.params y) :
    ProductFixedSet
        (productParamsOfOfficialWellFormed wp)
        (productStateOfOfficialWellFormedState wp y hspace)
      ↔
    RestrictedBridge.inFixedSetR wp.params y := by
  let p := productParamsOfOfficialWellFormed wp
  have hParams :
      officialRestrictedParams p = wp.params :=
    officialRestrictedParams_productParamsOfOfficialWellFormed_eq_params wp
  change
    ProductFixedSet p
        (productStateOfOfficialRestrictedState p y _)
      ↔
    RestrictedBridge.inFixedSetR wp.params y
  rw [productFixedSet_iff_officialRestrictedBridge_inFixedSetR]
  rw [officialRestrictedState_productStateOfOfficialRestrictedState]
  rw [hParams]

/--
Along every official well-formed trajectory, the frozen Product proof spine
with the pulled-back official ledger effect as score and `[0, 0]` as score
window holds exactly when the initial official state is fixed or the trajectory
time is positive.
-/
theorem officialWellFormed_officialLedgerEffect_trajectoryProofSpineTarget_iff_initialFixed_or_pos
    (wp : RestrictedBridge.WellFormedRestrictedParams)
    (y : RestrictedBridge.State)
    (hspace :
      RestrictedBridge.inRestrictedStateSpace wp.params y)
    (t : Nat) :
    let p := productParamsOfOfficialWellFormed wp
    let xAt :=
      productStateOfOfficialWellFormedState
        wp
        (officialWellFormedUpdateTrajectory wp y t)
        (officialWellFormedUpdateTrajectory_inRestrictedStateSpace
          wp y hspace t)
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
        p
        xAt
        (productUpdateState p)
        (fun z : p.State =>
          RestrictedBridge.ledgerEffectR
            wp.params
            (officialRestrictedState p z))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          xAt
          (productUpdateState p))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          xAt
          (productUpdateState p)
          (fun z : p.State =>
            RestrictedBridge.ledgerEffectR
              wp.params
              (officialRestrictedState p z)))
        (ProductFixedSet p xAt)
        0
        0
        (Int.le_refl 0)
      ↔
    RestrictedBridge.inFixedSetR wp.params y ∨ 0 < t := by
  dsimp only
  let p := productParamsOfOfficialWellFormed wp
  have hParams :
      officialRestrictedParams p = wp.params :=
    officialRestrictedParams_productParamsOfOfficialWellFormed_eq_params wp
  have hScore :
      (fun z : p.State =>
        RestrictedBridge.ledgerEffectR
          wp.params
          (officialRestrictedState p z)) =
        productLedgerEffect p := by
    funext z
    rw [← hParams]
    exact
      ProductOfficialRestrictedBridgeDynamicsTransport.officialRestrictedBridge_ledgerEffectR_eq_productLedgerEffect
        p z
  rw [hScore]
  rw [
    ProductRestrictedParamsLedgerEffectProofSpineCharacterization.restrictedParams_productLedgerEffect_proofSpineTarget_iff_productFixedSet
  ]
  rw [
    productStateOfOfficialWellFormedState_trajectory
      wp y hspace t
  ]
  cases t with
  | zero =>
      simpa using
        (productFixedSet_productStateOfOfficialWellFormedState_iff_inFixedSetR
          wp y hspace)
  | succ k =>
      constructor
      · intro _hFixed
        exact Or.inr (Nat.succ_pos k)
      · intro _hClassification
        exact
          productUpdateTrajectory_ProductFixedSet_of_pos
            p
            (productStateOfOfficialWellFormedState wp y hspace)
            (k + 1)
            (Nat.succ_pos k)

end ProductOfficialRestrictedBridgeLedgerEffectTrajectoryProofSpineCharacterization
end VFH2
