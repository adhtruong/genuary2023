from itertools import product

from cairo import RadialGradient

from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day22_shadows.png"


def draw(context: Context) -> None:
    context.set_white()
    context.paint()

    context.set_line_width(10)
    n = 9
    square_size = context.size / n

    pattern = RadialGradient(0, 0, 0, 0, 0, square_size / 4)
    pattern.add_color_stop_rgb(0, 0, 0, 0)
    pattern.add_color_stop_rgb(1, 1, 1, 1)

    for i, j in product(range(n), repeat=2):
        x_offset = 0.05 * (i - 3)
        y_offset = 0.05 * (j - 3)
        with context.save():
            context.translate(
                (i + 0.5 + x_offset) * square_size,
                (j + 0.5 + y_offset) * square_size,
            )
            context.circle(0, 0, square_size / 4)
            context.set_source(pattern)
            context.fill()

        context.circle(
            (i + 0.5) * square_size,
            (j + 0.5) * square_size,
            square_size / 4,
        )
        context.set_white()
        context.fill()


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
