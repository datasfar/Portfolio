import reflex as rx
import datasfar_blog.styles.styles as styles

def course_card(image:str, link:str, title:str, description:str, tags:list[str]) -> rx.Component:
    return rx.link(
        rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.stack(
                            rx.image(src=image, width="24px"),
                            rx.heading(
                                title,
                                style={
                                    "font_size":"1.2em"
                                }
                            ),
                            align_items="center"
                        ),
                        align="start",
                        justify="between",
                        width="100%"
                    ),
                    rx.text(description),
                    rx.stack(
                        rx.foreach(
                            tags,
                            lambda x: rx.card(x, style=styles.BLOG_TAGS)
                        ),
                        align="end",
                        justify="end",
                        width="100%"
                    )
                )
        ),
        href=link
    )