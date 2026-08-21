import VFH2.UnrestrictedBridge.ProductConservativity

/-!
# Product Embedding Admissibility

This module proves that the canonical Product embedding introduced by the
countably indexed finite-observation bridge automatically satisfies the two
semantic hypotheses used by the C73 and C74 ledger-effect characterizations:

- the zero-extended embedded state is bounded at every natural coordinate;
- the canonical finite observation window covers every embedded active index.

The proofs use the bounds and active-width facts of the existing canonical
Product-to-official-restricted serialization. No additional assumption is
introduced.

Boundary:
- This is an admissibility result for the existing restricted Product
  serialization inside the countably indexed finite-observation bridge.
- It does not define a global infinite ledger.
- It is not unrestricted `TTP-VF-H2-004`.
- It makes no full-theory, empirical, or biological claim.
-/

namespace VFH2
namespace UnrestrictedBridge

open ProductOfficialRestrictedBridgeStateTransport

/--
Every canonically embedded Product state belongs to the countably indexed
state space.

Inside the serialized finite width, this is the existing Product-state bound.
Outside that width, the official embedding is zero by construction.
-/
theorem stateUOfProduct_inStateSpaceU
    (p : ProductRestrictedParams)
    (x : p.State) :
    inStateSpaceU
      (paramsUOfProduct p)
      (stateUOfProduct p x) := by
  intro i
  change
    (officialRestrictedState p x).getD i 0 ≤
      (officialRestrictedParams p).n

  have hspace :
      RestrictedBridge.inRestrictedStateSpace
        (officialRestrictedParams p)
        (officialRestrictedState p x) :=
    (officialRestrictedInput_wellFormed p x).1

  by_cases hi : i < (officialRestrictedState p x).length
  · exact
      RestrictedBridge.getD_le_of_inRestrictedStateSpace
        hspace
        i
        hi
  · rw [List.getD_eq_getElem?_getD]
    rw [List.getElem?_eq_none (Nat.le_of_not_gt hi)]
    simp

/--
The canonical Product observation window contains every canonically embedded
active coordinate.
-/
theorem productWindowU_covers_active
    (p : ProductRestrictedParams) :
    ∀ i : Nat,
      i ∈ (paramsUOfProduct p).active →
      i ∈ productWindowU p := by
  intro i hi
  change i ∈ (officialRestrictedParams p).active at hi
  change
    i ∈ List.range
      (RestrictedBridge.expectedWidth (officialRestrictedParams p))
  exact
    List.mem_range.mpr
      (officialRestrictedParams_activeIndicesWithinWidth p i hi)

end UnrestrictedBridge
end VFH2
