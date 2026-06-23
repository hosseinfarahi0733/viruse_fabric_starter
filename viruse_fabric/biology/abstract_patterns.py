from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ViralPattern:
    """Safe abstract viral pattern: no real pathogen parameters."""

    physical_compatibility: float
    information_compatibility: float
    heredity_compatibility: float

    @property
    def fabric_compatibility(self) -> float:
        return (
            0.4 * self.physical_compatibility
            + 0.35 * self.information_compatibility
            + 0.25 * self.heredity_compatibility
        )
