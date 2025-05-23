"Carlos Gael Ortega Ruiz"
import numpy as p

def multiplos_fila(n):

    v = p.random.randint(1, 10, n)
    print("vector generado : fila:", v)
    matriz = p.array([[v[j] * (i + 1) for j in range(n)] for i in range(n)])
    print("matriz generada:")
    print(matriz)

def multiplos_columna(n):

    v = p.random.randint(1, 10, n)
    print("vector generado :columna:", v)
    matriz = p.array([[v[i] * (j + 1) for j in range(n)] for i in range(n)])
    print("matriz generada:")
    print(matriz)

def ejercicio5():
    try:
        n = 4
        if n > 0:
            multiplos_fila(n)
            multiplos_columna(n)
        else:
            print("error: el número debe ser entero y positivo.")
    except ValueError:
        print("error: debes ingresar un número entero válido.")

if __name__ == "__main__":
    ejercicio5()
