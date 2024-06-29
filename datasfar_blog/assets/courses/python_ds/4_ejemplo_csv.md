# Cargar datos de un archivo CSV

---

## Índice: 

1. [Leer el archivo CSV](#leer)
2. [Obtener medias de los datos](#media)
3. [Obtener datos únicos](#unicos)
4. [Crear conjuntos de datos relacionados](#relaciones)

---

<a id="leer"></a>

## Leer el archivo CSV
Leer y escribir documentos csv. El dataset utilizado contiene información de sobre coches.


```python
import csv 

# cargamos el documento
with open("../datasets/mpg.csv") as csvfile:
    mpg =  list(csv.DictReader(csvfile))

print(mpg[0]) # ejemplo de registro
print(len(mpg)) # nº de registros
print(mpg[0].keys()) # keys del registro
```

    {'': '1', 'manufacturer': 'audi', 'model': 'a4', 'displ': '1.8', 'year': '1999', 'cyl': '4', 'trans': 'auto(l5)', 'drv': 'f', 'cty': '18', 'hwy': '29', 'fl': 'p', 'class': 'compact'}
    234
    dict_keys(['', 'manufacturer', 'model', 'displ', 'year', 'cyl', 'trans', 'drv', 'cty', 'hwy', 'fl', 'class'])
    

<a id="media"></a>

## Obtener la media
Supongamos que queremos saber el consumo medio de todos los coches en nuestro dataset. Se muestra en millas / galón (cosas de los americanos).


```python
# [float(d['cty']) for d in mpg] itera sobre cada diccionario en la lista mpg, extrae el valor de 'cty' y lo convierte en float
# sum() realiza un sumatorio de todos los valores anteriores
# lo dividimos por len(mpg), nº de valores, para obtener la media

consumo_medio = sum(float(d['cty']) for d in mpg) / len(mpg)
print(consumo_medio)
```

    16.858974358974358
    

<a id="unicos"></a>

## Valores únicos 
Podemos crear sets con todos los valores de un registro para obtener valores unicos.


```python
# así podemos ver las diferentes opciones de un registro concreto
cilindros = set(d["cyl"] for d in mpg)
print(cilindros)
```

    {'6', '8', '4', '5'}
    

<a id="relaciones"></a>

## Crear conjuntos relacionados
Ahora vamos a generar una nueva lista que contendra el número de cilindros y el consumo medio correspondiente.


```python
consumo_cilindros = []

for c in cilindros: # iteramos sobre cilindros
    summpg = 0
    contador = 0

    for d in mpg: # iteramos sobre todos los registros
        if d["cyl"] == c: # cuando el el cilindor en registro coincide con cilindros
            summpg += float(d["cty"]) # suma el consumo a una variable
            contador += 1 # cuenta cuantas veces se suma
    
    consumo_cilindros.append((c, summpg / contador)) # se hace la media y se guarda el registro

consumo_cilindros.sort(key=lambda x: x[0]) # se ordena con una función lambda
print(consumo_cilindros)
```

    [('4', 21.012345679012345), ('5', 20.5), ('6', 16.21518987341772), ('8', 12.571428571428571)]
    
