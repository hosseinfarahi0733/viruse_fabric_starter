# C34Z Active-Length Lower-Bound Integration

C34Z integrates the successful C34W active-length route as real source.

Main result:

```lean
p.active.length < Typed.typedWidth p.d
→ ¬ ∀ i : ProductIndex p.d, i ∈ p.active
→ ActiveNoncoverageCertificate p
```

The route depends on the C34S custom product-index enumeration:

- `productIndexEnum_complete`
- `productIndexEnum_nodup`
- `productIndexEnum_length_typedWidth`

and a local list-cardinality kernel:

```lean
length_le_of_nodup_and_mem_subset_beq
```

This commit intentionally does not create a tag. A final audit should precede any `v17.23.0` tag.
