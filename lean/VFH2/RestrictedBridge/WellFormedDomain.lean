import VFH2.RestrictedBridge.ActiveRangeBridge

/-!
# VF-H2 Restricted Bridge Well-Formed Domain

This file packages the restricted scaffold assumptions into one named
well-formed input domain.

Boundary:
- This is a presentation-strengthening theorem for the current restricted
  Lean scaffold.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted `TTP-VF-H2-004`.
- It is not empirical validation.
- It is not biological validation.
-/

namespace VFH2
namespace RestrictedBridge

/--
Well-formed restricted input domain for the current list-backed Lean scaffold.

It combines:
- membership in the restricted state space;
- parameter-level active-index width well-formedness.
-/
def wellFormedRestrictedInput
    (p : RestrictedParams) (x : State) : Prop :=
  inRestrictedStateSpace p x ∧ activeIndicesWithinWidth p

/-- Well-formed restricted inputs expose restricted state-space membership. -/
theorem wellFormedRestrictedInput_space
    {p : RestrictedParams} {x : State}
    (hwf : wellFormedRestrictedInput p x) :
    inRestrictedStateSpace p x := by
  exact hwf.1

/-- Well-formed restricted inputs expose active-width well-formedness. -/
theorem wellFormedRestrictedInput_activeWidth
    {p : RestrictedParams} {x : State}
    (hwf : wellFormedRestrictedInput p x) :
    activeIndicesWithinWidth p := by
  exact hwf.2

/-- Well-formed restricted inputs imply concrete active-index range. -/
theorem activeIndicesInRange_of_wellFormedRestrictedInput
    {p : RestrictedParams} {x : State}
    (hwf : wellFormedRestrictedInput p x) :
    activeIndicesInRange p x := by
  exact activeIndicesInRange_of_activeIndicesWithinWidth hwf.1 hwf.2

/-- Combined bridge target using the named well-formed restricted input domain. -/
def restrictedBridgeWellFormedTarget
    (p : RestrictedParams) (x : State) : Prop :=
  wellFormedRestrictedInput p x →
    (inFixedSetR p x → ledgerEffectR p x = 0) ∧
    (¬ inFixedSetR p x → 0 < ledgerEffectR p x)

/-- Final restricted bridge theorem over the named well-formed input domain. -/
theorem restrictedBridgeWellFormedTarget_proved
    (p : RestrictedParams) (x : State) :
    restrictedBridgeWellFormedTarget p x := by
  intro hwf
  exact restrictedBridgeWithActiveWidthTarget_proved p x hwf.1 hwf.2

/-- Fixed-set corollary over the named well-formed input domain. -/
theorem finalRestrictedBridge_wellFormed_fixed_zero
    {p : RestrictedParams} {x : State}
    (hwf : wellFormedRestrictedInput p x)
    (hfixed : inFixedSetR p x) :
    ledgerEffectR p x = 0 := by
  exact (restrictedBridgeWellFormedTarget_proved p x hwf).1 hfixed

/-- Nonfixed corollary over the named well-formed input domain. -/
theorem finalRestrictedBridge_wellFormed_nonfixed_positive
    {p : RestrictedParams} {x : State}
    (hwf : wellFormedRestrictedInput p x)
    (hnotfixed : ¬ inFixedSetR p x) :
    0 < ledgerEffectR p x := by
  exact (restrictedBridgeWellFormedTarget_proved p x hwf).2 hnotfixed

/-- Dichotomy form over the named well-formed input domain. -/
theorem finalRestrictedBridge_wellFormed_dichotomy
    {p : RestrictedParams} {x : State}
    (hwf : wellFormedRestrictedInput p x) :
    (inFixedSetR p x → ledgerEffectR p x = 0) ∧
    (¬ inFixedSetR p x → 0 < ledgerEffectR p x) := by
  exact restrictedBridgeWellFormedTarget_proved p x hwf

end RestrictedBridge
end VFH2
