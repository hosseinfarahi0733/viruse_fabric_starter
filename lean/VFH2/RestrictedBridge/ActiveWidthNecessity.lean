import VFH2.RestrictedBridge.ActiveRangeEquivalence

/-!
# VF-H2 Restricted Bridge Active-Width Necessity

This file proves that the parameter-level active-width condition is not
derivable from the lightweight `RestrictedParams` record alone.

Boundary:
- This is a negative/necessity lemma for the current restricted Lean scaffold.
- It explains why `activeIndicesWithinWidth p` must remain part of the
  well-formed restricted input domain unless `RestrictedParams` is strengthened.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted `TTP-VF-H2-004`.
- It is not empirical validation.
- It is not biological validation.
-/

namespace VFH2
namespace RestrictedBridge

/-- A concrete parameter record with an out-of-width active index.

Here `d = 1`, so `expectedWidth = 3`.
The active index `3` is out of range for a length-3 list, whose valid indices
are `0`, `1`, and `2`.
-/
def activeWidthCounterexampleParams : RestrictedParams :=
  { n := 1, d := 1, active := [3] }

/-- The counterexample has expected width 3. -/
theorem activeWidthCounterexample_expectedWidth :
    expectedWidth activeWidthCounterexampleParams = 3 := by
  simp [activeWidthCounterexampleParams, expectedWidth]

/-- The out-of-width index 3 is active in the counterexample. -/
theorem activeWidthCounterexample_mem :
    3 ∈ activeWidthCounterexampleParams.active := by
  simp [activeWidthCounterexampleParams]

/-- The counterexample does not satisfy active-width well-formedness. -/
theorem not_activeIndicesWithinWidth_activeWidthCounterexampleParams :
    ¬ activeIndicesWithinWidth activeWidthCounterexampleParams := by
  intro h
  have hmem : 3 ∈ activeWidthCounterexampleParams.active :=
    activeWidthCounterexample_mem
  have hlt : 3 < expectedWidth activeWidthCounterexampleParams :=
    h 3 hmem
  simp [activeWidthCounterexampleParams, expectedWidth] at hlt

/-- There exist lightweight restricted parameters that do not satisfy
active-width well-formedness.
-/
theorem exists_params_not_activeIndicesWithinWidth :
    ∃ p : RestrictedParams, ¬ activeIndicesWithinWidth p := by
  exact ⟨
    activeWidthCounterexampleParams,
    not_activeIndicesWithinWidth_activeWidthCounterexampleParams
  ⟩

/-- Therefore active-width well-formedness cannot be derived for all
`RestrictedParams` records in the current scaffold.
-/
theorem not_forall_activeIndicesWithinWidth :
    ¬ (∀ p : RestrictedParams, activeIndicesWithinWidth p) := by
  intro hforall
  exact
    not_activeIndicesWithinWidth_activeWidthCounterexampleParams
      (hforall activeWidthCounterexampleParams)

end RestrictedBridge
end VFH2
