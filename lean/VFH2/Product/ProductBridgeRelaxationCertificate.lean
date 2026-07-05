import VFH2.Product.ProductEffectBoundBridgeMonotonicity

namespace VFH2

namespace ProductBridgeRelaxationCertificate

structure BridgeRelaxationCertificate : Prop where
  genericConditionMono :
    ∀ {fixed conditionStrong conditionWeak : Prop},
      (conditionStrong → conditionWeak) →
      ProductBridgeGeneralization.genericBridgeTarget fixed conditionStrong →
      ProductBridgeGeneralization.genericBridgeTarget fixed conditionWeak
  genericLowerMono :
    ∀ (fixed : Prop)
      (effect thresholdLo thresholdHi : Int),
      thresholdLo ≤ thresholdHi →
      ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ effect) →
      ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdLo ≤ effect)
  genericUpperMono :
    ∀ (fixed : Prop)
      (effect thresholdLo thresholdHi : Int),
      thresholdLo ≤ thresholdHi →
      ProductBridgeGeneralization.genericBridgeTarget fixed (effect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget fixed (effect ≤ thresholdHi)
  generalizedTypedLowerMono :
    ∀ (fixed : Prop)
      (typedEffect thresholdLo thresholdHi : Int),
      thresholdLo ≤ thresholdHi →
      ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ typedEffect) →
      ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdLo ≤ typedEffect)
  generalizedProductLowerMono :
    ∀ (fixed : Prop)
      (productEffect thresholdLo thresholdHi : Int),
      thresholdLo ≤ thresholdHi →
      ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ productEffect) →
      ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdLo ≤ productEffect)
  generalizedTypedUpperMono :
    ∀ (fixed : Prop)
      (typedEffect thresholdLo thresholdHi : Int),
      thresholdLo ≤ thresholdHi →
      ProductBridgeGeneralization.genericBridgeTarget fixed (typedEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget fixed (typedEffect ≤ thresholdHi)
  generalizedProductUpperMono :
    ∀ (fixed : Prop)
      (productEffect thresholdLo thresholdHi : Int),
      thresholdLo ≤ thresholdHi →
      ProductBridgeGeneralization.genericBridgeTarget fixed (productEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget fixed (productEffect ≤ thresholdHi)
  restrictedTypedLowerMono :
    ∀ (fixed : Prop)
      (typedLedgerEffect thresholdLo thresholdHi : Int),
      thresholdLo ≤ thresholdHi →
      ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ typedLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdLo ≤ typedLedgerEffect)
  restrictedProductLowerMono :
    ∀ (fixed : Prop)
      (productLedgerEffect thresholdLo thresholdHi : Int),
      thresholdLo ≤ thresholdHi →
      ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ productLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdLo ≤ productLedgerEffect)
  restrictedTypedUpperMono :
    ∀ (fixed : Prop)
      (typedLedgerEffect thresholdLo thresholdHi : Int),
      thresholdLo ≤ thresholdHi →
      ProductBridgeGeneralization.genericBridgeTarget fixed (typedLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget fixed (typedLedgerEffect ≤ thresholdHi)
  restrictedProductUpperMono :
    ∀ (fixed : Prop)
      (productLedgerEffect thresholdLo thresholdHi : Int),
      thresholdLo ≤ thresholdHi →
      ProductBridgeGeneralization.genericBridgeTarget fixed (productLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget fixed (productLedgerEffect ≤ thresholdHi)

theorem genericConditionMono_certificate :
    ∀ {fixed conditionStrong conditionWeak : Prop},
      (conditionStrong → conditionWeak) →
      ProductBridgeGeneralization.genericBridgeTarget fixed conditionStrong →
      ProductBridgeGeneralization.genericBridgeTarget fixed conditionWeak := by
  intro fixed conditionStrong conditionWeak hCondition
  exact ProductEffectBoundBridgeMonotonicity.genericBridgeTarget_condition_mono
    (fixed := fixed)
    (conditionStrong := conditionStrong)
    (conditionWeak := conditionWeak)
    hCondition

theorem genericLowerMono_certificate :
    ∀ (fixed : Prop)
      (effect thresholdLo thresholdHi : Int),
      thresholdLo ≤ thresholdHi →
      ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ effect) →
      ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdLo ≤ effect) := by
  intro fixed effect thresholdLo thresholdHi hThreshold
  exact ProductEffectBoundBridgeMonotonicity.genericLowerBoundBridgeTarget_mono
    fixed effect thresholdLo thresholdHi hThreshold

theorem genericUpperMono_certificate :
    ∀ (fixed : Prop)
      (effect thresholdLo thresholdHi : Int),
      thresholdLo ≤ thresholdHi →
      ProductBridgeGeneralization.genericBridgeTarget fixed (effect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget fixed (effect ≤ thresholdHi) := by
  intro fixed effect thresholdLo thresholdHi hThreshold
  exact ProductEffectBoundBridgeMonotonicity.genericUpperBoundBridgeTarget_mono
    fixed effect thresholdLo thresholdHi hThreshold

theorem bridgeRelaxation_certificate :
    BridgeRelaxationCertificate := by
  constructor
  · exact genericConditionMono_certificate
  · exact genericLowerMono_certificate
  · exact genericUpperMono_certificate
  · intro fixed typedEffect thresholdLo thresholdHi hThreshold
    exact ProductEffectBoundBridgeMonotonicity.generalized_typedLowerBoundBridgeTarget_mono
      fixed typedEffect thresholdLo thresholdHi hThreshold
  · intro fixed productEffect thresholdLo thresholdHi hThreshold
    exact ProductEffectBoundBridgeMonotonicity.generalized_productLowerBoundBridgeTarget_mono
      fixed productEffect thresholdLo thresholdHi hThreshold
  · intro fixed typedEffect thresholdLo thresholdHi hThreshold
    exact ProductEffectBoundBridgeMonotonicity.generalized_typedUpperBoundBridgeTarget_mono
      fixed typedEffect thresholdLo thresholdHi hThreshold
  · intro fixed productEffect thresholdLo thresholdHi hThreshold
    exact ProductEffectBoundBridgeMonotonicity.generalized_productUpperBoundBridgeTarget_mono
      fixed productEffect thresholdLo thresholdHi hThreshold
  · intro fixed typedLedgerEffect thresholdLo thresholdHi hThreshold
    exact ProductEffectBoundBridgeMonotonicity.restricted_typedLowerBoundBridgeTarget_mono
      fixed typedLedgerEffect thresholdLo thresholdHi hThreshold
  · intro fixed productLedgerEffect thresholdLo thresholdHi hThreshold
    exact ProductEffectBoundBridgeMonotonicity.restricted_productLowerBoundBridgeTarget_mono
      fixed productLedgerEffect thresholdLo thresholdHi hThreshold
  · intro fixed typedLedgerEffect thresholdLo thresholdHi hThreshold
    exact ProductEffectBoundBridgeMonotonicity.restricted_typedUpperBoundBridgeTarget_mono
      fixed typedLedgerEffect thresholdLo thresholdHi hThreshold
  · intro fixed productLedgerEffect thresholdLo thresholdHi hThreshold
    exact ProductEffectBoundBridgeMonotonicity.restricted_productUpperBoundBridgeTarget_mono
      fixed productLedgerEffect thresholdLo thresholdHi hThreshold

theorem bridgeRelaxation_genericConditionMono :
    ∀ {fixed conditionStrong conditionWeak : Prop},
      (conditionStrong → conditionWeak) →
      ProductBridgeGeneralization.genericBridgeTarget fixed conditionStrong →
      ProductBridgeGeneralization.genericBridgeTarget fixed conditionWeak :=
  bridgeRelaxation_certificate.genericConditionMono

theorem bridgeRelaxation_genericLowerMono :
    ∀ (fixed : Prop)
      (effect thresholdLo thresholdHi : Int),
      thresholdLo ≤ thresholdHi →
      ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ effect) →
      ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdLo ≤ effect) :=
  bridgeRelaxation_certificate.genericLowerMono

theorem bridgeRelaxation_genericUpperMono :
    ∀ (fixed : Prop)
      (effect thresholdLo thresholdHi : Int),
      thresholdLo ≤ thresholdHi →
      ProductBridgeGeneralization.genericBridgeTarget fixed (effect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget fixed (effect ≤ thresholdHi) :=
  bridgeRelaxation_certificate.genericUpperMono

theorem bridgeRelaxation_restrictedProductLowerMono :
    ∀ (fixed : Prop)
      (productLedgerEffect thresholdLo thresholdHi : Int),
      thresholdLo ≤ thresholdHi →
      ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ productLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdLo ≤ productLedgerEffect) :=
  bridgeRelaxation_certificate.restrictedProductLowerMono

theorem bridgeRelaxation_restrictedProductUpperMono :
    ∀ (fixed : Prop)
      (productLedgerEffect thresholdLo thresholdHi : Int),
      thresholdLo ≤ thresholdHi →
      ProductBridgeGeneralization.genericBridgeTarget fixed (productLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget fixed (productLedgerEffect ≤ thresholdHi) :=
  bridgeRelaxation_certificate.restrictedProductUpperMono

end ProductBridgeRelaxationCertificate

end VFH2
