import pytest

from cairo_utils.lerp import interpolate, lerp
from cairo_utils.point import Point


@pytest.mark.parametrize(
    ("a", "b", "t", "expected"),
    (
        (0, 1, 0.5, 0.5),
        (1, 3, 0.5, 2),
        (0.5, -1, 0, 0.5),
        (0.5, -2, 0.8, -1.5),
    ),
)
def test_lerp(a: float, b: float, t: float, expected: float) -> None:
    assert lerp(a, b, t) == expected


@pytest.mark.parametrize(
    ("args", "expected"),
    (
        ((1, 3, 1, 5, 1), 1),
        ((1, 3, 1, 5, 2), 3),
        ((1, -1, -1, 1, 2), -2),
    ),
)
def test_interpolate(args: tuple[float, float, float, float, float], expected: float) -> None:
    assert interpolate(*args) == expected


def test_point_interpolate() -> None:
    assert Point(0.5, -1) == interpolate(0, 10, Point(0, 1), Point(5, -19), 1)
