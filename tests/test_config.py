from pathlib import Path

import pytest
from pydantic import ValidationError

from novoweave.config import FrameworkConfig


def test_example_config_is_valid() -> None:
    config = FrameworkConfig.from_yaml(Path("configs/base.yaml"))
    assert config.schema_version == "1.0"
    assert config.evaluation.require_human_review is True


def test_unknown_fields_are_rejected(tmp_path: Path) -> None:
    path = tmp_path / "bad.yaml"
    path.write_text(
        """
schema_version: '1.0'
project_name: test
seed: 1
unexpected: true
backbone: {component: placeholder, num_steps: 1, coordinate_scale: 1.0}
sequence: {component: placeholder, temperature: 1.0, num_candidates: 1}
evaluation: {metrics: [], require_human_review: true}
output: {directory: artifacts, save_intermediates: false}
""",
        encoding="utf-8",
    )
    with pytest.raises(ValidationError):
        FrameworkConfig.from_yaml(path)
