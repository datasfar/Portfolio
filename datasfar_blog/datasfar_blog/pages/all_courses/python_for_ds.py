import reflex as rx

from datasfar_blog.components.header import header
from datasfar_blog.components.side_menu import side_menu

from datasfar_blog.states.CourseState import CourseState

@rx.page(route="/curso/python-para-ciencia-de-datos")
def python_for_ds():
        return rx.container(
                header(),
                side_menu(),
                rx.markdown(
                    CourseState.load_content
                ),
        )
