from __future__ import annotations
import numpy as np
from frame import Frame
from scipy.spatial.transform import Rotation as R
from scipy.linalg import svd

# Note: using same algorithm we used on question 12 of homework 1

class Registration:
    def __init__(self, source_points:np.ndarray, target_points:np.ndarray):
        """
        Initialize registration class for point to point registration
        Args:
            source_points (np.ndarray): points of source 
            target_points (np.ndarray): target points performing the registration to
        """

        self.source = np.array(source_points)
        self.target = np.array(target_points)

    def closest_points(self):
        """
        Determining the closest points and their respective distances between source and target
        Args:

        Returns:
            np.array: returns the closest points
            np.array: returns the distance of respective closest points
        """
        closest_points = []
        distances = []

        for point in self.source:
            # compute distance between points
            dist = np.linalg.norm(self.target - point, axis=1)
            min_index = np.argmin(dist)
            closest_points.append(self.target[min_index])
            distances.append(dist[min_index])

        return np.array(closest_points), np.array(distances)
    
    def icp(self, max_iterations = 100, tolerance = 1e-5) -> Frame:
        """Follows the iterative closest point algorithm to minimize the difference between 2 clouds of points
        Args:
            max_iterations (int): maximum number of times going through for loop
            tolerance (float): threshold for minimized error and optimized early before max_iterations

        Returns:
            Frame: final transformation frame
        """
        # complete setup for algorithm
        source = np.copy(self.source) # create a copy of source point array
        total_rot = np.eye(3)
        total_trans = np.zeros(3)

        prev_error = float('inf')

        for i in range(max_iterations):
    
            # find closest points
            closest_points, _ = self.closest_points()

            # compute centroids and subtract to find center
            src_centroid = np.mean(source, axis=0)
            src_center = source - src_centroid
            target_centroid = np.mean(closest_points, axis=0)
            target_center = closest_points - target_centroid

            # cross-covariance matrix
            H = src_center.T @ target_center
            U, _, Vt = svd(H)

            # compute R
            rotation_opt = Vt.T @ U.T 

            # make sure det(R) == 1
            # Ensure the rotation matrix is a proper rotation
            if np.linalg.det(rotation_opt) < 0:
                Vt[2, :] *= -1  
                rotation_opt = Vt.T @ U.T

            # compute translation and apply transformation
            translation_opt = target_centroid.T - rotation_opt @ src_centroid
            source = (rotation_opt @ source.T).T + translation_opt

            # compute mean squared error
            curr_error = np.mean(np.linalg.norm(source - closest_points, axis=1))

            # check if already optimized and if so break out of for loop
            if abs(prev_error - curr_error) < tolerance:
                break

            prev_error = curr_error


        return Frame(rotation_opt, translation_opt)
