from itertools import cycle
from math import pi

from cairo import LineJoin

from cairo_utils import BLACK, WHITE, Context
from cairo_utils.core import write_to_png
from cairo_utils.geometry import from_radial

SIZE = 6_000
OUTPUT = "run/day08_sdf.png"


def draw_regular_shape(context: Context, n: int, radius: float) -> None:
    base_angle = 2 * pi / n
    for i in range(6):
        context.line_to(*from_radial(radius, i * base_angle))
    context.close_path()


def draw(context: Context) -> None:
    context.set_white()
    context.paint()

    context.translate(
        context.size / 2,
        context.size / 2,
    )
    context.set_line_join(LineJoin.ROUND)

    iterations = 21
    for idx, c in zip(range(iterations + 1), cycle((BLACK, WHITE))):
        context.set_source_rgb(*c)
        for angle_index in range(6):
            with context.save():
                context.translate(
                    *from_radial(context.size / 3, angle_index * 2 * pi / 6),
                )
                # context.circle(0, 0, context.size / 6)
                draw_regular_shape(context, 6, context.size / 3)
                context.set_line_width(
                    context.size / 3 * (1 - idx / iterations - 1 / (2 * iterations)),
                )
                context.stroke()

    return
    for i in range(6):
        context.set_black()
        draw_regular_shape(context, 6, context.size / 6)
        context.stroke()


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
