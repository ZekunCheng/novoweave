"""Typed boundaries shared by the conceptual pipeline components."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol


@dataclass(frozen=True, slots=True)
class DesignBrief:
    """Human-authored constraints for one conceptual design run."""

    name: str
    length: int
    objective: str
    symmetry: str | None = None
    fixed_positions: tuple[int, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        """Validate software-level boundaries, not biological feasibility."""
        if not self.name.strip():
            raise ValueError("Design brief name must not be empty")
        if not 20 <= self.length <= 2_000:
            raise ValueError("Conceptual length must be between 20 and 2000")
        if not self.objective.strip():
            raise ValueError("Objective must not be empty")
        if any(position < 1 or position > self.length for position in self.fixed_positions):
            raise ValueError("Fixed positions must use one-based indices within length")


@dataclass(frozen=True, slots=True)
class BackboneCandidate:
    """Opaque placeholder for a generated backbone representation."""

    candidate_id: str
    coordinates: Any
    provenance: dict[str, Any]


@dataclass(frozen=True, slots=True)
class SequenceCandidate:
    """Opaque placeholder for a structure-conditioned sequence."""

    candidate_id: str
    sequence: str
    parent_backbone_id: str
    provenance: dict[str, Any]


@dataclass(frozen=True, slots=True)
class RankedCandidate:
    """Candidate plus transparent, non-validated ranking metadata."""

    sequence_candidate: SequenceCandidate
    scores: dict[str, float]
    rank: int


@dataclass(frozen=True, slots=True)
class DesignResult:
    """Audit-friendly output contract for a future implementation."""

    run_id: str
    brief: DesignBrief
    candidates: tuple[RankedCandidate, ...]
    manifest_path: Path
    warnings: tuple[str, ...]


class BackboneGenerator(Protocol):
    """Contract for models that propose backbone candidates."""

    def sample(self, brief: DesignBrief, *, seed: int) -> list[BackboneCandidate]: ...


class SequenceDesigner(Protocol):
    """Contract for structure-conditioned sequence models."""

    def design(
        self, backbones: list[BackboneCandidate], *, seed: int
    ) -> list[SequenceCandidate]: ...


class CandidateEvaluator(Protocol):
    """Contract for auditable in-silico evaluation adapters."""

    def score(self, candidate: SequenceCandidate) -> dict[str, float]: ...

