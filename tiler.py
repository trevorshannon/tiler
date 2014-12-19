import itertools
from matplotlib import pyplot
import numpy

_TILE_WIDTH = 6.0  # in
_TILE_HEIGHT = 3.0  # in
_PLANE_WIDTH = 32.0  # in
_PLANE_HEIGHT = 64.0  # in
_OVERLAP = 0.5

def get_spaced_points(unit_dim, plane_dim, fixed_point=0):
  offset = fixed_point % unit_dim
  vertices = numpy.arange(offset, plane_dim, unit_dim).tolist()
  # include edges
  vertices.insert(0, 0)
  vertices.append(plane_dim)
  return vertices

x_pos = (_PLANE_WIDTH - _TILE_WIDTH) / 2.0 + 1
y_pos = 0
x_shift = _TILE_WIDTH * _OVERLAP

fig = pyplot.figure()
axes = fig.add_subplot(111)

# compute tile row positions
y_vertices = get_spaced_points(_TILE_HEIGHT, _PLANE_HEIGHT, y_pos)

# draw tiles
for j in range(len(y_vertices) - 1):
  # compute x tile positions for this row
  x_vertices = get_spaced_points(_TILE_WIDTH, _PLANE_WIDTH,
                                 x_pos + x_shift * (j%2))
  axes.plot(x_vertices, [y_vertices[j]] * len(x_vertices), 'k')
  axes.plot(x_vertices, [y_vertices[j + 1]] * len(x_vertices), 'k')
  for x_vertex in x_vertices:
    axes.plot([x_vertex, x_vertex], [y_vertices[j], y_vertices[j + 1]], 'k')

# draw bounding box
axes.plot([0, _PLANE_WIDTH, _PLANE_WIDTH, 0, 0],
          [0, 0, _PLANE_HEIGHT, _PLANE_HEIGHT, 0], 'r', alpha=0.5)
# adjust display settings and display the result
pyplot.axis('equal')
axes.set_ylim(-0.05 * _PLANE_HEIGHT, 1.05 * _PLANE_HEIGHT)
axes.set_xlim(-0.05 * _PLANE_WIDTH, 1.05 * _PLANE_WIDTH)
pyplot.show()
