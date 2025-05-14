from typing import List, Tuple

from pptx_shapes import Presentation
from pptx_shapes.shapes import Group, Polygon
from pptx_shapes.style import FillStyle, StrokeStyle


def split_polygon(polygon: List[Tuple[float, float]], line: Tuple[float, float, float]) -> Tuple[List[Tuple[float, float]], List[Tuple[float, float]]]:
    polygon1, polygon2 = [], []
    a, b, c = line

    for i, (x1, y1) in enumerate(polygon):
        x2, y2 = polygon[(i + 1) % len(polygon)]

        sign1 = a * x1 + b * y1 + c
        sign2 = a * x2 + b * y2 + c

        if sign1 <= 0:
            polygon1.append((x1, y1))

        if sign1 >= 0:
            polygon2.append((x1, y1))

        if sign1 * sign2 >= 0:
            continue

        t = sign1 / (sign1 - sign2)
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)

        polygon1.append((x, y))
        polygon2.append((x, y))

    return polygon1, polygon2


def mix_colors(color1: str, color2: str) -> str:
    r1, g1, b1 = color1[1:3], color1[3:5], color1[5:]
    r2, g2, b2 = color2[1:3], color2[3:5], color2[5:]

    r = (int(r1, 16) + int(r2, 16)) // 2
    g = (int(g1, 16) + int(g2, 16)) // 2
    b = (int(b1, 16) + int(b2, 16)) // 2

    return f"#{r:02X}{g:02X}{b:02X}"


def split_polygons(polygons: List[dict], line: Tuple[float, float, float]) -> List[dict]:
    new_polygons = []

    for polygon in polygons:
        polygon1, polygon2 = split_polygon(polygon=polygon["points"], line=line)

        if len(polygon1) > 2:
            new_polygons.append({"points": polygon1, "color": mix_colors(polygon["color"], "#dd7373")})

        if len(polygon2) > 2:
            new_polygons.append({"points": polygon2, "color": mix_colors(polygon["color"], "#7699d4")})

    return new_polygons


def view_points(points: List[Tuple[float, float]], limits: dict, x0: float, y0: float, width: float, height: float) -> List[Tuple[float, float]]:
    mapped_points = []

    for x, y in points:
        x = x0 + (x - limits["x_min"]) / (limits["x_max"] - limits["x_min"]) * width
        y = y0 + (limits["y_max"] - y) / (limits["y_max"] - limits["y_min"]) * height
        mapped_points.append((x, y))

    return mapped_points


def main() -> None:
    lines = [
        (0.04, 0.3, -0.01),
        (-0.75, 0.1, -0.97),
        (-0.14, 0.9, 0.96),
        (1.14, 0.18, -1.05),
        (1.27, -0.07, 0.04),
        (-0.2, 0.24, -0.15),
        (0.35, 1.34, -0.96),
        (0.26, -0.9, -0.54)
    ]

    limits = {"x_min": -1.7, "y_min": -1.7, "x_max": 1.7, "y_max": 1.7}
    polygons = [
        {"points": [(-1.7, -1.7), (-1.7, 1.7), (1.7, 1.7), (1.7, -1.7)], "color": "#ffffff"}
    ]

    x0, y0 = 1, 1.5
    size = 7.5
    gap = 0.5
    columns = 4

    with Presentation(presentation_path="empty.pptx") as presentation:
        for i, line in enumerate(lines):
            polygons = split_polygons(polygons=polygons, line=line)
            x = x0 + (size + gap) * (i % columns)
            y = y0 + (size + gap) * (i // columns)

            shapes = []
            for polygon in polygons:
                points = view_points(points=polygon["points"], limits=limits, x0=x, y0=y, width=size, height=size)
                shapes.append(Polygon(points=points, fill=FillStyle(color=polygon["color"]), stroke=StrokeStyle(color="#222", thickness=0.5)))

            presentation.add(shape=Group(shapes=shapes))

        presentation.save("polygons.pptx")


if __name__ == "__main__":
    main()
