"Carlos Gael Ortega Ruiz"
import numpy as np

def problema4():
    
    try:
        n = 5
        
        if n > 0:
            vector = np.random.randint(1, 10, n)
            print("el número es válido")
            print("vector generado:", vector)
            
       
            matriz = np.array([[vector[j] * (i + 1) for j in range(n)] for i in range(n)])
            print("matriz generada:")
            print(matriz)
        else:
            print("error: el número debe ser un entero positivo")
    
    except ValueError:
        print("error: debes ingresar un número entero válido.")

problema4()
