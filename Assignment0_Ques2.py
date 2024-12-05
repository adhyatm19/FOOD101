from re import M
#problem 2
import numpy as np

def matrix_operation(a1, a2, op):
    def dot(a, b):
        return sum(a[i][j] * b[i][j] for i in range(a.shape[0]) for j in range(a.shape[1]))
    def mult(a, b):
        return([[sum(a[i][k] * b[k][j] for k in range(b.shape[0])) for j in range(b.shape[1])] for i in range(a.shape[0])])
    def det(arr):
      det = 0
      if arr.shape[0] > 2:
        for j in range(arr.shape[0]):
            element = np.multiply(((-1)**j)*arr[0][j],det(np.delete(arr[1:], j, 1)), dtype=object)
            det += element
        return det
      else:
        return arr[0][0]*arr[1][1] - arr[0][1]*arr[1][0]
        return determinant
    if op == "dot":
        return dot(a1, a2)
    elif op == "matrix":
        return mult(a1, a2)
    elif op == "determinant":
        det1 = det(a1)
        det2 = det(a2)
        return (det1, det2)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print("Dot", matrix_operation(arr1, arr2, "dot"))
print("Matrix", matrix_operation(arr1, arr2, "matrix"))
print("Determinants:", matrix_operation(arr1, arr2, "determinant"))
