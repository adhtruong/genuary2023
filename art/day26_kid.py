from itertools import product
from math import cos, pi, sin

from more_itertools import numeric_range

from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day26_kid.png"


def get_point(
    radius: float,
    k: float,
    l: float,
    t: float,
) -> tuple[float, float]:
    return (
        radius * ((1 - k) * cos(t) + l * k * cos((1 - k) * k * t)),
        radius * ((1 - k) * sin(t) + l * k * sin((1 - k) * k * t)),
    )


def draw(context: Context) -> None:
    context.set_white()
    context.paint()

    context.set_black()
    context.set_line_width(context.size / 300)

    n = 3
    for i, j in product(range(n), repeat=2):
        with context.save():
            context.translate(
                context.size / n * (i + 0.5),
                context.size / n * (j + 0.5),
            )

            l_ = 1 - (i + 1) * 1 / 6
            k = 1 - (j + 1) * 1 / 6
            for t in numeric_range(
                0,
                20 * (i + 2) * (j + 2) * pi,
                0.01,
            ):
                context.line_to(
                    *get_point(
                        context.size / (n * 2),
                        l_,
                        k,
                        t,
                    ),
                )
            context.stroke()


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
