#### Consultas a un dataframe

El primer paso para entender las consultas de dataframe, es entender el proceso de enmascaramiento booleano. Este es la base de la eficiencia tanto en Pandas como en Numpy. Y es analogo al enmascaramiento de bits que se utiliza en otras areas de la informática.

El enmascaramiento booleano en pandas es una técnica que permite filtrar datos de un DataFrame o Serie utilizando condiciones lógicas. Se basa en la creación de una Serie de valores booleanos (True o False), que se utiliza para seleccionar únicamente las filas o columnas que cumplen con una condición específica.


```python
import pandas as pd

dataframe = pd. read_csv("datasets/Admission_Predict.csv", index_col=0)
dataframe.columns = [x.lower().strip() for x in dataframe.columns]
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
      <th>gre score</th>
      <th>toefl score</th>
      <th>university rating</th>
      <th>sop</th>
      <th>lor</th>
      <th>cgpa</th>
      <th>research</th>
      <th>chance of admit</th>
    </tr>
    <tr>
      <th>Serial No.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>337</td>
      <td>118</td>
      <td>4</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.65</td>
      <td>1</td>
      <td>0.92</td>
    </tr>
    <tr>
      <th>2</th>
      <td>324</td>
      <td>107</td>
      <td>4</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>8.87</td>
      <td>1</td>
      <td>0.76</td>
    </tr>
    <tr>
      <th>3</th>
      <td>316</td>
      <td>104</td>
      <td>3</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>8.00</td>
      <td>1</td>
      <td>0.72</td>
    </tr>
    <tr>
      <th>4</th>
      <td>322</td>
      <td>110</td>
      <td>3</td>
      <td>3.5</td>
      <td>2.5</td>
      <td>8.67</td>
      <td>1</td>
      <td>0.80</td>
    </tr>
    <tr>
      <th>5</th>
      <td>314</td>
      <td>103</td>
      <td>2</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>8.21</td>
      <td>0</td>
      <td>0.65</td>
    </tr>
  </tbody>
</table>
</div>




```python
# las mascaras booleanas se crean aplicando operadores directamente al dataframe

# por ejemplo en nuestra dataframe podriamos mostrar solamente los estudiantes con mas de un 
# 0.7 de  probabilidad de ser admitidos
admision_bm = dataframe["chance of admit"] > 0.7
admision_bm
```




    Serial No.
    1       True
    2       True
    3       True
    4       True
    5      False
           ...  
    396     True
    397     True
    398     True
    399    False
    400     True
    Name: chance of admit, Length: 400, dtype: bool




```python
# ahora podemos aplicar la mascara al dataframe para mostrar los valores que han sido marcados
# como True y ocultar los False. Para esto usamos el método where()
dataframe.where(admision_bm)
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
      <th>gre score</th>
      <th>toefl score</th>
      <th>university rating</th>
      <th>sop</th>
      <th>lor</th>
      <th>cgpa</th>
      <th>research</th>
      <th>chance of admit</th>
    </tr>
    <tr>
      <th>Serial No.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>337</td>
      <td>118</td>
      <td>4</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.65</td>
      <td>1</td>
      <td>0.92</td>
    </tr>
    <tr>
      <th>2</th>
      <td>324</td>
      <td>107</td>
      <td>4</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>8.87</td>
      <td>1</td>
      <td>0.76</td>
    </tr>
    <tr>
      <th>3</th>
      <td>316</td>
      <td>104</td>
      <td>3</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>8.00</td>
      <td>1</td>
      <td>0.72</td>
    </tr>
    <tr>
      <th>4</th>
      <td>322</td>
      <td>110</td>
      <td>3</td>
      <td>3.5</td>
      <td>2.5</td>
      <td>8.67</td>
      <td>1</td>
      <td>0.80</td>
    </tr>
    <tr>
      <th>5</th>
      <td>314</td>
      <td>103</td>
      <td>2</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>8.21</td>
      <td>0</td>
      <td>0.65</td>
    </tr>
  </tbody>
</table>
</div>




```python
# podemos ver que solo los valores que cumplen la condición son mostrados, mientras que 
# los que no la cumplen han sido sustituidos por NaN

# ahora podemos utilizar la función dropna() para eliminar los valores NaN
dataframe.where(admision_bm).dropna().head()
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
      <th>gre score</th>
      <th>toefl score</th>
      <th>university rating</th>
      <th>sop</th>
      <th>lor</th>
      <th>cgpa</th>
      <th>research</th>
      <th>chance of admit</th>
    </tr>
    <tr>
      <th>Serial No.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>337.0</td>
      <td>118.0</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.65</td>
      <td>1.0</td>
      <td>0.92</td>
    </tr>
    <tr>
      <th>2</th>
      <td>324.0</td>
      <td>107.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>8.87</td>
      <td>1.0</td>
      <td>0.76</td>
    </tr>
    <tr>
      <th>3</th>
      <td>316.0</td>
      <td>104.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>8.00</td>
      <td>1.0</td>
      <td>0.72</td>
    </tr>
    <tr>
      <th>4</th>
      <td>322.0</td>
      <td>110.0</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>2.5</td>
      <td>8.67</td>
      <td>1.0</td>
      <td>0.80</td>
    </tr>
    <tr>
      <th>6</th>
      <td>330.0</td>
      <td>115.0</td>
      <td>5.0</td>
      <td>4.5</td>
      <td>3.0</td>
      <td>9.34</td>
      <td>1.0</td>
      <td>0.90</td>
    </tr>
  </tbody>
</table>
</div>




```python
# podemos obtener el mismo resultado de manera más simple
dataframe[dataframe["chance of admit"] > 0.7].head()
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
      <th>gre score</th>
      <th>toefl score</th>
      <th>university rating</th>
      <th>sop</th>
      <th>lor</th>
      <th>cgpa</th>
      <th>research</th>
      <th>chance of admit</th>
    </tr>
    <tr>
      <th>Serial No.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>337</td>
      <td>118</td>
      <td>4</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.65</td>
      <td>1</td>
      <td>0.92</td>
    </tr>
    <tr>
      <th>2</th>
      <td>324</td>
      <td>107</td>
      <td>4</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>8.87</td>
      <td>1</td>
      <td>0.76</td>
    </tr>
    <tr>
      <th>3</th>
      <td>316</td>
      <td>104</td>
      <td>3</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>8.00</td>
      <td>1</td>
      <td>0.72</td>
    </tr>
    <tr>
      <th>4</th>
      <td>322</td>
      <td>110</td>
      <td>3</td>
      <td>3.5</td>
      <td>2.5</td>
      <td>8.67</td>
      <td>1</td>
      <td>0.80</td>
    </tr>
    <tr>
      <th>6</th>
      <td>330</td>
      <td>115</td>
      <td>5</td>
      <td>4.5</td>
      <td>3.0</td>
      <td>9.34</td>
      <td>1</td>
      <td>0.90</td>
    </tr>
  </tbody>
</table>
</div>




```python
# tambien podemos combinar multiples mascaras booleanas, al igual que multiples criterios
dataframe[(dataframe["chance of admit"] > 0.7) & (dataframe["chance of admit"] < 0.9)].head()
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
      <th>gre score</th>
      <th>toefl score</th>
      <th>university rating</th>
      <th>sop</th>
      <th>lor</th>
      <th>cgpa</th>
      <th>research</th>
      <th>chance of admit</th>
    </tr>
    <tr>
      <th>Serial No.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>324</td>
      <td>107</td>
      <td>4</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>8.87</td>
      <td>1</td>
      <td>0.76</td>
    </tr>
    <tr>
      <th>3</th>
      <td>316</td>
      <td>104</td>
      <td>3</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>8.00</td>
      <td>1</td>
      <td>0.72</td>
    </tr>
    <tr>
      <th>4</th>
      <td>322</td>
      <td>110</td>
      <td>3</td>
      <td>3.5</td>
      <td>2.5</td>
      <td>8.67</td>
      <td>1</td>
      <td>0.80</td>
    </tr>
    <tr>
      <th>7</th>
      <td>321</td>
      <td>109</td>
      <td>3</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>8.20</td>
      <td>1</td>
      <td>0.75</td>
    </tr>
    <tr>
      <th>12</th>
      <td>327</td>
      <td>111</td>
      <td>4</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>9.00</td>
      <td>1</td>
      <td>0.84</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Pandas cuenta con funciones que darían la misma salida sin utilizar signos de compararación
# .gt() = >
# .lt() = <
dataframe[(dataframe["chance of admit"].gt(0.7)) & (dataframe["chance of admit"].lt(0.9))].head()
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
      <th>gre score</th>
      <th>toefl score</th>
      <th>university rating</th>
      <th>sop</th>
      <th>lor</th>
      <th>cgpa</th>
      <th>research</th>
      <th>chance of admit</th>
    </tr>
    <tr>
      <th>Serial No.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>324</td>
      <td>107</td>
      <td>4</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>8.87</td>
      <td>1</td>
      <td>0.76</td>
    </tr>
    <tr>
      <th>3</th>
      <td>316</td>
      <td>104</td>
      <td>3</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>8.00</td>
      <td>1</td>
      <td>0.72</td>
    </tr>
    <tr>
      <th>4</th>
      <td>322</td>
      <td>110</td>
      <td>3</td>
      <td>3.5</td>
      <td>2.5</td>
      <td>8.67</td>
      <td>1</td>
      <td>0.80</td>
    </tr>
    <tr>
      <th>7</th>
      <td>321</td>
      <td>109</td>
      <td>3</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>8.20</td>
      <td>1</td>
      <td>0.75</td>
    </tr>
    <tr>
      <th>12</th>
      <td>327</td>
      <td>111</td>
      <td>4</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>9.00</td>
      <td>1</td>
      <td>0.84</td>
    </tr>
  </tbody>
</table>
</div>




```python
# al ser funciones de Pandas podemos concatenarlas sin usar &
dataframe[dataframe["chance of admit"].gt(0.7).lt(0.9)].head()
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
      <th>gre score</th>
      <th>toefl score</th>
      <th>university rating</th>
      <th>sop</th>
      <th>lor</th>
      <th>cgpa</th>
      <th>research</th>
      <th>chance of admit</th>
    </tr>
    <tr>
      <th>Serial No.</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>314</td>
      <td>103</td>
      <td>2</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>8.21</td>
      <td>0</td>
      <td>0.65</td>
    </tr>
    <tr>
      <th>8</th>
      <td>308</td>
      <td>101</td>
      <td>2</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>7.90</td>
      <td>0</td>
      <td>0.68</td>
    </tr>
    <tr>
      <th>9</th>
      <td>302</td>
      <td>102</td>
      <td>1</td>
      <td>2.0</td>
      <td>1.5</td>
      <td>8.00</td>
      <td>0</td>
      <td>0.50</td>
    </tr>
    <tr>
      <th>10</th>
      <td>323</td>
      <td>108</td>
      <td>3</td>
      <td>3.5</td>
      <td>3.0</td>
      <td>8.60</td>
      <td>0</td>
      <td>0.45</td>
    </tr>
    <tr>
      <th>11</th>
      <td>325</td>
      <td>106</td>
      <td>3</td>
      <td>3.5</td>
      <td>4.0</td>
      <td>8.40</td>
      <td>1</td>
      <td>0.52</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
