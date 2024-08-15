import reflex as rx
from rxconfig import config

# pages
from datasfar_blog.pages.index import index

from datasfar_blog.pages.projects import projects

from datasfar_blog.pages.blog import blog
from datasfar_blog.pages.post import post

from datasfar_blog.pages.courses import courses
from datasfar_blog.pages.all_courses.python_for_ds import python_for_ds
from datasfar_blog.pages.all_courses.pandas import pandas
from datasfar_blog.pages.all_courses.data_bases_1 import data_bases_1

# styles
import datasfar_blog.styles.styles as styles


app = rx.App(
    theme=rx.theme(
        appearance="dark", has_background=True, radius="large", accent_color="gray", gray_color="slate"
    ),
    style=styles.MAIN_STYLES
)

app.add_page(index)

app.add_page(projects)

app.add_page(blog)
app.add_page(post)

app.add_page(courses)
app.add_page(python_for_ds)
app.add_page(pandas)
app.add_page(data_bases_1)


