import numpy as np


def compute_cosine_similarity(vector1: np.ndarray, vector2: np.ndarray):
    return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
