import VFH2.Product.ProductRestrictedConcreteBridgeAssemblySpecialization
import VFH2.Product.ProductEffectBoundConditionMonotonicity

namespace VFH2

namespace ProductRestrictedParamsBridgeCorePivot

def restrictedParamsSelfBridgeCoreSource
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) : Prop :=
  VFH2.ProductEffectBoundConditionMonotonicity.RestrictedEffectBoundMonotoneTransportCertificate
      p x thresholdLo thresholdHi hThreshold ∧
    VFH2.ProductRestrictedConcreteBridgeAssemblySpecialization.restrictedConcreteSelfBridgeAssemblySource
      fixed effect thresholdLo thresholdHi

def restrictedParamsSelfBridgeCoreTarget
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) : Prop :=
  VFH2.ProductEffectBoundConditionMonotonicity.RestrictedEffectBoundMonotoneTransportCertificate
      p x thresholdLo thresholdHi hThreshold ∧
    VFH2.ProductRestrictedConcreteBridgeAssemblySpecialization.restrictedConcreteSelfBridgeAssemblyTarget
      fixed effect thresholdLo thresholdHi

theorem restrictedParams_selfBridgeCorePivot_theorem
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsSelfBridgeCoreSource
        p x fixed effect thresholdLo thresholdHi hThreshold) :
    restrictedParamsSelfBridgeCoreTarget
      p x fixed effect thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsSelfBridgeCoreSource at hSource
  unfold restrictedParamsSelfBridgeCoreTarget
  exact ⟨
    hSource.1,
    VFH2.ProductRestrictedConcreteBridgeAssemblySpecialization.restricted_selfConcreteThresholdBridgeAssembly_theorem
      fixed effect thresholdLo thresholdHi hThreshold hSource.2
  ⟩

theorem restrictedParams_selfBridgeCorePivot_from_existingRestrictedTransport
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ effect))
    (hUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (effect ≤ thresholdLo)) :
    restrictedParamsSelfBridgeCoreTarget
      p x fixed effect thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsSelfBridgeCoreTarget
  exact ⟨
    VFH2.ProductEffectBoundConditionMonotonicity.restrictedEffectBoundMonotoneTransport_certificate
      p x thresholdLo thresholdHi hThreshold,
    VFH2.ProductRestrictedConcreteBridgeAssemblySpecialization.restricted_selfConcreteThresholdBridgeAssembly_direct_theorem
      fixed effect thresholdLo thresholdHi hThreshold hLowerBridgeStrong hUpperBridgeStrong
  ⟩

theorem restrictedParams_selfBridgeCorePivot_lower_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsSelfBridgeCoreSource
        p x fixed effect thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ effect) := by
  have hTarget :
      restrictedParamsSelfBridgeCoreTarget
        p x fixed effect thresholdLo thresholdHi hThreshold :=
    restrictedParams_selfBridgeCorePivot_theorem
      p x fixed effect thresholdLo thresholdHi hThreshold hSource
  unfold restrictedParamsSelfBridgeCoreTarget at hTarget
  exact hTarget.2.1

theorem restrictedParams_selfBridgeCorePivot_upper_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsSelfBridgeCoreSource
        p x fixed effect thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (effect ≤ thresholdHi) := by
  have hTarget :
      restrictedParamsSelfBridgeCoreTarget
        p x fixed effect thresholdLo thresholdHi hThreshold :=
    restrictedParams_selfBridgeCorePivot_theorem
      p x fixed effect thresholdLo thresholdHi hThreshold hSource
  unfold restrictedParamsSelfBridgeCoreTarget at hTarget
  exact hTarget.2.2

theorem restrictedParams_existingRestrictedTransport_coreCertificate
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    VFH2.ProductEffectBoundConditionMonotonicity.RestrictedEffectBoundMonotoneTransportCertificate
      p x thresholdLo thresholdHi hThreshold := by
  exact VFH2.ProductEffectBoundConditionMonotonicity.restrictedEffectBoundMonotoneTransport_certificate
    p x thresholdLo thresholdHi hThreshold

theorem restrictedParams_selfBridgeCorePivot_direct_lower_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ effect))
    (hUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (effect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ effect) := by
  have hTarget :
      restrictedParamsSelfBridgeCoreTarget
        p x fixed effect thresholdLo thresholdHi hThreshold :=
    restrictedParams_selfBridgeCorePivot_from_existingRestrictedTransport
      p x fixed effect thresholdLo thresholdHi hThreshold
      hLowerBridgeStrong hUpperBridgeStrong
  unfold restrictedParamsSelfBridgeCoreTarget at hTarget
  exact hTarget.2.1

theorem restrictedParams_selfBridgeCorePivot_direct_upper_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ effect))
    (hUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (effect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (effect ≤ thresholdHi) := by
  have hTarget :
      restrictedParamsSelfBridgeCoreTarget
        p x fixed effect thresholdLo thresholdHi hThreshold :=
    restrictedParams_selfBridgeCorePivot_from_existingRestrictedTransport
      p x fixed effect thresholdLo thresholdHi hThreshold
      hLowerBridgeStrong hUpperBridgeStrong
  unfold restrictedParamsSelfBridgeCoreTarget at hTarget
  exact hTarget.2.2

end ProductRestrictedParamsBridgeCorePivot

end VFH2
