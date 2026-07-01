# Restricted Bridge Simulation Sanity Check

## Boundary

This artifact is a restricted finite computational sanity check only.

It is not a proof of the full Viruse Fabric theory.
It is not a proof of unrestricted TTP-VF-H2-004.
It is not empirical validation.
It is not biological validation.

## Checked restricted claim

`ledger_effect_size_R(x)=V_R(f_R(x))-V_R(x)`

- `x notin F_R => ledger_effect_size_R(x)>0`
- `x in F_R => ledger_effect_size_R(x)=0`

## Summary

- Total cases: 4
- Total states checked: 4860
- Total violations: 0
- Passed: True

## Case table

| Case | n | d | h_mode | states | fixed | nonfixed | violations | passed |
|---|---:|---:|---|---:|---:|---:|---:|---|
| RBSC-001-small-single-active | 1 | 1 | increment_by_1 | 8 | 4 | 4 | 0 | True |
| RBSC-002-all-time-active | 2 | 1 | increment_by_1 | 27 | 1 | 26 | 0 | True |
| RBSC-003-two-space-mixed-active | 2 | 2 | jump_to_top | 729 | 27 | 702 | 0 | True |
| RBSC-004-two-space-capped-increment | 3 | 2 | increment_by_2_capped | 4096 | 64 | 4032 | 0 | True |
