import reflex as rx

class CourseState(rx.State):

    course_index:list[dict] = [
        {
        "title":"Introducción a la estadistica descriptiva",
        "link":"/",
        },{
        "title":"Conceptos clave de estadista con python",
        "link":"/",
        },{
        "title":"Introducción a la estadistica descriptiva",
        "link":"/",
        },{
        "title":"Conceptos clave de estadista con python",
        "link":"/",
        },
        ]
    
    @rx.var
    def load_content(self) -> str:
        # recibimos el id lesson_id y se lo pasamos al path
        lesson_path = "assets/courses/python_ds/lesson.md"
        try:
            with open(lesson_path, "r") as file:
                self.markdown_content = file.read()
                print("archivo cargado")
                return self.markdown_content
        except FileNotFoundError:
            print("Error 1")
            return " "
        except Exception as e:
            print("Error 2")
            return f"Error al leer el post: {str(e)}"