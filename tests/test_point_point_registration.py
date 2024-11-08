import unittest
import numpy as np
from scipy.spatial.transform import Rotation as R
import sys
sys.path.append('../utils/')
from point_point_registration import Registration
from frame import Frame

class TestRegistration(unittest.TestCase):

    def setUp(self):
        # Setup source and target points for testing
        self.source_points = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0]])
        self.target_points = np.array([[1, 1, 1], [2, 1, 1], [1, 2, 1], [2, 2, 1]])

        
        self.registration = Registration(self.source_points, self.target_points)
    
    def test_closest_points(self):
        # Reset source points to original state before calling closest_points
        self.registration.source = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0]])

        # Call closest_points method
        closest_points, distances = self.registration.closest_points()

        # Expected closest points based on target points
        expected_closest_points = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])

        # Expected distances manually
        expected_distances = [1.7320508075688772, 1.4142135623730951, 1.4142135623730951, 1.0]

        # Test if closest points match expected points
        np.testing.assert_array_almost_equal(closest_points, expected_closest_points, decimal=5)

        # Test if the distances match the expected distances
        np.testing.assert_array_almost_equal(distances, expected_distances, decimal=5)

    def test_icp(self):
        # Run ICP and obtain the transformation frame
        final_frame = self.registration.icp(max_iterations=10, tolerance=1e-5)
        
        # Check if the Frame object returned contains valid rotation and translation matrices
        self.assertIsInstance(final_frame, Frame)
        
        # Check the rotation matrix is orthogonal (R.T * R = I)
        rotation = final_frame.rotation
        identity = np.dot(rotation.T, rotation)
        np.testing.assert_array_almost_equal(identity, np.eye(3), decimal=5)
        
        # Check if determinant of the rotation matrix is 1 (to ensure proper rotation)
        self.assertAlmostEqual(np.linalg.det(rotation), 1.0, places=5)
        
        # Check if translation is of correct shape and matches expected values
        translation = final_frame.translation
        self.assertEqual(translation.shape, (3,))

        # Optionally, you could test specific values for rotation and translation in simple cases
        
if __name__ == "__main__":
    unittest.main()
