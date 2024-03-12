from classic.components import component

from simple_blog.application import services


@component
class Post:
    post: services.Post

    def on_get_post(self, request, response):
        post = self.post.get


@component
class Category:
    category: services.Category


@component
class Comment:
    comment: services.Comment
