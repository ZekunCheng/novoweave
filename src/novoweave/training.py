"""Pseudocode training orchestration for future model implementations."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class TrainingManifest:
    dataset_revision: str
    split_revision: str
    config_digest: str
    code_revision: str
    random_seed: int


class ConceptualTrainer:
    """Documents a reproducible trainer contract without training a model."""

    def fit(self, model: Any, data_module: Any, manifest: TrainingManifest) -> None:
        """Planned loop: validate provenance, train, evaluate, checkpoint, audit."""
        raise NotImplementedError("Training logic and datasets are intentionally absent")

    def evaluate(self, model: Any, data_module: Any) -> dict[str, float]:
        """Planned held-out evaluation with uncertainty and subgroup reporting."""
        raise NotImplementedError("Benchmark definitions are intentionally absent")

