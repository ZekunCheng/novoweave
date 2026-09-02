"""Top-level orchestration for the conceptual design workflow."""

from __future__ import annotations

from pathlib import Path

from novoweave.config import FrameworkConfig
from novoweave.contracts import DesignBrief, DesignResult
from novoweave.evaluation import PlaceholderEvaluator
from novoweave.models import (
    GeometricDiffusionBackbone,
    StructureConditionedTransformer,
)


class DesignPipeline:
    """Wire typed components together while keeping capability boundaries clear."""

    def __init__(self, config: FrameworkConfig) -> None:
        self.config = config
        self.backbone_generator = GeometricDiffusionBackbone(config.backbone)
        self.sequence_designer = StructureConditionedTransformer(config.sequence)
        self.evaluator = PlaceholderEvaluator()

    @classmethod
    def from_config(cls, path: str | Path) -> DesignPipeline:
        return cls(FrameworkConfig.from_yaml(path))

    def design(self, brief: DesignBrief) -> DesignResult:
        """Validate the request, then stop at the non-functional model boundary."""
        brief.validate()
        raise NotImplementedError(
            "This repository defines the workflow contract but cannot design proteins"
        )
