from dataclasses import dataclass


@dataclass
class FontFormat:
    bold: bool = False
    italic: bool = False
    underline: bool = False
    strike: bool = False

    def to_pptx(self) -> dict:
        formatting = {}

        if self.bold:
            formatting["b"] = "1"

        if self.italic:
            formatting["i"] = "1"

        if self.underline:
            formatting["u"] = "sng"

        if self.strike:
            formatting["strike"] = "sngStrike"

        return formatting
