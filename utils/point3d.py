from __future__ import annotations
import numpy as np


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_array(self):
        return np.array([self.x, self.y, self.z])
    
    def __sub__(self, other: Point3D):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def distance(self, other: Point3D):
        return np.linalg.norm(self.to_array() - other.to_array())
    
    # TODO: any other functions that we could use for both?