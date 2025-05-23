x = [1, 2, 3, 5, 7]
y = [3, 6, 19, 99, 291]

n = len(x)
dif = [[0]*n for _ in range(n)]
for i in range(n):
    dif[i][0] = y[i]

for j in range(1,n):
    for i in range(n-j):
        dif[i][j] = (dif[i+1][j-1]-dif[i][j-1])/(x[i+j]-x[i])

coef = [dif[0][i] for i in range(n)]

def P(x_val):
    result = coef[-1]
    for i in range(n-2,-1,-1):
        result = result*(x_val - x[i]) + coef[i]
    return result

f4 = P(4)
print(f"f(4) = {f4:.2f}")

x_curve = [x[0] + i*(x[-1]-x[0])/100 for i in range(101)]
y_curve = [P(xi) for xi in x_curve]

import matplotlib.pyplot as plt
plt.scatter(x, y, color='red')
plt.plot(x_curve, y_curve, 'b-')
