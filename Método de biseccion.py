import math
import matplotlib.pyplot as plt
def f(x):
    return 2 * x * math.cos(2 * x) - (x + 1)**2
a, b = -3, -2
iteraciones = 5
for i in range(iteraciones):
    c = (a + b) / 2
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
    print(f"Iteración {i+1}: x = {c}, intervalo = [{a}, {b}]")
x_vals = [i * 0.1 for i in range(-30, 20)]
y_vals = [f(x) for x in x_vals]
plt.plot(x_vals, y_vals)
plt.show()
plt.scatter(c,0, 'ro')
