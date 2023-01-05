from math import cos, sin


def from_radial(radius: float, angle: float) -> tuple[float, float]:
    return (
        radius * cos(angle),
        radius * sin(angle),
    )
