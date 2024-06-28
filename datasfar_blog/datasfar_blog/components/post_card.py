import reflex as rx
import datasfar_blog.styles.styles as styles

def post_card(article:dict[str, str]) -> rx.Component:
    return rx.card(
                rx.vstack(
                    rx.link(
                        rx.heading(
                            article["title"],
                            style={
                                "font_size":"1.2em",
                                "_hover":{
                                    "text_decoration":"underline dotted",
                                },
                            }
                        ),
                        width="100%",
                        href=article["link"]
                    ),
                    rx.text(article["description"]),
                    rx.hstack(
                        rx.stack(
                            rx.foreach(
                                article["tags"],
                                lambda x: rx.card(x, style=styles.BLOG_TAGS)
                            ),
                        justify="start",
                        ),
                        rx.text(article["date"], font_weight="200"),
                        align="end",
                        justify="between",
                        width="100%"
                    ),
                )
        )