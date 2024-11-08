from pathlib import Path
import pandas as pd

class ReadData:
    def __init__(self, filename: str) -> None:
        with open(filename) as f:
            self.lines = f.readlines()  
        self.line_1 = self.lines[0].strip().split()  

class ReadBody(ReadData):
    def __init__(self, filename: str) -> None:
        super().__init__(filename)  
        self.N_markers = int(self.line_1[0])   # num of marker LEDs
        self.name = self.line_1[1].replace("\n","")  # ascii string giving file name
        # find next N_markers records
        self.markers = [list(map(float, line.strip().split())) for line in self.lines[1:self.N_markers + 1]]
        # find coordinates of tip in body coordinates
        self.tip = list(map(float, self.lines[self.N_markers+1].strip().split())) 

class ReadMesh(ReadData):
    def __init__(self, filename: str) -> None:
        super().__init__(filename)  
        self.N_verticies = int(self.line_1[0])   # num of verticies
        # find next N_verticies records
        self.verticies = [list(map(float, line.strip().split())) for line in self.lines[1:self.N_verticies + 1]]
        self.N_triangles = int(self.lines[self.N_verticies+1])   # num of triangles
        # find next N_triangles records
        self.triangles_indicies = [list(map(int, line.strip().split()))[:3] for line in self.lines[self.N_verticies+2:self.N_verticies + self.N_triangles + 2]]
        self.neighbors_indicies = [list(map(int, line.strip().split()))[3:] for line in self.lines[self.N_verticies+2:self.N_verticies + self.N_triangles + 2]]
