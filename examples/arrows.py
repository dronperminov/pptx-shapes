from pptx_shapes import Presentation
from pptx_shapes.enums import ArrowSize, ArrowType
from pptx_shapes.shapes import Arrow, TextBox
from pptx_shapes.style import ArrowHead, FontStyle, StrokeStyle


def main() -> None:
    x0 = 3
    y0 = 0.75
    width = 10
    height = 6

    stroke = StrokeStyle(color="#222", thickness=1.5)

    with Presentation(presentation_path="empty.pptx") as presentation:
        for i, arrow_length in enumerate(ArrowSize):
            for j, arrow_width in enumerate(ArrowSize):
                x1 = x0 + j * width
                x2 = x1 + 8
                y = y0 + i * height

                arrow_head = ArrowHead(head=ArrowType.ARROW, length=arrow_length, width=arrow_width)
                triangle_head = ArrowHead(head=ArrowType.TRIANGLE, length=arrow_length, width=arrow_width)
                oval_head = ArrowHead(head=ArrowType.OVAL, length=arrow_length, width=arrow_width)
                diamond_head = ArrowHead(head=ArrowType.DIAMOND, length=arrow_length, width=arrow_width)

                presentation.add(shape=TextBox(
                    x=x1, y=y,
                    width=8, height=2,
                    text=f"width: {arrow_width}\nlength: {arrow_length}",
                    style=FontStyle(size=16)
                ))

                presentation.add(shape=Arrow(x1=x1, y1=y + 2, x2=x2, y2=y + 2, start_head=None, end_head=arrow_head, stroke=stroke))
                presentation.add(shape=Arrow(x1=x1, y1=y + 3, x2=x2, y2=y + 3, start_head=None, end_head=triangle_head, stroke=stroke))

                presentation.add(shape=Arrow(x1=x1, y1=y + 4, x2=x2, y2=y + 4, start_head=oval_head, end_head=arrow_head, stroke=stroke))
                presentation.add(shape=Arrow(x1=x1, y1=y + 5, x2=x2, y2=y + 5, start_head=diamond_head, end_head=triangle_head, stroke=stroke))

        presentation.save("arrows.pptx")


if __name__ == "__main__":
    main()
