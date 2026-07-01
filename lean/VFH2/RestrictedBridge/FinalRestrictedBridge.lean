import VFH2.RestrictedBridge.LedgerIncrease

/-!
# VF-H2 Final Restricted Bridge Scaffold Theorem

This file combines the fixed-zero and nonfixed-positive halves for the current
restricted Lean scaffold.

Boundary:
- This proves the final combined theorem for the current restricted
  list-backed Lean scaffold.
- The theorem explicitly assumes:
  - `inRestrictedStateSpace p x`;
  - `activeIndicesInRange p x`.
- This is not a proof of the full Viruse Fabric theory.
- This is not a proof of unrestricted `TTP-VF-H2-004`.
- This is not empirical validation.
- This is not biological validation.
- This does not remove the restricted/toy/scaffold boundary.
-/

namespace VFH2
namespace RestrictedBridge

/-- Combined restricted bridge target for the current Lean scaffold.

Inside the restricted state space, and assuming active indices refer to real
coordinates of the concrete list-backed state:

- fixed-set states have zero scaffold ledger effect;
- nonfixed states have positive scaffold ledger effect.
-/
def restrictedBridgeWithRangeTarget
    (p : RestrictedParams) (x : State) : Prop :=
  inRestrictedStateSpace p x →
  activeIndicesInRange p x →
    (inFixedSetR p x → ledgerEffectR p x = 0) ∧
    (¬ inFixedSetR p x → 0 < ledgerEffectR p x)

/-- Final combined restricted bridge theorem for the current Lean scaffold. -/
theorem restrictedBridgeWithRangeTarget_proved
    (p : RestrictedParams) (x : State) :
    restrictedBridgeWithRangeTarget p x := by
  intro hspace hrange
  constructor
  · intro hfixed
    exact ledgerEffectR_zero_of_inFixedSetR_no_assumption p x hfixed
  · intro hnotfixed
    exact ledgerEffectR_pos_of_not_inFixedSetR hspace hrange hnotfixed

/-- Fixed-set corollary of the final restricted bridge scaffold theorem. -/
theorem finalRestrictedBridge_fixed_zero
    {p : RestrictedParams} {x : State}
    (_hspace : inRestrictedStateSpace p x)
    (_hrange : activeIndicesInRange p x)
    (hfixed : inFixedSetR p x) :
    ledgerEffectR p x = 0 := by
  exact ledgerEffectR_zero_of_inFixedSetR_no_assumption p x hfixed

/-- Nonfixed corollary of the final restricted bridge scaffold theorem. -/
theorem finalRestrictedBridge_nonfixed_positive
    {p : RestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace p x)
    (hrange : activeIndicesInRange p x)
    (hnotfixed : ¬ inFixedSetR p x) :
    0 < ledgerEffectR p x := by
  exact ledgerEffectR_pos_of_not_inFixedSetR hspace hrange hnotfixed

/-- Dichotomy form of the final restricted bridge scaffold theorem. -/
theorem finalRestrictedBridge_dichotomy
    {p : RestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace p x)
    (hrange : activeIndicesInRange p x) :
    (inFixedSetR p x → ledgerEffectR p x = 0) ∧
    (¬ inFixedSetR p x → 0 < ledgerEffectR p x) := by
  exact restrictedBridgeWithRangeTarget_proved p x hspace hrange

end RestrictedBridge
end VFH2
