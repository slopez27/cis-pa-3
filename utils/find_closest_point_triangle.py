import numpy as np
from point3d import Point3D

# right now we are starting with the barycentric form discussed 
# in Dr. Taylor's slides called Finding point-pairs (FindClosestPoint(a, [p, q, r]))
"""
psedocode:

    project point onto plane of the triangle
    calculate barycentric coordinates
        define triangle vertices (p, q, r)
        let a be point for which we want to find the closest point
        compute the relevant vectors (qp, rp, ap)
        calculate all dot products of vectors (d1, d2, d3, d4, d5)
    if inside triangle ... return 
    if on triangle edge or outside... return call to closest point on segment... closest point on segment follows slides

"""

class FindClosestPointTriangle:
    def __init__(self, point: Point3D, triangle: list[int], vertices: list[Point3D]):
        self.a = point.to_array()               # point
        self.triangle = triangle                # triangle is a list of 3 vertex indices
        self.vertices = vertices                # list of all vertices

        p, q, r = [vertices[i] for i in triangle]

        self.p = p.to_array()                 # first vertex point as an array
        self.q = q.to_array()                 # second vertex point as an array
        self.r = r.to_array()                 # third vertex point as an array

    def compute_vectors(self):
        qp = self.q - self.p
        rp = self.r - self.p
        ap = self.a - self.p

        return qp, rp, ap
    
    def compute_dot_products(self):
        qp, rp, ap = self.compute_vectors()

        d1 = np.dot(qp, ap)
        d2 = np.dot(rp, ap)
        d3 = np.dot(qp, qp)
        d4 = np.dot(rp, qp)
        d5 = np.dot(rp, rp)

        return d1, d2, d3, d4, d5
    
    def barycentric_coordinate(self):
        d1, d2, d3, d4, d5 = self.compute_dot_products()
        
        # project the points (u and v) aka barycentric_coordinates
        denominator = d3 * d5 - d4 * d4
        u = (d5 * d1 - d4 * d2) / denominator
        v = (d3 * d2 - d4 * d1) / denominator

        return u, v

    def check_barycentric_coordinates(self):
        u, v = self.barycentric_coordinate()

        # check if projected points are in triangle
        if u >= 0 and v >= 0 and u + v < 1:
            return self.p + u * (self.q - self.p) + v * (self.r - self.p)   # inside the triangle

        # check if projected points are on triangle edges
        if v <= 0:          # edge pq
            return self.closest_point_on_segment(self.p, self.q)
        
        if u <= 0:          # edge pr
            return self.closest_point_on_segment(self.p, self.r)
        
        if u + v >= 1:      # edge qr
            return self.closest_point_on_segment(self.q, self.r)

    def closest_point_on_segment(self, x1, x2):
        X = x2 - x1
        t = np.dot(self.a - x1, X) / np.dot(X, X)
        t = max(0, min(1,t))
        return x1 + t * X

        
if __name__ == "__main__":
    pass

