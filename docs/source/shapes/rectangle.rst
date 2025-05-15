.. _rectangle:

Rectangle
=========

A rectangle or rounded rectangle, positioned by its bounding box.

.. image:: /_static/shapes/rectangle.png
   :alt: Rectangle example
   :align: center

.. autoclass:: pptx_shapes.shapes.Rectangle

**Parameters**

- ``x`` (`float`) – left position (in centimeters).
- ``y`` (`float`) – top position (in centimeters).
- ``width`` (`float`) – width (in centimeters).
- ``height`` (`float`) – height (in centimeters).
- ``radius`` (`float`) – the radius of rounded corners as a percentage of the width/height (default is ``0``)
- ``angle`` (`float`, optional) – rotation in degrees, default is ``0``.
- ``fill`` (:ref:`FillStyle <fill-style>`, optional) – fill style.
- ``stroke`` (:ref:`StrokeStyle <stroke-style>`, optional) – stroke style.


**Example**

.. code-block:: python

   from pptx_shapes.shapes import Rectangle
   from pptx_shapes.style import FillStyle

   rectangle = Rectangle(
       x=1, y=1,
       width=3, height=2,
       fill=FillStyle(color="#00aff0")
   )

:ref:`← Back to all shapes <shapes-index>`
