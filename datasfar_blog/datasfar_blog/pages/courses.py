import reflex as rx

from datasfar_blog.components.header import header
from datasfar_blog.components.course_card import course_card

@rx.page(route="/cursos")
def courses():
        """Una página que se actualiza basada en la ruta."""
        return rx.container(
        header(),
        rx.hstack(
            rx.heading("Notebooks"),
            align="start",
            justify="between",
            width="100%"
        ),
        rx.chakra.responsive_grid(
            
            course_card("/courses_images/python.png",
                 "/curso/python-para-ciencia-de-datos", 
                 "Python para Ciencia de Datos", 
                 "Una pequeña introducción al uso de python enfocado a la ciencia de datos: documentos csv, regex y numpy. Requiere conocimientos básicos sobre python.",
                 ["Python", "Numpy", "DS"]),
            course_card("/courses_images/math.png",
                 "/curso/introduccion-a-pandas", 
                 "Introducción a Pandas", 
                 "Uso básico de pandas, la librería de python más usada en ciencia de datos: dataframes y series, indexación, consultas, datos faltantes...",
                 ["Pandas", "Python"]),
            gap="5",
            columns=[1, 1, 2, 2, 2],
        ),
        margin_bottom="40px"
    )
