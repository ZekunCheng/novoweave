import pytest

from novoweave import DesignBrief


def test_valid_brief_passes_software_boundary_validation() -> None:
    brief = DesignBrief(name="example", length=100, objective="contract test")
    brief.validate()


@pytest.mark.parametrize("length", [0, 19, 2_001])
def test_invalid_length_is_rejected(length: int) -> None:
    brief = DesignBrief(name="example", length=length, objective="contract test")
    with pytest.raises(ValueError, match="length"):
        brief.validate()


def test_out_of_range_fixed_position_is_rejected() -> None:
    brief = DesignBrief(
        name="example",
        length=100,
        objective="contract test",
        fixed_positions=(101,),
    )
    with pytest.raises(ValueError, match="Fixed positions"):
        brief.validate()
