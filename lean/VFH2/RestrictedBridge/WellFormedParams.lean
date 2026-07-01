import VFH2.RestrictedBridge.ActiveWidthNecessity

/-!
# VF-H2 Restricted Bridge Well-Formed Parameters

This file strengthens the current restricted Lean scaffold by packaging the
active-width condition inside a parameter wrapper.

Boundary:
- This is a model-strengthening step for the restricted Lean scaffold.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted `TTP-VF-H2-004`.
- It is not empirical validation.
- It is not biological validation.

Motivation:
The lightweight `RestrictedParams` record cannot guarantee
`activeIndicesWithinWidth p` by itself. The counterexample in
`ActiveWidthNecessity.lean` proves that this well-formedness condition is
not derivable for all raw `RestrictedParams`.

This wrapper records the missing invariant explicitly.
-/

namespace VFH2
namespace RestrictedBridge

/-- Well-formed restricted parameters.

This wraps the lightweight scaffold parameters with the missing active-width
well-formedness invariant.
-/
structure WellFormedRestrictedParams where
  params : RestrictedParams
  activeWithinWidth : activeIndicesWithinWidth params

/-- The underlying lightweight parameters of a well-formed parameter record. -/
def WellFormedRestrictedParams.toParams
    (wp : WellFormedRestrictedParams) : RestrictedParams :=
  wp.params

/-- Well-formed parameters expose active-width well-formedness. -/
theorem activeIndicesWithinWidth_of_WellFormedRestrictedParams
    (wp : WellFormedRestrictedParams) :
    activeIndicesWithinWidth wp.params := by
  exact wp.activeWithinWidth

/-- For well-formed parameters, restricted state-space membership is enough
to build the named well-formed restricted input domain.
-/
theorem wellFormedRestrictedInput_of_WellFormedRestrictedParams
    {wp : WellFormedRestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace wp.params x) :
    wellFormedRestrictedInput wp.params x := by
  exact ⟨hspace, wp.activeWithinWidth⟩

/-- For well-formed parameters, restricted state-space membership implies
concrete active-index range.
-/
theorem activeIndicesInRange_of_WellFormedRestrictedParams
    {wp : WellFormedRestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace wp.params x) :
    activeIndicesInRange wp.params x := by
  exact activeIndicesInRange_of_activeIndicesWithinWidth
    hspace
    wp.activeWithinWidth

/-- Restricted bridge target over well-formed parameters.

Since active-width is packaged inside `WellFormedRestrictedParams`, the input
state only needs to satisfy the restricted state-space predicate.
-/
def restrictedBridgeWellFormedParamsTarget
    (wp : WellFormedRestrictedParams) (x : State) : Prop :=
  inRestrictedStateSpace wp.params x →
    (inFixedSetR wp.params x → ledgerEffectR wp.params x = 0) ∧
    (¬ inFixedSetR wp.params x → 0 < ledgerEffectR wp.params x)

/-- Restricted bridge theorem over well-formed parameters. -/
theorem restrictedBridgeWellFormedParamsTarget_proved
    (wp : WellFormedRestrictedParams) (x : State) :
    restrictedBridgeWellFormedParamsTarget wp x := by
  intro hspace
  have hwf : wellFormedRestrictedInput wp.params x :=
    wellFormedRestrictedInput_of_WellFormedRestrictedParams hspace
  exact restrictedBridgeWellFormedTarget_proved wp.params x hwf

/-- Official scaffold theorem specialized to well-formed parameters. -/
theorem RBRIDGE_VF_H2_001_R_Lean_scaffold_wellFormedParams
    (wp : WellFormedRestrictedParams) (x : State) :
    restrictedBridgeWellFormedParamsTarget wp x := by
  exact restrictedBridgeWellFormedParamsTarget_proved wp x

/-- Fixed-set zero-effect corollary over well-formed parameters. -/
theorem RBRIDGE_VF_H2_001_R_Lean_scaffold_wellFormedParams_fixed_zero
    {wp : WellFormedRestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace wp.params x)
    (hfixed : inFixedSetR wp.params x) :
    ledgerEffectR wp.params x = 0 := by
  exact
    (restrictedBridgeWellFormedParamsTarget_proved wp x hspace).1 hfixed

/-- Nonfixed positive-effect corollary over well-formed parameters. -/
theorem RBRIDGE_VF_H2_001_R_Lean_scaffold_wellFormedParams_nonfixed_positive
    {wp : WellFormedRestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace wp.params x)
    (hnotfixed : ¬ inFixedSetR wp.params x) :
    0 < ledgerEffectR wp.params x := by
  exact
    (restrictedBridgeWellFormedParamsTarget_proved wp x hspace).2 hnotfixed

/-- Dichotomy form over well-formed parameters. -/
theorem RBRIDGE_VF_H2_001_R_Lean_scaffold_wellFormedParams_dichotomy
    {wp : WellFormedRestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace wp.params x) :
    (inFixedSetR wp.params x → ledgerEffectR wp.params x = 0) ∧
    (¬ inFixedSetR wp.params x → 0 < ledgerEffectR wp.params x) := by
  exact restrictedBridgeWellFormedParamsTarget_proved wp x hspace

end RestrictedBridge
end VFH2
