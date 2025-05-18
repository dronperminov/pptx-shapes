from pptx_shapes import Presentation
from pptx_shapes.enums import Align, ArrowType, LineDash, VerticalAlign
from pptx_shapes.shapes import Arc, Arrow, Ellipse, Group, Line, Polygon, Rectangle, TextBox
from pptx_shapes.style import ArrowHead, FillStyle, FontFormat, FontStyle, StrokeStyle


def main() -> None:
    with Presentation(presentation_path="empty.pptx") as presentation:
        presentation.add(shape=TextBox(
            x=23, y=4, width=12, height=2, text="Hello from pptx-shapes!", angle=45, style=FontStyle(size=32), formatting=FontFormat(bold=True)
        ))

        presentation.add(shape=TextBox(
            x=7.5, y=17.2, width=18.5, height=1.5,
            text="Python library for adding basic geometric shapes directly to PowerPoint (.pptx) slides by editing the XML structure.",
            style=FontStyle(size=16, align=Align.LEFT),
            auto_fit=True
        ))

        # ellipses
        presentation.add(shape=Ellipse(x=20, y=2, width=4, height=4, fill=FillStyle(color="#7699d4")))

        # arrows
        presentation.add(shape=Arrow(
            x1=10, y1=9, x2=14, y2=11,
            start_head=ArrowHead(head=ArrowType.OVAL),
            end_head=ArrowHead(head=ArrowType.ARROW),
            stroke=StrokeStyle(thickness=2)
        ))

        # arcs
        presentation.add(shape=Arc(
            x=24, y=9, width=5, height=8, start_angle=90, end_angle=270, angle=45, stroke=StrokeStyle(color="#f00", thickness=2.5, dash=LineDash.DASH_DOTTED)
        ))
        presentation.add(shape=Arc(
            x=19.5, y=1.5, width=5, height=5, start_angle=5, end_angle=175, stroke=StrokeStyle(color="#7699d4", thickness=2, dash=LineDash.DOTTED)
        ))
        presentation.add(shape=Arc(
            x=19.5, y=1.5, width=5, height=5, start_angle=185, end_angle=355, stroke=StrokeStyle(color="#7699d4", thickness=2, dash=LineDash.DASHED)
        ))

        # rectangles
        presentation.add(shape=Rectangle(
            x=18, y=8, width=4, height=8.5, radius=0.25, fill=FillStyle(color="#dd7373"), stroke=StrokeStyle(color="#222", thickness=3), angle=30
        ))
        presentation.add(shape=Rectangle(
            x=27, y=14, width=3, height=3, radius=0, fill=FillStyle(color="#dd7373"), stroke=StrokeStyle(color="#222", thickness=1)
        ))

        # polygons
        presentation.add(shape=Polygon(
            points=[(11, 12), (13, 14), (11, 16), (9, 14), (11, 12)], fill=FillStyle(color="yellow"), stroke=StrokeStyle(color="magenta", thickness=2.5)
        ))
        presentation.add(shape=Polygon(
            points=[(15, 5), (16, 6), (15, 7), (12, 7), (11, 6), (12, 5)], angle=45, fill=FillStyle(color="#88ff88")
        ))

        # groups
        presentation.add(shape=Group(shapes=[
            Line(x1=1, y1=1, x2=13, y2=1, stroke=StrokeStyle(thickness=2, color="#7699d4")),
            Line(x1=1, y1=1, x2=1, y2=6, stroke=StrokeStyle(thickness=2, color="#dd7373")),
            Line(x1=13, y1=1, x2=1, y2=6, stroke=StrokeStyle(thickness=2, color="#89dd73")),
            TextBox(x=0.7, y=3.5, width=13, height=1, text="hypotenuse", angle=-22.6, style=FontStyle(size=18, color="#89dd73", vertical_align=VerticalAlign.TOP)),
            TextBox(x=-2, y=3, width=5, height=1, text="kathete", angle=90, style=FontStyle(size=18, color="#dd7373", vertical_align=VerticalAlign.TOP)),
            TextBox(x=1, y=0, width=12, height=1, text="kathete", style=FontStyle(size=18, color="#7699d4", vertical_align=VerticalAlign.BOTTOM))
        ]))

        presentation.add(shape=Group(shapes=[
            Ellipse(x=4.5, y=6.0, width=2.0, height=3.5, fill=FillStyle(color="#dd7373", opacity=0.5), stroke=StrokeStyle(color="black", thickness=2, opacity=0.75)),
            Ellipse(x=3.0, y=8.5, width=3.5, height=2.0, fill=FillStyle(color="#dd7373", opacity=0.25), stroke=StrokeStyle(color="black", opacity=0.25), angle=-45),
            Ellipse(x=5.0, y=8.5, width=3.5, height=2.0, fill=FillStyle(color="#dd7373", opacity=0.85), stroke=StrokeStyle(color="black", opacity=0.85), angle=45)
        ]))

        presentation.add(shape=Group(shapes=[
            TextBox(x=1, y=15, width=4.8, height=1, text="little histogram", style=FontStyle(size=20, color="#7699d4")),
            Rectangle(x=1, y=16, width=1.2, height=2.7, radius=0.2, fill=FillStyle(color="#7699d4"), stroke=StrokeStyle(color="#fff")),
            Rectangle(x=2.2, y=16.4, width=1.2, height=2.3, radius=0.2, fill=FillStyle(color="#7699d4"), stroke=StrokeStyle(color="#fff")),
            Rectangle(x=3.4, y=17, width=1.2, height=1.7, radius=0.2, fill=FillStyle(color="#7699d4"), stroke=StrokeStyle(color="#fff")),
            Rectangle(x=4.6, y=16.1, width=1.2, height=2.6, radius=0.2, fill=FillStyle(color="#7699d4"), stroke=StrokeStyle(color="#fff"))
        ]))

        presentation.save("basic.pptx")


if __name__ == "__main__":
    main()
