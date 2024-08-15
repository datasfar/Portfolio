# Introdución a SQL

---

## Índice: 

1. [¿Qué es el lenguaje de consultas estructurado?](#1)
2. [Uso de SQL](#2)
3. [Ventajas de SQL](#3)
4. [Introducción a la sintaxis de SQL](#4)
5. [Comandos SQL más comunes](#5)


---
<a id="1"></a>

### ¿Qué es el lenguaje de consultas estructurado?

- **Interacción con Bases de Datos**:
    - Los ingenieros de datos interactúan con bases de datos utilizando SQL (Structured Query Language).
    - SQL se pronuncia "sequel".
- **Operaciones CRUD**:
    - **CRUD** es un acrónimo para **Create, Read, Update, y Delete**, que son las operaciones básicas que se realizan en los datos de una base de datos.
- **Uso de SQL**:
    - **SQL** es el **lenguaje estándar para interactuar con todas las bases de datos.**
    - Es especialmente útil para bases de datos relacionales que manejan datos estructurados.
    - Ejemplos de bases de datos relacionales que usan SQL incluyen MySQL, PostgreSQL, Oracle, y Microsoft SQL Server.
- **DBMS (Sistema de Gestión de Bases de Datos)**:
    - Un **DBMS interpreta y ejecuta instrucciones SQL**.
    - Los desarrolladores web ejecutan instrucciones SQL en una base de datos utilizando un DBMS.
    - El DBMS transforma las instrucciones SQL en un formulario que la base de datos subyacente puede comprender.
    

---
<a id="2"></a>

### Uso de SQL

- SQL se divide en varios sublenguajes: **DDL, DML, DQL y DCL**.

- **DDL (Lenguaje de Definición de Datos)**:
    - Utilizado para definir y estructurar la base de datos.
    - Comandos principales:
        - `CREATE`: Crear bases de datos y tablas.
        - `ALTER`: Modificar la estructura de tablas existentes.
        - `DROP`: Eliminar objetos de la base de datos.
        
- **DML (Lenguaje de Manipulación de Datos)**:
    - Utilizado para manipular datos dentro de las tablas.
    - Comandos principales:
        - `INSERT`: Agregar datos a una tabla.
        - `UPDATE`: Modificar datos existentes.
        - `DELETE`: Eliminar datos de una tabla.
        
- **DQL (Lenguaje de Consulta de Datos)**:
    - Utilizado para consultar y recuperar datos de la base de datos.
    - Comando principal:
        - `SELECT`: Recuperar datos de una o más tablas, especificando los campos y criterios de filtrado.
        
- **DCL (Lenguaje de Control de Datos)**:
    - Utilizado para controlar el acceso a la base de datos.
    - Comandos principales:
        - `GRANT`: Otorgar privilegios de acceso a los usuarios.
        - `REVOKE`: Revocar privilegios de acceso otorgados previamente.
        

---
<a id="3"></a>

### Ventajas de SQL

- **Simplicidad y Facilidad de Uso**:
    - Requiere pocas habilidades de codificación.
    - Usa un conjunto de palabras clave simples para realizar operaciones CRUD.
- **Interactividad**:
    - Permite escribir consultas complejas rápidamente.
- **Estándar y Compatible**:
    - Funciona con todas las bases de datos relacionales, como MySQL.
    - Amplia disponibilidad de asistencia e información.
- **Portabilidad**:
    - El código SQL se puede ejecutar en cualquier hardware, sistema operativo o plataforma.
    - El mismo código se puede usar en entornos de escritorio y servidores de producción.
- **Integridad**:
    - Cubre todas las áreas de administración de bases de datos.
    - Permite crear bases de datos, insertar, actualizar, eliminar, recuperar y compartir datos, y administrar la seguridad de la base de datos.
- **Eficiencia**:
    - Permite procesar grandes cantidades de datos rápida y eficientemente.
    

---
<a id="4"></a>

### Introducción a la sintaxis SQL

- **Creación de una Base de Datos con DDL**:
    - **Crear Base de Datos**: Usar `CREATE DATABASE nombre_base_datos;` para crear una base de datos.
    - **Crear Tablas**: Usar `CREATE TABLE nombre_tabla (...);` para crear tablas dentro de la base de datos.
    
- **Manipulación de Datos con DML**:
    - **Insertar Datos**: Usar `INSERT INTO nombre_tabla (columnas) VALUES (valores);` para agregar datos a una tabla.
    - **Actualizar Datos**: Usar `UPDATE nombre_tabla SET columna = valor WHERE condición;` para modificar datos existentes en una tabla.
    - **Eliminar Datos**: Usar `DELETE FROM nombre_tabla WHERE condición;` para eliminar datos de una tabla.
    
- **Consulta de Datos con DQL**:
    - **Seleccionar Datos**: Usar `SELECT columnas FROM nombre_tabla WHERE condición;` para leer y recuperar datos de la base de datos.
    

---
<a id="5"></a>

### Comandos SQL más comunes

- **Lenguaje de Definición de Datos (DDL)**
    - **CREATE**: Crea una base de datos o tablas.
        
        ```sql
        CREATE TABLE table_name (
            column_name1 datatype(size),
            column_name2 datatype(size),
            column_name3 datatype(size)
        );
        ```
        
    - **DROP**: Elimina una base de datos o tablas.
        
        ```sql
        DROP TABLE table_name;
        ```
        
    - **ALTER**: Modifica la estructura de una tabla, como agregar una columna o clave principal.
        
        ```sql
        ALTER TABLE table_name ADD (column_name datatype(size));
        ALTER TABLE table_name ADD primary key (column_name);
        ```
        
    - **TRUNCATE**: Elimina todos los registros de una tabla.
        
        ```sql
        TRUNCATE TABLE table_name
        ```
        
    - **COMMENT**: Añade comentarios en las sentencias SQL.
        
        ```sql
        -- Recuperar todos los datos de una tabla
        SELECT * FROM table_name;
        ```
        

- **Lenguaje de Manipulación de Datos (DML)**
    - **SELECT**: Recupera datos de tablas.
        
        ```sql
        SELECT * FROM table_name
        ```
        
    - **INSERT**: Añade registros de datos a una tabla.
        
        ```sql
        INSERT INTO table_name (column1, column2, column3) VALUES (value1, value2, value3);
        ```
        
    - **UPDATE**: Modifica o actualiza datos en una tabla.
        
        ```sql
        UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
        ```
        
    - **DELETE**: Elimina datos de una tabla.
        
        ```sql
        DELETE FROM table_name WHERE condition;
        ```
        

- **Lenguaje de Control de Datos (DCL)**
    - **GRANT**: Proporciona privilegios a los usuarios para acceder y manipular la base de datos.
    - **REVOKE**: Quita permisos a los usuarios.
    
- **Lenguaje de Control de Transacciones (TCL)**
    - **COMMIT**: Guarda todos los cambios realizados en la base de datos.
    - **ROLLBACK**: Restaura la base de datos al último estado confirmado.
    

---