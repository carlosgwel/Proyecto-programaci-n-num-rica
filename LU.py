import numpy as np

def lu(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    
    # Inicializamos L con 1s en la diagonal
    for i in range(n):
        L[i][i] = 1.0
    
    # Descomposición
    for k in range(n):
        U[k][k] = A[k][k] - sum(L[k][j] * U[j][k] for j in range(k))
        for i in range(k + 1, n):
            U[k][i] = A[k][i] - sum(L[k][j] * U[j][i] for j in range(k))
        for i in range(k + 1, n):
            L[i][k] = (A[i][k] - sum(L[i][j] * U[j][k] for j in range(k))) / U[k][k]
    
    return L, U


A1 = [[4, -2, 1], [-2, 4, -2], [1, -2, 4]]
L1, U1 = lu(A1)
print("Sistema 1 - L:", L1)
print("Sistema 1 - U:", U1)