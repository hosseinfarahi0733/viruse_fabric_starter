import VFH2.RestrictedBridge.ProofBasics

/-!
# VF-H2 Restricted Bridge Update Map Scaffold

This file adds a scaffold-level update map for the restricted bridge
formalization path.

Boundary:
- This is a scaffold-level update map, not the completed Lean proof.
- This is not yet a machine-checked proof of `RBRIDGE-VF-H2-001-R`.
- This is not a proof of the full Viruse Fabric theory.
- This is not a proof of unrestricted `TTP-VF-H2-004`.
- This is not empirical validation.
- This is not biological validation.

The update used here is the simple active-coordinate jump-to-top scaffold:
active coordinates are mapped to `p.n`; inactive coordinates are unchanged.

Future work should generalize this to a dependent representation of
`h_alpha : L_n -> L_n` with strict progress below top.
-/

namespace VFH2
namespace RestrictedBridge

/-- Boolean active-index membership for flattened active coordinates. -/
def isActiveIndex (p : RestrictedParams) (i : Nat) : Bool :=
  decide (i ∈ p.active)

/-- Scaffold-level coordinate update.

If index `i` is active, send the coordinate to top `p.n`.
Otherwise keep the coordinate unchanged.
-/
def updateCoordinateR (p : RestrictedParams) (i a : Nat) : Nat :=
  if isActiveIndex p i then p.n else a

theorem updateCoordinateR_active
    (p : RestrictedParams) (i a : Nat)
    (h : isActiveIndex p i = true) :
    updateCoordinateR p i a = p.n := by
  simp [updateCoordinateR, h]

theorem updateCoordinateR_inactive
    (p : RestrictedParams) (i a : Nat)
    (h : isActiveIndex p i = false) :
    updateCoordinateR p i a = a := by
  simp [updateCoordinateR, h]

/-- Recursive helper for the scaffold-level restricted update map.

The explicit index avoids relying on version-sensitive list enumeration APIs.
-/
def updateStateAuxR (p : RestrictedParams) : Nat → State → State
  | _, [] => []
  | i, a :: xs => updateCoordinateR p i a :: updateStateAuxR p (i + 1) xs

theorem updateStateAuxR_length (p : RestrictedParams) (x : State) (i : Nat) :
    (updateStateAuxR p i x).length = x.length := by
  induction x generalizing i with
  | nil =>
      simp [updateStateAuxR]
  | cons a xs ih =>
      simp [updateStateAuxR, ih]

/-- Scaffold-level restricted update map over flattened states. -/
def updateStateR (p : RestrictedParams) (x : State) : State :=
  updateStateAuxR p 0 x

theorem updateStateR_length (p : RestrictedParams) (x : State) :
    (updateStateR p x).length = x.length := by
  simp [updateStateR, updateStateAuxR_length]

theorem updateStateR_preserves_expected_width
    {p : RestrictedParams} {x : State}
    (h : hasExpectedWidth p x) :
    hasExpectedWidth p (updateStateR p x) := by
  unfold hasExpectedWidth
  rw [updateStateR_length]
  exact h

/-- Ledger effect for the scaffold-level restricted update map. -/
def ledgerEffectR (p : RestrictedParams) (x : State) : Int :=
  Int.ofNat (ledgerVR (updateStateR p x)) - Int.ofNat (ledgerVR x)

theorem ledgerEffectR_def (p : RestrictedParams) (x : State) :
    ledgerEffectR p x =
      Int.ofNat (ledgerVR (updateStateR p x)) - Int.ofNat (ledgerVR x) := by
  rfl

/-- Target proposition for fixed states under the scaffold-level update map.

This is a target, not yet a completed theorem.
-/
def updateFixedZeroEffectTarget
    (p : RestrictedParams)
    (x : State) : Prop :=
  inRestrictedStateSpace p x →
  inFixedSetR p x →
  ledgerEffectR p x = 0

/-- Target proposition for non-fixed states under the scaffold-level update map.

This is a target, not yet a completed theorem.
-/
def updateNonfixedPositiveEffectTarget
    (p : RestrictedParams)
    (x : State) : Prop :=
  inRestrictedStateSpace p x →
  ¬ inFixedSetR p x →
  ledgerEffectR p x > 0

/-- Combined restricted bridge target using the scaffold-level update map.

This remains a target statement, not a completed Lean proof.
-/
def restrictedBridgeUpdateMapTarget
    (p : RestrictedParams)
    (x : State) : Prop :=
  updateNonfixedPositiveEffectTarget p x ∧
  updateFixedZeroEffectTarget p x

theorem restrictedBridgeUpdateMapTarget_nonfixed_part
    {p : RestrictedParams} {x : State}
    (h : restrictedBridgeUpdateMapTarget p x) :
    updateNonfixedPositiveEffectTarget p x := by
  exact h.1

theorem restrictedBridgeUpdateMapTarget_fixed_part
    {p : RestrictedParams} {x : State}
    (h : restrictedBridgeUpdateMapTarget p x) :
    updateFixedZeroEffectTarget p x := by
  exact h.2

end RestrictedBridge
end VFH2
