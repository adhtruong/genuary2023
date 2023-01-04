from itertools import cycle
from math import pi, sqrt
from random import random, seed

from more_itertools import numeric_range

from cairo_utils import Context
from cairo_utils.core import BLACK, WHITE, write_to_png
from cairo_utils.geometry import from_radial

SIZE = 6_000
OUTPUT = "run/day03_glitch.png"


def draw_circle(
    context: Context,
    size: float,
    circle_size: float,
) -> None:
    n = 80
    gap = size / n
    max_offset = size / 20

    for y in range(n):
        with context.save():
            offset = (random() - 0.5) * max_offset
            context.rectangle(
                -size / 2,
                -size / 2 + y * gap,
                size,
                gap,
            )
            context.clip()

            for color, current in zip(
                cycle((BLACK, WHITE)),
                numeric_range(1, 0, -0.05),
            ):
                context.set_source_rgb(*color)
                context.set_line_width(gap)
                context.circle(
                    offset,
                    0,
                    circle_size * current,
                )
                context.stroke()


def draw(context: Context) -> None:
    seed(0)

    context.set_white()
    context.paint()

    context.translate(
        context.size / 2,
        context.size / 2,
    )

    draw_circle(
        context,
        size=context.size / 2,
        circle_size=context.size / 7,
    )

    for shrink, angle_offset in (
        (1 / 3, 0),
        (sqrt(3) * 1 / 3, 0.5),
        (2 / 3, 1),
    ):
        for i in range(6):
            with context.save():
                context.translate(
                    *from_radial(
                        context.size * shrink,
                        (i + angle_offset) * pi / 3,
                    ),
                )
                draw_circle(
                    context,
                    size=context.size / 2,
                    circle_size=context.size * 1 / 7,
                )


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
