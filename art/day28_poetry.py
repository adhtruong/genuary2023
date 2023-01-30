from itertools import accumulate
from random import randint, random, sample, seed

from cairo import LineCap

from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day28_poetry.png"


def constrained_sum_sample_pos(n: int, total: int) -> list[int]:
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""

    dividers = sorted(sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]


def draw_haiku(context: Context, size: float) -> None:
    gap = size / 2
    for line in (5, 7, 5):
        context.translate(0, size)
        with context.save():
            context.translate(gap, 0)

            words = constrained_sum_sample_pos(
                randint(2, line - 2),
                line,
            )
            for word in words:
                current = list(
                    accumulate(
                        range(word),
                        lambda current, _: current + gap * (1 + random() * 2),
                        initial=0.0,
                    )
                )
                context.line_to(0, 0)
                context.line_to(current[-1], 0)
                context.set_black()
                context.stroke()

                for syllable in current[:-1]:
                    context.circle(syllable, 0, gap / 3)
                    context.set_white()
                    context.fill_preserve()
                    context.set_black()
                    context.stroke()

                context.translate(current[-1] + gap, 0)


def draw(context: Context) -> None:
    seed(0)

    context.set_white()
    context.paint()

    context.set_black()
    context.set_line_width(context.size / 100)
    context.set_line_cap(LineCap.ROUND)

    for _ in range(3):
        draw_haiku(context, context.size / 12)
        context.translate(0, context.size / 12)


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
