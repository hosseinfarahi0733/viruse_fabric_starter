import VFH2.UnrestrictedBridge.ProductFiniteObservationSignedLedgerEffectFormula

/-!
# Product finite-observation signed ledger-effect range

This module determines the exact image of the Product-window ledger effect
over every countably indexed state. If the Product active list is empty, the
image is exactly `{0}`. If it is nonempty, the image is the integer lower
half-line ending at the canonical membership-masked active capacity.

The reverse direction is constructive. It selects an active Product
coordinate and concentrates the required active-value total at that
coordinate. Thus the result is a genuine range characterization, rather than
a restatement of the pointwise signed formula.

Only the canonical finite Product window is observed. Inactive coordinates
and the infinite tail remain irrelevant. This does not define a global
infinite ledger, is not unrestricted `TTP-VF-H2-004`, and makes no
full-theory, empirical, physical, medical, causal, or biological validation
claim. No model assumption is introduced.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem sum_ofFn_zero_for_single_spike
    (n : Nat) :
    (List.ofFn (fun _ : Fin n => 0)).sum = 0 := by
  induction n with
  | zero =>
      simp
  | succ n ih =>
      simp [List.ofFn_succ, ih]

private theorem sum_ofFn_single_spike
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
            sum_ofFn_zero_for_single_spike n
        rw [htail]
        simp
      · subst k
        rw [List.ofFn_succ, List.sum_cons]
        have hzero : (0 : Fin (n + 1)) ≠ j.succ :=
          (Fin.succ_ne_zero j).symm
        simp only [hzero, ↓reduceIte, Nat.zero_add]
        simpa only [Fin.succ_inj] using ih j

/--
For fixed Product parameters, the image of the signed finite-observation
ledger effect is `{0}` when the active list is empty, and otherwise is the
integer lower half-line ending at the canonical active capacity.
-/
theorem exists_ledgerEffectOn_productWindowU_eq_iff_empty_zero_or_nonempty_le_activeCapacity
    (p : ProductRestrictedParams)
    (e : Int) :
    (∃ x : StateU,
      ledgerEffectOn
        (paramsUOfProduct p)
        (productWindowU p)
        x = e) ↔
      (p.active = [] ∧ e = 0) ∨
      (p.active ≠ [] ∧
        e ≤
          ((List.ofFn
            (fun w : Typed.WidthIndex p.d =>
              if ProductIndex.unflatten w ∈ p.active then
                p.n
              else
                0)).sum : Int)) := by
  constructor
  · rintro ⟨x, hx⟩
    rw [
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
    ] at hx
    by_cases hactive : p.active = []
    · left
      refine ⟨hactive, ?_⟩
      simpa [hactive] using hx.symm
    · right
      refine ⟨hactive, ?_⟩
      rw [← hx]
      omega
  · rintro (⟨hactive, rfl⟩ | ⟨hactive, he⟩)
    · let x : StateU := fun _ => 0
      refine ⟨x, ?_⟩
      rw [
        ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
      ]
      simp [hactive, x]
    · obtain ⟨i, hi⟩ :=
        List.exists_mem_of_ne_nil p.active hactive
      let capacity : Nat :=
        (List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              p.n
            else
              0)).sum
      let k : Typed.WidthIndex p.d :=
        ProductIndex.flatten i
      let q : Nat :=
        Int.toNat ((capacity : Int) - e)
      let x : StateU :=
        fun j =>
          if j = k.val then
            q
          else
            0
      have hkActive :
          ProductIndex.unflatten k ∈ p.active := by
        simpa [k, ProductIndex.unflatten_flatten] using hi
      have hactiveValues :
          List.ofFn
              (fun w : Typed.WidthIndex p.d =>
                if ProductIndex.unflatten w ∈ p.active then
                  x w.val
                else
                  0) =
            List.ofFn
              (fun w : Typed.WidthIndex p.d =>
                if w = k then
                  q
                else
                  0) := by
        apply congrArg List.ofFn
        funext w
        by_cases hwk : w = k
        · subst w
          simp [hkActive, x]
        · have hval : w.val ≠ k.val := by
            intro h
            exact hwk (Fin.ext h)
          simp [hwk, x, hval]
      have hsum :
          (List.ofFn
            (fun w : Typed.WidthIndex p.d =>
              if ProductIndex.unflatten w ∈ p.active then
                x w.val
              else
                0)).sum = q := by
        rw [hactiveValues]
        exact
          sum_ofFn_single_spike
            (Typed.typedWidth p.d)
            k
            q
      have hnonneg :
          0 ≤ (capacity : Int) - e := by
        omega
      have hq :
          (q : Int) = (capacity : Int) - e := by
        exact Int.toNat_of_nonneg hnonneg
      refine ⟨x, ?_⟩
      rw [
        ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues,
        hsum
      ]
      change (capacity : Int) - (q : Int) = e
      rw [hq]
      omega

end UnrestrictedBridge
end VFH2
