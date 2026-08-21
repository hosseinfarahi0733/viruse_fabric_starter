import VFH2.UnrestrictedBridge.ProductFiniteObservationSignedLedgerEffectNormalForm

/-!
# Product finite-observation state-space signed ledger-effect normal form

This module identifies exactly when the unique fixed-anchor, globally
single-supported normal form from the preceding arbitrary-state theorem is
admissible. For a fixed active Product coordinate, the bounded normal-form
effects form the closed signed interval from the canonical active capacity
minus one coordinate's top value through the capacity itself.

The lower endpoint is essential. When several distinct Product coordinates
are active, a state supported only on one of them leaves the other active
coordinates at zero, so this single-support class generally realizes only the
top layer of the full admissible effect range.

Existence and uniqueness are encoded explicitly because an `ExistsUnique`
notation is not imported by this project. Uniqueness is only within the class of
states globally supported on the fixed coordinate and satisfying
`inStateSpaceU`; no uniqueness in the full effect fiber is claimed.

Only the canonical finite Product window is observed. This does not define a
global infinite ledger, is not unrestricted `TTP-VF-H2-004`, and makes no
full-theory, empirical, physical, medical, causal, or biological validation
claim. No model assumption is introduced.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem sum_ofFn_zero_for_stateSpaceSingleSupport
    (n : Nat) :
    (List.ofFn (fun _ : Fin n => 0)).sum = 0 := by
  induction n with
  | zero =>
      simp
  | succ n ih =>
      simp [List.ofFn_succ, ih]

private theorem sum_ofFn_single_for_stateSpaceSingleSupport
    (n : Nat)
    (k : Fin n)
    (q : Nat) :
    (List.ofFn
      (fun w : Fin n =>
        if w = k then
          q
        else
          0)).sum = q := by
  induction n with
  | zero =>
      exact Fin.elim0 k
  | succ n ih =>
      rcases Fin.eq_zero_or_eq_succ k with hk | ⟨j, hk⟩
      · subst k
        rw [List.ofFn_succ, List.sum_cons]
        simp only [↓reduceIte]
        have htail :
            (List.ofFn
              (fun w : Fin n =>
                if w.succ = (0 : Fin (n + 1)) then
                  q
                else
                  0)).sum = 0 := by
          simpa only [Fin.succ_ne_zero, ↓reduceIte] using
            sum_ofFn_zero_for_stateSpaceSingleSupport n
        rw [htail]
        simp
      · subst k
        rw [List.ofFn_succ, List.sum_cons]
        have hzero : (0 : Fin (n + 1)) ≠ j.succ :=
          (Fin.succ_ne_zero j).symm
        simp only [hzero, ↓reduceIte, Nat.zero_add]
        simpa only [Fin.succ_inj] using ih j

private theorem sum_activeValues_eq_of_stateSpaceSingleSupport
    (p : ProductRestrictedParams)
    (i : ProductIndex p.d)
    (hi : i ∈ p.active)
    (x : StateU)
    (hx :
      ∀ j : Nat,
        j ≠ (ProductIndex.flatten i).val →
          x j = 0) :
    (List.ofFn
      (fun w : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten w ∈ p.active then
          x w.val
        else
          0)).sum =
      x (ProductIndex.flatten i).val := by
  let k : Typed.WidthIndex p.d :=
    ProductIndex.flatten i
  have hkActive :
      ProductIndex.unflatten k ∈ p.active := by
    simpa [k, ProductIndex.unflatten_flatten] using hi
  have hmasked :
      List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              x w.val
            else
              0) =
        List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if w = k then
              x k.val
            else
              0) := by
    apply congrArg List.ofFn
    funext w
    by_cases hwk : w = k
    · subst w
      simp [hkActive]
    · have hval : w.val ≠ k.val := by
        intro h
        exact hwk (Fin.ext h)
      have hxZero : x w.val = 0 := by
        exact hx w.val (by simpa [k] using hval)
      simp [hwk, hxZero]
  rw [hmasked]
  simpa [k] using
    sum_ofFn_single_for_stateSpaceSingleSupport
      (Typed.typedWidth p.d)
      k
      (x k.val)

/--
For every fixed active Product coordinate, an integer has a unique admissible,
globally single-supported representative at that coordinate exactly when it
lies between active capacity minus one top value and active capacity.
-/
theorem existsUnique_singleActiveSupport_inStateSpaceU_ledgerEffectOn_productWindowU_eq_iff_activeCapacity_sub_n_le_and_le
    (p : ProductRestrictedParams)
    (i : ProductIndex p.d)
    (hi : i ∈ p.active)
    (e : Int) :
    (∃ x : StateU,
      ((∀ j : Nat,
          j ≠ (ProductIndex.flatten i).val →
            x j = 0) ∧
        inStateSpaceU
          (paramsUOfProduct p)
          x ∧
        ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          x = e) ∧
      ∀ z : StateU,
        ((∀ j : Nat,
            j ≠ (ProductIndex.flatten i).val →
              z j = 0) ∧
          inStateSpaceU
            (paramsUOfProduct p)
            z ∧
          ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            z = e) →
          z = x) ↔
      ((List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              p.n
            else
              0)).sum : Int) -
          (p.n : Int) ≤ e ∧
      e ≤
        ((List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              p.n
            else
              0)).sum : Int) := by
  let capacity : Nat :=
    (List.ofFn
      (fun w : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten w ∈ p.active then
          p.n
        else
          0)).sum
  constructor
  · rintro ⟨x, hx, _⟩
    have hxSum :
        (List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              x w.val
            else
              0)).sum =
          x (ProductIndex.flatten i).val :=
      sum_activeValues_eq_of_stateSpaceSingleSupport
        p
        i
        hi
        x
        hx.1
    have hxFormula :=
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        x
    rw [hxSum] at hxFormula
    change
      ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          x =
        (capacity : Int) -
          (x (ProductIndex.flatten i).val : Int) at hxFormula
    have hxBound :
        x (ProductIndex.flatten i).val ≤ p.n := by
      have h := hx.2.1 (ProductIndex.flatten i).val
      change x (ProductIndex.flatten i).val ≤ p.n at h
      exact h
    constructor
    · change (capacity : Int) - (p.n : Int) ≤ e
      omega
    · change e ≤ (capacity : Int)
      omega
  · rintro ⟨heLower, heUpper⟩
    have hbase :=
      (existsUnique_singleActiveSupport_ledgerEffectOn_productWindowU_eq_iff_le_activeCapacity
        p
        i
        hi
        e).mpr
        heUpper
    rcases hbase with ⟨x, hx, hxUnique⟩
    have hxSum :
        (List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              x w.val
            else
              0)).sum =
          x (ProductIndex.flatten i).val :=
      sum_activeValues_eq_of_stateSpaceSingleSupport
        p
        i
        hi
        x
        hx.1
    have hxFormula :=
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        x
    rw [hxSum] at hxFormula
    change
      ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          x =
        (capacity : Int) -
          (x (ProductIndex.flatten i).val : Int) at hxFormula
    have hxBound :
        x (ProductIndex.flatten i).val ≤ p.n := by
      change (capacity : Int) - (p.n : Int) ≤ e at heLower
      omega
    have hxSpace :
        inStateSpaceU
          (paramsUOfProduct p)
          x := by
      intro j
      change x j ≤ p.n
      by_cases hj :
          j = (ProductIndex.flatten i).val
      · subst j
        exact hxBound
      · rw [hx.1 j hj]
        exact Nat.zero_le _
    refine ⟨x, ⟨hx.1, hxSpace, hx.2⟩, ?_⟩
    intro z hz
    exact hxUnique z ⟨hz.1, hz.2.2⟩

end UnrestrictedBridge
end VFH2
