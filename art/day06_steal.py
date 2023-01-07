from itertools import product
from random import random, seed

from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day06_steal.png"


def draw(context: Context) -> None:
    seed(0)

    context.set_white()
    context.paint()

    n = 16
    tile_size = context.size / n
    for x, y in product(range(n + 1), repeat=2):
        with context.save():
            context.translate(
                x * tile_size,
                y * tile_size,
            )
            context.move_to(0, 0)
            context.line_to(tile_size, -tile_size)
            context.line_to(tile_size, 0)
            context.line_to(0, tile_size)
            context.close_path()
            context.set_grey(random())
            context.stroke_preserve()
            context.fill()


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
