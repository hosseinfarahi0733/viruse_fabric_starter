import VFH2.RestrictedBridge.FixedZeroEffect

/-!
# VF-H2 Restricted Bridge Active-Top Fixed Update Bridge

This file adds proof-bearing Lean lemmas connecting an operational
active-top predicate to the pointwise fixed-update predicate.

Boundary:
- This proves a scaffold-level active-top bridge.
- This is not yet the full machine-checked proof of `RBRIDGE-VF-H2-001-R`.
- This is not a proof of the full Viruse Fabric theory.
- This is not a proof of unrestricted `TTP-VF-H2-004`.
- This is not empirical validation.
- This is not biological validation.

Next bridge still needed:
connect the original `inFixedSetR p x` predicate to
`activeTopForUpdate p 0 x` under suitable index/well-formedness assumptions.
-/

namespace VFH2
namespace RestrictedBridge

/-- Operational predicate: along the update traversal, every active coordinate
is already at top `p.n`.

Inactive coordinates impose no condition.
-/
def activeTopForUpdate (p : RestrictedParams) : Nat → State → Prop
  | _, [] => True
  | i, a :: xs =>
      (isActiveIndex p i = true → a = p.n) ∧
      activeTopForUpdate p (i + 1) xs

theorem activeTopForUpdate_nil (p : RestrictedParams) (i : Nat) :
    activeTopForUpdate p i ([] : State) := by
  simp [activeTopForUpdate]

theorem activeTopForUpdate_cons_head
    {p : RestrictedParams} {i a : Nat} {xs : State}
    (h : activeTopForUpdate p i (a :: xs)) :
    isActiveIndex p i = true → a = p.n := by
  exact h.1

theorem activeTopForUpdate_cons_tail
    {p : RestrictedParams} {i a : Nat} {xs : State}
    (h : activeTopForUpdate p i (a :: xs)) :
    activeTopForUpdate p (i + 1) xs := by
  exact h.2

/-- If an active coordinate is already top, and inactive coordinates are
unconstrained, the coordinate update leaves the value unchanged.
-/
theorem updateCoordinateR_eq_self_of_activeTopStep
    (p : RestrictedParams) (i a : Nat)
    (h : isActiveIndex p i = true → a = p.n) :
    updateCoordinateR p i a = a := by
  unfold updateCoordinateR
  cases hidx : isActiveIndex p i with
  | false =>
      simp
  | true =>
      have ha : a = p.n := h hidx
      simp [ha]

/-- Active-top along the update traversal implies pointwise fixed update. -/
theorem pointwiseFixedForUpdate_of_activeTopForUpdate
    (p : RestrictedParams) (x : State) (i : Nat)
    (h : activeTopForUpdate p i x) :
    pointwiseFixedForUpdate p i x := by
  induction x generalizing i with
  | nil =>
      simp [pointwiseFixedForUpdate]
  | cons a xs ih =>
      have hhead : isActiveIndex p i = true → a = p.n := h.1
      have htail : activeTopForUpdate p (i + 1) xs := h.2
      exact And.intro
        (updateCoordinateR_eq_self_of_activeTopStep p i a hhead)
        (ih (i + 1) htail)

/-- Active-top states are unchanged by the scaffold update. -/
theorem updateStateR_eq_self_of_activeTopForUpdate
    (p : RestrictedParams) (x : State)
    (h : activeTopForUpdate p 0 x) :
    updateStateR p x = x := by
  exact updateStateR_eq_self_of_pointwiseFixed
    p x
    (pointwiseFixedForUpdate_of_activeTopForUpdate p x 0 h)

/-- Active-top states have zero scaffold ledger effect. -/
theorem ledgerEffectR_zero_of_activeTopForUpdate
    (p : RestrictedParams) (x : State)
    (h : activeTopForUpdate p 0 x) :
    ledgerEffectR p x = 0 := by
  exact ledgerEffectR_zero_of_updateStateR_eq_self
    p x
    (updateStateR_eq_self_of_activeTopForUpdate p x h)

/-- Active-top states satisfy the fixed-zero-effect target.

This is a proof-bearing bridge toward:

`x ∈ F_R => ledger_effect_size_R(x)=0`

The remaining future bridge is:

`inFixedSetR p x => activeTopForUpdate p 0 x`

under suitable active-index assumptions.
-/
theorem updateFixedZeroEffectTarget_of_activeTopForUpdate
    (p : RestrictedParams) (x : State)
    (h : activeTopForUpdate p 0 x) :
    updateFixedZeroEffectTarget p x := by
  intro _hspace _hfixed
  exact ledgerEffectR_zero_of_activeTopForUpdate p x h

end RestrictedBridge
end VFH2
