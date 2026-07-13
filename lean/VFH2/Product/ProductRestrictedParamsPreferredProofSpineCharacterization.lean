import VFH2.Product.ProductRestrictedParamsPreferredAfterOneUpdateProofSpine
import VFH2.Product.ProductRestrictedParamsCurrentBestMainTheorem

/-!
# VF-H2 Preferred Restricted Proof-Spine Characterization

This file characterizes the actual restricted proof-spine target over the entire
preferred restricted state space.

Scientific result:
- Parameters enter only through the preferred front door.
- An inactive coordinate is derived from preferred active noncoverage.
- The associated inactive-coordinate score, inactive-insensitivity, and natural
  score bounds are derived.
- For every state, not merely states lying on an update trajectory, the current
  restricted proof-spine target holds exactly when the state belongs to
  `ProductFixedSet`.

This strictly generalizes the temporal preferred result: the characterization is
pointwise over the complete state space and does not mention trajectory time.

Architecture:
- Raw erase-construction declarations are not used.
- Compatibility declarations are not used.
- No new trajectory predicate or certificate wrapper is introduced.

Boundary:
- The result remains restricted to `ProductRestrictedParams`.
- It does not prove unrestricted TTP-VF-H2-004 or the full Viruse Fabric theory.
- It is not empirical or biological validation.
-/

namespace VFH2

namespace ProductRestrictedParamsPreferredProofSpineCharacterization

/--
For every state of preferred restricted parameters, the current restricted
proof-spine target is equivalent to semantic fixedness.

All score-side assumptions and the inactive coordinate are derived internally.
-/
theorem restrictedParams_preferredParams_restrictedProofSpineTarget_iff_fixedSet
    (n d : Nat)
    (missing : ProductIndex d)
    (y :
      (ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing).State) :
    let p :=
      ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing
    let cert :=
      ProductRestrictedParamsPreferredAfterOneUpdateProofSpine.preferredInactiveIndexCertificate
        n d missing
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
        p
        y
        (productUpdateState p)
        (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
          p cert.i)
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          y
          (productUpdateState p))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          y
          (productUpdateState p)
          (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
            p cert.i))
        (ProductFixedSet p y)
        0
        (Int.ofNat p.n)
        (Int.natCast_nonneg p.n)
      ↔
    ProductFixedSet p y := by
  dsimp only

  let p :=
    ProductRestrictedParamsPreferredFrontDoor.preferredParams
      n d missing

  let cert :=
    ProductRestrictedParamsPreferredAfterOneUpdateProofSpine.preferredInactiveIndexCertificate
      n d missing

  change
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
        p
        y
        (productUpdateState p)
        (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
          p cert.i)
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          y
          (productUpdateState p))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          y
          (productUpdateState p)
          (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
            p cert.i))
        (ProductFixedSet p y)
        0
        (Int.ofNat p.n)
        (Int.natCast_nonneg p.n)
      ↔
    ProductFixedSet p y

  constructor

  · intro hTarget

    have hBaseTarget :
        ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
          p
          y
          (productUpdateState p)
          (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
            p cert.i)
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
            p
            y
            (productUpdateState p))
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
            p
            y
            (productUpdateState p)
            (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
              p cert.i))
          (ProductFixedSet p y)
          0
          (Int.ofNat p.n)
          (Int.natCast_nonneg p.n) :=
      ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParams_policyEndToEnd_baseTarget_projection
        p
        y
        (productUpdateState p)
        (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
          p cert.i)
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          y
          (productUpdateState p))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          y
          (productUpdateState p)
          (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
            p cert.i))
        (ProductFixedSet p y)
        0
        (Int.ofNat p.n)
        (Int.natCast_nonneg p.n)
        hTarget

    have hWindow :
        ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindow
          p
          y
          (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
            p cert.i)
          (ProductFixedSet p y)
          0
          (Int.ofNat p.n) :=
      ProductRestrictedParamsScoreWindow.restrictedParams_baseScoreWindowTarget_window_projection
        p
        y
        (productUpdateState p)
        (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
          p cert.i)
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          y
          (productUpdateState p))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          y
          (productUpdateState p)
          (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
            p cert.i))
        (ProductFixedSet p y)
        0
        (Int.ofNat p.n)
        (Int.natCast_nonneg p.n)
        hBaseTarget

    have hLower :
        ProductBridgeGeneralization.genericBridgeTarget
          (ProductFixedSet p y)
          (0 ≤
            ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
              p cert.i y) :=
      ProductRestrictedParamsScoreWindow.restrictedParams_baseScoreWindow_lower_projection
        p
        y
        (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
          p cert.i)
        (ProductFixedSet p y)
        0
        (Int.ofNat p.n)
        hWindow

    unfold ProductBridgeGeneralization.genericBridgeTarget at hLower

    exact hLower.1

  · intro hFixed

    have hInactive :
        ProductRestrictedParamsActiveInsensitiveScore.productScoreInactiveInsensitive
          p
          (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
            p cert.i) :=
      ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore_inactiveInsensitive_of_inactive_index
        p
        cert.i
        cert.inactive

    have hRange :
        ProductRestrictedParamsFixedStateConstruction.ScoreRangeCertificate
          p
          (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
            p cert.i)
          0
          (Int.ofNat p.n) :=
      ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore_range_zero_top
        p
        cert.i

    exact
      ProductRestrictedParamsCurrentBestMainTheorem.restrictedParams_currentBestMainTheorem
        p
        y
        (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
          p cert.i)
        0
        (Int.ofNat p.n)
        (Int.natCast_nonneg p.n)
        hInactive
        hFixed
        (hRange.lower y)
        (hRange.upper y)

end ProductRestrictedParamsPreferredProofSpineCharacterization

end VFH2
