import reflex as rx

from datasfar_blog.components.header import header
from datasfar_blog.components.side_menu import side_menu

from datasfar_blog.states.CourseState import CourseState

class LessonState(rx.State):
    ...
    
@rx.page(route="/curso/python-para-ciencia-de-datos",
         on_load=CourseState.load_lesson("python_ds", "1_tipos"))
def python_for_ds():
    return rx.container(
        header(),
        side_menu(CourseState.course_index),
        rx.markdown(
            CourseState.lesson_content
        ),
    )
