from math import pi, sin

from more_itertools import numeric_range

from cairo_utils import Context
from cairo_utils.core import write_to_png
from cairo_utils.lerp import interpolate

SIZE = 6_000
OUTPUT = "run/day16_reflection.png"


def draw(context: Context) -> None:
    context.set_black()
    context.paint()

    context.translate(
        context.size / 2,
        context.size / 2,
    )
    length = context.size / 2
    diff = length / 30
    context.set_line_width(diff / 3)
    for centre_offset in numeric_range(diff * 5, length, diff):
        for i in range(32):
            with context.save():
                offset = centre_offset
                if i % 2 == 1:
                    offset += length / 30 * 7
                context.rotate(i * pi / 8)
                context.circle(
                    offset,
                    offset,
                    interpolate(
                        -1,
                        1,
                        length / 20,
                        length / 8,
                        sin(offset / length * 4 * 2 * pi),
                    ),
                )
                context.set_black()
                context.fill_preserve()
                context.set_white()
                context.stroke()


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
