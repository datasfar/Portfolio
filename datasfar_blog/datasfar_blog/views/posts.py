import reflex as rx
from datasfar_blog.components.post_card import post_card
from datasfar_blog.states.ArticleState import ArticleState

# post view
def posts()-> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading("Posts"),
            rx.link("Ver todos", 
                    rx.icon("move-right", margin_left="1em"),
                    display="flex",
                    cursor="pointer",
                    href="/posts"
            ),
            align="start",
            justify="between",
            width="100%"
        ),
        rx.chakra.responsive_grid(
            
            rx.foreach(
                     ArticleState.articles,
                     post_card
                ),
            width="100%",
            gap="5",
            columns=[1, 1, 1, 1, 1],
        ),
        margin_bottom="60px"
    )