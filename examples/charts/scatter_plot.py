import math
import random

from pptx_shapes import Presentation
from pptx_shapes.charts.scatter import Axes, ScatterPlot, ScatterPlotConfig, ScatterPoint
from pptx_shapes.charts.scatter.config import AxesFont
from pptx_shapes.shapes import Group
from pptx_shapes.style import FillStyle, StrokeStyle


def spiral(h: float = 1.25, delta: float = 0.1) -> ScatterPoint:
    label = random.randint(0, 1)
    angle = random.random()
    r = angle - delta + random.random() * delta * 2
    t = h * angle * 2 * math.pi

    if label == 1:
        t += math.pi

    return ScatterPoint(
        x=r * math.sin(t),
        y=r * math.cos(t),
        radius=0.11,
        fill=FillStyle(color=["#7699d4", "#dd7373"][label]),
        stroke=StrokeStyle(color="#fff", thickness=0.5)
    )


def main() -> None:
    x0, y0 = 9.5, 2
    points_count = 1000

    points = [spiral() for _ in range(points_count)]

    config = ScatterPlotConfig(
        x=x0, y=y0,
        width=15, height=15,
        axes=Axes(show_x=True, show_y=True, color="#222", font=AxesFont(size=10, color="#222")),
        padding=0.2
    )

    with Presentation(presentation_path="../empty.pptx") as presentation:
        plot = ScatterPlot()
        presentation.add(shape=Group(plot.render(points=points, config=config)))
        presentation.save("scatter_plot.pptx")


if __name__ == "__main__":
    main()
