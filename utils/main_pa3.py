from frame import Frame
from point3d import Point3D
from read_input import ReadSampleReadings, ReadBody
from find_dk import find_dk
from sample_points import SamplePoints
from output_pa3 import output
from pathlib import Path


def main(name: str, X: str):
    filename_mesh = Path(f"../data/Problem{X}MeshFile.sur")
    filename_sample_readings = Path(f"../data/{name}-SampleReadingsTest.txt")
    filename_body_a = Path(f"../data/Problem{X}-BodyA.txt")
    filename_body_b = Path(f"../data/Problem{X}-BodyB.txt")

    sample_readings = ReadSampleReadings(filename_sample_readings)
    body_a = ReadBody(filename_body_a)
    body_b = ReadBody(filename_body_b)

    n_samples = sample_readings.N_samps
    d_k = []
    s_k = []
    a_tip = body_a.tip

    for i in range(n_samples):
        a_tracker = sample_readings.A_coords[i]
        b_tracker = sample_readings.B_coords[i]
        solve_for_d_k = find_dk(a_tracker, b_tracker, body_a.markers, body_b.markers, a_tip)
        d_k.append(solve_for_d_k.compute_dk())

    sample_points = SamplePoints(d_k)
    s_k = sample_points.solve_for_s_k(filename_mesh)

    output(n_samples, name, d_k, s_k).write_to_file()

if __name__ == "__main__":
    name = "PA3-C-Debug"
    X = '3'
    main(name, X)