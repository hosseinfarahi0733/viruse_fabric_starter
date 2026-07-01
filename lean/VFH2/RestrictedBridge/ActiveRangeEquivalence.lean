import VFH2.RestrictedBridge.OfficialRBridge

/-!
# VF-H2 Restricted Bridge Active Range / Width Equivalence

This file proves that, inside the restricted state space, the older
state-specific active range condition is equivalent to the cleaner
parameter-level active-width condition.

Boundary:
- This is a proof-strengthening/domain-clarification lemma for the current
  restricted Lean scaffold.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted `TTP-VF-H2-004`.
- It is not empirical validation.
- It is not biological validation.
-/

namespace VFH2
namespace RestrictedBridge

/-- Inside the restricted state space, concrete active-index range is equivalent
to parameter-level active-width well-formedness.

This justifies replacing the state-specific condition
`activeIndicesInRange p x` with the cleaner parameter-level condition
`activeIndicesWithinWidth p`.
-/
theorem activeIndicesInRange_iff_activeIndicesWithinWidth_of_inRestrictedStateSpace
    {p : RestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace p x) :
    activeIndicesInRange p x ↔ activeIndicesWithinWidth p := by
  constructor
  · intro hrange
    intro i hi
    have hix : i < x.length := hrange i hi
    have hwidth : x.length = expectedWidth p := hspace.1
    simpa [hwidth] using hix
  · intro hactiveWidth
    exact activeIndicesInRange_of_activeIndicesWithinWidth hspace hactiveWidth

/-- Active range implies active-width well-formedness inside the restricted
state space.
-/
theorem activeIndicesWithinWidth_of_activeIndicesInRange
    {p : RestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace p x)
    (hrange : activeIndicesInRange p x) :
    activeIndicesWithinWidth p := by
  exact
    (activeIndicesInRange_iff_activeIndicesWithinWidth_of_inRestrictedStateSpace
      hspace).1 hrange

/-- Active-width well-formedness implies active range inside the restricted
state space.
-/
theorem activeIndicesInRange_of_activeIndicesWithinWidth_and_space
    {p : RestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace p x)
    (hactiveWidth : activeIndicesWithinWidth p) :
    activeIndicesInRange p x := by
  exact
    (activeIndicesInRange_iff_activeIndicesWithinWidth_of_inRestrictedStateSpace
      hspace).2 hactiveWidth

/-- The named well-formed input domain is equivalent to the original pair of
restricted state-space and concrete active-range assumptions.
-/
theorem wellFormedRestrictedInput_iff_space_and_activeRange
    {p : RestrictedParams} {x : State} :
    wellFormedRestrictedInput p x ↔
      inRestrictedStateSpace p x ∧ activeIndicesInRange p x := by
  constructor
  · intro hwf
    exact ⟨
      wellFormedRestrictedInput_space hwf,
      activeIndicesInRange_of_wellFormedRestrictedInput hwf
    ⟩
  · intro h
    exact ⟨
      h.1,
      activeIndicesWithinWidth_of_activeIndicesInRange h.1 h.2
    ⟩

/-- The official scaffold theorem can also be read over the original
state-space plus active-range domain.
-/
theorem RBRIDGE_VF_H2_001_R_Lean_scaffold_original_domain
    {p : RestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace p x)
    (hrange : activeIndicesInRange p x) :
    (inFixedSetR p x → ledgerEffectR p x = 0) ∧
    (¬ inFixedSetR p x → 0 < ledgerEffectR p x) := by
  have hwf : wellFormedRestrictedInput p x := by
    exact (wellFormedRestrictedInput_iff_space_and_activeRange).2
      ⟨hspace, hrange⟩
  exact RBRIDGE_VF_H2_001_R_Lean_scaffold_dichotomy hwf

end RestrictedBridge
end VFH2
