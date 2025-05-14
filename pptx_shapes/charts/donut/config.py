from dataclasses import dataclass, field
from typing import Optional


@dataclass
class GapConfig:
    thickness: float = 1
    color: str = "#ffffff"


@dataclass
class LabelConfig:
    size: int = 20
    color: str = "#222222"
    family: str = "Calibri"
    bold: bool = True


@dataclass
class DonutChartConfig:
    inner_radius: float = 3
    outer_radius: float = 5
    start_angle: float = 90
    gap: Optional[GapConfig] = field(default_factory=GapConfig)
    label: Optional[LabelConfig] = field(default_factory=LabelConfig)
