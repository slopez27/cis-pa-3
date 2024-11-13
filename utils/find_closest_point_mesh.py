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
            


if __name__=="__main__":
    pass
