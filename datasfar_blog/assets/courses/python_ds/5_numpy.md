# Numpy: Libreria numérica de Python

---

## Índice: 

1. [Arrays multidimensionales (ndarray)](#array)
2. [Manipulación de arrays multidimensionales](#manipular)
3. [Acceder a elementos de un array multidimensional](#acceder)

---

Proporciona soporte para arrays y matrices de gran tamaño y multidimensionales, junto con una colección de funciones matemáticas para operar con estos arrays de manera eficiente. NumPy es esencialmente el estándar de facto para el manejo de datos numéricos en Python, y muchas otras bibliotecas científicas y de análisis de datos (como SciPy, Pandas y Matplotlib) están construidas sobre NumPy.


```python
import numpy as np
import math
```
<a id="array"></a>

## Arrays multidemensionales
NumPy introduce el objeto ndarray, que es una matriz N-dimensional con elementos homogéneos. Este objeto es mucho más eficiente en términos de memoria y velocidad que las listas de Python.


```python
# crear un array unidimensional
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# crear un array bidimensional
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# crear un array lleno de ceros
arr3 = np.zeros((2, 3))
print(arr3)

# crear un array con numeros aleatorios
arr_random = np.random.rand(2, 3) # <- forma del array (2, 3)
print(arr_random)

# crear un array con un rango de numeros
arr_rango = np.arange(10, 50, 1) # <- (inicio (incluido), fin (excluido), frecuencia (incremento))
print(arr_rango)

# crear un array con una secuencia de floats
arr_sec = np.linspace(0, 2, 15) # 15 numeros, desde 0 (incluido) hasta el 2 (excluido)
print(arr_sec)
```

    [1 2 3 4 5]
    [[1 2 3]
     [4 5 6]]
    [[0. 0. 0.]
     [0. 0. 0.]]
    [[0.2971926  0.90123087 0.76745256]
     [0.89139524 0.78600581 0.35680347]]
    [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
     34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49]
    [0.         0.14285714 0.28571429 0.42857143 0.57142857 0.71428571
     0.85714286 1.         1.14285714 1.28571429 1.42857143 1.57142857
     1.71428571 1.85714286 2.        ]
    


```python
# ndim -> ver las dimensiones de un array
print(arr1.ndim)
print(arr2.ndim)

# shape -> ver la forma (longitud de cada dimension)
print(arr1.shape)
print(arr2.shape)

# dtype -> ver tipo de datos de un ndarray
print(arr1.dtype)
print(arr_sec.dtype)
```

    1
    2
    (5,)
    (2, 3)
    int32
    float64
    

<a id="manipular"></a>

## Manipular ndarrays


```python
# array con temperaturas x día en farenheit
farenheit = np.array([0, -15, -5, -15, 0])

# formula farenheit a celsius -> ((ºF - 32) * 5/9 = ºC)
celsius = (farenheit - 32) * (5/9)
print(celsius)

# podemos convertirlo en un array que nos diga que días hará más de x grados
buen_clima = celsius > - 20
print(buen_clima)
```

    [-17.77777778 -26.11111111 -20.55555556 -26.11111111 -17.77777778]
    [ True False False False  True]
    


```python
# usando el mismo sistema podriamos ver que numeros en un array son pares
array = np.arange(0, 21, 3)
es_par = array %2 == 0
print(array)
print(es_par)
```

    [ 0  3  6  9 12 15 18]
    [ True False  True False  True False  True]
    

Además de manipular los valores del array uno por uno, numpy tambien nos permite manipular las matices y realizar operaciones con ellas.


```python
a = np.array([[1,1],[0,1]])
b = np.array([[2,0],[3,4]])

# multiplicación elemento por elemento
# (1 * 2) = 2
# (1 * 0) = 0
# (0 * 3) = 0
# (1 * 4) = 4
print(a*b)

# multiplicación maticial 
# el elemento en la posición (0, 0) es 1*2 + 1*3 = 5
# el elemento en la posición (0, 1) es 1*0 + 1*4 = 4
# el elemento en la posición (1, 0) es 0*2 + 1*3 = 3
# el elemento en la posición (1, 1) es 0*0 + 1*4 = 4
print(a@b)

```

    [[2 0]
     [0 4]]
    [[5 4]
     [3 4]]
    

NumPy tiene agregadas algunas funciones muy interesantes como: 


```python
array = np.array([-12, 2.3, -1, 2, 21, -4, 7, 23, 14, 51])

# sum() -> sumatorio de los elementos de un array
print(array.sum())

# max() -> elemento más grande o máximo
print(array.max())

# min() -> elemento más pequeño o mínimo
print(array.min())

# mean() -> media de los elementos
print(array.mean())
```

    103.3
    51.0
    -12.0
    10.33
    


```python
# en los arrays de ndimensiones podemos hacer lo mismo para filas o columnas
array = np.arange(1, 16, 1).reshape(3,5)
print(array)

print(array.sum(axis=0)) # sumar columnas
print(array.sum(axis=1)) # sumar filas

print(array.max(axis=0)) # maximo columnas
print(array.max(axis=1)) # maximo filas

print(array.min(axis=0)) # minimo columnas
print(array.min(axis=1)) # minimo filas

print(array.mean(axis=0)) # media columnas
print(array.mean(axis=1)) # media filas
```

    [[ 1  2  3  4  5]
     [ 6  7  8  9 10]
     [11 12 13 14 15]]
    [18 21 24 27 30]
    [15 40 65]
    [11 12 13 14 15]
    [ 5 10 15]
    [1 2 3 4 5]
    [ 1  6 11]
    [ 6.  7.  8.  9. 10.]
    [ 3.  8. 13.]
    

<a id="acceder"></a>

## Acceder a elementos de un array por índice


```python
array = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# acceder al elemento en la fila 0, columna 1 (segunda columna)
elemento = array[0, 1]
print("Elemento en la posición (0, 1):", elemento) 

# acceder a la segunda (1) fila completa
fila_completa = array[1, :]
print("Segunda fila completa:", fila_completa)  # Salida: [4 5 6]

# acceder a la primera (0) columna completa
columna_completa = array[:, 0]
print("Primera columna completa:", columna_completa)

# acceder a filas y columnas a la vez
array_dos = array[:2, 1:3] 
# [:2]: filas desde el inicio hasta antes del índice 2 (es decir, las filas 0 y 1).
# [1:3]: columnas desde el índice 1 hasta antes del índice 3 (es decir, las columnas 1 y 2).
print("Slices de filas [0:2] y columnas [1:3]:", array_dos)

# indexación por listas
indices_filas = [0, 2]
indices_columnas = [1, 2]
elementos_seleccionados = array[indices_filas, indices_columnas]
print("Elementos seleccionados:", elementos_seleccionados) 

# indexación booleana elemento a elemento
print(array>4) # develve un array (de True/False) con las misma forma 
print(array[array>4]) # devuelve los valores que cumplen la condición
```

    Elemento en la posición (0, 1): 2
    Segunda fila completa: [4 5 6]
    Primera columna completa: [1 4 7]
    Slices de filas [0:2] y columnas [1:3]: [[2 3]
     [5 6]]
    Elementos seleccionados: [2 9]
    [[False False False]
     [False  True  True]
     [ True  True  True]]
    [5 6 7 8 9]
    
