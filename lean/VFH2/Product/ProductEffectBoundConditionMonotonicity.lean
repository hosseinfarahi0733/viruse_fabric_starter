import VFH2.Product.ProductEffectBoundBridgeCertificate

namespace VFH2

namespace ProductEffectBoundConditionMonotonicity

/--
Lower-bound effect predicates are monotone under threshold relaxation:
if `thresholdLo ≤ thresholdHi`, then satisfying the high threshold implies
satisfying the low threshold.
-/
theorem effectLowerBoundPredicate_mono
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ∀ e : Int,
      ProductEffectBoundBridgeSpecialization.effectLowerBoundPredicate
          thresholdHi e →
      ProductEffectBoundBridgeSpecialization.effectLowerBoundPredicate
          thresholdLo e := by
  intro e hHi
  unfold ProductEffectBoundBridgeSpecialization.effectLowerBoundPredicate at hHi ⊢
  exact Int.le_trans hThreshold hHi

/--
Upper-bound effect predicates are monotone under threshold relaxation:
if `thresholdLo ≤ thresholdHi`, then satisfying the low threshold implies
satisfying the high threshold.
-/
theorem effectUpperBoundPredicate_mono
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ∀ e : Int,
      ProductEffectBoundBridgeSpecialization.effectUpperBoundPredicate
          thresholdLo e →
      ProductEffectBoundBridgeSpecialization.effectUpperBoundPredicate
          thresholdHi e := by
  intro e hLo
  unfold ProductEffectBoundBridgeSpecialization.effectUpperBoundPredicate at hLo ⊢
  exact Int.le_trans hLo hThreshold

/--
Generalized typed-side lower-bound effect conditions are monotone under
threshold relaxation.
-/
theorem generalized_typedEffectLowerBoundCondition_mono
    {n d : Nat}
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (typedScore : Typed.TypedState n d → Int)
    (x : ProductTypedState n d)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductEffectBoundBridgeSpecialization.generalizedTypedEffectLowerBoundCondition
        typedUpdate typedScore x thresholdHi →
    ProductEffectBoundBridgeSpecialization.generalizedTypedEffectLowerBoundCondition
        typedUpdate typedScore x thresholdLo := by
  intro hHi
  unfold ProductEffectBoundBridgeSpecialization.generalizedTypedEffectLowerBoundCondition at hHi ⊢
  unfold ProductEffectConditionBridgeGeneralization.generalizedTypedEffectCondition at hHi ⊢
  exact effectLowerBoundPredicate_mono thresholdLo thresholdHi hThreshold _ hHi

/--
Generalized product-side lower-bound effect conditions are monotone under
threshold relaxation.
-/
theorem generalized_productEffectLowerBoundCondition_mono
    {n d : Nat}
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (productScore : ProductTypedState n d → Int)
    (x : ProductTypedState n d)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductEffectBoundBridgeSpecialization.generalizedProductEffectLowerBoundCondition
        productUpdate productScore x thresholdHi →
    ProductEffectBoundBridgeSpecialization.generalizedProductEffectLowerBoundCondition
        productUpdate productScore x thresholdLo := by
  intro hHi
  unfold ProductEffectBoundBridgeSpecialization.generalizedProductEffectLowerBoundCondition at hHi ⊢
  unfold ProductEffectConditionBridgeGeneralization.generalizedProductEffectCondition at hHi ⊢
  exact effectLowerBoundPredicate_mono thresholdLo thresholdHi hThreshold _ hHi

/--
Generalized typed-side upper-bound effect conditions are monotone under
threshold relaxation.
-/
theorem generalized_typedEffectUpperBoundCondition_mono
    {n d : Nat}
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (typedScore : Typed.TypedState n d → Int)
    (x : ProductTypedState n d)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductEffectBoundBridgeSpecialization.generalizedTypedEffectUpperBoundCondition
        typedUpdate typedScore x thresholdLo →
    ProductEffectBoundBridgeSpecialization.generalizedTypedEffectUpperBoundCondition
        typedUpdate typedScore x thresholdHi := by
  intro hLo
  unfold ProductEffectBoundBridgeSpecialization.generalizedTypedEffectUpperBoundCondition at hLo ⊢
  unfold ProductEffectConditionBridgeGeneralization.generalizedTypedEffectCondition at hLo ⊢
  exact effectUpperBoundPredicate_mono thresholdLo thresholdHi hThreshold _ hLo

/--
Generalized product-side upper-bound effect conditions are monotone under
threshold relaxation.
-/
theorem generalized_productEffectUpperBoundCondition_mono
    {n d : Nat}
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (productScore : ProductTypedState n d → Int)
    (x : ProductTypedState n d)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductEffectBoundBridgeSpecialization.generalizedProductEffectUpperBoundCondition
        productUpdate productScore x thresholdLo →
    ProductEffectBoundBridgeSpecialization.generalizedProductEffectUpperBoundCondition
        productUpdate productScore x thresholdHi := by
  intro hLo
  unfold ProductEffectBoundBridgeSpecialization.generalizedProductEffectUpperBoundCondition at hLo ⊢
  unfold ProductEffectConditionBridgeGeneralization.generalizedProductEffectCondition at hLo ⊢
  exact effectUpperBoundPredicate_mono thresholdLo thresholdHi hThreshold _ hLo

/--
Restricted typed-side lower-bound ledger-effect conditions are monotone under
threshold relaxation.
-/
theorem restricted_typedLedgerEffectLowerBoundCondition_mono
    (p : ProductRestrictedParams)
    (x : p.State)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectLowerBoundCondition
        p x thresholdHi →
    ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectLowerBoundCondition
        p x thresholdLo := by
  intro hHi
  unfold ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectLowerBoundCondition at hHi ⊢
  unfold ProductRestrictedEffectConditionBridgeRecovery.restrictedTypedLedgerEffectCondition at hHi ⊢
  exact effectLowerBoundPredicate_mono thresholdLo thresholdHi hThreshold _ hHi

/--
Restricted product-side lower-bound ledger-effect conditions are monotone under
threshold relaxation.
-/
theorem restricted_productLedgerEffectLowerBoundCondition_mono
    (p : ProductRestrictedParams)
    (x : p.State)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectLowerBoundCondition
        p x thresholdHi →
    ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectLowerBoundCondition
        p x thresholdLo := by
  intro hHi
  unfold ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectLowerBoundCondition at hHi ⊢
  unfold ProductRestrictedEffectConditionBridgeRecovery.restrictedProductLedgerEffectCondition at hHi ⊢
  exact effectLowerBoundPredicate_mono thresholdLo thresholdHi hThreshold _ hHi

/--
Restricted typed-side upper-bound ledger-effect conditions are monotone under
threshold relaxation.
-/
theorem restricted_typedLedgerEffectUpperBoundCondition_mono
    (p : ProductRestrictedParams)
    (x : p.State)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectUpperBoundCondition
        p x thresholdLo →
    ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectUpperBoundCondition
        p x thresholdHi := by
  intro hLo
  unfold ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectUpperBoundCondition at hLo ⊢
  unfold ProductRestrictedEffectConditionBridgeRecovery.restrictedTypedLedgerEffectCondition at hLo ⊢
  exact effectUpperBoundPredicate_mono thresholdLo thresholdHi hThreshold _ hLo

/--
Restricted product-side upper-bound ledger-effect conditions are monotone under
threshold relaxation.
-/
theorem restricted_productLedgerEffectUpperBoundCondition_mono
    (p : ProductRestrictedParams)
    (x : p.State)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectUpperBoundCondition
        p x thresholdLo →
    ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectUpperBoundCondition
        p x thresholdHi := by
  intro hLo
  unfold ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectUpperBoundCondition at hLo ⊢
  unfold ProductRestrictedEffectConditionBridgeRecovery.restrictedProductLedgerEffectCondition at hLo ⊢
  exact effectUpperBoundPredicate_mono thresholdLo thresholdHi hThreshold _ hLo

/--
Transport plus lower-bound threshold relaxation:
a product-side high-threshold lower-bound condition implies the typed-side
low-threshold lower-bound condition.
-/
theorem generalized_productLowerBound_to_typedLowerBound_relaxed_transport
    {n d : Nat}
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (productScore : ProductTypedState n d → Int)
    (typedScore : Typed.TypedState n d → Int)
    (x : ProductTypedState n d)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hUpdate :
      ProductStateTransport.productToTyped (productUpdate x)
        =
      typedUpdate (ProductStateTransport.productToTyped x))
    (hBase :
      typedScore (ProductStateTransport.productToTyped x)
        =
      productScore x)
    (hUpdated :
      typedScore (ProductStateTransport.productToTyped (productUpdate x))
        =
      productScore (productUpdate x)) :
    ProductEffectBoundBridgeSpecialization.generalizedProductEffectLowerBoundCondition
        productUpdate productScore x thresholdHi →
    ProductEffectBoundBridgeSpecialization.generalizedTypedEffectLowerBoundCondition
        typedUpdate typedScore x thresholdLo := by
  intro hProductHi
  have hTransport :=
    ProductEffectBoundBridgeSpecialization.generalized_effectLowerBoundCondition_transport
      productUpdate typedUpdate productScore typedScore x thresholdHi
      hUpdate hBase hUpdated
  have hTypedHi :
      ProductEffectBoundBridgeSpecialization.generalizedTypedEffectLowerBoundCondition
        typedUpdate typedScore x thresholdHi := by
    exact hTransport.mpr hProductHi
  exact
    generalized_typedEffectLowerBoundCondition_mono
      typedUpdate typedScore x thresholdLo thresholdHi hThreshold hTypedHi

/--
Transport plus lower-bound threshold relaxation:
a typed-side high-threshold lower-bound condition implies the product-side
low-threshold lower-bound condition.
-/
theorem generalized_typedLowerBound_to_productLowerBound_relaxed_transport
    {n d : Nat}
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (productScore : ProductTypedState n d → Int)
    (typedScore : Typed.TypedState n d → Int)
    (x : ProductTypedState n d)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hUpdate :
      ProductStateTransport.productToTyped (productUpdate x)
        =
      typedUpdate (ProductStateTransport.productToTyped x))
    (hBase :
      typedScore (ProductStateTransport.productToTyped x)
        =
      productScore x)
    (hUpdated :
      typedScore (ProductStateTransport.productToTyped (productUpdate x))
        =
      productScore (productUpdate x)) :
    ProductEffectBoundBridgeSpecialization.generalizedTypedEffectLowerBoundCondition
        typedUpdate typedScore x thresholdHi →
    ProductEffectBoundBridgeSpecialization.generalizedProductEffectLowerBoundCondition
        productUpdate productScore x thresholdLo := by
  intro hTypedHi
  have hTransport :=
    ProductEffectBoundBridgeSpecialization.generalized_effectLowerBoundCondition_transport
      productUpdate typedUpdate productScore typedScore x thresholdHi
      hUpdate hBase hUpdated
  have hProductHi :
      ProductEffectBoundBridgeSpecialization.generalizedProductEffectLowerBoundCondition
        productUpdate productScore x thresholdHi := by
    exact hTransport.mp hTypedHi
  exact
    generalized_productEffectLowerBoundCondition_mono
      productUpdate productScore x thresholdLo thresholdHi hThreshold hProductHi

/--
Transport plus upper-bound threshold relaxation:
a product-side low-threshold upper-bound condition implies the typed-side
high-threshold upper-bound condition.
-/
theorem generalized_productUpperBound_to_typedUpperBound_relaxed_transport
    {n d : Nat}
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (productScore : ProductTypedState n d → Int)
    (typedScore : Typed.TypedState n d → Int)
    (x : ProductTypedState n d)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hUpdate :
      ProductStateTransport.productToTyped (productUpdate x)
        =
      typedUpdate (ProductStateTransport.productToTyped x))
    (hBase :
      typedScore (ProductStateTransport.productToTyped x)
        =
      productScore x)
    (hUpdated :
      typedScore (ProductStateTransport.productToTyped (productUpdate x))
        =
      productScore (productUpdate x)) :
    ProductEffectBoundBridgeSpecialization.generalizedProductEffectUpperBoundCondition
        productUpdate productScore x thresholdLo →
    ProductEffectBoundBridgeSpecialization.generalizedTypedEffectUpperBoundCondition
        typedUpdate typedScore x thresholdHi := by
  intro hProductLo
  have hTransport :=
    ProductEffectBoundBridgeSpecialization.generalized_effectUpperBoundCondition_transport
      productUpdate typedUpdate productScore typedScore x thresholdLo
      hUpdate hBase hUpdated
  have hTypedLo :
      ProductEffectBoundBridgeSpecialization.generalizedTypedEffectUpperBoundCondition
        typedUpdate typedScore x thresholdLo := by
    exact hTransport.mpr hProductLo
  exact
    generalized_typedEffectUpperBoundCondition_mono
      typedUpdate typedScore x thresholdLo thresholdHi hThreshold hTypedLo

/--
Transport plus upper-bound threshold relaxation:
a typed-side low-threshold upper-bound condition implies the product-side
high-threshold upper-bound condition.
-/
theorem generalized_typedUpperBound_to_productUpperBound_relaxed_transport
    {n d : Nat}
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (productScore : ProductTypedState n d → Int)
    (typedScore : Typed.TypedState n d → Int)
    (x : ProductTypedState n d)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hUpdate :
      ProductStateTransport.productToTyped (productUpdate x)
        =
      typedUpdate (ProductStateTransport.productToTyped x))
    (hBase :
      typedScore (ProductStateTransport.productToTyped x)
        =
      productScore x)
    (hUpdated :
      typedScore (ProductStateTransport.productToTyped (productUpdate x))
        =
      productScore (productUpdate x)) :
    ProductEffectBoundBridgeSpecialization.generalizedTypedEffectUpperBoundCondition
        typedUpdate typedScore x thresholdLo →
    ProductEffectBoundBridgeSpecialization.generalizedProductEffectUpperBoundCondition
        productUpdate productScore x thresholdHi := by
  intro hTypedLo
  have hTransport :=
    ProductEffectBoundBridgeSpecialization.generalized_effectUpperBoundCondition_transport
      productUpdate typedUpdate productScore typedScore x thresholdLo
      hUpdate hBase hUpdated
  have hProductLo :
      ProductEffectBoundBridgeSpecialization.generalizedProductEffectUpperBoundCondition
        productUpdate productScore x thresholdLo := by
    exact hTransport.mp hTypedLo
  exact
    generalized_productEffectUpperBoundCondition_mono
      productUpdate productScore x thresholdLo thresholdHi hThreshold hProductLo

/--
Restricted transport plus lower-bound threshold relaxation:
a product-side high-threshold lower-bound ledger-effect condition implies the
typed-side low-threshold condition.
-/
theorem restricted_productLowerBound_to_typedLowerBound_relaxed_transport
    (p : ProductRestrictedParams)
    (x : p.State)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectLowerBoundCondition
        p x thresholdHi →
    ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectLowerBoundCondition
        p x thresholdLo := by
  intro hProductHi
  have hTransport :=
    ProductEffectBoundBridgeSpecialization.restricted_ledgerEffectLowerBoundCondition_transport
      p x thresholdHi
  have hTypedHi :
      ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectLowerBoundCondition
        p x thresholdHi := by
    exact hTransport.mpr hProductHi
  exact
    restricted_typedLedgerEffectLowerBoundCondition_mono
      p x thresholdLo thresholdHi hThreshold hTypedHi

/--
Restricted transport plus lower-bound threshold relaxation:
a typed-side high-threshold lower-bound ledger-effect condition implies the
product-side low-threshold condition.
-/
theorem restricted_typedLowerBound_to_productLowerBound_relaxed_transport
    (p : ProductRestrictedParams)
    (x : p.State)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectLowerBoundCondition
        p x thresholdHi →
    ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectLowerBoundCondition
        p x thresholdLo := by
  intro hTypedHi
  have hTransport :=
    ProductEffectBoundBridgeSpecialization.restricted_ledgerEffectLowerBoundCondition_transport
      p x thresholdHi
  have hProductHi :
      ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectLowerBoundCondition
        p x thresholdHi := by
    exact hTransport.mp hTypedHi
  exact
    restricted_productLedgerEffectLowerBoundCondition_mono
      p x thresholdLo thresholdHi hThreshold hProductHi

/--
Restricted transport plus upper-bound threshold relaxation:
a product-side low-threshold upper-bound ledger-effect condition implies the
typed-side high-threshold condition.
-/
theorem restricted_productUpperBound_to_typedUpperBound_relaxed_transport
    (p : ProductRestrictedParams)
    (x : p.State)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectUpperBoundCondition
        p x thresholdLo →
    ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectUpperBoundCondition
        p x thresholdHi := by
  intro hProductLo
  have hTransport :=
    ProductEffectBoundBridgeSpecialization.restricted_ledgerEffectUpperBoundCondition_transport
      p x thresholdLo
  have hTypedLo :
      ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectUpperBoundCondition
        p x thresholdLo := by
    exact hTransport.mpr hProductLo
  exact
    restricted_typedLedgerEffectUpperBoundCondition_mono
      p x thresholdLo thresholdHi hThreshold hTypedLo

/--
Restricted transport plus upper-bound threshold relaxation:
a typed-side low-threshold upper-bound ledger-effect condition implies the
product-side high-threshold condition.
-/
theorem restricted_typedUpperBound_to_productUpperBound_relaxed_transport
    (p : ProductRestrictedParams)
    (x : p.State)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectUpperBoundCondition
        p x thresholdLo →
    ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectUpperBoundCondition
        p x thresholdHi := by
  intro hTypedLo
  have hTransport :=
    ProductEffectBoundBridgeSpecialization.restricted_ledgerEffectUpperBoundCondition_transport
      p x thresholdLo
  have hProductLo :
      ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectUpperBoundCondition
        p x thresholdLo := by
    exact hTransport.mp hTypedLo
  exact
    restricted_productLedgerEffectUpperBoundCondition_mono
      p x thresholdLo thresholdHi hThreshold hProductLo

/--
Certificate collecting the generalized monotone relaxed transport layer for
effect-bound conditions.
-/
structure GeneralizedEffectBoundMonotoneTransportCertificate
    {n d : Nat}
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (productScore : ProductTypedState n d → Int)
    (typedScore : Typed.TypedState n d → Int)
    (x : ProductTypedState n d)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hUpdate :
      ProductStateTransport.productToTyped (productUpdate x)
        =
      typedUpdate (ProductStateTransport.productToTyped x))
    (hBase :
      typedScore (ProductStateTransport.productToTyped x)
        =
      productScore x)
    (hUpdated :
      typedScore (ProductStateTransport.productToTyped (productUpdate x))
        =
      productScore (productUpdate x)) : Prop where
  productLowerToTypedLower :
    ProductEffectBoundBridgeSpecialization.generalizedProductEffectLowerBoundCondition
        productUpdate productScore x thresholdHi →
    ProductEffectBoundBridgeSpecialization.generalizedTypedEffectLowerBoundCondition
        typedUpdate typedScore x thresholdLo
  typedLowerToProductLower :
    ProductEffectBoundBridgeSpecialization.generalizedTypedEffectLowerBoundCondition
        typedUpdate typedScore x thresholdHi →
    ProductEffectBoundBridgeSpecialization.generalizedProductEffectLowerBoundCondition
        productUpdate productScore x thresholdLo
  productUpperToTypedUpper :
    ProductEffectBoundBridgeSpecialization.generalizedProductEffectUpperBoundCondition
        productUpdate productScore x thresholdLo →
    ProductEffectBoundBridgeSpecialization.generalizedTypedEffectUpperBoundCondition
        typedUpdate typedScore x thresholdHi
  typedUpperToProductUpper :
    ProductEffectBoundBridgeSpecialization.generalizedTypedEffectUpperBoundCondition
        typedUpdate typedScore x thresholdLo →
    ProductEffectBoundBridgeSpecialization.generalizedProductEffectUpperBoundCondition
        productUpdate productScore x thresholdHi

/--
Generalized monotone relaxed transport certificate theorem.
-/
theorem generalizedEffectBoundMonotoneTransport_certificate
    {n d : Nat}
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (productScore : ProductTypedState n d → Int)
    (typedScore : Typed.TypedState n d → Int)
    (x : ProductTypedState n d)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hUpdate :
      ProductStateTransport.productToTyped (productUpdate x)
        =
      typedUpdate (ProductStateTransport.productToTyped x))
    (hBase :
      typedScore (ProductStateTransport.productToTyped x)
        =
      productScore x)
    (hUpdated :
      typedScore (ProductStateTransport.productToTyped (productUpdate x))
        =
      productScore (productUpdate x)) :
    GeneralizedEffectBoundMonotoneTransportCertificate
      productUpdate typedUpdate productScore typedScore x
      thresholdLo thresholdHi hThreshold hUpdate hBase hUpdated := by
  exact {
    productLowerToTypedLower :=
      generalized_productLowerBound_to_typedLowerBound_relaxed_transport
        productUpdate typedUpdate productScore typedScore x
        thresholdLo thresholdHi hThreshold hUpdate hBase hUpdated,
    typedLowerToProductLower :=
      generalized_typedLowerBound_to_productLowerBound_relaxed_transport
        productUpdate typedUpdate productScore typedScore x
        thresholdLo thresholdHi hThreshold hUpdate hBase hUpdated,
    productUpperToTypedUpper :=
      generalized_productUpperBound_to_typedUpperBound_relaxed_transport
        productUpdate typedUpdate productScore typedScore x
        thresholdLo thresholdHi hThreshold hUpdate hBase hUpdated,
    typedUpperToProductUpper :=
      generalized_typedUpperBound_to_productUpperBound_relaxed_transport
        productUpdate typedUpdate productScore typedScore x
        thresholdLo thresholdHi hThreshold hUpdate hBase hUpdated
  }

/--
Certificate collecting the restricted monotone relaxed transport layer for
ledger-effect bound conditions.
-/
structure RestrictedEffectBoundMonotoneTransportCertificate
    (p : ProductRestrictedParams)
    (x : p.State)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) : Prop where
  productLowerToTypedLower :
    ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectLowerBoundCondition
        p x thresholdHi →
    ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectLowerBoundCondition
        p x thresholdLo
  typedLowerToProductLower :
    ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectLowerBoundCondition
        p x thresholdHi →
    ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectLowerBoundCondition
        p x thresholdLo
  productUpperToTypedUpper :
    ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectUpperBoundCondition
        p x thresholdLo →
    ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectUpperBoundCondition
        p x thresholdHi
  typedUpperToProductUpper :
    ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectUpperBoundCondition
        p x thresholdLo →
    ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectUpperBoundCondition
        p x thresholdHi

/--
Restricted monotone relaxed transport certificate theorem.
-/
theorem restrictedEffectBoundMonotoneTransport_certificate
    (p : ProductRestrictedParams)
    (x : p.State)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    RestrictedEffectBoundMonotoneTransportCertificate
      p x thresholdLo thresholdHi hThreshold := by
  exact {
    productLowerToTypedLower :=
      restricted_productLowerBound_to_typedLowerBound_relaxed_transport
        p x thresholdLo thresholdHi hThreshold,
    typedLowerToProductLower :=
      restricted_typedLowerBound_to_productLowerBound_relaxed_transport
        p x thresholdLo thresholdHi hThreshold,
    productUpperToTypedUpper :=
      restricted_productUpperBound_to_typedUpperBound_relaxed_transport
        p x thresholdLo thresholdHi hThreshold,
    typedUpperToProductUpper :=
      restricted_typedUpperBound_to_productUpperBound_relaxed_transport
        p x thresholdLo thresholdHi hThreshold
  }

end ProductEffectBoundConditionMonotonicity

end VFH2
