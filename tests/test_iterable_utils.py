import pytest

from cairo_utils.itertool_utils import get_first


def test_get_first_with_empty_iterable() -> None:
    with pytest.raises(RuntimeError):
        get_first(())


@pytest.mark.parametrize("input_", ((1,), (1, 2)))
def test_get_first(input_: tuple[int, ...]) -> None:
    first, output = get_first(input_)
    assert first == input_[0]
    assert tuple(output) == input_
