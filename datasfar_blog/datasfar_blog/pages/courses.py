import reflex as rx

from datasfar_blog.components.header import header

@rx.page(route="/cursos")
def courses():
        """Una página que se actualiza basada en la ruta."""
        return rx.container(
                header(),
                rx.text("Cursos")
        )
