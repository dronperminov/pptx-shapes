from typing import List, Tuple

from pptx_shapes.charts.line.config import LineChartConfig
from pptx_shapes.enums import Align, VerticalAlign
from pptx_shapes.shapes import Ellipse, Polygon, Polyline, Shape, TextBox
from pptx_shapes.style import FillStyle, FontStyle, StrokeStyle


class LineChart:
    def __init__(self, config: LineChartConfig) -> None:
        self.config = config

    def render(self, data: List[dict], x: float, y: float) -> List[Shape]:
        width = len(data) * self.config.marker.width
        min_value = min(0, min([item["value"] for item in data], default=0))
        max_value = max([item["value"] for item in data], default=1)

        points = []
        shapes = []

        for i, item in enumerate(data):
            px = x + self.__map(i, 0, len(data) - 1, self.config.marker.width / 2, width - self.config.marker.width / 2)
            py = y + self.__map(item["value"], min_value, max_value, self.config.marker.height, 0)
            offset = (self.config.marker.width / 2 - self.config.marker.radius * 1.5) * (-1 if i == 0 else 1 if i == len(data) - 1 else 0)
            align = Align.LEFT if i == 0 else Align.RIGHT if i == len(data) - 1 else Align.CENTER

            points.append((px + offset, py))
            shapes.append(self.__get_label(x=px - self.config.marker.width / 2, y=y + self.config.marker.height, label=item["label"]))
            shapes.append(self.__get_value_label(x=px - self.config.marker.width / 2, y=py - self.config.marker.radius, value=item["value"], align=align))
            shapes.append(self.__get_marker(x=px + offset, y=py))

        y0 = y + self.__map(0, min_value, max_value, self.config.marker.height, 0)
        lines = self.__get_line(points=points, y0=y0)
        return lines + shapes

    def __map(self, x: float, x_min: float, x_max: float, out_min: float, out_max: float) -> float:
        return (x - x_min) * (out_max - out_min) / (x_max - x_min) + out_min

    def __get_value_label(self, x: float, y: float, value: float, align: Align) -> TextBox:
        style = FontStyle(size=self.config.value.size, color=self.config.value.color, family=self.config.value.family, align=align, vertical_align=VerticalAlign.BOTTOM)
        return TextBox(x=x, y=y - self.config.value.height, width=self.config.marker.width, height=self.config.value.height, text=str(value), style=style)

    def __get_label(self, x: float, y: float, label: str) -> TextBox:
        style = FontStyle(size=self.config.label.size, color=self.config.label.color, family=self.config.label.family, vertical_align=VerticalAlign.TOP)
        return TextBox(x=x, y=y, width=self.config.marker.width, height=self.config.label.height, text=label, style=style)

    def __get_marker(self, x: float, y: float) -> Ellipse:
        r = self.config.marker.radius
        fill = FillStyle(color=self.config.marker.background)
        stroke = StrokeStyle(color=self.config.marker.color, thickness=self.config.marker.thickness)
        return Ellipse(x=x - r, y=y - r, width=2 * r, height=2 * r, fill=fill, stroke=stroke)

    def __get_line(self, points: List[Tuple[float, float]], y0: float) -> List[Shape]:
        stroke = StrokeStyle(color=self.config.line.color, thickness=self.config.line.thickness)
        fill = FillStyle(color=self.config.line.background, opacity=self.config.line.background_opacity)
        smoothed_points = self.__smooth_points(points=points, smooth_count=self.config.smooth_count)

        return [
            Polygon(points=[(points[0][0], y0), *smoothed_points, (points[-1][0], y0)], fill=fill),
            Polyline(points=smoothed_points, stroke=stroke)
        ]

    def __smooth_points(self, points: List[Tuple[float, float]], smooth_count: int = 50) -> List[Tuple[float, float]]:
        smoothed_points = [points[0]]

        for i, point in enumerate(points[1:]):
            for j in range(smooth_count):
                smoothed_points.append(self.__interpolate(self.__map(j, -1, smooth_count, points[i][0], point[0]), points))

            smoothed_points.append(point)

        return smoothed_points

    def __interpolate(self, x: float, points: List[Tuple[float, float]]) -> Tuple[float, float]:
        y = 0
        sum_weight = 0

        for px, py in points:
            distance = abs(x - px)

            if distance == 0:
                return px, py

            weight = 1 / distance ** 2
            y += py * weight
            sum_weight += weight

        return x, y / sum_weight
