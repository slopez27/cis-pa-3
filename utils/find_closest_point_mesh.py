from find_closest_point_triangle import FindClosestPointTriangle
from point3d import Point3D
from read_input import ReadMesh
import numpy as np
import time

# THIS IS THE PART GOING TO START WITH BRUTE FORCE... keeping track of runtime here!

class FindClosestPointMesh:
    def __init__(self, filename, points: list[list[float]]):
        read_mesh_file = ReadMesh(filename)

        self.vertices = read_mesh_file.vertices
        self.triangles_indices = read_mesh_file.triangles_indices
        self.points = points

    def iterate(self):
        start = time.time()
        closest_points = []

        for point in self.points:  
            closest_point = None
            min = np.inf
            point = Point3D(point[0], point[1], point[2])

            for triangle in self.triangles_indices:
                find = FindClosestPointTriangle(point, triangle, self.vertices).check_barycentric_coordinates()

                distance = point.distance(Point3D(find[0], find[1], find[2]))
                if distance < min:
                    closest_point = find
                    min = distance

            closest_points.append(closest_point)
        end = time.time()
        print(f"Time for iterate: {end - start} seconds")
        return closest_points
    
    def iterate_bounding_boxes(self):
        """
        //triangle i has corners p, q, r
        bounding box lower is L_i = L_xi, L_yi, L_zi and upper is U_i = U_xi, U_yi, U_zi
        bound = infinity
        for i = 1 to N do
            if L_xi - bound <= a_x <= U_xi + bound and L_y_i - bound <= a_y <= U_yi + bound and L_zi - bound <= a_y <= U_zi + bound
                h = FindClosestPoint(a, [p,q,r])
                if magnitude(h - a) < bound then
                    c = h
                    bound = magniture(h - a)
        
        """
        start = time.time()
        closest_points = []

        for point in self.points:
            min = np.inf
            point = Point3D(point[0], point[1], point[2])

            for triangle in self.triangles_indices:
                bound = np.inf
                # TODO: define lower bounding box
                # TODO: define upper bounding box

                for i in range(len(self.triangles_indices)): # TODO: what is N supposed to be? number of triangles?
                    h = FindClosestPointTriangle(point, triangle, self.vertices).check_barycentric_coordinates()
                    
                    if np.linalg.norm(h - point.to_array()) < bound:
                        c = h
                        bound = np.linalg.norm(h = point.to_array())
        closest_points.append(c)
                
if __name__=="__main__":
    pass
