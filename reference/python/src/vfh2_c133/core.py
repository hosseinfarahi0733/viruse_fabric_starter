from __future__ import annotations

from dataclasses import asdict, dataclass
from itertools import product
from typing import Callable, Iterable


BoolConstraint = Callable[[bool, bool, bool], bool]
Evidence = Callable[["State"], bool]
BOOLEAN_DOMAIN: tuple[bool, bool] = (False, True)


@dataclass(frozen=True)
class State:
    """One complete state across ordered causal epochs."""

    past: bool
    present: bool
    future: bool


@dataclass(frozen=True)
class BooleanTriTemporalSCM:
    """Finite deterministic three-epoch SCM used by the exact oracle."""

    name: str
    present_law: Callable[[bool], bool]
    future_law: Callable[[bool, bool], bool]


PARITY_SCM = BooleanTriTemporalSCM(
    name="boolean-parity-scm-v1",
    present_law=lambda past: past,
    future_law=lambda past, present: past ^ present,
)


def realize(model: BooleanTriTemporalSCM, past: bool) -> State:
    present = model.present_law(past)
    return State(past=past, present=present, future=model.future_law(past, present))


def do_present(model: BooleanTriTemporalSCM, past: bool, present: bool) -> State:
    """Surgical present intervention with downstream recomputation."""

    return State(past=past, present=present, future=model.future_law(past, present))


def do_future(model: BooleanTriTemporalSCM, past: bool, future: bool) -> State:
    """Surgical terminal intervention; upstream epochs remain generated."""

    return State(past=past, present=model.present_law(past), future=future)


def candidate_pasts(
    evidence: Evidence,
    present: bool,
    future: bool,
    domain: Iterable[bool] = BOOLEAN_DOMAIN,
) -> tuple[bool, ...]:
    return tuple(
        past for past in domain if evidence(State(past, present, future))
    )


def evidence_refines(
    stronger: Evidence,
    weaker: Evidence,
    domain: Iterable[bool] = BOOLEAN_DOMAIN,
) -> bool:
    return all(
        not stronger(State(past, present, future))
        or weaker(State(past, present, future))
        for past, present, future in product(domain, repeat=3)
    )


def even_parity(past: bool, present: bool, future: bool) -> bool:
    """True exactly for triples containing an even number of true values."""

    return not (past ^ present ^ future)


def unconstrained_evidence(_: State) -> bool:
    return True


def even_parity_evidence(state: State) -> bool:
    return even_parity(state.past, state.present, state.future)


def natural_rectangle_defect(
    relation: BoolConstraint,
    past_one: bool,
    past_two: bool,
    present: bool,
    future_one: bool,
    future_two: bool,
) -> int:
    """Executable counterpart of C133 `naturalRectangleDefect`."""

    return int(
        relation(past_one, present, future_one)
        and relation(past_two, present, future_two)
        and not relation(past_one, present, future_two)
    )


def all_rectangle_defects_zero(
    relation: BoolConstraint,
    domain: Iterable[bool] = BOOLEAN_DOMAIN,
) -> bool:
    return all(
        natural_rectangle_defect(
            relation, past_one, past_two, present, future_one, future_two
        )
        == 0
        for past_one, past_two, present, future_one, future_two in product(
            domain, repeat=5
        )
    )


def middle_rectangle_closed(
    relation: BoolConstraint,
    domain: Iterable[bool] = BOOLEAN_DOMAIN,
) -> bool:
    for past_one, past_two, present, future_one, future_two in product(
        domain, repeat=5
    ):
        if (
            relation(past_one, present, future_one)
            and relation(past_two, present, future_two)
            and not relation(past_one, present, future_two)
        ):
            return False
    return True


def adjacent_chain_relation(past: bool, present: bool, future: bool) -> bool:
    return past == present and present == future


def flip_relation(relation: BoolConstraint) -> BoolConstraint:
    """Bijective state renaming by Boolean complementation."""

    return lambda past, present, future: relation(
        not past, not present, not future
    )


def full_semantic_report() -> dict[str, object]:
    observational = realize(PARITY_SCM, False)
    present_intervention = do_present(PARITY_SCM, False, True)
    future_intervention = do_future(PARITY_SCM, False, True)
    weak_candidates = candidate_pasts(unconstrained_evidence, False, False)
    strong_candidates = candidate_pasts(even_parity_evidence, False, False)

    parity_defects = sum(
        natural_rectangle_defect(
            even_parity, past_one, past_two, present, future_one, future_two
        )
        for past_one, past_two, present, future_one, future_two in product(
            BOOLEAN_DOMAIN, repeat=5
        )
    )
    renamed_parity_defects = sum(
        natural_rectangle_defect(
            flip_relation(even_parity),
            past_one,
            past_two,
            present,
            future_one,
            future_two,
        )
        for past_one, past_two, present, future_one, future_two in product(
            BOOLEAN_DOMAIN, repeat=5
        )
    )

    return {
        "schema": "vfh2.c133.semantic-report.v1",
        "claim_boundary": (
            "finite mathematical semantics; no physical, biological, or "
            "empirical claim"
        ),
        "model": PARITY_SCM.name,
        "observational_state": asdict(observational),
        "present_intervention": asdict(present_intervention),
        "future_intervention": asdict(future_intervention),
        "no_retrocausality": {
            "present_intervention_preserves_past": (
                present_intervention.past == observational.past
            ),
            "future_intervention_preserves_past": (
                future_intervention.past == observational.past
            ),
            "future_intervention_preserves_present": (
                future_intervention.present == observational.present
            ),
        },
        "observer_recontextualization": {
            "weak_candidate_pasts": list(weak_candidates),
            "strong_candidate_pasts": list(strong_candidates),
            "strict_refinement": (
                set(strong_candidates) < set(weak_candidates)
            ),
            "actual_past_unchanged_and_retained": (
                observational.past is False and False in strong_candidates
            ),
        },
        "constraint_geometry": {
            "parity_defect_count": parity_defects,
            "parity_all_defects_zero": all_rectangle_defects_zero(even_parity),
            "parity_middle_rectangle_closed": middle_rectangle_closed(even_parity),
            "chain_all_defects_zero": all_rectangle_defects_zero(
                adjacent_chain_relation
            ),
            "chain_middle_rectangle_closed": middle_rectangle_closed(
                adjacent_chain_relation
            ),
            "renaming_preserves_parity_defect_count": (
                parity_defects == renamed_parity_defects
            ),
        },
    }
