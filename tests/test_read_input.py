import unittest
import tempfile
import os
import numpy as np
import sys
sys.path.append('../utils/')
from read_input import ReadBody

class TestReadBody(unittest.TestCase):

    def test_read_body(self):
        reader = ReadBody('../data/Problem3-BodyA.txt')
        self.assertEqual(reader.N_markers, 6)
        self.assertEqual(reader.name, 'Problem3-BodyA.txt')
        self.assertEqual(len(reader.markers), reader.N_markers)
        self.assertEqual(reader.markers,[[-49.999, -36.846, 25.561], [-4.135, 3.277, -28.104], [-45.296, 17.886, 17.93], [43.469, -11.65, 1.942], [33.097, -46.543, -44.654], [2.97, 17.115, -49.23]])
        self.assertEqual(reader.tip,[0.0, 0.0, -100.0])
        print("Passed test_read_body!")


if __name__ == "__main__":
    unittest.main()
