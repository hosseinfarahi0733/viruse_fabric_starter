# VF-H2 Dependency Graph

## High-level dependency flow

Definitions
  ↓
Product parameters and product-index state
  ↓
Product update semantics
  ↓
Fixed-set and ledger semantics
  ↓
Nonfixed increase / fixed-zero bridge components
  ↓
Score-preserving policy layer
  ↓
Transport and canonical typed/product equivalences
  ↓
Restricted bridge / restricted proof-spine target
  ↓
Full natural restricted proof spine

## Conceptual graph

```text
ProductRestrictedParams
ProductIndex
Product State
        |
        v
ProductUpdate / productUpdateState
        |
        +-------------------------+
        |                         |
        v                         v
ProductFixedSet             ProductLedgerEffect
        |                         |
        v                         v
Fixed-zero results          Nonfixed-positive results
        \                         /
         \                       /
          v                     v
          Product Restricted Bridge
                    |
                    v
Score Preservation / Identity-like Policy
                    |
                    v
Canonical Raw Equalities / Transport
                    |
                    v
Restricted Proof Spine Target
                    |
                    v
Full Natural Restricted Proof Spine
```

## Reviewer warning

Transport lemmas are representation lemmas, not domain theorems.

Bridge dichotomies split on fixedness/nonfixedness. They do not by themselves derive fixedness.
