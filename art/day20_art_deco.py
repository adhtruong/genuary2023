from itertools import product
from math import pi

from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day20_art_deco.png"


def draw_pattern(context: Context, radius: float) -> None:
    context.set_white()

    context.line_to(0, -radius)
    context.line_to(0, radius)
    context.stroke()

    context.arc(0, 0, radius, pi, 0)
    context.stroke()

    context.circle(0, 0, radius)
    context.clip()

    for radius_offset in (1, 2, 4, 8):
        for offset in (1, -1):
            context.circle(
                offset * radius_offset * radius,
                radius,
                radius_offset * radius,
            )
            context.stroke()


def draw(context: Context) -> None:
    context.set_black()
    context.paint()

    context.set_black()
    context.set_line_width(context.size / 300)

    n = 14
    tile_size = context.size / n
    for j, i in product(range(n + 1), repeat=2):
        with context.save():
            if j % 2 == 0:
                rotation = i % 2 * 2 + j % 4 + 1
            else:
                rotation = i % 2 * 2 + j % 4 + 3

            context.translate(
                (i - (j % 2) / 2) * tile_size * 2,
                j * tile_size,
            )
            context.rotate(rotation * pi / 2)
            draw_pattern(context, tile_size)


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
