import reflex as rx

from datasfar_blog.components.header import header
from datasfar_blog.components.side_menu import side_menu

from datasfar_blog.states.CourseState import CourseState

@rx.page(route="/curso/introduccion-a-pandas",
         on_load=CourseState.load_lesson("pandas", "1_pandas_series"))
def pandas():
        return rx.container(
        header(),
        side_menu(CourseState.course_2_index),
        rx.markdown(
            CourseState.lesson_content
        ),
    )
