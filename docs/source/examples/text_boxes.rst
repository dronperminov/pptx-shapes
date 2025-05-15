TextBoxes example
==================

This example demonstrates how to use the :ref:`TextBox <textbox>` class to add styled text boxes to a PowerPoint presentation.

It shows how to customize:

- Font family and size
- Text alignment (left, center, right)
- Vertical text orientation (via `angle`)
- Fill and stroke styles
- Font formatting (bold, italic, etc.)

Overview
--------

This script:

- Adds five horizontally aligned text boxes with different fonts and alignments
- Adds one vertical, italic, dashed-bordered text box with background fill

Each text box uses:

- :ref:`FontStyle <font-style>` — for font size, family, alignment, color
- :ref:`FontFormat <font-format>` — for extra formatting like **bold**, *italic*, etc.
- :ref:`FillStyle <fill-style>` and :ref:`StrokeStyle <stroke-style>` — for visual styling
- :ref:`TextBox <textbox>` — to place and configure the text shape

Example Code
------------

.. literalinclude:: ../../../examples/text_boxes.py
   :language: python
   :linenos:


Result
------

This example produces a PowerPoint file (``text_boxes.pptx``) with six text boxes on a blank slide.

.. image:: /_static/examples/text_boxes.png
   :alt: Basic example
   :align: center

- The left column demonstrates different font families and alignment styles.
- The right column features a vertically rotated, styled text box with custom fill and dashed border.
