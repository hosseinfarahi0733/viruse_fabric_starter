import VFH2.UnrestrictedBridge.ProductFiniteObservationSignedLedgerEffectRangeCharacterization

/-!
# Product finite-observation signed ledger-effect normal form

This module strengthens the exact arbitrary-state range theorem with a unique
single-support normal form. Fix any active Product coordinate. An integer is
in the signed Product-window effect range exactly when there is a unique
`StateU`, among the states supported only on that fixed coordinate, with that
effect.

The support restriction is global over `Nat`, not merely over the finite
window, so the unobserved tail cannot destroy uniqueness. Support is contained
in one coordinate rather than required to be nonempty: at the capacity
endpoint the unique representative is the zero state.

The theorem does not claim uniqueness in the full effect fiber, where active
value distributions and the infinite tail remain free. It also does not claim
that the representative belongs to `inStateSpaceU`; negative effects may
require a spike above the Product top value.

Only the canonical finite Product window is observed. This does not define a
global infinite ledger, is not unrestricted `TTP-VF-H2-004`, and makes no
full-theory, empirical, physical, medical, causal, or biological validation
claim. No model assumption is introduced.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem sum_ofFn_zero_for_singleSupport
    (n : Nat) :
    (List.ofFn (fun _ : Fin n => 0)).sum = 0 := by
  induction n with
  | zero =>
      simp
  | succ n ih =>
      simp [List.ofFn_succ, ih]

private theorem sum_ofFn_single_for_singleSupport
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
            sum_ofFn_zero_for_singleSupport n
        rw [htail]
        simp
      · subst k
        rw [List.ofFn_succ, List.sum_cons]
        have hzero : (0 : Fin (n + 1)) ≠ j.succ :=
          (Fin.succ_ne_zero j).symm
        simp only [hzero, ↓reduceIte, Nat.zero_add]
        simpa only [Fin.succ_inj] using ih j

private theorem sum_activeValues_eq_of_singleSupport
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
    sum_ofFn_single_for_singleSupport
      (Typed.typedWidth p.d)
      k
      (x k.val)

/--
For every fixed active Product coordinate, an integer lies in the full signed
Product-window range exactly when it has a unique globally single-supported
representative anchored at that coordinate.
-/
theorem existsUnique_singleActiveSupport_ledgerEffectOn_productWindowU_eq_iff_le_activeCapacity
    (p : ProductRestrictedParams)
    (i : ProductIndex p.d)
    (hi : i ∈ p.active)
    (e : Int) :
    (∃ x : StateU,
      ((∀ j : Nat,
          j ≠ (ProductIndex.flatten i).val →
            x j = 0) ∧
        ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          x = e) ∧
      ∀ z : StateU,
        ((∀ j : Nat,
            j ≠ (ProductIndex.flatten i).val →
              z j = 0) ∧
          ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            z = e) →
          z = x) ↔
      e ≤
        ((List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              p.n
            else
              0)).sum : Int) := by
  constructor
  · rintro ⟨x, hx, _⟩
    have hrange :=
      (exists_ledgerEffectOn_productWindowU_eq_iff_empty_zero_or_nonempty_le_activeCapacity
        p
        e).mp
        ⟨x, hx.2⟩
    rcases hrange with ⟨hactive, _⟩ | ⟨_, he⟩
    · simp [hactive] at hi
    · exact he
  · intro he
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
    have heUpper :
        e ≤ (capacity : Int) := by
      simpa [capacity] using he
    have hgapNonneg :
        0 ≤ (capacity : Int) - e := by
      omega
    have hq :
        (q : Int) = (capacity : Int) - e := by
      exact Int.toNat_of_nonneg hgapNonneg
    have hxSupport :
        ∀ j : Nat,
          j ≠ (ProductIndex.flatten i).val →
            x j = 0 := by
      intro j hj
      have hjk : j ≠ k.val := by
        simpa [k] using hj
      simp [x, hjk]
    have hxSum :
        (List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              x w.val
            else
              0)).sum =
          x (ProductIndex.flatten i).val :=
      sum_activeValues_eq_of_singleSupport
        p
        i
        hi
        x
        hxSupport
    have hxAt :
        x (ProductIndex.flatten i).val = q := by
      simp [x, k]
    have hxEffect :
        ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            x =
          e := by
      rw [
        ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues,
        hxSum,
        hxAt
      ]
      change (capacity : Int) - (q : Int) = e
      rw [hq]
      omega
    refine ⟨x, ⟨hxSupport, hxEffect⟩, ?_⟩
    intro z hz
    have hzSum :
        (List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              z w.val
            else
              0)).sum =
          z (ProductIndex.flatten i).val :=
      sum_activeValues_eq_of_singleSupport
        p
        i
        hi
        z
        hz.1
    have hxFormula :=
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        x
    have hzFormula :=
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        z
    rw [hxSum] at hxFormula
    rw [hzSum] at hzFormula
    have htop :
        z (ProductIndex.flatten i).val =
          x (ProductIndex.flatten i).val := by
      apply Int.ofNat_inj.mp
      omega
    funext j
    by_cases hj : j = (ProductIndex.flatten i).val
    · subst j
      exact htop
    · rw [hz.1 j hj, hxSupport j hj]

end UnrestrictedBridge
end VFH2
