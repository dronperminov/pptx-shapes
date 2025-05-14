from typing import List

from pptx_shapes import Presentation
from pptx_shapes.shapes import Group, Rectangle
from pptx_shapes.style import FillStyle, StrokeStyle


def plot_histogram(histogram: dict, x0: float, y0: float, bar_width: float, height: float) -> List[Rectangle]:
    width = bar_width * len(histogram["values"]) + 1
    max_value = max(histogram["values"])
    rectangles = []

    for i, value in enumerate(histogram["values"]):
        bar_height = value / max_value * height

        rectangles.append(Rectangle(
            x=x0 + i * bar_width, y=y0 + height - bar_height,
            width=bar_width, height=bar_height,
            fill=FillStyle(color=histogram["fill"]),
            stroke=StrokeStyle(color=histogram["stroke"])
        ))

    rectangles.append(Rectangle(x=x0 - 0.5, y=y0 - 0.5, width=width, height=height + 0.5, stroke=StrokeStyle(color="#222"), radius=0.1))
    return rectangles


def main() -> None:
    histograms = [
        {"values": [0, 2, 4, 9, 16, 25, 15, 10, 3, 1, 1], "fill": "#7699d4", "stroke": "#fff"},
        {"values": [1, 2, 1, 2, 1, 3, 1, 4, 5, 2, 3, 1], "fill": "#dd7373", "stroke": "#fff"},
        {"values": [200, 100, 50, 25, 12, 6, 3], "fill": "#89dd73", "stroke": "#fff"}
    ]

    x0, y0 = 2, 1.25
    bar_width = 1.8
    height = 5

    with Presentation(presentation_path="empty.pptx") as presentation:
        for histogram in histograms:
            rectangles = plot_histogram(histogram=histogram, x0=x0, y0=y0, bar_width=bar_width, height=height)
            presentation.add(shape=Group(shapes=rectangles))
            y0 += height + 1

        presentation.save("histograms.pptx")


if __name__ == "__main__":
    main()
