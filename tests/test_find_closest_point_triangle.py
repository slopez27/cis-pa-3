import sys
sys.path.append('utils/')
from point3d import Point3D
from find_closest_point_triangle import FindClosestPointTriangle

import unittest
import tempfile
import os
import numpy as np

class TestClosestPointMeshBody(unittest.TestCase):

    def test_point_inside_triangle(self):
        p = Point3D(0, 0, 0)
        q = Point3D(1, 0, 0)
        r = Point3D(0, 1, 0)
        vertices = [p, q, r]

        point_in_triangle = Point3D(0.25, 0.25, 0)

        find = FindClosestPointTriangle(point_in_triangle, [0, 1, 2], vertices)

        closest_point = find.check_barycentric_coordinates()
        self.assertTrue(np.allclose(closest_point, point_in_triangle.to_array()))
        print(closest_point)
        print("Passed test_point_inside_triangle!")

    def test_point_outside_triangle(self):
        p = Point3D(0, 0, 0)
        q = Point3D(1, 0, 0)
        r = Point3D(0, 1, 0)
        vertices = [p, q, r]

        point_outside_triangle = Point3D(1, 1, 0)

        find = FindClosestPointTriangle(point_outside_triangle, [0, 1, 2], vertices)
        
        expected_closest_point = Point3D(.5, .5, 0).to_array()
        closest_point = find.check_barycentric_coordinates()
        self.assertTrue(np.allclose(closest_point, expected_closest_point))

        print("Passed test_point_outside_triangle!")
        

    def test_point_on_edge(self):
        p = Point3D(0, 0, 0)
        q = Point3D(1, 0, 0)
        r = Point3D(0, 1, 0)
        vertices = [p, q, r]

        point_on_edge = Point3D(0.5, 0, 0)

        find = FindClosestPointTriangle(point_on_edge, [0, 1, 2], vertices)

        closest_point = find.check_barycentric_coordinates()
        self.assertTrue(np.allclose(closest_point, point_on_edge.to_array()))

        print("Passed test_point_on_edge!")

    def test_point_above_triangle(self):
        p = Point3D(0, 0, 0)
        q = Point3D(1, 0, 0)
        r = Point3D(0, 1, 0)
        vertices = [p, q, r]

        point_above = Point3D(.25, .25, 1)

        find = FindClosestPointTriangle(point_above, [0, 1, 2], vertices)

        expected_closest_point = Point3D(.25, .25, 0).to_array()
        closest_point = find.check_barycentric_coordinates()
        self.assertTrue(np.allclose(closest_point, expected_closest_point))

        print("Passed test_point_above_triangle!")
        

if __name__ == "__main__":
    unittest.main()