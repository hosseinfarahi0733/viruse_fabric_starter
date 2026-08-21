import VFH2.Product.ProductOfficialRestrictedBridgeLedgerEffectCharacterization

/-!
# Official Restricted-Bridge Ledger-Effect Bounds Necessity

This module proves that the coordinate-bounds premise in the exact official
ledger-effect characterization cannot be removed from the raw list-backed
model, even when the state has the expected width and every active index is in
range.

The witness contains one active coordinate above top and another below top.
Their update contributions cancel, so the ledger effect is zero although the
state is not fixed.  This is a genuine assumption-sharpness result for the C62
characterization, not a wrapper around either direction of that theorem.

Boundary:
- This concerns only the official finite list-backed restricted model.
- The witness lies outside `inRestrictedStateSpace` precisely because its
  coordinate bounds fail, so it does not contradict the official RBRIDGE
  theorem.
- It introduces no new assumption, model, bridge, or compatibility API.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
-/

namespace VFH2
namespace RestrictedBridge

/--
Without `hasLnBounds`, expected width and concrete active-index range do not
make zero ledger effect characterize fixed-set membership.
-/
theorem exists_expectedWidth_activeRange_zeroEffect_nonfixed_without_hasLnBounds :
    ∃ p : RestrictedParams,
      ∃ x : State,
        hasExpectedWidth p x ∧
        activeIndicesInRange p x ∧
        ¬ hasLnBounds p x ∧
        ledgerEffectR p x = 0 ∧
        ¬ inFixedSetR p x := by
  exact Exists.intro
    { n := 1, d := 1, active := [0, 1] }
    (Exists.intro [2, 0, 0]
      (And.intro rfl
        (And.intro (by simp [activeIndicesInRange])
          (And.intro (by simp [hasLnBounds])
            (And.intro rfl (by simp [inFixedSetR]))))))

end RestrictedBridge
end VFH2
