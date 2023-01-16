from itertools import cycle, product
from math import pi, sin

from cairo import LineCap

from cairo_utils import BLACK, WHITE, Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day15_sine.png"


def draw_sine_curve(
    context: Context,
    length: int,
    height: float,
    frequency: float,
) -> None:
    for x in range(length):
        offset = (
            1
            / 3
            * sin(
                x / length * frequency * 2 * pi,
            )
        )
        context.line_to(
            x,
            height * offset,
        )


def draw(context: Context) -> None:
    context.set_white()
    context.paint()

    context.set_line_cap(LineCap.ROUND)

    n = 5
    widths = (
        context.size / 50 * (1.2**width)
        for width in range(
            14,
            0,
            -1,
        )
    )
    for colour, width in zip(
        cycle((WHITE, BLACK)),
        widths,
    ):
        for is_vertical, offset in product(
            (False, True),
            range(0, n + 1),
        ):
            with context.save():
                if is_vertical:
                    context.translate(context.size / n * offset, 0)
                    context.rotate(pi / 2)
                else:
                    context.translate(0, context.size / n * offset)
                draw_sine_curve(context, context.size, -context.size / 6, 2)
                context.set_source_rgb(*colour)
                context.set_line_width(width)
                context.stroke()


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
