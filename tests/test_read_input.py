import unittest
import tempfile
import os
import numpy as np
import sys
sys.path.append('../utils/')
from read_input import ReadBody, ReadMesh

class TestReadBody(unittest.TestCase):

    def test_read_body(self):
        reader = ReadBody('../data/Problem3-BodyA.txt')
        self.assertEqual(reader.N_markers, 6)
        self.assertEqual(reader.name, 'Problem3-BodyA.txt')
        self.assertEqual(len(reader.markers), reader.N_markers)
        self.assertEqual(reader.markers,[[-49.999, -36.846, 25.561], [-4.135, 3.277, -28.104], [-45.296, 17.886, 17.93], [43.469, -11.65, 1.942], [33.097, -46.543, -44.654], [2.97, 17.115, -49.23]])
        self.assertEqual(reader.tip,[0.0, 0.0, -100.0])
        print("Passed test_read_body!")

class TestReadMesh(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        self.temp_file.write("5\n")  # Sample data
        self.temp_file.write("1.0 2.0 3.0\n" * 5)  # N_verticies = 5
        self.temp_file.write("3\n")  # Sample data
        self.temp_file.write("8 9 10 -1 4 5\n" * 3)  # N_triangles = 3
        self.temp_file.seek(0)
        self.temp_file.close()

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_read_mesh(self):
        reader = ReadMesh(self.temp_file.name)
        self.assertEqual(reader.N_verticies, 5)
        self.assertEqual(reader.N_triangles, 3)
        self.assertEqual(reader.triangles_indicies, [[8, 9, 10], [8, 9, 10], [8, 9, 10]])
        self.assertEqual(reader.neighbors_indicies, [[-1, 4, 5], [-1, 4, 5], [-1, 4, 5]])
        print("Passed test_read_mesh!")

if __name__ == "__main__":
    unittest.main()
