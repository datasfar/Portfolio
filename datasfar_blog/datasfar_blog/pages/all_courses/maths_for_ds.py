import reflex as rx

from datasfar_blog.components.header import header

@rx.page(route="/curso/matematicas-para-ciencia-de-datos")
def maths_for_ds():
        return rx.container(
                header(),
                rx.text("Matemáticas para Ciencia de datos")
        )
