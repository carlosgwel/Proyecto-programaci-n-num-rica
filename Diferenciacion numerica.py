import numpy as np

def funcion(x):
    return -x**2 - x/2 + 4

def derivada_analitica(x):
    return -2*x - 0.5


def diferencia_adelante(func, x, h):
    fx_h = func(x + h)
    fx_2h = func(x + 2*h)
    return (-fx_2h + 4*fx_h - 3*func(x)) / (2*h)


def diferencia_atras(func, x, h):
    fx_h = func(x - h)
    fx_2h = func(x - 2*h)
    return (3*func(x) - 4*fx_h + fx_2h) / (2*h)

def diferencia_centrada(func, x, h):
    fx_h = func(x + h)
    fx_2h = func(x + 2*h)
    fx_menosh = func(x - h)
    fx_menos2h = func(x - 2*h)
    return (-fx_2h + 8*fx_h - 8*fx_menosh + fx_menos2h) / (12*h)

def error_relativo(analitico, calculado):
    return abs((analitico - calculado) / analitico) * 100

punto = 0
valores_h = [0.2, 0.1]
valor_analitico = derivada_analitica(punto) 

print("derivadas numéricas de f(x) = -x^2 - x/2 + 4 en x = 0 ****")
print(f"analitica")

for h in valores_h:
    print(f" Para h = {h}")
    adelante = diferencia_adelante(funcion, punto, h)
    atras = diferencia_atras(funcion, punto, h)
    centrada = diferencia_centrada(funcion, punto, h)
    
    print(f"Diferencia hacia adelante: {adelante:.6f}, Error: {error_relativo(valor_analitico, adelante):.6f}%")
    print(f"Diferencia hacia atrás: {atras:.6f}, Error: {error_relativo(valor_analitico, atras):.6f}%")
    print(f"Diferencia centrada: {centrada:.6f}, Error: {error_relativo(valor_analitico, centrada):.6f}%")
    print()