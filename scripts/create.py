from argparse import ArgumentParser
from pathlib import Path

_OUTPUT = Path(__file__).parent.parent / "art"

_TEMPLATE = """from cairo_utils import Context
from cairo_utils.core import write_to_png

SIZE = 1_000
OUTPUT = "run/{name}.png"


def draw(context: Context) -> None:
    context.set_white()
    context.paint()


def main() -> None:
    with write_to_png(SIZE, OUTPUT) as context:
        draw(context)


if __name__ == "__main__":
    main()
"""


def parse_args() -> tuple[int, str]:
    arg_parser = ArgumentParser()
    arg_parser.add_argument("day", type=int)
    arg_parser.add_argument("name", type=str)
    args = arg_parser.parse_args()
    return args.day, args.name


def main() -> None:
    day, piece_name = parse_args()
    name = f"day{day:02}_{piece_name}"
    output = _OUTPUT / f"{name}.py"
    output.write_text(_TEMPLATE.format(name=name))


if __name__ == "__main__":
    main()
