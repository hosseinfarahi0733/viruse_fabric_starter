import VFH2.UnrestrictedBridge.ProductFiniteObservationCompleteness

/-!
# Product finite-observation level-set characterization

This module transports the exact Product ledger-effect fiber classification to
admissible countably indexed states observed through the canonical Product
window. Two such observations have equal ledger effects exactly when their
canonical membership-masked totals of active-coordinate values are equal.

The theorem concerns only the existing finite observation window. It neither
reconstructs nor equates the infinite tails, and it imposes no tail condition
beyond the standing state-space bound. It does not define a global infinite
ledger, is not unrestricted `TTP-VF-H2-004`, and makes no full-theory,
empirical, physical, or biological validation claim. No new model assumption
is introduced.
-/

namespace VFH2
namespace UnrestrictedBridge

open ProductOfficialRestrictedBridgeStateTransport

private theorem stateUOfProduct_apply_width_for_levelSet
    (p : ProductRestrictedParams)
    (y : p.State)
    (w : Typed.WidthIndex p.d) :
    stateUOfProduct p y w.val =
      (y (ProductIndex.unflatten w)).val := by
  change
    (officialRestrictedState p y).getD w.val 0 =
      (y (ProductIndex.unflatten w)).val
  simpa only [ProductIndex.flatten_unflatten] using
    officialRestrictedState_getD_flatten
      p
      y
      (ProductIndex.unflatten w)

private theorem representative_value_eq
    (p : ProductRestrictedParams)
    (x : StateU)
    (y : p.State)
    (hy :
      ∀ i : Nat,
        i ∈ productWindowU p →
          stateUOfProduct p y i = x i)
    (w : Typed.WidthIndex p.d) :
    (y (ProductIndex.unflatten w)).val = x w.val := by
  have hwMem :
      w.val ∈ productWindowU p := by
    change w.val ∈ List.range (3 * p.d)
    exact
      List.mem_range.mpr
        (by
          change w.val < Typed.typedWidth p.d
          exact w.isLt)
  have hObserved := hy w.val hwMem
  rw [stateUOfProduct_apply_width_for_levelSet p y w] at hObserved
  exact hObserved

private theorem representative_sum_activeValues_eq
    (p : ProductRestrictedParams)
    (x : StateU)
    (y : p.State)
    (hy :
      ∀ i : Nat,
        i ∈ productWindowU p →
          stateUOfProduct p y i = x i) :
    (List.ofFn
      (fun w : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten w ∈ p.active then
          (y (ProductIndex.unflatten w)).val
        else
          0)).sum =
      (List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            x w.val
          else
            0)).sum := by
  apply congrArg List.sum
  apply congrArg List.ofFn
  funext w
  by_cases hw : ProductIndex.unflatten w ∈ p.active
  · simp only [hw, ↓reduceIte]
    exact representative_value_eq p x y hy w
  · simp [hw]

/--
For fixed Product-derived parameters, two admissible countably indexed states
have equal finite-observation ledger effects exactly when their canonical
totals of active-coordinate values agree.
-/
theorem ledgerEffectOn_productWindowU_eq_iff_sum_activeValues_eq
    (p : ProductRestrictedParams)
    (x z : StateU)
    (hx : inStateSpaceU (paramsUOfProduct p) x)
    (hz : inStateSpaceU (paramsUOfProduct p) z) :
    ledgerEffectOn
        (paramsUOfProduct p)
        (productWindowU p)
        x =
      ledgerEffectOn
        (paramsUOfProduct p)
        (productWindowU p)
        z
      ↔
    (List.ofFn
      (fun w : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten w ∈ p.active then
          x w.val
        else
          0)).sum =
      (List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            z w.val
          else
            0)).sum := by
  obtain ⟨y, hyWindow, hyEffect, _⟩ :=
    exists_productState_finiteObservationRepresentative p x hx
  obtain ⟨v, hvWindow, hvEffect, _⟩ :=
    exists_productState_finiteObservationRepresentative p z hz

  rw [
    ← hyEffect,
    ← hvEffect,
    productLedgerEffect_eq_productLedgerEffect_iff_sum_activeValues_eq,
    representative_sum_activeValues_eq p x y hyWindow,
    representative_sum_activeValues_eq p z v hvWindow
  ]

end UnrestrictedBridge
end VFH2
