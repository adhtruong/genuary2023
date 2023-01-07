from math import sqrt

from cairo import LineCap

from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 8_000
OUTPUT = "run/day07_palette.png"

_PALETTE = [
    ((237, 237, 237, 255), 12376),
    ((236, 236, 236, 255), 11550),
    ((238, 238, 238, 255), 4589),
    ((235, 235, 235, 255), 3772),
    ((234, 234, 232, 255), 2333),
    ((235, 234, 232, 255), 2181),
    ((236, 235, 233, 255), 2065),
    ((235, 235, 233, 255), 2045),
    ((233, 233, 231, 255), 2042),
    ((234, 233, 231, 255), 1692),
    ((237, 236, 234, 255), 1320),
    ((236, 236, 234, 255), 1314),
    ((232, 232, 230, 255), 1268),
    ((233, 232, 230, 255), 1047),
    ((227, 226, 222, 255), 857),
    ((226, 225, 221, 255), 818),
    ((225, 224, 220, 255), 805),
    ((228, 227, 223, 255), 741),
    ((231, 231, 229, 255), 653),
    ((224, 223, 219, 255), 601),
    ((237, 237, 235, 255), 582),
    ((229, 228, 224, 255), 551),
    ((239, 239, 239, 255), 535),
    ((232, 231, 229, 255), 513),
    ((238, 237, 235, 255), 504),
    ((0, 0, 0, 255), 498),
    ((234, 234, 234, 255), 452),
    ((223, 222, 218, 255), 403),
    ((230, 229, 225, 255), 393),
    ((255, 255, 255, 255), 310),
    ((230, 230, 228, 255), 308),
    ((222, 221, 217, 255), 284),
    ((231, 230, 226, 255), 277),
    ((231, 230, 228, 255), 256),
    ((237, 237, 237, 241), 242),
    ((8, 8, 8, 255), 237),
    ((236, 236, 236, 241), 220),
    ((233, 234, 232, 255), 206),
    ((236, 234, 232, 255), 197),
    ((234, 235, 233, 255), 190),
    ((235, 233, 231, 255), 187),
    ((221, 220, 216, 255), 181),
    ((237, 235, 233, 255), 179),
    ((8, 8, 7, 255), 170),
    ((232, 233, 231, 255), 169),
    ((230, 229, 226, 255), 155),
    ((9, 8, 8, 255), 154),
    ((229, 228, 225, 255), 152),
    ((230, 229, 227, 255), 142),
    ((232, 231, 227, 255), 142),
    ((231, 230, 227, 255), 140),
    ((228, 227, 224, 255), 139),
    ((229, 229, 227, 255), 130),
    ((238, 238, 236, 255), 114),
    ((237, 237, 236, 255), 113),
    ((10, 12, 9, 255), 112),
    ((229, 228, 223, 255), 112),
    ((235, 236, 234, 255), 109),
    ((230, 229, 224, 255), 108),
    ((9, 11, 8, 255), 107),
    ((236, 236, 235, 255), 107),
    ((239, 238, 236, 255), 106),
    ((230, 230, 227, 255), 105),
    ((234, 232, 230, 255), 105),
    ((229, 228, 226, 255), 105),
    ((238, 236, 234, 255), 104),
    ((231, 232, 230, 255), 102),
    ((227, 226, 223, 255), 97),
    ((228, 227, 222, 255), 95),
    ((220, 219, 215, 255), 94),
    ((9, 8, 7, 255), 94),
    ((229, 229, 226, 255), 90),
    ((8, 7, 7, 255), 90),
    ((9, 9, 8, 255), 88),
    ((231, 230, 225, 255), 85),
    ((8, 7, 8, 255), 84),
    ((227, 226, 221, 255), 84),
    ((231, 231, 228, 255), 81),
    ((9, 9, 7, 255), 79),
    ((10, 9, 8, 255), 78),
    ((228, 228, 226, 255), 77),
    ((238, 238, 238, 241), 75),
    ((232, 231, 228, 255), 74),
    ((9, 7, 8, 255), 74),
    ((10, 9, 7, 255), 71),
    ((228, 228, 225, 255), 71),
    ((7, 7, 7, 255), 70),
    ((10, 10, 8, 255), 69),
    ((7, 7, 6, 255), 66),
    ((227, 227, 225, 255), 64),
    ((230, 231, 229, 255), 64),
    ((11, 10, 8, 255), 63),
    ((10, 9, 9, 255), 63),
    ((236, 236, 233, 255), 62),
    ((228, 227, 225, 255), 61),
    ((10, 8, 8, 255), 61),
    ((235, 235, 234, 255), 61),
    ((232, 231, 226, 255), 61),
    ((9, 8, 9, 255), 61),
    ((228, 228, 224, 255), 61),
]


def draw(context: Context, rows: int = 36) -> None:
    context.set_black()
    context.paint()

    context.translate(
        context.size / 2,
        context.size / 2,
    )
    context.set_line_cap(LineCap.ROUND)

    if rows == 0:
        rows = len(_PALETTE)
    max_radius = context.size * sqrt(2) / 2
    radius_diff = max_radius / rows
    for row, colour in zip(range(rows), _PALETTE):
        context.circle(0, 0, radius_diff * row)
        context.set_source_rgba(*colour[0])
        context.set_line_width(
            max(
                colour[1]
                / sum(
                    (c[1] for c in _PALETTE[:rows]),
                )
                * context.size
                / 10,
                context.size / 500,
            )
        )
        context.stroke()


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
