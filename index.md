# Proyecto de Programación numerica

Este repositorio contiene los programas en Python desarrollados durante el semestre.

## Temas y Programas

### 1. Resolución de Sistemas Lineales

- **Gauss-Jordan.py**: Resuelve tres sistemas lineales de 3x3 usando el método de Gauss-Jordan. Imprime las soluciones de los sistemas.

- **Matriz inversa.py**: Resuelve tres sistemas lineales de 3x3 usando el método de la inversa de la matriz. Imprime las soluciones.

- **Cramer.py**: Resuelve tres sistemas lineales de 3x3 usando la regla de Cramer, calculando determinantes con NumPy. Imprime las soluciones.
- [click aqui](https://github.com/carlosgwel/Proyecto-programaci-n-num-rica/blob/main/Cramer%20(1).py) 

- **Jacobi, Gauss-Seidel.py**: Resuelve un sistema lineal de 3x3 usando los métodos iterativos de Jacobi y Gauss-Seidel con 3 iteraciones cada uno. Imprime los resultados por iteración.

- **Lu.py** : Implementa el análisis LU de una matriz 3x3 ( A1 = [[4, -2, 1], [-2, 4, -2], [1, -2, 4]] ) . Descompone la matriz en un triangular inferior ( L , con 1s en la diagonal) y un triangular superior ( U ) tal que A = LU . Imprime las matrices L y U .

- **Cholseky.py**: Realiza la revisión de Cholesky de una matriz 3x3 simétrica y  positiva de una matriz. Devuelve la matriz triangular inferior L tal que A = LL^T 
### 3. Interpolación

- **interpolacion cuadratica.py**: Implementa interpolación usando el método de diferencias divididas de Newton para los puntos (`x = [1, 2, 3, 5, 7]`, `y = [3, 6, 19, 99, 291]`). Evalúa en `x = 4` y grafica la curva con Matplotlib.  

- **interpolacion de newton.py**:interpolación cuadrática para los puntos ( x = [2, 3, 5] , y = [6, 19, 99] ), calcula el valor estimado de f(4) usando el método de diferencias divididas y gráfica los puntos

- **estimacion lineal.py**: Realiza interpolación cuadrática para los puntos (`x = [2, 3, 5]`, `y = [6, 19, 99]`), evalúa en `x = 4` y grafica la curva con Matplotlib.
  
### 4. Búsqueda de Raíces

- **metodo birge vieta.py**: Usa el método de Newton-Raphson (asociado a Birge-Vieta) para encontrar una raíz del polinomio `f(x) = x^3 - 2x^2 - 5x + 6` desde `x0 = 0.8`. Realiza 5 iteraciones y grafica la raíz.  

- **metodo falsa posicion.py**: Aplica el método de la falsa posición para encontrar una raíz de `f(x) = x - cos(x)` en el intervalo `[0.5, 1.0]`. Realiza 5 iteraciones y grafica la raíz.  

- **Método de Newton-Raphson.py**: Usa el método de Newton-Raphson para encontrar una raíz de `f(x) = 8x*sin(x)*e^(-x) - 1` desde `x = 0.3`. Realiza 5 iteraciones, calcula errores relativos y grafica la raíz.  
 
- **Método de la secante.py**: Aplica el método de la secante para encontrar una raíz de `f(x) = 8x*sin(x)*e^(-x) - 1` con puntos iniciales `x = 0.5` y `x1 = -0.3`. Realiza 5 iteraciones, calcula errores y grafica la raíz.  

- **Método de biseccion.py**: Usa el método de bisección para encontrar una raíz de `f(x) = 2x*cos(2x) - (x + 1)^2` en el intervalo `[-3, -2]`. Realiza 5 iteraciones y grafica la raíz.  

### 5. Integración Numérica

- **Integración numerica.py**: Aplica los métodos de trapecio simple, trapecio múltiple, Simpson 1/3 y Simpson 3/8 para integrar tres funciones (`2*cos(2x)`, `-x^2 - x/2 + 4`, `e^(-x^2)`). Compara resultados con valores analíticos y calcula errores relativos.

### 6. Diferenciación Numérica

- **Diferenciacion numerica.py**: Calcula la derivada numérica de `f(x) = -x^2 - x/2 + 4` en `x = 0` usando diferencias hacia adelante, hacia atrás y centradas con pasos `h = 0.2` y `h = 0.1`. Calcula errores relativos respecto a la derivada analítica.

### 7. Generación de Vectores y Matrices

- **ejercicio 1.py**: Intenta generar un vector aleatorio con un tamaño no entero `n = 3.5`, lo que causa un error. Incluye manejo de errores para entradas inválidas.

- **ejercicio 2.py**: Genera un vector aleatorio de tamaño `n = 5` y crea una matriz `n x n` donde cada columna es el vector multiplicado por el índice de columna. Incluye manejo de errores.

- **ejercicio 3.py**: Solicita al usuario un entero positivo `n`, genera un vector aleatorio y crea una matriz `n x n` con columnas como múltiplos del vector. Incluye manejo de errores.

- **ejercicio 4.py**: Genera un vector aleatorio de tamaño `n = 5` y crea una matriz `n x n` donde cada fila es el vector multiplicado por el índice de fila. Incluye manejo de errores.

- **ejercicio 5.py**: Genera un vector aleatorio de tamaño `n = 4` y crea dos matrices `n x n`: una con filas como múltiplos del vector y otra con columnas como múltiplos.

- **ejercicio 6.py**: Grafica las funciones `sin(x)` y `cos(x)` en el intervalo `[-5, 5]` usando Matplotlib, con etiquetas, leyenda y cuadrícula.  
  [Imagen: Gráfico de sin(x) y cos(x)]
