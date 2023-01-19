from dataclasses import dataclass
from itertools import product
from math import pi, sqrt
from random import sample
from typing import Iterable

from cairo_utils import Context
from cairo_utils.core import write_to_png
from cairo_utils.geometry import from_radial

SIZE = 6_000
OUTPUT = "run/day19_black_and_white.png"


@dataclass
class Hexagon:
    x: float
    y: float

    def draw(
        self,
        context: Context,
        radius: float,
    ) -> None:
        with context.save():
            context.translate(self.x, self.y)
            for i in range(6):
                context.line_to(
                    *from_radial(radius, i * 2 * pi / 6 + pi / 2),
                )
            context.close_path()


def get_hexagons(radius: float) -> Iterable[Hexagon]:
    for i, j in product(range(15), range(45)):
        yield Hexagon(
            (i + (j % 2) / 2) * radius * sqrt(3),
            j * 0.5 * radius,
        )


def draw(context: Context) -> None:
    context.set_white()
    context.paint()

    context.set_line_width(context.size / 50)

    radius = context.size / 18
    input_ = list(get_hexagons(radius))
    hexagons = sample(input_, len(input_))
    for hexagon in hexagons:
        for r in (
            radius,
            radius * 2 / 3,
            radius / 3,
        ):
            hexagon.draw(context, r)
            context.set_black()
            context.stroke_preserve()
            context.set_white()
            context.fill()


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
