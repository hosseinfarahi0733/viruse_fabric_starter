import VFH2.Product.ProductRestrictedParamsActiveNoncoverageCertificate

namespace VFH2
namespace ProductRestrictedParamsInactiveCoordScore

#check ProductRestrictedParams
#check ProductIndex

#check exists_inactive_of_not_all_active
#check InactiveIndexCertificate.of_not_all_active
#check restrictedParams_notAllActive_fixedProductState_to_currentBestMainTheorem

#check ActiveNoncoverageCertificate
#check ActiveNoncoverageCertificate.of_not_all_active
#check ActiveNoncoverageCertificate.exists_inactive
#check ActiveNoncoverageCertificate.toInactiveIndexCertificate
#check restrictedParams_activeNoncoverageCertificate_fixedProductState_to_currentBestMainTheorem

#check InactiveIndexCertificate
#check InactiveIndexCertificate.of_exists_inactive
#check restrictedParams_existsInactiveIndex_fixedProductState_to_currentBestMainTheorem

#check fun (p : ProductRestrictedParams) =>
  ActiveNoncoverageCertificate p

#check fun (p : ProductRestrictedParams) =>
  ¬ ∀ i : ProductIndex p.d, i ∈ p.active

#check fun (p : ProductRestrictedParams) =>
  ∃ i : ProductIndex p.d, ¬ i ∈ p.active

end ProductRestrictedParamsInactiveCoordScore
end VFH2
