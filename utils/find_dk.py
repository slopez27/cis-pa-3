#TODO: Diana solve this today :) 
import numpy as np

class find_dk:
    def __init__(self, a_body, b_body, a_tracker, b_tracker, a_tip):
        """
        Initialize with arrays of coordinates and the tip position of A.
        Args:
            a_coords (numpy array): shape (N, 3) for LED marker positions in frame A.
            b_coords (numpy array): shape (N, 3) for LED marker positions in frame B.
            a_tip (numpy array): shape (3) for the tip position in frame A.
        """
        self.a_body = np.array(a_body)
        self.b_body = np.array(b_body)
        self.a_tracker = np.array(a_tracker)
        self.b_tracker = np.array(b_tracker)
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
        H = np.dot(source_centered.T, target_centered)
        # SVD
        U, S, Vt = np.linalg.svd(H)
        R = np.dot(Vt.T, U.T)
        # Ensure a right-handed coordinate system
        # print(f"determinant of R is: {np.linalg.det(R)}")
        if np.linalg.det(R) < 0:
            # print("entering that det of r is less than 0!!!!!")
            Vt[-1, :] *= -1
            R = np.dot(Vt.T, U.T)
        # Translation
        t = target_centroid - np.dot(R, source_centroid)
        return R, t

    def compute_dk(self):
        """
        Compute dk for each sample point given the coordinates of LED markers.
        Returns:
            numpy array of dk values for each sample
        """
        # print(f"about to find R and t for A!!!!!!!")
        R_a, t_a = self.transform(self.a_tracker, self.a_body)
        # print(f"about to find R and t for B!!!!!")
        R_b, t_b = self.transform(self.b_tracker, self.b_body)
        
        R_b_inv = np.linalg.inv(R_b)

        dk = np.dot(R_b_inv, (R_a @ self.a_tip)) + np.dot(R_b_inv, t_a) - np.dot(R_b_inv, t_b)
        # dk = R_b_inv @ f_a_k_a_tip + t_b_inv # extra negitive??
        # dk = np.array([R @ self.a_tip + t ])
        return dk
