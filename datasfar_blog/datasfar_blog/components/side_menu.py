import reflex as rx

from datasfar_blog.states.CourseState import CourseState

def side_menu() -> rx.Component:
    return rx.drawer.root(
    rx.drawer.trigger(rx.card(rx.icon("arrow-right-from-line")),position="absolute",
                              top="10px",
                              left="10px"),
    rx.drawer.overlay(z_index="5"),
    rx.drawer.portal(
        rx.drawer.content(
            rx.vstack(
                rx.drawer.close(rx.card(rx.icon("arrow-left-to-line")),
                                align_self="end"),
                rx.foreach(
                    CourseState.course_index,
                    index_card
                ),
                width="100%",
            ),
            top="auto",
            right="auto",
            height="100%",
            width="35vw",
            padding="2em",
        ),
        border="none !important"
    ),
    direction="left",
)

def index_card(section:dict) -> rx.Component:
    return rx.card(
        rx.link(
            rx.text(section["title"]),
            href=f"#{section["link"]}"
        ),
        rx.checkbox(),
        display="flex",
        justify_content="space-between",
        align_items="end",
        width="100%"
    )