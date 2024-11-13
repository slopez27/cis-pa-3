import sys
sys.path.append('../utils/')
from point3d import Point3D
from find_closest_point_mesh import FindClosestPointMesh
from read_input import ReadMesh, ReadBody

import unittest
import tempfile
import os
import numpy as np

class TestClosestPointMeshBody(unittest.TestCase):
    def setUp(self):
        self.tempfile = tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.sur')
        self.tempfile.write("3\n")  # Number of vertices
        self.tempfile.write("0 0 0\n")  # Vertex 1 (p)
        self.tempfile.write("1 0 0\n")  # Vertex 2 (q)
        self.tempfile.write("0 1 0\n")  # Vertex 3 (r)
        self.tempfile.write("1\n")  # Number of triangles
        self.tempfile.write("0 1 2 -1 -1 -1\n")  # Triangle defined by vertices (0,1,2)
        self.tempfile.flush()

        # Set up points to test
        self.point_inside = Point3D(0.25, 0.25, 0)
        self.point_on_edge = Point3D(0.5, 0, 0)
        self.point_outside = Point3D(1.2, 0.1, 0)
        self.point_above = Point3D(0.25, 0.25, 1)

    def tearDown(self):
        # Clean up the temporary file
        os.unlink(self.tempfile.name)

    def test_point_inside_triangle(self):
        points = [self.point_inside.to_array()]
        finder = FindClosestPointMesh(self.tempfile.name, points)
        closest_points = finder.iterate()
        
        expected_point = np.array([0.25, 0.25, 0])
        self.assertTrue(np.allclose(closest_points[0], expected_point))
        print("Passed test_point_inside_triangle!")

    def test_point_on_edge(self):
        points = [self.point_on_edge.to_array()]
        finder = FindClosestPointMesh(self.tempfile.name, points)
        closest_points = finder.iterate()
        
        expected_point = np.array([0.5, 0, 0])
        self.assertTrue(np.allclose(closest_points[0], expected_point))
        print("Passed test_point_on_edge!")

    def test_point_outside_near_triangle(self):
        points = [self.point_outside.to_array()]
        finder = FindClosestPointMesh(self.tempfile.name, points)
        closest_points = finder.iterate()
        
        expected_point = np.array([1, 0, 0])  # Closest point on the triangle edge
        self.assertTrue(np.allclose(closest_points[0], expected_point))
        print("Passed test_point_outside_near_triangle!")

    def test_point_above_triangle_plane(self):
        points = [self.point_above.to_array()]
        finder = FindClosestPointMesh(self.tempfile.name, points)
        closest_points = finder.iterate()
        
        expected_point = np.array([0.25, 0.25, 0])  # Projected onto the triangle
        self.assertTrue(np.allclose(closest_points[0], expected_point))
        print("Passed test_point_above_triangle_plane!")

    def test_multiple_points(self):
        points = [self.point_above.to_array(), self.point_inside.to_array(), self.point_on_edge.to_array(), self.point_outside.to_array()]
        finder = FindClosestPointMesh(self.tempfile.name, points)

        closest_points = finder.iterate()

        expected_points = [np.array([0.25, 0.25, 0]), np.array([0.25, 0.25, 0]), np.array([0.5, 0, 0]), np.array([1, 0, 0])]
        self.assertTrue(np.allclose(closest_points, expected_points))
        print("Passed test_multiple_points!")


if __name__ == '__main__':

    unittest.main()