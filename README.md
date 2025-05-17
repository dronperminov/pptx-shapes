# pptx-shapes

[![PyPI version](https://badge.fury.io/py/pptx-shapes.svg)](https://pypi.org/project/pptx-shapes/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![Documentation Status](https://readthedocs.org/projects/pptx-shapes/badge/?version=latest)](https://pptx-shapes.readthedocs.io/en/latest)
[![CI tests](https://github.com/dronperminov/pptx-shapes/workflows/CI/badge.svg)](https://github.com/dronperminov/pptx-shapes/actions)

Python library for adding basic geometric shapes directly to PowerPoint (.pptx) slides by editing the XML structure.

![Example](https://github.com/dronperminov/pptx-shapes/raw/master/examples/main.png)

## Features

- Add basic shapes (ellipse, line, polygon, etc.) to existing slides
- Control position, size, fill, stroke, and other styles
- Simple, expressive API with smart defaults
- Supports minimalistic charts such as donut, bar, scatter charts
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
        x=20, y=2, width=4, height=4,
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
| [Arc](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/shapes/arc.py)             | `Arc`       | Curved segment defined by the bounding box and start/end angles              |
| [Arch](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/shapes/arch.py)           | `Arch`      | Ring-shaped arc defined by the bounding box, thickness and start/end angles  |
| [Ellipse](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/shapes/ellipse.py)     | `Ellipse`   | Ellipse defined by top-left corner, size, and rotation angle                 |
| [Rectangle](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/shapes/rectangle.py) | `Rectangle` | Rectangle defined by top-left corner, size, corner radius and rotation angle |
| [Pie](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/shapes/pie.py)             | `Pie`       | Filled sector of a circle, defined by the bounding box and start/end angles  |
| [Polygon](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/shapes/polygon.py)     | `Polygon`   | Arbitrary polygon defined by a list of points and rotation angle             |
| [TextBox](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/shapes/textbox.py)     | `TextBox`   | Text container with position, size, rotation, and font style                 |
| [Group](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/shapes/group.py)         | `Group`     | A group of multiple shapes                                                   |

## Supported charts

The `pptx_shapes.charts` module provides classes for adding simple charts to PowerPoint presentations using basic shapes.

| Chart                                                                                                 | Class         | Description                                                             |
|-------------------------------------------------------------------------------------------------------|---------------|-------------------------------------------------------------------------|
| [Donut](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/charts/donut/chart.py)    | `DonutChart`  | A donut chart used to visualize proportions of categorical data.        |
| [Bar](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/charts/bar/chart.py)        | `BarChart`    | A bar chart used to display values across categories or time series.    |
| [Scatter](https://github.com/dronperminov/pptx-shapes/blob/master/pptx_shapes/charts/scatter/plot.py) | `ScatterPlot` | A scatter plot used to visualize a set of points on a coordinate plane. |

## Documentation

Full documentation and examples are available at [pptx-shapes.readthedocs.io](https://pptx-shapes.readthedocs.io/en/latest)

## Examples

The following examples illustrate how to generate PowerPoint slides with various geometric shapes using `pptx-shapes`.
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


## Chart examples

### Example 1. Donut charts

This example demonstrates how to use `DonutChart` from `charts.donut` module
([examples/charts/donut_chart.py](https://github.com/dronperminov/pptx-shapes/blob/master/examples/charts/donut_chart.py)).

![Donut chart example](https://github.com/dronperminov/pptx-shapes/raw/master/examples/charts/donut_chart.png)

Download .pptx: [examples/charts/donut_chart.pptx](https://github.com/dronperminov/pptx-shapes/blob/master/examples/charts/donut_chart.pptx)

### Example 2. Bar chart

This example demonstrates how to use `BarChart` from `charts.bar` module
([examples/charts/bar_chart.py](https://github.com/dronperminov/pptx-shapes/blob/master/examples/charts/bar_chart.py)).

![Bar chart example](https://github.com/dronperminov/pptx-shapes/raw/master/examples/charts/bar_chart.png)

Download .pptx: [examples/charts/bar_chart.pptx](https://github.com/dronperminov/pptx-shapes/blob/master/examples/charts/bar_chart.pptx)

### Example 3. Scatter plot

This example demonstrates how to use `ScatterPlot` from `charts.scatter` module
([examples/charts/scatter_plot.py](https://github.com/dronperminov/pptx-shapes/blob/master/examples/charts/scatter_plot.py)).

![Scatter plot example](https://github.com/dronperminov/pptx-shapes/raw/master/examples/charts/scatter_plot.png)

Download .pptx: [examples/charts/scatter_plot.pptx](https://github.com/dronperminov/pptx-shapes/blob/master/examples/charts/scatter_plot.pptx)


## Changelog

See [CHANGELOG.md](https://github.com/dronperminov/pptx-shapes/blob/master/CHANGELOG.md) for version history.


## License

Licensed under the MIT License.
Feel free to use it in your projects.


## Contributing

Pull requests, issues, and feature ideas are very welcome!