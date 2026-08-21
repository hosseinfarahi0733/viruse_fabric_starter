import VFH2.Product.ProductOfficialRestrictedBridgeLedgerEffectTrajectoryProofSpineCharacterization

/-!
# Official Ledger-Effect / Product Proof-Spine Equivalence

This module closes the current restricted semantic integration by identifying
the transported frozen Product proof-spine target at each official trajectory
time with the actual same-time zero-ledger-effect conclusion of the named
official restricted bridge theorem.

The reverse fixed/zero direction uses the official nonfixed-positive
conclusion, so the equivalence is not merely the fixed-zero projection.

Boundary:
- This connects only the two current restricted formalizations.
- It uses the existing official `RBRIDGE_VF_H2_001_R_Lean_scaffold` theorem,
  trajectory, update, ledger effect, decoder, and Product proof spine.
- It introduces neither a new official theorem nor an official-native proof
  spine.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
-/

namespace VFH2
namespace ProductOfficialRestrictedBridgeLedgerEffectProofSpineEquivalence

open ProductOfficialRestrictedBridgeStateTransport
open ProductOfficialRestrictedBridgeStateSpaceEquivalence
open ProductOfficialRestrictedBridgeParameterSpaceEquivalence
open ProductOfficialRestrictedBridgeLedgerStateSpaceEquivalence
open ProductOfficialRestrictedBridgeWellFormedDynamicalEquivalence
open ProductOfficialRestrictedBridgeLedgerEffectTrajectoryProofSpineCharacterization

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

private theorem officialWellFormedUpdateTrajectory_inFixedSetR_iff_initialFixed_or_pos
    (wp : RestrictedBridge.WellFormedRestrictedParams)
    (y : RestrictedBridge.State)
    (hspace :
      RestrictedBridge.inRestrictedStateSpace wp.params y)
    (t : Nat) :
    RestrictedBridge.inFixedSetR
        wp.params
        (officialWellFormedUpdateTrajectory wp y t)
      ↔
    RestrictedBridge.inFixedSetR wp.params y ∨ 0 < t := by
  cases t with
  | zero =>
      simp [officialWellFormedUpdateTrajectory]
  | succ k =>
      constructor
      · intro _hFixed
        exact Or.inr (Nat.succ_pos k)
      · intro _hClassification
        change
          RestrictedBridge.inFixedSetR
            wp.params
            (RestrictedBridge.updateStateR
              wp.params
              (officialWellFormedUpdateTrajectory wp y k))
        exact
          RestrictedBridge.updateStateR_inFixedSetR_of_WellFormedRestrictedParams
            wp
            (officialWellFormedUpdateTrajectory_inRestrictedStateSpace
              wp y hspace k)

private theorem officialWellFormed_inFixedSetR_iff_ledgerEffectR_eq_zero
    (wp : RestrictedBridge.WellFormedRestrictedParams)
    (y : RestrictedBridge.State)
    (hspace :
      RestrictedBridge.inRestrictedStateSpace wp.params y) :
    RestrictedBridge.inFixedSetR wp.params y
      ↔
    RestrictedBridge.ledgerEffectR wp.params y = 0 := by
  have hOfficial :
      (RestrictedBridge.inFixedSetR wp.params y →
        RestrictedBridge.ledgerEffectR wp.params y = 0) ∧
      (¬ RestrictedBridge.inFixedSetR wp.params y →
        0 < RestrictedBridge.ledgerEffectR wp.params y) :=
    RestrictedBridge.RBRIDGE_VF_H2_001_R_Lean_scaffold
      wp.params
      y
      (RestrictedBridge.wellFormedRestrictedInput_of_WellFormedRestrictedParams
        hspace)
  constructor
  · exact hOfficial.1
  · intro hZero
    apply Classical.byContradiction
    intro hNotFixed
    have hPositive :
        0 < RestrictedBridge.ledgerEffectR wp.params y :=
      hOfficial.2 hNotFixed
    rw [hZero] at hPositive
    exact (Int.lt_irrefl 0) hPositive

/--
At every time of every official well-formed restricted trajectory, the
transported frozen Product proof-spine target with pulled-back official ledger
effect and exact zero window is equivalent to the official current ledger
effect being zero.
-/
theorem officialWellFormed_officialFixed_ledgerEffect_trajectoryProofSpineTarget_iff_currentLedgerEffectR_eq_zero
    (wp : RestrictedBridge.WellFormedRestrictedParams)
    (y : RestrictedBridge.State)
    (hspace :
      RestrictedBridge.inRestrictedStateSpace wp.params y)
    (t : Nat) :
    let p := productParamsOfOfficialWellFormed wp
    let yAt := officialWellFormedUpdateTrajectory wp y t
    let hspaceAt :=
      officialWellFormedUpdateTrajectory_inRestrictedStateSpace
        wp y hspace t
    let xAt :=
      productStateOfOfficialWellFormedState
        wp
        yAt
        hspaceAt
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
        (RestrictedBridge.inFixedSetR wp.params yAt)
        0
        0
        (Int.le_refl 0)
      ↔
    RestrictedBridge.ledgerEffectR
        wp.params
        yAt =
      0 := by
  dsimp only
  have hFixedEq :
      RestrictedBridge.inFixedSetR
          wp.params
          (officialWellFormedUpdateTrajectory wp y t) =
        ProductFixedSet
          (productParamsOfOfficialWellFormed wp)
          (productStateOfOfficialWellFormedState
            wp
            (officialWellFormedUpdateTrajectory wp y t)
            (officialWellFormedUpdateTrajectory_inRestrictedStateSpace
              wp y hspace t)) :=
    propext
      (productFixedSet_productStateOfOfficialWellFormedState_iff_inFixedSetR
        wp
        (officialWellFormedUpdateTrajectory wp y t)
        (officialWellFormedUpdateTrajectory_inRestrictedStateSpace
          wp y hspace t)).symm
  rw [hFixedEq]
  exact
    (officialWellFormed_officialLedgerEffect_trajectoryProofSpineTarget_iff_initialFixed_or_pos
      wp y hspace t).trans
      ((officialWellFormedUpdateTrajectory_inFixedSetR_iff_initialFixed_or_pos
        wp y hspace t).symm.trans
        (officialWellFormed_inFixedSetR_iff_ledgerEffectR_eq_zero
          wp
          (officialWellFormedUpdateTrajectory wp y t)
          (officialWellFormedUpdateTrajectory_inRestrictedStateSpace
            wp y hspace t)))

end ProductOfficialRestrictedBridgeLedgerEffectProofSpineEquivalence
end VFH2
