from cairo_utils.point import Point


def test_point_add() -> None:
    assert Point(1, 1) == Point(0.5, 1.5) + Point(0.5, -0.5)


def test_point_subtract() -> None:
    assert Point(0, 2) == Point(0.5, 1.5) - Point(0.5, -0.5)
