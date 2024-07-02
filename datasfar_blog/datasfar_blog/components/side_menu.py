import reflex as rx

from datasfar_blog.states.CourseState import CourseState


def side_menu(menu:list[dict]) -> rx.Component:
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
                    menu,
                    index_card
                ),
                width="100%",
            ),
            top="auto",
            right="auto",
            height="100%",
            width="35vw",
            padding="2em",
            background=rx.color_mode_cond(
                light="#ffffff",
                dark="#111113"
            ),
        ),
        border="none !important"
    ),
    direction="left",
)

def index_card(section:dict) -> rx.Component:
    return rx.card(
        rx.text(section["title"]),
        display="flex",
        justify_content="space-between",
        align_items="end",
        width="100%",
        on_click=CourseState.change_current_lesson(section["lesson"], section["course"])
    )