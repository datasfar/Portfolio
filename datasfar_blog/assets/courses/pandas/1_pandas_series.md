#### Pandas Series
Proporciona estructuras de datos fáciles de usar y herramientas de análisis de datos de alto rendimiento. Las dos estructuras de datos principales que ofrece son las series y los dataframes.


```python
import pandas as pd
```

##### Series
Son una estructura unidimensional que puede almacenar datos de cualquier tipo (enteros, cadenas, números flotantes, objetos de Python, etc.). Es similar a un array unidimensional pero con etiquetas en el eje.



```python
# se crea una lista llamada estudiantes que contiene tres nombres como cadenas de texto.
# el tipo de datos de la Serie (dtype) es string porque todos los elementos son cadenas de texto.
estudiantes = ["Pedro", "Alicia", "Marcos"]
print(pd.Series(estudiantes)) #dtype string

# se define una lista llamada numeros que contiene tres enteros. El tipo de datos de la Serie 
# (dtype) es int64 porque todos los elementos son enteros.
numeros = [1,2,3]
print(pd.Series(numeros)) #dtype int64

# se crea una lista llamada nuevos_estudiantes que contiene dos cadenas de texto y un valor None.
# El tipo de datos de la Serie (dtype) es object porque contiene tanto cadenas de texto como un 
# valor None. En pandas, object es un tipo de datos general que se utiliza cuando la Serie contiene 
# datos heterogéneos.
nuevos_estudiantes = ["Jhon", "Josh", None]
print(pd.Series(nuevos_estudiantes)) #dtype object

# cuando tenemos datos faltantes (None) pandas los transforma en NaN, que es representado como
# un dato de tipo float, por lo que cambiara el type de la serie entera a float.                      
nuevos_numeros = [1,2, None] # None pasa a ser NaN (Not a Number)
print(pd.Series(nuevos_numeros)) # dtype float64 
```

    0     Pedro
    1    Alicia
    2    Marcos
    dtype: object
    0    1
    1    2
    2    3
    dtype: int64
    0    Jhon
    1    Josh
    2    None
    dtype: object
    0    1.0
    1    2.0
    2    NaN
    dtype: float64
    


```python
# es importante destacar que aunque en ciencia de datos None y NaN se utilizan para representar 
# datos faltantes, ambos valores no son equivalentes

import numpy as np

print(np.nan == None)
print(np.isnan(np.nan))
```

    False
    True
    


```python
# cuando creas una Serie a partir de un diccionario, las claves del diccionario se convierten 
# automáticamente en los índices de la Serie.
estudiantes = {
    "Alicia":"Geología",
    "Martin":"Biología",
    "Marc":"Informática",
    "Paola":"Física"
}

mi_serie = pd.Series(estudiantes)
print(mi_serie)
print(mi_serie.index)

# tambien podemos acceder a los elementos usando sus indices
print(mi_serie["Alicia"])

# y modificar los valores de la misma forma
mi_serie["Alicia"] = "Matemáticas"
print(mi_serie["Alicia"])

# pandas también nos permite separar la creación del indice de los datos pasados
mi_nueva_serie = pd.Series(["Geología", "Matemáticas", "Física"], index=["Alicia", "Marc", "Martin"])
print(mi_nueva_serie)

# si creamos una serie a partir de una lista de tuplas los índices se crear 
# como números autoincrementados
estudiantes = [("Alicia", "Swan"), ("Marc", "Hallen"), ("Martin", "Miller")]
print(pd.Series(estudiantes))
```

    Alicia       Geología
    Martin       Biología
    Marc      Informática
    Paola          Física
    dtype: object
    Index(['Alicia', 'Martin', 'Marc', 'Paola'], dtype='object')
    Geología
    Matemáticas
    Alicia       Geología
    Marc      Matemáticas
    Martin         Física
    dtype: object
    0      (Alicia, Swan)
    1      (Marc, Hallen)
    2    (Martin, Miller)
    dtype: object
    


```python
# ¿qué pasaría en caso de que al crear una serie los datos no esten alineados?
# es decir, tenemos índices o valores que no se corresponden
estudiantes = {"Alicia":"Geología",
               "Martin":"Biología",
               "Marc":"Informática",
               "Paola":"Física"}

serie = pd.Series(estudiantes, index=["Alicia", "Martin", "Jan"])
print(serie)

# Jan no esta presente en estudiantes, pero ha sido pasado como índice por lo que aparecerá
# en la serie con un valor asociado NaN, el dtype seguirá siendo object
```

    Alicia    Geología
    Martin    Biología
    Jan            NaN
    dtype: object
    

##### Realizar consultas a Series


```python
# las series de pandas pueden ser accesibles tanto por las etiquetas del index
# como por la posición de su índice. La posición y la etiqueta representan el 
# mismo valor. Para localizar una posición numérica utilizamos el método .iloc[]
# para acceder por clave (key) podemos usar .loc[]
estudiantes = {"Alicia":"Geología",
               "Martin":"Biología",
               "Marc":"Informática",
               "Paola":"Física"}

serie = pd.Series(estudiantes)
print(serie.iloc[2]) # devuelve el valor por indice numérico
print(serie.loc["Marc"]) # devuelve el valor por clave
print(serie.iloc[0:2]) # devuelve una serie con el segmento especificado [)

# pandas nos permite hacerlo más intuitivo obviando el método 
print(serie[2]) # deprecated (se eliminará en futuras versiones de pandas)
print(serie["Alicia"])
```

    Informática
    Informática
    Alicia    Geología
    Martin    Biología
    dtype: object
    Informática
    Geología
    


```python
# pandas nos permite realizar multitud de operaciones con las series
notas = pd.Series([7, 8, 6, 9, 4])

media = np.sum(notas) / len(notas) # podemos usar sum() y len() para obtener la media
print(media)
```

    6.8
    


```python
# podemos unir dos series con append()
notas_clase_a = pd.Series([7, 8, 6, 9, 4])
notas_clase_b = pd.Series([2, 9, 0, 0, 7])

notas_completas = np.append(notas_clase_a, notas_clase_b)
print(notas_completas)
```

    [7 8 6 9 4 2 9 0 0 7]
    

##### Prueba de eficiencia


```python
# ahora vamos a realizar una prueba de eficiencia para comparar el funcionamiento 
# normal, con la vectorización (cálculos realizados sobre series)

# primero creamos una serie con 10.000 valores
numeros = pd.Series(np.random.randint(0, 10000, 100000))
print(len(numeros))
```

    100000
    


```python
%%timeit -n 100 
# %%timeit -> magic command que indica que se va a medir el tiempo de ejecución del código en la celda
# -n 100 -> indica el número de veces que se debe ejecutar el bloque

total = 0
for numero in numeros:
    total  += numero

total/len(numeros) 

# Salida -> 18.3 ms ± 1.12 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

    9.31 ms ± 118 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    


```python
%%timeit -n 100
total = np.sum(numeros)
total/len(numeros)

# Salida -> The slowest run took 9.29 times longer than the fastest. This could mean that an 
# intermediate result is being cached. 146 µs ± 178 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

    101 µs ± 2.57 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    

##### Propagación (Broadcasting)
El broadcasting nos permite aplicar una operación a cada valor de una serie, modificando la serie.


```python
# por ejemplo podemos añadir 2 a cada número dentro de la serie
print(numeros[0:5])
numeros+=2
print(numeros[0:5])
```

    0    3072
    1    6658
    2    1062
    3    6630
    4    6903
    dtype: int32
    0    3074
    1    6660
    2    1064
    3    6632
    4    6905
    dtype: int32
    


```python
# tambien podemos iterar atraves de todos los items utilizando la función
# .items() que devuelve la etiqueta y el valor y .at[] como selector

for label, value in numeros.items():
    numeros.at[label] = value + 2

print(numeros[0:5])

# como vimos anteriormente esta forma es mucho menos eficiente 
```

    0    3076
    1    6662
    2    1066
    3    6634
    4    6907
    dtype: int32
    

##### Índices con tipos mixtos


```python
# pandas puede trabajar con diferentes tipos de datos para los índices de una misma
# serie. Pandas cambiará automaticamente el tipo de dato de numpy que usa por debajo
# al tipo de dato más apropiado
serie = pd.Series([1,2,3])
print(serie)

serie.loc[3.9] = 100 # al no existir el valor, pandas crea el nuevo registro
print(serie)
```

    0    1
    1    2
    2    3
    dtype: int64
    0.0      1
    1.0      2
    2.0      3
    3.9    100
    dtype: int64
    

##### Consideraciones
    1.- Inmutabilidad de las Series Originales: muchos métodos en pandas que, por defecto, no modifican los objetos originales sino que devuelven nuevos objetos.

    2.- Indices No Únicos: una característica interesante y poderosa de pandas es que permite índices no únicos
