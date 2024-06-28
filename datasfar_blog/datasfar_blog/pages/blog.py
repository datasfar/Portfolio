import reflex as rx

from datasfar_blog.components.header import header
from datasfar_blog.components.post_card import post_card
from datasfar_blog.components.searcher import searcher

from datasfar_blog.states.ArticleState import ArticleState



class BlogState(rx.State):   
    ...

@rx.page(route="/posts") 
def blog():
        
        return rx.container(
                header(),
                searcher(),
                rx.chakra.responsive_grid(
                    rx.foreach(
                            ArticleState.selected_articles,
                            post_card,
                        ),
                    gap="5",
                    columns=[1, 1, 1, 1, 1],
                ))
