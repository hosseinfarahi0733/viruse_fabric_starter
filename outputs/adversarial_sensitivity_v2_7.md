# Adversarial Sensitivity Sweep v2.7

## Purpose

This adversarial sensitivity sweep pushes scoring weights into hostile but interpretable configurations and adds decoy cases designed to mimic targeting without strong constructive support.

## Thresholds

- Minimum adversarial stability rate: 70.00%
- Minimum supported-route margin: 10.00
- Maximum ablated route score: 65.00
- Maximum shortcut route score: 50.00
- Maximum tension well route score: 40.00

## Summary

- Cases tested: 7
- Profiles tested: 8640
- Stable profiles: 7004
- Unstable profiles: 1636
- Stability rate: 81.06%
- Minimum supported margin: 0.00
- Median supported margin: 25.47
- Maximum supported margin: 58.45

## Top-case counts

| Case | Top count |
|---|---:|
| supported_constructive_route | 8640 |
| ablated_route | 0 |
| shortcut_gateway_route | 0 |
| tension_well_route | 0 |
| high_salience_ablated_decoy | 0 |
| high_path_shortcut_decoy | 0 |
| low_penalty_tension_decoy | 0 |

## Failure reason counts

| Reason | Count |
|---|---:|
| supported route won without enough margin | 608 |
| ablated route exceeded adversarial threshold | 1024 |
| shortcut gateway route exceeded adversarial threshold | 4 |

## Closest adversarial runs

| Profile | Top case | Supported | Strongest rival | Margin | Stable | Failure reason |
|---|---|---:|---:|---:|---|---|
| adversarial_profile_1713 | supported_constructive_route | 100.00 | 100.00 | 0.00 | False | supported route won without enough margin |
| adversarial_profile_1714 | supported_constructive_route | 100.00 | 100.00 | 0.00 | False | supported route won without enough margin |
| adversarial_profile_1715 | supported_constructive_route | 100.00 | 100.00 | 0.00 | False | supported route won without enough margin |
| adversarial_profile_1716 | supported_constructive_route | 100.00 | 100.00 | 0.00 | False | supported route won without enough margin |
| adversarial_profile_1717 | supported_constructive_route | 100.00 | 100.00 | 0.00 | False | supported route won without enough margin |
| adversarial_profile_1718 | supported_constructive_route | 100.00 | 100.00 | 0.00 | False | supported route won without enough margin |
| adversarial_profile_1719 | supported_constructive_route | 100.00 | 100.00 | 0.00 | False | supported route won without enough margin |
| adversarial_profile_1720 | supported_constructive_route | 100.00 | 100.00 | 0.00 | False | supported route won without enough margin |
| adversarial_profile_1721 | supported_constructive_route | 100.00 | 100.00 | 0.00 | False | supported route won without enough margin |
| adversarial_profile_1722 | supported_constructive_route | 100.00 | 100.00 | 0.00 | False | supported route won without enough margin |
| adversarial_profile_1723 | supported_constructive_route | 100.00 | 100.00 | 0.00 | False | supported route won without enough margin |
| adversarial_profile_1724 | supported_constructive_route | 100.00 | 100.00 | 0.00 | False | supported route won without enough margin |
| adversarial_profile_1725 | supported_constructive_route | 100.00 | 100.00 | 0.00 | False | supported route won without enough margin |
| adversarial_profile_1726 | supported_constructive_route | 100.00 | 100.00 | 0.00 | False | supported route won without enough margin |
| adversarial_profile_1727 | supported_constructive_route | 100.00 | 100.00 | 0.00 | False | supported route won without enough margin |

## Findings

| Severity | Code | Message |
|---|---|---|
| warning | supported_route_won_without_enough_margin | supported route won without enough margin: 608 profiles. |
| warning | ablated_route_exceeded_adversarial_threshold | ablated route exceeded adversarial threshold: 1024 profiles. |
| warning | shortcut_gateway_route_exceeded_adversarial_threshold | shortcut gateway route exceeded adversarial threshold: 4 profiles. |

## Interpretation

This test does not require perfect stability. It asks whether the model remains usable under hostile weight settings, near-tie pressure, and decoy cases. Warnings identify fragile regions without automatically invalidating the model.

## Boundary

This adversarial sensitivity analysis is conceptual and non-operational. It does not use real pathogens, real hosts, biological protocols, laboratory procedures, or executable interventions.
