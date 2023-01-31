from itertools import cycle
from math import pi
from random import randint, random, seed

from more_itertools import numeric_range

from cairo_utils import Context
from cairo_utils.core import write_to_png
from cairo_utils.geometry import from_radial

SIZE = 6_000
OUTPUT = "run/day29_maximalism.png"


def draw_shape(
    context: Context,
    n: int,
    radius: float,
    offset: float,
) -> None:
    context.rotate(offset)
    angle = 2 * pi / n
    for i in range(n):
        context.line_to(*from_radial(radius, i * angle))
    context.close_path()


def draw(context: Context) -> None:
    seed(1)

    context.set_white()
    context.paint()

    for _ in range(1000):
        with context.save():
            context.translate(
                context.size * random(),
                context.size * random(),
            )
            n = randint(3, 7)
            offset = random() * 2 * pi
            radius = context.size / 12
            draw_shape(
                context,
                n,
                radius,
                offset,
            )
            context.clip_preserve()

            for color, line_width in zip(
                cycle((1, 0)),
                numeric_range(2 * radius, 0, -radius / 7),
            ):
                context.set_grey(color)
                context.set_line_width(line_width)
                context.stroke_preserve()

            context.new_path()


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
