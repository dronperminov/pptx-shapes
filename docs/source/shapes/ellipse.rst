.. _ellipse:

Ellipse
=======

An ellipse (oval or circle), positioned by its bounding box.

.. image:: /_static/shapes/ellipse.png
   :alt: Ellipse example
   :align: center

.. autoclass:: pptx_shapes.shapes.Ellipse

**Parameters**

- ``x`` (`float`) – left position (in centimeters).
- ``y`` (`float`) – top position (in centimeters).
- ``width`` (`float`) – width (in centimeters).
- ``height`` (`float`) – height (in centimeters).
- ``angle`` (`float`, optional) – rotation in degrees, default is ``0``.
- ``fill`` (:ref:`FillStyle <fill-style>`, optional) – fill style.
- ``stroke`` (:ref:`StrokeStyle <stroke-style>`, optional) – stroke style.


**Example**

.. code-block:: python

   from pptx_shapes.shapes import Ellipse
   from pptx_shapes.style import FillStyle

   ellipse = Ellipse(
       x=1, y=1,
       width=3, height=2,
       fill=FillStyle(color="blue")
   )

:ref:`← Back to all shapes <shapes-index>`
