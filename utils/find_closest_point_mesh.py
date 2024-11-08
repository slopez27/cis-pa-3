import numpy as np
from point3d import Point3D

# right now we are starting with the barycentric form discussed 
# in Dr. Taylor's slides called Finding point-pairs (FindClosestPoint(a, [p, q, r]))

class FindClosestPointMesh:
    def __init__(self, point: Point3D, triangle: list[int], vertices: list[Point3D]):
        self.a = point.to_array()               # point
        self.triangle = triangle                # triangle is a list of 3 vertex indices
        self.vertices = vertices                # list of all vertices

        p, q, r = [vertices[i] for i in triangle]

        self.p = p.to_array()                 # first vertex point as an array
        self.q = q.to_array()                 # second vertex point as an array
        self.r = r.to_array()                 # third vertex point as an array

    def compute_vectors(self):
        ab = self.q - self.p
        ac = self.r - self.p
        ap = self.a - self.p

        return ab, ac, ap
    
    def compute_dot_products(self):
        ab, ac, ap = self.compute_vectors()

        d1 = np.dot(ab, ap)
        d2 = np.dot(ac, ap)
        d3 = np.dot(ab, ab)
        d4 = np.dot(ac, ab)
        d5 = np.dot(ac, ac)

        return d1, d2, d3, d4, d5
    
    def barycentric_coordinate_check(self):
        d1, d2, d3, d4, d5 = self.compute_dot_products()
        if d1 <= 0 and d2 <= 0:
            return self.p
        elif d3 <= d1 and d4 <= d2:
            return self.q
        elif d5 <= d2 and d4 <= d1:
            return self.r
        
if __name__ == "__main__":
    pass

