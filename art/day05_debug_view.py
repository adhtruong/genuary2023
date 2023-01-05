from itertools import accumulate
from random import randint, random, seed

from more_itertools import pairwise

from cairo_utils import Context
from cairo_utils.core import write_to_png
from cairo_utils.lerp import lerp

SIZE = 6_000
OUTPUT = "run/day05_debug_view_{}.png"


def get_random_sum(n: int) -> list[float]:
    raw = [random() for _ in range(n)]
    sum_ = sum(raw)
    return [value / sum_ for value in raw]


def draw_bar(
    context: Context,
    max_: int,
    start: float,
    end: float,
    size: float,
    generation: int = 0,
) -> None:
    with context.save():
        context.translate(
            start,
            -size,
        )
        context.rectangle(0, 0, end - start, size)
        context.set_black(lerp(0.85, 1, random()))
        context.fill_preserve()
        context.set_white()
        context.stroke()

        if generation >= max_:
            return
        children = randint(1, max_ - generation)
        current_size = end - start
        initial = random() * 0.01
        current_size *= 1 - initial
        values = get_random_sum(children)
        for new_start, new_end in pairwise(
            accumulate(values, initial=initial),
        ):
            if random() < 0.1:
                continue

            draw_bar(
                context,
                max_,
                new_start * current_size,
                new_end * current_size,
                size,
                generation + 1,
            )


def draw(context: Context, seed_: int) -> None:
    seed(seed_)

    context.set_white()
    context.paint()

    margin = context.size / 20
    context.translate(0, context.size * 3 / 4)
    draw_bar(
        context,
        10,
        margin,
        context.size - margin,
        margin,
    )


def main() -> None:
    for i in range(5):
        output = OUTPUT.format(i)
        with write_to_png(SIZE, output) as context:
            draw(context, i)


if __name__ == "__main__":
    main()
