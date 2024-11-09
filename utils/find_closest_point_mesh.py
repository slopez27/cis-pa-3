from find_closest_point_triangle import FindClosestPointTriangle
from point3d import Point3D
from read_input import ReadMesh, ReadBody

# THIS IS THE PART GOING TO START WITH BRUTE FORCE

class FindClosestPointMesh:
    def __init__(self, filename, points: list[Point3D]):
        read_mesh_file = ReadMesh(filename)

        N_vertices = read_mesh_file.N_vertices
        self.vertices = read_mesh_file.vertices
        N_triangles = read_mesh_file.N_triangles

        self.triangles_indices = read_mesh_file.triangles_indices
        neighbors_indices = read_mesh_file.neighbors_indices

        self.points = points

    def iterate(self):
        closest_points = []
        for point in self.points:
            find = FindClosestPointTriangle(point, self.triangles_indices, self.vertices)
            closest_points.append(find.check_barycentric_coordinates())
        return closest_points
            


if __name__=="__main__":
    # filename = 'Problem3MeshFile.sur'
    pass


