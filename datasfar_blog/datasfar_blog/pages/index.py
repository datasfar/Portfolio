import reflex as rx

# components
from datasfar_blog.components.header import header
from datasfar_blog.components.hero import hero
from datasfar_blog.components.footer import footer

# views
from datasfar_blog.views.projects import projects
from datasfar_blog.views.courses import courses
from datasfar_blog.views.posts import posts



def index() -> rx.Component:
    return rx.container(
        rx.theme_panel(default_open=False),
        header(),
        hero(),
        projects(),
        posts(),
        courses(),
        footer()
    )