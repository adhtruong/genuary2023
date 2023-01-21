from math import pi, sin
from typing import Callable, Iterable

from cairo import LineCap, LineJoin

from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 6_000
OUTPUT = "run/day21_persian_rug.png"


def draw_sine_curve(
    context: Context,
    length: int,
    height: float,
    period: float = 1,
) -> None:
    for x in range(length):
        offset = (
            1
            / 3
            * sin(
                period * x / length * 2 * pi,
            )
        )
        context.line_to(
            x,
            height * offset,
        )


def draw_boundary(
    context: Context,
    foreground: int,
    background: int,
    margin: float,
    stroke: Callable[[Context], None],
) -> None:
    offset = 0
    tile_size = context.size - offset * 2

    with context.save():
        context.translate(
            offset + margin / 2,
            offset + margin / 2,
        )
        context.rotate(pi / 2)
        for _ in range(4):
            draw_sine_curve(
                context,
                int(tile_size - margin),
                margin,
                period=4.5,
            )

            context.translate(tile_size - margin, 0)
            context.rotate(-pi / 2)

        context.close_path()
        stroke(context)

    context.square(
        offset + margin,
        offset + margin,
        tile_size - 2 * margin,
    )
    stroke(context)

    context.square(
        0,
        0,
        context.size,
    )
    stroke(context)


def rotate_repeat(context: Context, n: int) -> Iterable[int]:
    rotation = 2 * pi / n
    with context.save():
        for i in range(n):
            context.rotate(rotation)
            with context.save():
                yield i


def draw_branch(
    context: Context,
    stroke: Callable[[Context], None],
    tile_size: float,
) -> None:
    minor_size = tile_size / 30
    major_size = tile_size / 18
    for _ in rotate_repeat(context, 4):
        context.circle(tile_size / 4, 0, major_size)
        stroke(context)
        context.circle(
            (tile_size / 2 + major_size + tile_size / 4 - minor_size) / 2,
            0,
            (major_size + minor_size) / 2,
        )
        stroke(context)
        context.circle(tile_size / 2, 0, minor_size)
        stroke(context)


def draw(context: Context) -> None:
    background, foreground = 0, 1

    context.set_grey(background)
    context.paint()
    context.set_line_cap(LineCap.ROUND)
    context.set_line_join(LineJoin.ROUND)

    margin = context.size / 12

    for color, line_width in (
        (foreground, margin / 4),
        (background, margin / 12),
    ):

        def stroke(c: Context) -> None:
            c.set_grey(color)
            c.set_line_width(line_width)
            c.stroke()

        draw_boundary(
            context,
            foreground=foreground,
            background=background,
            margin=margin,
            stroke=stroke,
        )

        with context.save():
            tile_size = context.size - 2 * margin
            context.square(
                margin,
                margin,
                tile_size,
            )
            context.clip()

            context.translate(
                context.size / 2,
                context.size / 2,
            )
            for centre_size in (
                13 / 100,
                10 / 100,
                7 / 100,
                4 / 100,
            ):
                square_size = context.size * centre_size
                context.square(
                    -square_size,
                    -square_size,
                    square_size * 2,
                )
                stroke(context)

            draw_branch(context, stroke, tile_size)
            for _ in rotate_repeat(context, 4):
                context.translate(
                    tile_size / 2,
                    tile_size / 2,
                )

                for circle_size, number_circles in (
                    (7 / 18, None),
                    (6 / 18, 24),
                    (5 / 18, None),
                    (4 / 18, 20),
                    (3 / 18, None),
                    (2 / 18, 8),
                ):
                    if number_circles is None:
                        context.circle(
                            0,
                            0,
                            context.size * circle_size,
                        )
                        context.stroke()
                    else:
                        for _ in rotate_repeat(
                            context,
                            number_circles,
                        ):
                            context.circle(
                                0,
                                context.size * circle_size,
                                margin / 6,
                            )
                            stroke(context)


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
