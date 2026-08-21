import VFH2.UnrestrictedBridge.ProductConservativity

/-!
# Product finite-observation signed ledger-effect formula

This module computes the Product-window ledger effect directly for every
countably indexed state, without a boundedness premise. The result is the
canonical membership-masked active capacity minus the corresponding total of
the observed active-coordinate values, with the subtraction performed in
`Int`.

Consequently, observations above the Product top value may have negative
effect; no nonnegativity claim is made outside the admissible state space.
Only the canonical finite Product window is used, so the infinite tail remains
unobserved. This does not define a global infinite ledger, is not unrestricted
`TTP-VF-H2-004`, and makes no full-theory, empirical, physical, or biological
validation claim. No model assumption is introduced.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem ledgerOn_eq_sum_map
    (window : List Nat)
    (x : StateU) :
    ledgerOn window x =
      (window.map fun i => x i).sum := by
  unfold ledgerOn
  rw [List.sum_eq_foldl_nat, List.foldl_map]

private theorem ledgerEffectOn_eq_sum_activeSignedDeficits
    (p : ParamsU)
    (window : List Nat)
    (x : StateU) :
    ledgerEffectOn p window x =
      (window.map fun i =>
        if i ∈ p.active then
          (p.top : Int) - (x i : Int)
        else
          0).sum := by
  unfold ledgerEffectOn
  rw [
    ledgerOn_eq_sum_map window (updateU p x),
    ledgerOn_eq_sum_map window x
  ]
  induction window with
  | nil =>
      simp
  | cons i window ih =>
      simp only [List.map_cons, List.sum_cons, Int.natCast_add]
      rw [← ih]
      by_cases hi : i ∈ p.active
      · simp [updateU, hi]
        omega
      · simp [updateU, hi]
        omega

private theorem map_range_eq_ofFn_signed
    {α : Type}
    (n : Nat)
    (f : Nat → α) :
    (List.range n).map f =
      List.ofFn (fun i : Fin n => f i.val) := by
  induction n with
  | zero =>
      simp
  | succ n ih =>
      rw [List.range_succ, List.map_append, List.ofFn_succ_last]
      simpa using congrArg (fun xs => xs ++ [f n]) ih

private theorem val_mem_paramsUOfProduct_active_iff_signed
    (p : ProductRestrictedParams)
    (w : Typed.WidthIndex p.d) :
    w.val ∈ (paramsUOfProduct p).active ↔
      ProductIndex.unflatten w ∈ p.active := by
  unfold paramsUOfProduct paramsUOfRestricted
  change
    w.val ∈
        (ProductParamsTransport.typedParamsOfProduct p).active.map
          (fun v => v.val) ↔
      ProductIndex.unflatten w ∈ p.active
  constructor
  · intro hw
    rcases List.mem_map.mp hw with ⟨v, hv, hval⟩
    have hvw : v = w := by
      apply Fin.ext
      exact hval
    subst v
    exact
      (ProductUpdateTransport.mem_typed_active_iff_unflatten_mem_product_active
        p
        w).mp hv
  · intro hw
    exact
      List.mem_map.mpr
        ⟨w,
          (ProductUpdateTransport.mem_typed_active_iff_unflatten_mem_product_active
            p
            w).mpr hw,
          rfl⟩

private theorem productWindow_activeSignedDeficits_eq_ofFn
    (p : ProductRestrictedParams)
    (x : StateU) :
    (productWindowU p).map
        (fun i =>
          if i ∈ (paramsUOfProduct p).active then
            ((paramsUOfProduct p).top : Int) - (x i : Int)
          else
            0) =
      List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            (p.n : Int) - (x w.val : Int)
          else
            0) := by
  change
    (List.range (Typed.typedWidth p.d)).map
        (fun i =>
          if i ∈ (paramsUOfProduct p).active then
            ((paramsUOfProduct p).top : Int) - (x i : Int)
          else
            0) =
      List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            (p.n : Int) - (x w.val : Int)
          else
            0)
  rw [map_range_eq_ofFn_signed]
  apply congrArg List.ofFn
  funext w
  by_cases hw : ProductIndex.unflatten w ∈ p.active
  · have hwU : w.val ∈ (paramsUOfProduct p).active :=
      (val_mem_paramsUOfProduct_active_iff_signed p w).mpr hw
    simp only [hw, hwU, ↓reduceIte]
    rfl
  · have hwU : w.val ∉ (paramsUOfProduct p).active := by
      intro hwU
      exact
        hw
          ((val_mem_paramsUOfProduct_active_iff_signed p w).mp hwU)
    simp [hw, hwU]

private theorem sum_ofFn_signed_eq_sub_natCast_sums_for_formula
    (n : Nat)
    (f g : Fin n → Nat)
    (delta : Fin n → Int)
    (hpointwise :
      ∀ i : Fin n,
        delta i = (g i : Int) - (f i : Int)) :
    (List.ofFn delta).sum =
      ((List.ofFn g).sum : Int) -
        ((List.ofFn f).sum : Int) := by
  induction n with
  | zero =>
      simp
  | succ n ih =>
      simp only [List.ofFn_succ, List.sum_cons, Int.natCast_add]
      rw [
        ih
          (fun i => f i.succ)
          (fun i => g i.succ)
          (fun i => delta i.succ)
          (fun i => hpointwise i.succ)
      ]
      have hzero := hpointwise (0 : Fin (n + 1))
      omega

/--
For every countably indexed state, the Product-window ledger effect is the
canonical active capacity minus the canonical total of observed active values.
The subtraction is signed and therefore also covers unbounded observations.
-/
theorem ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
    (p : ProductRestrictedParams)
    (x : StateU) :
    ledgerEffectOn
        (paramsUOfProduct p)
        (productWindowU p)
        x =
      ((List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            p.n
          else
            0)).sum : Int) -
      ((List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            x w.val
          else
            0)).sum : Int) := by
  rw [
    ledgerEffectOn_eq_sum_activeSignedDeficits,
    productWindow_activeSignedDeficits_eq_ofFn
  ]
  exact
    sum_ofFn_signed_eq_sub_natCast_sums_for_formula
      (Typed.typedWidth p.d)
      (fun w : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten w ∈ p.active then
          x w.val
        else
          0)
      (fun w : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten w ∈ p.active then
          p.n
        else
          0)
      (fun w : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten w ∈ p.active then
          (p.n : Int) - (x w.val : Int)
        else
          0)
      (by
        intro w
        by_cases hw : ProductIndex.unflatten w ∈ p.active <;>
          simp [hw])

end UnrestrictedBridge
end VFH2
