# C9.1 hFixed ProductFixedSet Semantic Specialization

## Result

C9.1 specializes the arbitrary v17.4 fixed proposition:

```lean
fixed : Prop
hFixed : fixed
```

to the concrete product-side fixed-set predicate:

```lean
ProductFixedSet p x
hFixedSet : ProductFixedSet p x
```

## Boundary

This is a semantic specialization, not a derivation.

It does not prove ProductFixedSet p x from update/domain dynamics.

It does not prove full VF-H2.

It should not create a scientific tag.
