# pptx-shapes

[![PyPI version](https://badge.fury.io/py/pptx-shapes.svg)](https://pypi.org/project/pptx-shapes/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![CI tests](https://github.com/dronperminov/pptx-shapes/workflows/CI/badge.svg)](https://github.com/dronperminov/pptx-shapes/actions)

Python library for adding basic geometric shapes directly to PowerPoint (.pptx) slides by editing the XML structure.

![Example](https://github.com/dronperminov/pptx-shapes/raw/master/examples/basic.png)

## Features

- Add basic shapes (ellipse, line, polygon, etc.) to existing slides
- Control position, size, fill, stroke, and other styles
- Work directly with slides XML structure
- Save result as `.pptx`

## Installation

```bash
pip install pptx-shapes
```

## Quick Start

```python
from pptx_shapes import Presentation
from pptx_shapes.shapes import Ellipse, Rectangle, TextBox
from pptx_shapes.style import FillStyle, FontFormat, FontStyle, StrokeStyle

with Presentation(presentation_path="empty.pptx") as presentation:
    presentation.add(shape=TextBox(
        x=23, y=4, width=12, height=2, angle=45,
        text="Hello from pptx-shapes!",
        style=FontStyle(size=32),
        formatting=FontFormat(bold=True)
    ))

    presentation.add(shape=Ellipse(
        x=20, y=2, dx=4, dy=4,
        fill=FillStyle(color="#7699d4")
    ))

    presentation.add(shape=Rectangle(
        x=18, y=8, width=4, height=8.5, radius=0.25, angle=30,
        fill=FillStyle(color="#dd7373"),
        stroke=StrokeStyle(color="magenta", thickness=3)
    ))

    presentation.save("result.pptx")
```


## How it works

This library modifies `.pptx` files by directly editing the underlying XML structure.

A `.pptx` presentation is essentially a ZIP archive containing XML files that describe slides, layouts, and content. This library works by:

* Unzipping the `.pptx` file.
* Locating and parsing the target slide file (e.g., `ppt/slides/slide1.xml`).
* Inserting new shape elements into the slide's XML tree, using tags like `<p:sp>`, `<p:cxnSp>`, and `<a:prstGeom>`.
* Saving the modified XML.
* Repacking all files into a `.pptx` archive.

This low-level approach is ideal for automated slide generation, data visualizations, and geometric illustrations –
especially when you need to create many shapes or apply programmatic styles.

## Supported Shapes

Currently, `pptx-shapes` supports the following geometric shapes:

| Shape                                                                                                | Class       | Description                                                                  |
|------------------------------------------------------------------------------------------------------|-------------|------------------------------------------------------------------------------|
| [Line](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/shapes/line.py)           | `Line`      | Straight line between two points                                             |
| [Arrow](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/shapes/arrow.py)         | `Arrow`     | Straight arrow between two points                                            |
| [Arc](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/shapes/arc.py)             | `Arc`       | Curved segment defined by the bounding box and start/end angles.             |
| [Ellipse](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/shapes/ellipse.py)     | `Ellipse`   | Ellipse defined by top-left corner, diameters, and rotation angle            |
| [Rectangle](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/shapes/rectangle.py) | `Rectangle` | Rectangle defined by top-left corner, size, corner radius and rotation angle |
| [Polygon](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/shapes/polygon.py)     | `Polygon`   | Arbitrary polygon defined by a list of points and rotation angle             |
| [TextBox](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/shapes/textbox.py)     | `TextBox`   | Text container with position, size, rotation, and font style                 |
| [Group](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/shapes/group.py)         | `Group`     | A group of multiple shapes                                                   |


### Line

A straight line connecting two points.

```python
Line(
    x1=0.5, y1=1, # start point (cm)
    x2=1.5, y2=5, # end point (cm)
    stroke=...    # StrokeStyle
)
```

#### Parameters
* `x1`, `y1`: coordinates for the start point
* `x2`, `y2`: coordinates for the end point
* `stroke`: `StrokeStyle` for the stroke


### Arrow

A straight arrow connecting two points.

```python
Arrow(
    x1=0.5, y1=1,                 # start point (cm)
    x2=1.5, y2=5,                 # end point (cm)
    start_type=ArrowType.NONE,    # type of arrow at the start
    end_type=ArrowType.TRIANGLE,  # type of arrow at the end
    stroke=...                    # StrokeStyle
)
```

#### Parameters
* `x1`, `y1`: coordinates for the start point
* `x2`, `y2`: coordinates for the end point
* `start_type`: `ArrowType` of arrow at the start point
* `end_type`: `ArrowType` of arrow at the end point
* `stroke`: `StrokeStyle` for the stroke


### Arc

Draws a curved segment defined by the bounding box and start/end angles.

```python
Arc(
    x=24, y=9,          # top-left angle (cm)
    width=5, height=8,  # diameters (cm)
    start_angle=90,     # start angle of the arc (degrees)
    end_angle=270,      # end angle of the arc (degrees)
    angle=30,           # optional rotation angle (degrees)
    fill=...,           # optional FillStyle
    stroke=...          # optional StrokeStyle
)
```

#### Parameters
* `x`, `y`: top-left corner of the bounding box in centimeters
* `width`, `height`: width and height of the bounding box in centimeters
* `start_angle`: start angle of the arc (in degrees, default `0`)
* `end_angle`: end angle of the arc (in degrees, default `180`)
* `angle`: the rotation angle of the arc in degrees (default is `0`).
* `fill`: optional `FillStyle` to fill the arc
* `stroke`: optional `StrokeStyle` for the border


### Ellipse

An ellipse is defined by its top-left corner and the diameters in horizontal and vertical directions. It can be rotated by a given angle.

```python
Ellipse(
    x=2, y=3.5, # top-left angle (cm)
    dx=4, dy=6, # diameters (cm)
    angle=30,   # optional rotation angle (degrees)
    fill=...,   # optional FillStyle
    stroke=...  # optional StrokeStyle
)
```

#### Parameters
* `x`, `y`: top-left corner coordinates in centimeters
* `dx`, `dy`: diameters in centimeters
* `angle`: the rotation angle of the ellipse in degrees (default is `0`).
* `fill`: optional `FillStyle` to fill the ellipse
* `stroke`: optional `StrokeStyle` for the border


### Rectangle
A rectangle is defined by its top-left corner and its width and height. Like the ellipse, it can be rotated by a specific angle.

```python
Rectangle(
    x=2, y=3.5,        # top-left angle (cm)
    width=4, height=6, # sizes (cm)
    angle=45,          # optional rotation angle (degrees)
    radius=0.05,       # optional radius of corner rounding (percents)
    fill=...,          # optional FillStyle
    stroke=...         # optional StrokeStyle
)
```

#### Parameters
* `x`, `y`: coordinates defining the top-left corner (cm)
* `width`, `height`: the width and height of the rectangle (cm)
* `radius`: the radius of rounded corners as a percentage of the width/height (default is `0`)
* `angle`: the rotation angle of the rectangle in degrees (default is `0`)
* `fill`: fill style
* `stroke`: stroke style

### Polygon

A polygon can be an arbitrary shape defined by a list of points. It can also be rotated by an angle.

```python
Polygon(
    points=[
        (11, 12),
        (13, 14),
        (11, 16),
        (9, 14),
        (11, 12)
    ],         # list of tuple points (cm)
    angle=15,  # optional rotation angle (degrees)
    fill=...,  # optional FillStyle
    stroke=... # optional StrokeStyle
)
```

#### Parameters
* `points`: a list of tuples of `(x, y)` coordinates that define the vertices of the polygon
* `angle`: the rotation angle of the polygon in degrees (default is `0`)
* `fill`: fill style
* `stroke`: stroke style

### TextBox

A text box that holds text with customizable size, font style, margins, and rotation. You can define margins (padding around the text), and enable auto_fit to automatically resize
the box based on the text's length. If auto_fit is set to `True`, the width and height of the text box will be adjusted to accommodate the text content.

```python
TextBbox(
    x=23, y=4,          # top-left angle (cm)
    width=12, height=2, # sizes (cm)
    text="Hello!",      # text content (new lines also possible)
    angle=45,           # optional rotation angle (degrees)
    auto_fit=False,     # fit sizes by the text content
    style=...,          # optional FontStyle
    formatting=...,     # optional FontFormat
    margin=...,         # optional Margin
    fill=...,           # optional FillStyle
    stroke=...          # optional StrokeStyle
)
```

#### Parameters
* `x`, `y`: coordinates defining the top-left corner (cm)
* `width`, `height`: the width and height of the text box
* `text`: the text content of the box
* `angle`: the rotation angle of the text box in degrees (default is `0`)
* `auto_fit`: boolean that, when set to `True`, automatically adjusts the size of the text box to fit its
* `style`: style of the font (font size, color, etc.)
* `formatting`: formatting of the content (bold, italic, underline, ...)
* `margin`: (left, top, right, bottom) margins that define the inner spacing of the text box
* `fill`: fill style
* `stroke`: stroke style

### Group

A group allows you to combine multiple shapes into one unit. This is useful for creating complex compositions of shapes that should be manipulated together.

```python
Group(shapes=[
    Ellipse(...),
    Rectangle(...),
    ...
])
```

#### Parameters
* `shapes`: a list of `Shape` objects that you want to group together.

## Style and formatting classes

The library provides several classes to define the style and formatting of shapes. These classes help customize the appearance of shapes, including their colors, borders,
text styling, and margins.

### `FillStyle`

Defines the fill color and opacity for a shape. The `FillStyle` class allows you to control the internal color of shapes like rectangles, ellipses, and more.

```python
FillStyle(
    color="#7699d4", # hex, rgb or named color
    opacity=1
)
```

### `StrokeStyle`

Defines the stroke (outline) of a shape, including its color, thickness, opacity, and line style. Use this class to customize the borders of shapes such as lines, rectangles,
and ellipses.

```python
StrokeStyle(
    color="#7699d4", # hex, rgb or named color
    thickness=1,     # width in pt
    opacity=1,
    dash=LineDash.SOLID
)
```

### `FontStyle`

Defines the font style for text shape (`TextBox`). This includes font size, color, and alignments.

```python
FontStyle(
    size=14,
    family="Calibri",
    color="#000000",
    align=Align.CENTER,
    vertical_align=VerticalAlign.CENTER
)
```

### `FontFormat`

Defines additional text formatting options for font styling. You can use this class to apply bold, italic, underline, or strike-through to text.

```python
FontFormat(
    bold=False,
    italic=False,
    underline=False,
    strike=False
)
```

### `Margin`

Defines the margins inside a `TextBox`. These margins control the inner spacing around the text content.

```python
Margin(
    left=0.25,
    right=0.25,
    top=0.1,
    bottom=0.1
)
```

These formatting classes allow you to fine-tune the appearance of shapes and text on your slides. You can apply custom fills, strokes, fonts, and margins to make the presentation
visually appealing and precise.


## Enums

Several enums are used to standardize alignment, line styles, and arrowheads.

### `Align`
Horizontal text alignment:

```python
Align.LEFT     # "l"
Align.CENTER   # "ctr"
Align.RIGHT    # "r"
```

### `VerticalAlign`
Vertical text alignment:

```python
VerticalAlign.TOP     # "t"
VerticalAlign.CENTER  # "ctr"
VerticalAlign.BOTTOM  # "b"
```

### `ArrowType`
Arrowhead style:

```python
ArrowType.TRIANGLE  # triangle arrowhead
ArrowType.ARROW     # classic open arrowhead
ArrowType.DIAMOND   # diamond arrowhead
ArrowType.OVAL      # oval arrowhead
ArrowType.NONE      # no arrowhead
```

### `LineDash`
Stroke dash style for lines:

```python
LineDash.SOLID                 # solid line
LineDash.DASHED                # dashed line
LineDash.DOTTED                # dotted line
LineDash.SHORT_DASHED          # short dashes
LineDash.DASH_DOTTED           # dash-dot pattern
LineDash.LONG_DASH             # long dashes
LineDash.LONG_DASH_DOTTED      # long dash-dot
LineDash.LONG_DASH_DOT_DOTTED  # long dash-dot-dot
```

## Examples

The following examples illustrate how to generate PowerPoint slides with various geometric shapes using `python-shapes`.
All examples include screenshots, downloadable .pptx files, and links to the corresponding source code.

### Example 1. Basic shapes

A simple demonstration of how to draw basic geometric elements – lines, ellipses, rectangles, polygons, arrows and text – on a blank slide
([examples/basic.py](https://github.com/dronperminov/pptx-shapes/blob/master/examples/basic.py)).

![Basic slide](https://github.com/dronperminov/pptx-shapes/raw/master/examples/basic.png)

Download .pptx: [examples/basic.pptx](https://github.com/dronperminov/pptx-shapes/blob/master/examples/basic.pptx)


### Example 2. Scatter plots

This example shows how to render a scatter plot using ellipses as data points, demonstrating precise positioning and styling
([examples/scatter.py](https://github.com/dronperminov/pptx-shapes/blob/master/examples/scatter.py)).

![Slide example](https://github.com/dronperminov/pptx-shapes/raw/master/examples/scatter.png)

Download .pptx: [examples/scatter.pptx](https://github.com/dronperminov/pptx-shapes/blob/master/examples/scatter.pptx)


### Example 3. Histograms

Bar-style visualizations built using rectangles – this example illustrates how to construct a histogram layout with custom colors
([examples/histogram.py](https://github.com/dronperminov/pptx-shapes/blob/master/examples/histograms.py)).

![Slide example](https://github.com/dronperminov/pptx-shapes/raw/master/examples/histograms.png)

Download .pptx: [examples/histogram.pptx](https://github.com/dronperminov/pptx-shapes/blob/master/examples/histograms.pptx)


### Example 4. Polygons split

A more advanced use case – splitting polygonal shapes by lines. Useful for illustrating partitions or segmentations
([examples/polygons.py](https://github.com/dronperminov/pptx-shapes/blob/master/examples/polygons.py)).

![Slide example](https://github.com/dronperminov/pptx-shapes/raw/master/examples/polygons.png)

Download .pptx: [examples/polygons.pptx](https://github.com/dronperminov/pptx-shapes/blob/master/examples/polygons.pptx)


### Example 5. Font families and text styles

This example demonstrates how to use different font families and styles in `TextBox` shapes. It shows how to customize font size, alignment, color, and the font family.
([examples/text_boxes.py](https://github.com/dronperminov/pptx-shapes/blob/master/examples/text_boxes.py)).

![Slide example](https://github.com/dronperminov/pptx-shapes/raw/master/examples/text_boxes.png)

Download .pptx: [examples/text_boxes.pptx](https://github.com/dronperminov/pptx-shapes/blob/master/examples/text_boxes.pptx)


## Changelog

See [CHANGELOG.md](https://github.com/dronperminov/pptx-shapes/blob/master/CHANGELOG.md) for version history.


## License

Licensed under the MIT License.
Feel free to use it in your projects.


## Contributing

Pull requests, issues, and feature ideas are very welcome!