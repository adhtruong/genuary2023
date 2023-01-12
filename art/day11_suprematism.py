from random import random, seed

from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day11_suprematism.png"


def form(context: Context, x: float, y: float, w: float, h: float) -> None:
    context.rectangle(x, y, w, h)
    context.fill()
    with context.save():
        context.translate(x, y)
        context.set_white()
        for _ in range(int(x * y / 500)):
            context.circle(
                random() * w,
                random() * h,
                (random() + 0.1) * w / 800,
            )
            context.fill()


def draw(context: Context) -> None:
    seed(5)

    context.set_white()
    context.paint()

    for _ in range(30):
        context.set_grey(random() * 0.15)
        square_size = context.size / 4 * (random() + 0.2)
        form(
            context,
            # *(
            #     x + context.size / 2 - square_size / 2
            #     for x in from_radial(
            #         random() * context.size / 3,
            #         random() * 2 * pi,
            #     )
            # ),
            context.size * random() - square_size / 2,
            context.size * random() - square_size / 2,
            square_size,
            square_size,
        )


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
