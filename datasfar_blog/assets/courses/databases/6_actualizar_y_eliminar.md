# Actualizar y eliminar

---

## Índice: 

1. [Actualización de datos](#1)
2. [Eliminación de datos](#2)
3. [Ejercicio 1: Eliminación de registros](#3)

---
<a id="1"></a>

### Actualización de datos

- La cláusula `UPDATE` se utiliza para modificar datos existentes en una tabla de base de datos.
- **Sintaxis Básica de UPDATE**:
    - La estructura básica de la sentencia `UPDATE` es:
        
        ```sql
        UPDATE nombre_tabla
        SET columna1 = valor1, columna2 = valor2, ...
        WHERE condición;
        ```
        
    - Se especifica la tabla a actualizar, las columnas a modificar con sus nuevos valores, y una condición para identificar los registros a actualizar.
- **Ejemplo Práctico - Actualización de un Registro**:
    - Para actualizar el domicilio y el número de contacto de un estudiante con ID 3:
        
        ```sql
        UPDATE tabla_estudiantes
        SET domicilio = 'nuevo_domicilio', numero_contacto = 'nuevo_numero'
        WHERE ID = 3;
        ```
        
    - Se utiliza `UPDATE` seguido del nombre de la tabla, `SET` seguido de las columnas y sus nuevos valores, y `WHERE` para especificar el registro con ID 3.
- **Confirmación de la Actualización**:
    - Después de ejecutar la sentencia, se recibe una confirmación y se verifica en la tabla que los valores han sido actualizados.
- **Actualización de Múltiples Registros**:
    - La sentencia `UPDATE` también puede actualizar varios registros a la vez.
    - Ejemplo para actualizar la dirección del departamento de ingeniería a "Harper Building":
        
        ```sql
        UPDATE tabla_estudiantes
        SET direccion_universidad = 'Harper Building'
        WHERE departamento = 'Ingeniería';
        ```
        
- **Actualizar Varios Valores en Varios Registros**:
    - Es posible actualizar múltiples columnas en varios registros en una sola sentencia `UPDATE`.
    - Ejemplo de actualización de la dirección y el número de contacto:
        
        ```sql
        UPDATE tabla_estudiantes
        SET direccion_universidad = 'Harper Building', domicilio = 'nuevo_domicilio'
        WHERE departamento = 'Ingeniería';
        ```
        
    - Se agregan múltiples pares de columna-valor en la cláusula `SET`, separados por comas.

---
<a id="2"></a>

### Eliminación de datos

- **Eliminación de un Solo Registro**:
    - **Comando Básico**: La sentencia para eliminar un registro comienza con la palabra clave `DELETE`.
    - **Especificación de la Tabla**: Se debe especificar el nombre de la tabla con la que se está trabajando, por ejemplo, `tabla_estudiantes`.
    - **Cláusula WHERE**: Se utiliza la cláusula `WHERE` para definir la condición que debe cumplir el registro a eliminar. Por ejemplo, para eliminar un registro con el apellido "Miller":
        
        ```sql
        DELETE FROM tabla_estudiantes
        WHERE apellido = 'Miller';
        ```
        
    - **Ejecución y Confirmación**: La sentencia se ejecuta y se recibe una confirmación de la eliminación. Luego, se verifica en la tabla que el registro ha sido eliminado.
- **Eliminación de Múltiples Registros**:
    - **Comando Similar**: La sentencia comienza igual que para un solo registro, con `DELETE` y el nombre de la tabla.
    - **Condición de Múltiples Registros**: La cláusula `WHERE` se ajusta para eliminar todos los registros que cumplan con una condición específica. Por ejemplo, para eliminar todos los estudiantes del departamento de ingeniería:
        
        ```sql
        DELETE FROM tabla_estudiantes
        WHERE departamento = 'Ingeniería';
        ```
        
    - **Precaución con WHERE**: Es crucial especificar correctamente la cláusula `WHERE` para evitar eliminar todos los registros de la tabla.
- **Eliminación de Todos los Registros**:
    - **Comando General**: Para eliminar todos los registros de una tabla, se omite la cláusula `WHERE`.
    - **Sintaxis Simplificada**: La sentencia se reduce a:
        
        ```sql
        DELETE FROM tabla_estudiantes;
        ```
        
    - **Ejecución y Verificación**: Después de ejecutar la sentencia, se confirma la eliminación y se verifica que la tabla está vacía.

---
<a id="3"></a>

### Ejercicio 1: Eliminación de registros

**Objetivo**

El objetivo de este ejercicio es enseñarle a eliminar registros. Tendrá la oportunidad de practicar la eliminación de un registro de una tabla de una base de datos.

**Escenario**

El Sr. John Ericson es propietario de una pequeña librería. La base de datos de su librería incluye una tabla “Clientes” que contiene los datos de los clientes de la librería. La siguiente imagen muestra todos los registros de datos almacenados en la tabla de clientes.

![Untitled](/courses/databases/Actualizar%20y%20eliminar%20896fc34247b24be9950885b8593a3c6d/Untitled.png)

El Sr. Ericson quiere eliminar el registro de cliente de Jimmy con el ID número 3. Los siguientes pasos lo guiarán a través del proceso para eliminar el registro de Jimmy de la base de datos de la librería.

1. Escriba el comando "DELETE", seguido de la palabra clave FROM para identificar la tabla de origen que contiene los registros. En este caso, el nombre de la tabla se llama tabla “clientes”.
2. Escriba la cláusula WHERE seguida del estado para especificar el registro que desea eliminar. La condición debe ser WHERE IDdelcliente = 3. La sintaxis completa es la siguiente:

**Punto de partida:**

```sql
-- Crear la base de datos
CREATE DATABASE bookshop;

-- Usar la base de datos
USE bookshop;

-- Crear la tabla devices con las 3 columnas
CREATE TABLE customers (
    customerID int,
    customerName varchar(50),
    customerAddress varchar(255)
);

-- Insertar datos
INSERT INTO `customers` (`customerID`, `customerName`, `customerAddress`) VALUES
(1, 'Jack', '115 Old street Belfast'),
(2, 'James', '24 Carlson Rd London'),
(4, 'Maria', '5 Fredrik Rd, Bedford'),
(5, 'Jade', '10 Copland Ave Portsmouth'),
(6, 'Yasmine', '15 Fredrik Rd, Bedford'),
(3, 'Jimmy', '110 Copland Ave Portsmouth');
```

**Solución:**

```sql
-- Delete
DELETE FROM customers WHERE customerID = 3;

-- Ver los registros 
SELECT * FROM customers;
```

**Tarea adicional (opcional)**

El Sr. Ericson quiere eliminar el registro de Yasmine. Su tarea ahora es eliminar los detalles de este cliente de la tabla de clientes.

**Solución:**

```sql
-- Delete
DELETE FROM customers WHERE customerName = "Yasmine";

-- Ver los registros 
SELECT * FROM customers;
```

---