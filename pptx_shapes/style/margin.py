from dataclasses import dataclass

from pptx_shapes import units


@dataclass
class Margin:
    left: float = 0.25
    right: float = 0.25
    top: float = 0.1
    bottom: float = 0.1

    def to_pptx(self) -> dict:
        return {
            "bIns": units.cm_to_emu(self.bottom),
            "lIns": units.cm_to_emu(self.left),
            "rIns": units.cm_to_emu(self.right),
            "tIns": units.cm_to_emu(self.top)
        }
