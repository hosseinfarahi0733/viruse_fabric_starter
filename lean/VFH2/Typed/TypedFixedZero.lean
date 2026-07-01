import VFH2.Typed.TypedLedger

/-!
# VF-H2 v10 Typed Fixed-Zero Effect

This file proves the fixed-zero ledger-effect half for the v10 typed scaffold.

Boundary:
- This proves the typed fixed-zero effect for the current v10 scaffold.
- It does not prove the full restricted typed bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.

Purpose:
If a typed state is fixed, the typed update preserves every coordinate value.
Therefore the typed ledger is unchanged and the typed ledger effect is zero.
-/

namespace VFH2
namespace Typed

/-- Equal coordinate values at every typed index imply equal typed ledger values. -/
theorem typedLedgerValues_eq_of_pointwise_val_eq
    {p : TypedRestrictedParams}
    {x y : p.State}
    (hpoint : ∀ i : WidthIndex p.d, (y i).val = (x i).val) :
    typedLedgerValues p y = typedLedgerValues p x := by
  unfold typedLedgerValues
  have hfun :
      (fun i : WidthIndex p.d => (y i).val) =
      (fun i : WidthIndex p.d => (x i).val) := by
    funext i
    exact hpoint i
  rw [hfun]

/-- Equal coordinate values at every typed index imply equal typed ledgers. -/
theorem typedLedger_eq_of_pointwise_val_eq
    {p : TypedRestrictedParams}
    {x y : p.State}
    (hpoint : ∀ i : WidthIndex p.d, (y i).val = (x i).val) :
    typedLedger p y = typedLedger p x := by
  unfold typedLedger
  rw [typedLedgerValues_eq_of_pointwise_val_eq hpoint]

/-- If a typed state is fixed, the updated typed state has the same coordinate
values everywhere.
-/
theorem typedUpdateState_pointwise_val_eq_self_of_fixed
    {p : TypedRestrictedParams}
    {x : p.State}
    (hfixed : TypedFixedSet p x) :
    ∀ i : WidthIndex p.d, (typedUpdateState p x i).val = (x i).val := by
  intro i
  exact typedUpdateState_val_eq_self_of_fixed hfixed i

/-- If a typed state is fixed, typed ledger values are preserved by update. -/
theorem typedLedgerValues_eq_update_of_fixed
    {p : TypedRestrictedParams}
    {x : p.State}
    (hfixed : TypedFixedSet p x) :
    typedLedgerValues p (typedUpdateState p x) = typedLedgerValues p x := by
  exact typedLedgerValues_eq_of_pointwise_val_eq
    (typedUpdateState_pointwise_val_eq_self_of_fixed hfixed)

/-- If a typed state is fixed, typed ledger is preserved by update. -/
theorem typedLedger_eq_update_of_fixed
    {p : TypedRestrictedParams}
    {x : p.State}
    (hfixed : TypedFixedSet p x) :
    typedLedger p (typedUpdateState p x) = typedLedger p x := by
  exact typedLedger_eq_of_pointwise_val_eq
    (typedUpdateState_pointwise_val_eq_self_of_fixed hfixed)

/-- If a typed state is fixed, typed ledger effect is zero. -/
theorem typedLedgerEffect_zero_of_fixed
    {p : TypedRestrictedParams}
    {x : p.State}
    (hfixed : TypedFixedSet p x) :
    typedLedgerEffect p x = 0 := by
  have hledger :
      typedLedger p (typedUpdateState p x) = typedLedger p x :=
    typedLedger_eq_update_of_fixed hfixed
  unfold typedLedgerEffect
  rw [hledger]
  simp

/-- Fixed-zero target for the current v10 typed scaffold. -/
def typedFixedZeroEffectTarget
    (p : TypedRestrictedParams)
    (x : p.State) : Prop :=
  TypedFixedSet p x → typedLedgerEffect p x = 0

/-- The current v10 typed scaffold proves the fixed-zero target. -/
theorem typedFixedZeroEffectTarget_proved
    (p : TypedRestrictedParams)
    (x : p.State) :
    typedFixedZeroEffectTarget p x := by
  intro hfixed
  exact typedLedgerEffect_zero_of_fixed hfixed

end Typed
end VFH2
