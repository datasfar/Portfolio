# Clasificación y filtrado de datos

---

## Índice: 

1. [Cláusula ORDER BY](#1)
2. [Cláusula WHERE](#2)
3. [Ejercicio 1: ORDER BY y WHERE](#3)
4. [Cláusula SELECT DISTINCT](#4)

---
<a id="1"></a>

### Cláusula ORDER BY

- **Propósito de la Cláusula ORDER BY**:
    - Ordenar datos en una tabla mediante una o varias columnas.
    - Puede ordenar en orden ascendente o descendente.
- **Funcionalidad**:
    - Es una cláusula opcional que se agrega a una sentencia SELECT.
    - Ordena los datos por las columnas especificadas.
- **Sintaxis Básica**:
    - Comienza con una sentencia SELECT.
    - Lista de columnas a ordenar.
    - Palabra clave FROM seguida del nombre de la tabla.
    - Cláusula ORDER BY seguida del nombre de la columna a ordenar.
    - Especificar ASC (ascendente) o DESC (descendente).
- **Ordenar por Múltiples Columnas**:
    - Similar a ordenar por una sola columna, pero listando varias columnas separadas por comas.
    - Se puede especificar el orden (ASC o DESC) para cada columna individualmente.
- **Ejemplos Prácticos**:
    - **Ordenar por una Columna**:
        - Ordenar estudiantes por nacionalidad en orden ascendente:
            
            ```sql
            SELECT ID, first_name, last_name, nationality
            FROM students
            ORDER BY nationality ASC;
            ```
            
        - Si se omite ASC, el orden ascendente es el predeterminado.
    - **Ordenar por una Columna en Orden Descendente**:
        - Ordenar estudiantes por nacionalidad en orden descendente:
            
            ```sql
            SELECT ID, first_name, last_name, nationality
            FROM students
            ORDER BY nationality DESC;
            ```
            
    - **Ordenar por Múltiples Columnas**:
        - Ordenar estudiantes por nacionalidad en orden ascendente y fecha de nacimiento en orden descendente:
            
            ```sql
            SELECT ID, first_name, last_name, nationality, birth_date
            FROM students
            ORDER BY nationality ASC, birth_date DESC;
            ```
            
- **Influencia del Tipo de Datos**:
    - Columnas con datos numéricos se ordenan en orden numérico.
    - Columnas con datos de texto se ordenan en orden alfabético.
- **Ejemplo Completo**:
    - Clasificar estudiantes por nacionalidad y luego por fecha de nacimiento:
        
        ```sql
        SELECT ID, first_name, last_name, nationality, birth_date
        FROM students
        ORDER BY nationality ASC, birth_date DESC;
        ```
        

---
<a id="2"></a>

### Cláusula WHERE

**Propósito de la Cláusula WHERE**:

- Filtrar datos en una tabla basado en una condición.
- Se utiliza en sentencias SQL `SELECT`, `UPDATE` y `DELETE`.
- **Operadores de Comparación**:
    - `=`: Igual a.
    - `!=` o `<>`: No igual a.
    - `>`: Mayor que.
    - `<`: Menor que.
    - `>=`: Mayor o igual a.
    - `<=`: Menor o igual a.
    - `!<`: No menor que.
    - `!>`: No mayor que.
- **Operadores Lógicos**:
    - `ALL`: Compara un valor con todos los valores de un conjunto.
    - `AND`: Combina varias condiciones que todas deben ser verdaderas.
    - `ANY`: Compara un valor con cualquier valor en una lista.
    - `BETWEEN`: Busca valores dentro de un rango.
    - `EXISTS`: Verifica la existencia de filas que cumplen con una condición.
    - `IN`: Compara un valor con una lista de valores.
    - `LIKE`: Compara con valores similares usando comodines.
    - `NOT`: Invierte el resultado del operador lógico.
    - `OR`: Combina varias condiciones donde al menos una debe ser verdadera.
    - `IS NULL`: Compara un valor con `NULL`.
    - `UNIQUE`: Busca valores únicos (sin duplicados).
- **Ejemplos de Uso**:
    - Filtrar facturas con un valor total superior a $2:
        
        ```sql
        SELECT * FROM invoices WHERE Total > 2;
        ```
        
    - Filtrar facturas con un valor total superior a $2 y país de facturación EE.UU.:
        
        ```sql
        SELECT * FROM invoices WHERE Total > 2 AND BillingCountry = 'USA';
        ```
        
    - Filtrar facturas con país de facturación EE.UU. o Francia:
        
        ```sql
        SELECT * FROM invoices WHERE BillingCountry = 'USA' OR BillingCountry = 'France';
        ```
        
    - Filtrar facturas con valor total superior a $2 y país de facturación EE.UU. o Francia (usando AND/OR juntos):
        
        ```sql
        SELECT * FROM invoices WHERE Total > 2 AND (BillingCountry = 'USA' OR BillingCountry = 'France');
        ```
        

**Ejemplos Prácticos**

1. **Filtrar por una Condición Simple**
    - **Ejemplo de Filtrado por Texto**:
        
        ```sql
        SELECT *
        FROM student_table
        WHERE facultad = 'Ingeniería';
        ```
        
        - Esta consulta recupera todos los registros de estudiantes de la facultad de ingeniería.
2. **Filtrar por Condición Numérica**
    - **Ejemplo de Filtrado por ID**:
        
        ```sql
        SELECT *
        FROM student_table
        WHERE student_id = 01;
        ```
        
        - Recupera el registro del estudiante con el ID igual a 01.
3. **Utilizar Operadores de Comparación**
    - **Mayor que**:
        
        ```sql
        SELECT *
        FROM student_table
        WHERE edad > 20;
        ```
        
    - **Menor que**:
        
        ```sql
        SELECT *
        FROM student_table
        WHERE edad < 25;
        ```
        
    - **Mayor o igual que**:
        
        ```sql
        SELECT *
        FROM student_table
        WHERE edad >= 18;
        ```
        
    - **Menor o igual que**:
        
        ```sql
        SELECT *
        FROM student_table
        WHERE edad <= 22;
        ```
        
    - **No igual a**:
        
        ```sql
        SELECT *
        FROM student_table
        WHERE facultad != 'Ciencias';
        ```
        
4. **Operador BETWEEN**
    - Filtrar por Rango de Fechas:
        
        ```sql
        SELECT *
        FROM student_table
        WHERE DOB BETWEEN '2010-01-01' AND '2010-05-30';
        ```
        
        - Recupera los registros de estudiantes nacidos entre el 1 de enero de 2010 y el 30 de mayo de 2010.
5. **Operador LIKE**
    - Filtrar por un Patrón de Texto:
        
        ```sql
        SELECT *
        FROM student_table
        WHERE facultad LIKE 'Sc%';
        ```
        
        - Recupera registros donde el valor de la columna facultad comienza con "Sc".
6. **Operador IN**
    - Filtrar por Múltiples Valores:
        
        ```sql
        SELECT *
        FROM student_table
        WHERE country IN ('USA', 'UK');
        ```
        
        - Recupera registros de estudiantes cuya columna país es "USA" o "UK".

---
<a id="3"></a>

### Ejercicio 1: ORDER BY y WHERE

**Objetivos**

1. Utilice la cláusula SQL ORDER BY para ordenar el resultado de una consulta

2. Utilice la cláusula SQL WHERE para especificar una condición para el filtrado de registros

**El ejemplo de base de datos de chinook**

En este ejercicio vamos a considerar la conocida base de datos “chinook sample”, muy utilizada para demostraciones y pruebas. Además, se ha implementado en la plataforma Coursera, con la que es bueno estar familiarizado ya que la va a utilizar para completar este ejercicio.

La base de datos de ejemplo de chinook consiste en el siguiente esquema de base de datos.

![Untitled](/courses/databases/Clasificacio%CC%81n%20y%20filtrado%20de%20datos%208b91c10149544b258487e8b7323dce7b/Untitled.png)

**Código para la creación de la base de datos:**

```sql
-- Creación de la base de datos
CREATE DATABASE Chinook;
USE Chinook;

-- Creación de la tabla 
CREATE TABLE Customer (CustomerId INT NOT NULL, FirstName VARCHAR(40) NOT NULL, LastName VARCHAR(20) NOT NULL, Company VARCHAR(80), Address VARCHAR(70), City VARCHAR(40), State VARCHAR(40), Country VARCHAR(40), PostalCode VARCHAR(10), Phone VARCHAR(24), Fax VARCHAR(24), Email VARCHAR(60) NOT NULL, SupportRepId INT, CONSTRAINT PK_Customer PRIMARY KEY (CustomerId));

-- Inserción de los datos
INSERT INTO Customer (CustomerId, FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email, SupportRepId) VALUES (1, 'Luís', 'Gonçalves', 'Embraer - Empresa Brasileira de Aeronáutica S.A.', 'Av. Brigadeiro Faria Lima, 2170', 'São José dos Campos', 'SP', 'Brazil', '12227-000', '+55 (12) 3923-5555', '+55 (12) 3923-5566', 'luisg@embraer.com.br', 3);

INSERT INTO Customer (CustomerId, FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email, SupportRepId) VALUES (2, 'Eduardo', 'Martins', 'Woodstock Discos', 'Rua Dr. Falcão Filho, 155', 'São Paulo', 'SP', 'Brazil', '01007-010', '+55 (11) 3033-5446', '+55 (11) 3033-4564', 'eduardo@woodstock.com.br', 4);

INSERT INTO Customer (CustomerId, FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email, SupportRepId) VALUES
(3, 'Alexandre', 'Rocha', 'Banco do Brasil S.A.', 'Av. Paulista, 2022', 'São Paulo', 'SP', 'Brazil', '01310-200', '+55 (11) 3055-3278', '+55 (11) 3055-8131', 'alero@uol.com.br', 5);

INSERT INTO Customer (CustomerId, FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email, SupportRepId) VALUES
(4, 'Roberto', 'Almeida', 'Riotur', 'Praça Pio X, 119', 'Rio de Janeiro', 'RJ', 'Brazil', '20040-020', '+55 (21) 2271-7000', '+55 (21) 2271-7070', 'roberto.almeida@riotur.gov.br', 3);

INSERT INTO Customer (CustomerId, FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email, SupportRepId) VALUES (5, 'Mark', 'Philips', 'Telus', '8210 111 ST NW', 'Edmonton', 'AB', 'Canada', 'T6G 2C7', '+1 (780) 434-4554', '+1 (780) 434-5565', 'mphilips12@shaw.ca', 5);

INSERT INTO Customer (CustomerId, FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email, SupportRepId) VALUES (6, 'Jennifer', 'Peterson', 'Rogers Canada', '700 W Pender Street', 'Vancouver', 'BC', 'Canada', 'V6C 1G8', '+1 (604) 688-2255', '+1 (604) 688-8756', 'jenniferp@rogers.ca', 3); 
```

**Instrucciones**

Tarea 1: Escriba una sentencia SQL para mostrar todos los datos existentes en la tabla de clientes.

```sql
SELECT CustomerID, FirstName, LastName, City, State, Country FROM Customer;
```

Tarea 2: Escriba una sentencia SQL para ordenar el conjunto de resultados en orden ascendente por nombre.

```sql
SELECT CustomerID, FirstName, LastName, City, State, Country 
FROM Customer 
ORDER BY FirstName;
```

Tarea 3: Filtre los datos del conjunto de resultados basándose en una condición donde país = Francia.

```sql
SELECT *
FROM Customer
WHERE Country = 'France'
ORDER BY FirstName;
```

**Ejercicio adicional (opcional)**

Tiene que escribir una sentencia SQL para mostrar sólo el nombre y el país de los clientes de Canadá.

```sql
SELECT FirstName, Country
FROM Customer
WHERE Country = 'Canada'
ORDER BY FirstName;
```

---
<a id="4"></a>

### Cláusula SELECT DISTINCT

- **Propósito de `SELECT DISTINCT`**:
    - La sentencia `SELECT DISTINCT` se usa en SQL para obtener resultados únicos sin duplicados en una consulta. Es útil para listar diferentes valores sin repeticiones.
- **Uso Básico**:
    - Para obtener una lista de países distintos de una tabla de estudiantes, se puede usar `SELECT DISTINCT país FROM estudiantes`. Esto elimina duplicados y muestra solo una vez cada país.
- **Aplicación con Varias Columnas**:
    - Al usar `SELECT DISTINCT` con varias columnas, como `SELECT DISTINCT facultad, país FROM estudiantes`, se obtienen combinaciones únicas de los valores en esas columnas.
- **Manejo de Valores `NULL`**:
    - `SELECT DISTINCT` considera los valores `NULL` como únicos. Si una columna tiene valores `NULL`, se incluyen en los resultados distintos como una entrada separada.

**Ejemplos de uso:**

- **Ejemplo Básico con Una Columna**:
    
    ```sql
    SELECT DISTINCT país
    FROM estudiantes;
    ```
    
    - Esta consulta devuelve una lista de todos los países representados en la tabla de estudiantes, eliminando cualquier duplicado.
- **Ejemplo con Varias Columnas**:
    
    ```sql
    SELECT DISTINCT facultad, país
    FROM estudiantes;
    ```
    
    - Esta consulta devuelve combinaciones únicas de facultad y país. Esto muestra qué combinaciones de facultades y países están representadas en la tabla, eliminando duplicados en la combinación de ambas columnas.
- **Ejemplo con Valores `NULL`**:
    
    ```sql
    SELECT DISTINCT facultad, país
    FROM estudiantes;
    ```
    
    - Si hay registros con valores `NULL` en la columna facultad, `DISTINCT` los considerará únicos. Por ejemplo, si Julia Smith tiene `NULL` en facultad y EE. UU. en país, la combinación (`NULL`, `EE. UU.`) se tratará como un valor distinto y aparecerá en los resultados.

---