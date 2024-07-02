import reflex as rx
import datasfar_blog.styles.styles as styles

def header() -> rx.Component:
    return rx.hstack(
        rx.stack(
            rx.link(rx.color_mode.button(size="2")),
            rx.link("blog.datasfar", 
                    href="/",
                    text_decoration="none",
                    style={
                        "font_size":"1.2em",
                        "font_weight":"600"}
            ),
            align="center"
        ),
        rx.stack(
            rx.link(rx.icon("linkedin", size=34, style=styles.SOCIAL_LINKS), href="https://www.linkedin.com/in/francisco-alcaide/"),
            rx.link(rx.icon("github", size=34, style=styles.SOCIAL_LINKS), href="https://github.com/datasfar"),
            rx.link(rx.icon("instagram", size=34, style=styles.SOCIAL_LINKS), href="https://www.instagram.com/datasfar?igsh=MTl0aTU5bHJzdGl3bw=="),
        ),
        justify="between",
        align="center",
        margin_bottom="40px",
    )