import unittest
import tempfile
import os
import numpy as np
import sys
sys.path.append('../utils/')
import filecmp
from output_pa3 import output

N_samps = 2
letter = 'pa3-test'
d_k = [[1,2,3],[4,5,6]]
s_k = [[0,0,0],[0,0,0]]
test = output(N_samps, letter, d_k, s_k)
test.write_to_file()

class TestOutput(unittest.TestCase):
    def test_output(self):
        N_samps = 2
        name = 'pa3-test'
        path = "../outputs/pa3-test-Output.txt"
        comp_path = "../outputs/pa3-test-comp-Output.txt"
        d_k = [[1,2,3],[4,5,6]]
        s_k = [[0,0,0],[0,0,0]]
        test = output(N_samps, name, d_k, s_k)
        test.write_to_file()
        self.assertTrue(filecmp.cmp(path,comp_path,shallow=False))

if __name__ == "__main__":
    unittest.main()
