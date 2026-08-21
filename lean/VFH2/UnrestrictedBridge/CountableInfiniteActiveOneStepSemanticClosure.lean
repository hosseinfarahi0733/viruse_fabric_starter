import VFH2.UnrestrictedBridge.CountableInfiniteActiveGlobalLedgerFinalCharacterization

/-!
# Countable Infinite-Active One-Step Semantic Closure

This module derives fixedness and zero residual ledger directly from the
concrete countable update.  The results hold for an arbitrary Boolean active
predicate, including genuinely infinite support.

No fixedness premise, convergence premise, finite-support premise, or score
premise is introduced.
-/

namespace VFH2
namespace UnrestrictedBridge

/-- The concrete infinite-active update preserves the bounded state space. -/
theorem updateInfiniteActiveU_preserves_inInfiniteActiveStateSpaceU
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x) :
    inInfiniteActiveStateSpaceU p (updateInfiniteActiveU p x) := by
  intro i
  cases hi : p.active i with
  | false =>
      simpa [updateInfiniteActiveU, hi] using hspace i
  | true =>
      simp [updateInfiniteActiveU, hi]

/-- One concrete update fixes every active coordinate. -/
theorem updateInfiniteActiveU_inInfiniteActiveFixedSetU
    (p : InfiniteActiveParamsU)
    (x : StateU) :
    inInfiniteActiveFixedSetU p (updateInfiniteActiveU p x) := by
  intro i hi
  simp [updateInfiniteActiveU, hi]

/-- Fixedness is exactly equality with the concrete update. -/
theorem updateInfiniteActiveU_eq_self_iff_inInfiniteActiveFixedSetU
    (p : InfiniteActiveParamsU)
    (x : StateU) :
    updateInfiniteActiveU p x = x ↔
      inInfiniteActiveFixedSetU p x := by
  constructor
  · intro hUpdate i hi
    have hCoordinate := congrFun hUpdate i
    simpa [updateInfiniteActiveU, hi] using hCoordinate.symm
  · intro hfixed
    funext i
    cases hi : p.active i with
    | false =>
        simp [updateInfiniteActiveU, hi]
    | true =>
        simp [updateInfiniteActiveU, hi, hfixed i hi]

/-- The concrete infinite-active update is idempotent. -/
theorem updateInfiniteActiveU_idempotent
    (p : InfiniteActiveParamsU)
    (x : StateU) :
    updateInfiniteActiveU p (updateInfiniteActiveU p x) =
      updateInfiniteActiveU p x := by
  exact
    (updateInfiniteActiveU_eq_self_iff_inInfiniteActiveFixedSetU
      p
      (updateInfiniteActiveU p x)).2
      (updateInfiniteActiveU_inInfiniteActiveFixedSetU p x)

/-- Every residual active-deficit prefix is zero after one update. -/
theorem infiniteActiveLedgerEffectPrefixU_updateInfiniteActiveU_eq_zero
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (cutoff : Nat) :
    infiniteActiveLedgerEffectPrefixU
      p
      (updateInfiniteActiveU p x)
      cutoff = 0 := by
  induction cutoff with
  | zero =>
      rfl
  | succ cutoff ih =>
      calc
        infiniteActiveLedgerEffectPrefixU
              p
              (updateInfiniteActiveU p x)
              (Nat.succ cutoff) =
            infiniteActiveLedgerEffectPrefixU
                p
                (updateInfiniteActiveU p x)
                cutoff +
              (if p.active cutoff then
                p.top - updateInfiniteActiveU p x cutoff
              else 0) := by
                simp [
                  infiniteActiveLedgerEffectPrefixU,
                  List.range_succ
                ]
        _ = 0 := by
          rw [ih]
          cases hActive : p.active cutoff with
          | false =>
              simp
          | true =>
              simp [updateInfiniteActiveU, hActive]

/-- A finite global effect exists after one update and its value is zero. -/
theorem hasInfiniteActiveGlobalLedgerEffectU_updateInfiniteActiveU_zero
    (p : InfiniteActiveParamsU)
    (x : StateU) :
    HasInfiniteActiveGlobalLedgerEffectU
      p
      (updateInfiniteActiveU p x)
      0 := by
  refine ⟨0, ?_⟩
  intro n hn
  exact
    infiniteActiveLedgerEffectPrefixU_updateInfiniteActiveU_eq_zero
      p x n

/-- Every positive trajectory time is exactly the one-step updated state. -/
theorem infiniteActiveUpdateTrajectoryU_succ_eq_updateInfiniteActiveU
    (p : InfiniteActiveParamsU)
    (x : StateU) :
    ∀ t : Nat,
      infiniteActiveUpdateTrajectoryU p x (Nat.succ t) =
        updateInfiniteActiveU p x := by
  intro t
  induction t with
  | zero =>
      rfl
  | succ t ih =>
      change
        updateInfiniteActiveU p
            (infiniteActiveUpdateTrajectoryU p x (Nat.succ t)) =
          updateInfiniteActiveU p x
      rw [ih, updateInfiniteActiveU_idempotent]

/-- Every positive trajectory state is fixed without a fixedness assumption. -/
theorem infiniteActiveUpdateTrajectoryU_inInfiniteActiveFixedSetU_of_pos
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (t : Nat)
    (ht : 0 < t) :
    inInfiniteActiveFixedSetU p
      (infiniteActiveUpdateTrajectoryU p x t) := by
  obtain ⟨u, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : t ≠ 0)
  rw [infiniteActiveUpdateTrajectoryU_succ_eq_updateInfiniteActiveU]
  exact updateInfiniteActiveU_inInfiniteActiveFixedSetU p x

/-- Every positive trajectory state has global residual effect zero. -/
theorem hasInfiniteActiveGlobalLedgerEffectU_infiniteActiveUpdateTrajectoryU_zero_of_pos
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (t : Nat)
    (ht : 0 < t) :
    HasInfiniteActiveGlobalLedgerEffectU
      p
      (infiniteActiveUpdateTrajectoryU p x t)
      0 := by
  obtain ⟨u, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : t ≠ 0)
  rw [infiniteActiveUpdateTrajectoryU_succ_eq_updateInfiniteActiveU]
  exact hasInfiniteActiveGlobalLedgerEffectU_updateInfiniteActiveU_zero p x

end UnrestrictedBridge
end VFH2
