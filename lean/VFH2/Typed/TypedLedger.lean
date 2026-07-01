import VFH2.Typed.TypedUpdate

/-!
# VF-H2 v10 Typed Ledger Scaffold

This file defines the typed ledger and typed ledger effect for v10.

Boundary:
- This is a typed-formalization scaffold component.
- It does not prove the restricted bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.

Purpose:
The v9 scaffold used list-backed summation over raw Nat coordinates.

In v10, a typed state is a function from typed valid indices to bounded
coordinates. The typed ledger enumerates all valid width indices and sums the
underlying coordinate values.
-/

namespace VFH2
namespace Typed

/-- Values of a typed state over all valid width indices. -/
def typedLedgerValues
    (p : TypedRestrictedParams)
    (x : p.State) : List Nat :=
  List.ofFn (fun i : WidthIndex p.d => (x i).val)

/-- Typed ledger over a typed restricted state.

This is the v10 analogue of the v9 `ledgerVR`, but over typed valid indices
rather than raw list positions.
-/
def typedLedger
    (p : TypedRestrictedParams)
    (x : p.State) : Nat :=
  (typedLedgerValues p x).foldl (fun acc a => acc + a) 0

/-- Typed ledger effect induced by the typed update map. -/
def typedLedgerEffect
    (p : TypedRestrictedParams)
    (x : p.State) : Int :=
  (typedLedger p (typedUpdateState p x) : Int) - (typedLedger p x : Int)

/-- Definitional expansion of typed ledger values. -/
theorem typedLedgerValues_def
    (p : TypedRestrictedParams)
    (x : p.State) :
    typedLedgerValues p x =
      List.ofFn (fun i : WidthIndex p.d => (x i).val) := by
  rfl

/-- Definitional expansion of typed ledger. -/
theorem typedLedger_def
    (p : TypedRestrictedParams)
    (x : p.State) :
    typedLedger p x =
      (typedLedgerValues p x).foldl (fun acc a => acc + a) 0 := by
  rfl

/-- Definitional expansion of typed ledger effect. -/
theorem typedLedgerEffect_def
    (p : TypedRestrictedParams)
    (x : p.State) :
    typedLedgerEffect p x =
      (typedLedger p (typedUpdateState p x) : Int) - (typedLedger p x : Int) := by
  rfl

/-- Typed ledger values are natural numbers, so the ledger is nonnegative. -/
theorem typedLedger_zero_le
    (p : TypedRestrictedParams)
    (x : p.State) :
    0 ≤ typedLedger p x := by
  exact Nat.zero_le (typedLedger p x)

/-- Every coordinate value used by the typed ledger is bounded by top. -/
theorem typedLedger_coordinate_val_le_top
    (p : TypedRestrictedParams)
    (x : p.State)
    (i : WidthIndex p.d) :
    (x i).val ≤ p.n := by
  exact (x i).bound

/-- Every updated coordinate value used by the typed ledger is bounded by top. -/
theorem typedLedger_updated_coordinate_val_le_top
    (p : TypedRestrictedParams)
    (x : p.State)
    (i : WidthIndex p.d) :
    (typedUpdateState p x i).val ≤ p.n := by
  exact (typedUpdateState p x i).bound

end Typed
end VFH2
