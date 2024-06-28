import reflex as rx
import re

from datasfar_blog.components.header import header

class PostState(rx.State):

    @rx.var
    def post_id(self) -> str:
        return self.router.page.params.get("pid", "no pid")

    @rx.var
    def post_content(self) -> str:
        post_id = self.router.page.params.get("pid", "no pid")
        post_path = f"assets/posts/{post_id}.md"
        try:
            with open(post_path, "r") as file:
                self.markdown_content = file.read()
                return self.markdown_content
        except FileNotFoundError:
            return " "
        except Exception as e:
            return f"Error al leer el post: {str(e)}"
    
@rx.page(
        route="/post/[pid]",
)
def post():  
    return rx.container(
        header(),
        rx.markdown(PostState.post_content),
        )  