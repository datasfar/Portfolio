import reflex as rx

from datasfar_blog.components.header import header
from datasfar_blog.components.side_menu import side_menu

from datasfar_blog.states.CourseState import CourseState

@rx.page(route="/curso/introduccion-a-bases-de-datos",
         on_load=CourseState.load_lesson("databases", "1_introduccion"))
def data_bases_1():
        return rx.container(
        header(),
        side_menu(CourseState.course_3_index),
        rx.markdown(
            CourseState.lesson_content
        ),
    )
