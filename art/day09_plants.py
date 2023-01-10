from itertools import cycle
from math import pi
from typing import Any, Callable

from cairo import LineCap

from cairo_utils import BLACK, WHITE, Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day09_plants.png"


def draw_segment(context: Context, length: float, renderer: Callable[[float], Any]) -> None:
    if length < context.size / 100:
        return

    renderer(length)

    with context.save():
        context.translate(0, -length)
        for angle in (pi * 3 / 2, pi / 2):
            with context.save():
                context.rotate(angle)
                draw_segment(
                    context,
                    length * 2 / 3,
                    renderer,
                )


def draw(context: Context) -> None:
    context.set_white()
    context.paint()

    context.translate(
        context.size / 2,
        context.size * 9 / 10,
    )

    context.set_line_cap(LineCap.ROUND)

    for color, line_width in zip(
        cycle((BLACK, WHITE)),
        range(6, 0, -1),
    ):
        context.set_source_rgb(*color)
        context.set_line_width(
            line_width * context.size * 5 / 1000,
        )

        def renderer(length: float) -> None:
            context.line_to(0, 0)
            context.line_to(0, -length)
            context.stroke()

        draw_segment(context, context.size * 2 / 5, renderer)


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
