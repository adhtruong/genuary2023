from itertools import product
from random import random, seed

from cairo import LineCap

from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day14_aesemic.png"


def draw_letter(context: Context, tile_size: float) -> None:
    margin = tile_size / 6

    context.set_line_width(margin / 3)
    context.set_line_cap(LineCap.ROUND)

    context.set_black()
    context.line_to(tile_size / 2, margin)
    context.line_to(tile_size / 2, tile_size - margin)
    context.stroke()

    for start_y, end_x in product(
        (
            0,
            tile_size / 2 - margin,
            tile_size - 2 * margin,
        ),
        (
            (tile_size - margin) / 2,
            -(tile_size - margin) / 2,
        ),
    ):
        if random() < 0.5:
            continue

        context.line_to(tile_size / 2, margin + start_y)
        end = tile_size / 2 + end_x, margin + start_y
        context.line_to(*end)

        context.set_black()
        context.stroke()

        if random() < 0.6:
            continue

        context.circle(*end, margin / 4)
        context.set_white()
        context.fill_preserve()
        context.set_black()
        context.stroke()


def draw(context: Context) -> None:
    seed(0)

    context.set_white()
    context.paint()

    n = 11
    tile_size = context.size / n
    for y, x in product(range(n), repeat=2):
        with context.save():
            context.translate(
                tile_size * x,
                tile_size * y,
            )
            draw_letter(context, tile_size)


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
