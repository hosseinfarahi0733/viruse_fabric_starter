import VFH2.Product.ProductEffectBoundConditionMonotonicity

namespace VFH2

namespace ProductEffectBoundBridgeMonotonicity

theorem genericBridgeTarget_condition_mono
    {fixed conditionStrong conditionWeak : Prop}
    (hCondition : conditionStrong → conditionWeak) :
    ProductBridgeGeneralization.genericBridgeTarget fixed conditionStrong →
    ProductBridgeGeneralization.genericBridgeTarget fixed conditionWeak := by
  intro hBridge
  unfold ProductBridgeGeneralization.genericBridgeTarget at hBridge ⊢
  exact ⟨hBridge.1, hCondition hBridge.2⟩

theorem genericLowerBoundBridgeTarget_mono
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ effect) →
    ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdLo ≤ effect) := by
  exact genericBridgeTarget_condition_mono
    (fixed := fixed)
    (conditionStrong := thresholdHi ≤ effect)
    (conditionWeak := thresholdLo ≤ effect)
    (fun hStrong => Int.le_trans hThreshold hStrong)

theorem genericUpperBoundBridgeTarget_mono
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed (effect ≤ thresholdLo) →
    ProductBridgeGeneralization.genericBridgeTarget fixed (effect ≤ thresholdHi) := by
  exact genericBridgeTarget_condition_mono
    (fixed := fixed)
    (conditionStrong := effect ≤ thresholdLo)
    (conditionWeak := effect ≤ thresholdHi)
    (fun hStrong => Int.le_trans hStrong hThreshold)

theorem generalized_typedLowerBoundBridgeTarget_mono
    (fixed : Prop)
    (typedEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ typedEffect) →
    ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdLo ≤ typedEffect) := by
  exact genericLowerBoundBridgeTarget_mono fixed typedEffect thresholdLo thresholdHi hThreshold

theorem generalized_productLowerBoundBridgeTarget_mono
    (fixed : Prop)
    (productEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ productEffect) →
    ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdLo ≤ productEffect) := by
  exact genericLowerBoundBridgeTarget_mono fixed productEffect thresholdLo thresholdHi hThreshold

theorem generalized_typedUpperBoundBridgeTarget_mono
    (fixed : Prop)
    (typedEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed (typedEffect ≤ thresholdLo) →
    ProductBridgeGeneralization.genericBridgeTarget fixed (typedEffect ≤ thresholdHi) := by
  exact genericUpperBoundBridgeTarget_mono fixed typedEffect thresholdLo thresholdHi hThreshold

theorem generalized_productUpperBoundBridgeTarget_mono
    (fixed : Prop)
    (productEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed (productEffect ≤ thresholdLo) →
    ProductBridgeGeneralization.genericBridgeTarget fixed (productEffect ≤ thresholdHi) := by
  exact genericUpperBoundBridgeTarget_mono fixed productEffect thresholdLo thresholdHi hThreshold

theorem restricted_typedLowerBoundBridgeTarget_mono
    (fixed : Prop)
    (typedLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ typedLedgerEffect) →
    ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdLo ≤ typedLedgerEffect) := by
  exact genericLowerBoundBridgeTarget_mono fixed typedLedgerEffect thresholdLo thresholdHi hThreshold

theorem restricted_productLowerBoundBridgeTarget_mono
    (fixed : Prop)
    (productLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ productLedgerEffect) →
    ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdLo ≤ productLedgerEffect) := by
  exact genericLowerBoundBridgeTarget_mono fixed productLedgerEffect thresholdLo thresholdHi hThreshold

theorem restricted_typedUpperBoundBridgeTarget_mono
    (fixed : Prop)
    (typedLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed (typedLedgerEffect ≤ thresholdLo) →
    ProductBridgeGeneralization.genericBridgeTarget fixed (typedLedgerEffect ≤ thresholdHi) := by
  exact genericUpperBoundBridgeTarget_mono fixed typedLedgerEffect thresholdLo thresholdHi hThreshold

theorem restricted_productUpperBoundBridgeTarget_mono
    (fixed : Prop)
    (productLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed (productLedgerEffect ≤ thresholdLo) →
    ProductBridgeGeneralization.genericBridgeTarget fixed (productLedgerEffect ≤ thresholdHi) := by
  exact genericUpperBoundBridgeTarget_mono fixed productLedgerEffect thresholdLo thresholdHi hThreshold

end ProductEffectBoundBridgeMonotonicity

end VFH2
