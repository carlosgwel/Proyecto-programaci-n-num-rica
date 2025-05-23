
import math
import matplotlib.pyplot as plt
def f(x):
    return 8 * x * math.sin(x) * math.exp(-x) - 1
x, x1 = 0.5, -0.3
iteraciones = 5
x_values = [x, x1]
errors = []
for i in range(iteraciones):
    x2 = x1 - f(x1) * (x1 - x) / (f(x1) - f(x))
    error_relativo = abs((x2 - x1) / x2) * 100
    x_values.append(x2)
    print(f"Iteración {i+1}: x = {x2}, el error relativo es = {error_relativo}%")
    x, x1 = x1, x2
x_vals = [i * 0.1 for i in range(-10, 20)]
y_vals = [f(x) for x in x_vals]
plt.plot(x_vals, y_vals, label="f(x)")
plt.scatter(x_values[-1], f(x_values[-1]), color="black", label="raiz") 

