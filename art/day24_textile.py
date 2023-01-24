from itertools import product
from math import pi
from random import random, seed

from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day24_textile.png"


def draw_line(
    context: Context,
    width: float,
    height: float,
) -> None:
    radius = width / 2 * (3 / 5 + random() * 1 / 5)
    with context.save():
        context.arc(width / 2, width / 2, radius, pi, 0)
        context.arc(
            width / 2,
            height - width / 2,
            radius,
            0,
            pi,
        )
        context.close_path()
        context.fill()


def draw(context: Context) -> None:
    seed(0)

    context.set_white()
    context.paint()

    n = 9
    tile_size = context.size / n

    splits = 9
    context.set_black()
    for i, j in product(range(n), repeat=2):
        with context.save():
            context.translate(
                (i + 0.5) * tile_size,
                (j + 0.5) * tile_size,
            )
            context.rotate(
                pi / 2 if (i + j) % 2 == 1 else 0,
            )
            context.translate(
                (-0.5) * tile_size,
                (-0.5) * tile_size,
            )
            for _ in range(splits):
                draw_line(
                    context,
                    tile_size / splits,
                    tile_size,
                )
                context.translate(tile_size / splits, 0)


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
