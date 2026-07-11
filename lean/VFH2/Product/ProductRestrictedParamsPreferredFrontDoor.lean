import VFH2.Product.ProductRestrictedParamsActiveEraseConstruction

namespace VFH2
namespace ProductRestrictedParamsPreferredFrontDoor

/--
Preferred restricted-parameter construction for the current product proof route.

The active list is not supplied as an unconstrained raw list. It is constructed
from the complete product-index enumeration by erasing one selected product
index, so the strict active-length deficit and active noncoverage are derived by
construction.
-/
abbrev preferredParams
    (n d : Nat)
    (missing : ProductIndex d) :
    ProductRestrictedParams :=
  ProductRestrictedParamsActiveEraseConstruction.paramsWithInactiveProductIndex
    n d missing

/--
Preferred structural source for the construction-level restricted parameters.
-/
def preferredActiveLengthSource
    (n d : Nat)
    (missing : ProductIndex d) :
    ProductRestrictedParamsActiveLengthLowerBound.ActiveLengthLtTypedWidthSource
      (preferredParams n d missing) :=
  ProductRestrictedParamsActiveEraseConstruction.activeLengthLtTypedWidthSource_of_paramsWithInactiveProductIndex
    n d missing

/--
Preferred active-noncoverage certificate. The certificate is derived from the
construction-local active-length bound rather than a raw noncoverage premise.
-/
def preferredActiveNoncoverageCertificate
    (n d : Nat)
    (missing : ProductIndex d) :
    ProductRestrictedParamsInactiveCoordScore.ActiveNoncoverageCertificate
      (preferredParams n d missing) :=
  ProductRestrictedParamsActiveEraseConstruction.activeNoncoverageCertificate_of_paramsWithInactiveProductIndex
    n d missing

/--
Preferred C35B front door into the current restricted proof-spine theorem.

New construction-level callers should use this declaration. It accepts only the
construction data `n`, `d`, and the selected missing product index. The active
length source, noncoverage certificate, inactive coordinate, score, score range,
and fixed-state route are selected by the existing verified chain.
-/
noncomputable def currentBestMainTheorem
    (n d : Nat)
    (missing : ProductIndex d) :=
  ProductRestrictedParamsActiveEraseConstruction.restrictedParams_paramsWithInactiveProductIndex_fixedProductState_to_currentBestMainTheorem
    n d missing

namespace Compatibility

/--
Compatibility adapter for arbitrary restricted parameters that already carry a
strict active-length source. Prefer `currentBestMainTheorem` when parameters are
created by the erase construction.
-/
def activeNoncoverageCertificate_of_activeLengthSource
    (p : ProductRestrictedParams)
    (src :
      ProductRestrictedParamsActiveLengthLowerBound.ActiveLengthLtTypedWidthSource
        p) :
    ProductRestrictedParamsInactiveCoordScore.ActiveNoncoverageCertificate p :=
  ProductRestrictedParamsActiveLengthLowerBound.activeNoncoverageCertificate_of_active_length_lt_typedWidth
    p src

/--
Compatibility front door for arbitrary parameters equipped with the structural
active-length source.
-/
noncomputable def currentBestMainTheorem_of_activeLengthSource
    (p : ProductRestrictedParams)
    (src :
      ProductRestrictedParamsActiveLengthLowerBound.ActiveLengthLtTypedWidthSource
        p) :=
  ProductRestrictedParamsInactiveCoordScore.restrictedParams_activeNoncoverageCertificate_fixedProductState_to_currentBestMainTheorem
    p
    (activeNoncoverageCertificate_of_activeLengthSource p src)

/--
Compatibility front door for callers that already own an active-noncoverage
certificate. New construction-level code should not manufacture this
certificate from a raw premise when the erase constructor is available.
-/
noncomputable def currentBestMainTheorem_of_activeNoncoverageCertificate
    (p : ProductRestrictedParams)
    (cert :
      ProductRestrictedParamsInactiveCoordScore.ActiveNoncoverageCertificate p) :=
  ProductRestrictedParamsInactiveCoordScore.restrictedParams_activeNoncoverageCertificate_fixedProductState_to_currentBestMainTheorem
    p cert

/--
Legacy compatibility front door from the raw noncoverage premise.

This declaration intentionally preserves the old route without making it the
preferred API. New code should use `ProductRestrictedParamsPreferredFrontDoor.currentBestMainTheorem`
when the active list is produced by the erase construction.
-/
noncomputable def currentBestMainTheorem_of_notAllActive
    (p : ProductRestrictedParams)
    (hNotAllActive : ¬ ∀ i : ProductIndex p.d, i ∈ p.active) :=
  ProductRestrictedParamsInactiveCoordScore.restrictedParams_notAllActive_fixedProductState_to_currentBestMainTheorem
    p hNotAllActive

end Compatibility

#check preferredParams
#check preferredActiveLengthSource
#check preferredActiveNoncoverageCertificate
#check currentBestMainTheorem
#check Compatibility.activeNoncoverageCertificate_of_activeLengthSource
#check Compatibility.currentBestMainTheorem_of_activeLengthSource
#check Compatibility.currentBestMainTheorem_of_activeNoncoverageCertificate
#check Compatibility.currentBestMainTheorem_of_notAllActive

end ProductRestrictedParamsPreferredFrontDoor
end VFH2
