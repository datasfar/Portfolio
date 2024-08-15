# Crear y Leer
---

## Índice: 

1. [CREATE y DROP](#1)
2. [Sentencia CREATE TABLE](#2)
3. [Sentencia ALTER TABLE](#3)
4. [Sentencia INSERT](#4)
5. [Resumen: Creación de tablas](#5)
6. [Ejercicio 1: Crear base de datos, crear tabla e insertar datos](#6)
7. [Sentencia SELECT](#7)
8. [Sentencia INSERT INTO SELECT](#8)
9. [Ejercicio 2: Practicar la creación de tablas](#9)


---
<a id="1"></a>

### Base de datos CREATE y DROP

**Objetivo de la Base de Datos**

- Antes de crear una base de datos, definir claramente su propósito.
- Ejemplo: Para una librería en línea, la base de datos debe registrar datos de títulos, autores, clientes y ventas.
- Estos datos se deben almacenar en tablas organizadas dentro de la base de datos.
- Usuarios pueden acceder, recuperar y actualizar los datos según sea necesario.

**Crear una Base de Datos con SQL**

1. **Sintaxis Básica para Crear una Base de Datos:**
    - Escribir las palabras clave `Create Database`.
    - Seguir con el nombre de la base de datos.
    
    ```sql
    CREATE DATABASE nombre_de_base_de_datos;
    ```
    
2. **Ejemplo Práctico:**
    - Crear una segunda base de datos para la librería.
    - Usar `Create Database` seguido del nombre significativo `bookstore2_db`.
    
    ```sql
    CREATE DATABASE bookstore2_db;
    ```
    
3. **Consideraciones:**
    - El nombre de la base de datos debe ser único.
    - Puede tener un máximo de 63 caracteres.
    - Terminar la sentencia con un punto y coma.

**Eliminar una Base de Datos con SQL**

1. **Sintaxis Básica para Eliminar una Base de Datos:**
    - Escribir las palabras clave `Drop Database`.
    - Seguir con el nombre de la base de datos que se desea eliminar.
    
    ```sql
    DROP DATABASE nombre_de_base_de_datos;
    ```
    
2. **Ejemplo Práctico:**
    - Eliminar la base de datos `bookstore_db`.
    
    ```sql
    DROP DATABASE bookstore_db;
    ```
    

---
<a id="2"></a>

### Sentencia CREATE TABLE

**Ejemplo Práctico: Creación de una Tabla de Clientes**

1. **Crear la Tabla:**
    - Asegurarse de tener una base de datos existente.
    - Escribir la sentencia SQL para crear una tabla llamada `clientes`.
    
    ```sql
    CREATE TABLE clientes (
        nombre_cliente VARCHAR(255),
        numero_telefono INT
    );
    ```
    
2. **Detalles de la Sintaxis:**
    - **`nombre_cliente`**: Columna para almacenar nombres de clientes.
        - Tipo de dato: `VARCHAR(255)` (cadena de caracteres con un máximo de 255 caracteres).
    - **`numero_telefono`**: Columna para almacenar números de teléfono.
        - Tipo de dato: `INT` (números enteros).
    - Terminar la definición de la tabla con un paréntesis de cierre y un punto y coma.

---
<a id="3"></a>

### Sentencia ALTER TABLE

- Las tablas no son estáticas; se pueden reestructurar para agregar, eliminar o modificar columnas.
- Las modificaciones se realizan utilizando la sintaxis SQL, específicamente con la sentencia `ALTER TABLE`.

**Sintaxis de `ALTER TABLE`**

1. **Estructura Básica:**
    - Comenzar con las palabras clave `ALTER TABLE`.
    - Seguir con el nombre de la tabla que se desea modificar.
    - Incluir comandos adicionales para agregar, eliminar o modificar columnas.
    
    ```sql
    ALTER TABLE nombre_de_tabla
    [ADD COLUMN nombre_columna tipo_dato, ...]
    [DROP COLUMN nombre_columna, ...]
    [MODIFY COLUMN nombre_columna tipo_dato];
    ```
    
2. **Agregar Columnas:**
    - Usar la palabra clave `ADD` para indicar que se agregarán nuevas columnas.
    - Especificar el nombre y tipo de datos para cada nueva columna.
    
    ```sql
    ALTER TABLE nombre_de_tabla
    ADD COLUMN nombre_columna tipo_dato;
    ```
    
3. **Eliminar Columnas:**
    - Usar la palabra clave `DROP COLUMN` para eliminar una columna existente.
    
    ```sql
    ALTER TABLE nombre_de_tabla
    DROP COLUMN nombre_columna;
    ```
    
4. **Modificar Columnas:**
    - Usar la palabra clave `MODIFY COLUMN` para cambiar los atributos de una columna existente.
    
    ```sql
    ALTER TABLE nombre_de_tabla
    MODIFY COLUMN nombre_columna nuevo_tipo_dato;
    ```
    

---
<a id="4"></a>

### Sentencia INSERT

- En el manejo de bases de datos, se necesita agregar nuevas filas y columnas a tablas existentes o crear nuevas tablas desde cero.
- La sentencia SQL `INSERT` permite agregar datos a tablas de manera rápida y eficiente.

**Sintaxis de `INSERT INTO`**

1. **Estructura Básica:**
    - **Agregar una Fila:**
        
        ```sql
        INSERT INTO nombre_de_tabla (columna1, columna2, ...)
        VALUES (valor1, valor2, ...);
        ```
        
    - **Agregar Múltiples Filas:**
        
        ```sql
        INSERT INTO nombre_de_tabla (columna1, columna2, ...)
        VALUES (valor1, valor2, ...),
               (valor3, valor4, ...),
               ...;
        ```
        
2. **Pasos para Insertar Datos:**
    - Escribir `INSERT INTO` seguido del nombre de la tabla.
    - Enumerar las columnas en las que se insertarán los datos entre paréntesis.
    - Usar `VALUES` seguido de los datos que se insertarán, también entre paréntesis.
    - Asegurarse de que cada valor corresponda a la columna específica y refleje el mismo tipo de datos y el mismo orden que las columnas listadas.
    - Los valores de texto y fecha deben ir entre comillas. Los valores numéricos no necesitan comillas.

**Ejemplo Práctico**

1. **Insertar Datos en una Tabla:**
    - Tabla: `jugadores` en la base de datos `club_deportivo`.
    - Columnas: `ID`, `Nombre`, `edad`, `fecha_de_inicio`.
    
    ```sql
    INSERT INTO jugadores (ID, Nombre, edad, fecha_de_inicio)
    VALUES (1, 'Yuval', 25, '2020-10-15');
    ```
    
    - **Notas:**
        - Los valores deben coincidir en tipo y orden con las columnas especificadas.
        - Las fechas deben estar en formato `YYYY-MM-DD`.
        - Los valores no numéricos (como texto y fechas) deben estar entre comillas simples.
2. **Insertar Múltiples Filas:**
    - Añadir dos nuevos jugadores, Mark y Karl.
    
    ```sql
    INSERT INTO jugadores (ID, Nombre, edad, fecha_de_inicio)
    VALUES (2, 'Mark', 27, '2020-10-12'),
           (3, 'Karl', 26, '2020-10-07');
    ```
    
    - **Notas:**
        - Los datos de cada fila se separan por comas.
        - Cada conjunto de valores está entre paréntesis.

**Consultar Datos en una Tabla**

1. **Mostrar Todos los Datos:**
    - Utilizar la sentencia `SELECT` para mostrar todos los datos en una tabla.
    
    ```sql
    SELECT * FROM jugadores;
    ```
    
    - **Notas:**
        - El asterisco (*) indica que se deben devolver todas las columnas.
        - La palabra clave `FROM` seguida del nombre de la tabla especifica de dónde obtener los datos.

---
<a id="5"></a>

### Creación de tablas (Resumen)

1. **Comandos Básicos**:
    - **CREATE DATABASE**: Crea una nueva base de datos.
    - **DROP DATABASE**: Elimina una base de datos existente.
    - **CREATE TABLE**: Crea una nueva tabla en una base de datos.
    - **ALTER TABLE**: Modifica la estructura de una tabla existente.
2. **Sintaxis CREATE TABLE**:
    - Utiliza la sentencia `CREATE TABLE` para definir una tabla.
    - Ejemplo de sintaxis: `CREATE TABLE table_name (column_name data_type(size), ...);`
    - Cada columna se define con un nombre y un tipo de datos, y opcionalmente un tamaño.
3. **Puntos Importantes al Crear Tablas**:
    - **Nombres Significativos**: Asigna nombres claros a las tablas y columnas.
    - **Tipos de Datos**: Los tipos de datos pueden variar entre sistemas de base de datos (e.g., `NUMBER` en Oracle, `INT` en MySQL).
    - **Longitud Adecuada**: Define la longitud apropiada para cada tipo de datos. Por ejemplo, `VARCHAR(n)` para datos textuales.
    - **Espacio de Almacenamiento**: `VARCHAR` es eficiente en el almacenamiento de texto, ocupando 1 byte por carácter más 2 bytes adicionales para la longitud.
4. **Ejemplo de Sintaxis**:
    - Para crear una tabla llamada “clientes” con diversas columnas:
        
        ```sql
        CREATE TABLE clientes (
          CustomerId INT,
          FirstName VARCHAR(40),
          LastName VARCHAR(20),
          Company VARCHAR(80),
          Address VARCHAR(70),
          City VARCHAR(40),
          State VARCHAR(40),
          Country VARCHAR(40),
          PostalCode VARCHAR(10),
          Phone VARCHAR(24),
          Fax VARCHAR(24),
          Email VARCHAR(60),
          SupportRapid INT
        );
        ```
        
    - En la sintaxis:
        - Se define el nombre de la tabla y se enumeran las columnas con su tipo de datos y longitud.
        - Los tipos de datos numéricos (e.g., `INT`) se usan para valores numéricos, mientras que los datos textuales utilizan `VARCHAR` con longitudes específicas.
        - Termina la sentencia con un punto y coma.

Estos puntos ayudan a comprender y aplicar correctamente la sentencia `CREATE TABLE` en SQL, asegurando una estructura adecuada y eficiente para las tablas en bases de datos.

---
<a id="6"></a>

### Ejercicio 1: Crear base de datos, crear tabla e insertar datos

**Objetivo**

El objetivo de este ejercicio es llevarlo a través de un proceso gradual para crear una base de datos, crear una tabla en la base de datos e insertar datos en la tabla. El fin es que practique cómo crear una base de datos, una tabla e insertar datos.

**Escenario**

El Sr. John Ericson es propietario de una pequeña librería. Decide crear una base de datos digital para mantener los datos de sus clientes de forma electrónica, en lugar de utilizar bolígrafo y papel. En este ejercicio, creará la base de datos de la librería.

**Instrucciones**

Tarea 1: Crear una base de datos llamada librería.

Tarea 2: Elaborar una tabla llamada clientes con ID de cliente, nombre y dirección.

Tarea 3: Insertar un registro de datos para un cliente.

**Solución:**

```sql
-- Crear la base de datos
CREATE DATABASE bookshop;

-- Usar la base de datos
USE bookshop;

-- Crear la tabla devices con las 3 columnas
CREATE TABLE custome (
    customer_id int,
    customer_name varchar(50),
    customer_address varchar(255)
);

-- Ver las columnas
SHOW columns FROM customers;

-- Insertar registros
INSERT INTO customers (customer_id, customer_name, customer_address) VALUES (1, "Jack", "Calle Falsa 123");

-- Ver los registros
SELECT * FROM customers;
```

**Tarea adicional (opcional)**

El Sr. Ericson quiere insertar otro registro de datos para otro cliente con los siguientes detalles: el ID es 2, el nombre es "James" y la dirección es "24 Carlson Road London".  Ahora su tarea es añadir los detalles del cliente en la tabla de cliente

```sql
INSERT INTO customers (customer_id, customer_name, customer_address) VALUES (2, "James", "24 Carlson Road London");
```

---
<a id="7"></a>

### Sentencia SELECT

- **Uso de la Sentencia SELECT**:
    - La sentencia `SELECT` se utiliza para consultar datos de una tabla en una base de datos.
    - Es posible recuperar datos específicos, realizar cálculos matemáticos, consultas sobre fecha y hora, y funciones de concatenación.
- **Sintaxis Básica de SELECT**:
    - La estructura básica de una sentencia `SELECT` es: `SELECT nombre_columna FROM nombre_tabla;`
    - Ejemplo: Para obtener los nombres de los jugadores de una tabla llamada `jugadores`, la sentencia sería: `SELECT nombre FROM jugadores;`
- **Consultas de Varias Columnas**:
    - Para recuperar datos de varias columnas, se enumeran los nombres de las columnas separados por comas.
    - Ejemplo: `SELECT nombre, nivel FROM jugadores;`
- **Recuperar Todos los Datos**:
    - Existen dos métodos para recuperar todos los datos de todas las columnas en una tabla:
        1. Enumerar todas las columnas en la sentencia `SELECT`: `SELECT id, nombre, edad, nivel FROM jugadores;`
        2. Utilizar un asterisco (*) como abreviatura: `SELECT * FROM jugadores;`

---
<a id="8"></a>

### Sentencia INSERT INTO SELECT

- **Uso de INSERT INTO SELECT**:
    - La sentencia `INSERT INTO SELECT` se utiliza para recuperar información de una o más tablas y rellenar las columnas de otra tabla.
    - Se consulta una tabla de origen y se insertan los resultados en una tabla de destino.
- **Sintaxis Básica**:
    - La estructura de una sentencia `INSERT INTO SELECT` es:
        
        ```sql
        INSERT INTO nombre_tabla_destino (columna_destino)
        SELECT columna_origen
        FROM nombre_tabla_origen;
        ```
        
- **Ejemplo Práctico**:
    - En una base de datos de club de fútbol, se tienen dos tablas: `jugadores` y `países`.
    - La tabla `jugadores` contiene registros de jugadores y la tabla `países` está vacía y necesita datos.
    - Para llenar la columna `countryName` en la tabla `países` con los datos de la columna `país` en la tabla `jugadores`, se usaría:
        
        ```sql
        INSERT INTO países (countryName)
        SELECT país
        FROM jugadores;
        ```
        

---
<a id="9"></a>

### Ejercicio 2: Practicar la creación de tablas

**Objetivo**

En este ejercicio, aprenderá a practicar la creación de tablas desde cero en una base de datos. El objetivo del ejercicio es crear una tabla en una base de datos para el escenario dado. A continuación, revisará la solución para comprobar y comparar su diseño e implementación de la tabla.

**Escenario**

El Sr. Erik Anderson ha creado un nuevo club de fútbol para niños menores de 16 años.Necesita crear una tabla para almacenar los datos personales básicos de los jugadores, como el número de identidad, el nombre y la edad.

**Instrucciones**

Intente realizar las tareas que se encuentran a continuación antes de avanzar para poder comprobar y comparar sus respuestas con la solución.

Tarea 1: Elabore una base de datos llamada club de fútbol.

Tarea 2: Cree una tabla para almacenar los datos de la siguiente manera

- Identifique un nombre de tabla adecuado para almacenar los datos personales de los jugadores.
- Identifique los atributos y tipos de datos de la tabla.
- Escriba una sentencia SQL para crear la tabla.

**Solución:**

```sql
-- Crear la base de datos
CREATE DATABASE football_club;

-- Usar la base de datos
USE football_club;

-- Crear la tabla devices con las 3 columnas
CREATE TABLE players (
    player_id int,
    player_name varchar(50),
    player_age int)
);

-- Ver tablas
SHOW tables;

-- Ver las columnas
SHOW columns FROM players;
```

**Tarea adicional (opcional)**

El Sr. Anderson quiere crear otra tabla para registrar información sobre los partidos que jugará el equipo, incluyendo el gameID, el resultado de cada partido y las fechas en las que se juegan. Su tarea es crear esta tabla para el club de fútbol

```sql
CREATE TABLE games(
	game_id int,
	game_date DATE
	score INT
);
```

---