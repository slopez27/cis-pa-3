from frame import Frame
from point3d import Point3D
from read_input import ReadMesh, ReadSampleReadings, ReadBody
from find_dk import find_dk
from find_closest_point_mesh import FindClosestPointMesh
from find_closest_point_triangle import FindClosestPointTriangle
from sample_points import SamplePoints
from output_pa3 import output


def main(name: str, X: str, Y: str):
    filename_mesh = f"Problem{X}MeshFile"
    filename_sample_readings = f"{name}-SampleReadings.txt"
    filename_body = f"Problem{X}-Body{Y}"

    sample_readings = ReadSampleReadings(filename_sample_readings)
    mesh = ReadMesh(filename_mesh)
    body = ReadBody(filename_body)

    a_coords = sample_readings.A_coords
    b_coords = sample_readings.B_coords
    a_tip = body.tip

    solve_for_d_k = find_dk(a_coords, b_coords, a_tip)
    d_k = solve_for_d_k.compute_dk()
    
    sample_points = SamplePoints(d_k)

    c_k = sample_points.solve_for_c_k()
    s_k = sample_points.solve_for_s_k(filename_mesh)

    n_samples = sample_readings.N_samps

    write_to_file = output(n_samples, name, d_k, s_k)

if __name__ == "__main__":
    name = "PA3-A-Debug"
    X = '3'
    Y = 'A'
    main(name, X, Y)