from __future__ import annotations

import numpy as np
from viruse_fabric.core.node import Coord6D


def spatial_distance2(a: Coord6D, b: Coord6D) -> float:
    d = b.space - a.space
    return float(np.dot(d, d))


def temporal_distance2(a: Coord6D, b: Coord6D, c=(1.0, 1.0, 1.0)) -> float:
    dt = b.time - a.time
    c_arr = np.asarray(c, dtype=float)
    return float(np.dot(c_arr * dt, c_arr * dt))


def causal_interval(a: Coord6D, b: Coord6D, c=(1.0, 1.0, 1.0)) -> float:
    """Positive means time-like dominance in this toy 3+3 model."""

    return temporal_distance2(a, b, c=c) - spatial_distance2(a, b)


def orientation(a: Coord6D, b: Coord6D, omega=(1.0, 1.0, 1.0)) -> float:
    """Projection of the 3-time delta onto a causal orientation vector."""

    dt = b.time - a.time
    return float(np.dot(np.asarray(omega, dtype=float), dt))
