.. _pie:

Pie
===

A filled sector of an ellipse, defined by its bounding box and angular range.

.. image:: /_static/shapes/pie.png
   :alt: Pie example
   :align: center

.. autoclass:: pptx_shapes.shapes.Pie

**Parameters**

- ``x`` (`float`) – left position (in centimeters).
- ``y`` (`float`) – top position (in centimeters).
- ``width`` (`float`) – width (in centimeters).
- ``height`` (`float`) – height (in centimeters).
- ``start_angle`` (`float`, optional) – start angle of the pie (in degrees, default ``0``)
- ``end_angle`` (`float`, optional) – end angle of the pie (in degrees, default ``180``)
- ``angle`` (`float`, optional) – rotation in degrees, default is ``0``.
- ``fill`` (:ref:`FillStyle <fill-style>`, optional) – fill style.
- ``stroke`` (:ref:`StrokeStyle <stroke-style>`, optional) – stroke style.


**Example**

.. code-block:: python

   from pptx_shapes.enums import LineDash
   from pptx_shapes.shapes import Pie

   pie = Pie(
       x=24, y=9,
       width=5, height=8,
       start_angle=90,
       end_angle=270,
       stroke=StrokeStyle(color="#f00", thickness=2.5)
   )

:ref:`← Back to all shapes <shapes-index>`
