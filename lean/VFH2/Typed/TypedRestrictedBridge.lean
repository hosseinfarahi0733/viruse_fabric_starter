import VFH2.Typed.TypedPositiveLedger

/-!
# VF-H2 v10 Typed Restricted Bridge Theorem

This file combines the fixed-zero and nonfixed-positive halves of the current
v10 typed scaffold.

Boundary:
- This proves the typed restricted bridge theorem for the current v10 typed
  scaffold.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.

Result:
For typed restricted parameters and typed states:
1. fixed states have zero typed ledger effect;
2. nonfixed states have positive typed ledger effect.

The v10 typed formulation internalizes the active-index width guard through
`WidthIndex d` and coordinate bounds through `BoundedCoord n`.
-/

namespace VFH2
namespace Typed

/-- Typed restricted bridge target for the current v10 scaffold. -/
def typedRestrictedBridgeTarget
    (p : TypedRestrictedParams)
    (x : p.State) : Prop :=
  (TypedFixedSet p x → typedLedgerEffect p x = 0)
  ∧
  (¬ TypedFixedSet p x → 0 < typedLedgerEffect p x)

/-- The current v10 typed scaffold proves the typed restricted bridge target. -/
theorem typedRestrictedBridgeTarget_proved
    (p : TypedRestrictedParams)
    (x : p.State) :
    typedRestrictedBridgeTarget p x := by
  constructor
  · intro hfixed
    exact typedLedgerEffect_zero_of_fixed hfixed
  · intro hnotfixed
    exact typedLedgerEffect_pos_of_not_fixed hnotfixed

/-- Fixed-state half of the typed restricted bridge theorem. -/
theorem typedRestrictedBridge_fixed_zero
    {p : TypedRestrictedParams}
    {x : p.State}
    (hfixed : TypedFixedSet p x) :
    typedLedgerEffect p x = 0 := by
  exact typedLedgerEffect_zero_of_fixed hfixed

/-- Nonfixed-state half of the typed restricted bridge theorem. -/
theorem typedRestrictedBridge_nonfixed_positive
    {p : TypedRestrictedParams}
    {x : p.State}
    (hnotfixed : ¬ TypedFixedSet p x) :
    0 < typedLedgerEffect p x := by
  exact typedLedgerEffect_pos_of_not_fixed hnotfixed

/-- Dichotomy form of the typed restricted bridge theorem. -/
theorem typedRestrictedBridge_dichotomy
    (p : TypedRestrictedParams)
    (x : p.State) :
    (TypedFixedSet p x ∧ typedLedgerEffect p x = 0)
    ∨
    (¬ TypedFixedSet p x ∧ 0 < typedLedgerEffect p x) := by
  classical
  by_cases hfixed : TypedFixedSet p x
  · exact Or.inl ⟨hfixed, typedRestrictedBridge_fixed_zero hfixed⟩
  · exact Or.inr ⟨hfixed, typedRestrictedBridge_nonfixed_positive hfixed⟩

end Typed
end VFH2
