from classic.http_api import App as BaseApp

from simple_blog.adapters.api.controllers import Post, Category, Comment


class App(BaseApp):
    @classmethod
    def create(cls, post: Post, category: Category, comment: Comment):
        app = cls()
        app.register(post)
        app.register(category)
        app.register(comment)
        return app
