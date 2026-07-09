# Raw Source Conditions

lean/VFH2/Product/ProductRestrictedParamsActiveNoncoverageCertificate.lean:18:  not_all_active : ¬ ∀ i : ProductIndex p.d, i ∈ p.active
lean/VFH2/Product/ProductRestrictedParamsActiveNoncoverageCertificate.lean:23:def ActiveNoncoverageCertificate.of_not_all_active
lean/VFH2/Product/ProductRestrictedParamsActiveNoncoverageCertificate.lean:25:    (hNotAllActive : ¬ ∀ i : ProductIndex p.d, i ∈ p.active) :
lean/VFH2/Product/ProductRestrictedParamsActiveNoncoverageCertificate.lean:27:  { not_all_active := hNotAllActive }
lean/VFH2/Product/ProductRestrictedParamsActiveNoncoverageCertificate.lean:32:theorem ActiveNoncoverageCertificate.exists_inactive
lean/VFH2/Product/ProductRestrictedParamsActiveNoncoverageCertificate.lean:36:  exists_inactive_of_not_all_active p cert.not_all_active
lean/VFH2/Product/ProductRestrictedParamsActiveNoncoverageCertificate.lean:46:  InactiveIndexCertificate.of_exists_inactive p
lean/VFH2/Product/ProductRestrictedParamsActiveNoncoverageCertificate.lean:47:    (ActiveNoncoverageCertificate.exists_inactive p cert)
lean/VFH2/Product/ProductRestrictedParamsActiveNoncoverageCertificate.lean:58:  restrictedParams_existsInactiveIndex_fixedProductState_to_currentBestMainTheorem p
lean/VFH2/Product/ProductRestrictedParamsActiveNoncoverageCertificate.lean:59:    (ActiveNoncoverageCertificate.exists_inactive p cert)
lean/VFH2/Product/ProductRestrictedParamsInactiveCoordScore.lean:258:noncomputable def InactiveIndexCertificate.of_exists_inactive
lean/VFH2/Product/ProductRestrictedParamsInactiveCoordScore.lean:260:    (hExists : ∃ i : VFH2.ProductIndex p.d, ¬ i ∈ p.active) :
lean/VFH2/Product/ProductRestrictedParamsInactiveCoordScore.lean:263:    i := Classical.choose hExists
lean/VFH2/Product/ProductRestrictedParamsInactiveCoordScore.lean:264:    inactive := Classical.choose_spec hExists
lean/VFH2/Product/ProductRestrictedParamsInactiveCoordScore.lean:271:theorem restrictedParams_existsInactiveIndex_fixedProductState_to_currentBestMainTheorem
lean/VFH2/Product/ProductRestrictedParamsInactiveCoordScore.lean:273:    (hExists : ∃ i : VFH2.ProductIndex p.d, ¬ i ∈ p.active) :
lean/VFH2/Product/ProductRestrictedParamsInactiveCoordScore.lean:278:        (InactiveIndexCertificate.of_exists_inactive p hExists))
lean/VFH2/Product/ProductRestrictedParamsInactiveCoordScore.lean:286:          (InactiveIndexCertificate.of_exists_inactive p hExists)))
lean/VFH2/Product/ProductRestrictedParamsInactiveCoordScore.lean:295:      (InactiveIndexCertificate.of_exists_inactive p hExists)
lean/VFH2/Product/ProductRestrictedParamsActiveCoverage.lean:14:theorem exists_inactive_of_not_all_active
lean/VFH2/Product/ProductRestrictedParamsActiveCoverage.lean:16:    (hNotAllActive : ¬ ∀ i : ProductIndex p.d, i ∈ p.active) :
lean/VFH2/Product/ProductRestrictedParamsActiveCoverage.lean:20:    hNotAllActive (fun i =>
lean/VFH2/Product/ProductRestrictedParamsActiveCoverage.lean:30:noncomputable def InactiveIndexCertificate.of_not_all_active
lean/VFH2/Product/ProductRestrictedParamsActiveCoverage.lean:32:    (hNotAllActive : ¬ ∀ i : ProductIndex p.d, i ∈ p.active) :
lean/VFH2/Product/ProductRestrictedParamsActiveCoverage.lean:34:  InactiveIndexCertificate.of_exists_inactive p
lean/VFH2/Product/ProductRestrictedParamsActiveCoverage.lean:35:    (exists_inactive_of_not_all_active p hNotAllActive)
lean/VFH2/Product/ProductRestrictedParamsActiveCoverage.lean:44:noncomputable def restrictedParams_notAllActive_fixedProductState_to_currentBestMainTheorem
lean/VFH2/Product/ProductRestrictedParamsActiveCoverage.lean:46:    (hNotAllActive : ¬ ∀ i : ProductIndex p.d, i ∈ p.active) :=
lean/VFH2/Product/ProductRestrictedParamsActiveCoverage.lean:47:  restrictedParams_existsInactiveIndex_fixedProductState_to_currentBestMainTheorem p
lean/VFH2/Product/ProductRestrictedParamsActiveCoverage.lean:48:    (exists_inactive_of_not_all_active p hNotAllActive)
docs/impact/C30_ACTIVE_NONCOVERAGE_SOURCE_AUDIT.md:24:    exists_inactive_of_not_all_active
docs/impact/C30_ACTIVE_NONCOVERAGE_SOURCE_AUDIT.md:25:    InactiveIndexCertificate.of_not_all_active
docs/impact/C30_ACTIVE_NONCOVERAGE_SOURCE_AUDIT.md:26:    restrictedParams_notAllActive_fixedProductState_to_currentBestMainTheorem
docs/impact/C26_INACTIVE_COORD_SCORE_INSENSITIVE_ROUTE.md:74:exists_inactive_index
docs/impact/C29_NOT_ALL_ACTIVE_COVERAGE_ROUTE.md:17:    InactiveIndexCertificate.of_not_all_active
docs/impact/C29_NOT_ALL_ACTIVE_COVERAGE_ROUTE.md:21:    restrictedParams_notAllActive_fixedProductState_to_currentBestMainTheorem
docs/impact/C28_EXISTS_INACTIVE_INDEX_CERTIFICATE_ROUTE.md:24:InactiveIndexCertificate.of_exists_inactive
docs/impact/C28_EXISTS_INACTIVE_INDEX_CERTIFICATE_ROUTE.md:28:restrictedParams_existsInactiveIndex_fixedProductState_to_currentBestMainTheorem
docs/impact/C28_EXISTS_INACTIVE_INDEX_CERTIFICATE_ROUTE.md:50:hExists : ∃ i : ProductIndex p.d, ¬ i ∈ p.active
docs/impact/C28_EXISTS_INACTIVE_INDEX_CERTIFICATE_ROUTE.md:80:exists_inactive_of_active_length_lt_index_count
docs/impact/C27_INACTIVE_INDEX_CERTIFICATE_ROUTE.md:97:exists_inactiveIndexCertificate
docs/impact/C27_INACTIVE_INDEX_CERTIFICATE_ROUTE.md:103:InactiveIndexCertificate.of_not_all_active
docs/impact/C31_ACTIVE_NONCOVERAGE_CERTIFICATE.md:17:    not_all_active : not forall i : ProductIndex p.d, i in p.active
docs/impact/C31_ACTIVE_NONCOVERAGE_CERTIFICATE.md:31:    ActiveNoncoverageCertificate.of_not_all_active
docs/impact/C31_ACTIVE_NONCOVERAGE_CERTIFICATE.md:32:    ActiveNoncoverageCertificate.exists_inactive
