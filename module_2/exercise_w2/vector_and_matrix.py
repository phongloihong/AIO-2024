import numpy as np


def compute_vector_length(vector: np.ndarray):
    return np.linalg.norm(vector)


def compute_dot_product(vector1: np.ndarray, vector2: np.ndarray):
    return np.dot(vector1, vector2)


def matrix_multi_vector(matrix: np.ndarray, vector: np.ndarray):
    return matrix.dot(vector)


def matrix_multi_matrix(matrix1: np.ndarray, matrix2: np.ndarray):
    return matrix1.dot(matrix2)


def inverse_matrix(matrix: np.ndarray):
    return np.linalg.inv(matrix)
