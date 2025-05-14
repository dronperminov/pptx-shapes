import math
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class BBox:
    x: float
    y: float
    width: float
    height: float

    @classmethod
    def from_points(cls: "BBox", points: List[Tuple[float, float]], angle: float = 0) -> "BBox":
        angle = angle / 180 * math.pi
        cx = sum(x for x, _ in points) / len(points)
        cy = sum(y for _, y in points) / len(points)

        x_min = x_max = cx
        y_min = y_max = cy

        for px, py in points:
            dx, dy = px - cx, py - cy
            x = cx + dx * math.cos(angle) - dy * math.sin(angle)
            y = cy + dx * math.sin(angle) + dy * math.cos(angle)

            x_min, y_min = min(x_min, x), min(y_min, y)
            x_max, y_max = max(x_max, x), max(y_max, y)

        return BBox(x=x_min, y=y_min, width=x_max - x_min, height=y_max - y_min)

    @classmethod
    def from_rect(cls: "BBox", x: float, y: float, width: float, height: float, angle: float = 0) -> "BBox":
        if angle == 0:
            return BBox(x=x, y=y, width=width, height=height)

        points = [(x, y), (x + width, y), (x + width, y + height), (x, y + height)]
        return BBox.from_points(points=points, angle=angle)
