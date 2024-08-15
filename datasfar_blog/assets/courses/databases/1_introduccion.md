# Introducción a las bases de datos

---

## Índice: 

1. [¿Qué es una base de datos?](#1)
2. [¿Cómo se relacionan los datos?](#2)
3. [Gráficos de ejemplo con datos relacionales](#3)
4. [Tipos alternativos de bases de datos](#4)
5. [Evolución de las bases de datos](#5)


---
<a id="1"></a>
### ¿Qué es una base de datos?

- **Definición de datos**: Los datos son hechos y cifras sobre cualquier cosa, como información personal (nombre, edad, correo electrónico) o detalles de una transacción (número de pedido, descripción, cantidad).
- **Definición de bases de datos**: Una base de datos es un sistema electrónico para almacenar y organizar datos de manera sistemática, facilitando su manejo, eficiencia y seguridad.
- **Ejemplos de uso de bases de datos**:
    - Un banco utiliza bases de datos para clientes, cuentas y transacciones.
    - Un hospital utiliza bases de datos para pacientes, personal y datos de laboratorio.
- **Estructura de una base de datos**:
    - Las bases de datos están **organizadas en entidades** (como tablas en una hoja de cálculo) que contienen filas (instancias de datos específicos) y columnas (atributos que describen los datos).
- **Tipos de bases de datos**:
    - **Relacionales**: Organizadas en tablas con relaciones entre los datos.
    - **Orientadas a objetos**: Almacenan datos como objetos, útiles para representar estructuras complejas.
    - **Gráficas**: Utilizan nodos para representar entidades y aristas para representar relaciones.
    - **Documentales**: Almacenan datos en formato de documentos, como JSON.
- **Ubicación de las bases de datos**:
    - Pueden ser **alojadas en servidores físicos** en las instalaciones de una organización o en **la nube,** siendo esta última opción cada vez más popular por su accesibilidad y gestión simplificada.
    

---
<a id="2"></a>
### ¿Cómo se relacionan los datos?

- **Relación de Datos en Bases de Datos**:
    - Los datos en una base de datos deben estar relacionados para que puedan convertirse en información significativa.
    - Las tablas en una base de datos se relacionan entre sí mediante campos específicos.
    
    - **Ejemplo de Relación en una Tienda en Línea**:
        - Una tienda en línea puede tener una tabla de clientes y una tabla de pedidos.
        - Para relacionar los datos, se utiliza un campo común, como el ID del cliente.
    - **Detalles de la Tabla de Clientes**:
        - Contiene columnas como ID del cliente, nombre, apellido y correo electrónico.
        - Las filas representan registros de clientes individuales.
        - Cada cliente se identifica de forma única mediante un campo de clave primaria (ID del cliente).
    - **Detalles de la Tabla de Pedidos**:
        - Contiene columnas como ID del pedido y ID del cliente.
        - El ID del pedido es la clave principal de la tabla de pedidos.
        - El ID del cliente en la tabla de pedidos actúa como una clave externa que conecta con la tabla de clientes.
        
- **Claves Primarias y Claves Externas**:
    - La **clave primaria** es un campo con **valores únicos que identifica de forma exclusiva cada registro** en una tabla.
    - La **clave externa** es un campo que **conecta con la clave primaria de otra tabla** para establecer una relación entre ambas tablas.
- **Importancia de la Relación de Datos**:
    - Establecer relaciones entre datos en diferentes tablas permite extraer información significativa y realizar consultas efectivas.
    - Permite identificar de manera precisa los datos relacionados, como los detalles de un pedido específico de un cliente.
    

---
<a id="3"></a>
### Gráficos de ejemplo con datos relacionales

- **Importancia de Organizar y Presentar Datos**:
    - Los datos se recopilan de diversas fuentes (pedidos de clientes, inscripciones de cursos, interacciones de usuarios).
    - Organizar, procesar y presentar datos eficientemente los hace más útiles y significativos.
    - Los gráficos ayudan a visualizar y comprender mejor los datos, facilitando la toma de decisiones.
    
- **Tipos de Gráficos y su Uso**:
    - **Gráfico de barras**:
        - Presenta datos categóricos con barras rectangulares proporcionales a los valores.
        - Ejemplo: Mostrar ingresos anuales de una librería para analizar el impacto de la COVID-19.
    - **Gráfico de burbujas**:
        - Muestra comparación de valores en términos de tamaño de burbuja.
        - Ejemplo: Comparar la población de los 10 países más grandes en 2015.
    - **Gráfico de líneas**:
        - Presenta datos como puntos conectados por líneas, útil para mostrar tendencias.
        - Ejemplo: Cotización del oro en un mes, destacando cambios positivos y negativos.
    - **Gráfico circular**:
        - Muestra partes de un todo, con cada porción representando un porcentaje.
        - Ejemplo: Preferencias deportivas de estudiantes en una clase.
        
- **Otros Tipos de Gráficos**:
    - Gráficos de doble eje.
    - Gráficos de Gantt.
    - Mapas de calor.
    - Diagramas de dispersión.
    - Gráficos de área, que combinan gráficos de líneas y barras.
    
- **Elección del Gráfico Adecuado**:
    - Depende de la audiencia, la idea a presentar y la meta a alcanzar.
    - Gráficos de líneas son buenos para identificar tendencias.
    - Gráficos circulares son simples para mostrar partes de un todo pero pueden ser difíciles de leer con muchas porciones.
    - Evaluar la audiencia y los datos para experimentar con diferentes gráficos y elegir el más adecuado.
    

---
<a id="4"></a>
### Tipos alternativos de bases de datos

- **Definición y Evolución de Big Data**:
    - **Big Data** se refiere a **datos complejos que aumentan exponencialmente con el tiempo,** generados por plataformas de redes sociales, sitios de compras en línea, y el Internet de las cosas (IoT).
    - Los datos son **altamente no estructurados o semiestructurados.**
    - **Big Data combina datos estructurados, semiestructurados y no estructurados** de diversas fuentes, abordando problemas empresariales complejos y mejorando la toma de decisiones.
    
- **Limitaciones de Bases de Datos Relacionales y NoSQL**:
    - Las bases de datos relacionales tienen limitaciones para almacenar datos no estructurados.
    - Las **bases de datos NoSQL** ofrecen una **estructura flexible** y son esenciales para aplicaciones que generan grandes cantidades de datos no estructurados (e.g., redes sociales, IoT, IA).
    - Tipos de bases de datos NoSQL incluyen bases de datos de documentos, de valores clave y gráficas.
    
- **Impacto de Big Data en la Industria**:
    - **Sector de Fabricación**:
        - Predicción de fallas de equipos, evaluación de procesos de producción, respuesta proactiva a comentarios de clientes, y anticipación de demandas futuras.
    - **Sector Minorista**:
        - Anticipación de la demanda de clientes, mejora de la experiencia del cliente, análisis del comportamiento de gasto, y oportunidades de mejora de precios.
    - **Sector de Telecomunicaciones**:
        - Planificación de inversiones en infraestructura, diseño de nuevos servicios, análisis de datos de calidad del servicio, y mecanismos para retener clientes.
        
- **Bases de Datos en la Nube**:
    - Las organizaciones se trasladan a **la nube** para **evitar la infraestructura de servidores físicos**, **reduciendo costos de mantenimiento y almacenamiento**.
    - Ejemplos de servicios de almacenamiento en la nube incluyen Dropbox y iCloud.
    - Almacenar datos en la nube es una solución más asequible.
    
- **Inteligencia Empresarial (BI)**:
    - Las organizaciones utilizan **tecnologías y estrategias de BI** para **analizar datos y extraer información valiosa**, **mejorando la toma de decisiones empresariales.**
    - Las bases de datos han evolucionado de simples herramientas de almacenamiento a componentes críticos para el análisis empresarial y la estrategia.
    

---
<a id="5"></a>
### Evolución de las bases de datos

- **Historia y Evolución**:
    - La computarización de las bases de datos comenzó en la década de 1960, facilitando el almacenamiento y manejo de datos.
    - Cronología del desarrollo de bases de datos:
        - **1970-1990**: Archivos planos, jerárquicos y de red.
        - **1980-presente**: Relacionales.
        - **1990-presente**: Orientadas a objetos, objeto-relacionales, habilitadas para la web.
        
- **Tipos de Bases de Datos**:
    - **Archivos Planos**: Utilizados entre 1970 y 1990, almacenan datos en un único archivo o tabla.
    - **Sistemas Jerárquicos**: Almacenan datos de forma jerárquica con relaciones de uno a muchos.
    - **Bases de Datos de Red**: Introducidas por Charles Bachmann, permiten múltiples relaciones de muchos a muchos, con una estructura similar a un gráfico.
    - **Bases de Datos Relacionales**: Introducidas en los años 80 por E. F. Codd, almacenan datos en tablas con relaciones entre ellas mediante claves primarias y externas.
    - **Bases de Datos Orientadas a Objetos**: Introducidas en los 90, almacenan datos como objetos en el marco de lenguajes de programación OO como Java y C++.
    - **Bases de Datos NoSQL**: Surgieron en respuesta a la necesidad de manejar datos no estructurados y grandes volúmenes de datos, ofreciendo velocidad, flexibilidad y escalabilidad.
    
- **Desarrollo de SQL**:
    - SEQUEL, un lenguaje de consulta usado en bases de datos de red, evolucionó a SQL (Structured Query Language), convirtiéndose en un estándar para bases de datos relacionales.
    
- **Ventajas de Bases de Datos NoSQL**:
    - Mayor escalabilidad y distribución.
    - Menores costos y esquema flexible.
    - Capacidad para procesar datos no estructurados y semiestructurados.
    - No tienen relaciones complejas.
- **Tipos de Bases de Datos NoSQL**:
    - **Bases de Datos de Documentos**: Almacenan datos en documentos similares a objetos JSON.
    - **Bases de Datos Clave-Valor**: Contienen pares de claves y valores.
    - **Bases de Datos de Columnas Anchas**: Almacenan datos en tablas, filas y columnas dinámicas.
    - **Bases de Datos de Gráficos**: Almacenan datos en nodos y bordes, representando relaciones entre nodos.
    

---