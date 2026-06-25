# Formal Notation Scaffold v3.5

## Purpose

This scaffold introduces a cautious symbolic vocabulary for the Viruse Fabric manuscript. Its purpose is clarity, not proof. The notation helps the manuscript state what is being modeled: constraints, paths, compatibility, constructive attractors, observer projection, false intentionality, and correction.

The scaffold should be read as a manuscript-facing bridge between conceptual explanation and later formalization. It is not a formal proof, not a complete mathematical theory, and not externally validated. Apparently even symbols need supervision, because otherwise humans start mistaking notation for truth.

## Core Formal Object

The top-level scaffold is:

```text
F = (C, P, A, O)
```

Where:

- `F` is the fabric.
- `C` is the constraint set.
- `P` is the path space.
- `A` is the constructive attractor set.
- `O` is observer projection.

This says that Viruse Fabric is not a simple chain of events. It is a structured object containing constraints, possible paths, attractor regions, and interpretive projection.

## Working Definitions

- A constraint is any abstract condition, pressure, relation, or filter that shapes the space of possible paths.
- Constraint geometry is the joint structure produced when constraints make some paths easier, harder, stable, unstable, visible, or suppressed.
- A path is a candidate route through the fabric, not necessarily a literal physical trajectory.
- Path compatibility describes how well a path fits the active constraint set.
- A constructive attractor is a region where compatible paths and tensions concentrate without requiring intention.
- Observer projection is the interpretive mapping that can make a structured path appear purposeful.
- Apparent intentionality is the appearance of purpose without a commitment to actual intention.
- False intentionality occurs when observer projection exceeds what intrinsic structure supports.
- Projection correction reduces false intentionality by separating observer interpretation from fabric structure.

## Notation Table

| Symbol | Name | Meaning | Manuscript use |
|---|---|---|---|
| `F` | Fabric | The abstract causal fabric containing constraints, paths, attractors, and observer projections. | Use F as the top-level object of the model. |
| `C` | Constraint set | The set of abstract conditions, pressures, relations, or filters that shape possible paths. | Use C to avoid treating causality as a simple event chain. |
| `c_i` | Individual constraint | A single constraint inside C, such as a pressure, relation, filter, or compatibility condition. | Use c_i when discussing how local restrictions shape path behavior. |
| `P` | Path space | The set of possible paths available inside the fabric before compatibility filtering. | Use P to distinguish possible paths from selected or interpreted paths. |
| `p` | Path | A candidate trajectory, sequence, or structured route through the fabric. | Use p for the object whose compatibility and apparent intentionality are evaluated. |
| `K(p, C)` | Compatibility score | A score describing how well path p fits the active constraint set C. | Use K to explain why some paths remain stable while others are suppressed. |
| `A` | Constructive attractor set | The set of regions where compatible paths, tensions, and relations concentrate. | Use A to formalize constructive attractor concentration without implying intention. |
| `alpha(p, A)` | Attractor concentration | A score describing how strongly path p concentrates around constructive attractors. | Use alpha to connect path compatibility with attractor-centered structure. |
| `O` | Observer projection | The interpretive mapping imposed by an observer on a structured path. | Use O to separate intrinsic fabric structure from observer interpretation. |
| `I_app(p, O)` | Apparent intentionality | The apparent purpose attributed to path p under observer projection O. | Use I_app to discuss purpose-like readings without claiming real intention. |
| `I_false` | False intentionality | Cases where observer projection assigns purpose beyond what intrinsic fabric structure supports. | Use I_false to represent observer-driven misreading. |
| `R` | Correction operator | A correction procedure that reduces false intentionality by separating projection from intrinsic structure. | Use R to describe projection correction and reduction of observer error. |

## Formal Relations

### 1. Fabric composition

```text
F = (C, P, A, O)
```

**Explanation.** The fabric is represented as constraints, possible paths, constructive attractors, and observer projection.

**Boundary.** This is a scaffold definition, not a complete mathematical ontology.

### 2. Constraint set

```text
C = {c_1, c_2, ..., c_n}
```

**Explanation.** The constraint set contains the abstract conditions that shape which paths remain possible or stable.

**Boundary.** The entries are abstract and do not represent biological protocols or operational interventions.

### 3. Path compatibility

```text
K(p, C) -> [0, 1]
```

**Explanation.** Compatibility maps a path and constraint set to a bounded score, where higher values mean better fit.

**Boundary.** The scaffold does not specify a final scoring equation.

### 4. Compatible path subset

```text
P_C = {p in P | K(p, C) >= theta_K}
```

**Explanation.** The compatible path subset contains paths whose compatibility exceeds a chosen threshold.

**Boundary.** The threshold is a modeling convention, not an externally validated biological constant.

### 5. Constructive attractor concentration

```text
alpha(p, A) -> [0, 1]
```

**Explanation.** Attractor concentration estimates how strongly a path gathers around constructive attractor regions.

**Boundary.** A constructive attractor is not an intentional agent.

### 6. Apparent intentionality

```text
I_app(p, O) = O(K(p, C), alpha(p, A), context)
```

**Explanation.** Apparent intentionality is modeled as an observer projection over compatibility, attractor concentration, and context.

**Boundary.** The expression describes apparent purpose, not actual intention.

### 7. False intentionality

```text
I_false = I_app - I_intrinsic_support
```

**Explanation.** False intentionality is the excess purpose-like interpretation beyond intrinsic structural support.

**Boundary.** This is a conceptual difference, not a claim of directly measured mental intention.

### 8. Projection correction

```text
R(I_app) -> I_corrected
```

**Explanation.** The correction operator reduces observer-driven purpose attribution by re-weighting intrinsic support.

**Boundary.** The current correction is internally validated only.

### 9. Correction drop

```text
Delta_R = (I_false_before - I_false_after) / I_false_before
```

**Explanation.** Correction drop measures the proportional reduction of false intentionality after projection correction.

**Boundary.** The value is meaningful inside the model and does not establish external validation.

## Interpretive Flow

The intended manuscript logic is:

```text
constraints -> compatible paths -> attractor concentration -> observer projection -> apparent intentionality
```

This flow does not claim that a path has real intention. It claims that a path can become compatible, concentrated, and then interpreted as if it were directed toward an end.

A compact version is:

```text
C shapes P; K selects P_C; alpha highlights attractor concentration; O produces I_app.
```

False intentionality appears when `I_app` is stronger than the intrinsic structural support provided by compatibility and attractor concentration. Projection correction then tries to reduce this gap.

## Minimal Example Logic

- If K(p, C) is high, the path is compatible with the constraint set.
- If alpha(p, A) is high, the path concentrates around constructive attractors.
- If I_app is high while intrinsic support is low, the observer may be producing false intentionality.
- If Delta_R is high, projection correction has reduced observer-driven misreading.

## Manuscript Boundaries

- This scaffold is not a formal proof.
- This scaffold is not a complete mathematical theory.
- This scaffold is not externally validated.
- This scaffold does not model real pathogens or real hosts.
- This scaffold does not support biological protocols, laboratory procedures, or executable interventions.
- This scaffold does not support strong public claims.
- The notation is intended to clarify the manuscript before deeper formalization.

## Recommendations

- Convert the scaffold into a dedicated Formal Model section in the manuscript.
- Define the compatibility score more precisely in a later version.
- Separate intrinsic support from observer projection in all future validation reports.
- Avoid treating constructive attractors as agents.
- Keep the notation abstract until external validation exists.
- Use the notation to improve clarity, not to decorate uncertainty.

## Next Manuscript Step

The next manuscript step after this scaffold is integration: the notation should be inserted into the Formal Model section of the manuscript draft, then checked against the manuscript quality audit. The goal is not to make the paper look mathematical. The goal is to make the conceptual commitments explicit enough that they can be criticized, tested, and improved.
