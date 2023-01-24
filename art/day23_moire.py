from itertools import product
from math import cos, pi, sin, sqrt
from random import randint, seed

from more_itertools import numeric_range

from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day23_moire.png"


def draw(context: Context) -> None:
    seed(1)

    context.set_white()
    context.paint()

    margin = context.size / 20
    n = 5
    tile_size = (context.size - margin * 2) / n

    context.set_black()
    context.set_line_width(tile_size / 40)

    for i, j in product(range(-1, n + 1), repeat=2):
        offset = randint(-2, 2)
        with context.save():
            context.translate(
                tile_size * (i + 0.5) + margin,
                tile_size * (j + 0.5) + margin,
            )

            diff = tile_size / 20
            for radius in numeric_range(
                tile_size * 2 / 3 + diff * offset,
                tile_size / 10,
                -diff,
            ):
                context.circle(0, 0, radius)
                context.stroke()

    return
    context.translate(
        context.size / 2,
        context.size / 2,
    )

    context.set_line_width(5)
    for _ in range(3):
        r = context.size / 50
        for n in range(10, 2000):
            r1 = r * sqrt(n)
            x = r1 * cos(n * 137.5)
            y = r1 * sin(n * 137.5)

            context.circle(x, y, 3)
            context.set_black()
            context.stroke()

        context.rotate(pi / 300)


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
