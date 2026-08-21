import VFH2.Product.ThreeTimeChainRepresentabilityCharacterization

/-!
# C119: Local-to-Global Gluing and Its Obstruction

Pairwise compatibility is the conjunction of the three existential shadows.
This module identifies the exact obstruction to reconstructing a global
ternary constraint from those local observations and exhibits that obstruction
for even parity.
-/

namespace VFH2
namespace ThreeTime

/-- All three pairwise shadows accept the proposed triple. -/
def PairwiseCompatible
    {alpha : Type}
    (r : TernaryConstraint alpha)
    (past present future : alpha) : Prop :=
  pastPresentShadow r past present /\
    presentFutureShadow r present future /\
      pastFutureShadow r past future

/-- Pairwise shadows recover the global relation pointwise. -/
def PairwiseShadowReconstructible
    {alpha : Type}
    (r : TernaryConstraint alpha) : Prop :=
  forall past present future,
    r past present future <->
      PairwiseCompatible r past present future

/-- A locally compatible triple rejected by the global constraint. -/
def HasPairwiseGluingObstruction
    {alpha : Type}
    (r : TernaryConstraint alpha) : Prop :=
  exists past present future,
    PairwiseCompatible r past present future /\
      ¬ r past present future

/-- A global witness always supplies witnesses for all three local shadows. -/
theorem constraint_implies_pairwiseCompatible
    {alpha : Type}
    {r : TernaryConstraint alpha}
    {past present future : alpha}
    (hr : r past present future) :
    PairwiseCompatible r past present future := by
  exact ⟨
    ⟨future, hr⟩,
    ⟨past, hr⟩,
    ⟨present, hr⟩
  ⟩

/--
Exact local-to-global theorem: pairwise reconstruction works precisely when no
locally compatible but globally forbidden triple exists.
-/
theorem pairwiseShadowReconstructible_iff_no_gluingObstruction
    {alpha : Type}
    (r : TernaryConstraint alpha) :
    PairwiseShadowReconstructible r <->
      (¬ HasPairwiseGluingObstruction r) := by
  constructor
  · intro hreconstruct hobstruction
    rcases hobstruction with
      ⟨past, present, future, hlocal, hnotGlobal⟩
    exact hnotGlobal
      ((hreconstruct past present future).mpr hlocal)
  · intro hnoObstruction past present future
    constructor
    · exact constraint_implies_pairwiseCompatible
    · intro hlocal
      classical
      by_cases hglobal : r past present future
      · exact hglobal
      · exact False.elim
          (hnoObstruction
            ⟨past, present, future, hlocal, hglobal⟩)

/-- Even parity has a concrete pairwise gluing obstruction. -/
theorem evenParity_has_pairwiseGluingObstruction :
    HasPairwiseGluingObstruction evenParity := by
  refine ⟨false, false, true, ?_, ?_⟩
  · exact ⟨
      evenParity_pastPresentShadow false false,
      evenParity_presentFutureShadow false true,
      evenParity_pastFutureShadow false true
    ⟩
  · simp [evenParity]

/-- Therefore even parity cannot be recovered from all pairwise shadows. -/
theorem evenParity_not_pairwiseShadowReconstructible :
    ¬ PairwiseShadowReconstructible evenParity := by
  intro hreconstruct
  exact
    ((pairwiseShadowReconstructible_iff_no_gluingObstruction
      evenParity).mp hreconstruct)
      evenParity_has_pairwiseGluingObstruction

end ThreeTime
end VFH2
