import VFH2.UnrestrictedBridge.ProductLedgerEffectRangeCharacterization

/-!
# Product finite-observation completeness

This module supplies the first direct reverse semantic transport from an
admissible countably indexed `StateU` observation to the typed Product model.
Every bounded `StateU` has a unique Product representative on the canonical
finite Product window, and that representative preserves the observed ledger
effect exactly.

The result reconstructs only the canonical finite window. It does not
reconstruct or equate the unobserved infinite tail and imposes no condition on
that tail beyond the standing state-space bound. Consequently, it is not a
global surjectivity or equivalence theorem for unrestricted states, does not
define an infinite ledger, and is not unrestricted `TTP-VF-H2-004`. It makes no
full-theory, empirical, physical, or biological validation claim and introduces
no new assumptions.
-/

namespace VFH2
namespace UnrestrictedBridge

open ProductOfficialRestrictedBridgeStateTransport

private theorem stateUOfProduct_apply_width
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

private theorem boundedCoord_eq_of_val_eq
    {n : Nat}
    {a b : Typed.BoundedCoord n}
    (h : a.val = b.val) :
    a = b := by
  cases a with
  | mk av ah =>
      cases b with
      | mk bv bh =>
          simp only at h
          subst bv
          rfl

private theorem foldl_add_apply_eq_of_eq_on
    (window : List Nat)
    (x z : StateU)
    (h : ∀ i : Nat, i ∈ window → x i = z i)
    (acc : Nat) :
    List.foldl (fun a i => a + x i) acc window =
      List.foldl (fun a i => a + z i) acc window := by
  induction window generalizing acc with
  | nil =>
      rfl
  | cons i window ih =>
      simp only [List.foldl_cons]
      rw [h i (by simp)]
      exact
        ih
          (h := fun j hj => h j (by simp [hj]))
          (acc := acc + z i)

private theorem ledgerOn_eq_of_eq_on_window
    (window : List Nat)
    (x z : StateU)
    (h : ∀ i : Nat, i ∈ window → x i = z i) :
    ledgerOn window x = ledgerOn window z := by
  exact foldl_add_apply_eq_of_eq_on window x z h 0

private theorem ledgerEffectOn_eq_of_eq_on_window
    (q : ParamsU)
    (window : List Nat)
    (x z : StateU)
    (h : ∀ i : Nat, i ∈ window → x i = z i) :
    ledgerEffectOn q window x =
      ledgerEffectOn q window z := by
  have hupdate :
      ∀ i : Nat,
        i ∈ window →
          updateU q x i = updateU q z i := by
    intro i hi
    by_cases ha : i ∈ q.active
    · simp [updateU, ha]
    · simp [updateU, ha, h i hi]

  unfold ledgerEffectOn
  rw [
    ledgerOn_eq_of_eq_on_window
      window
      (updateU q x)
      (updateU q z)
      hupdate,
    ledgerOn_eq_of_eq_on_window window x z h
  ]

/--
Every admissible countably indexed state has a unique typed Product
representative on the canonical Product window. The representative preserves
the ledger effect computed from exactly that finite observation.
-/
theorem exists_productState_finiteObservationRepresentative
    (p : ProductRestrictedParams)
    (x : StateU)
    (hx : inStateSpaceU (paramsUOfProduct p) x) :
    ∃ y : p.State,
      (∀ i : Nat,
        i ∈ productWindowU p →
          stateUOfProduct p y i = x i) ∧
      productLedgerEffect p y =
        ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          x ∧
      ∀ z : p.State,
        (∀ i : Nat,
          i ∈ productWindowU p →
            stateUOfProduct p z i = x i) →
        z = y := by
  let y : p.State :=
    fun i =>
      { val := x (ProductIndex.flatten i).val
        bound := by
          have hi := hx (ProductIndex.flatten i).val
          simpa [
            paramsUOfProduct,
            paramsUOfRestricted,
            officialRestrictedParams
          ] using hi }

  have hyWidth :
      ∀ w : Typed.WidthIndex p.d,
        stateUOfProduct p y w.val = x w.val := by
    intro w
    rw [stateUOfProduct_apply_width]
    simp [y, ProductIndex.flatten_unflatten]

  have hyWindow :
      ∀ i : Nat,
        i ∈ productWindowU p →
          stateUOfProduct p y i = x i := by
    intro i hi
    change i ∈ List.range (3 * p.d) at hi
    have hiWidth : i < Typed.typedWidth p.d := by
      simpa [Typed.typedWidth] using List.mem_range.mp hi
    let w : Typed.WidthIndex p.d := ⟨i, hiWidth⟩
    simpa [w] using hyWidth w

  have hyEffect :
      productLedgerEffect p y =
        ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          x := by
    calc
      productLedgerEffect p y =
          ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            (stateUOfProduct p y) :=
        (ledgerEffectOn_productWindowU_stateUOfProduct p y).symm

      _ =
          ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            x :=
        ledgerEffectOn_eq_of_eq_on_window
          (paramsUOfProduct p)
          (productWindowU p)
          (stateUOfProduct p y)
          x
          hyWindow

  have hyUnique :
      ∀ z : p.State,
        (∀ i : Nat,
          i ∈ productWindowU p →
            stateUOfProduct p z i = x i) →
        z = y := by
    intro z hz
    apply funext
    intro i
    apply boundedCoord_eq_of_val_eq

    have hflatMem :
        (ProductIndex.flatten i).val ∈
          productWindowU p := by
      change
        (ProductIndex.flatten i).val ∈
          List.range (3 * p.d)
      exact List.mem_range.mpr (ProductIndex.flatten i).isLt

    have hzObserved :=
      hz (ProductIndex.flatten i).val hflatMem
    have hyObserved :=
      hyWindow (ProductIndex.flatten i).val hflatMem

    rw [
      stateUOfProduct_apply_width
        p
        z
        (ProductIndex.flatten i)
    ] at hzObserved
    rw [
      stateUOfProduct_apply_width
        p
        y
        (ProductIndex.flatten i)
    ] at hyObserved
    simp only [ProductIndex.unflatten_flatten] at hzObserved hyObserved
    exact hzObserved.trans hyObserved.symm

  exact ⟨y, hyWindow, hyEffect, hyUnique⟩

end UnrestrictedBridge
end VFH2
