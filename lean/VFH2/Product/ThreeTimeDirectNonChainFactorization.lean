import VFH2.Product.ThreeTimeConstraintGeometry

/-!
# C117: Direct Non-Chain Factorization

This module strengthens the C114 shadow counterexample.  It defines an exact
adjacent-chain factorization and proves directly that the even-parity
three-time constraint has no such factorization.

The obstruction is a failed rectangle law at a fixed present: two admissible
past/future corners cannot be mixed to form a third admissible corner.
-/

namespace VFH2
namespace ThreeTime

/-- A binary constraint between two adjacent temporal layers. -/
abbrev BinaryConstraint (alpha : Type) : Type :=
  alpha -> alpha -> Prop

/-- Exact representation of a ternary constraint by an adjacent two-link chain. -/
def ChainRepresentable
    {alpha : Type}
    (r : TernaryConstraint alpha) : Prop :=
  exists left right : BinaryConstraint alpha,
    forall past present future,
      r past present future <->
        left past present /\ right present future

/-- Mixing admissible corners at a fixed present preserves admissibility. -/
def MiddleRectangleClosed
    {alpha : Type}
    (r : TernaryConstraint alpha) : Prop :=
  forall pastOne pastTwo present futureOne futureTwo,
    r pastOne present futureOne ->
      r pastTwo present futureTwo ->
        r pastOne present futureTwo

/-- Every adjacent-chain factorization obeys the middle rectangle law. -/
theorem chainRepresentable_middleRectangleClosed
    {alpha : Type}
    {r : TernaryConstraint alpha}
    (hchain : ChainRepresentable r) :
    MiddleRectangleClosed r := by
  rcases hchain with ⟨left, right, hfactor⟩
  intro pastOne pastTwo present futureOne futureTwo hOne hTwo
  have hOneFactors :=
    (hfactor pastOne present futureOne).mp hOne
  have hTwoFactors :=
    (hfactor pastTwo present futureTwo).mp hTwo
  exact
    (hfactor pastOne present futureTwo).mpr
      ⟨hOneFactors.1, hTwoFactors.2⟩

/-- Even parity violates the rectangle law at the middle value `false`. -/
theorem evenParity_not_middleRectangleClosed :
    ¬ MiddleRectangleClosed evenParity := by
  intro hrectangle
  have hmixed : evenParity false false true :=
    hrectangle false true false false true (by rfl) (by rfl)
  simp [evenParity] at hmixed

/-- Direct theorem: even parity cannot be reduced to an adjacent causal chain. -/
theorem evenParity_not_chainRepresentable :
    ¬ ChainRepresentable evenParity := by
  intro hchain
  exact evenParity_not_middleRectangleClosed
    (chainRepresentable_middleRectangleClosed hchain)

/-- A concrete genuinely ternary constraint exists. -/
theorem exists_non_chainRepresentable_threeTimeConstraint :
    exists r : TernaryConstraint Bool,
      ¬ ChainRepresentable r := by
  exact ⟨evenParity, evenParity_not_chainRepresentable⟩

end ThreeTime
end VFH2
