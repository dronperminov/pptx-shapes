import math
from typing import List

from pptx_shapes.charts.scatter.config import Limits, ScatterPlotConfig
from pptx_shapes.charts.scatter.point import ScatterPoint
from pptx_shapes.enums import Align, VerticalAlign
from pptx_shapes.shapes import Ellipse, Line, Rectangle, Shape, TextBox
from pptx_shapes.style import FontStyle, StrokeStyle


class ScatterPlot:
    def render(self, points: List[ScatterPoint], config: ScatterPlotConfig) -> List[Shape]:
        limits = self.__get_limits(points=points, config=config)
        ellipses = self.__get_points(points=points, limits=limits, config=config)
        axes = self.__get_axes(limits=limits, config=config)
        return [*ellipses, *axes]

    def __get_limits(self, points: List[ScatterPoint], config: ScatterPlotConfig) -> Limits:
        if config.limits:
            return config.limits

        limits = Limits.from_points(points=points)

        dx, dy = limits.x_max - limits.x_min, limits.y_max - limits.y_min
        dw = dx / config.width
        dh = dy / config.height
        scale = max(dw, dh)

        new_dx = scale * config.width
        limits.x_min -= (new_dx - dx) / 2
        limits.x_max += (new_dx - dx) / 2

        new_dy = scale * config.height
        limits.y_min -= (new_dy - dy) / 2
        limits.y_max += (new_dy - dy) / 2

        return limits

    def __get_points(self, points: List[ScatterPoint], limits: Limits, config: ScatterPlotConfig) -> List[Ellipse]:
        ellipses = []

        for point in points:
            if not (limits.x_min <= point.x <= limits.x_max and limits.y_min <= point.y <= limits.y_max):
                continue

            size = 2 * point.radius
            ellipses.append(Ellipse(
                x=limits.map_x(point.x, config.x + config.padding, config.width - 2 * config.padding) - point.radius,
                y=limits.map_y(point.y, config.y + config.padding, config.height - 2 * config.padding) - point.radius,
                width=size,
                height=size,
                fill=point.fill,
                stroke=point.stroke
            ))

        return ellipses

    def __get_axes(self, limits: Limits, config: ScatterPlotConfig) -> List[Shape]:
        shapes = [Rectangle(x=config.x, y=config.y, width=config.width, height=config.height, stroke=StrokeStyle(color=config.axes.color))]

        if config.axes.show_x:
            shapes.extend(self.__get_x_axis(limits=limits, config=config))

        if config.axes.show_y:
            shapes.extend(self.__get_y_axis(limits=limits, config=config))

        return shapes

    def __get_x_axis(self, limits: Limits, config: ScatterPlotConfig) -> List[Shape]:
        shapes = []
        axes = config.axes
        style = FontStyle(color=axes.font.color, size=axes.font.size, family=axes.font.family, align=Align.CENTER, vertical_align=VerticalAlign.TOP)

        for tick in self.__get_axis_ticks(v_min=limits.x_min, v_max=limits.x_max):
            x = limits.map_x(x=tick, x_min=config.x + config.padding, dx=config.width - 2 * config.padding)
            y = config.y + config.height + axes.tick_length

            shapes.append(Line(x1=x, y1=y - axes.tick_length, x2=x, y2=y, stroke=StrokeStyle(color=axes.color, thickness=axes.thickness)))
            shapes.append(TextBox(x=x - axes.text_size / 2, y=y + 0.1, width=axes.text_size, height=axes.text_size, text=str(tick), style=style))

        return shapes

    def __get_y_axis(self, limits: Limits, config: ScatterPlotConfig) -> List[Shape]:
        shapes = []
        axes = config.axes
        style = FontStyle(color=axes.font.color, size=axes.font.size, family=axes.font.family, align=Align.RIGHT, vertical_align=VerticalAlign.CENTER)

        for tick in self.__get_axis_ticks(v_min=limits.y_min, v_max=limits.y_max):
            x = config.x - axes.tick_length
            y = limits.map_y(y=tick, y_min=config.y + config.padding, dy=config.height - config.padding * 2)

            shapes.append(Line(x1=x, y1=y, x2=x + axes.tick_length, y2=y, stroke=StrokeStyle(color=axes.color, thickness=axes.thickness)))
            shapes.append(TextBox(x=x - axes.text_size - 0.1, y=y - axes.text_size / 2, width=axes.text_size, height=axes.text_size, text=str(tick), style=style))

        return shapes

    def __get_axis_ticks(self, v_min: float, v_max: float, ticks: int = 10) -> List[float]:
        raw_step = (v_max - v_min) / max(ticks - 1, 1)
        step = 10 ** math.floor(math.log10(raw_step))
        residual = raw_step / step

        if residual > 5:
            step *= 10
        elif residual > 2:
            step *= 5
        elif residual > 1:
            step *= 2

        return [self.__round(i * step) for i in range(math.ceil(v_min / step), math.floor(v_max / step) + 1)]

    def __round(self, value: float) -> float:
        if abs(value) < 1e-6:
            return 0

        if abs(value) > 0.001:
            scale = 3
        else:
            scale = (2 - math.floor(math.log10(abs(value))))

        sign = 1 if value > 0 else -1
        return sign * round(abs(value), scale)
