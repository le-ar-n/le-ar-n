---
layout: session
title: Geometry
lesson: 2
---

### Useful links:

* [Compas Docs](https://compas.dev/compas/latest/index.html)
* [Compas Geometry](https://compas.dev/compas/latest/api/compas.geometry.html)
* [Compas Artists](https://compas.dev/compas/latest/api/compas_ghpython.artists.html)


### COMPAS Geometry

### Cross Product using COMPAS Classes

```python
>>> from compas.geometry import Vector

>>> u = Vector(1.0, 0.0, 0.0)
>>> v = Vector(0.0, 1.0, 0.0)

>>> uxv = u.cross(v)

>>> print(uxv)

Vector(0.000, 0.000, 1.000)
```

### Draw in Rhino

```python
>>> from random import random
>>> from compas.geometry import Pointcloud,Point, Circle, Plane
>>> from compas.utilities import i_to_green, i_to_red
>>> from compas_rhino.artists import PointArtist, CircleArtist

>>> cloud = Pointcloud.from_bounds(10, 5, 0, 50)

>>> for point in cloud:
>>>     n = random()
>>>     PointArtist(point, color=i_to_red(n), layer="points").draw()
>>>     circle = Circle(Plane([0, 0, 0], [0, 0, 1]), n)
>>>     circle.center = point
>>>     CircleArtist(circle, color=i_to_red(n), layer="circles").draw()
```