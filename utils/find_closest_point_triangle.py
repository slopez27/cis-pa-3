import numpy as np
from point3d import Point3D

# right now we are starting with the barycentric form discussed 
# in Dr. Taylor's slides called Finding point-pairs (FindClosestPoint(a, [p, q, r]))
class FindClosestPointTriangle:
    def __init__(self, point: Point3D, triangle: list[int], vertices: list[Point3D]):
        self.a = point.to_array()               # point
        self.triangle = triangle                # triangle is a list of 3 vertex indices
        self.vertices = vertices                # list of all vertices
   
        p = vertices[triangle[0]]
        q = vertices[triangle[1]]
        r = vertices[triangle[2]]

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
        if u >= 0 and v >= 0 and u + v <= 1:
            return self.p + u * (self.q - self.p) + v * (self.r - self.p)   # inside the triangle
        
        closest_to_edge_pq = self.closest_point_on_segment(self.p, self.q)
        closest_to_edge_pr = self.closest_point_on_segment(self.p, self.r)
        closest_to_edge_qr = self.closest_point_on_segment(self.q, self.r)

        distance_point_to_pq = (Point3D(self.a[0], self.a[1], self.a[2])).distance(Point3D(closest_to_edge_pq[0], closest_to_edge_pq[1], closest_to_edge_pq[2]))
        distance_point_to_pr = (Point3D(self.a[0], self.a[1], self.a[2])).distance(Point3D(closest_to_edge_pr[0], closest_to_edge_pr[1], closest_to_edge_pr[2]))
        distance_point_to_qr = (Point3D(self.a[0], self.a[1], self.a[2])).distance(Point3D(closest_to_edge_qr[0], closest_to_edge_qr[1], closest_to_edge_qr[2]))

        # return whichever corresponding point has the smallest distance
        if distance_point_to_pq < distance_point_to_pr and distance_point_to_pq < distance_point_to_qr:
            closest_point = closest_to_edge_pq
        
        elif distance_point_to_pr < distance_point_to_qr and distance_point_to_pr < distance_point_to_pq:
            closest_point = closest_to_edge_pr
        
        else:
            closest_point = closest_to_edge_qr
        
        return closest_point

    def closest_point_on_segment(self, x1, x2):
        X = np.subtract(x2, x1)
        t = np.dot(self.a - x1, X) / np.dot(X, X)
        t = max(0, min(t,1))
        return x1 + t * X

        
if __name__ == "__main__":
    pass

