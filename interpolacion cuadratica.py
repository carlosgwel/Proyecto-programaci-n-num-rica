import matplotlib.pyplot as plt
x = [2, 3, 5]
y = [6, 19, 99]

b0 = y[0]
b1 = (y[1] - y[0]) / (x[1] - x[0])
b2 = ((y[2] - y[1]) / (x[2] - x[1]) - b1) / (x[2] - x[0])
def P(x_val):
    return b0 + b1 * (x_val - x[0]) + b2 * (x_val - x[0]) * (x_val - x[1])
f4 = P(4)
print(f"Estimación de f(4) por interpolación cuadrática: {f4:.2f}")

x_curve = [x[0] + i * (x[-1] - x[0]) / 100 for i in range(101)]
y_curve = [P(xi) for xi in x_curve]

plt.scatter(x, y, color='red', label='Puntos dados')
plt.plot(x_curve, y_curve, 'b-', label='Curva de interpolación cuadrática')
