#### Valores faltantes
Pandas maneja los valores faltantes usando el tipo None y los valores NaN de NumPy. Los valores faltantes son bastante comunes en las actividades de limpieza de datos.

Por ejemplo, si estás realizando una encuesta y un encuestado no respondió una pregunta, el valor faltante es en realidad una omisión. Este tipo de datos faltantes se llama Missing at Random (MAR) (Faltante al Azar) si hay otras variables que podrían usarse para predecir la variable que falta. En mi trabajo, cuando realizo encuestas, a menudo encuentro que los datos faltantes, como el interés en participar en un estudio de seguimiento, a menudo tienen alguna correlación con otro campo de datos, como el género o la etnia. Si no hay relación con otras variables, entonces llamamos a estos datos Missing Completely at Random (MCAR) (Faltante Completamente al Azar).


```python
import pandas as pd
```


```python
# pandas es muy bueno detectando datos faltantes. A pesar de que los datos faltantes a menudo
# se formatean como NAN, NULL, None or N/A, aveces los datos no estan marcados tan claramente. 

# la función de pandas read_csv() tiene un parámetro llamado na_values que nos permite especificar
# el formato de los valores faltantes
dataframe = pd.read_csv("datasets/class_grades.csv")
dataframe.head()
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
      <th>Prefix</th>
      <th>Assignment</th>
      <th>Tutorial</th>
      <th>Midterm</th>
      <th>TakeHome</th>
      <th>Final</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>57.14</td>
      <td>34.09</td>
      <td>64.38</td>
      <td>51.48</td>
      <td>52.50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8</td>
      <td>95.05</td>
      <td>105.49</td>
      <td>67.50</td>
      <td>99.07</td>
      <td>68.33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
      <td>83.70</td>
      <td>83.17</td>
      <td>NaN</td>
      <td>63.15</td>
      <td>48.89</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>49.38</td>
      <td>105.93</td>
      <td>80.56</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8</td>
      <td>91.32</td>
      <td>93.64</td>
      <td>95.00</td>
      <td>107.41</td>
      <td>73.89</td>
    </tr>
  </tbody>
</table>
</div>




```python
# podemos pasarle la función isnull() para crear una mascara booleana de todo el dataframe
# esto propaga la función isnull a todos los elementos del dataframe
mascara = dataframe.isnull()
mascara.head()
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
      <th>Prefix</th>
      <th>Assignment</th>
      <th>Tutorial</th>
      <th>Midterm</th>
      <th>TakeHome</th>
      <th>Final</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
# otra operación que podemos realizar es dropear (eliminar) las filas que contengan algun
# valor faltante, para esto utilizamos dropna()
dataframe.dropna().head()
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
      <th>Prefix</th>
      <th>Assignment</th>
      <th>Tutorial</th>
      <th>Midterm</th>
      <th>TakeHome</th>
      <th>Final</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>57.14</td>
      <td>34.09</td>
      <td>64.38</td>
      <td>51.48</td>
      <td>52.50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8</td>
      <td>95.05</td>
      <td>105.49</td>
      <td>67.50</td>
      <td>99.07</td>
      <td>68.33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8</td>
      <td>91.32</td>
      <td>93.64</td>
      <td>95.00</td>
      <td>107.41</td>
      <td>73.89</td>
    </tr>
    <tr>
      <th>5</th>
      <td>7</td>
      <td>95.00</td>
      <td>92.58</td>
      <td>93.12</td>
      <td>97.78</td>
      <td>68.06</td>
    </tr>
    <tr>
      <th>6</th>
      <td>8</td>
      <td>95.05</td>
      <td>102.99</td>
      <td>56.25</td>
      <td>99.07</td>
      <td>50.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
# podemos cambiar todos los valores faltantes por un valor concreto utilizando la función
# fillna(). Esta función toma un número de parametros, podemos pasarle un solo valor para 
# cambiar todos los datos faltantes a un valor.

# por ejemplo podemos querer rellenar todos los datos faltantes con un 0. Con inplace=True
# aplicamos los cambios sobre el dataframe en lugar de generar una copia
dataframe.fillna(0, inplace=True)
```


```python
# también podemos usar la opción na_filter, para desactivar el filtrado de espacios en blanco
# en grandes dataframes pasar na_filter=False, puede mejorar el rendimiento de lectura

# a veces es util considerar los valores faltantes como información efectiva, en el siguien 
# dataframe por ejemplo NaN se utiliza para representar que no hay cambios desde el registro 
# anterior
dataframe = pd.read_csv("datasets/log.csv")
dataframe.head()
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
      <th>time</th>
      <th>user</th>
      <th>video</th>
      <th>playback position</th>
      <th>paused</th>
      <th>volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1469974424</td>
      <td>cheryl</td>
      <td>intro.html</td>
      <td>5</td>
      <td>False</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1469974454</td>
      <td>cheryl</td>
      <td>intro.html</td>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1469974544</td>
      <td>cheryl</td>
      <td>intro.html</td>
      <td>9</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1469974574</td>
      <td>cheryl</td>
      <td>intro.html</td>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1469977514</td>
      <td>bob</td>
      <td>intro.html</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# en pandas podemos ordenar por index o por valor, vamos a promocionar los timestamps a 
# indices y entonces ordenaremos por indices
dataframe = dataframe.set_index("time")
dataframe = dataframe.sort_index()
dataframe.head()
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
      <th>user</th>
      <th>video</th>
      <th>playback position</th>
      <th>paused</th>
      <th>volume</th>
    </tr>
    <tr>
      <th>time</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1469974424</th>
      <td>cheryl</td>
      <td>intro.html</td>
      <td>5</td>
      <td>False</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1469974424</th>
      <td>sue</td>
      <td>advanced.html</td>
      <td>23</td>
      <td>False</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1469974454</th>
      <td>cheryl</td>
      <td>intro.html</td>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1469974454</th>
      <td>sue</td>
      <td>advanced.html</td>
      <td>24</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1469974484</th>
      <td>cheryl</td>
      <td>intro.html</td>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# podemos ver que el indice en este caso no es unico, es decir, dos usuarios pueden tener el
# mismo timestamp. 

# para obtener una visión más clara de los datos podemos usar indices multinivel con time y
# user, promocionando user a un indice de segundo nivel
dataframe = dataframe.reset_index()
dataframe = dataframe.set_index(["time", "user"])
dataframe.head()
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
      <th></th>
      <th>video</th>
      <th>playback position</th>
      <th>paused</th>
      <th>volume</th>
    </tr>
    <tr>
      <th>time</th>
      <th>user</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1469974424</th>
      <th>cheryl</th>
      <td>intro.html</td>
      <td>5</td>
      <td>False</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>sue</th>
      <td>advanced.html</td>
      <td>23</td>
      <td>False</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1469974454</th>
      <th>cheryl</th>
      <td>intro.html</td>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>sue</th>
      <td>advanced.html</td>
      <td>24</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1469974484</th>
      <th>cheryl</th>
      <td>intro.html</td>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ahora que tenemos los datos indexados y ordenados correctamente, podemos rellenar los datas
# faltantes utilizando ffill.
dataframe = dataframe.ffill()
dataframe.head()
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
      <th></th>
      <th>video</th>
      <th>playback position</th>
      <th>paused</th>
      <th>volume</th>
    </tr>
    <tr>
      <th>time</th>
      <th>user</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1469974424</th>
      <th>cheryl</th>
      <td>intro.html</td>
      <td>5</td>
      <td>False</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>sue</th>
      <td>advanced.html</td>
      <td>23</td>
      <td>False</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1469974454</th>
      <th>cheryl</th>
      <td>intro.html</td>
      <td>6</td>
      <td>False</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>sue</th>
      <td>advanced.html</td>
      <td>24</td>
      <td>False</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1469974484</th>
      <th>cheryl</th>
      <td>intro.html</td>
      <td>7</td>
      <td>False</td>
      <td>10.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# también podemos personalizar con que rellenamos los datos faltantes, utilizando la función
# replace(). Nos permite el reemplazo con varios enfoques: valor por valor, lists, diccionarios y
# regex...

dataframe = pd.DataFrame({'A': [1, 1, 2, 3, 4],
                   'B': [3, 6, 3, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']})
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3</td>
      <td>a</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>6</td>
      <td>b</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>c</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>8</td>
      <td>d</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>9</td>
      <td>e</td>
    </tr>
  </tbody>
</table>
</div>




```python
# reemplazar valor por valor
dataframe.replace(1, 100)
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100</td>
      <td>3</td>
      <td>a</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100</td>
      <td>6</td>
      <td>b</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>c</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>8</td>
      <td>d</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>9</td>
      <td>e</td>
    </tr>
  </tbody>
</table>
</div>




```python
# cambiar dos valores a la vez. 1 por 100 y 2 por 200
dataframe.replace([1, 2], [100, 200])
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100</td>
      <td>3</td>
      <td>a</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100</td>
      <td>6</td>
      <td>b</td>
    </tr>
    <tr>
      <th>2</th>
      <td>200</td>
      <td>3</td>
      <td>c</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>8</td>
      <td>d</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>9</td>
      <td>e</td>
    </tr>
  </tbody>
</table>
</div>




```python
# para reemplazar valores usando regex, pasamos el patron regex como primer parámetro
# el segundo parámetro será el valor por el que vamos a sustituir cuando coincidan y el 
# tercero "regex=True"
dataframe = pd.read_csv("../datasets/log.csv")

dataframe.replace(to_replace=".*.html$", value="página web", regex=True, inplace=True)
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
      <th>time</th>
      <th>user</th>
      <th>video</th>
      <th>playback position</th>
      <th>paused</th>
      <th>volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1469974424</td>
      <td>cheryl</td>
      <td>página web</td>
      <td>5</td>
      <td>False</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1469974454</td>
      <td>cheryl</td>
      <td>página web</td>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1469974544</td>
      <td>cheryl</td>
      <td>página web</td>
      <td>9</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1469974574</td>
      <td>cheryl</td>
      <td>página web</td>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1469977514</td>
      <td>bob</td>
      <td>página web</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1469977544</td>
      <td>bob</td>
      <td>página web</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1469977574</td>
      <td>bob</td>
      <td>página web</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1469977604</td>
      <td>bob</td>
      <td>página web</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1469974604</td>
      <td>cheryl</td>
      <td>página web</td>
      <td>11</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1469974694</td>
      <td>cheryl</td>
      <td>página web</td>
      <td>14</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1469974724</td>
      <td>cheryl</td>
      <td>página web</td>
      <td>15</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1469974454</td>
      <td>sue</td>
      <td>página web</td>
      <td>24</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1469974524</td>
      <td>sue</td>
      <td>página web</td>
      <td>25</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1469974424</td>
      <td>sue</td>
      <td>página web</td>
      <td>23</td>
      <td>False</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1469974554</td>
      <td>sue</td>
      <td>página web</td>
      <td>26</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1469974624</td>
      <td>sue</td>
      <td>página web</td>
      <td>27</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1469974654</td>
      <td>sue</td>
      <td>página web</td>
      <td>28</td>
      <td>NaN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1469974724</td>
      <td>sue</td>
      <td>página web</td>
      <td>29</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1469974484</td>
      <td>cheryl</td>
      <td>página web</td>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1469974514</td>
      <td>cheryl</td>
      <td>página web</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>1469974754</td>
      <td>sue</td>
      <td>página web</td>
      <td>30</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1469974824</td>
      <td>sue</td>
      <td>página web</td>
      <td>31</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1469974854</td>
      <td>sue</td>
      <td>página web</td>
      <td>32</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23</th>
      <td>1469974924</td>
      <td>sue</td>
      <td>página web</td>
      <td>33</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1469977424</td>
      <td>bob</td>
      <td>página web</td>
      <td>1</td>
      <td>True</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1469977454</td>
      <td>bob</td>
      <td>página web</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>26</th>
      <td>1469977484</td>
      <td>bob</td>
      <td>página web</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>1469977634</td>
      <td>bob</td>
      <td>página web</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>1469977664</td>
      <td>bob</td>
      <td>página web</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29</th>
      <td>1469974634</td>
      <td>cheryl</td>
      <td>página web</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>30</th>
      <td>1469974664</td>
      <td>cheryl</td>
      <td>página web</td>
      <td>13</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>31</th>
      <td>1469977694</td>
      <td>bob</td>
      <td>página web</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>32</th>
      <td>1469977724</td>
      <td>bob</td>
      <td>página web</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>


