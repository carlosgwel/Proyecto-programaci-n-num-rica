"Carlos Gael Ortega Ruiz"
import numpy as np

def problema1():
    
    try:
        n = 3.5
        
        if n > 0:
            vector = np.random.randint(1, 10, n)
            print("el número es válido")
            print("vector generado:", vector)
        else:
            print("error: el número debe ser un entero positivo")
    
    except ValueError:
        print("error: debes ingresar un número entero válido.")

problema1()
