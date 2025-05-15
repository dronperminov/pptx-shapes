from pptx_shapes import Presentation
from pptx_shapes.charts.bar import BarChart, BarChartConfig, BarConfig, LabelConfig
from pptx_shapes.shapes import Group


def main() -> None:
    x0, y0 = 0.9, 2

    config = BarChartConfig(
        bar=BarConfig(width=2, height=15, thickness=2),
        value=LabelConfig(size=14, color="#222"),
        label=LabelConfig(size=12, color="#222")
    )

    data = [
        {"value": 12, "label": "январь\n2024"},
        {"value": 19, "label": "февраль\n2024"},
        {"value": 20, "label": "март\n2024"},
        {"value": 24, "label": "апрель\n2024"},
        {"value": 27, "label": "май\n2024"},
        {"value": 27, "label": "июнь\n2024"},
        {"value": 34, "label": "июль\n2024"},
        {"value": 38, "label": "август\n2024"},
        {"value": 49, "label": "сентябрь\n2024"},
        {"value": 34, "label": "октябрь\n2024"},
        {"value": 42, "label": "ноябрь\n2024"},
        {"value": 35, "label": "декабрь\n2024"},
        {"value": 10, "label": "январь\n2025"},
        {"value": 45, "label": "февраль\n2025"},
        {"value": 12, "label": "март\n2025"},
        {"value": 19, "label": "апрель\n2025"}
    ]

    with Presentation(presentation_path="../empty.pptx") as presentation:
        chart = BarChart(config=config)
        presentation.add(shape=Group(chart.render(data=data, x=x0, y=y0)))
        presentation.save("bar_chart.pptx")


if __name__ == "__main__":
    main()
