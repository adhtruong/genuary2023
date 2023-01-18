from math import pi
from random import random, seed
from typing import Iterable, NamedTuple

from cairo_utils import Context
from cairo_utils.core import write_to_png
from cairo_utils.geometry import from_radial

SIZE = 6_000
OUTPUT = "run/day18_not_grid.png"


class Circle(NamedTuple):
    x: float
    y: float
    radius: float


def get_circles(size: float) -> Iterable[Circle]:
    for _ in range(60):
        centre: tuple[float, float] = tuple(  # type: ignore[assignment]
            pos + size / 2
            for pos in from_radial(
                size / 2 * random(),
                2 * pi * random(),
            )
        )
        yield Circle(
            *centre,
            (random() + 0.15) * size / 20,
        )


def draw(context: Context) -> None:
    seed(1)

    context.set_white()
    context.paint()

    circles = list(get_circles(context.size))

    context.set_black()
    n = 40
    diff = context.size / n
    context.set_line_width(diff / 2)
    for i in range(n + 1):
        with context.save():
            context.translate(0, i * diff)
            context.line_to(0, 0)
            context.line_to(context.size, 0)
            context.stroke()

    context.set_white()
    for circle in circles:
        context.circle(*circle)
        context.fill()

    context.set_black()
    for circle in circles:
        with context.save():
            context.circle(*circle)
            context.clip()

            for i in range(n + 1):
                with context.save():
                    context.translate(i * diff, 0)
                    context.line_to(0, 0)
                    context.line_to(0, context.size)
                    context.stroke()


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
