from itertools import cycle
from math import pi, sin, sqrt

from more_itertools import numeric_range

from cairo_utils import BLACK, WHITE, Context
from cairo_utils.core import write_to_png
from cairo_utils.geometry import from_radial

SIZE = 6_000
OUTPUT = "run/day12_tessellation.png"


def draw_triangle(
    context: Context,
    x: float,
    y: float,
    radius: float,
) -> None:
    side_length = sqrt(3) * radius
    for i in range(3):
        with context.save():
            xx, yy = from_radial(
                radius,
                i * pi * 2 / 3 + pi / 2,
            )
            context.translate(x + xx, y + yy)
            rotation = {
                0: 4 / 3 * pi,
                1: 0,
                2: pi * 2 / 3,
            }
            context.rotate(rotation[i])
            draw_sine_curve(context, int(side_length), side_length / 3)
    context.close_path()


def draw_sine_curve(context: Context, length: int, height: float) -> None:
    for x in range(length):
        offset = (
            1
            / 3
            * sin(
                x / length * 2 * pi,
            )
        )
        context.line_to(
            x,
            height * offset,
        )


def draw(context: Context) -> None:
    context.set_white()
    context.paint()

    radius = context.size / 12
    x_offset, _ = from_radial(radius, pi / 6)
    for colour, width in zip(
        cycle((WHITE, BLACK)),
        numeric_range(
            context.size / 10,
            0,
            -context.size / 100,
        ),
    ):
        for i in range(10):
            for j in range(10):
                draw_triangle(
                    context,
                    (2 * i + 1 - j % 2) * x_offset,
                    sqrt(3) * j * x_offset,
                    radius,
                )
                context.set_line_width(width)
                context.set_source_rgb(*colour)
                context.stroke()


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
