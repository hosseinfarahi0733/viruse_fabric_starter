import VFH2.RestrictedBridge.ActiveTopBridge

/-!
# VF-H2 Restricted Bridge Membership-Top Fixed Update Bridge

This file adds proof-bearing Lean lemmas connecting a membership-based
active-top predicate to the existing pointwise fixed-update path.

Boundary:
- This proves a scaffold bridge from membership-top conditions to zero ledger effect.
- This is not yet the full machine-checked proof of `RBRIDGE-VF-H2-001-R`.
- This is not a proof of the full Viruse Fabric theory.
- This is not a proof of unrestricted `TTP-VF-H2-004`.
- This is not empirical validation.
- This is not biological validation.

Next bridge still needed:
connect the original `inFixedSetR p x` predicate, which is based on `getD`,
to `membershipTopForUpdate p 0 x`.
-/

namespace VFH2
namespace RestrictedBridge

/-- Soundness bridge for the Boolean active-index test.

This is kept as an explicit assumption for now to avoid hiding the list
membership bridge inside automation.
-/
def activeIndexSound (p : RestrictedParams) : Prop :=
  ∀ i : Nat, isActiveIndex p i = true → i ∈ p.active

/-- Operational membership-top predicate along the update traversal.

At each visited index `i`, if `i` is in the active list, the current coordinate
is already at top `p.n`.
-/
def membershipTopForUpdate (p : RestrictedParams) : Nat → State → Prop
  | _, [] => True
  | i, a :: xs =>
      (i ∈ p.active → a = p.n) ∧
      membershipTopForUpdate p (i + 1) xs

theorem membershipTopForUpdate_nil (p : RestrictedParams) (i : Nat) :
    membershipTopForUpdate p i ([] : State) := by
  simp [membershipTopForUpdate]

theorem membershipTopForUpdate_cons_head
    {p : RestrictedParams} {i a : Nat} {xs : State}
    (h : membershipTopForUpdate p i (a :: xs)) :
    i ∈ p.active → a = p.n := by
  exact h.1

theorem membershipTopForUpdate_cons_tail
    {p : RestrictedParams} {i a : Nat} {xs : State}
    (h : membershipTopForUpdate p i (a :: xs)) :
    membershipTopForUpdate p (i + 1) xs := by
  exact h.2

/-- Membership-top plus active-index soundness gives active-top. -/
theorem activeTopForUpdate_of_membershipTopForUpdate
    (p : RestrictedParams) (x : State) (i : Nat)
    (hsound : activeIndexSound p)
    (h : membershipTopForUpdate p i x) :
    activeTopForUpdate p i x := by
  induction x generalizing i with
  | nil =>
      simp [activeTopForUpdate]
  | cons a xs ih =>
      have hheadMem : i ∈ p.active → a = p.n := h.1
      have htail : membershipTopForUpdate p (i + 1) xs := h.2
      exact And.intro
        (fun hidx => hheadMem (hsound i hidx))
        (ih (i + 1) htail)

/-- Membership-top plus active-index soundness gives pointwise fixed update. -/
theorem pointwiseFixedForUpdate_of_membershipTopForUpdate
    (p : RestrictedParams) (x : State) (i : Nat)
    (hsound : activeIndexSound p)
    (h : membershipTopForUpdate p i x) :
    pointwiseFixedForUpdate p i x := by
  exact pointwiseFixedForUpdate_of_activeTopForUpdate
    p x i
    (activeTopForUpdate_of_membershipTopForUpdate p x i hsound h)

/-- Membership-top states are unchanged by the scaffold update. -/
theorem updateStateR_eq_self_of_membershipTopForUpdate
    (p : RestrictedParams) (x : State)
    (hsound : activeIndexSound p)
    (h : membershipTopForUpdate p 0 x) :
    updateStateR p x = x := by
  exact updateStateR_eq_self_of_pointwiseFixed
    p x
    (pointwiseFixedForUpdate_of_membershipTopForUpdate p x 0 hsound h)

/-- Membership-top states have zero scaffold ledger effect. -/
theorem ledgerEffectR_zero_of_membershipTopForUpdate
    (p : RestrictedParams) (x : State)
    (hsound : activeIndexSound p)
    (h : membershipTopForUpdate p 0 x) :
    ledgerEffectR p x = 0 := by
  exact ledgerEffectR_zero_of_updateStateR_eq_self
    p x
    (updateStateR_eq_self_of_membershipTopForUpdate p x hsound h)

/-- Membership-top states satisfy the fixed-zero-effect target.

This is a proof-bearing bridge toward:

`x ∈ F_R => ledger_effect_size_R(x)=0`

The remaining future bridge is:

`inFixedSetR p x => membershipTopForUpdate p 0 x`

under suitable index/getD assumptions.
-/
theorem updateFixedZeroEffectTarget_of_membershipTopForUpdate
    (p : RestrictedParams) (x : State)
    (hsound : activeIndexSound p)
    (h : membershipTopForUpdate p 0 x) :
    updateFixedZeroEffectTarget p x := by
  intro _hspace _hfixed
  exact ledgerEffectR_zero_of_membershipTopForUpdate p x hsound h

end RestrictedBridge
end VFH2
