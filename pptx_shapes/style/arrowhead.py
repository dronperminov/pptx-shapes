from dataclasses import dataclass

from pptx_shapes.enums import ArrowType
from pptx_shapes.enums.arrow_size import ArrowSize


@dataclass
class ArrowHead:
    head: ArrowType = ArrowType.TRIANGLE
    length: ArrowSize = ArrowSize.MEDIUM
    width: ArrowSize = ArrowSize.MEDIUM

    def to_pptx(self) -> dict:
        return {
            "len": self.length.value,
            "type": self.head.value,
            "w": self.width.value
        }
