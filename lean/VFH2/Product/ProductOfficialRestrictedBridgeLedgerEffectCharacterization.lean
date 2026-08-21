import VFH2.Product.ProductOfficialRestrictedBridgeOneStepStabilization

/-!
# Official Restricted-Bridge Ledger-Effect Characterization

This module upgrades the two one-way conclusions of the official restricted
bridge theorem to exact semantic characterizations on their minimal direct
domain:

- ledger effect is zero exactly at fixed-set states;
- ledger effect is positive exactly away from the fixed set;
No expected-width or well-formed-parameter hypothesis is needed.  Coordinate
bounds prevent decreases from above top, while active-index range ensures that
every declared active coordinate is visited by the list update.

Boundary:
- This concerns only the official finite list-backed restricted model.
- It uses only `hasLnBounds` and `activeIndicesInRange`; both are genuine
  semantic requirements of the raw list-backed model.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
-/

namespace VFH2
namespace RestrictedBridge

private theorem ledgerEffectR_pos_of_not_inFixedSetR_of_hasLnBounds_and_activeIndicesInRange
    {p : RestrictedParams}
    {x : State}
    (hb : hasLnBounds p x)
    (hrange : activeIndicesInRange p x)
    (hNotFixed : ¬ inFixedSetR p x) :
    0 < ledgerEffectR p x := by
  obtain ⟨i, hi, hNotTop⟩ :=
    exists_active_not_top_of_not_inFixedSetR p x hNotFixed
  have hLe : x.getD i 0 ≤ p.n :=
    getD_le_of_hasLnBounds hb i (hrange i hi)
  have hBelow : x.getD i 0 < p.n :=
    nat_lt_top_of_le_and_ne hLe hNotTop
  have hLocal : localActiveBelowTopFrom p 0 x :=
    localActiveBelowTopFrom_zero_of_exists_active_below_top
      hrange
      ⟨i, hi, hBelow⟩
  have hLedger :
      ledgerVR x < ledgerVR (updateStateR p x) := by
    simpa [updateStateR] using
      ledgerVR_lt_updateStateAuxR_of_localActiveBelowTop
        p x 0 hb hLocal
  unfold ledgerEffectR
  change
    (0 : Int) <
      (ledgerVR (updateStateR p x) : Int) -
        (ledgerVR x : Int)
  omega

/--
Under coordinate bounds and concrete active-index range, zero official ledger
effect is exactly fixed-set membership.
-/
theorem ledgerEffectR_eq_zero_iff_inFixedSetR_of_hasLnBounds_and_activeIndicesInRange
    {p : RestrictedParams}
    {x : State}
    (hb : hasLnBounds p x)
    (hrange : activeIndicesInRange p x) :
    ledgerEffectR p x = 0 ↔ inFixedSetR p x := by
  constructor
  · intro hZero
    by_cases hFixed : inFixedSetR p x
    · exact hFixed
    · have hPositive :
          0 < ledgerEffectR p x :=
        ledgerEffectR_pos_of_not_inFixedSetR_of_hasLnBounds_and_activeIndicesInRange
          hb hrange hFixed
      rw [hZero] at hPositive
      exact False.elim ((Int.lt_irrefl 0) hPositive)
  · intro hFixed
    exact
      ledgerEffectR_zero_of_inFixedSetR_no_assumption
        p x hFixed

/--
Under coordinate bounds and concrete active-index range, positive official
ledger effect is exactly failure of fixed-set membership.
-/
theorem ledgerEffectR_pos_iff_not_inFixedSetR_of_hasLnBounds_and_activeIndicesInRange
    {p : RestrictedParams}
    {x : State}
    (hb : hasLnBounds p x)
    (hrange : activeIndicesInRange p x) :
    0 < ledgerEffectR p x ↔ ¬ inFixedSetR p x := by
  constructor
  · intro hPositive hFixed
    have hZero :
        ledgerEffectR p x = 0 :=
      ledgerEffectR_zero_of_inFixedSetR_no_assumption
        p x hFixed
    rw [hZero] at hPositive
    exact (Int.lt_irrefl 0) hPositive
  · intro hNotFixed
    exact
      ledgerEffectR_pos_of_not_inFixedSetR_of_hasLnBounds_and_activeIndicesInRange
        hb hrange hNotFixed

end RestrictedBridge
end VFH2
