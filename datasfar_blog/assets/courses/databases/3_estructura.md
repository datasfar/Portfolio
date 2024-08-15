# Estructura básica de la base de datos

---

## Índice: 

1. [¿Qué son las tablas en las bases de datos?](#1)
2. [Resumen de las tablas](#2)
3. [Resumen de la estructura de una base de datos](#3)
4. [Tipos de claves en una tabla de base de datos](#4)
5. [Diseño básico de bases de datos](#5)


---
<a id="1"></a>

### ¿Qué son las tablas en las bases de datos?

- **Tablas de Base de Datos**: Se componen de filas y columnas que contienen datos. Una base de datos contiene múltiples tablas, también conocidas como relaciones, ya que están relacionadas entre sí.
- **Entidades y Objetos**: En un sentido conceptual, **una tabla se conoce como entidad** u objeto en una base de datos orientada a objetos (OODB). Las columnas o campos de una tabla son los atributos de esa entidad u objeto.
- **Columnas (Atributos)**: Cada columna tiene un nombre y un tipo de datos únicos. Los tipos de datos pueden ser numéricos, de cadena, de fecha y hora, o binarios. Estos tipos de datos varían según el sistema de base de datos (por ejemplo, MySQL, SQL Server).
- **Filas (Registros)**: **Cada fila es un registro único** que contiene una combinación de columnas o campos con datos. Un registro es una representación única de una entidad.
- **Dominios**: **Un dominio es el conjunto de valores legales que se puede asignar a un atributo**, asegurando que los valores en el campo estén bien definidos y adecuados (por ejemplo, solo números en un dominio numérico).
- **Clave Primaria**: Una **columna con valores únicos** que identifica de forma única cada registro en una tabla. En caso de que una sola columna no tenga valores únicos, la clave primaria puede ser una combinación de columnas.

---
<a id="2"></a>

### Resumen de las tablas

- **Tablas**: Son el objeto más básico en una base de datos relacional, responsables de almacenar datos. Se componen de filas (registros) y columnas (atributos o campos).

**Estructura de una Tabla:**

- **Filas**: Representan cada registro y abarcan varias columnas.
- **Columnas**: Definen cada campo y tienen un nombre y un tipo de datos únicos (por ejemplo, `FirstName`, `LastName`, `ProductID`, `Price`).
- **Celdas**: El punto donde se cruza una fila con una columna, almacenando un elemento de datos específico.

**Tipos de Datos:**

- **Numéricos**: `INT`, `TINYINT`, `BIGINT`, `FLOAT`, `REAL`.
- **Fecha y Hora**: `DATE`, `TIME`, `DATETIME`.
- **Cadenas**: `CHAR`, `VARCHAR`.
- **Binarios**: `BINARY`, `VARBINARY`.
- **Otros**:
    - **CLOB**: Almacena grandes bloques de texto.
    - **BLOB**: Almacena datos binarios, como imágenes.
    

**Claves en una Tabla:**

- **Clave Principal (Primary Key)**: Identifica de manera única una fila en una tabla. Ejemplo: `StudentID` en una tabla de estudiantes.

![Untitled](/courses/databases/Estructura%20ba%CC%81sica%20de%20la%20base%20de%20datos%2094a3d4b7642b4a48871cab4af9069dcb/Untitled.png)

- **Clave Principal Compuesta**: Cuando una sola columna no es suficiente, se utilizan múltiples columnas para crear una clave principal.
    
    ![Untitled](/courses/databases/Estructura%20ba%CC%81sica%20de%20la%20base%20de%20datos%2094a3d4b7642b4a48871cab4af9069dcb/Untitled%201.png)
    
- **Clave Externa (Foreign Key)**: Vincula tablas entre sí usando una columna clave principal de una tabla que también está presente en la tabla relacionada.

![Untitled](/courses/databases/Estructura%20ba%CC%81sica%20de%20la%20base%20de%20datos%2094a3d4b7642b4a48871cab4af9069dcb/Untitled%202.png)

**Esquema de una Tabla:**

- **Nombre de la Tabla**: El identificador de la tabla.
- **Atributos**: Los nombres de las columnas y sus tipos de datos.

**Restricciones de Integridad:**

- **Restricciones de Claves**: Aseguran que una o varias columnas se puedan usar para identificar datos de cualquier fila (clave principal). Estos valores no deben ser `NULL` ni repetidos.
- **Restricciones de Dominio**: Definen las reglas para los valores que se pueden almacenar en una columna (por ejemplo, un número de contacto debe tener 10 dígitos).
- **Restricciones de Integridad Referencial**: Garantizan que el valor de una columna clave externa en una tabla debe existir en la tabla referenciada.

**Importancia de las Claves y Relaciones:**

- **Claves Primarias**: Garantizan la unicidad de cada registro.
- **Claves Externas**: Crean relaciones entre tablas, esencial para la integridad referencial y la estructura lógica de la base de datos.

---
<a id="3"></a>

### Resumen de estructura de una base de datos

- **Estructura de Base de Datos**: Organización de los datos en una base de datos, agrupados en tablas que consisten en filas (tuplas) y columnas (atributos).

**Estructura Lógica de la Base de Datos:**

- **Diagrama Entidad-Relación (ERD)**: Representación visual de cómo se implementará la base de datos en tablas, mostrando las relaciones entre entidades.
- **Relaciones**:
    - **Uno a Uno**: Una entidad se relaciona con una única entidad de otra tabla.
    - **Uno a Muchos**: Una entidad se relaciona con múltiples entidades de otra tabla.
    - **Muchos a Muchos**: Varias entidades se relacionan con múltiples entidades de otra tabla.

![Untitled](/courses/databases/Estructura%20ba%CC%81sica%20de%20la%20base%20de%20datos%2094a3d4b7642b4a48871cab4af9069dcb/Untitled%203.png)

**Estructura Física de la Base de Datos:**

- **Tablas**: Implementación de entidades como tablas en el diseño físico.
- **Claves Externas**: Campos en una tabla que hacen referencia a la clave principal de otra tabla para establecer relaciones.

![Untitled](/courses/databases/Estructura%20ba%CC%81sica%20de%20la%20base%20de%20datos%2094a3d4b7642b4a48871cab4af9069dcb/Untitled%204.png)

---

<a id="4"></a>

### Tipos de claves en una tabla de base de datos

- **Modelo de Base de Datos Relacional**:
    - Comprende cómo se relacionan las tablas usando claves.
    - Se basa en dos conceptos principales: entidades (tablas) y relaciones (vínculos entre tablas).
    
- **Tablas y Atributos en Bases de Datos**:
    - Ejemplo de competencia deportiva con tres tablas: liga, equipos y puntos.
    
    ![Untitled](/courses/databases/Estructura%20ba%CC%81sica%20de%20la%20base%20de%20datos%2094a3d4b7642b4a48871cab4af9069dcb/Untitled%205.png)
    
    - Las columnas de cada tabla representan atributos de la entidad.
    - Los atributos pueden ser simples (un único valor) o multivalor (múltiples valores, que deben evitarse).
    
- **Tipos de Claves en Bases de Datos Relacionales**:
    - **Clave Primaria**: Identifica de forma única un registro en una tabla (e.g., ID del personal).
    - **Clave Candidata**: Cualquier atributo con un valor único en cada fila (e.g., ID del personal, números de contacto).
    - **Clave Compuesta**: Formada por dos o más atributos para crear un valor único (e.g., nombre y cargo del personal).
    - **Clave Alternativa (Secundaria)**: Clave candidata que no se seleccionó como clave primaria (e.g., número de contacto).
    - **Clave Externa**: Atributo que referencia una clave única en otra tabla (e.g., ID del personal como clave externa en otras tablas).
    
- **Relaciones Entre Claves**:
    - Claves primarias y externas crean vínculos entre tablas.
    

---
<a id="5"></a>

### Diseño básico de bases de datos

**Principios de un Buen Diseño de Base de Datos**

- **Evitar Datos Redundantes:** La información duplicada desperdicia espacio y puede causar errores e inconsistencias.
- **Asegurar la Exactitud de los Datos:** La corrección y la completitud de los datos son cruciales para generar informes fiables y tomar decisiones informadas.

**Pasos en el Proceso de Diseño**

1. **Determinar el Propósito:** Definir claramente el propósito de la base de datos y cómo se usará.
2. **Organizar la Información:** Reunir y listar todos los tipos de información necesarios.
3. **Dividir la Información en Tablas:** Agrupar la información relacionada en tablas basadas en temas.
4. **Convertir la Información en Columnas:** Decidir qué datos específicos debe contener cada tabla, convirtiendo estos puntos de datos en campos.
5. **Especificar Claves Primarias:** Elegir un identificador único para los registros de cada tabla para asegurar que cada registro pueda identificarse de manera única.
6. **Establecer Relaciones entre Tablas:** Definir cómo se relacionan las tablas entre sí y refinar el diseño para eliminar cualquier error.
7. **Aplicar las Reglas de Normalización:** Asegurar que las tablas estén estructuradas correctamente para minimizar la redundancia y la dependencia.

**Determinar el Propósito de la Base de Datos**

- Escribir el propósito de la base de datos ayuda a enfocarse en los objetivos y tomar decisiones informadas durante el proceso de diseño.

**Organizar la Información Requerida**

- Usar documentos existentes o imaginar formularios para listar todos los tipos de información necesarios.
- Considerar los tipos de informes o envíos que se necesitarán para identificar elementos de información adicionales.

**Dividir la Información en Tablas**

- Identificar entidades principales (por ejemplo, productos, proveedores, clientes, pedidos) y crear una tabla para cada una.
- Evitar colocar toda la información en una sola tabla para prevenir la redundancia y los errores.

**Convertir los Elementos de Información en Columnas**

- Determinar los datos específicos que se deben rastrear para cada tema.
- Desglosar la información en sus partes más pequeñas y lógicas para una recuperación y manipulación eficientes de los datos.

**Especificar Claves Primarias**

- Cada tabla debe tener una clave primaria, un identificador único para sus registros.
- Las claves primarias deben tener valores únicos y no nulos, y no deben cambiar con el tiempo.
- El tipo de dato AutoNumber puede usarse para generar claves primarias únicas.

**Crear las Relaciones entre Tablas  para Unir la Información de Varias Tablas**

Una vez que has dividido tu información en tablas, necesitas una manera de unir la información nuevamente de manera significativa. Por ejemplo, un formulario de pedidos puede incluir información de varias tablas:

1. **Clientes**
2. **Empleados**
3. **Pedidos**
4. **Productos**
5. **Detalles del Pedido**

Access es un sistema de gestión de bases de datos relacional, donde la información se divide en tablas basadas en temas y se utilizan relaciones entre tablas para reunir la información según sea necesario.

**Creación de una Relación Uno a Muchos**

Considera las tablas Proveedores y Productos. Un proveedor puede suministrar varios productos, por lo tanto, la relación entre estas tablas es uno a muchos. Para representar esta relación, toma la clave primaria de la tabla del "uno" y añádela como una columna adicional en la tabla del "muchos". Por ejemplo, agrega la columna ID del Proveedor de la tabla Proveedores a la tabla Productos. La columna ID del Proveedor en la tabla Productos se llama clave foránea, ya que es la clave primaria en la tabla Proveedores.

**Creación de una Relación Muchos a Muchos**

Considera la relación entre las tablas Productos y Pedidos. Un pedido puede incluir varios productos y un producto puede aparecer en varios pedidos. Esta relación se llama muchos a muchos. Para resolver esto, crea una tercera tabla, llamada tabla de intersección, que descompone la relación muchos a muchos en dos relaciones uno a muchos. Inserta la clave primaria de cada una de las dos tablas en la tercera tabla, registrando cada instancia de la relación.

**Creación de una Relación Uno a Uno**

En una relación uno a uno, cada registro en una tabla corresponde a un único registro en otra tabla. Por ejemplo, si necesitas registrar información suplementaria para productos que se aplica raramente, esta información se almacena mejor en una tabla separada con la misma clave primaria que la tabla Productos. Esta relación uno a uno asegura que ambos registros compartan un campo común.

**Refinando el Diseño**

Una vez que tienes las tablas, campos y relaciones necesarios, crea y llena tus tablas con datos de muestra y prueba trabajar con la información. Esto ayuda a identificar posibles problemas, como la necesidad de agregar una columna olvidada o dividir una tabla para eliminar duplicación. Verifica si puedes usar la base de datos para obtener las respuestas que necesitas. Crea borradores de formularios e informes para ver si muestran los datos esperados y busca duplicación innecesaria de datos para ajustar tu diseño en consecuencia.

**Aplicación de las Reglas de Normalización**

La normalización ayuda a asegurar que has dividido correctamente la información en las tablas adecuadas. Las reglas de normalización, aplicadas en sucesión, llevan tu diseño a uno de los "formas normales". Las tres primeras formas normales son las más comunes en el diseño de bases de datos.

- **Primera Forma Normal:** Cada intersección de fila y columna debe contener un solo valor.
- **Segunda Forma Normal:** Cada columna no clave debe depender completamente de toda la clave primaria.
- **Tercera Forma Normal:** Las columnas no clave deben ser independientes entre sí y depender solo de la clave primaria.

Aplicar estas reglas te ayuda a refinar y validar tu diseño de base de datos, asegurando una estructura eficiente y sin redundancias innecesarias.

---