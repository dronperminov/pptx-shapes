from dataclasses import dataclass, field


@dataclass
class LineConfig:
    color: str = "#fe7a81"
    background: str = "#fe7a81"
    background_opacity: float = 0.1
    thickness: float = 1.5


@dataclass
class MarkerConfig:
    color: str = "#fe7a81"
    background: str = "#ffffff"
    radius: float = 0.1
    width: float = 1.5
    height: float = 8
    thickness: float = 1.5


@dataclass
class LabelConfig:
    size: float = 8
    color: str = "#222222"
    family: str = "Calibri"
    height: float = 1


@dataclass
class LineChartConfig:
    line: LineConfig = field(default_factory=lambda: LineConfig())
    marker: MarkerConfig = field(default_factory=lambda: MarkerConfig())
    value: LabelConfig = field(default_factory=lambda: LabelConfig(color="#fe7a81", size=9))
    label: LabelConfig = field(default_factory=lambda: LabelConfig(color="#888888", size=8))
    smooth_count: int = 20
