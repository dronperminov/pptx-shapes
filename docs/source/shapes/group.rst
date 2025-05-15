.. _group:

Group
=====

A group allows you to combine multiple shapes into one unit. This is useful for creating complex compositions of shapes that should be manipulated together.

.. image:: /_static/shapes/group.png
   :alt: Group example
   :align: center

.. autoclass:: pptx_shapes.shapes.Group

**Parameters**

- ``shapes`` (`List[Shape]`) – a list of ``Shape`` objects that you want to group together.


**Example**

.. code-block:: python

   from pptx_shapes.enums import VerticalAlign
   from pptx_shapes.shapes import Group, Line, TextBox
   from pptx_shapes.style import FontStyle, StrokeStyle

   group = Group(shapes=[
       Line(x1=1, y1=1, x2=13, y2=1, stroke=StrokeStyle(thickness=2, color="#7699d4")),
       Line(x1=1, y1=1, x2=1, y2=6, stroke=StrokeStyle(thickness=2, color="#dd7373")),
       Line(x1=13, y1=1, x2=1, y2=6, stroke=StrokeStyle(thickness=2, color="#89dd73")),
       TextBox(x=0.7, y=3.5, width=13, height=1, text="hypotenuse", angle=-22.6, style=FontStyle(size=18, color="#89dd73", vertical_align=VerticalAlign.TOP)),
       TextBox(x=-2, y=3, width=5, height=1, text="kathete", angle=90, style=FontStyle(size=18, color="#dd7373", vertical_align=VerticalAlign.TOP)),
       TextBox(x=1, y=0, width=12, height=1, text="kathete", style=FontStyle(size=18, color="#7699d4", vertical_align=VerticalAlign.BOTTOM))
   ])

:ref:`← Back to all shapes <shapes-index>`
