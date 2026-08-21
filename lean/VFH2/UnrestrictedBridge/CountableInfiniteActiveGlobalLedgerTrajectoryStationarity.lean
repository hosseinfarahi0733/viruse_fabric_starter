import VFH2.UnrestrictedBridge.CountableInfiniteActiveGlobalLedgerConvergenceCharacterization

/-!
# Countable Infinite-Active Global Ledger Trajectory Stationarity

This module adds the native discrete trajectory of the infinite-active update
and proves the exact dynamical meaning of zero global effect. At every time,
finite convergence to zero is equivalent to equality of the complete
countably indexed state at all later trajectory times.

No finite-support premise or finite Product representation is used.
-/

namespace VFH2
namespace UnrestrictedBridge

/-- Repeated application of the countable infinite-active update. -/
def infiniteActiveUpdateTrajectoryU
    (p : InfiniteActiveParamsU)
    (x : StateU) : Nat → StateU
  | 0 => x
  | Nat.succ t =>
      updateInfiniteActiveU p (infiniteActiveUpdateTrajectoryU p x t)

private theorem c105_updateInfiniteActiveU_preserves_stateSpace
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x) :
    inInfiniteActiveStateSpaceU p (updateInfiniteActiveU p x) := by
  intro i
  cases hActive : p.active i with
  | false =>
      simpa [updateInfiniteActiveU, hActive] using hspace i
  | true =>
      simp [updateInfiniteActiveU, hActive]

private theorem c105_updateInfiniteActiveU_eq_self_iff_fixed
    (p : InfiniteActiveParamsU)
    (x : StateU) :
    updateInfiniteActiveU p x = x ↔
      inInfiniteActiveFixedSetU p x := by
  constructor
  · intro hUpdate i hiActive
    have hCoordinate := congrFun hUpdate i
    simpa [updateInfiniteActiveU, hiActive] using hCoordinate.symm
  · intro hfixed
    funext i
    cases hiActive : p.active i with
    | false =>
        simp [updateInfiniteActiveU, hiActive]
    | true =>
        simp [updateInfiniteActiveU, hfixed i hiActive]

private theorem c105_infiniteActiveUpdateTrajectoryU_inStateSpace
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x) :
    ∀ t : Nat,
      inInfiniteActiveStateSpaceU p
        (infiniteActiveUpdateTrajectoryU p x t) := by
  intro t
  induction t with
  | zero =>
      exact hspace
  | succ t ih =>
      exact c105_updateInfiniteActiveU_preserves_stateSpace p _ ih

/--
At every trajectory time, convergence of the complete infinite-active global
ledger to zero is equivalent to stationarity of the full countable state from
that time onward.
-/
theorem hasInfiniteActiveGlobalLedgerEffectU_infiniteActiveUpdateTrajectoryU_zero_iff_stationaryFrom
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x)
    (t : Nat) :
    HasInfiniteActiveGlobalLedgerEffectU
        p
        (infiniteActiveUpdateTrajectoryU p x t)
        0 ↔
      ∀ u : Nat,
        t ≤ u →
          infiniteActiveUpdateTrajectoryU p x u =
            infiniteActiveUpdateTrajectoryU p x t := by
  have hspaceTrajectory :
      inInfiniteActiveStateSpaceU p
        (infiniteActiveUpdateTrajectoryU p x t) :=
    c105_infiniteActiveUpdateTrajectoryU_inStateSpace p x hspace t
  rw [
    hasInfiniteActiveGlobalLedgerEffectU_zero_iff_inInfiniteActiveFixedSetU
      p
      (infiniteActiveUpdateTrajectoryU p x t)
      hspaceTrajectory,
    ← c105_updateInfiniteActiveU_eq_self_iff_fixed
  ]
  constructor
  · intro hFixed u htu
    induction u with
    | zero =>
        have ht : t = 0 := by omega
        subst t
        rfl
    | succ u ih =>
        by_cases hEq : t = Nat.succ u
        · subst t
          rfl
        · have htu' : t ≤ u := by omega
          change
            updateInfiniteActiveU p
                (infiniteActiveUpdateTrajectoryU p x u) =
              infiniteActiveUpdateTrajectoryU p x t
          rw [ih htu', hFixed]
  · intro hStationary
    have hStep := hStationary (Nat.succ t) (by omega)
    simpa [infiniteActiveUpdateTrajectoryU] using hStep

end UnrestrictedBridge
end VFH2
