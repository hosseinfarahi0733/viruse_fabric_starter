import VFH2.Product.ProductOfficialRestrictedBridgeStateTransport
import VFH2.Product.ProductUpdateTransport
import VFH2.Product.ProductLedgerTypedValuesDecomposition
import VFH2.RestrictedBridge.OfficialRBridge

/-!
# Product/Official Restricted-Bridge Dynamics Transport

This module connects the current typed Product restricted formalization to the
official list-backed `RestrictedBridge` restricted formalization at the level
of update, ledger, effect, and the official restricted theorem.

This is not unrestricted TTP-VF-H2-004. It is not full-theory, empirical, or
biological validation. No new dynamics or assumptions are introduced here.
-/

namespace VFH2
namespace ProductOfficialRestrictedBridgeDynamicsTransport

open ProductOfficialRestrictedBridgeStateTransport

private theorem officialRestrictedParams_active_val_iff_typed_active
    (p : ProductRestrictedParams)
    (w : Typed.WidthIndex p.d) :
    w.val ∈ (officialRestrictedParams p).active ↔
      w ∈ (ProductParamsTransport.typedParamsOfProduct p).active := by
  unfold officialRestrictedParams
  constructor
  · intro h
    rcases List.mem_map.mp h with ⟨v, hv, hval⟩
    have hvw : v = w := Fin.ext hval
    subst v
    exact hv
  · intro h
    exact List.mem_map.mpr ⟨w, h, rfl⟩

private theorem officialRestricted_updateCoordinate_eq_typedUpdate_val
    (p : ProductRestrictedParams)
    (x : p.State)
    (w : Typed.WidthIndex p.d) :
    RestrictedBridge.updateCoordinateR
        (officialRestrictedParams p)
        w.val
        (ProductStateTransport.productToTyped x w).val
      =
    (Typed.typedUpdateState
      (ProductParamsTransport.typedParamsOfProduct p)
      (ProductStateTransport.productToTyped x)
      w).val := by
  by_cases hw :
      w ∈ (ProductParamsTransport.typedParamsOfProduct p).active
  · have hrawMem :
        w.val ∈ (officialRestrictedParams p).active :=
      (officialRestrictedParams_active_val_iff_typed_active p w).mpr hw
    have hraw :
        RestrictedBridge.isActiveIndex
          (officialRestrictedParams p) w.val = true := by
      simp [RestrictedBridge.isActiveIndex, hrawMem]
    rw [RestrictedBridge.updateCoordinateR_active _ _ _ hraw]
    exact
      (Typed.typedUpdateState_active_val
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x)
        hw).symm
  · have hrawNotMem :
        w.val ∉ (officialRestrictedParams p).active := by
      intro hrawMem
      exact hw
        ((officialRestrictedParams_active_val_iff_typed_active p w).mp
          hrawMem)
    have hraw :
        RestrictedBridge.isActiveIndex
          (officialRestrictedParams p) w.val = false := by
      simp [RestrictedBridge.isActiveIndex, hrawNotMem]
    rw [RestrictedBridge.updateCoordinateR_inactive _ _ _ hraw]
    exact
      (Typed.typedUpdateState_inactive_val
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x)
        hw).symm

private theorem officialRestricted_updateCoordinate_eq_productUpdate_val
    (p : ProductRestrictedParams)
    (x : p.State)
    (w : Typed.WidthIndex p.d) :
    RestrictedBridge.updateCoordinateR
        (officialRestrictedParams p)
        w.val
        (ProductStateTransport.productToTyped x w).val
      =
    (ProductStateTransport.productToTyped
      (productUpdateState p x) w).val := by
  calc
    RestrictedBridge.updateCoordinateR
        (officialRestrictedParams p)
        w.val
        (ProductStateTransport.productToTyped x w).val =
      (Typed.typedUpdateState
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x)
        w).val :=
      officialRestricted_updateCoordinate_eq_typedUpdate_val p x w
    _ =
      (ProductStateTransport.productToTyped
        (productUpdateState p x) w).val := by
      rw [
        ProductUpdateTransport.typedUpdateState_eq_productToTyped_productUpdateState
      ]

private theorem updateStateAuxR_getElem?
    (q : RestrictedBridge.RestrictedParams)
    (xs : RestrictedBridge.State)
    (base k : Nat) :
    (RestrictedBridge.updateStateAuxR q base xs)[k]? =
      xs[k]?.map
        (RestrictedBridge.updateCoordinateR q (base + k)) := by
  induction xs generalizing base k with
  | nil =>
      simp [RestrictedBridge.updateStateAuxR]
  | cons a xs ih =>
      cases k with
      | zero =>
          simp [RestrictedBridge.updateStateAuxR]
      | succ k =>
          simpa [
            RestrictedBridge.updateStateAuxR,
            Nat.succ_eq_add_one,
            Nat.add_assoc,
            Nat.add_comm,
            Nat.add_left_comm
          ] using ih (base := base + 1) (k := k)

private theorem updateStateR_getElem?
    (q : RestrictedBridge.RestrictedParams)
    (xs : RestrictedBridge.State)
    (k : Nat) :
    (RestrictedBridge.updateStateR q xs)[k]? =
      xs[k]?.map (RestrictedBridge.updateCoordinateR q k) := by
  simpa [RestrictedBridge.updateStateR] using
    updateStateAuxR_getElem? q xs 0 k

/-- Canonical serialization commutes with the restricted state update. -/
theorem officialRestrictedState_productUpdateState_eq_updateStateR
    (p : ProductRestrictedParams)
    (x : p.State) :
    officialRestrictedState p (productUpdateState p x) =
      RestrictedBridge.updateStateR
        (officialRestrictedParams p)
        (officialRestrictedState p x) := by
  apply List.ext_getElem?
  intro k
  rw [updateStateR_getElem?]
  unfold officialRestrictedState
  simp only [List.getElem?_ofFn]
  by_cases hk : k < Typed.typedWidth p.d
  · simp only [dif_pos hk, Option.map_some, Option.some.injEq]
    exact
      (officialRestricted_updateCoordinate_eq_productUpdate_val
        p x ⟨k, hk⟩).symm
  · simp [hk]

/-- The official list-backed ledger agrees with the Product ledger. -/
theorem officialRestrictedBridge_ledgerVR_eq_productLedger
    (p : ProductRestrictedParams)
    (x : p.State) :
    RestrictedBridge.ledgerVR (officialRestrictedState p x) =
      productLedger p x := by
  have hvalues :
      officialRestrictedState p x = productLedgerValues p x := by
    calc
      officialRestrictedState p x =
          ProductLedgerEquivalenceTarget.transportedTypedLedgerValues p x := by
        rfl
      _ =
          ProductLedgerTypedBlocks.transportedTypedLedgerBlockValues p x :=
        ProductLedgerTypedValuesDecomposition.transportedTypedLedgerValues_eq_blockValues
          p x
      _ = productLedgerValues p x :=
        ProductLedgerTypedBlocks.transportedTypedLedgerBlockValues_eq_productLedgerValues
          p x
  unfold RestrictedBridge.ledgerVR productLedger
  rw [hvalues]

/-- The official list-backed ledger effect agrees with the Product effect. -/
theorem officialRestrictedBridge_ledgerEffectR_eq_productLedgerEffect
    (p : ProductRestrictedParams)
    (x : p.State) :
    RestrictedBridge.ledgerEffectR
        (officialRestrictedParams p)
        (officialRestrictedState p x)
      =
    productLedgerEffect p x := by
  unfold RestrictedBridge.ledgerEffectR productLedgerEffect
  rw [← officialRestrictedState_productUpdateState_eq_updateStateR]
  rw [officialRestrictedBridge_ledgerVR_eq_productLedger]
  rw [officialRestrictedBridge_ledgerVR_eq_productLedger]
  rfl

/--
The Product fixed set is characterized by zero effect in the official
list-backed restricted model, using the official restricted theorem.
-/
theorem productFixedSet_iff_officialRestrictedBridge_ledgerEffect_eq_zero
    (p : ProductRestrictedParams)
    (x : p.State) :
    ProductFixedSet p x ↔
      RestrictedBridge.ledgerEffectR
        (officialRestrictedParams p)
        (officialRestrictedState p x) = 0 := by
  have hofficial :
      (RestrictedBridge.inFixedSetR
          (officialRestrictedParams p)
          (officialRestrictedState p x) →
        RestrictedBridge.ledgerEffectR
          (officialRestrictedParams p)
          (officialRestrictedState p x) = 0) ∧
      (¬ RestrictedBridge.inFixedSetR
          (officialRestrictedParams p)
          (officialRestrictedState p x) →
        0 <
          RestrictedBridge.ledgerEffectR
            (officialRestrictedParams p)
            (officialRestrictedState p x)) :=
    RestrictedBridge.RBRIDGE_VF_H2_001_R_Lean_scaffold
      (officialRestrictedParams p)
      (officialRestrictedState p x)
      (officialRestrictedInput_wellFormed p x)
  constructor
  · intro hfixed
    exact
      hofficial.1
        ((productFixedSet_iff_officialRestrictedBridge_inFixedSetR
          p x).mp hfixed)
  · intro hzero
    by_cases hfixed : ProductFixedSet p x
    · exact hfixed
    · have hnotOfficial :
          ¬ RestrictedBridge.inFixedSetR
            (officialRestrictedParams p)
            (officialRestrictedState p x) := by
        intro hoffixed
        exact hfixed
          ((productFixedSet_iff_officialRestrictedBridge_inFixedSetR
            p x).mpr hoffixed)
      have hpositive := hofficial.2 hnotOfficial
      rw [hzero] at hpositive
      exact False.elim ((Int.lt_irrefl 0) hpositive)

end ProductOfficialRestrictedBridgeDynamicsTransport
end VFH2
