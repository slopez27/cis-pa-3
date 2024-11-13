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
        bounding_boxes = []
        for triangle_indices in self.triangles_indices:
            p = self.vertices[triangle_indices[0]].to_array()
            q = self.vertices[triangle_indices[1]].to_array()
            r = self.vertices[triangle_indices[2]].to_array()

            # Calculate the lower and upper bounds
            lower = np.min([p, q, r], axis=0)
            upper = np.max([p, q, r], axis=0)
            bounding_boxes.append((lower, upper))
        start = time.time()
        closest_points = []
        for point in self.points:
            # Initialize minimum bound and closest point
            bound = np.inf
            closest_point = None
            point = Point3D(point[0], point[1], point[2])
            point_coords = point.to_array()
            for (triangle_indices, (lower, upper)) in zip(self.triangles_indices, bounding_boxes):
                # Check if the point is within the expanded bounding box
                if np.all(lower - bound <= point_coords) and np.all(point_coords <= upper + bound):
                    # Compute the closest point on the triangle
                    p = self.vertices[triangle_indices[0]].to_array()
                    q = self.vertices[triangle_indices[1]].to_array()
                    r = self.vertices[triangle_indices[2]].to_array()

                    h = FindClosestPointTriangle(point, triangle_indices, self.vertices).check_barycentric_coordinates()
                    h_coords = np.array([h[0], h[1], h[2]])
                    distance = np.linalg.norm(h_coords - point_coords)
                    if distance < bound:
                        closest_point = h_coords
                        bound = distance
            closest_points.append(closest_point)
        end = time.time()
        print(f"Time for iterate_bounding_boxes: {end - start} seconds")
        return closest_points
if __name__=="__main__":
    pass
