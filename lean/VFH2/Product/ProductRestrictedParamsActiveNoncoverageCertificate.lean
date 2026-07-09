import VFH2.Product.ProductRestrictedParamsActiveCoverage

namespace VFH2
namespace ProductRestrictedParamsInactiveCoordScore

/--
A source certificate recording that the active list does not cover every
product index.

This packages the C29 source condition:

  ¬ ∀ i : ProductIndex p.d, i ∈ p.active

as a first-class certificate, keeping the proof-spine API aligned with the
project's certificate-based architecture.
-/
structure ActiveNoncoverageCertificate (p : ProductRestrictedParams) : Type where
  not_all_active : ¬ ∀ i : ProductIndex p.d, i ∈ p.active

/--
Constructor from the raw noncoverage proof.
-/
def ActiveNoncoverageCertificate.of_not_all_active
    (p : ProductRestrictedParams)
    (hNotAllActive : ¬ ∀ i : ProductIndex p.d, i ∈ p.active) :
    ActiveNoncoverageCertificate p :=
  { not_all_active := hNotAllActive }

/--
The active-noncoverage certificate yields an inactive-index witness.
-/
theorem ActiveNoncoverageCertificate.exists_inactive
    (p : ProductRestrictedParams)
    (cert : ActiveNoncoverageCertificate p) :
    ∃ i : ProductIndex p.d, ¬ i ∈ p.active :=
  exists_inactive_of_not_all_active p cert.not_all_active

/--
Convert an active-noncoverage certificate into the inactive-index certificate
introduced earlier.
-/
noncomputable def ActiveNoncoverageCertificate.toInactiveIndexCertificate
    (p : ProductRestrictedParams)
    (cert : ActiveNoncoverageCertificate p) :
    InactiveIndexCertificate p :=
  InactiveIndexCertificate.of_exists_inactive p
    (ActiveNoncoverageCertificate.exists_inactive p cert)

/--
Front-door route from an active-noncoverage certificate to the current
restricted proof-spine target.

This avoids exposing the raw noncoverage proof at the final API boundary.
-/
noncomputable def restrictedParams_activeNoncoverageCertificate_fixedProductState_to_currentBestMainTheorem
    (p : ProductRestrictedParams)
    (cert : ActiveNoncoverageCertificate p) :=
  restrictedParams_existsInactiveIndex_fixedProductState_to_currentBestMainTheorem p
    (ActiveNoncoverageCertificate.exists_inactive p cert)

end ProductRestrictedParamsInactiveCoordScore
end VFH2
