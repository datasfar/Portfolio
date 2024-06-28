import reflex as rx

from datasfar_blog.components.project_card import project_card

from datasfar_blog.states.ProjectState import ProjectState

def projects()-> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading("Proyectos"),
            rx.link("Ver todos", 
                    rx.icon("move-right", margin_left="1em"),
                    display="flex",
                    cursor="pointer",
                    href="/proyectos"
            ),
            align="start",
            justify="between",
            width="100%"
        ),
        rx.chakra.responsive_grid(
            rx.foreach(
                ProjectState.projects[0:4],
                project_card
            ),
            width="100%",
            gap="5",
            columns=[1, 1, 2, 2, 2],
        ),
        margin_bottom="60px"
    )