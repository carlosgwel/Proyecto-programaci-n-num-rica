import matplotlib.pyplot as plt
import math

def f(x):
    return x**3 - 2*x**2 - 5*x + 6

def df(x):
    return 3*x**2 - 4*x - 5

x0 = 0.8
iteraciones = 5
x_values = [x0]

for i in range(iteraciones):
    x1 = x0 - f(x0) / df(x0)
    x_values.append(x1)
    print(f"Iteración {i+1}: x = {x1}")
    x0 = x1

x_vals = [i * 0.1 for i in range(-10, 20)]
y_vals = [f(x) for x in x_vals]
plt.plot(x_vals, y_vals, label="f(x)")
plt.scatter(x_values[-1], f(x_values[-1]), color="black", label="raiz")