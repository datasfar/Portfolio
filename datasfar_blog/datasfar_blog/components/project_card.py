import reflex as rx
import datasfar_blog.styles.styles as styles

def project_card(project:dict) -> rx.Component:
    return rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.link(
                            rx.image(src=project["favicon"], width="24px", border_radius="50%"),
                            rx.heading(
                                project["title"],
                                rx.icon("arrow-up-right", size=18),
                                style={
                                    "gap":"2px",
                                    "margin_left":".4em",
                                    "display":"flex",
                                    "align_items":"center",
                                    "font_size":"1.2em",
                                    "_hover":{
                                        "align_items":"baseline",
                                    },
                                    "transition_duration":".15s"
                                }
                            ),
                            display="flex",
                            align_items="center",
                            href=project["link"]
                        ),
                        rx.link(rx.icon("github", size=22), href=project["link_repo"]),
                        align_items="center",
                        justify="between",
                        width="100%"
                    ),
                    rx.text(project["description"]),
                    rx.stack(
                        rx.foreach(
                            project["tags"],
                            lambda x: rx.card(x, style=styles.BLOG_TAGS)
                        ),
                        align="end",
                        justify="end",
                        width="100%"
                    )
                )
    )
