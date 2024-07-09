import reflex as rx

def footer()->rx.Component:
    return rx.hstack(
        rx.text(
        "Diseño Inspirado 🎨 por ", rx.link(rx.text.strong("@pheralb"), href="https://github.com/pheralb")
        ),
        rx.text(
        "Desarrollado con ❤️ por ", rx.text.strong("datasfar")
        ),
        display="flex",
        justify_content="space-between"
    )