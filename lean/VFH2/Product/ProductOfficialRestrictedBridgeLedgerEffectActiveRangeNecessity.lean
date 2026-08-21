import VFH2.Product.ProductOfficialRestrictedBridgeLedgerEffectCharacterization

/-!
# Official Restricted-Bridge Ledger-Effect Active-Range Necessity

This module proves that the active-index-range premise in the exact official
ledger-effect characterization cannot be removed from the raw list-backed
model, even for a state inside the restricted state space.

The witness declares an active index just beyond the end of the state.  The
list update never visits that index and therefore has zero ledger effect, while
`inFixedSetR` still observes it through `getD` and rejects the default value.
This is a genuine assumption-sharpness result for the C62 characterization,
complementary to the independent coordinate-bounds counterexample.

Boundary:
- This concerns only the official finite list-backed restricted model.
- The witness satisfies `inRestrictedStateSpace` but fails active-index range
  and parameter well-formedness, so it does not contradict the official
  RBRIDGE theorem.
- It introduces no new assumption, model, bridge, or compatibility API.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
-/

namespace VFH2
namespace RestrictedBridge

/--
Without concrete active-index range, restricted state-space membership does
not make zero ledger effect characterize fixed-set membership.
-/
theorem exists_inRestrictedStateSpace_zeroEffect_nonfixed_without_activeRange :
    ∃ p : RestrictedParams,
      ∃ x : State,
        inRestrictedStateSpace p x ∧
        ¬ activeIndicesInRange p x ∧
        ledgerEffectR p x = 0 ∧
        ¬ inFixedSetR p x := by
  exact Exists.intro
    activeWidthCounterexampleParams
    (Exists.intro [0, 0, 0]
      (And.intro
        (And.intro rfl
          (by simp [hasLnBounds, activeWidthCounterexampleParams]))
        (And.intro
          (by simp [activeIndicesInRange, activeWidthCounterexampleParams])
          (And.intro rfl
            (by simp [inFixedSetR, activeWidthCounterexampleParams])))))

end RestrictedBridge
end VFH2
