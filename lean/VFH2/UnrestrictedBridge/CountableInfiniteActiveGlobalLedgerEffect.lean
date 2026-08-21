import VFH2.UnrestrictedBridge.ProductFiniteActiveGlobalLedgerEffectTrajectoryConservativity

/-!
# Countable Infinite-Active Global Ledger Effect

This module introduces a separate countably indexed parameter model whose
active support is a Boolean predicate rather than a finite list. Its prefix
ledger effect is the natural sum of active-coordinate deficits below a cutoff.
For bounded states this prefix is exactly the signed change of the corresponding
finite ledger under the infinite-active update.

Because every summand is a natural number, convergence to a finite global
effect is represented explicitly by eventual constancy of the prefix effects.
The main theorem proves that convergence to zero is equivalent to every active
coordinate already being fixed, even when the active predicate has genuinely
infinite support.

Boundary:
- Finite support is not assumed or encoded in the parameter type.
- A finite global effect is not asserted for every state; convergence is an
  explicit hypothesis expressed by `HasInfiniteActiveGlobalLedgerEffectU`.
- The result concerns a nonnegative countable deficit ledger. It does not
  introduce conditionally convergent integer series.
- This is a proof-only bridge milestone, not an empirical, physical, or
  biological validation claim.
- No claim beyond the definitions and theorem statements in this module is
  made.
-/

namespace VFH2
namespace UnrestrictedBridge

/-- Parameters with a countably indexed, potentially infinite active support. -/
structure InfiniteActiveParamsU where
  top : Nat
  active : Nat → Bool

/-- Every coordinate is bounded by the common top value. -/
def inInfiniteActiveStateSpaceU
    (p : InfiniteActiveParamsU)
    (x : StateU) : Prop :=
  ∀ i : Nat, x i ≤ p.top

/-- Every coordinate selected by the active predicate is already at the top. -/
def inInfiniteActiveFixedSetU
    (p : InfiniteActiveParamsU)
    (x : StateU) : Prop :=
  ∀ i : Nat, p.active i = true → x i = p.top

/-- Set every selected coordinate to the top and preserve every other value. -/
def updateInfiniteActiveU
    (p : InfiniteActiveParamsU)
    (x : StateU) : StateU :=
  fun i => if p.active i then p.top else x i

/-- The accumulated nonnegative active-coordinate deficit below `cutoff`. -/
def infiniteActiveLedgerEffectPrefixU
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (cutoff : Nat) : Nat :=
  (List.range cutoff |>.map fun i =>
    if p.active i then p.top - x i else 0).sum

/--
The countable nonnegative ledger has finite value `effect` when its prefix
effects are eventually constant at `effect`.
-/
def HasInfiniteActiveGlobalLedgerEffectU
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (effect : Nat) : Prop :=
  ∃ cutoff : Nat, ∀ n : Nat, cutoff ≤ n →
    infiniteActiveLedgerEffectPrefixU p x n = effect

private theorem c103_eq_zero_of_mem_of_natList_sum_eq_zero
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

private theorem c103_natList_sum_eq_zero_of_forall_mem_eq_zero
    (values : List Nat)
    (hzero : ∀ value : Nat, value ∈ values → value = 0) :
    values.sum = 0 := by
  induction values with
  | nil =>
      rfl
  | cons head tail ih =>
      have hhead : head = 0 := hzero head (by simp)
      have htail : ∀ value : Nat, value ∈ tail → value = 0 := by
        intro value hmem
        exact hzero value (by simp [hmem])
      simp [hhead, ih htail]

private theorem c103_prefix_eq_ledger_change_on_list
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x)
    (support : List Nat) :
    (((support.map fun i =>
        if p.active i then p.top - x i else 0).sum : Nat) : Int) =
      ((support.map fun i => updateInfiniteActiveU p x i).sum : Int) -
        ((support.map fun i => x i).sum : Int) := by
  induction support with
  | nil =>
      rfl
  | cons i support ih =>
      simp only [List.map_cons, List.sum_cons]
      push_cast
      rw [ih]
      cases hi : p.active i with
      | false =>
          simp [updateInfiniteActiveU, hi]
          omega
      | true =>
          have hle : x i ≤ p.top := hspace i
          simp [updateInfiniteActiveU, hi]
          omega

/--
For every finite cutoff of a bounded state, the natural deficit prefix is
exactly the signed ledger change induced by the infinite-active update.
-/
theorem infiniteActiveLedgerEffectPrefixU_eq_ledgerChange
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x)
    (cutoff : Nat) :
    (infiniteActiveLedgerEffectPrefixU p x cutoff : Int) =
      (((List.range cutoff).map fun i =>
          updateInfiniteActiveU p x i).sum : Int) -
        (((List.range cutoff).map fun i => x i).sum : Int) := by
  unfold infiniteActiveLedgerEffectPrefixU
  exact
    c103_prefix_eq_ledger_change_on_list
      p
      x
      hspace
      (List.range cutoff)

/--
For a bounded countable state, the convergent infinite-active global ledger has
value zero exactly when every active coordinate is fixed. The statement makes
no finiteness assumption on the Boolean active predicate.
-/
theorem hasInfiniteActiveGlobalLedgerEffectU_zero_iff_inInfiniteActiveFixedSetU
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x) :
    HasInfiniteActiveGlobalLedgerEffectU p x 0 ↔
      inInfiniteActiveFixedSetU p x := by
  constructor
  · rintro ⟨cutoff, hEventually⟩
    intro i hiActive
    let n := Nat.max cutoff (Nat.succ i)
    have hCutoff : cutoff ≤ n := Nat.le_max_left _ _
    have hiLt : i < n := by
      have hmax : Nat.succ i ≤ n :=
        Nat.le_max_right cutoff (Nat.succ i)
      omega
    have hsum :
        (List.range n |>.map fun j =>
          if p.active j then p.top - x j else 0).sum = 0 := by
      exact hEventually n hCutoff
    have hmemRange : i ∈ List.range n :=
      List.mem_range.mpr hiLt
    have hmemValue :
        (if p.active i then p.top - x i else 0) ∈
          (List.range n |>.map fun j =>
            if p.active j then p.top - x j else 0) := by
      exact List.mem_map.mpr ⟨i, hmemRange, rfl⟩
    have hdeficitZero :
        (if p.active i then p.top - x i else 0) = 0 :=
      c103_eq_zero_of_mem_of_natList_sum_eq_zero
        (List.range n |>.map fun j =>
          if p.active j then p.top - x j else 0)
        (if p.active i then p.top - x i else 0)
        hmemValue
        hsum
    have hsub : p.top - x i = 0 := by
      simpa [hiActive] using hdeficitZero
    have hle : x i ≤ p.top := hspace i
    omega
  · intro hfixed
    refine ⟨0, ?_⟩
    intro n hn
    unfold infiniteActiveLedgerEffectPrefixU
    apply c103_natList_sum_eq_zero_of_forall_mem_eq_zero
    intro deficit hdeficit
    rcases List.mem_map.mp hdeficit with ⟨i, hiRange, rfl⟩
    cases hiActive : p.active i with
    | false =>
        simp
    | true =>
        simp [hfixed i hiActive]

end UnrestrictedBridge
end VFH2
