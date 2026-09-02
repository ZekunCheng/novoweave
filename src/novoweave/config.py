"""Configuration schema for the conceptual framework."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, ConfigDict, Field


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class BackboneConfig(StrictModel):
    component: str
    num_steps: int = Field(ge=1, le=10_000)
    coordinate_scale: float = Field(gt=0)


class SequenceConfig(StrictModel):
    component: str
    temperature: float = Field(gt=0, le=10)
    num_candidates: int = Field(ge=1, le=10_000)


class EvaluationConfig(StrictModel):
    metrics: tuple[str, ...]
    require_human_review: bool = True


class OutputConfig(StrictModel):
    directory: Path
    save_intermediates: bool = False


class FrameworkConfig(StrictModel):
    schema_version: str
    project_name: str
    seed: int
    backbone: BackboneConfig
    sequence: SequenceConfig
    evaluation: EvaluationConfig
    output: OutputConfig

    @classmethod
    def from_yaml(cls, path: str | Path) -> FrameworkConfig:
        """Load a YAML file and reject unknown configuration fields."""
        payload: Any = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("Configuration root must be a mapping")
        return cls.model_validate(payload)

