from datetime import datetime

from classic.components import component
from classic.operations import operation
from pydantic import BaseModel as ValidationModel

from simple_blog.application import entities, errors, interfaces


class PostInfo(ValidationModel):
    author: entities.User
    category: entities.Category
    title: str
    text: str
    publication_date: datetime


@component
class Blog:  # FIXME: implement pydantic
    posts: interfaces.PostsRepo

    @operation
    def search_posts(self, pattern: str) -> list[entities.Post]:
        return list(self.posts.search(pattern))

    @operation
    def get_post(self, post_id: int) -> entities.Post:
        post = self.posts.get_by_id(post_id)
        if post is None:
            raise errors.NoPost(post_id=post_id)
        return post

    @operation
    def add_post(self, post_info: PostInfo):
        self.posts.add(post_info.create_obj(entities.Post))

    @operation
    def update_post(self, post_info: PostInfo):
        post = self.posts.get_by_id(post_info.id)
        if post is None:
            raise errors.NoPost(post_id=post_info.id)
        post_info.populate_obj(post)


@component
class Category:
    category: interfaces.CategoriesRepo


@component
class Comment:
    comment: interfaces.CommentsRepo
