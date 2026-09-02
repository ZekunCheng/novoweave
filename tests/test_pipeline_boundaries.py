from pathlib import Path

import pytest

from novoweave import DesignBrief, DesignPipeline


@pytest.mark.conceptual
def test_pipeline_refuses_to_claim_generation_capability() -> None:
    pipeline = DesignPipeline.from_config(Path("configs/base.yaml"))
    brief = DesignBrief(name="example", length=100, objective="boundary test")
    with pytest.raises(NotImplementedError, match="cannot design proteins"):
        pipeline.design(brief)
