from pptx_shapes import Presentation
from pptx_shapes.charts.donut import DonutChart, DonutChartConfig, GapConfig, LabelConfig
from pptx_shapes.shapes import Group


def main() -> None:
    x0, y0 = 1, 2
    gap = 1

    configs = [
        DonutChartConfig(inner_radius=3, outer_radius=5, gap=GapConfig(thickness=2), label=LabelConfig(size=75)),
        DonutChartConfig(inner_radius=0, outer_radius=5, gap=GapConfig(thickness=2), label=None),
        DonutChartConfig(inner_radius=4.5, outer_radius=5, gap=None, label=None),
    ]

    data = [
        {"value": 180, "color": "#f39c12"},
        {"value": 95, "color": "#2ecc71"},
        {"value": 150, "color": "#e74c3c"},
        {"value": 75, "color": "#3498db"}
    ]

    with Presentation(presentation_path="../empty.pptx") as presentation:
        for i, config in enumerate(configs):
            chart = DonutChart(config=config)
            presentation.add(shape=Group(chart.render(data=data, x=x0 + i * (gap + chart.size), y=y0)))

        presentation.save("donut_chart.pptx")


if __name__ == "__main__":
    main()
