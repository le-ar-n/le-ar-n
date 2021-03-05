---
layout: session
title: Geometry
lesson: 2
---

### Useful links:

* [Compas Docs](https://compas.dev/compas/latest/index.html)
* [Compas Geometry](https://compas.dev/compas/latest/api/compas.geometry.html)
* [Compas Artists](https://compas.dev/compas/latest/api/compas_ghpython.artists.html)

### COMPAS main

<img src="https://github.com/le-ar-n/le-ar-n/blob/main/docs/_images/compas_geometry.png" width="500">

The main library of COMPAS provides flexible data structures, a geometry processing library, robot fundamentals, numerical solvers, and various other components as a base framework for computational AE(F)C research.

The CAD packages (compas_rhino, compas_ghpython, compas_blender) provide a unified framework for reading and writing CAD geometry, for visualization of COMPAS geometry and data structures, and for basic user inter interaction in Blender, Rhino, and Grasshopper.

### Cross Product


### Cross Product using COMPAS Classes

```python
>>> from compas.geometry import Vector

>>> u = Vector(1.0, 0.0, 0.0)
>>> v = Vector(0.0, 1.0, 0.0)

>>> uxv = u.cross(v)

>>> print(uxv)

Vector(0.000, 0.000, 1.000)
```

### Draw in Plotters

```python
>>> from compas.geometry import Pointcloud
>>> from compas_plotters import Plotter

>>> cloud = Pointcloud.from_bounds(10, 5, 0, 20)

>>> points = []
>>> for xyz in cloud:
>>>     points.append({'pos': xyz, 'radius': 0.8})

>>> plotter = Plotter(figsize=(8, 5))
>>> plotter.draw_points(points)
>>> plotter.show()
```

### Draw in Rhino using artists

```python
from random import random
from compas.geometry import Pointcloud,Point, Circle, Plane
from compas.utilities import i_to_green, i_to_red
from compas_rhino.artists import PointArtist, CircleArtist

cloud = Pointcloud.from_bounds(10, 5, 0, 50)

for point in cloud:
    n = random()
    PointArtist(point, color=i_to_red(n), layer="points").draw()
    circle = Circle(Plane([0, 0, 0], [0, 0, 1]), n)
    circle.center = point
    CircleArtist(circle, color=i_to_red(n), layer="circles").draw()
```