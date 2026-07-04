# VF-H2 v12.0.0 — Generalization Gap Register

## Purpose

This register lists the remaining gaps between the current v11 restricted
transport scaffold and a future generalized VF-H2 theory.

## Gap summary

| Gap ID | Area | Current v11 status | Required v12 action | Status |
|---|---|---|---|---|
| G-001 | Restriction definitions | Restricted scaffold audited | Inventory exact restrictions | Open |
| G-002 | Active-set transport | Proven for current Product/Typed scaffold | Generalize membership assumptions | Open |
| G-003 | Update transport | Proven for restricted top-coordinate update | Generalize update operator carefully | Open |
| G-004 | Ledger transport | Proven for current ledger | Identify aggregation assumptions | Open |
| G-005 | Ledger-effect transport | Proven by composition | Reprove after update/ledger generalization | Open |
| G-006 | Fixed-set transport | Proven for current predicate | Generalize predicate assumptions | Open |
| G-007 | Bridge target transport | Proven for restricted target | Rebuild after fixed-set generalization | Open |
| G-008 | End-to-end unrestricted claim | Not proven | Define formal target before proof attempt | Open |
| G-009 | Empirical validation | Not part of Lean proof | Separate experimental protocol required | Open |
| G-010 | Biological validation | Not part of Lean proof | Separate domain validation required | Open |

## Highest priority gaps

### G-001 — Restriction definitions

Before proving any generalized theorem, v12 must identify the exact definitions
that encode restrictedness. This prevents accidental overclaiming.

### G-002 — Active-set transport

Active-set membership transport is upstream of update, fixed-set, and bridge
theorems. It should be generalized before those downstream results.

### G-003 — Update transport

The current update transport depends on the restricted update structure. Any
change to the update operator must be isolated before ledger-effect transport is
reused.

## Blocked claims

The following claims remain blocked until corresponding gaps are closed:

```text
Unrestricted Product/Typed transport ladder
Full VF-H2 theorem
General end-to-end dynamics theorem
Empirical or biological validation
```

## Recommended next milestone

```text
v12.1.0: Restriction inventory and definition-surface audit
```

The next milestone should produce a definition-level map of restrictedness, not
a new headline theorem.
