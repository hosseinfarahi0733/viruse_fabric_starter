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
# VF-H2 Proof Gates v15.3 Addendum

`v15.3.0` introduces the update-score bound rule.

The new theorem layer must derive explicit lower/upper projected bound targets from raw update-score transport equalities.

## Required shape

The main accepted theorem shape is:

```text
raw update-score equalities
+ strong lower/upper bridge inputs
+ ProductRestrictedParams / p.State
+ productUpdate / productScore / typedUpdate / typedScore / productToTyped
+ thresholdLo ≤ thresholdHi
→ lower projected bound target
→ upper projected bound target
→ restricted certificate projection
```

## Rejected shape

The milestone is rejected if it only returns a generic bridge target bundle without projection theorems for lower and upper bounds.
# VF-H2 Proof Gates v15.4 Addendum

`v15.4.0` introduces the score-effect binding rule.

The new theorem layer must not leave:

```text
effect : Int
```

floating without relation to the actual score.

## Required direction

A milestone must consume at least one explicit score-effect binding:

```text
effect = productScore x
```

or:

```text
effect = productScore (productUpdate x)
```

and produce a bound target over the score itself:

```text
thresholdLo ≤ productScore x
productScore x ≤ thresholdHi
thresholdLo ≤ productScore (productUpdate x)
productScore (productUpdate x) ≤ thresholdHi
```

## Rejected shape

The milestone is rejected if it only proves bounds over:

```text
effect
```

without moving those bounds to `productScore`.
# VF-H2 Proof Gates v15.5 Addendum

`v15.5.0` introduces the score-window rule.

The new theorem layer must combine separate score lower/upper bounds into explicit score windows.

## Required direction

The milestone must prove window targets over:

```text
productScore x
productScore (productUpdate x)
```

not merely over:

```text
effect
```

## Accepted shape

```text
thresholdLo ≤ productScore x ∧ productScore x ≤ thresholdHi

thresholdLo ≤ productScore (productUpdate x) ∧
productScore (productUpdate x) ≤ thresholdHi
```

The theorem may use separate base and updated effects, but the final target must be score-level.

## Rejected shape

The milestone is rejected if the final target still leaves score-level lower/upper bounds separated without a window theorem.
# VF-H2 Proof Gates v15.6 Addendum

`v15.6.0` introduces the score-window preservation rule.

The new theorem layer must use an existing base score-window target and produce an updated score-window target under raw update-score transport and updated score-effect binding.

## Required direction

The milestone must prove:

```text
base score-window target
+ raw update-score transport certificate
+ updatedEffect = productScore (productUpdate x)
+ updated strong bridge inputs
→ base and updated score-window target
```

## Required final score-level projections

The theorem surface must expose:

```text
thresholdLo ≤ productScore (productUpdate x)
productScore (productUpdate x) ≤ thresholdHi
```

## Rejected shape

The milestone is rejected if it only repacks the v15.5 base-and-updated window theorem without taking a prior base window target as input.
