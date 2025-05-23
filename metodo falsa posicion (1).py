import matplotlib.pyplot as plt
import math

def f(x):
    return x - math.cos(x)

a, b = 0.5, 1.0
iteraciones = 5
x_values = [a, b]

for i in range(iteraciones):
    xi = b - (f(b) * (a - b)) / (f(a) - f(b))
    x_values.append(xi)
    print(f"Iteración {i+1}: x = {xi}")
    if f(a) * f(xi) < 0:
        b = xi
    else:
        a = xi

x_vals = [i * 0.1 for i in range(-10, 20)]
y_vals = [f(x) for x in x_vals]
plt.plot(x_vals, y_vals, label="f(x)")
plt.scatter(x_values[-1], f(x_values[-1]), color="black", label="raiz")