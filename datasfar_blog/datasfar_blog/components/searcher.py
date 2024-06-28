import reflex as rx

from datasfar_blog.states.ArticleState import ArticleState

class SearchState(rx.State):
    filter_text: str = ""
    
    def call_filter(self, filter: str):

        self.filter_text = filter
        print(self.filter_text)
        ArticleState.filter_articles(self.filter_text)

def searcher()-> rx.Component:
    return rx.hstack(
        rx.input(rx.icon("search", margin_left=".2em"),
            id="search",
            placeholder="Busca aquí...",
            name="search",
            on_change=ArticleState.call_filter,
            value=ArticleState.filter_text,
            variant="surface",
            width="100%",
            display="flex",
            flex_direction="row-reverse",
            align_items="center",
            margin_bottom="1.4em"
            
        ),

    )

