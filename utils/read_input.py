from pathlib import Path
import pandas as pd
from point3d import Point3D

class ReadData:
    def __init__(self, filename: str) -> None:
        with open(filename) as f:
            self.lines = f.readlines()  

class ReadBody(ReadData):
    def __init__(self, filename: str) -> None:
        super().__init__(filename)  
        self.line_1 = self.lines[0].strip().split()  
        self.N_markers = int(self.line_1[0])   # num of marker LEDs
        self.name = self.line_1[1].replace("\n","")  # ascii string giving file name
        # find next N_markers records
        self.markers = [list(map(float, line.strip().split())) for line in self.lines[1:self.N_markers + 1]]
        # find coordinates of tip in body coordinates
        self.tip = list(map(float, self.lines[self.N_markers+1].strip().split())) 

class ReadMesh(ReadData):
    def __init__(self, filename: str) -> None:
        super().__init__(filename)  
        self.line_1 = self.lines[0].strip().split()  
        self.N_vertices = int(self.line_1[0])   # num of verticies
        # find next N_verticies records
        vertices = [list(map(float, line.strip().split())) for line in self.lines[1:self.N_vertices + 1]]
        self.vertices = []
        for vertex in vertices:
            self.vertices.append(Point3D(vertex[0], vertex[1], vertex[2]))

        self.N_triangles = int(self.lines[self.N_vertices+1])   # num of triangles
        # find next N_triangles records
        self.triangles_indices = [list(map(int, line.strip().split()))[:3] for line in self.lines[self.N_vertices+2:self.N_vertices + self.N_triangles + 2]]
        self.neighbors_indices = [list(map(int, line.strip().split()))[3:] for line in self.lines[self.N_vertices+2:self.N_vertices + self.N_triangles + 2]]

class ReadSampleReadings(ReadData):
    def __init__(self, filename: str) -> None:
        super().__init__(filename)  
        self.line_1 = self.lines[0].strip().split(', ')  
        self.N_s = int(self.line_1[0])   # num of LEDs read by the tracker in each sample frame
        # N_s = N_a + N_b + N_d
        self.N_samps = int(self.line_1[1]) # num of sample frames
        self.name = self.line_1[2].replace(" 0","")  # ascii string giving file name
        self.N_a, self.N_b, self.N_d = 6, 6, 4
        self.A_coords = []
        self.B_coords = []
        self.D_coords = []
        for i in range(self.N_samps):
            A = [list(map(float, line.strip().split(', '))) for line in self.lines[1+(self.N_s*i):1+(self.N_s*i)+self.N_a]]
            self.A_coords.append(A)
            B = [list(map(float, line.strip().split(', '))) for line in self.lines[1+(self.N_s*i)+self.N_a:1+(self.N_s*i)+self.N_a+self.N_b]]
            self.B_coords.append(B)
            D = [list(map(float, line.strip().split(', '))) for line in self.lines[1+(self.N_s*i)+self.N_a+self.N_b:1+(self.N_s*i)+self.N_a+self.N_b+self.N_d]]
            self.D_coords.append(D)

    def get_A_coords_at_I(self, frame_number: int):
        return self.A_coords[frame_number]
    def get_B_coords_at_I(self, frame_number: int):
        return self.B_coords[frame_number]
    def get_D_coords_at_I(self, frame_number: int):
        return self.D_coords[frame_number]