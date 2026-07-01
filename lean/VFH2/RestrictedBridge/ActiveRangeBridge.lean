import VFH2.RestrictedBridge.FinalRestrictedBridge

/-!
# VF-H2 Restricted Bridge Active Range Bridge

This file replaces the state-specific `activeIndicesInRange p x` assumption
with a cleaner parameter-level active-width condition.

Boundary:
- This strengthens the presentation of the current restricted Lean scaffold.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted `TTP-VF-H2-004`.
- It is not empirical validation.
- It is not biological validation.
-/

namespace VFH2
namespace RestrictedBridge

/-- Parameter-level active index well-formedness.

Every active index must be below the expected restricted width.
-/
def activeIndicesWithinWidth (p : RestrictedParams) : Prop :=
  ∀ i : Nat, i ∈ p.active → i < expectedWidth p

/-- If a state has the expected restricted width, then any active index below
that width is in range for the concrete list-backed state.
-/
theorem activeIndicesInRange_of_activeIndicesWithinWidth
    {p : RestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace p x)
    (hactiveWidth : activeIndicesWithinWidth p) :
    activeIndicesInRange p x := by
  intro i hi
  have hwidth : x.length = expectedWidth p := by
    exact hspace.1
  have hiwidth : i < expectedWidth p := hactiveWidth i hi
  simpa [hwidth] using hiwidth

/-- Combined restricted bridge target using parameter-level active-width
well-formedness instead of a state-specific range assumption.
-/
def restrictedBridgeWithActiveWidthTarget
    (p : RestrictedParams) (x : State) : Prop :=
  inRestrictedStateSpace p x →
  activeIndicesWithinWidth p →
    (inFixedSetR p x → ledgerEffectR p x = 0) ∧
    (¬ inFixedSetR p x → 0 < ledgerEffectR p x)

/-- Restricted bridge theorem with parameter-level active-width assumption. -/
theorem restrictedBridgeWithActiveWidthTarget_proved
    (p : RestrictedParams) (x : State) :
    restrictedBridgeWithActiveWidthTarget p x := by
  intro hspace hactiveWidth
  have hrange : activeIndicesInRange p x :=
    activeIndicesInRange_of_activeIndicesWithinWidth hspace hactiveWidth
  exact finalRestrictedBridge_dichotomy hspace hrange

/-- Fixed-set corollary under parameter-level active-width well-formedness. -/
theorem finalRestrictedBridge_activeWidth_fixed_zero
    {p : RestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace p x)
    (hactiveWidth : activeIndicesWithinWidth p)
    (hfixed : inFixedSetR p x) :
    ledgerEffectR p x = 0 := by
  exact (restrictedBridgeWithActiveWidthTarget_proved p x hspace hactiveWidth).1 hfixed

/-- Nonfixed corollary under parameter-level active-width well-formedness. -/
theorem finalRestrictedBridge_activeWidth_nonfixed_positive
    {p : RestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace p x)
    (hactiveWidth : activeIndicesWithinWidth p)
    (hnotfixed : ¬ inFixedSetR p x) :
    0 < ledgerEffectR p x := by
  exact (restrictedBridgeWithActiveWidthTarget_proved p x hspace hactiveWidth).2 hnotfixed

end RestrictedBridge
end VFH2
