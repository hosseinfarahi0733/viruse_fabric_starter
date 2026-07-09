# C32 Lean Probe Output

VFH2.ProductRestrictedParams : Type
VFH2.ProductIndex (d : Nat) : Type
VFH2.ProductRestrictedParamsInactiveCoordScore.exists_inactive_of_not_all_active (p : ProductRestrictedParams)
  (hNotAllActive : ¬∀ (i : ProductIndex p.d), i ∈ p.active) : ∃ i, ¬i ∈ p.active
VFH2.ProductRestrictedParamsInactiveCoordScore.InactiveIndexCertificate.of_not_all_active (p : ProductRestrictedParams)
  (hNotAllActive : ¬∀ (i : ProductIndex p.d), i ∈ p.active) : InactiveIndexCertificate p
VFH2.ProductRestrictedParamsInactiveCoordScore.restrictedParams_notAllActive_fixedProductState_to_currentBestMainTheorem
  (p : ProductRestrictedParams) (hNotAllActive : ¬∀ (i : ProductIndex p.d), i ∈ p.active) :
  ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget p
    (ProductRestrictedParamsFixedStateConstruction.fixedProductState p) (productUpdateState p)
    (inactiveIndexCertificateScore p (InactiveIndexCertificate.of_exists_inactive p ⋯))
    (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p
      (ProductRestrictedParamsFixedStateConstruction.fixedProductState p) (productUpdateState p))
    (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p
      (ProductRestrictedParamsFixedStateConstruction.fixedProductState p) (productUpdateState p)
      (inactiveIndexCertificateScore p (InactiveIndexCertificate.of_exists_inactive p ⋯)))
    (ProductFixedSet p (ProductRestrictedParamsFixedStateConstruction.fixedProductState p)) 0 (Int.ofNat p.n) ⋯
VFH2.ProductRestrictedParamsInactiveCoordScore.ActiveNoncoverageCertificate (p : ProductRestrictedParams) : Type
VFH2.ProductRestrictedParamsInactiveCoordScore.ActiveNoncoverageCertificate.of_not_all_active
  (p : ProductRestrictedParams) (hNotAllActive : ¬∀ (i : ProductIndex p.d), i ∈ p.active) :
  ActiveNoncoverageCertificate p
VFH2.ProductRestrictedParamsInactiveCoordScore.ActiveNoncoverageCertificate.exists_inactive
  (p : ProductRestrictedParams) (cert : ActiveNoncoverageCertificate p) : ∃ i, ¬i ∈ p.active
VFH2.ProductRestrictedParamsInactiveCoordScore.ActiveNoncoverageCertificate.toInactiveIndexCertificate
  (p : ProductRestrictedParams) (cert : ActiveNoncoverageCertificate p) : InactiveIndexCertificate p
VFH2.ProductRestrictedParamsInactiveCoordScore.restrictedParams_activeNoncoverageCertificate_fixedProductState_to_currentBestMainTheorem
  (p : ProductRestrictedParams) (cert : ActiveNoncoverageCertificate p) :
  ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget p
    (ProductRestrictedParamsFixedStateConstruction.fixedProductState p) (productUpdateState p)
    (inactiveIndexCertificateScore p (InactiveIndexCertificate.of_exists_inactive p ⋯))
    (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p
      (ProductRestrictedParamsFixedStateConstruction.fixedProductState p) (productUpdateState p))
    (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p
      (ProductRestrictedParamsFixedStateConstruction.fixedProductState p) (productUpdateState p)
      (inactiveIndexCertificateScore p (InactiveIndexCertificate.of_exists_inactive p ⋯)))
    (ProductFixedSet p (ProductRestrictedParamsFixedStateConstruction.fixedProductState p)) 0 (Int.ofNat p.n) ⋯
VFH2.ProductRestrictedParamsInactiveCoordScore.InactiveIndexCertificate (p : ProductRestrictedParams) : Type
VFH2.ProductRestrictedParamsInactiveCoordScore.InactiveIndexCertificate.of_exists_inactive (p : ProductRestrictedParams)
  (hExists : ∃ i, ¬i ∈ p.active) : InactiveIndexCertificate p
VFH2.ProductRestrictedParamsInactiveCoordScore.restrictedParams_existsInactiveIndex_fixedProductState_to_currentBestMainTheorem
  (p : ProductRestrictedParams) (hExists : ∃ i, ¬i ∈ p.active) :
  ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget p
    (ProductRestrictedParamsFixedStateConstruction.fixedProductState p) (productUpdateState p)
    (inactiveIndexCertificateScore p (InactiveIndexCertificate.of_exists_inactive p hExists))
    (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p
      (ProductRestrictedParamsFixedStateConstruction.fixedProductState p) (productUpdateState p))
    (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p
      (ProductRestrictedParamsFixedStateConstruction.fixedProductState p) (productUpdateState p)
      (inactiveIndexCertificateScore p (InactiveIndexCertificate.of_exists_inactive p hExists)))
    (ProductFixedSet p (ProductRestrictedParamsFixedStateConstruction.fixedProductState p)) 0 (Int.ofNat p.n) ⋯
fun p => ActiveNoncoverageCertificate p : ProductRestrictedParams → Type
fun p => ¬∀ (i : ProductIndex p.d), i ∈ p.active : ProductRestrictedParams → Prop
fun p => ∃ i, ¬i ∈ p.active : ProductRestrictedParams → Prop
