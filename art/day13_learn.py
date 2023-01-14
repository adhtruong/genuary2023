from itertools import cycle, product

from cairo import RadialGradient
from more_itertools import numeric_range

from cairo_utils import BLACK, WHITE, Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day13_learn.png"


def draw_square(context: Context, size: float, swap: bool) -> None:
    pattern = RadialGradient(
        size / 2,
        size / 2,
        0,
        size / 2,
        size / 2,
        size / 2,
    )
    color_iterable = cycle((BLACK, WHITE))
    if swap:
        next(color_iterable, None)
    for color, stop_size in zip(
        color_iterable,
        numeric_range(0, 1.2, 0.2),
    ):
        pattern.add_color_stop_rgb(stop_size, *color)
    context.set_source(pattern)
    context.square(0, 0, size)
    context.fill()


def draw(context: Context) -> None:
    context.set_white()
    context.paint()

    n = 3
    tile_size = context.size / n
    for i, j in product(range(n), repeat=2):
        with context.save():
            context.translate(i * tile_size, j * tile_size)
            draw_square(context, tile_size, bool((i + j) % 2))


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
