# Funciones  

---

## Índice: 

1. [Funciones básicas](#funciones-basicas)
2. [Map()](#map)
3. [Funciones Lambda](#funciones-lambda)
4. [Compresión List (List Comprehension) ](#compresion-list)

---

<a id="funciones-basicas"></a>

## Funciones básicas

```python
# Función básica con parametros
def add_number(x, y):
    return x + y

add_number(1,2)
```




    3




```python
# Función con parámetros por defecto
def calcutale(x, y, operation="plus"):

    if operation == "plus":
        return x + y
    elif operation == "minus":
        return x - y
    else:
        return "Operation unknown"
    
print(calcutale(1, 2))
print(calcutale(1, 2, "minus"))
print(calcutale(1, 2, "other operation"))
```

    3
    -1
    Operation unknown
    


```python
# Función con parámetros opcionales
def calcutale(x, y, operation=None):

    if operation:
        return x + y
    else:
        return "Operation unknown"

print(calcutale(2, 3))
print(calcutale(2, 3, "yes"))
```

    Operation unknown
    5
    


```python
# Función con tipado
def operate(x:int, y:int, units:str) -> str:
    return str(x + y) + " " + units

# Función con tipado y f-string
def operate_f(x:int, y:int, units:str) -> str:
    return f"{x + y} {units}"

print(operate(1, 2, "kilograms"))
print(operate_f(1, 2, "kilograms"))
```

    3 kilograms
    3 kilograms
    

<a id="map"></a>

### Map()
Es una función incorporada que se utiliza para aplicar una función a cada ítem de una lista (o cualquier iterable) y devolver un mapa (un objeto que se puede convertir en una lista, tupla, etc.). Permite aplicar una operación a cada elemento de una colección sin tener que usar un bucle explícito.


```python
# ejemplo con una función definida
def multiplicar_por_dos(x):
    return x * 2

m_list =  [1, 2, 3, 4, 5, 6]

mapa = map(multiplicar_por_dos, m_list)
print(list(mapa))
```

    [2, 4, 6, 8, 10, 12]
    


```python
# ejemplo con función lambda
numeros = [1, 2, 3, 4, 5]

resultado = map(lambda x: x * 2, numeros)
print(list(resultado))  
```

    [2, 4, 6, 8, 10]
    


```python
# ejemplo con funciones de python
m_list =  [1, 2, 3, 4, 5, 6]
m_list_dos = [0, 2, 1, 4, 0, 6]

mapa_min = map(min, m_list, m_list_dos) # compara valores y devuelve el más pequeño
print(list(mapa_min))
```

    [0, 2, 1, 4, 0, 6]
    
<a id="funciones-lambda"></a>

### Funciones Lambda
Las funciones lambda se definen en una sola línea y no tienen un nombre explícito, por lo que se les suele llamar "funciones anónimas".          

Forma -> lambda argumentos: expresión


```python
# ejemplo básico 
suma = lambda x, y: x + y
print(suma(3, 5))
```

    8
    

Se utilizan principalmente donde se necesitan funciones de corta duración, por ejemplo, como argumentos a funciones de orden superior como map(), filter(), y sorted().


```python
# ejemplo con map()
numeros = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x**2, numeros)
print(list(cuadrados)) 

# ejemplo con filter()
numeros = [1, 2, 3, 4, 5]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))

# ejemplo con sorted()
puntos = [(1, 2), (3, 1), (5, -1), (2, 3)]
puntos_ordenados = sorted(puntos, key=lambda punto: punto[1]) # ordenar los puntos por la segunda coordenada
print(puntos_ordenados) 
```

    [1, 4, 9, 16, 25]
    [2, 4]
    [(5, -1), (3, 1), (1, 2), (2, 3)]
    
<a id="compresion-list"></a>

### Compresión de listas (List comprehension)
Es una sintaxis concisa para crear listas basadas en secuencias o iterables existentes. Utiliza una sola línea de código para realizar operaciones y filtrar elementos, ofreciendo una forma más compacta y legible de generar listas en comparación con el uso de bucles for tradicionales.

Forma -> [nueva_expr for item in iterable]


```python
# ejemplo sin list comprehension
numeros = [1, 2, 3, 4, 5]
cuadrados = []
for n in numeros:
    cuadrados.append(n ** 2)
print(cuadrados)   
```

    [1, 4, 9, 16, 25]
    


```python
# ejemplo con list comprehension
numeros = [1, 2, 3, 4, 5]
cuadrados = [n ** 2 for n in numeros]
print(cuadrados) 

# ejemplo de list compr. con condicional
numeros = [1, 2, 3, 4, 5]
dobles_pares = [n * 2 for n in numeros if n % 2 == 0]
print(dobles_pares)  

# ejemplo de list comp. con listas anidadas
matriz = [[j for j in range(3)] for i in range(3)]
print(matriz) 
```

    [1, 4, 9, 16, 25]
    [4, 8]
    [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
    
