import numpy as np

A1 = [[4, -2, 1], [-2, 4, -2], [1, -2, 4]]
b1 = [11, -16, 17]
A1_inv = np.linalg.inv(A1)
x1 = np.matmul(A1_inv, b1)
print("Solución Sistema 1 . ", x1)

# Sistema 2
A2 = [[1, 1, 1], [1, 2, 5], [1, 4, 25]]
b2 = [6, 12, 36]
A2_inv = np.linalg.inv(A2)
x2 = np.matmul(A2_inv, b2)
print("Solución Sistema 2 :", x2)

# Sistema 3
A3 = [[1, 2, 1], [3, 8, 1], [0, 4, 1]]
b3 = [2, 12, 2]
A3_inv = np.linalg.inv(A3)
x3 = np.matmul(A3_inv, b3)
print("Solución Sistema 3 :", x3)