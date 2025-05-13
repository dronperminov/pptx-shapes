from dataclasses import dataclass


@dataclass
class FontStyle:
    size: float = 14
    color: str = "#000000"
    align: str = "center"
    vertical_align: str = "center"
