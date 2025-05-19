from pptx_shapes import Presentation
from pptx_shapes.charts.line import LabelConfig, LineChart, LineChartConfig, LineConfig, MarkerConfig
from pptx_shapes.shapes import Group


def main() -> None:
    x0, y0 = 1.25, 2

    config = LineChartConfig(
        line=LineConfig(color="#fe7a81", background="#ffddd7", background_opacity=1, thickness=1.5),
        marker=MarkerConfig(radius=0.16, width=2.6, height=14, thickness=2),
        value=LabelConfig(color="#fe7a81", size=12),
        label=LabelConfig(color="#888888", size=13),
        smooth_count=20
    )

    data = [
        {"value": 6.2, "label": "январь\n2024"},
        {"value": 4.5, "label": "февраль\n2024"},
        {"value": 7.1, "label": "март\n2024"},
        {"value": 7, "label": "апрель\n2024"},
        {"value": 4.1, "label": "май\n2024"},
        {"value": 5.3, "label": "июнь\n2024"},
        {"value": 6.1, "label": "июль\n2024"},
        {"value": 5.9, "label": "август\n2024"},
        {"value": 9.3, "label": "сентябрь\n2024"},
        {"value": 8.5, "label": "октябрь\n2024"},
        {"value": 10.1, "label": "ноябрь\n2024"},
        {"value": 8.2, "label": "декабрь\n2024"}
    ]

    with Presentation(presentation_path="../empty.pptx") as presentation:
        chart = LineChart(config=config)
        presentation.add(shape=Group(chart.render(data=data, x=x0, y=y0)))
        presentation.save("line_chart.pptx")


if __name__ == "__main__":
    main()
