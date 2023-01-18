from dataclasses import dataclass
from itertools import cycle, product
from random import random, seed
from typing import Iterable

from more_itertools import numeric_range

from cairo_utils import BLACK, WHITE, Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day17_grid.png"


@dataclass(frozen=True)
class Square:
    x: float
    y: float
    size: float


def get_squares(
    x: float,
    y: float,
    size: float,
    n: int = 2,
    iterations: int = 4,
) -> Iterable[Square]:
    yield Square(x, y, size)
    if iterations <= 0:
        return

    tile_size = size / n
    for i, j in product(range(n), repeat=2):
        if random() < 0.5 - iterations * 0.1:
            continue

        yield from get_squares(
            x + i * tile_size,
            y + j * tile_size,
            tile_size,
            iterations=iterations - 1,
        )


def draw(context: Context) -> None:
    seed(2)

    context.set_white()
    context.paint()

    margin = context.size / 25
    squares = list(
        get_squares(
            margin,
            margin,
            context.size - 2 * margin,
        ),
    )
    for color, width in zip(
        cycle((BLACK, WHITE)),
        numeric_range(
            context.size / 30,
            0,
            -context.size / 150,
        ),
    ):
        context.set_source_rgb(*color)
        context.set_line_width(width)
        for square in squares:
            context.square(
                square.x,
                square.y,
                square.size,
            )
            context.stroke()


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
