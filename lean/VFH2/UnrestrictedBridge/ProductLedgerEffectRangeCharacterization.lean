import VFH2.UnrestrictedBridge.ProductLedgerEffectLevelSetCharacterization

/-!
# Product Ledger-Effect Range Characterization

For fixed restricted Product parameters, this module identifies the exact
image of `productLedgerEffect`. Its values are precisely the integers from
zero through the canonical active capacity, with no gaps.

The capacity is enumerated over `WidthIndex` and tests activity by membership.
Thus every Product coordinate is counted once, and repeated entries in
`p.active` do not enlarge the range. The reverse direction is constructive:
it realizes every value in the interval by a bounded Product state.

Boundary:
- This concerns only the existing finite restricted Product model.
- Realization means existence in its formal typed state space.
- It uses only the canonical finite Product coordinate enumeration.
- It does not define or use a global infinite ledger.
- It is not unrestricted `TTP-VF-H2-004`.
- It makes no full-theory, empirical, physical, or biological claim.
- It introduces no new assumptions.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem sum_ofFn_zero
    (n : Nat) :
    (List.ofFn (fun _ : Fin n => 0)).sum = 0 := by
  induction n with
  | zero =>
      simp
  | succ n ih =>
      simp [List.ofFn_succ, ih]

private theorem sum_ofFn_le_sum_ofFn
    (n : Nat)
    (f g : Fin n → Nat)
    (hpointwise : ∀ i : Fin n, f i ≤ g i) :
    (List.ofFn f).sum ≤ (List.ofFn g).sum := by
  induction n with
  | zero =>
      simp
  | succ n ih =>
      simp only [List.ofFn_succ, List.sum_cons]
      exact
        Nat.add_le_add
          (hpointwise (0 : Fin (n + 1)))
          (ih
            (fun i => f i.succ)
            (fun i => g i.succ)
            (fun i => hpointwise i.succ))

private theorem exists_bounded_ofFn_sum_eq
    (n : Nat)
    (cap : Fin n → Nat)
    (q : Nat)
    (hq : q ≤ (List.ofFn cap).sum) :
    ∃ v : Fin n → Nat,
      (∀ i : Fin n, v i ≤ cap i) ∧
      (List.ofFn v).sum = q := by
  induction n generalizing q with
  | zero =>
      have hqZero : q = 0 := by
        simpa using hq
      subst q
      refine ⟨fun i => Fin.elim0 i, ?_, ?_⟩
      · intro i
        exact Fin.elim0 i
      · simp
  | succ n ih =>
      rw [List.ofFn_succ, List.sum_cons] at hq
      by_cases hqHead : q ≤ cap (0 : Fin (n + 1))
      · let v : Fin (n + 1) → Nat :=
          Fin.cases q (fun _ => 0)
        refine ⟨v, ?_, ?_⟩
        · intro i
          refine Fin.cases ?_ (fun j => ?_) i
          · simpa [v] using hqHead
          · simp [v]
        · simpa [v, List.ofFn_succ] using sum_ofFn_zero n
      · have htail :
          q - cap (0 : Fin (n + 1)) ≤
            (List.ofFn
              (fun i : Fin n => cap i.succ)).sum := by
          omega
        obtain ⟨tail, htailBound, htailSum⟩ :=
          ih
            (fun i : Fin n => cap i.succ)
            (q - cap (0 : Fin (n + 1)))
            htail
        let v : Fin (n + 1) → Nat :=
          Fin.cases (cap (0 : Fin (n + 1))) tail
        refine ⟨v, ?_, ?_⟩
        · intro i
          refine Fin.cases ?_ (fun j => ?_) i
          · simp [v]
          · simpa [v] using htailBound j
        · rw [List.ofFn_succ, List.sum_cons]
          change
            cap (0 : Fin (n + 1)) +
                (List.ofFn tail).sum =
              q
          rw [htailSum]
          omega

/--
For fixed Product parameters, the image of the remaining ledger effect is
exactly the closed integer interval from zero to the canonical active
capacity.
-/
theorem exists_productLedgerEffect_eq_iff_nonneg_and_le_activeCapacity
    (p : ProductRestrictedParams)
    (e : Int) :
    (∃ x : p.State, productLedgerEffect p x = e) ↔
      0 ≤ e ∧
        e ≤
          ((List.ofFn
            (fun w : Typed.WidthIndex p.d =>
              if ProductIndex.unflatten w ∈ p.active then
                p.n
              else
                0)).sum : Int) := by
  constructor
  · rintro ⟨x, hx⟩
    have hformula :=
      productLedgerEffect_eq_sum_activeDeficits p x
    have hsumLe :
        (List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              p.n - (x (ProductIndex.unflatten w)).val
            else
              0)).sum ≤
          (List.ofFn
            (fun w : Typed.WidthIndex p.d =>
              if ProductIndex.unflatten w ∈ p.active then
                p.n
              else
                0)).sum := by
      apply
        sum_ofFn_le_sum_ofFn
          (Typed.typedWidth p.d)
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              p.n - (x (ProductIndex.unflatten w)).val
            else
              0)
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              p.n
            else
              0)
      intro w
      by_cases hw : ProductIndex.unflatten w ∈ p.active
      · simp only [hw, ↓reduceIte]
        omega
      · simp [hw]
    constructor
    · calc
        0 ≤
            ((List.ofFn
              (fun w : Typed.WidthIndex p.d =>
                if ProductIndex.unflatten w ∈ p.active then
                  p.n - (x (ProductIndex.unflatten w)).val
                else
                  0)).sum : Int) :=
          Int.natCast_nonneg _
        _ = productLedgerEffect p x := hformula.symm
        _ = e := hx
    · have hsumLeInt :
          ((List.ofFn
            (fun w : Typed.WidthIndex p.d =>
              if ProductIndex.unflatten w ∈ p.active then
                p.n - (x (ProductIndex.unflatten w)).val
              else
                0)).sum : Int) ≤
            ((List.ofFn
              (fun w : Typed.WidthIndex p.d =>
                if ProductIndex.unflatten w ∈ p.active then
                  p.n
                else
                  0)).sum : Int) := by
        exact_mod_cast hsumLe
      calc
        e = productLedgerEffect p x := hx.symm
        _ =
            ((List.ofFn
              (fun w : Typed.WidthIndex p.d =>
                if ProductIndex.unflatten w ∈ p.active then
                  p.n - (x (ProductIndex.unflatten w)).val
                else
                  0)).sum : Int) :=
          hformula
        _ ≤
            ((List.ofFn
              (fun w : Typed.WidthIndex p.d =>
                if ProductIndex.unflatten w ∈ p.active then
                  p.n
                else
                  0)).sum : Int) :=
          hsumLeInt
  · rintro ⟨heNonneg, heUpper⟩
    cases e with
    | ofNat q =>
        have hq :
            q ≤
              (List.ofFn
                (fun w : Typed.WidthIndex p.d =>
                  if ProductIndex.unflatten w ∈ p.active then
                    p.n
                  else
                    0)).sum := by
          exact Int.ofNat_le.mp heUpper
        obtain ⟨delta, hdeltaBound, hdeltaSum⟩ :=
          exists_bounded_ofFn_sum_eq
            (Typed.typedWidth p.d)
            (fun w : Typed.WidthIndex p.d =>
              if ProductIndex.unflatten w ∈ p.active then
                p.n
              else
                0)
            q
            hq
        let x : p.State :=
          fun i =>
            { val := p.n - delta (ProductIndex.flatten i)
              bound := Nat.sub_le p.n (delta (ProductIndex.flatten i)) }
        have hdeficits :
            List.ofFn
                (fun w : Typed.WidthIndex p.d =>
                  if ProductIndex.unflatten w ∈ p.active then
                    p.n - (x (ProductIndex.unflatten w)).val
                  else
                    0) =
              List.ofFn delta := by
          apply congrArg List.ofFn
          funext w
          by_cases hw : ProductIndex.unflatten w ∈ p.active
          · have hdeltaLe : delta w ≤ p.n := by
              simpa [hw] using hdeltaBound w
            simp only [hw, ↓reduceIte, x, ProductIndex.flatten_unflatten]
            omega
          · have hdeltaZero : delta w = 0 := by
              have hzero := hdeltaBound w
              simp only [hw, ↓reduceIte] at hzero
              omega
            simp [hw, hdeltaZero]
        refine ⟨x, ?_⟩
        rw [productLedgerEffect_eq_sum_activeDeficits p x]
        rw [hdeficits, hdeltaSum]
        rfl
    | negSucc q =>
        omega

end UnrestrictedBridge
end VFH2
