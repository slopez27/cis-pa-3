import sys
sys.path.append('../utils/')
from point3d import Point3D
from test_find_closest_point_mesh import FindClosestPointMesh

import unittest
import tempfile
import os
import numpy as np

class TestClosestPointMeshBody(unittest.TestCase):
    def test_point_inside_triangle():
        p = Point3D(0, 0, 0)
        q = Point3D(1, 0, 0)
        r = Point3D(0, 1, 0)
        vertices = [p, q, r]

        point_in_triangle = Point3D(0.25, 0.25, 0)

        find = FindClosestPointMesh(point_in_triangle, [0, 1, 2], vertices)

        closest_point = find.check_barycentric_coordinates()
        assert(np.allclose(closest_point, point_in_triangle.to_array()))