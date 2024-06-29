# Fechas y horas

---

## Índice: 

1. [DateTime](#datetime)
2. [Delta](#timestamp)

---

Las fechas y horas se pueden almacenar de muchas formas diferentes. Uno de los formatos más utilizado esta basado en el desplazamiento de la época, es decir, almacena los segundos o milisengundos pasados desde 1/01/1970 hasta el momento del registro.

## Datetime

```python
import datetime as dt
import time as tm
```

<a id="datetime"></a>

```python
print(tm.time()) # timestamp

datetime_now =  dt.datetime.fromtimestamp(tm.time()) # formato legible
print(datetime_now)

# tambien podemos acceder a cada valor independientemente
print(datetime_now.year, datetime_now.month, datetime_now.day, datetime_now.hour)
```

    1719656032.8880942
    2024-06-29 12:13:52.888094
    2024 6 29 12
    


<a id="timestamp"></a>

## Delta

```python
delta = dt.timedelta(days=100) # podemos crear intervalos de tiempo
print(delta)

hoy = dt.date.today() # y operar con ellos si tienen el mismo formato
hace_100_dias = hoy - delta 
print(hace_100_dias)
print(hoy > hace_100_dias)
```

    100 days, 0:00:00
    2024-03-21
    True
    
