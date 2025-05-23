"Carlos Gael Ortega Ruiz"
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 100)
plt.plot(x, np.sin(x), 'r--', linewidth=2, label="sin(x)")  
plt.plot(x, np.cos(x), 'b-.', linewidth=2, label="cos(x)")
plt.xlabel("eje X")
plt.ylabel("eje Y")
plt.title("funciones: sin(x) y cos(x)")
plt.legend()
plt.grid(True)
plt.show()
