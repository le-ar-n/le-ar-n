---
layout: session
title: Data Structures
lesson: 3
---

### Useful links:

* [Compas Docs](https://compas.dev/compas/latest/index.html)
* [Compas Datastructures](https://compas.dev/compas/latest/api/compas.datastructures.html)
* [Compas Meshes](https://compas.dev/compas/latest/tutorial/meshes.html)

### Data Structures in COMPAS

#### Meshes
In COMPAS meshes are presented using a half-edge data structure. In a half-edge data structure, each edge is composed of two half-edges with opposite orientation. Each half-edge is part of exactly one face, unless it is on the boundary. An edge is thus incident to at least one face and at most to two. The half-edges of a face form a continuous cycle, connecting the vertices of the face in a specific order forming a closed n-sided polygon. The ordering of the vertices determines the direction of its normal.

#### Networks
In COMPAS a network is a “directed edge graph” that encodes the relationships between “nodes” with “edges”. Networks can, for example, be used to keep track of the relationships between the individual elements of a Discrete Element Assembly, or to represent the elements of a cable net.

### Constructing a Mesh

```python
>>> import os
>>> import compas
>>> from compas.datastructures import Mesh

>>> HERE = os.path.dirname(__file__)
>>> DATA = os.path.join(HERE, 'data')
>>> FILE = os.path.join(DATA, 'faces.obj')

>>> mesh = Mesh.from_obj(FILE)

>>> print(mesh.summary())
```

```python
>>>
Mesh summary
============
- vertices: 36
- edges: 60
- faces: 25
```

### Constructing a Network

```python
>>> import os
>>> import compas
>>> from compas.datastructures import Network

>>> HERE = os.path.dirname(__file__)
>>> DATA = os.path.join(HERE, 'data')
>>> FILE = os.path.join(DATA, 'lines.obj')

>>> network = Network.from_obj(FILE)

>>> print(network.summary())
```

```python
>>>
Graph summary
============
- nodes: 32
- edges: 43
```

### Draw Mesh in Grasshopper


### Draw Network in Grasshopper 
