import VFH2.RestrictedBridge.WellFormedDomain

/-!
# VF-H2 Official Restricted Bridge Lean Scaffold Alias

This file gives the current restricted Lean scaffold theorem a canonical
project-level name.

Boundary:
- This theorem is restricted, list-backed, and scaffold-level.
- It is over the named `wellFormedRestrictedInput` domain.
- It is not a proof of the full Viruse Fabric theory.
- It is not a proof of unrestricted `TTP-VF-H2-004`.
- It is not empirical validation.
- It is not biological validation.
-/

namespace VFH2
namespace RestrictedBridge

/-- Canonical target for the Lean scaffold version of `RBRIDGE-VF-H2-001-R`. -/
def RBRIDGE_VF_H2_001_R_Lean_scaffold_target
    (p : RestrictedParams) (x : State) : Prop :=
  restrictedBridgeWellFormedTarget p x

/-- Official Lean scaffold alias for the restricted bridge theorem.

For every well-formed restricted input:
- fixed-set states have zero scaffold ledger effect;
- nonfixed states have positive scaffold ledger effect.
-/
theorem RBRIDGE_VF_H2_001_R_Lean_scaffold
    (p : RestrictedParams) (x : State) :
    RBRIDGE_VF_H2_001_R_Lean_scaffold_target p x := by
  exact restrictedBridgeWellFormedTarget_proved p x

/-- Official fixed-set zero-effect corollary. -/
theorem RBRIDGE_VF_H2_001_R_Lean_scaffold_fixed_zero
    {p : RestrictedParams} {x : State}
    (hwf : wellFormedRestrictedInput p x)
    (hfixed : inFixedSetR p x) :
    ledgerEffectR p x = 0 := by
  exact finalRestrictedBridge_wellFormed_fixed_zero hwf hfixed

/-- Official nonfixed positive-effect corollary. -/
theorem RBRIDGE_VF_H2_001_R_Lean_scaffold_nonfixed_positive
    {p : RestrictedParams} {x : State}
    (hwf : wellFormedRestrictedInput p x)
    (hnotfixed : ¬ inFixedSetR p x) :
    0 < ledgerEffectR p x := by
  exact finalRestrictedBridge_wellFormed_nonfixed_positive hwf hnotfixed

/-- Official dichotomy corollary for the restricted Lean scaffold. -/
theorem RBRIDGE_VF_H2_001_R_Lean_scaffold_dichotomy
    {p : RestrictedParams} {x : State}
    (hwf : wellFormedRestrictedInput p x) :
    (inFixedSetR p x → ledgerEffectR p x = 0) ∧
    (¬ inFixedSetR p x → 0 < ledgerEffectR p x) := by
  exact finalRestrictedBridge_wellFormed_dichotomy hwf

end RestrictedBridge
end VFH2
