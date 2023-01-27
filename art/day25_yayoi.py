from random import random, seed

from more_itertools import numeric_range

from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day25_yayoi.png"


def draw(context: Context) -> None:
    seed(0)

    context.set_black()
    context.paint()

    context.set_white()

    max_x = 10
    y_unit = context.size / 20
    for y in numeric_range(
        0,
        context.size + 1,
        y_unit,
    ):
        for x in range(max_x + 1):
            context.circle(
                x * context.size / 10,
                y,
                (random() + 1) * y_unit / 5,
            )
            context.fill()


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
