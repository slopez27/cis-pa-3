from __future__ import annotations
import numpy as np
import logging
from typing import Union

log = logging.getLogger(__name__)

class Frame:
    def __init__(self, r: np.ndarray, t: np.ndarray) -> None:
        """Create a frame with rotation 'r' and translation t
        
        Args:
            rotation (np.ndarray): _description_
            translation(np.ndarray): _description_
        """
        self.rotation = np.array(r)
        self.translation = np.array(t)

    def __array__(self):
        out = np.eye(4, dtype=np.float32)
        out[:3, :3] = self.rotation
        out[:3, 3] = self.translation
        return out

    def __str__(self) -> str:
        rotation_str = np.array_str(self.rotation, precision=4, suppress_small=True)
        translation_str = np.array_str(self.translation, precision=4, suppress_small=True)
        return f"Rotation:\n{rotation_str}\nTranslation:\n{translation_str}"

    
    def inv(self) -> Frame:
        return Frame(self.rotation.T, -(self.rotation.T @ self.translation))
    
    def __matmul__(self, other: Union[np.ndarray, Frame]) -> Frame:
        """_summary_
        Args:
            other (Union[np.ndarray, Frame]): _description_

        Returns:
            Frame: _description_
        """

        if isinstance(other, np.ndarray):
            return (self.rotation @ other.T).T + self.translation
        
        elif isinstance(other, Frame):
            return Frame(self.rotation @ other.rotation, self.rotation @ other.translation + self.translation)
        
        else:
            raise TypeError
        