from itertools import product
from math import cos, pi, sin
from random import random, seed

from cairo import LineCap, LineJoin

from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day02_ten_minutes.png"


def from_radial(radius: float, angle: float) -> tuple[float, float]:
    return (
        radius * cos(angle),
        radius * sin(angle),
    )


def draw_clock(context: Context, size: float) -> None:
    context.set_line_join(LineJoin.ROUND)
    context.set_line_cap(LineCap.ROUND)
    context.set_line_width(size / 20)

    context.set_black()
    for i in range(12):
        context.line_to(
            *from_radial(size * 0.9, i / 12 * 2 * pi),
        )
        context.line_to(
            *from_radial(size, i / 12 * 2 * pi),
        )
        context.stroke()

    context.set_line_width(size / 40)

    angle = random() * 2 * pi
    ten_minutes_angle_minute = pi / 3
    context.line_to(0, 0)
    context.line_to(*from_radial(size, angle))
    context.arc(
        0,
        0,
        size,
        angle,
        angle + ten_minutes_angle_minute,
    )
    context.close_path()

    context.set_white()
    context.fill_preserve()

    context.set_black()
    context.stroke()


def draw(context: Context) -> None:
    seed(0)

    context.set_white()
    context.paint()

    n = 5
    tile_size = context.size / n
    margin = tile_size / 10
    for x, y in product(range(n), repeat=2):
        with context.save():
            context.translate(
                (x + 0.5) * tile_size,
                (y + 0.5) * tile_size,
            )
            draw_clock(
                context,
                (tile_size - 2 * margin) / 2,
            )


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
