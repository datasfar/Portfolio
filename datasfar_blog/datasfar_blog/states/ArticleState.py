import reflex as rx

class ArticleState(rx.State):

    articles: list[dict[str, str]] = [
        {
            "title":"Utilización de entornos virtuales con venv",
            "description": "En este artículo, exploraremos el uso de los entornos vituales en nuestros proyectos con venv.",
            "link":"/post/entornos-virtuales",
            "tags":["venv", "utilidades"],
            "date":"20 may 2024"
        },
        
    ]

    selected_articles: list[dict[str, str]] = articles
    

    def get_articles(self):
        """
        Método para obtener una copia de los artículos originales.
        Se utiliza para reiniciar la lista de artículos filtrados.
        """
        self.selected_articles = self.articles

    
    def filter_articles(self, filter:str):
        """
        Método para filtrar los artículos por el titulo.
        Actualiza la lista de artículos filtrados.
        """
        self.selected_articles = []
        for article in self.articles:
            if filter.lower() in article["title"].lower():
                self.selected_articles.append(dict(article)) 
    

    filter_text: str = ""

    def call_filter(self, filter: str):
        """
        Método para actualizar el texto del filtro y aplicar el filtro a los artículos.
        """
        self.filter_text = filter
        self.filter_articles(filter)