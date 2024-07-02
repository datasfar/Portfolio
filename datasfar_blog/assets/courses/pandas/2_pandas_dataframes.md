#### Pandas dataframes
Son una estructura bidimensional (similar a una tabla en una base de datos o una hoja de cálculo de Excel) que puede almacenar datos de diferentes tipos en cada columna. Tiene etiquetas en los ejes de filas y columnas, lo que permite una fácil manipulación y acceso a los datos.


```python
import pandas as pd

registro_uno = pd.Series({"Nombre":"Alicia", "Clase":"Física", "Nota":100})
registro_dos = pd.Series({"Nombre":"Marc", "Clase":"Matemáticas", "Nota":90})
registro_tres = pd.Series({"Nombre":"Martin", "Clase":"Literatura", "Nota":80})
```


```python
# podemos crear un dataframe a partir de series
dataframe = pd.DataFrame([registro_uno, registro_dos, registro_tres])
dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Nombre</th>
      <th>Clase</th>
      <th>Nota</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alicia</td>
      <td>Física</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Marc</td>
      <td>Matemáticas</td>
      <td>90</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Martin</td>
      <td>Literatura</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
# como las series, los dataframes son indexables, al crear el dataframe podemos pasarle
# el indice como parametro
df_indexado = pd.DataFrame([registro_uno, registro_dos, registro_tres], 
                           index=["reg 1", "reg 2", "reg 3"])
df_indexado
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Nombre</th>
      <th>Clase</th>
      <th>Nota</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>reg 1</th>
      <td>Alicia</td>
      <td>Física</td>
      <td>100</td>
    </tr>
    <tr>
      <th>reg 2</th>
      <td>Marc</td>
      <td>Matemáticas</td>
      <td>90</td>
    </tr>
    <tr>
      <th>reg 3</th>
      <td>Martin</td>
      <td>Literatura</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
# tambien podemos crear un dataframe a partir de una lista de diccionarios
estudiantes = [{"Nombre":"Alicia", "Clase":"Física", "Nota":100},
               {"Nombre":"Marc", "Clase":"Matemáticas", "Nota":90},
               {"Nombre":"Martin", "Clase":"Literatura", "Nota":80}]

df_estudiantes = pd.DataFrame(estudiantes, index=["reg 1", "reg 2", "reg 3"])
df_estudiantes
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Nombre</th>
      <th>Clase</th>
      <th>Nota</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>reg 1</th>
      <td>Alicia</td>
      <td>Física</td>
      <td>100</td>
    </tr>
    <tr>
      <th>reg 2</th>
      <td>Marc</td>
      <td>Matemáticas</td>
      <td>90</td>
    </tr>
    <tr>
      <th>reg 3</th>
      <td>Martin</td>
      <td>Literatura</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
# al igual que en las series, en los dataframes tambien podemos acceder a los datos
# utilizando los atributos .loc[] y .iloc[]. 

# podemos acceder a los tipos de los datos
print(type(df_estudiantes))
print(type(df_estudiantes.loc["reg 2"]))

# acceder a valores a partir del indice
df_estudiantes.loc["reg 2"]
```

    <class 'pandas.core.frame.DataFrame'>
    <class 'pandas.core.series.Series'>
    




    Nombre           Marc
    Clase     Matemáticas
    Nota               90
    Name: reg 2, dtype: object




```python
# los valores de los indices y los nombres de las columnas pueden no ser unico, por lo 
# que si tenemos más de un valor a ser devuelto, este será un nuevo dataframe
df_estudiantes = pd.DataFrame(estudiantes, index=["reg 1", "reg 2", "reg 1"]) # <- tenemos 2 "reg 1"

print(type(df_estudiantes))
df_estudiantes.loc["reg 1"]
```

    <class 'pandas.core.frame.DataFrame'>
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Nombre</th>
      <th>Clase</th>
      <th>Nota</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>reg 1</th>
      <td>Alicia</td>
      <td>Física</td>
      <td>100</td>
    </tr>
    <tr>
      <th>reg 1</th>
      <td>Martin</td>
      <td>Literatura</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
# loc[] permite pasar dos parametros y nos devolvería una serie de los valores en la columna
# y el indice seleccionado
print(type(df_estudiantes.loc["reg 1", "Nombre"]))
df_estudiantes.loc["reg 1", "Nombre"]
```

    <class 'pandas.core.series.Series'>
    




    reg 1    Alicia
    reg 1    Martin
    Name: Nombre, dtype: object




```python
# para acceder a una columna concreta tenemos varias opciones:

# la primera sería transponer la matriz para cambiar todas las filas por columnas y todas las 
# columnas por filas -> se hace con el atributo T
print(df_estudiantes.T)
print(df_estudiantes.T.loc["Nota"])
```

             reg 1        reg 2       reg 1
    Nombre  Alicia         Marc      Martin
    Clase   Física  Matemáticas  Literatura
    Nota       100           90          80
    reg 1    100
    reg 2     90
    reg 1     80
    Name: Nota, dtype: object
    


```python
# otra forma de acceder a las columnas es la utilización del nombre de la columna
print(type(df_estudiantes["Clase"]))
print(df_estudiantes["Clase"])
```

    <class 'pandas.core.series.Series'>
    reg 1         Física
    reg 2    Matemáticas
    reg 1     Literatura
    Name: Clase, dtype: object
    


```python
# tambien podemos acceder a los valores de una columna encadenando indexado
# debe evitarse siempre que podamos usar otro enfoque dado el alto coste computacional
# dado que devuelve una copia del dataframe en lugar de una vista
print(df_estudiantes.loc["reg 1"]["Nota"])
```

    reg 1    100
    reg 1     80
    Name: Nota, dtype: int64
    


```python
# si queremos seleccionar todas las filas, podemos utilizar las columnas para obtener una 
# porción (slice) desde el principio al final, de forma similar a como lo haciamos en las 
# listas de python

# así podemos seleccionar todos los registros de unas columnas concretas
df_estudiantes.loc[:,["Clase", "Nota"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Clase</th>
      <th>Nota</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>reg 1</th>
      <td>Física</td>
      <td>100</td>
    </tr>
    <tr>
      <th>reg 2</th>
      <td>Matemáticas</td>
      <td>90</td>
    </tr>
    <tr>
      <th>reg 1</th>
      <td>Literatura</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>



##### Eliminar datos (drop)


```python
# para eliminar las filas de un indice concreto podemos utilizar .drop() pasando como
# parametro el indice de las filas a eliminar

# realmente drop no elimina el registro del dataframe original, si no que genera una
# nueva copia del dataframe modificado.

print(df_estudiantes.drop("reg 2"))
print(df_estudiantes)
```

           Nombre       Clase  Nota
    reg 1  Alicia      Física   100
    reg 1  Martin  Literatura    80
           Nombre        Clase  Nota
    reg 1  Alicia       Física   100
    reg 2    Marc  Matemáticas    90
    reg 1  Martin   Literatura    80
    


```python
# con copy() podemos crear una copia de un dataframe
df_copia = df_estudiantes.copy()

# eliminar una columna, con implace=True el cambio se aplica al df en lugar de generar copia
df_copia.drop("Nota", inplace=True, axis=1) # ejes: filas = 0, columnas = 1
print(df_copia)
```

           Nombre        Clase
    reg 1  Alicia       Física
    reg 2    Marc  Matemáticas
    reg 1  Martin   Literatura
    


```python
# hay otra forma de dropear (eliminar) una columna de un dataframe, usando el operador de 
# indexación y la palabra clave del. 

# El cambio se realiza en el dataframe original y no devuelve una vista
del df_copia["Clase"]
print(df_copia)
```

           Nombre
    reg 1  Alicia
    reg 2    Marc
    reg 1  Martin
    

#### Añadir columnas 


```python
# añadir una nueva columna es muy facil, basta con asignar un valor utilizando el operador de
# indexación
df_copia["Ranking"] = None
print(df_copia)
```

           Nombre Ranking
    reg 1  Alicia    None
    reg 2    Marc    None
    reg 1  Martin    None
    
