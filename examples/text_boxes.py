from pptx_shapes import Presentation
from pptx_shapes.enums import Align, LineDash
from pptx_shapes.shapes import TextBox
from pptx_shapes.style import FillStyle, FontFormat, FontStyle, StrokeStyle


def main() -> None:
    with Presentation(presentation_path="empty.pptx") as presentation:
        presentation.add(shape=TextBox(x=1, y=1, width=15, height=2, text="Calibri text", style=FontStyle(size=42, family="Calibri", align=Align.LEFT, color="#dd7373")))
        presentation.add(shape=TextBox(x=1, y=4, width=15, height=2, text="Arial text", style=FontStyle(size=42, family="Arial", align=Align.CENTER)))
        presentation.add(shape=TextBox(x=1, y=7, width=15, height=2, text="Times New Roman text", style=FontStyle(size=42, family="Times New Roman", align=Align.LEFT)))
        presentation.add(shape=TextBox(x=1, y=10, width=15, height=2, text="Consolas text", style=FontStyle(size=42, family="Consolas", align=Align.LEFT)))
        presentation.add(shape=TextBox(x=1, y=13, width=15, height=2, text="Привет, МИР!", style=FontStyle(size=42, family="Consolas", align=Align.RIGHT)))

        presentation.add(shape=TextBox(
            x=17, y=8,
            width=15, height=3,
            text="Two lines of\nitalic vertical text",
            angle=90,
            style=FontStyle(size=35),
            formatting=FontFormat(italic=True),
            fill=FillStyle(color="#ddd"),
            stroke=StrokeStyle(color="#222", dash=LineDash.DASHED)
        ))

        presentation.save("text_boxes.pptx")


if __name__ == "__main__":
    main()
