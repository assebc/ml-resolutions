from numpy import asarray
def sparse_matrix_multiplication(matrix_a, matrix_b):
    if not len(matrix_a[0]) == len(matrix_b):
        return [[]]
    else:
        return (asarray(matrix_a) @ asarray(matrix_b)).tolist()