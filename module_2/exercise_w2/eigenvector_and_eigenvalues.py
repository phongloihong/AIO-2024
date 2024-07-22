import numpy as np


def compute_eigenvalues_eigenvectors(matrix: np.ndarray):
    eig = np.linalg.eig(matrix)
    return eig.eigenvalues, eig.eigenvectors
