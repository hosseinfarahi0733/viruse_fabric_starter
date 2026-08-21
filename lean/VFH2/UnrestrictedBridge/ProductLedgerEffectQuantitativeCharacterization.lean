import VFH2.UnrestrictedBridge.LedgerEffectQuantitativeCharacterization
import VFH2.UnrestrictedBridge.ProductAdmissibility

/-!
# Product Ledger-Effect Quantitative Characterization

This module transports the exact finite-observation deficit formula back to
the native Product coordinates. The canonical `WidthIndex` enumeration visits
every Product coordinate exactly once, in flattened row-major order, and
`ProductIndex.unflatten` restores the corresponding structured coordinate.

The formula tests membership in `p.active` instead of summing that list.
Consequently, repeated entries in the active list do not multiply a
coordinate's contribution, matching the membership-based Product update.

Boundary:
- This is a quantitative conservativity result for the existing finite
  restricted Product model.
- It uses only the canonical finite Product observation window.
- It does not define or use a global infinite ledger.
- It is not unrestricted `TTP-VF-H2-004`.
- It makes no full-theory, empirical, or biological claim.
- It introduces no new assumptions.
-/

namespace VFH2
namespace UnrestrictedBridge

open ProductOfficialRestrictedBridgeStateTransport

private theorem map_range_eq_ofFn
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

private theorem val_mem_paramsUOfProduct_active_iff
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

private theorem stateUOfProduct_apply_width
    (p : ProductRestrictedParams)
    (x : p.State)
    (w : Typed.WidthIndex p.d) :
    stateUOfProduct p x w.val =
      (x (ProductIndex.unflatten w)).val := by
  change
    (officialRestrictedState p x).getD w.val 0 =
      (x (ProductIndex.unflatten w)).val
  simpa only [ProductIndex.flatten_unflatten] using
    officialRestrictedState_getD_flatten
      p
      x
      (ProductIndex.unflatten w)

private theorem productWindow_activeDeficits_eq_ofFn
    (p : ProductRestrictedParams)
    (x : p.State) :
    (productWindowU p).map
        (fun i =>
          if i ∈ (paramsUOfProduct p).active then
            (paramsUOfProduct p).top - stateUOfProduct p x i
          else
            0) =
      List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            p.n - (x (ProductIndex.unflatten w)).val
          else
            0) := by
  change
    (List.range (Typed.typedWidth p.d)).map
        (fun i =>
          if i ∈ (paramsUOfProduct p).active then
            (paramsUOfProduct p).top - stateUOfProduct p x i
          else
            0) =
      List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            p.n - (x (ProductIndex.unflatten w)).val
          else
            0)
  rw [map_range_eq_ofFn]
  apply congrArg List.ofFn
  funext w
  by_cases hw : ProductIndex.unflatten w ∈ p.active
  · have hwU : w.val ∈ (paramsUOfProduct p).active :=
      (val_mem_paramsUOfProduct_active_iff p w).mpr hw
    simp only [hw, hwU, ↓reduceIte]
    change
      (officialRestrictedParams p).n -
          stateUOfProduct p x w.val =
        p.n - (x (ProductIndex.unflatten w)).val
    rw [stateUOfProduct_apply_width p x w]
    rfl
  · have hwU : w.val ∉ (paramsUOfProduct p).active := by
      intro hwU
      exact hw ((val_mem_paramsUOfProduct_active_iff p w).mp hwU)
    simp [hw, hwU]

/--
The Product ledger effect is exactly the sum of the active-coordinate deficits
from `p.n`, with every structured Product coordinate counted once.
-/
theorem productLedgerEffect_eq_sum_activeDeficits
    (p : ProductRestrictedParams)
    (x : p.State) :
    productLedgerEffect p x =
      ((List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            p.n - (x (ProductIndex.unflatten w)).val
          else
            0)).sum : Int) := by
  calc
    productLedgerEffect p x =
        ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          (stateUOfProduct p x) :=
      (ledgerEffectOn_productWindowU_stateUOfProduct p x).symm

    _ =
        (((productWindowU p).map
          (fun i =>
            if i ∈ (paramsUOfProduct p).active then
              (paramsUOfProduct p).top - stateUOfProduct p x i
            else
              0)).sum : Int) :=
      ledgerEffectOn_eq_sum_activeDeficits
        (paramsUOfProduct p)
        (productWindowU p)
        (stateUOfProduct p x)
        (stateUOfProduct_inStateSpaceU p x)

    _ =
        ((List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              p.n - (x (ProductIndex.unflatten w)).val
            else
              0)).sum : Int) := by
      rw [productWindow_activeDeficits_eq_ofFn p x]

end UnrestrictedBridge
end VFH2
