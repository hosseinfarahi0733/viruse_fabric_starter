# VF-H2 Proof Gates from v15 onward

This file is intentionally operational. It is not a manuscript note and not an audit artifact.

## Hard pivot rule

From `v15.0.0` onward, a milestone is not accepted if its new theorem layer is generic-only.

A theorem layer is generic-only if it only talks about:

```text
fixed : Prop
effect : Int
genericBridgeTarget
thresholdLo
thresholdHi
```

without also mentioning at least one core project object.

## Required core tokens

Every new proof milestone after `v14.5.0` must mention at least one of these in the theorem statement, and preferably more than one:

```text
ProductRestrictedParams
p.State
productUpdate
productScore
typedScore
productToTyped
RestrictedEffectBoundMonotoneTransportCertificate
restrictedEffectBoundMonotoneTransport_certificate
```

## Certificate-only ban

A milestone is rejected if its strongest theorem only proves a certificate proposition and does not connect that certificate to another proof target.

Allowed:

```text
restricted certificate + bridge target
restricted params + state + closure target
restricted params + update/score + transported bound
```

Rejected:

```text
exact existing_certificate
```

unless it is only a small helper theorem and not the milestone claim.

## Wrapper ban

A milestone is rejected if it merely renames or re-pairs earlier theorem outputs without reducing assumptions or connecting to a more concrete restricted scaffold.

## Accepted milestone test

A milestone must satisfy at least one of these:

```text
1. It removes assumptions compared with the previous layer.
2. It introduces ProductRestrictedParams and p.State into the main theorem statement.
3. It connects a ProductRestrictedParams theorem to a bridge/transport/recovery target.
4. It moves from genericBridgeTarget-only statements toward update/score/state-level statements.
```

## Current pivot

`v15.0.0` is the pivot away from generic-only v14 scaffolding.

Its target is:

```text
ProductRestrictedParams + p.State
+ existing restricted effect-bound monotone transport certificate
+ v14.5 self bridge assembly target
```

This is not the final VF-H2 theorem, but it forces the chain back toward the restricted product/state layer.
# VF-H2 Proof Gates v15.1 Addendum

`v15.1.0` tightens the pivot rule.

After `v15.0.0`, a new milestone should preferably move beyond:

```text
ProductRestrictedParams
p.State
```

toward update/score/state transport objects.

## v15.1 accepted direction

The main theorem layer must mention these tokens:

```text
ProductRestrictedParams
p.State
productUpdate
productScore
typedUpdate
typedScore
productToTyped
RestrictedEffectBoundMonotoneTransportCertificate
```

## Rejection rule

A milestone is rejected if it only preserves a bridge target while ignoring update-score alignment.

## Safe claim pattern

Use:

```text
connects ProductRestrictedParams/p.State with productUpdate/productScore and
typedUpdate/typedScore alignment over ProductStateTransport.productToTyped,
while preserving the restricted params bridge core target.
```

Do not claim full VF-H2, unrestricted proof, empirical validation, or biological validation.
# VF-H2 Proof Gates v15.2 Addendum

`v15.2.0` tightens the update-score rule.

A new theorem layer must not merely preserve a prebuilt alignment object.
It should expose raw update-score transport equalities in the source/statement.

## Required direction

The theorem layer should mention:

```text
productUpdate
productScore
typedUpdate
typedScore
ProductStateTransport.productToTyped x
ProductStateTransport.productToTyped (productUpdate x)
RestrictedEffectBoundMonotoneTransportCertificate
```

## Main accepted shape

```text
raw update-score transport certificate
+ strong lower/upper bridge inputs
+ thresholdLo ≤ thresholdHi
→ bridge target
+ preserved raw update-score transport certificate
```

## Rejected shape

```text
alignment source → alignment target
```

if it never exposes raw transport equalities.
