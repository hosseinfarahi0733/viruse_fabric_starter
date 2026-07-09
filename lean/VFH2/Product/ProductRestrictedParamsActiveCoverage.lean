import VFH2.Product.ProductRestrictedParamsInactiveCoordScore

namespace VFH2
namespace ProductRestrictedParamsInactiveCoordScore

/--
If the active list does not cover every product index, then there exists
an inactive product index.

This is intentionally not a cardinality theorem. It does not assume that
`p.active` is duplicate-free, nor that `ProductIndex p.d` has an exposed
enumeration. It only packages the logically minimal non-coverage condition.
-/
theorem exists_inactive_of_not_all_active
    (p : ProductRestrictedParams)
    (hNotAllActive : ¬ ∀ i : ProductIndex p.d, i ∈ p.active) :
    ∃ i : ProductIndex p.d, ¬ i ∈ p.active := by
  classical
  exact Classical.byContradiction (fun hNoExists =>
    hNotAllActive (fun i =>
      Classical.byContradiction (fun hi =>
        hNoExists ⟨i, hi⟩)))

/--
A certificate constructor from the structural non-coverage condition.

This is the smallest safe bridge from a coverage-style source condition
to the inactive-index certificate route built in C28.
-/
noncomputable def InactiveIndexCertificate.of_not_all_active
    (p : ProductRestrictedParams)
    (hNotAllActive : ¬ ∀ i : ProductIndex p.d, i ∈ p.active) :
    InactiveIndexCertificate p :=
  InactiveIndexCertificate.of_exists_inactive p
    (exists_inactive_of_not_all_active p hNotAllActive)

/--
Front-door route from non-coverage of the active list to the current
restricted proof-spine target.

The target type is inferred from the existing C28 theorem, avoiding
another fragile hand-written copy of the long proof-spine target.
-/
noncomputable def restrictedParams_notAllActive_fixedProductState_to_currentBestMainTheorem
    (p : ProductRestrictedParams)
    (hNotAllActive : ¬ ∀ i : ProductIndex p.d, i ∈ p.active) :=
  restrictedParams_existsInactiveIndex_fixedProductState_to_currentBestMainTheorem p
    (exists_inactive_of_not_all_active p hNotAllActive)

end ProductRestrictedParamsInactiveCoordScore
end VFH2
