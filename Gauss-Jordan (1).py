import numpy as np

A1 = [[4, -2, 1], [-2, 4, -2], [1, -2, 4]]
b1 = [11, -16, 17]
x1 = np.linalg.solve(A1, b1)
print("Solución Sistema 1:", x1)

A2 = [[1, 1, 1], [1, 2, 5], [1, 4, 25]]
b2 = [6, 12, 36]
x2 = np.linalg.solve(A2, b2)
print("Solución Sistema 2:", x2)

A3 = [[1, 2, 1], [3, 8, 1], [0, 4, 1]]
b3 = [2, 12, 2]
x3 = np.linalg.solve(A3, b3)
print("Solución Sistema 3 ", x3)