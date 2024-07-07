import reflex as rx

class ProjectState(rx.State):

    projects: list[dict[str,str]] = [
        {   
            "favicon":"/project_icons/py.jpg",
            "title":"Streamlit Apps Library",
            "description":"Una libreria de pequeñas aplicaciones funcionales.",
            "tags":["Streamlit", "Python", "Data Science"],
            "link":"https://pyapps.datasfar.com/",
            "link_repo":"https://github.com/datasfar/DatasFar-Apps"
        },
        {   
            "favicon":"/project_icons/blog.jpg",
            "title":"Datasfar Blog",
            "description":"Blog con entradas y notebooks sobre data science",
            "tags":["Reflex", "Python", "Data Science"],
            "link":"http://datasciencehub.datasfar.com",
            "link_repo":"http://www.github.com/datasfar"
        },
        {   
            "favicon":"/project_icons/sql.jpg",
            "title":"SQL Detective",
            "description":"Juego de comandos para aprender SQL.",
            "tags":["Reflex", "Python", "SQL"],
            "link":"https://sql-detective.datasfar.com/",
            "link_repo":"https://github.com/datasfar/SQL-Detective"
        },
        {   
            "favicon":"/project_icons/stock.jpg",
            "title":"Stock Manager",
            "description":"Sistema de gestión de stock.",
            "tags":["Django", "Python"],
            "link":"https://github.com/datasfar/Django-Stock-Manager",
            "link_repo":"https://github.com/datasfar/Django-Stock-Manager"
        },
        {   
            "favicon":"/project_icons/web.jpg",
            "title":"Reflex Blog Template",
            "description":"Plantilla para creación de un blog con reflex.",
            "tags":["Reflex", "Python"],
            "link":"http://www.pyapps.datasfar.com",
            "link_repo":"http://www.github.com"
        },
    ]