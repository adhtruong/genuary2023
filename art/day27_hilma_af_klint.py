from itertools import cycle
from math import pi
from random import random, seed

from more_itertools import numeric_range, pairwise

from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day27_hilma_af_klint.png"


def draw(context: Context) -> None:
    seed(1)

    context.set_white()
    context.paint()

    context.translate(
        context.size / 2,
        context.size * 2 / 5,
    )

    for index_offset, offset in enumerate(
        (pi / 2, -pi / 2),
    ):
        colors = cycle((0, 1))
        if index_offset:
            next(colors)
        for radius in numeric_range(
            context.size / 3,
            0,
            -context.size / 30,
        ):
            context.arc(0, 0, radius, offset, offset + pi)
            context.close_path()
            context.set_grey(next(colors))
            context.fill()

            if random() < 0.15:
                next(colors)

    colors = cycle((0, 1))
    for start, end in pairwise(
        (
            *numeric_range(pi / 4, 3 / 4 * pi, pi / 36),
            3 / 4 * pi,
        )
    ):
        context.line_to(0, 0)
        context.arc(0, 0, context.size * 2, start, end)
        context.close_path()
        context.set_grey(next(colors))
        context.stroke_preserve()
        context.fill()

        if random() < 0.15:
            next(colors)


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
