from itertools import product
from math import pi, sqrt

from cairo_utils import Context
from cairo_utils.core import write_to_png
from cairo_utils.geometry import from_radial

SIZE = 6_000
OUTPUT = "run/day04_intersections.png"


def draw_polygon(
    context: Context,
    n: int,
    radius: float,
    offset: float = 0,
) -> None:
    for i in range(n):
        context.line_to(
            *from_radial(radius, 2 * pi * i / n + offset),
        )
    context.close_path()


def draw(context: Context) -> None:
    context.set_white()
    context.paint()

    context.translate(
        context.size / 2,
        context.size / 2,
    )

    context.rotate(pi / 4)

    n = 14
    minor_squares = 3
    for x, y in product(
        range(-1, minor_squares - 1),
        repeat=2,
    ):
        if x == y == 0:
            continue
        color = 0.2 if (x + y) % 2 != 0 else 0.2
        context.set_black(color)

        with context.save():
            context.translate(
                context.size / minor_squares / sqrt(2) * x,
                context.size / minor_squares / sqrt(2) * y,
            )
            for offset in range(n):
                draw_polygon(
                    context,
                    3,
                    context.size * sqrt(2) / 4 / minor_squares,
                    2 * pi * offset / n,
                )
                context.fill()


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
