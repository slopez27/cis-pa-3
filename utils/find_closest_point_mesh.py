import numpy as np
from point3d import Point3D

class FindClosestPointMesh:
    def __init__(self, point: Point3D, triangle: list[int], vertices: list[Point3D]):
        self.point = point.to_array()           # point
        self.triangle = triangle                # triangle is a list of 3 vertex indices
        self.vertices = vertices                # list of all vertices

        v0, v1, v2 = [vertices[i] for i in triangle]

        self.v0 = v0.to_array()                 # first vertex point as an array
        self.v1 = v1.to_array()                 # second vertex point as an array
        self.v2 = v2.to_array()                 # third vertex point as an array

