
x1, x2, x3 = 0, 0, 0


print("Método de Jacobi")
for i in range(3):
    x1_new = (7.85 + 0.1 * x2 + 0.2 * x3) / 1
    x2_new = (19.3 - 0.1 * x1 - 0.3 * x3) / 7
    x3_new = (71.4 - 0.3 * x1 + 0.2 * x2) / -10
    x1, x2, x3 = x1_new, x2_new, x3_new
    print(f"Iteración {i+1}: x1 = {x1}, x2 = {x2}, x3 = {x3}")

x1, x2, x3 = 0, 0, 0

print("Método de Gauss-Seidel:")
for i in range(3):
    x1 = (7.85 + 0.1 * x2 + 0.2 * x3) / 1
    x2 = (19.3 - 0.1 * x1 - 0.3 * x3) / 7
    x3 = (71.4 - 0.3 * x1 + 0.2 * x2) / -10
    print(f"Iteración {i+1}: x1 = {x1}, x2 = {x2}, x3 = {x3}")