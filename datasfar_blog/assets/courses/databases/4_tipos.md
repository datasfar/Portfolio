# Tipos de datos SQL

---

## Índice: 

1. [Tipos de datos numéricos (INT)](#1)
2. [Ejercicio 1: Creación de bases de datos y datos numéricos](#2)
3. [Tipos de datos cadena de texto (STRINGS)](#3)
4. [Ejercicio 2: Trabajar con cadenas](#4)
5. [Restricciones en las bases de datos](#5)
6. [Ejercicio 3: Trabajar con valores predeterminados](#6)
7. [Ejercicio 4: Elegir el tipo de datos apropiado para una columna](#7)


---
<a id="1"></a>

### Tipos de datos numéricos (int)

- **Tipos de datos numéricos**:
    - Permiten que una columna almacene datos en forma de números.
    - **Enteros**: Para valores numéricos sin fracciones.
    - **Decimales**: Para números con fracciones.
    
- **Aplicación de tipos numéricos**:
    - **Cantidad de producto**:
        - Se define como tipo de datos entero (solo contiene números enteros).
        - Números fraccionarios se convierten automáticamente al entero más próximo.
    - **Precio total**:
        - Se define como tipo decimal (contiene números fraccionarios).
        - Ejemplo: $80.90 (80 es entero, 90 es decimal).
        - Números enteros también se aceptan y se almacenan como decimales con fracción de cero.
        
- **Especificidad de tipos numéricos en MySQL**:
    - **TINYINT**: Para valores enteros muy pequeños (máximo 255).
    - **INT**: Para valores enteros grandes (máximo supera los cuatro mil millones).
    - Ambos tipos pueden aceptar valores negativos y positivos.
    - En algunos SGBD, se puede forzar a que las columnas acepten solo números positivos, aumentando el valor máximo almacenable.
    

---
<a id="2"></a>

### Ejercicio 1: Creación de bases de datos y tipos numéricos

**Objetivo**

El objetivo de este ejercicio es que aprenda a trabajar con valores numéricos en una base de datos. El fin del ejercicio es que pueda demostrar cómo se trabaja con tipos de datos numéricos en SQL. En este ejercicio, aprenderá sobre dos variaciones principales de los tipos de datos numéricos.

**Escenario**

Esta información incluye:
●	El ID o número del dispositivo, 
●	El nombre del dispositivo,
●	Y el precio del aparato.

**Instrucciones**

**Tarea 1: Cree una base de datos llamada cm_dispositivos**

**Tarea 2: Cree una sentencia SQL con atributos y tipos de datos relevantes** 

**Solución:**

```sql
-- Crear la base de datos
CREATE DATABASE cm_devices;

-- Usar la base de datos
USE cm_devices;

-- Crear la tabla devices con las 3 columnas
CREATE TABLE devices (
    deviceID int,
    deviceName varchar(50),
    price decimal(10, 2)
);

-- Ver las tablas de la base de datos 
SHOW tables;

-- Ver las columnas
SHOW columns FROM devices;
```

**Tarea adicional (opcional)**

El Sr. Merkel quiere crear otra tabla básica en la base de datos para almacenar datos sobre el stock de los dispositivos, incluyendo el ID del dispositivo, la cantidad disponible en el stock y el coste total disponible de la cantidad. Esta tabla básica se muestra en la siguiente tabla, con cada columna mostrando el ID del dispositivo, la cantidad en stock y el precio total.

A partir de la tabla y la información anterior, complete lo siguiente:

**1.**	Identificar un nombre de tabla apropiado para crear, dada la información proporcionada.

- Stock (Existencias)

**2.**	Identifique las columnas que deberían estar disponibles en esta tabla y defínalas con los tipos de datos adecuados.

- device_id (INT), quantity (INT), price(Decimal)

**3.**	Escriba la sentencia SQL completa que crea la tabla y las columnas.

```sql
CREATE TABLE stock (
    device_ID int,
    quantity int,
    price decimal(10, 2)
);
```

---
<a id="3"></a>
### Tipos de datos cadena de texto (string)

- **Tipos de datos de cadena**:
    - Utilizados cuando se pretende almacenar datos con una mezcla de caracteres (alfabéticos, numéricos, especiales).
    - Permiten insertar cualquier tipo de texto en las columnas definidas.
    
- **Tipos de datos de cadena más utilizados**:
    - **CHAR**: Para caracteres de longitud fija. Definido como `CHAR(n)` donde `n` es el número de caracteres.
        - Ejemplo: `CHAR(50)` significa que cada entrada ocupará 50 caracteres de espacio.
    - **VARCHAR**: Para caracteres de longitud variable. Definido como `VARCHAR(n)` donde `n` es el número máximo de caracteres permitidos.
        - Ejemplo: `VARCHAR(50)` permite cualquier entrada de hasta 50 caracteres.
        
- **Diferencias entre CHAR y VARCHAR**:
    - **CHAR**: La longitud es fija y predeterminada. Utilizado cuando se tiene un tamaño constante de caracteres.
    - **VARCHAR**: La longitud es variable y no fija. Utilizado cuando no se sabe cuántos caracteres se insertarán en el campo.
    
- **Ejemplos en la tabla de estudiantes**:
    - Columna "Nombre de usuario" puede ser `CHAR(50)`, ocupando 50 caracteres de espacio, incluso si el nombre es más corto.
    - Columna "Nombre del estudiante" puede ser `VARCHAR(50)`, ocupando solo el espacio necesario según la longitud del nombre.
    
    ![Untitled](/courses/databases/Tipos%20de%20datos%20SQL%20cef815d65c554bc087db6426cb75c99e/Untitled.png)
    

- **Otros tipos de datos de cadena**:
    - **TINYTEXT**: Menos de 255 caracteres. Ejemplo: párrafos cortos.
    - **TEXT**: Menos de 65,000 caracteres. Ejemplo: artículos.
    - **MEDIUMTEXT**: Hasta 16.7 millones de caracteres. Ejemplo: texto de un libro.
    - **LONGTEXT**: Hasta 4 GB de datos de texto.
    

---
<a id="4"></a>

### Ejercicio 2: Trabajar con cadenas

**Objetivo**

El objetivo de este ejercicio es que aprenda a trabajar con valores numéricos en una base de datos. El fin es permitirle practicar el trabajo con tipos de datos de cadenas en SQL. Este ejercicio se centra en los dos tipos de datos de cadena más utilizados en SQL:

**Escenario**

El Sr. Carl Merkel es propietario de una pequeña empresa que vende dispositivos móviles llamada "CM Mobiles". Quiere crear una nueva tabla para almacenar información clave sobre los clientes, incluyendo el nombre de usuario del cliente, el nombre completo del cliente y la dirección de correo electrónico del cliente, como se muestra en la siguiente tabla de datos.

![Untitled](/courses/databases/Tipos%20de%20datos%20SQL%20cef815d65c554bc087db6426cb75c99e/Untitled%201.png)

**Instrucciones**

Intente realizar las siguientes tareas antes de continuar, para que pueda comprobar y comparar sus respuestas con nuestra solución.

Cree una sentencia SQL con los atributos y tipos de datos relevantes como se indica a continuación:

**1.** Identifique un nombre adecuado para la tabla en la que quiera almacenar datos sobre los dispositivos móviles.

**2.** Identifique el tipo de datos para cada columna de la tabla.

**3.** Escriba una sentencia SQL completa para crear la tabla dentro de la base de datos cm_devices.

**Solución:**

```sql
-- Crear la base de datos
CREATE DATABASE cm_devices;

-- Usar la base de datos
USE cm_devices;

-- Crear la tabla devices con las 3 columnas
CREATE TABLE clients (
    user_name CHAR(9),
    full_name VARCHAR(100),
    email VARCHAR(255)
);

-- Ver las tablas de la base de datos 
SHOW tables;

-- Ver las columnas
SHOW columns FROM clients;
```

**Tarea adicional (opcional)**

Crear otra tabla básica en la base de datos cm_devices para almacenar las opiniones de los clientes. Esta tabla debe incluir tres columnas:

●	Columna ID de comentarios,
●	Columna de tipo de comentarios con un máximo de 100 caracteres,
●	Una columna de comentarios con un máximo de 500 caracteres.

![Untitled](/courses/databases/Tipos%20de%20datos%20SQL%20cef815d65c554bc087db6426cb75c99e/Untitled%202.png)

A. Declare las columnas con el tipo de datos adecuado para cada una.

- comment_id CHAR(8), comment_type VARCHAR(100), comment _content TEXT(500)

B. Escriba la sentencia SQL que crea la tabla de comentarios.

```sql
CREATE TABLE comments (
    comment_id CHAR(9),
    comment_type VARCHAR(100),
    comment_content TEXT(500)
);
```

---
<a id="5"></a>

### Restricciones en las bases de datos

- **Importancia de las restricciones**:
    - Limitan el tipo de datos que se puede ingresar en una tabla.
    - Garantizan la precisión y confiabilidad de los datos.
    - Interrumpen operaciones que infringen las restricciones (p.ej., insertar datos no válidos).
    
- **Tipos de restricciones**:
    - **Nivel de columna**: Se aplican a una columna específica.
    - **Nivel de tabla**: Se aplican a toda la tabla (p.ej., claves externas para mantener la integridad referencial).
    
- **Restricciones comunes**:
    - **NOT NULL**: Garantiza que los campos de datos no queden vacíos.
    - **DEFAULT**: Establece un valor predeterminado para una columna si no se especifica ningún valor.
    
- **Ejemplo de restricción NOT NULL**:
    - En una tabla de u
    - Se define mediante una sentencia SQL `CREATE TABLE` que incluye `NOT NULL` para cada columna.
    - Evita la creación de registros con valores nulos.
    
- **Ejemplo de restricción DEFAULT**:
    - En una tabla de jugadores de un club de fútbol con columnas `nombre del jugador` y `ciudad`.
    - La mayoría de los jugadores son de Barcelona, por lo que se puede establecer un valor predeterminado `DEFAULT 'Barcelona'` para la columna `ciudad`.
    - Ahorra la necesidad de ingresar repetidamente "Barcelona" para cada nuevo jugador.
    
- **Implementación en SQL**:
    - **NOT NULL**:
        
        ```sql
        CREATE TABLE clientes (
            id_cliente INT NOT NULL,
            nombre_cliente VARCHAR(255) NOT NULL
        );
        ```
        
    - **DEFAULT**:
        
        ```sql
        CREATE TABLE jugadores (
            nombre_jugador VARCHAR(255) NOT NULL,
            ciudad VARCHAR(255) DEFAULT 'Barcelona'
        );
        ```
        

- **Propósito de las restricciones**:
    - Aseguran la integridad de los datos en la base de datos.
    - Facilitan el cumplimiento de reglas a nivel de columna y tabla.
    
- **Conclusión**:
    - Comprender y aplicar restricciones es fundamental para mantener la calidad y coherencia de los datos en las bases de datos.
    - Las restricciones `NOT NULL` y `DEFAULT` son herramientas clave para manejar entradas de datos y mantener la integridad de la información.
    

---
<a id="6"></a>

### Ejercicio 3: Trabajar con valores predeterminados

**Objetivo**

El objetivo de este ejercicio es que aprenda a trabajar con valores predeterminados en una base de datos. El fin es permitirle practicar el trabajo con valores por defecto utilizando la restricción por defecto en SQL.

**Escenario**

El Sr. Carl Merkel posee una pequeña empresa que vende dispositivos móviles llamada "CM Mobiles" en Harrow, Londres. Desea crear una nueva base de datos para almacenar información clave sobre las direcciones de los clientes que incluya ID del cliente, la calle, el código postal y el nombre del pueblo. La lista de direcciones de los clientes actuales de CM Mobiles se encuentra en la siguiente tabla de direcciones.

![Untitled](/courses/databases/Tipos%20de%20datos%20SQL%20cef815d65c554bc087db6426cb75c99e/Untitled%203.png)

**Instrucciones**

Crea una sentencia SQL con los atributos y restricciones pertinentes de la siguiente manera:

**1.** Identifique la columna que requiere valores predeterminados.

**2.**Escriba una sentencia SQL completa para crear la tabla de direcciones con las restricciones pertinentes.

**Solución:**

```sql
-- Crear la base de datos
CREATE DATABASE cm_devices;

-- Usar la base de datos
USE cm_devices;

-- Crear la tabla address
CREATE TABLE address(
    client_id int NOT NULL,
    street varchar(255),
    post_code varchar(10),
    town varchar(30) DEFAULT "Harrow"
);

-- Ver las tablas de la base de datos 
SHOW tables;

-- Ver las columnas
SHOW columns FROM address;
```

**Tarea adicional (opcional)**

El Sr. Carl Merkel se da cuenta de que la mayoría de los clientes tienen el mismo código postal, es decir, “HA97DE”.

Se le pide que escriba la sentencia SQL de nuevo para declarar tanto el código postal como el nombre de la ciudad con valores predeterminados.

Recuerde eliminar la tabla de direcciones antes de crear una nueva.

Para eliminar la tabla, simplemente escriba:  **DROP TABLE Address;**.

**Solución:**

```sql
-- Eliminar la tabla
DROP TABLE address

-- Crear la tabla address
CREATE TABLE address(
    client_id int NOT NULL,
    street varchar(255),
    post_code varchar(10) DEFAULT "HA97DE",
    town varchar(30) DEFAULT "Harrow"
);
```

---
<a id="7"></a>

### Ejercicio 4: Elegir el tipo de datos adecuado para una columna

**Objetivos del ejercicio**

Este ejercicio demuestra cómo elegir tipos de datos adecuados para una variedad de columnas para almacenar datos como cadena, entero, fecha y valores decimales.

**Escenario**

El Sr. Carl Merkel posee una pequeña empresa que vende dispositivos móviles llamada "CM Mobiles" en la ciudad de Harrow, cerca de Londres. El Sr. Carl desea crear una nueva base de datos para almacenar información clave sobre los pedidos de los clientes y generar facturas que incluyan el nombre del cliente, la fecha del pedido, la cantidad y precio total. Estos datos se pueden ver en la siguiente tabla de facturas:

![Untitled](/courses/databases/Tipos%20de%20datos%20SQL%20cef815d65c554bc087db6426cb75c99e/Untitled%204.png)

**Instrucciones**

Tiene que escribir la sentencia SQL "CREATE TABLE" con los atributos y tipos de datos relevantes.

1. Identifique las columnas y defina el tipo de datos para cada columna de la tabla.

2. Escriba una sentencia SQL completa para crear la tabla de facturas dentro de la base de datos cm_devices.

```sql
CREATE TABLE invoice(
    costumer_name varchar(50),
    order_date DATE,
    quantity INT,
    price decimal(10, 2)
);
```

**Tarea adicional (opcional)**

El sr. Carl necesita tener una nueva tabla para almacenar los datos de contacto de cada cliente, incluyendo el número de cuenta del cliente, el número de teléfono del cliente y la dirección de correo electrónico del cliente.

Se le pide que elija un tipo de datos relevante para cada una de las columnas.

- account_number INT
- phone_number INT
- email_address VARCHAR

---