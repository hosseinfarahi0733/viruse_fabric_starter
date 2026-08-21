import VFH2.UnrestrictedBridge.ProductFiniteObservationDynamicProofSpineConservativity

/-!
# Product Finite-Observation Proof-Spine Trajectory Stationarity

This module connects the concrete restricted Product proof spine directly to a
genuine global dynamical property of the countably indexed model. For a Product
state and a `StateU` observation agreeing on the canonical Product window, the
zero-ledger-effect restricted proof-spine target at time `t` holds exactly when
the complete countable trajectory is constant from `t` onward.

The proof is not a wrapper around the public C98 representative theorem. It
derives the countable stationarity classification directly from the existing
`updateU` semantics and idempotence, transfers initial fixedness using only
canonical-window agreement and active-coordinate coverage, and then joins that
classification to the existing restricted Product proof spine.

Boundary:
- Stationarity is global along the trajectory of the supplied `StateU`: every
  natural coordinate is equal at all future times. This is valid because
  `updateU` leaves every inactive coordinate unchanged and is idempotent.
- Canonical-window agreement transfers only the active-coordinate fixedness
  needed by the theorem. It does not reconstruct or equate the unobserved tail
  with the zero-extended Product embedding.
- No state-space bound or model-level assumption is required; canonical-window
  agreement is the theorem's sole hypothesis connecting `x` and `y`. No global
  infinite ledger or new score is introduced.
- The restricted proof spine uses the existing Product ledger effect and exact
  score window `[0, 0]`.
- This is not unrestricted `TTP-VF-H2-004` and not full-theory, empirical,
  physical, or biological validation.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem updateUTrajectory_succ_eq_updateU
    (q : ParamsU)
    (x : StateU)
    (k : Nat) :
    updateUTrajectory q x (Nat.succ k) = updateU q x := by
  induction k with
  | zero =>
      rfl
  | succ k ih =>
      change
        updateU q (updateUTrajectory q x (Nat.succ k)) =
          updateU q x
      rw [ih, updateU_idempotent]

private theorem updateUTrajectory_eq_updateU_of_pos
    (q : ParamsU)
    (x : StateU)
    (t : Nat)
    (ht : 0 < t) :
    updateUTrajectory q x t = updateU q x := by
  cases t with
  | zero =>
      omega
  | succ k =>
      exact updateUTrajectory_succ_eq_updateU q x k

private theorem inFixedSetU_of_updateU_eq_self
    (q : ParamsU)
    (x : StateU)
    (hUpdate : updateU q x = x) :
    inFixedSetU q x := by
  have hFixedUpdated : inFixedSetU q (updateU q x) :=
    updateU_inFixedSetU q x
  rwa [hUpdate] at hFixedUpdated

private theorem updateUTrajectory_stationaryFrom_iff_initialFixed_or_pos
    (q : ParamsU)
    (x : StateU)
    (t : Nat) :
    (∀ u : Nat,
      t ≤ u →
        updateUTrajectory q x u = updateUTrajectory q x t) ↔
      inFixedSetU q x ∨ 0 < t := by
  constructor
  · intro hStationary
    cases t with
    | zero =>
        left
        apply inFixedSetU_of_updateU_eq_self q x
        have hStep := hStationary 1 (by omega)
        simpa [updateUTrajectory] using hStep
    | succ k =>
        exact Or.inr (Nat.succ_pos k)
  · intro hClassification u htu
    rcases hClassification with hInitialFixed | htPositive
    · have hUpdate : updateU q x = x :=
        updateU_eq_self_of_inFixedSetU q x hInitialFixed
      have hTrajectoryInitial :
          ∀ v : Nat, updateUTrajectory q x v = x := by
        intro v
        induction v with
        | zero =>
            rfl
        | succ v ih =>
            simp only [updateUTrajectory]
            rw [ih, hUpdate]
      rw [hTrajectoryInitial u, hTrajectoryInitial t]
    · have huPositive : 0 < u := by
        omega
      rw [
        updateUTrajectory_eq_updateU_of_pos q x u huPositive,
        updateUTrajectory_eq_updateU_of_pos q x t htPositive
      ]

private theorem productFixedSet_iff_inFixedSetU_of_eq_on_window
    (p : ProductRestrictedParams)
    (x : StateU)
    (y : p.State)
    (hObserved :
      ∀ i : Nat,
        i ∈ productWindowU p →
          stateUOfProduct p y i = x i) :
    ProductFixedSet p y ↔
      inFixedSetU (paramsUOfProduct p) x := by
  rw [← inFixedSetU_stateUOfProduct_iff p y]
  constructor
  · intro hFixed i hi
    rw [← hObserved i (productWindowU_covers_active p i hi)]
    exact hFixed i hi
  · intro hFixed i hi
    rw [hObserved i (productWindowU_covers_active p i hi)]
    exact hFixed i hi

/--
For states agreeing on the canonical Product observation window, the concrete
restricted ledger-effect proof-spine target at time `t` is equivalent to global
stationarity of the complete countably indexed trajectory from `t` onward.
-/
theorem restrictedParams_productLedgerEffect_proofSpineTarget_iff_countableTrajectoryStationaryFrom
    (p : ProductRestrictedParams)
    (x : StateU)
    (y : p.State)
    (hObserved :
      ∀ i : Nat,
        i ∈ productWindowU p →
          stateUOfProduct p y i = x i)
    (t : Nat) :
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
        p
        (productUpdateTrajectory p y t)
        (productUpdateState p)
        (productLedgerEffect p)
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          (productUpdateTrajectory p y t)
          (productUpdateState p))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          (productUpdateTrajectory p y t)
          (productUpdateState p)
          (productLedgerEffect p))
        (ProductFixedSet p (productUpdateTrajectory p y t))
        0
        0
        (Int.le_refl 0)
      ↔
    ∀ u : Nat,
      t ≤ u →
        updateUTrajectory (paramsUOfProduct p) x u =
          updateUTrajectory (paramsUOfProduct p) x t := by
  rw [
    ProductRestrictedParamsLedgerEffectProofSpineCharacterization.restrictedParams_productLedgerEffect_proofSpineTarget_iff_productFixedSet
  ]
  rw [← productTrajectoryStationaryFrom_iff_fixedAt]
  rw [productTrajectoryStationaryFrom_iff_initialFixed_or_pos]
  rw [productFixedSet_iff_inFixedSetU_of_eq_on_window p x y hObserved]
  exact
    (updateUTrajectory_stationaryFrom_iff_initialFixed_or_pos
      (paramsUOfProduct p)
      x
      t).symm

end UnrestrictedBridge
end VFH2
