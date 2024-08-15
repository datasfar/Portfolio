import reflex as rx

class CourseState(rx.State):
    
    # Lista de diccionarios que representa el índice del curso
    # Cada diccionario contiene información sobre una lección
    course_index: list[dict] = [
        {
            "title": "1. Tipos de datos en Python",
            "link": "/",
            "lesson": "1_tipos",
            "course": "python_ds"
        },
        {
            "title": "2. Uso de fechas y horas",
            "link": "/",
            "lesson": "2_fechas_y_horas",
            "course": "python_ds"
        },
        {
            "title": "3. Funciones en Python",
            "link": "/",
            "lesson": "3_funciones",
            "course": "python_ds"
        },
        {
            "title": "4. Cargar datos de un archivo CSV",
            "link": "/",
            "lesson": "4_ejemplo_csv",
            "course": "python_ds"
        },
        {
            "title": "5. Uso básico de Numpy",
            "link": "/",
            "lesson": "5_numpy",
            "course": "python_ds"
        },
        {
            "title": "6. Expresiones regulares REGEX",
            "link": "/",
            "lesson": "6_regex",
            "course": "python_ds"
        },
    ]

    course_2_index: list[dict] = [
        {
            "title": "1. Pandas Series",
            "link": "/",
            "lesson": "1_pandas_series",
            "course": "pandas"
        },
        {
            "title": "2. Pandas Dataframes I",
            "link": "/",
            "lesson": "2_pandas_dataframes",
            "course": "pandas"
        },
        {
            "title": "3. Pandas Dataframes II",
            "link": "/",
            "lesson": "3_pandas_dataframes_II",
            "course": "pandas"
        },
        {
            "title": "4. Pandas Dataframes III",
            "link": "/",
            "lesson": "4_pandas_dataframes_III",
            "course": "pandas"
        },
        {
            "title": "5. Pandas Dataframes IV",
            "link": "/",
            "lesson": "5_pandas_dataframes_IV",
            "course": "pandas"
        },
        {
            "title": "6. Pandas Dataframes V",
            "link": "/",
            "lesson": "6_pandas_dataframe_V",
            "course": "pandas"
        },

    ]
    
    course_3_index: list[dict] = [
        {
            "title": "1. Introducción a Bases de Datos",
            "link": "/",
            "lesson": "1_introduccion",
            "course": "databases"
        },
        {
            "title": "2. Introducción a SQL",
            "link": "/",
            "lesson": "2_sql",
            "course": "databases"
        },
        {
            "title": "3. Estructura básica de las bases de datos",
            "link": "/",
            "lesson": "3_estructura",
            "course": "databases"
        },
        {
            "title": "4. Tipos de datos SQL",
            "link": "/",
            "lesson": "4_tipos",
            "course": "databases"
        },
        {
            "title": "5. Crear y Leer",
            "link": "/",
            "lesson": "5_crear_y_leer",
            "course": "databases"
        },
        {
            "title": "6. Actualizar y Eliminar",
            "link": "/",
            "lesson": "6_actualizar_y_eliminar",
            "course": "databases"
        },
        {
            "title": "7. Operaciones SQL",
            "link": "/",
            "lesson": "7_operaciones",
            "course": "databases"
        },
        {
            "title": "8. Clasificación y filtrado de datos",
            "link": "/",
            "lesson": "8_clasificacion",
            "course": "databases"
        },
    ]

    # Variable para almacenar el contenido del markdown de la lección actual
    markdown_content: str = ""
    
    # Variable para almacenar el identificador de la lección actual
    # current_lesson: str = "1_tipos"

    def load_lesson(self, course:str, current_lesson: str):
        """
        Carga el contenido de la lección actual desde un archivo markdown.
        """
        path_lesson = f"assets/courses/{course}/{current_lesson}.md"
        try:
            with open(path_lesson, "r") as file:
                self.markdown_content = file.read()
                print(f"archivo cargado en: {path_lesson}")
        except FileNotFoundError:
            print(f"Error 1: file not found at: {path_lesson}")
            self.markdown_content = " "  
        except Exception as e:
            print("Error 2")
            self.markdown_content = f"Error al leer el post: {str(e)}" 


    def change_current_lesson(self, lesson:str, course:str):
        """
        Cambia la lección actual y carga su contenido.
        
        Args:
            lesson (str): El identificador de la nueva lección a cargar.
        """
        #self.current_lesson = lesson
        self.load_lesson(course, lesson)
        print(f"lección cambiada {lesson}")


    @rx.var
    def lesson_content(self) -> str:
        """
        Variable computada que devuelve el contenido de la lección actual.
        
        Returns:
            str: El contenido de la lección actual en formato markdown.
        """
        return self.markdown_content