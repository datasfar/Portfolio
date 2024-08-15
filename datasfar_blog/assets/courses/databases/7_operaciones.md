# Operaciones SQL

---

## Índice: 

1. [Operadores artiméticos SQL](#1)
2. [Ejemplo con operadores aritmeticos](#2)
3. [Operadores de comparación](#3)
4. [Ejemplo con operadores de comparación](#4)

---
<a id="1"></a>

### Operadores aritméticos SQL

- **Contexto y Uso de Operadores en SQL**:
    - Las bases de datos corporativas manejan información de empleados, lo que requiere cálculos precisos y eficientes.
    - SQL permite realizar ajustes como aumentos salariales y cambios en deducciones usando operadores aritméticos.
    - Comprender y utilizar operadores aritméticos en SQL es crucial para manipular datos en bases de datos.
- **Definición y Tipos de Operadores**:
    - Los operadores en SQL son palabras o caracteres que facilitan diversas actividades en una base de datos.
    - Son esenciales para consultar y manipular datos para distintos propósitos.
    - Ejemplos de uso: calcular días de licencia restantes o verificar si los empleados cumplen con los objetivos de la empresa.
- **Operadores Aritméticos en SQL**:
    - Se utilizan para realizar cálculos matemáticos en una base de datos.
    - Símbolos:
        - `+` para la suma,
        - `-` para la resta,
        - `*` para la multiplicación,
        - `/` para la división,
        - `%` para el módulo (resto de una división).
- **Funcionamiento de Operadores Aritméticos**:
    - Un operador toma dos operandos y devuelve un resultado (ej.: 5 + 5 = 10).
    - El comando `SELECT` en SQL permite realizar estas operaciones.
    - Ejemplos prácticos:
        - Suma: `SELECT 10 + 15;` -> Resultado: 25.
        - Resta: `SELECT 10 - 10;` -> Resultado: 0.
        - Multiplicación: `SELECT 5 * 5;` -> Resultado: 25.
        - División: `SELECT 5 / 5;` -> Resultado: 1.
        - Módulo: `SELECT 5 % 5;` -> Resultado: 0.

---
<a id="2"></a>

### Ejemplos con operadores aritméticos

Partiremos de la siguiente tabla:

![Untitled](/courses/databases/Operaciones%20SQL%209805ae0bd155427c99770ab470aa55d7/Untitled.png)

- **Operador de Suma**:
    - Sumar valores de dos columnas:
        
        ```sql
        SELECT column_name1 + column_name2 FROM table_name;
        ```
        
    - Ejemplo con tabla de empleados para sumar salario y deducción:
        
        ```sql
        SELECT salary + allowance FROM employee;
        ```
        
    - Filtrar empleados con un salario total específico usando `WHERE`:
        
        ```sql
        SELECT * FROM employee WHERE salary + allowance = 25000;
        ```
        
- **Operador de Resta**:
    - Restar valores de una columna a otra:
        
        ```sql
        SELECT column_name1 - column_name2 FROM table_name;
        ```
        
    - Ejemplo para restar impuestos del salario:
        
        ```sql
        SELECT salary - tax FROM employee;
        ```
        
    - Filtrar empleados con un salario después de impuestos específico:
        
        ```sql
        SELECT * FROM employee WHERE salary - tax = 50000;
        ```
        
- **Operador de Multiplicación**:
    - Multiplicar valores de dos columnas:
        
        ```sql
        SELECT column_name1 * column_name2 FROM table_name;
        ```
        
    - Ejemplo para duplicar el impuesto:
        
        ```sql
        SELECT tax * 2 FROM employee;
        ```
        
    - Filtrar empleados con un impuesto duplicado específico:
        
        ```sql
        SELECT * FROM employee WHERE tax * 2 = 4000;
        ```
        
- **Operador de División**:
    - Dividir valores de una columna por otra:
        
        ```sql
        SELECT column_name1 / column_name2 FROM table_name;
        ```
        
    - Ejemplo para calcular el porcentaje de deducción:
        
        ```sql
        SELECT allowance / salary * 100 FROM employee;
        ```
        
    - Filtrar empleados con una deducción mínima específica:
        
        ```sql
        SELECT * FROM employee WHERE allowance / salary * 100 >= 5;
        ```
        
- **Operador de Módulo**:
    - Dar el resto de la división de valores de dos columnas:
        
        ```sql
        SELECT column_name1 % column_name2 FROM table_name;
        ```
        
    - Ejemplo para verificar si las horas trabajadas son pares:
        
        ```sql
        SELECT hours % 2 FROM employee;
        ```
        
    - Filtrar empleados con un número par de horas trabajadas:
        
        ```sql
        SELECT * FROM employee WHERE hours % 2 = 0;
        ```
        

---
<a id="3"></a>

### Operadores de comparación SQL

**Contexto y uso:**

- Los operadores de comparación se utilizan para clasificar y gestionar datos en una base de datos.
- Los operadores de comparación permiten comparar dos valores o expresiones, resultando en verdadero o falso.
- Se utilizan para filtrar, incluir y excluir datos.
- **Operadores de comparación en SQL**:
    - **Igual a (=)**: Se usa para verificar si los valores en una columna son iguales a un valor específico.
        - Ejemplo: `SELECT * FROM employee WHERE salary = 18000;`
    - **Menor que (<)**: Se usa para identificar valores menores que un valor específico.
        - Ejemplo: `SELECT * FROM employee WHERE salary < 24000;`
    - **Menor o igual que (<=)**: Se utiliza para identificar valores que son menores o iguales a un valor específico.
        - Ejemplo: `SELECT * FROM employee WHERE salary <= 24000;`
    - **Mayor o igual que (>=)**: Se utiliza para identificar valores que son mayores o iguales a un valor específico.
        - Ejemplo: `SELECT * FROM employee WHERE salary >= 24000;`
    - **No igual a (<> o !=)**: Se usa para identificar valores que no son iguales a un valor específico.
        - Ejemplo: `SELECT * FROM employee WHERE salary <> 24000;`

---
<a id="4"></a>

### Ejemplos de operadores de comparación

Partiremos de la siguiente tabla:

![Untitled](/courses/databases/Operaciones%20SQL%209805ae0bd155427c99770ab470aa55d7/Untitled%201.png)

- **Igualdad**:
    - Filtrar datos del empleado con ID igual a 1:
        
        ```sql
        SELECT * FROM employee WHERE employee_id = 1;
        ```
        
    - Filtrar datos del empleado cuyo nombre es "James":
        
        ```sql
        SELECT * FROM employee WHERE employee_name = 'James';
        ```
        
- **Desigualdad**:
    - Determinar empleados con salario distinto de 24,000:
        
        ```sql
        SELECT * FROM employee WHERE salary <> 24000;
        ```
        
- **Mayor que**:
    - Filtrar empleados con salario superior a 50,000:
        
        ```sql
        SELECT * FROM employee WHERE salary > 50000;
        ```
        
- **Mayor o Igual que**:
    - Determinar empleados que pagan impuestos de 1,000 o más:
        
        ```sql
        SELECT * FROM employee WHERE tax >= 1000;
        ```
        
- **Menor que**:
    - Determinar empleados con deducción inferior a 2,500:
        
        ```sql
        SELECT * FROM employee WHERE allowance < 2500;
        ```
        
- **Menor o Igual que**:
    - Filtrar empleados que han trabajado 10 horas o menos:
        
        ```sql
        SELECT * FROM employee WHERE hours <= 10;
        ```
        

---