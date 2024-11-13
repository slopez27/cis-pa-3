# cis-pa-3
Programming Assignment 3 for CIS 601.455 Fall 2024

Diana Leigh Neste

Samanta Lopez

Instructions: 
* Use Python 3.12.6
* Option to run main.py with arguments from within utils folder.
* Option to run any test file from within tests folder. 
* To automate the creation of the all output3 files, in terminal run:
      chmod +x run_all_files.sh
      ./run_all_files.sh
* To automate comparison of the debug output3 files, in terminal run from utils folder:
      chmod +x compare.sh
      ./compare.sh
main_pa3.py
* This is where the main of our program is.
* Takes input arguments:
  *  name (str): input test case (e.g. "PA3-A-Debug")
  *  X (int): problem number (3 in this case)

read_input.py
* parsing the various types of input files

frame.py
* Cartesian math package for 3D points, rotations, and frame transformations


find_closest_point_triangle.py
* finds cloesest point on given triangle using barycentric form

find_closest_point_mesh.py
* applies brute force method

find_dk.py
* does point cloud - point cloud registration and transformation to caclulate d_k

point3d.py
* class representing a point

sample_points.py
* calculate s_k

output_pa3.py
* format data and write to files