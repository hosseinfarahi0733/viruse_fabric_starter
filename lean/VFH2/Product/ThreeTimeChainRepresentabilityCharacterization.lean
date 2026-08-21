import VFH2.Product.ThreeTimeDirectNonChainFactorization

/-!
# C118: Exact Characterization of Adjacent-Chain Representability

The middle rectangle law is not merely necessary.  It is sufficient, and its
canonical factors are exactly the two adjacent existential shadows.
-/

namespace VFH2
namespace ThreeTime

/--
A ternary constraint factors through an adjacent chain exactly when each fiber
over the present is a Cartesian rectangle.
-/
theorem chainRepresentable_iff_middleRectangleClosed
    {alpha : Type}
    (r : TernaryConstraint alpha) :
    ChainRepresentable r <-> MiddleRectangleClosed r := by
  constructor
  · exact chainRepresentable_middleRectangleClosed
  · intro hrectangle
    refine ⟨pastPresentShadow r, presentFutureShadow r, ?_⟩
    intro past present future
    constructor
    · intro hr
      exact ⟨⟨future, hr⟩, ⟨past, hr⟩⟩
    · rintro ⟨⟨futureOne, hleft⟩, ⟨pastTwo, hright⟩⟩
      exact
        hrectangle past pastTwo present futureOne future
          hleft hright

/--
Whenever the rectangle law holds, the two adjacent shadows reconstruct the
entire three-time constraint exactly.
-/
theorem canonical_adjacentShadows_factorization
    {alpha : Type}
    (r : TernaryConstraint alpha)
    (hrectangle : MiddleRectangleClosed r) :
    forall past present future,
      r past present future <->
        pastPresentShadow r past present /\
          presentFutureShadow r present future := by
  rcases
      (chainRepresentable_iff_middleRectangleClosed r).mpr hrectangle with
    ⟨left, right, hfactor⟩
  intro past present future
  constructor
  · intro hr
    exact ⟨⟨future, hr⟩, ⟨past, hr⟩⟩
  · rintro ⟨⟨futureOne, hleft⟩, ⟨pastTwo, hright⟩⟩
    exact
      hrectangle past pastTwo present futureOne future
        hleft hright

/-- The parity witness fails the exact factorization criterion. -/
theorem evenParity_fails_chain_characterization :
    (¬ MiddleRectangleClosed evenParity) /\
      (¬ ChainRepresentable evenParity) := by
  exact ⟨
    evenParity_not_middleRectangleClosed,
    evenParity_not_chainRepresentable
  ⟩

end ThreeTime
end VFH2
