import reflex as rx

class CourseState(rx.State):
    
    # Lista de diccionarios que representa el índice del curso
    # Cada diccionario contiene información sobre una lección
    course_index: list[dict] = [
        {
            "title": "Introducción a la estadistica descriptiva",
            "link": "/",
            "lesson": "lesson-1"
        },
        {
            "title": "Conceptos clave de estadista con python",
            "link": "/",
            "lesson": "lesson-2"
        },
        {
            "title": "Introducción a la estadistica descriptiva",
            "link": "/",
            "lesson": "lesson-1"
        },
        {
            "title": "Conceptos clave de estadista con python",
            "link": "/",
            "lesson": "lesson-2"
        },
    ]

    # Variable para almacenar el contenido del markdown de la lección actual
    markdown_content: str = ""
    
    # Variable para almacenar el identificador de la lección actual
    current_lesson: str = "lesson-1"

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