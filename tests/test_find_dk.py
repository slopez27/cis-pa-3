import unittest
import tempfile
import os
import numpy as np
import sys
sys.path.append('../utils/')
from find_dk import find_dk

class TestFindDk(unittest.TestCase):
    def test_read_body(self):
        a_coords = [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0]
        ]
        b_coords = [
            [1.1, 2.1, 3.1],
            [4.1, 5.1, 6.1],
            [7.1, 8.1, 9.1]
        ]
        a_tip = [0.5, 0.5, 0.5]
        dk_calculator = find_dk(a_coords, b_coords, a_tip)
        print(dk_calculator.compute_dk())
        self.assertTrue(np.allclose(dk_calculator.compute_dk(),[[-1.4, 0.6, 2.6],[-1.4, 0.6, 2.6],[-1.4, 0.6, 2.6]]))
        print("Passed test_find)dk!")

if __name__ == "__main__":
    unittest.main()