import reflex as rx

class CourseState(rx.State):
    
    # Lista de diccionarios que representa el índice del curso
    # Cada diccionario contiene información sobre una lección
    course_index: list[dict] = [
        {
            "title": "1. Tipos de datos en Python",
            "link": "/",
            "lesson": "1_tipos"
        },
        {
            "title": "2. Uso de fechas y horas",
            "link": "/",
            "lesson": "2_fechas_y_horas"
        },
        {
            "title": "3. Funciones en Python",
            "link": "/",
            "lesson": "3_funciones"
        },
        {
            "title": "4. Cargar datos de un archivo CSV",
            "link": "/",
            "lesson": "4_ejemplo_csv"
        },
        {
            "title": "5. Uso básico de Numpy",
            "link": "/",
            "lesson": "5_numpy"
        },
        {
            "title": "6. Expresiones regulares REGEX",
            "link": "/",
            "lesson": "6_regex"
        },
    ]

    # Variable para almacenar el contenido del markdown de la lección actual
    markdown_content: str = ""
    
    # Variable para almacenar el identificador de la lección actual
    current_lesson: str = "1_tipos"

    def load_lesson(self):
        """
        Carga el contenido de la lección actual desde un archivo markdown.
        """
        path_lesson = f"assets/courses/python_ds/{self.current_lesson}.md"
        try:
            with open(path_lesson, "r") as file:
                self.markdown_content = file.read()
                print("archivo cargado")
        except FileNotFoundError:
            print("Error 1")
            self.markdown_content = " "  
        except Exception as e:
            print("Error 2")
            self.markdown_content = f"Error al leer el post: {str(e)}" 


    def change_current_lesson(self, lesson:str):
        """
        Cambia la lección actual y carga su contenido.
        
        Args:
            lesson (str): El identificador de la nueva lección a cargar.
        """
        self.current_lesson = lesson
        self.load_lesson()
        print(f"lección cambiada {self.current_lesson}")


    @rx.var
    def lesson_content(self) -> str:
        """
        Variable computada que devuelve el contenido de la lección actual.
        
        Returns:
            str: El contenido de la lección actual en formato markdown.
        """
        return self.markdown_content