#TODO: Diana solve this today :) 
import numpy as np

class find_dk:
    def __init__(self, a_coords, b_coords, a_tip):
        """
        Initialize with arrays of coordinates and the tip position of A.
        Args:
            a_coords (numpy array): shape (N, 3) for LED marker positions in frame A.
            b_coords (numpy array): shape (N, 3) for LED marker positions in frame B.
            a_tip (numpy array): shape (3) for the tip position in frame A.
        """
        self.a_coords = np.array(a_coords)
        self.b_coords = np.array(b_coords)
        self.a_tip = np.array(a_tip)

    def transform(self, source_points, target_points):
        """
        Calculate the rigid body transformation from source to target points.
        Uses Singular Value Decomposition (SVD) for point cloud - point cloud registration.
        Args: 
            source_points (numpy array): shape (N, 3)
            target_points (numpy array): shape (N, 3)
        Returns:
            Rotation matrix R and translation vector t
        """
        # Compute centroids
        source_centroid = np.mean(source_points, axis=0)
        target_centroid = np.mean(target_points, axis=0)
        # Center the points
        source_centered = source_points - source_centroid
        target_centered = target_points - target_centroid
        # Compute covariance matrix
        H = source_centered.T @ target_centered
        # SVD
        U, S, Vt = np.linalg.svd(H)
        R = Vt.T @ U.T
        # Ensure a right-handed coordinate system
        if np.linalg.det(R) < 0:
            Vt[-1, :] *= -1
            R = Vt.T @ U.T
        # Translation
        t = target_centroid - R @ source_centroid
        return R, t

    def compute_dk(self):
        """
        Compute dk for each sample point given the coordinates of LED markers.
        Returns:
            numpy array of dk values for each sample
        """
        R, t = self.transform(self.a_coords, self.b_coords)
        dk_array = np.array([R @ self.a_tip + t ])
        return dk_array
