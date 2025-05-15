.. _textbox:

TextBox
=======

A text box that holds text with customizable size, font style, margins, and rotation.
You can define margins (padding around the text), and enable ``auto_fit`` to automatically resize the box based on the text's length.
If ``auto_fit`` is set to ``True``, the width and height of the text box will be adjusted to accommodate the text content.

.. image:: /_static/shapes/textbox.png
   :alt: Textbox example
   :align: center

.. autoclass:: pptx_shapes.shapes.TextBox

**Parameters**

- ``x`` (`float`) – left position (in centimeters).
- ``y`` (`float`) – top position (in centimeters).
- ``width`` (`float`) – width (in centimeters).
- ``height`` (`float`) – height (in centimeters).
- ``angle`` (`float`, optional) – rotation in degrees, default is ``0``.
- ``auto_fit`` (`bool`, optional) – boolean that, when set to True, automatically adjusts the size of the text box to fit its, default is ``False``.
- ``style`` (:ref:`FontStyle <font-style>`, optional) – style of the font (font size, color, family, etc.).
- ``formatting`` (:ref:`FontFormat <font-format>`, optional) – formatting of the content (bold, italic, underline, ...).
- ``margin`` (:ref:`Margin <margin>`, optional) – (left, top, right, bottom) margins that define the inner spacing, default is ``Margin(0, 0, 0, 0)``.
- ``fill`` (:ref:`FillStyle <fill-style>`, optional) – fill style.
- ``stroke`` (:ref:`StrokeStyle <stroke-style>`, optional) – stroke style.


**Example**

.. code-block:: python

   from pptx_shapes.shapes import TextBox
   from pptx_shapes.style import FontStyle, FontFormat, FillStyle, strokeStyle

   textbox = TextBox(
       x=17, y=8,
       width=15, height=3,
       text="Two lines of\nitalic vertical text",
       angle=90,
       style=FontStyle(size=35, family="Arial", align=Align.LEFT),
       formatting=FontFormat(italic=True),
       fill=FillStyle(color="#ddd"),
       stroke=StrokeStyle(color="#222", dash=LineDash.DASHED)
   )

:ref:`← Back to all shapes <shapes-index>`
