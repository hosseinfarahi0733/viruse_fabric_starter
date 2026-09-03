from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import product
from typing import Iterator, TypeAlias


SCHEMA = "vfh2.c138.interventional-conformance.v1"
BOOLEAN_DOMAIN: tuple[bool, bool] = (False, True)
ConstraintTable: TypeAlias = tuple[
    bool, bool, bool, bool, bool, bool, bool, bool
]

_PRESENT_ROWS = BOOLEAN_DOMAIN
_FUTURE_ROWS = tuple(product(BOOLEAN_DOMAIN, repeat=2))
_CONSTRAINT_ROWS = tuple(product(BOOLEAN_DOMAIN, repeat=3))
_POINTWISE_ROWS = _CONSTRAINT_ROWS
_WITNESS_ROWS = tuple(product(BOOLEAN_DOMAIN, repeat=5))


def _require_bool(value: object, label: str) -> bool:
    if type(value) is not bool:
        raise TypeError(f"{label} must be a built-in bool")
    return value


def _require_bool_table(
    table: object, expected_length: int, label: str
) -> tuple[bool, ...]:
    if type(table) is not tuple:
        raise TypeError(f"{label} must be a tuple")
    if len(table) != expected_length:
        raise ValueError(
            f"{label} must contain exactly {expected_length} values"
        )
    for index, value in enumerate(table):
        _require_bool(value, f"{label}[{index}]")
    return table


def _require_constraint_table(table: object) -> ConstraintTable:
    checked = _require_bool_table(table, 8, "constraint")
    return (
        checked[0],
        checked[1],
        checked[2],
        checked[3],
        checked[4],
        checked[5],
        checked[6],
        checked[7],
    )


@dataclass(frozen=True)
class State:
    """One complete Boolean state across the three ordered epochs."""

    past: bool
    present: bool
    future: bool

    def __post_init__(self) -> None:
        _require_bool(self.past, "past")
        _require_bool(self.present, "present")
        _require_bool(self.future, "future")


@dataclass(frozen=True)
class BooleanTriTemporalSCM:
    """A deterministic Boolean SCM represented by immutable truth tables."""

    name: str
    present_table: tuple[bool, bool]
    future_table: tuple[bool, bool, bool, bool]

    def __post_init__(self) -> None:
        if type(self.name) is not str or not self.name:
            raise TypeError("name must be a nonempty built-in str")
        _require_bool_table(self.present_table, 2, "present_table")
        _require_bool_table(self.future_table, 4, "future_table")

    def present_law(self, past: bool) -> bool:
        return self.present_table[int(_require_bool(past, "past"))]

    def future_law(self, past: bool, present: bool) -> bool:
        past_value = _require_bool(past, "past")
        present_value = _require_bool(present, "present")
        return self.future_table[2 * int(past_value) + int(present_value)]


PAST_COPY_SCM = BooleanTriTemporalSCM(
    name="past-copy-scm-v1",
    present_table=(False, True),
    future_table=(False, False, True, True),
)

PRESENT_COPY_SCM = BooleanTriTemporalSCM(
    name="present-copy-scm-v1",
    present_table=(False, True),
    future_table=(False, True, False, True),
)

_BOOLEAN_PARITY_SCM = BooleanTriTemporalSCM(
    name="boolean-parity-scm-v1",
    present_table=(False, True),
    future_table=(False, True, True, False),
)


def _require_model(model: object) -> BooleanTriTemporalSCM:
    if type(model) is not BooleanTriTemporalSCM:
        raise TypeError("model must be a BooleanTriTemporalSCM")
    return model


def realize(model: BooleanTriTemporalSCM, past: bool) -> State:
    """Evaluate the observational trajectory generated from one past value."""

    checked_model = _require_model(model)
    checked_past = _require_bool(past, "past")
    present = checked_model.present_law(checked_past)
    return State(
        past=checked_past,
        present=present,
        future=checked_model.future_law(checked_past, present),
    )


def do_present(
    model: BooleanTriTemporalSCM, past: bool, present: bool
) -> State:
    """Set the present surgically and recompute the downstream future."""

    checked_model = _require_model(model)
    checked_past = _require_bool(past, "past")
    checked_present = _require_bool(present, "present")
    return State(
        past=checked_past,
        present=checked_present,
        future=checked_model.future_law(checked_past, checked_present),
    )


def law_graph(model: BooleanTriTemporalSCM) -> ConstraintTable:
    """Serialize the exact graph of a model's structural future law."""

    checked_model = _require_model(model)
    values = tuple(
        future is checked_model.future_law(past, present)
        for past, present, future in _CONSTRAINT_ROWS
    )
    return _require_constraint_table(values)


def _constraint_value(
    constraint: ConstraintTable,
    past: bool,
    present: bool,
    future: bool,
) -> bool:
    index = 4 * int(past) + 2 * int(present) + int(future)
    return constraint[index]


def constraint_characterizes_future_law(
    model: BooleanTriTemporalSCM, constraint: ConstraintTable
) -> bool:
    """Mirror Lean's eight-row future-law biconditional exactly."""

    checked_model = _require_model(model)
    checked_constraint = _require_constraint_table(constraint)
    return all(
        _constraint_value(checked_constraint, past, present, future)
        == (future is checked_model.future_law(past, present))
        for past, present, future in _CONSTRAINT_ROWS
    )


def present_causal_contrast_at(
    model: BooleanTriTemporalSCM,
    past: bool,
    present_one: bool,
    present_two: bool,
) -> bool:
    """Decide whether two fixed-past present interventions differ downstream."""

    checked_model = _require_model(model)
    checked_past = _require_bool(past, "past")
    checked_one = _require_bool(present_one, "present_one")
    checked_two = _require_bool(present_two, "present_two")
    return (
        checked_model.future_law(checked_past, checked_one)
        is not checked_model.future_law(checked_past, checked_two)
    )


def present_has_causal_effect_on_future(
    model: BooleanTriTemporalSCM,
) -> bool:
    """Decide Lean's existential present-to-future causal-effect predicate."""

    checked_model = _require_model(model)
    return any(
        present_causal_contrast_at(
            checked_model, past, present_one, present_two
        )
        for past, present_one, present_two in _POINTWISE_ROWS
    )


def constraint_contrast_witness_exists(
    constraint: ConstraintTable,
    past: bool,
    present_one: bool,
    present_two: bool,
) -> bool:
    """Search the independent constraint-side witness used by C135."""

    checked_constraint = _require_constraint_table(constraint)
    checked_past = _require_bool(past, "past")
    checked_one = _require_bool(present_one, "present_one")
    checked_two = _require_bool(present_two, "present_two")
    return any(
        _constraint_value(
            checked_constraint, checked_past, checked_one, future_one
        )
        and _constraint_value(
            checked_constraint, checked_past, checked_two, future_two
        )
        and future_one is not future_two
        for future_one, future_two in _FUTURE_ROWS
    )


def observationally_equivalent(
    left: BooleanTriTemporalSCM, right: BooleanTriTemporalSCM
) -> bool:
    """Compare all three realized fields for every Boolean past value."""

    checked_left = _require_model(left)
    checked_right = _require_model(right)
    for past in BOOLEAN_DOMAIN:
        left_state = realize(checked_left, past)
        right_state = realize(checked_right, past)
        if not (
            left_state.past is right_state.past
            and left_state.present is right_state.present
            and left_state.future is right_state.future
        ):
            return False
    return True


def _table_from_mask(mask: int, width: int, label: str) -> tuple[bool, ...]:
    if type(mask) is not int:
        raise TypeError(f"{label} must be a built-in int")
    if mask < 0 or mask >= 1 << width:
        raise ValueError(f"{label} must be in range(0, {1 << width})")
    return tuple(bool(mask & (1 << index)) for index in range(width))


def _constraint_from_mask(mask: int) -> ConstraintTable:
    return _require_constraint_table(_table_from_mask(mask, 8, "constraint_mask"))


def _constraint_mask(constraint: ConstraintTable) -> int:
    checked = _require_constraint_table(constraint)
    return sum(1 << index for index, value in enumerate(checked) if value)


def _model_from_masks(
    present_mask: int, future_mask: int
) -> BooleanTriTemporalSCM:
    present = _table_from_mask(present_mask, 2, "present_mask")
    future = _table_from_mask(future_mask, 4, "future_mask")
    return BooleanTriTemporalSCM(
        name=f"boolean-scm-p{present_mask:01x}-f{future_mask:01x}",
        present_table=(present[0], present[1]),
        future_table=(future[0], future[1], future[2], future[3]),
    )


def _all_models() -> Iterator[tuple[int, int, int, BooleanTriTemporalSCM]]:
    for present_mask in range(4):
        for future_mask in range(16):
            model_index = 16 * present_mask + future_mask
            yield (
                model_index,
                present_mask,
                future_mask,
                _model_from_masks(present_mask, future_mask),
            )


def _all_constraints() -> Iterator[tuple[int, ConstraintTable]]:
    for constraint_mask in range(256):
        yield constraint_mask, _constraint_from_mask(constraint_mask)


def _constraint_global_witness_exists(constraint: ConstraintTable) -> bool:
    checked = _require_constraint_table(constraint)
    return any(
        _constraint_value(checked, past, present_one, future_one)
        and _constraint_value(checked, past, present_two, future_two)
        and future_one is not future_two
        for past, present_one, present_two, future_one, future_two
        in _WITNESS_ROWS
    )


def _explicit_witness_count(constraint: ConstraintTable) -> int:
    checked = _require_constraint_table(constraint)
    return sum(
        1
        for past, present_one, present_two, future_one, future_two
        in _WITNESS_ROWS
        if _constraint_value(checked, past, present_one, future_one)
        and _constraint_value(checked, past, present_two, future_two)
        and future_one is not future_two
    )


def _rectangle_defect_count(constraint: ConstraintTable) -> int:
    checked = _require_constraint_table(constraint)
    return sum(
        1
        for past_one, past_two, present, future_one, future_two
        in _WITNESS_ROWS
        if _constraint_value(checked, past_one, present, future_one)
        and _constraint_value(checked, past_two, present, future_two)
        and not _constraint_value(checked, past_one, present, future_two)
    )


def _state_record(state: State) -> dict[str, bool]:
    return {
        "past": state.past,
        "present": state.present,
        "future": state.future,
    }


def _model_observation_signature(
    model: BooleanTriTemporalSCM,
) -> tuple[tuple[bool, bool, bool], tuple[bool, bool, bool]]:
    states = tuple(realize(model, past) for past in BOOLEAN_DOMAIN)
    return (
        (states[0].past, states[0].present, states[0].future),
        (states[1].past, states[1].present, states[1].future),
    )


def _named_fixture_report() -> dict[str, object]:
    parity_graph = law_graph(_BOOLEAN_PARITY_SCM)
    past_graph = law_graph(PAST_COPY_SCM)
    present_graph = law_graph(PRESENT_COPY_SCM)
    past_observations = [
        _state_record(realize(PAST_COPY_SCM, past))
        for past in BOOLEAN_DOMAIN
    ]
    present_observations = [
        _state_record(realize(PRESENT_COPY_SCM, past))
        for past in BOOLEAN_DOMAIN
    ]
    off_path = [
        {
            "past": past,
            "intervened_present": present,
            "past_copy_future": do_present(
                PAST_COPY_SCM, past, present
            ).future,
            "present_copy_future": do_present(
                PRESENT_COPY_SCM, past, present
            ).future,
        }
        for past, present in ((False, True), (True, False))
    ]

    empty_constraint = _constraint_from_mask(0)
    universal_constraint = _constraint_from_mask(255)
    return {
        "c134_boolean_parity": {
            "model_index": 38,
            "present_mask": 2,
            "future_mask": 6,
            "law_graph_mask": _constraint_mask(parity_graph),
            "present_effect": present_has_causal_effect_on_future(
                _BOOLEAN_PARITY_SCM
            ),
            "true_ordered_pointwise_contrasts": sum(
                present_causal_contrast_at(
                    _BOOLEAN_PARITY_SCM,
                    past,
                    present_one,
                    present_two,
                )
                for past, present_one, present_two in _POINTWISE_ROWS
            ),
            "rectangle_defect_count": _rectangle_defect_count(parity_graph),
        },
        "c136_geometry_causality": {
            "past_copy": {
                "model_index": 44,
                "law_graph_mask": _constraint_mask(past_graph),
                "middle_rectangle_closed": (
                    _rectangle_defect_count(past_graph) == 0
                ),
                "rectangle_defect_count": _rectangle_defect_count(past_graph),
                "present_effect": present_has_causal_effect_on_future(
                    PAST_COPY_SCM
                ),
            },
            "present_copy": {
                "model_index": 42,
                "law_graph_mask": _constraint_mask(present_graph),
                "middle_rectangle_closed": (
                    _rectangle_defect_count(present_graph) == 0
                ),
                "rectangle_defect_count": _rectangle_defect_count(
                    present_graph
                ),
                "present_effect": present_has_causal_effect_on_future(
                    PRESENT_COPY_SCM
                ),
                "witness": {
                    "past": False,
                    "present_one": False,
                    "present_two": True,
                },
            },
        },
        "c137_observational_nonidentifiability": {
            "past_copy_observations": past_observations,
            "present_copy_observations": present_observations,
            "fieldwise_observational_equivalence": observationally_equivalent(
                PAST_COPY_SCM, PRESENT_COPY_SCM
            ),
            "past_copy_present_effect": (
                present_has_causal_effect_on_future(PAST_COPY_SCM)
            ),
            "present_copy_present_effect": (
                present_has_causal_effect_on_future(PRESENT_COPY_SCM)
            ),
            "off_path_intervention_separation": off_path,
        },
        "premise_is_necessary": {
            "empty_constraint_with_present_copy": {
                "constraint_mask": 0,
                "characterizes_future_law": (
                    constraint_characterizes_future_law(
                        PRESENT_COPY_SCM, empty_constraint
                    )
                ),
                "model_has_effect": present_has_causal_effect_on_future(
                    PRESENT_COPY_SCM
                ),
                "constraint_has_global_witness": (
                    _constraint_global_witness_exists(empty_constraint)
                ),
            },
            "universal_constraint_with_past_copy": {
                "constraint_mask": 255,
                "characterizes_future_law": (
                    constraint_characterizes_future_law(
                        PAST_COPY_SCM, universal_constraint
                    )
                ),
                "model_has_effect": present_has_causal_effect_on_future(
                    PAST_COPY_SCM
                ),
                "constraint_has_global_witness": (
                    _constraint_global_witness_exists(universal_constraint)
                ),
            },
        },
    }


def full_interventional_conformance_report() -> dict[str, object]:
    """Exhaustively compare the Python decisions with the C134-C137 contract."""

    models = tuple(_all_models())
    constraints = tuple(_all_constraints())
    failures: list[dict[str, object]] = []
    per_model: list[dict[str, object]] = []
    graph_constraint_model_counts: Counter[int] = Counter()
    geometry_effect_counts: Counter[tuple[bool, bool]] = Counter()

    qualified_pair_count = 0
    qualified_pointwise_case_count = 0
    passing_pointwise_case_count = 0
    true_pointwise_case_count = 0
    false_pointwise_case_count = 0
    passing_global_case_count = 0
    effectful_model_count = 0
    effectless_model_count = 0
    satisfying_explicit_witness_count = 0

    observation_classes: dict[
        tuple[tuple[bool, bool, bool], tuple[bool, bool, bool]],
        list[tuple[int, bool]],
    ] = {}

    for model_index, present_mask, future_mask, model in models:
        graph = law_graph(model)
        graph_mask = _constraint_mask(graph)
        graph_constraint_model_counts[graph_mask] += 1
        effect = present_has_causal_effect_on_future(model)
        defect_count = _rectangle_defect_count(graph)
        geometry_effect_counts[(defect_count == 0, effect)] += 1

        signature = _model_observation_signature(model)
        observation_classes.setdefault(signature, []).append(
            (model_index, effect)
        )

        matching_constraint_masks: list[int] = []
        model_pointwise_passes = 0
        model_true_pointwise_cases = 0
        model_explicit_witnesses = 0

        for constraint_mask, constraint in constraints:
            if not constraint_characterizes_future_law(model, constraint):
                continue
            qualified_pair_count += 1
            matching_constraint_masks.append(constraint_mask)

            for past, present_one, present_two in _POINTWISE_ROWS:
                qualified_pointwise_case_count += 1
                contrast = present_causal_contrast_at(
                    model, past, present_one, present_two
                )
                witness = constraint_contrast_witness_exists(
                    constraint, past, present_one, present_two
                )
                if contrast == witness:
                    passing_pointwise_case_count += 1
                    model_pointwise_passes += 1
                else:
                    failures.append(
                        {
                            "check": "c135_pointwise_equivalence",
                            "model_index": model_index,
                            "constraint_mask": constraint_mask,
                            "past": past,
                            "present_one": present_one,
                            "present_two": present_two,
                            "contrast": contrast,
                            "witness": witness,
                        }
                    )
                if contrast:
                    true_pointwise_case_count += 1
                    model_true_pointwise_cases += 1
                else:
                    false_pointwise_case_count += 1

            global_witness = _constraint_global_witness_exists(constraint)
            if effect == global_witness:
                passing_global_case_count += 1
            else:
                failures.append(
                    {
                        "check": "c135_global_equivalence",
                        "model_index": model_index,
                        "constraint_mask": constraint_mask,
                        "effect": effect,
                        "witness": global_witness,
                    }
                )
            model_explicit_witnesses = _explicit_witness_count(constraint)
            satisfying_explicit_witness_count += model_explicit_witnesses

        if matching_constraint_masks != [graph_mask]:
            failures.append(
                {
                    "check": "unique_law_graph_recovery",
                    "model_index": model_index,
                    "expected_constraint_mask": graph_mask,
                    "matching_constraint_masks": matching_constraint_masks,
                }
            )

        if effect:
            effectful_model_count += 1
        else:
            effectless_model_count += 1

        per_model.append(
            {
                "model_index": model_index,
                "present_mask": present_mask,
                "future_mask": future_mask,
                "law_graph_mask": graph_mask,
                "matching_constraint_masks": matching_constraint_masks,
                "middle_rectangle_closed": defect_count == 0,
                "rectangle_defect_count": defect_count,
                "present_effect": effect,
                "pointwise_equivalence_pass_count": model_pointwise_passes,
                "true_ordered_pointwise_contrast_count": (
                    model_true_pointwise_cases
                ),
                "explicit_constraint_witness_count": (
                    model_explicit_witnesses
                ),
            }
        )

    constraint_defect_histogram = Counter(
        _rectangle_defect_count(constraint)
        for _, constraint in constraints
    )
    observational_ordered_including_self = sum(
        len(members) ** 2 for members in observation_classes.values()
    )
    observational_ordered_distinct = sum(
        len(members) * (len(members) - 1)
        for members in observation_classes.values()
    )
    observational_unordered_distinct = observational_ordered_distinct // 2
    observational_different_status_ordered = 0
    for members in observation_classes.values():
        effect_count = sum(effect for _, effect in members)
        no_effect_count = len(members) - effect_count
        observational_different_status_ordered += (
            2 * effect_count * no_effect_count
        )

    actual_counts = {
        "model_count": len(models),
        "constraint_count": len(constraints),
        "model_constraint_pair_count": len(models) * len(constraints),
        "qualified_pair_count": qualified_pair_count,
        "unqualified_pair_count": (
            len(models) * len(constraints) - qualified_pair_count
        ),
        "distinct_law_graph_constraint_count": len(
            graph_constraint_model_counts
        ),
        "qualified_pointwise_case_count": qualified_pointwise_case_count,
        "passing_pointwise_case_count": passing_pointwise_case_count,
        "true_pointwise_case_count": true_pointwise_case_count,
        "false_pointwise_case_count": false_pointwise_case_count,
        "passing_global_case_count": passing_global_case_count,
        "effectful_model_count": effectful_model_count,
        "effectless_model_count": effectless_model_count,
        "explicit_witness_candidate_count": qualified_pair_count * 32,
        "satisfying_explicit_witness_count": satisfying_explicit_witness_count,
        "observational_equivalence_class_count": len(observation_classes),
        "observational_ordered_pair_count_including_self": (
            observational_ordered_including_self
        ),
        "observational_ordered_distinct_pair_count": (
            observational_ordered_distinct
        ),
        "observational_unordered_distinct_pair_count": (
            observational_unordered_distinct
        ),
        "observational_different_causal_status_ordered_pair_count": (
            observational_different_status_ordered
        ),
        "observational_different_causal_status_unordered_pair_count": (
            observational_different_status_ordered // 2
        ),
    }
    expected_counts = {
        "model_count": 64,
        "constraint_count": 256,
        "model_constraint_pair_count": 16384,
        "qualified_pair_count": 64,
        "unqualified_pair_count": 16320,
        "distinct_law_graph_constraint_count": 16,
        "qualified_pointwise_case_count": 512,
        "passing_pointwise_case_count": 512,
        "true_pointwise_case_count": 128,
        "false_pointwise_case_count": 384,
        "passing_global_case_count": 64,
        "effectful_model_count": 48,
        "effectless_model_count": 16,
        "explicit_witness_candidate_count": 2048,
        "satisfying_explicit_witness_count": 128,
        "observational_equivalence_class_count": 16,
        "observational_ordered_pair_count_including_self": 256,
        "observational_ordered_distinct_pair_count": 192,
        "observational_unordered_distinct_pair_count": 96,
        "observational_different_causal_status_ordered_pair_count": 96,
        "observational_different_causal_status_unordered_pair_count": 48,
    }
    count_mismatches = {
        key: {"actual": actual_counts[key], "expected": expected}
        for key, expected in expected_counts.items()
        if actual_counts[key] != expected
    }
    if count_mismatches:
        failures.append(
            {
                "check": "frozen_exhaustive_counts",
                "mismatches": count_mismatches,
            }
        )

    class_size_histogram = Counter(
        len(members) for members in observation_classes.values()
    )
    return {
        "schema": SCHEMA,
        "claim_boundary": (
            "exhaustive finite Boolean semantic conformance; not statistical "
            "identification, causal discovery, or empirical, biological, or "
            "physical validation"
        ),
        "canonical_order": {
            "boolean_domain": [False, True],
            "present_rows": ["past=false", "past=true"],
            "future_rows": [
                "past=false,present=false",
                "past=false,present=true",
                "past=true,present=false",
                "past=true,present=true",
            ],
            "constraint_rows": [
                "past=false,present=false,future=false",
                "past=false,present=false,future=true",
                "past=false,present=true,future=false",
                "past=false,present=true,future=true",
                "past=true,present=false,future=false",
                "past=true,present=false,future=true",
                "past=true,present=true,future=false",
                "past=true,present=true,future=true",
            ],
            "mask_rule": "row i is encoded by bit (1 << i)",
            "model_index_rule": "16 * present_mask + future_mask",
        },
        "exhaustive_conformance": {
            "all_checks_pass": not failures,
            "counts": actual_counts,
            "expected_counts": expected_counts,
            "failures": failures,
            "graph_constraint_model_count_histogram": {
                str(count): sum(
                    matches == count
                    for matches in graph_constraint_model_counts.values()
                )
                for count in sorted(set(graph_constraint_model_counts.values()))
            },
            "constraint_rectangle_defect_histogram": {
                str(defect_count): constraint_defect_histogram[defect_count]
                for defect_count in sorted(constraint_defect_histogram)
            },
            "geometry_effect_model_counts": [
                {
                    "middle_rectangle_closed": geometry,
                    "present_effect": effect,
                    "model_count": geometry_effect_counts[(geometry, effect)],
                }
                for geometry, effect in product(BOOLEAN_DOMAIN, repeat=2)
            ],
            "observation_class_size_histogram": {
                str(size): class_size_histogram[size]
                for size in sorted(class_size_histogram)
            },
            "per_model": per_model,
        },
        "fixtures": _named_fixture_report(),
    }
