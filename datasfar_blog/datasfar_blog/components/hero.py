import reflex as rx

class HeroState(rx.State):

    def download_pdf(self):
        return rx.download(url="/CV_FranciscoAlcaide-1.pdf")

def hero() -> rx.Component:
    return rx.hstack(
            rx.image(src="avatar.png", border_radius="50%", width="100px"),
            rx.vstack(
                rx.heading(" 👋 Hola! Soy Fran", margin_bottom="0"),
                rx.text("Soy desarrollador Python y Data Scientist. Con casi 2 años en el mundo del desarrollo de software. Aquí encontrarás algunos de mis proyectos, certificaciones realizadas y más."),
                rx.chakra.responsive_grid(
                    rx.button(
                        rx.icon("circle", size=14, color="#82E0AA", stroke_width=2.5),
                        rx.text("Disponible para trabajar"),
                        display="flex",
                        align_items="center",
                        gap="5px",
                        padding="0.3em 0.8em",
                        variant="surface",
                        disabled=True
                    ),
                    rx.button(
                        rx.icon("download", size=18),
                        rx.text("Descargar curriculum"),
                        display="flex",
                        align_items="center",
                        gap="5px",
                        padding="0.3em 0.8em",
                        variant="surface",
                        on_click=HeroState.download_pdf,
                    ),
                    gap="1em",
                    columns=[1, 2, 2, 2, 2]
                ),
            ),
            margin_bottom="50px"
        ),