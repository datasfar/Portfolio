# Expresiones Regulares (REGEX)

---

## Índice: 

1. [Funciones regex](#funciones)
2. [Patrones básicos](#patrones-basicos)
3. [Grupos y alternancia](#grupos)
4. [Caracteres](#caracteres)
5. [Secuencias de escape](#escape)
6. [Anclas](#anclas)

---

Las regex son patrones utilizados para buscar y manipular cadenas de texto. Son muy potentes y se utilizan en una amplia variedad de tareas relacionadas con el procesamiento de texto, como validación de entradas, búsqueda y reemplazo de texto, extracción de datos, entre otros.


```python
import re
```

<a id="funciones"></a>

## Funciones 


```python
# match() -> busca un patrón al principio de una cadena. Si lo encuentra devuelve un 
# objeto Match, si no, devuelve "None"

texto = "Encantado de conocerte"

resultado = re.match("Encantado", texto)
print(resultado)

resultado = re.match("Hola", texto)
print(resultado)

```

    <re.Match object; span=(0, 9), match='Encantado'>
    None
    


```python
# search() -> busca un patrón en cualquier parte de la cadena. Si lo encuentra devuelve 
# un objeto Match, si no, devuelve "None"

texto = "Hoy será un buen día."
if re.search("buen", texto):
    print("Genial!")
else:
    print("F")
```

    Genial!
    


```python
# findall() -> devuelve una lista con todas las coincidencias que se encuentren en la 
# cadena. Se utiliza para extraer multiples elementos que coincidan con un patrón.

texto = "Esto es un texto de ejemplo, un tipo string."
resultados = re.findall("un", texto)
print(resultados)
```

    ['un', 'un']
    


```python
# split() -> divide una cadena en una lista utilizando un patrón como delimitador.
# Devuelve una lista de segmentos de la cadena.

texto = "Esto es un texto de ejemplo, un tipo string."
resultados = re.split("un", texto)
print(resultados)
```

    ['Esto es ', ' texto de ejemplo, ', ' tipo string.']
    

<a id="patrones-basicos"></a>

## Patrones

##### Básicos
    .: Cualquier carácter excepto nueva línea.
    ^: Inicio de la cadena.
    $: Final de la cadena.
    *: Cero o más repeticiones del carácter o grupo anterior.
    +: Una o más repeticiones del carácter o grupo anterior.
    ?: Cero o una repetición del carácter o grupo anterior.
    {n}: Exactamente n repeticiones.
    {n,}: Al menos n repeticiones.
    {n,m}: Entre n y m repeticiones.


```python
# "." coincide con cualquier cadena donde 'a' y 'b' están separados por un solo carácter
pattern = r'a.b'
string = 'acb a_b a-b a\nb'
matches = re.findall(pattern, string)
print("Coincidencias:", matches)

# "^" coincide con cualquier cadena que comienza con "Hola"
pattern = r'^Hola'
string = 'Hola mundo'
match = re.search(pattern, string)
print("Coincidencia:", match.group() if match else "No se encontró coincidencia")

# "$" coincide con cualquier cadena que termina con "mundo"
pattern = r'mundo$'
string = 'Hola mundo'
match = re.search(pattern, string)
print("Coincidencia:", match.group() if match else "No se encontró coincidencia") 

# "*" coincide con 'a' seguido de cero o más 'b', seguido de 'c'
pattern = r'ab*c'
string = 'ac abc abbc'
matches = re.findall(pattern, string)
print("Coincidencias:", matches) 

# "+" coincide con 'a' seguido de una o más 'b', seguido de 'c'
pattern = r'ab+c'
string = 'ac abc abbc'
matches = re.findall(pattern, string)
print("Coincidencias:", matches)

# "?" coincide con 'a' seguido de cero o una 'b', seguido de 'c'.
pattern = r'ab?c'
string = 'ac abc abbc'
matches = re.findall(pattern, string)
print("Coincidencias:", matches)

# "{n}" coincide con exactamente n veces 'a' consecutivas 
pattern = r'a{3}'
string = 'a aa aaa aaaa'
matches = re.findall(pattern, string)
print("Coincidencias:", matches)

# "{n,}" coincide con al menos n veces 'a' consecutivas
pattern = r'a{2,}'
string = 'a aa aaa aaaa'
matches = re.findall(pattern, string)
print("Coincidencias:", matches) 

# {n,n} cincide con entre n y n veces 'a' consecutivas
pattern = r'a{2,3}'
string = 'a aa aaa aaaa'
matches = re.findall(pattern, string)
print("Coincidencias:", matches)
```

    Coincidencias: ['acb', 'a_b', 'a-b']
    Coincidencia: Hola
    Coincidencia: mundo
    Coincidencias: ['ac', 'abc', 'abbc']
    Coincidencias: ['abc', 'abbc']
    Coincidencias: ['ac', 'abc']
    Coincidencias: ['aaa', 'aaa']
    Coincidencias: ['aa', 'aaa', 'aaaa']
    Coincidencias: ['aa', 'aaa', 'aaa']
    

<a id="grupos"></a>

## Grupos y Alternancia
    (): Agrupación de patrones.
    |: Alternancia (o lógico).


```python
# "()" los paréntesis se utilizan para agrupar partes de la expresión regular. Esto es útil 
# cuando necesitas aplicar operadores a un grupo de caracteres o cuando deseas capturar 
# partes específicas de la coincidencia
pattern = r'(\d{3})-(\d{2})-(\d{4})'
string = 'Mi número es 123-45-6789.'
match = re.search(pattern, string)

if match:
    print("Coincidencia:", match.group())  
    print("Grupo 1:", match.group(1))    
    print("Grupo 2:", match.group(2))      
    print("Grupo 3:", match.group(3))  


# "|" el operador | se utiliza para especificar alternativas. Coincide con cualquiera de los patrones
# separados por |
pattern = r'a|b'
string = 'a b c d e f g h'
matches = re.findall(pattern, string)
print("Coincidencias:", matches)
```

    Coincidencia: 123-45-6789
    Grupo 1: 123
    Grupo 2: 45
    Grupo 3: 6789
    Coincidencias: ['a', 'b']
    

<a id="caracteres"></a>

## Caracteres

### Clases
    \d: Cualquier dígito, equivale a [0-9].
    \D: Cualquier carácter que no sea un dígito, equivale a [^0-9].
    \w: Cualquier carácter de palabra (letra, dígito, guion bajo), equivale a [a-zA-Z0-9_].
    \W: Cualquier carácter que no sea de palabra, equivale a [^a-zA-Z0-9_].
    \s: Cualquier espacio en blanco (espacio, tabulación, nueva línea), equivale a [ \t\n\r\f\v].
    \S: Cualquier carácter que no sea un espacio en blanco, equivale a [^ \t\n\r\f\v].

### Conjuntos
    [abc]: Cualquier carácter 'a', 'b' o 'c'.
    [^abc]: Cualquier carácter excepto 'a', 'b' o 'c'.
    [a-z]: Cualquier carácter en el rango de 'a' a 'z'.
    [A-Z]: Cualquier carácter en el rango de 'A' a 'Z'.
    [0-9]: Cualquier dígito del 0 al 9.


```python
# Encontrar nombres propios en un texto
# Patrón: \b[A-Z][a-z]*\b
#
#   [A-Z]: Una letra mayúscula.
#   [a-z]*: Cero o más letras minúsculas.
#   \b: Borde de palabra.

pattern = r'\b[A-Z][a-z]*\b'
string = 'Alicia y Roberto asistieron a una entrevista con Pablo.'
matches = re.findall(pattern, string)
print("Nombres propios encontrados:", matches)
```

    Nombres propios encontrados: ['Alicia', 'Roberto', 'Pablo']
    


```python
# Validación de un número de teléfono en el formato "(123) 456-7890".
# Patrón: "^\(\d{3}\)\s\d{3}-\d{4}$"
#
#   \d{3}: Tres dígitos.
#   \s: Un espacio.
#   \d{4}: Cuatro dígitos.
#   \(\d{3}\): Tres dígitos dentro de paréntesis.

pattern = r'^\(\d{3}\)\s\d{3}-\d{4}$'
string = '(123) 456-7890'
match = re.match(pattern, string)
print("Número de teléfono válido:", bool(match)) 
```

    Número de teléfono válido: True
    


```python
# Validación de correo electrónico.
# Patrón: ^[\w\.-]+@[\w\.-]+\.\w+$
# 
#   \w: Cualquier carácter de palabra.
#   [\w\.-]+: Uno o más caracteres de palabra, puntos o guiones.
#   @: El símbolo arroba.
#   [\w\.-]+\.\w+: Dominio seguido de un punto y una palabra.

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
string = 'correo.ejemplo@dominio.com'
match = re.match(pattern, string)
print("Correo electrónico válido:", bool(match))
```

    Correo electrónico válido: True
    

<a id="escape"></a>

### Secuencias de Escape
    \\: Barra invertida literal.
    \.: Punto literal.
    \*: Asterisco literal.
    \+: Más literal.
    \?: Signo de interrogación literal.
    \|: Barra vertical literal.
    \(: Paréntesis izquierdo literal.
    \): Paréntesis derecho literal.
    \{: Llave izquierda literal.
    \}: Llave derecha literal.
    \[: Corchete izquierdo literal.
    \]: Corchete derecho literal.


```python
# busca el signo * en una cadena
pattern = r'\*'
string = '5 * 3 = 15'
match = re.search(pattern, string)
print("Coincidencia:", match.group() if match else "No se encontró coincidencia")

# busca el signo + en una cadena 
pattern = r'\+'
string = '3 + 5 = 8'
match = re.search(pattern, string)
print("Coincidencia:", match.group() if match else "No se encontró coincidencia")

# busca el signo ? en una cadena
pattern = r'\?'
string = '¿Cómo estás?'
match = re.search(pattern, string)
print("Coincidencia:", match.group() if match else "No se encontró coincidencia")
```

    Coincidencia: *
    Coincidencia: +
    Coincidencia: ?
    

<a id="anclas"></a>

### Anclas
    \b: Frontera de palabra.
    \B: No frontera de palabra.
    \A: Inicio de la cadena.
    \Z: Final de la cadena.


```python
# coincide con la palabra "word" como una palabra completa
pattern = r'\bword\b'
string = 'A word of warning: the word is out.'
matches = re.findall(pattern, string)
print("Coincidencias:", matches)

# coincide con "word" cuando no está en el límite de una palabra
pattern = r'\Bword\B'
string = 'A sword wordy wordsmith.'
matches = re.findall(pattern, string)
print("Coincidencias:", matches)

# coincide con "Start" solo si está al inicio de la cadena
pattern = r'\AStart'
string = 'Start at the beginning. Start again.'
match = re.match(pattern, string)
print("Coincidencia:", match.group() if match else "No se encontró coincidencia") 

# coincide con "end" solo si está al final de la cadena
pattern = r'end\Z'
string = 'This is the end'
match = re.search(pattern, string)
print("Coincidencia:", match.group() if match else "No se encontró coincidencia") 
```

    Coincidencias: ['word', 'word']
    Coincidencias: []
    Coincidencia: Start
    Coincidencia: end
    
