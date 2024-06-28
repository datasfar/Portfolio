import reflex as rx
from datasfar_blog.components.course_card import course_card


def courses() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading("Cursos"),
            rx.link("Ver todos", 
                    rx.icon("move-right", margin_left="1em"),
                    display="flex",
                    cursor="pointer",
                    href="/cursos"
            ),
            align="start",
            justify="between",
            width="100%"
        ),
        rx.chakra.responsive_grid(
            
            course_card("/courses_images/python.png",
                 "/curso/python-para-ciencia-de-datos", 
                 "Python para Ciencia de Datos", 
                 "Uso básico de pandas: indexación, consultas, limpiado de valores nulos, merge() y concat, codigo limpio y convenciones.",
                 ["Pandas", "Python", "Numpy"]),
            course_card("/courses_images/math.png",
                 "/curso/matematicas-para-ciencia-de-datos", 
                 "Matemáticas para Ciencia de Datos", 
                 "Ejemplo de un ejercicio de limpieza y analisis de datos. Se analizan los aspecto demograficos y financieros de un grupo.",
                 ["Pandas", "MatploitLib"]),
            gap="5",
            columns=[1, 1, 2, 2, 2],
        ),
        margin_bottom="40px"
    )