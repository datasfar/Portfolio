import reflex as rx

from datasfar_blog.components.header import header
from datasfar_blog.components.project_card import project_card

from datasfar_blog.states.ProjectState import ProjectState

@rx.page(route="/proyectos")
def projects():
        return rx.container(
                header(),
                rx.vstack(
                        rx.hstack(
                                rx.heading("Proyectos"),
                                margin_bottom="1em"
                        ),
                        align="start",
                        justify="between",
                        width="100%"
                        ),
                        rx.chakra.responsive_grid(
                                rx.foreach(
                                        ProjectState.projects,
                                        project_card
                                ),
                                width="100%",
                                gap="5",
                                columns=[1, 1, 2, 2, 2],
                        ),
                margin_bottom="60px"
        )
        
