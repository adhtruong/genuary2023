from itertools import cycle, product
from random import random, seed
from typing import Iterator

from more_itertools import numeric_range

from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 6_600
OUTPUT = "run/day30_minimalism.png"


def draw(context: Context) -> None:
    seed(2)

    context.set_white()
    context.paint()

    n = 13
    tile_size = context.size / n

    for i, j in product(range(n), repeat=2):
        with context.save():
            context.square(i * tile_size, j * tile_size, tile_size)
            context.clip()
            colors = cycle((1, 0))
            if random() < 0.3:
                next(colors)

            def get_radius() -> Iterator[float]:
                r: float = context.size
                while r > context.size / 30:
                    yield r
                    r *= 0.95

            for color, radius in zip(
                colors,
                get_radius()
                # numeric_range(
                #     context.size,
                #     0,
                #     -context.size / 30,
                # ),
            ):
                context.circle(
                    context.size / 2,
                    context.size / 2,
                    radius,
                )
                context.set_grey(color)
                context.fill()
    return

    context.size / 4
    for control in numeric_range(
        context.size / 4,
    ):
        context.line_to(0, -context.size / 4)
        context.curve_to(
            control,
            control / 2,
            control,
            -control / 2,
            0,
            context.size / 4,
        )
        context.stroke()


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
