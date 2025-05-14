# Changelog

## 0.1.4 (2025-05-14)

- Added `family` field to `FontStyle` for specifying font family (default: `"Calibri"`)
- New example: `text_boxes.py` showcasing different font families and text styles


## 0.1.3 (2025-05-14)

### Added
- New shape: `Arc` with support for rotation, bounding box size, and start/end angles


## 0.1.2 (2025-05-14)

### Added
- `Arrow` shape support.
- Four visual examples: basic shapes, scatter plot, histograms, and polygon splitting.
- Preview images and downloadable `.pptx` files linked in the `README.md`.
- Enum classes for formatting and styles:
  - `Align`: `LEFT`, `CENTER`, `RIGHT`
  - `VerticalAlign`: `TOP`, `CENTER`, `BOTTOM`
  - `ArrowType`: `TRIANGLE`, `ARROW`, `DIAMOND`, `OVAL`, `NONE`
  - `LineDash`: `SOLID`, `DASHED`, `DOTTED`, `SHORT_DASHED`, `DASH_DOTTED`, `LONG_DASH`, `LONG_DASH_DOTTED`, `LONG_DASH_DOT_DOTTED`


## 0.1.1 (2025-05-13)

### Changed
- Improved and expanded `README.md`:
  - Added shape overview table with descriptions.
  - Included parameters and usage notes for each shape.
  - Added section for style/formatting classes (`FillStyle`, `StrokeStyle`, etc.).


## 0.1.0 (2025-05-13)

### Added
- First public release of `python-shapes`.
- Support for geometric shapes: `Ellipse`, `Line`, `Rectangle`, `Polygon`, `TextBox`, and `Group`.
- Styling classes: `FillStyle`, `StrokeStyle`, `FontStyle`, `FontFormat`, `Margin`
- `Presentation` class with:
  - `.add()` method for placing shapes on slides
  - `.save()` method for saving the presentation
  - Context manager interface (`with Presentation(...) as presentation:`)
- Native editing of `.pptx` as a zip archive using `lxml` slide files using a temporary directory.