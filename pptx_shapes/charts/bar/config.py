from dataclasses import dataclass, field


@dataclass
class LabelConfig:
    size: float = 8
    color: str = "#222222"
    family: str = "Calibri"
    height: float = 1


@dataclass
class BarConfig:
    width: float = 1.2
    height: float = 8
    radius: float = 0.2
    fill_color: str = "#ffc154"
    stroke_color: str = "#ffffff"
    thickness: float = 1


@dataclass
class BarChartConfig:
    bar: BarConfig = field(default_factory=lambda: BarConfig())
    value: LabelConfig = field(default_factory=lambda: LabelConfig())
    label: LabelConfig = field(default_factory=lambda: LabelConfig())
