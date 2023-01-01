from dataclasses import dataclass
from functools import cache
from math import cos, pi, sin
from typing import Iterable

from cairo_utils import Context
from cairo_utils.core import write_to_png
from cairo_utils.lerp import lerp
from cairo_utils.video import get_renderer

SIZE = 3_000
BASE_OUTPUT = "run/day01_perfect_loop"
IMAGE_OUTPUT = BASE_OUTPUT + ".png"
VIDEO_OUTPUT = BASE_OUTPUT + ".mp4"


@cache
def from_radial(radius: float, angle: float) -> tuple[float, float]:
    return (
        radius * cos(angle),
        radius * sin(angle),
    )


@dataclass(frozen=True)
class Circle:
    x: float
    y: float
    radius: float
    grey: float


def draw_arc(
    context: Context,
    arc_index: int,
    offset: float,
) -> Iterable[Circle]:
    arc_width = context.size / 30
    density = 1000
    arcs = 2

    for i in range(density):
        grey = (i % (density / arcs)) / (density / arcs)
        circle = Circle(
            *from_radial(
                arc_width * 2 * (arc_index + 1),
                2 * pi * (i / density + offset),
            ),
            arc_width / 2,
            lerp(0.2, 1, grey),
        )
        yield circle


def draw(context: Context, offset: float) -> None:
    context.set_black()
    context.paint()
    context.translate(
        context.size / 2,
        context.size / 2,
    )
    for arc_index in range(7):
        for circle in sorted(
            draw_arc(context, arc_index, offset),
            key=lambda circle: circle.grey,
        ):
            context.set_grey(circle.grey)
            context.circle(circle.x, circle.y, circle.radius)
            context.fill()


def main() -> None:
    with write_to_png(6000, IMAGE_OUTPUT) as context:
        draw(context, 0)

    frames = 120
    for frame, context in enumerate(
        get_renderer(SIZE, frames, 30, VIDEO_OUTPUT),
    ):
        draw(context, frame / frames)


if __name__ == "__main__":
    main()
