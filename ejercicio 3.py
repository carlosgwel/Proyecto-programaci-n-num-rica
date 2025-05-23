"Carlos gael Ortega Ruiz"
import numpy as np

def problema3():
    
    
    
    try:
        n = int(input("ingresa un número entero y positivo: "))
        
        if n > 0:
            vector = np.random.randint(1, 10, n)
            print("el número es válido")
            print("vector generado:", vector)
            
     
            matriz = np.array([[vector[i] * (j + 1) for j in range(n)] for i in range(n)])
            print("matriz generada:")
            print(matriz)
        else:
            print("error: el número debe ser un entero positivo")
    
    except ValueError:
        print("error: debes ingresar un número entero válido.")

problema3()
