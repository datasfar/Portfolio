# Tipos y secuencias en python

---

## Índice: 

1. [Tipos de datos básicos](#tipo-dato-primitivo)
2. [Tuplas](#tuplas)
3. [Listas](#listas)
4. [Strings](#strings)
5. [Método Format](#metodo-format)
6. [Diccionarios](#diccionarios)


---

<a id="tipo-dato-primitivo"></a>

## Tipos de datos básicos

```python
# Tipos básicos
t_str = "Something here!"
print(type(t_str))

t_int = 12
print(type(t_int))

t_float = 12.12
print(type(t_float))

t_bool = True
print(type(t_bool))

t_none = None
print(type(t_none))

def operate(x, y):
    return x + y
t_function = operate
print(type(t_function))
```

    <class 'str'>
    <class 'int'>
    <class 'float'>
    <class 'bool'>
    <class 'NoneType'>
    <class 'function'>
    

<a id="tuplas"></a>

### Tuplas


```python
t_tuple = (1, "python", 2.3, "C++", "cobol", 0.2)
print(type(t_tuple))

# desempaque -> permite asociar varias variables a la vez
x, y, z, j, m, n = t_tuple
print(z)
```

    <class 'tuple'>
    2.3
    
<a id="listas"></a>

### Listas 
Las listas son muy parecidas a las tuplas pero son mutables, por lo que puedes cambiar son longitud, número de elementos y valores de los elementos.



```python
t_list = [1, 2, "b", 23, .2, "jdk"]
print(type(t_list))
print(t_list)

# append -> añade nuevos elementos a la lista
t_list.append(2.1)
t_list.append("vsc")
print(t_list)

# iterar -> podemos ver todos los valores individuales de una lista iterandola con un bucle for
for item in t_list:
    print(item)

# indexado -> podemos acceder a sus valores utilizando el indexado entre corchetes
print(t_list[0]) # primer elemento de la lista
print(t_list[-1]) # ultimo elemento de la lista
print(t_list[0:3]) # rango de elementos, primer valor x incluido, segundo y excluido [x:y)

# concatenar -> podemos concatenar listas con +
new_list = [1, 2, 3] + [4, 5]
print(new_list)

# repetir -> podemos repetir listas con *
print(new_list * 2)

# esta en -> podemos ver si un valor esta en una lista con in, retorna un boolean
print(5 in new_list)
```

    <class 'list'>
    [1, 2, 'b', 23, 0.2, 'jdk']
    [1, 2, 'b', 23, 0.2, 'jdk', 2.1, 'vsc']
    1
    2
    b
    23
    0.2
    jdk
    2.1
    vsc
    1
    vsc
    [1, 2, 'b']
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    True
    
<a id="strings"></a>

### Strings
Las listas y las cadenas de texto se comportan de forma muy parecida en python. Podemos ver los strings como listas de carácteres. Así que podemos realizar con ellas las mismas operaciones que con las listas.


```python
name = "Robert"
lastname = "Ribs"

print(name + " " + lastname)
print(name * 3)
print("R" in name)

# split() -> podemos dividir cadenas de caracteres basandonos en un criterio
some_text = "This is a example text."
print(some_text.split(" ")) # divimos por expacios
print(some_text.split(" ")[0]) # tambien permite la utilización de indices

# str() -> permite convertir otros tipos a strings para poder operar con ellos
print("Hello " + str(123))
```

    Robert Ribs
    RobertRobertRobert
    True
    ['This', 'is', 'a', 'example', 'text.']
    This
    Hello 123

<a id="metodo-format"></a> 

### Método Format
Podemos dar formatos de salida a un string de la siguiente forma.


```python
ventas = {
    "precio":2.10,
    "cantidad":5,
    "encargado": "Martin"
}

salida = "{} vendio {} objetos, a un precio de {} cada uno. El precio final es {}"

print(salida.format(
    ventas["encargado"],
    ventas["cantidad"],
    ventas["precio"],
    ventas["precio"] * ventas["cantidad"]
))
```

    Martin vendio 5 objetos, a un precio de 2.1 cada uno. El precio final es 10.5
    
<a id="diccionarios"></a>

### Diccionarios
Los diccionarios almacenan pares de clave-valor, no tienen orden. Se denotan con llaves {}.


```python
t_dict = {"name":"Robert", "mail":"rob@mail.com", "age":23}
print(type(t_dict))
print(t_dict)

print(t_dict.keys()) # podemos acceder a las claves con keys()
print(t_dict.values()) # podemos acceder a los valores con value()
print(t_dict["name"]) # tambien podemos acceder a los valores asociados usando la clave

# añadir nuevos grupos clave-valor
t_dict["job"] = False
print(t_dict)

# iterar claves en un diccionario
for key in t_dict:
    print(key)

# iterar valores en un diccionario
for stat in t_dict:
    print(t_dict[stat])

# items() -> nos permite iterar claves y valores a la vez
for group in t_dict.items():
    print(group)
```

    <class 'dict'>
    {'name': 'Robert', 'mail': 'rob@mail.com', 'age': 23}
    dict_keys(['name', 'mail', 'age'])
    dict_values(['Robert', 'rob@mail.com', 23])
    Robert
    {'name': 'Robert', 'mail': 'rob@mail.com', 'age': 23, 'job': False}
    name
    mail
    age
    job
    Robert
    rob@mail.com
    23
    False
    ('name', 'Robert')
    ('mail', 'rob@mail.com')
    ('age', 23)
    ('job', False)
    


