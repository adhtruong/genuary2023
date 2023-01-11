from random import random, seed

from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day10_music.png"


N = 50


def draw_stave(context: Context, height: float) -> None:
    with context.save():
        for i in range(-1, 10):
            if i % 2 == 0:
                context.line_to(height, 0)
                context.line_to(context.size - height, 0)
                context.set_line_width(context.size / 500)
                context.stroke()

            for offset in range(1, 50):
                if random() < 0.15:
                    context.circle(
                        offset * context.size / N,
                        0,
                        height / 3,
                    )
                    context.fill()

            context.translate(0, height / 2)


def draw(context: Context) -> None:
    seed(0)

    context.set_white()
    context.paint()

    height = context.size / 50
    context.set_black()
    context.translate(0, 2 * height)
    for _ in range(10):
        draw_stave(context, height)
        context.translate(0, 7 * height)


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
