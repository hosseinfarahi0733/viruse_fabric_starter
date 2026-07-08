# VF-H2 Proof Debt

| ID | Assumption / Debt | Status | Priority | Removable? | Notes |
|---|---|---:|---:|---:|---|
| A1 | Score preservation | Remaining | High | Maybe | Classified as pointwise score preservation. Not currently derived from update/domain semantics. |
| A2 | ProductFixedSet | Remaining | High | Unknown | C9.1 specialized fixedness to `ProductFixedSet p x`; C10 recorded that it is not currently derivable from existing semantics. |
| A3 | Natural base lower bound | Remaining | Medium | Unknown | `thresholdLo ≤ productScore x` is assumed in the current proof spine. |
| A4 | Natural base upper bound | Remaining | Medium | Unknown | `productScore x ≤ thresholdHi` is assumed in the current proof spine. |
| D1 | Over-wrapper risk | Active | High | Yes | Avoid additional theorem layers that only restate existing assumptions. |
| D2 | Theory entry-point clarity | Active | High | Yes | `THEORY.md` is required so a reviewer can identify the exact theorem, assumptions, and scientific claim. |
| D3 | Review evidence packaging | Active | Medium | Yes | Core Lean files and command outputs should be packaged separately from the full repository. |

## Current proof-debt interpretation

The project has a working conditional proof spine, but its highest-value proof debt is still assumption discharge.

The next scientifically meaningful work must answer:

- Can score preservation be derived from a concrete update semantics?
- Can `ProductFixedSet p x` be derived from a meaningful domain or initialization condition?
- Can natural bounds be derived rather than assumed?

If not, these assumptions must remain explicit and must not be marketed as proven facts.
