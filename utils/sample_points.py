import numpy as np
from frame import Frame
from find_closest_point_mesh import FindClosestPointMesh

class SamplePoints:
    def __init__(self, d_k: list[list[float]]):
        self.F_reg = np.identity(4)             # unknown transformation s.t. c_k = F_reg x d_k
        self.d_k = np.asarray(d_k)


    def solve_for_c_k(self):
        return self.d_k
    
    def solve_for_s_k(self, filename: str) -> list[list[float]]:
        find = FindClosestPointMesh(filename, self.solve_for_c_k())
        s_k = find.iterate()                    # returns list of list of floats
        return s_k
    
