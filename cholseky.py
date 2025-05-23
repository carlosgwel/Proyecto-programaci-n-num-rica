import numpy as np

def cholesky(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1):
            if i == j:
                L[i][i] = (A[i][i] - sum(L[i][k] ** 2 for k in range(i))) ** 0.5
            else:
                L[i][j] = (A[i][j] - sum(L[i][k] * L[j][k] for k in range(j))) / L[j][j]
    
    return L

A1 = [[4, -2, 1], [-2, 4, -2], [1, -2, 4]]
L = cholesky(A1)
print("Cholesky - L:", L)

