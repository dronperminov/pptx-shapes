Style and formatting
====================

The library provides several classes to define the style and formatting of shapes.
These classes help customize the appearance of shapes, including their colors, borders, text styling, and margins.

.. _fill-style:

FillStyle
---------

.. autoclass:: pptx_shapes.style.FillStyle
   :members:

Defines the fill color and opacity for a shape. The ``FillStyle`` class allows you to control the internal color of shapes like rectangles, ellipses, and more.

- ``color`` (`str`) – the fill color (see :ref:`supported color formats <colors>`).
- ``opacity`` (`float`, optional) – opacity of the fill (number, ``0-1``), default is ``1.0``.


.. _stroke-style:

StrokeStyle
-----------

.. autoclass:: pptx_shapes.style.StrokeStyle
   :members:

Defines the stroke (outline) of a shape, including its color, thickness, opacity, and line style.
Use this class to customize the borders of shapes such as lines, rectangles, and ellipses.

- ``color`` (`str`, optional) – the stroke color (see :ref:`supported color formats <colors>`), default is ``black``.
- ``thickness`` (`float`, optional) – width of the stroke in pt, default is ``1.0``.
- ``opacity`` (`float`, optional) – opacity of the stroke (number, ``0-1``), default is ``1.0``.
- ``dash`` (:ref:`LineDash <line-dash>`, optional) – stroke dash style, default is ``LineDash.SOLID``.


.. _font-style:

FontStyle
---------

.. autoclass:: pptx_shapes.style.FontStyle
   :members:

Defines the font style for text, including size, font family, color, alignment, and vertical alignment.
Use this class to customize text appearance inside textboxes and other shape elements.

- ``size`` (`float`, optional) – font size in pt, default is ``14``.
- ``color`` (`str`, optional) – font color (see :ref:`supported color formats <colors>`), default is ``#000000``.
- ``family`` (`str`, optional) – font family name (e.g., ``"Arial"``, ``"Calibri"``), default is ``Calibri``.
- ``align`` (:ref:`Align <align>`, optional) – horizontal alignment of text. Default is ``Align.CENTER``.
- ``vertical_align`` (:ref:`VerticalAlign <vertical-align>`, optional) – vertical alignment of text. Default is ``VerticalAlign.CENTER``.
- ``line_spacing`` (`float`, optional) – line spacing. Default is ``1.0``.


.. _font-format:

FontFormat
----------

.. autoclass:: pptx_shapes.style.FontFormat
   :members:

Specifies additional formatting options for text, such as bold, italic, underline, and strikethrough.
Can be used alongside :ref:`FontStyle <font-style>` to control text appearance.

- ``bold`` (`bool`, optional) – whether the text is bold, default is ``False``.
- ``italic`` (`bool`, optional) – whether the text is italic, default is ``False``.
- ``underline`` (`bool`, optional) – whether the text is underlined, default is ``False``.
- ``strike`` (`bool`, optional) – whether the text has a strikethrough, default is ``False``.


.. _margin:

Margin
------

.. autoclass:: pptx_shapes.style.Margin
   :members:

Defines internal margins for text container (:ref:`TextBox <textbox>`).
Margins are specified in centimeters.

- ``left`` (`float`, optional) – left margin in cm, default is ``0.25``.
- ``right`` (`float`, optional) – right margin in cm, default is ``0.25``.
- ``top`` (`float`, optional) – top margin in cm, default is ``0.1``.
- ``bottom`` (`float`, optional) – bottom margin in cm, default is ``0.1``.


.. _arrow-head:

ArrowHead
---------

.. autoclass:: pptx_shapes.style.ArrowHead
   :members:

Arrowhead styling options for :ref:`arrows <arrow>`

- ``head`` (:ref:`ArrowType <arrow-type>`, optional) – arrowhead type, default is ``ArrowType.TRIANGLE``.
- ``length`` (:ref:`ArrowSize <arrow-size>`, optional) – arrowhead length, default is ``ArrowSize.MEDIUM``.
- ``width`` (:ref:`ArrowSize <arrow-size>`, optional) – arrowhead width, default is ``ArrowSize.MEDIUM``.

.. image:: /_static/style/arrows.png
   :alt: Arrowheads example
   :align: center

.. _colors:

Supported color formats
-----------------------

Colors can be specified using one of the following formats:

- **Named colors** (case-insensitive):
    A set of common color names, such as: ``"black"``, ``"white"``, ``"red"``, ``"green"``, ``"blue"``, ``"yellow"``, ``"magenta"``, ``"cyan"``

    These are interpreted according to standard web color definitions.

- **Hexadecimal strings**:
    Hex color codes are supported in two forms:

    - 3-digit format: ``"#f00"`` (equivalent to ``"#ff0000"``, red)
    - 6-digit format: ``"#00ff00"`` (green)

    Both uppercase and lowercase letters are allowed.

- **RGB functional notation**:
    You may also use the CSS-like syntax: ``rgb(r, g, b)``

    - ``"rgb(255, 0, 0)"`` (red)
    - ``"rgb(0, 128, 255)"`` (blue-ish)

    Values must be integers between 0 and 255.

- **HSL functional notation**:
    You may also use the CSS-like syntax: ``hsl(h, s%, l%)``

    - ``"hsl(0, 100%, 50%)"`` (red)
    - ``"hsl(39, 100%, 50%)"`` (orange)

    Values must be integers, ``h`` between 0 and 360, ``s`` and ``l`` between 0 and 100.

If a color string is invalid or unsupported, an error will be raised at runtime.
