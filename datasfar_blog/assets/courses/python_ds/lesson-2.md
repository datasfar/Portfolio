
# LESSON 2

---

## Índice: 

1. [Instalación de `venv`](#instalación-de-venv)
2. [Creación de un Entorno Virtual](#creación-de-un-entorno-virtual)
3. [Activación y Desactivación de Entornos Virtuales](#activación-y-desactivación-de-entornos-virtuales)
4. [Comandos Útiles para la Gestión de Entornos Virtuales](#comandos-útiles-para-la-gestión-de-entornos-virtuales)

---

En el desarrollo de aplicaciones Python, es común trabajar con diferentes paquetes y dependencias. Sin embargo, instalar todos estos paquetes de manera global puede llevar a conflictos entre versiones y problemas de dependencias. Imagina que estás trabajando en dos proyectos diferentes y ambos requieren versiones distintas de una misma biblioteca. Esto puede convertirse en un problema si tienes que instalar las bibliotecas globalmente.

Para evitar estos problemas, es recomendable trabajar en entornos virtuales. Un entorno virtual es una instalación de Python que está aislada de otras instalaciones. Esto significa que los paquetes instalados en un entorno virtual no afectarán a otros entornos virtuales ni a la instalación global de Python.

En este tutorial, aprenderemos a utilizar `venv`, una herramienta integrada en Python que nos permite crear entornos virtuales de forma sencilla. Con `venv`, podrás crear, activar, desactivar y eliminar entornos virtuales de manera rápida y eficiente, facilitando así el desarrollo de tus proyectos Python.

<a id="instalación-de-venv"></a>

## Instalación de `venv`

En la mayoría de los casos, `venv` viene incluido con la instalación estándar de Python 3, por lo que no es necesario instalarlo por separado. Sin embargo, si por alguna razón no tienes `venv` instalado, puedes instalarlo utilizando `pip`, el gestor de paquetes de Python.

Para instalar `venv` con `pip`, ejecuta el siguiente comando en tu terminal:

```bash
pip install virtualenv
```

<a id="creación-de-un-entorno-virtual"></a>

## Creación de un Entorno Virtual

Al crear un nuevo entorno virtual, el sistema configurará un directorio separado donde se almacenarán los paquetes y dependencias del proyecto. Para crear un entorno virtual, sigue estos pasos:

1. Abre tu terminal.
2. Navega hasta el directorio donde deseas crear el entorno virtual.
3. Ejecuta el siguiente comando, reemplazando `mi_entorno_virtual` por el nombre que desees para tu entorno:

```bash
python -m venv mi_entorno_virtual
```

Este comando creará un directorio con el nombre especificado, que contendrá los archivos necesarios para el entorno virtual.

<a id="activación-y-desactivación-de-entornos-virtuales"></a>

## Activación y Desactivación de Entornos Virtuales

### Activación del Entorno Virtual

Para activar el entorno virtual, debes ejecutar un comando específico dependiendo de tu sistema operativo.

- En Windows:

```bash
mi_entorno_virtual\Scriptsctivate
```

- En MacOS/Linux:

```bash
source mi_entorno_virtual/bin/activate
```

Una vez activado, deberías ver el nombre de tu entorno virtual en la línea de comandos, indicándote que estás trabajando dentro de ese entorno.

### Desactivación del Entorno Virtual

Para desactivar el entorno virtual, simplemente ejecuta el siguiente comando en tu terminal:

```bash
deactivate
```

<a id="comandos-útiles-para-la-gestión-de-entornos-virtuales"></a>

## Comandos Útiles para la Gestión de Entornos Virtuales

### Instalación de paquetes

Dentro del entorno virtual activado, puedes instalar paquetes utilizando `pip`:

```bash
pip install nombre_del_paquete
```

### Creación del `requirements.txt`

Para guardar una lista de todos los paquetes instalados en tu entorno virtual en un archivo `requirements.txt`, ejecuta el siguiente comando:

```bash
pip freeze > requirements.txt
```

### Listado de paquetes

Puedes listar todos los paquetes instalados en tu entorno virtual con:

```bash
pip list
```

### Desinstalación de paquetes

Para desinstalar un paquete de tu entorno virtual, ejecuta:

```bash
pip uninstall nombre_del_paquete
```

### Instalación desde `requirements.txt`

Para instalar todos los paquetes listados en un archivo `requirements.txt` en tu entorno virtual, ejecuta:

```bash
pip install -r requirements.txt
```

### Eliminación del entorno virtual

Para eliminar un entorno virtual, simplemente borra su directorio. Puedes hacerlo desde la interfaz gráfica o con un comando en la terminal:

- En Windows:

```bash
rmdir /s mi_entorno_virtual
```

- En MacOS/Linux:

```bash
rm -r mi_entorno_virtual
```

Con estos conocimientos, estarás listo para gestionar eficazmente entornos virtuales en Python, asegurando que tus proyectos mantengan dependencias organizadas y sin conflictos.

---
