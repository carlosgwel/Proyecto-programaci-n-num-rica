import numpy as np
from sympy import symbols, integrate, cos, exp

variable = symbols('x')
def f1(x): return 2 * np.cos(2 * x)
def f2(x): return -x**2 - x/2 + 4
def f3(x): return np.exp(-x**2)

limites_a = [0, 0.5, 0]
limites_b = [np.pi/4, 1.5, 1]
funciones = [f1, f2, f3]
funciones_sympy = [2 * cos(2 * variable), -variable**2 - variable/2 + 4, exp(-variable**2)]
valores_analiticos = [1.0, 29/12, 0.7468241328]

def trapecio_simple(func, a, b):
    return (b - a) / 2 * (func(a) + func(b))

def trapecio_multiple(func, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    return h / 2 * (func(x[0]) + 2 * sum(func(x[1:-1])) + func(x[-1]))

def simpson_13(func, a, b, n=2):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    return h / 3 * (func(x[0]) + 4 * sum(func(x[1::2])) + 2 * sum(func(x[2:-1:2])) + func(x[-1]))

def simpson_38(func, a, b, n=3):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    suma = func(x[0]) + func(x[-1])
    for i in range(1, n):
        suma += 3 * func(x[i]) if i % 3 != 0 else 2 * func(x[i])
    return 3 * h / 8 * suma

def error_relativo(analitico, calculado):
    return abs((analitico - calculado) / analitico) * 100

print('Integrales Analíticals')
for i, f in enumerate(funciones_sympy):
    integral = integrate(f, (variable, limites_a[i], limites_b[i]))
    print(f'Función {i+1}: {float(integral):.6f}')

print('Trapecio Simple ')
for i in range(3):
    resultado = trapecio_simple(funciones[i], limites_a[i], limites_b[i])
    error = error_relativo(valores_analiticos[i], resultado)
    print(f'Función {i+1}: {resultado:.6f}, Error: {error:.6f}%')

print('Trapecio Múltiple')
for i in range(3):
    for n in [2, 4, 6]:
        resultado = trapecio_multiple(funciones[i], limites_a[i], limites_b[i], n)
        error = error_relativo(valores_analiticos[i], resultado)
        print(f'Función {i+1}, n={n}: {resultado:.6f}, Error: {error:.6f}%')

print('Simpson 1/3')
for i in range(3):
    resultado = simpson_13(funciones[i], limites_a[i], limites_b[i])
    error = error_relativo(valores_analiticos[i], resultado)
    print(f'Función {i+1}: {resultado:.6f}, Error: {error:.6f}%')

print('Simpson 3/8')
for i in range(3):
    resultado = simpson_38(funciones[i], limites_a[i], limites_b[i])
    error = error_relativo(valores_analiticos[i], resultado)
    print(f'Función {i+1}: {resultado:.6f}, Error: {error:.6f}%')