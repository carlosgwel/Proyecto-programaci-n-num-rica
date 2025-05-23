import math
import matplotlib.pyplot as plt
def f(x):
    return 8 * x * math.sin(x) * math.exp(-x) - 1
def df(x):
    return 8 * math.sin(x) * math.exp(-x) + 8 * x * math.cos(x) * math.exp(-x) - 8 * x * math.sin(x) * math.exp(-x)
x = 0.3
iteraciones = 5
for i in range(iteraciones):
    xnuevo = x - f(x) / df(x) 
    error_relativo = abs((xnuevo - x) / xnuevo) * 100 
    print(f"Iteración {i+1}: x = {xnuevo}, el error relativo es = {error_relativo}%")
    x = xnuevo
x_vals = [i * 0.1 for i in range(-10, 20)]  
y_vals = [f(x) for x in x_vals]
plt.plot(x_vals, y_vals, label="f(x)") 
plt.scatter(x, f(x), color="black", label="raiz")

