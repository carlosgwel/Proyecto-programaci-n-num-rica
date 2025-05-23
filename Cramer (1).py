import numpy as np

A1 = [[4, -2, 1], [-2, 4, -2], [1, -2, 4]]
b1 = [11, -16, 17]
det_A1 = np.linalg.det(A1)

A1_x = [[11, -2, 1], [-16, 4, -2], [17, -2, 4]]  
A1_y = [[4, 11, 1], [-2, -16, -2], [1, 17, 4]]
A1_z = [[4, -2, 11], [-2, 4, -16], [1, -2, 17]]   

det_A1_x = np.linalg.det(A1_x)
det_A1_y = np.linalg.det(A1_y)
det_A1_z = np.linalg.det(A1_z)

x1 = det_A1_x / det_A1
y1 = det_A1_y / det_A1
z1 = det_A1_z / det_A1
print("Solución Sistema 1 : x =", x1, "y =", y1, "z =", z1)

A2 = [[1, 1, 1], [1, 2, 5], [1, 4, 25]]
b2 = [6, 12, 36]
det_A2 = np.linalg.det(A2)

A2_x = [[6, 1, 1], [12, 2, 5], [36, 4, 25]]
A2_y = [[1, 6, 1], [1, 12, 5], [1, 36, 25]]
A2_z = [[1, 1, 6], [1, 2, 12], [1, 4, 36]]

det_A2_x = np.linalg.det(A2_x)
det_A2_y = np.linalg.det(A2_y)
det_A2_z = np.linalg.det(A2_z)

x2 = det_A2_x / det_A2
y2 = det_A2_y / det_A2
z2 = det_A2_z / det_A2
print("Solución Sistema 2 : x =", x2, "y =", y2, "z =", z2)

A3 = [[1, 2, 1], [3, 8, 1], [0, 4, 1]]
b3 = [2, 12, 2]
det_A3 = np.linalg.det(A3)

A3_x = [[2, 2, 1], [12, 8, 1], [2, 4, 1]]
A3_y = [[1, 2, 1], [3, 12, 1], [0, 2, 1]]
A3_z = [[1, 2, 2], [3, 8, 12], [0, 4, 2]]

det_A3_x = np.linalg.det(A3_x)
det_A3_y = np.linalg.det(A3_y)
det_A3_z = np.linalg.det(A3_z)

x3 = det_A3_x / det_A3
y3 = det_A3_y / det_A3
z3 = det_A3_z / det_A3
print("Solución Sistema 3  x =", x3, "y =", y3, "z =", z3)