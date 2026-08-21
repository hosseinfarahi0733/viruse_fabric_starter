import VFH2.UnrestrictedBridge.ProductFiniteObservationDynamicProofSpineConservativity

/-!
# Countable Finite-Active Global Ledger Effect

This module gives the countably indexed `ParamsU` model a canonical global
update ledger effect when its active support is the existing finite `List Nat`.
Unlike `ledgerEffectOn`, the definition accepts no observation window: it sums
exactly the active support. `List.eraseDups` makes repeated active indices
semantically irrelevant while preserving a computable finite enumeration.

For states in the existing `inStateSpaceU`, the global effect is the exact sum
of the distinct active-coordinate deficits. Consequently it is nonnegative,
vanishes exactly on `inFixedSetU`, and is positive exactly off that fixed set.
The active-coordinate bounds supplied by the existing `inStateSpaceU`
invariant are needed for the nonnegative natural-deficit characterization.
Using the full invariant keeps the theorem on the established admissible
domain, although no bound on inactive tail coordinates enters the proof.

Boundary:
- The ambient state remains countably indexed, but active support is finite.
- This is a finite sum over the complete active support, not an infinite series
  and it needs no summability or convergence assumption.
- This does not define genuinely infinite active support.
- This is not yet unrestricted `TTP-VF-H2-004` and makes no full-theory,
  empirical, physical, or biological claim.
- No Product object occurs in these definitions or theorem statements; the
  import only reuses the existing generic `updateUTrajectory` declaration.
- No compatibility namespace or new front door is introduced.
-/

namespace VFH2
namespace UnrestrictedBridge

/--
The signed change in the canonical ledger over all distinct active coordinates.

There is no observation-window argument. The active list is deduplicated before
both ledger totals are formed, so coordinate multiplicity cannot alter the
value.
-/
def finiteActiveGlobalLedgerEffectU
    (p : ParamsU)
    (x : StateU) : Int :=
  ((p.active.eraseDups.map fun i => updateU p x i).sum : Int) -
    ((p.active.eraseDups.map fun i => x i).sum : Int)

private theorem map_eq_map_of_forall_mem
    {α β : Type}
    (support : List α)
    (f g : α → β)
    (h : ∀ a : α, a ∈ support → f a = g a) :
    support.map f = support.map g := by
  induction support with
  | nil =>
      rfl
  | cons a support ih =>
      have ha : f a = g a :=
        h a (by simp)
      have htail : ∀ b : α, b ∈ support → f b = g b := by
        intro b hb
        exact h b (by simp [hb])
      simp only [List.map_cons, ha]
      rw [ih htail]

private theorem intCast_sum_sub_intCast_sum_eq_sum_signedDifferences
    (support : List Nat)
    (a b : Nat → Nat) :
    ((support.map a).sum : Int) -
        ((support.map b).sum : Int) =
      (support.map fun i => (a i : Int) - (b i : Int)).sum := by
  induction support with
  | nil =>
      rfl
  | cons i support ih =>
      simp only [List.map_cons, List.sum_cons]
      push_cast
      omega

private theorem eq_zero_of_mem_of_natList_sum_eq_zero
    (values : List Nat)
    (value : Nat)
    (hmem : value ∈ values)
    (hsum : values.sum = 0) :
    value = 0 := by
  induction values with
  | nil =>
      simp at hmem
  | cons head tail ih =>
      simp only [List.sum_cons] at hsum
      simp only [List.mem_cons] at hmem
      rcases hmem with rfl | htail
      · omega
      · exact ih htail (by omega)

/--
Without any state-space hypothesis, the global effect is the exact sum of the
signed changes required at the distinct active coordinates.
-/
theorem finiteActiveGlobalLedgerEffectU_eq_sum_activeSignedDeficits
    (p : ParamsU)
    (x : StateU) :
    finiteActiveGlobalLedgerEffectU p x =
      (p.active.eraseDups.map fun i =>
        (p.top : Int) - (x i : Int)).sum := by
  unfold finiteActiveGlobalLedgerEffectU
  rw [
    intCast_sum_sub_intCast_sum_eq_sum_signedDifferences
      p.active.eraseDups
      (updateU p x)
      x
  ]
  apply congrArg List.sum
  apply
    map_eq_map_of_forall_mem
      p.active.eraseDups
      (fun i => (updateU p x i : Int) - (x i : Int))
      (fun i => (p.top : Int) - (x i : Int))
  intro i hi
  rw [updateU_apply_of_mem p x (List.mem_eraseDups.mp hi)]

/-
For a bounded state, the window-free global effect is exactly the sum of the
natural deficits at the distinct active coordinates.
-/
private theorem finiteActiveGlobalLedgerEffectU_eq_sum_activeDeficits
    (p : ParamsU)
    (x : StateU)
    (hspace : inStateSpaceU p x) :
    finiteActiveGlobalLedgerEffectU p x =
      ((p.active.eraseDups.map fun i => p.top - x i).sum : Int) := by
  rw [finiteActiveGlobalLedgerEffectU_eq_sum_activeSignedDeficits p x]
  induction p.active.eraseDups with
  | nil =>
      rfl
  | cons i support ih =>
      simp only [List.map_cons, List.sum_cons]
      push_cast
      rw [ih]
      have hi : x i ≤ p.top :=
        hspace i
      omega

/- Every bounded state has a nonnegative finite-active global ledger effect. -/
private theorem finiteActiveGlobalLedgerEffectU_nonneg
    (p : ParamsU)
    (x : StateU)
    (hspace : inStateSpaceU p x) :
    0 ≤ finiteActiveGlobalLedgerEffectU p x := by
  rw [finiteActiveGlobalLedgerEffectU_eq_sum_activeDeficits p x hspace]
  omega

/--
For a bounded state, the global effect vanishes exactly when every active
coordinate is fixed. Duplicate active entries and the empty active list are
handled by the canonical deduplicated support.
-/
theorem finiteActiveGlobalLedgerEffectU_eq_zero_iff_inFixedSetU
    (p : ParamsU)
    (x : StateU)
    (hspace : inStateSpaceU p x) :
    finiteActiveGlobalLedgerEffectU p x = 0 ↔
      inFixedSetU p x := by
  constructor
  · intro hzero i hi
    have hsumZero :
        (p.active.eraseDups.map fun j => p.top - x j).sum = 0 := by
      have hformula :=
        finiteActiveGlobalLedgerEffectU_eq_sum_activeDeficits p x hspace
      rw [hformula] at hzero
      omega
    have hdeficitMem :
        p.top - x i ∈
          (p.active.eraseDups.map fun j => p.top - x j) := by
      exact
        List.mem_map.mpr
          ⟨i, List.mem_eraseDups.mpr hi, rfl⟩
    have hdeficitZero : p.top - x i = 0 :=
      eq_zero_of_mem_of_natList_sum_eq_zero
        (p.active.eraseDups.map fun j => p.top - x j)
        (p.top - x i)
        hdeficitMem
        hsumZero
    have hle : x i ≤ p.top :=
      hspace i
    omega
  · intro hfixed
    have hUpdate : updateU p x = x :=
      updateU_eq_self_of_inFixedSetU p x hfixed
    simp [finiteActiveGlobalLedgerEffectU, hUpdate]

/--
For a bounded state, the global effect is strictly positive exactly away from
the active-coordinate fixed set.
-/
theorem finiteActiveGlobalLedgerEffectU_pos_iff_not_inFixedSetU
    (p : ParamsU)
    (x : StateU)
    (hspace : inStateSpaceU p x) :
    0 < finiteActiveGlobalLedgerEffectU p x ↔
      ¬ inFixedSetU p x := by
  constructor
  · intro hpos hfixed
    have hzero : finiteActiveGlobalLedgerEffectU p x = 0 :=
      (finiteActiveGlobalLedgerEffectU_eq_zero_iff_inFixedSetU
        p
        x
        hspace).2 hfixed
    omega
  · intro hnotfixed
    have hnonneg : 0 ≤ finiteActiveGlobalLedgerEffectU p x :=
      finiteActiveGlobalLedgerEffectU_nonneg p x hspace
    have hne : finiteActiveGlobalLedgerEffectU p x ≠ 0 := by
      intro hzero
      exact
        hnotfixed
          ((finiteActiveGlobalLedgerEffectU_eq_zero_iff_inFixedSetU
            p
            x
            hspace).1 hzero)
    omega

private theorem updateU_eq_self_iff_inFixedSetU
    (p : ParamsU)
    (x : StateU) :
    updateU p x = x ↔
      inFixedSetU p x := by
  constructor
  · intro hUpdate i hi
    have hCoordinate := congrFun hUpdate i
    simpa [updateU, hi] using hCoordinate.symm
  · intro hfixed
    exact updateU_eq_self_of_inFixedSetU p x hfixed

/--
Along the countable trajectory, zero total finite-active effect at time `t` is
equivalent to global stationarity from `t` onward. Equality here is equality of
the complete `StateU` functions along their own trajectory; it does not compare
an unobserved tail with a finite Product embedding.
-/
theorem finiteActiveGlobalLedgerEffectU_updateUTrajectory_eq_zero_iff_stationaryFrom
    (p : ParamsU)
    (x : StateU)
    (hspace : inStateSpaceU p x)
    (t : Nat) :
    finiteActiveGlobalLedgerEffectU p (updateUTrajectory p x t) = 0 ↔
      ∀ u : Nat,
        t ≤ u →
        updateUTrajectory p x u = updateUTrajectory p x t := by
  have hspaceTrajectory :
      inStateSpaceU p (updateUTrajectory p x t) := by
    induction t with
    | zero =>
        exact hspace
    | succ t ih =>
        exact updateU_preserves_inStateSpaceU p _ ih
  rw [
    finiteActiveGlobalLedgerEffectU_eq_zero_iff_inFixedSetU
      p
      (updateUTrajectory p x t)
      hspaceTrajectory,
    ← updateU_eq_self_iff_inFixedSetU
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
            updateU p (updateUTrajectory p x u) =
              updateUTrajectory p x t
          rw [ih htu', hFixed]
  · intro hStationary
    have hStep := hStationary (Nat.succ t) (by omega)
    simpa [updateUTrajectory] using hStep

end UnrestrictedBridge
end VFH2
