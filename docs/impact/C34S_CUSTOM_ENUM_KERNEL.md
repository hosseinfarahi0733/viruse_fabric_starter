# C34S Custom Product Index Enumeration Kernel

This integrates the C34R-passing transparent enumeration kernel as source infrastructure.

Added module:

- `VFH2.Product.ProductRestrictedParamsActiveCustomEnumKernel`

Main local facts:

- `finEnum_length`
- `finEnum_nodup`
- `finEnum_complete`
- `productWidthEnum_length_typedWidth`
- `productWidthEnum_complete`
- `productWidthEnum_nodup`
- `productIndexEnum_length_typedWidth`
- `productIndexEnum_complete`
- `productIndexEnum_nodup`
- `typedWidth_le_active_length_of_productIndexEnum_sublist`
- `not_all_active_of_productIndexEnum_sublist_source`
- `activeNoncoverageCertificate_of_productIndexEnum_sublist_source`

Scientific status:

This is real infrastructure, but it still does **not** derive the final lower-bound theorem from all-active membership. The remaining target is:

```lean
productIndexEnum_complete
productIndexEnum_nodup
all-active membership
⊢ Typed.typedWidth p.d ≤ p.active.length
```

No release tag should be created for this integration alone.
