Fractal drawing example
=======================

This example demonstrates how to generate a colorful recursive fractal pattern on a PowerPoint slide using lines and groups of shapes.
It highlights the flexibility of the pptx_shapes library for programmatically creating complex, data-driven illustrations.

The fractal is built by recursively branching from a center point, with configurable depth, angles, and color transitions.
It uses the :ref:`Line <line>` and :ref:`Group <group>` shapes, along with custom :ref:`StrokeStyle <stroke-style>` for gradient-like effects.

Overview
--------

- Start from a central point and recursively add branches
- Configure the number of initial and recursive branches
- Assign stroke colors dynamically based on recursion depth
- Combine all shapes into a single group for easier slide positioning
- Fill the background with a solid color for visual contrast by adding full slide rectangle

Example Code
------------

.. literalinclude:: ../../../examples/fractal.py
   :language: python
   :linenos:

Result
------

This example produces a fractal-like structure radiating from the center of the slide, with smoothly changing colors and transparency to enhance depth.

.. image:: /_static/examples/fractal.png
   :alt: Fractal example
   :align: center

Fractal is created using:

- :ref:`Line <line>` – to represent each branch of the fractal
- :ref:`Group <group>` – to group all branches into a single composite object
- :ref:`StrokeStyle <stroke-style>` – to apply dynamic coloring and transparency based on depth

.. note::
   Colors are interpolated between ``start_color`` and ``end_color`` using linear RGB blending.
   Stroke opacity decreases quadratically with depth for a fading effect.

Output file: ``fractal.pptx``
