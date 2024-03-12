from abc import ABC, abstractmethod
from typing import List

from simple_blog.application.entities import Post, Category, Comment


class PostsRepo(ABC):
    @abstractmethod
    def add(self, post: Post): ...

    @abstractmethod
    def remove(self, post: Post): ...

    @abstractmethod
    def update(self, post: Post): ...

    @abstractmethod
    def get_by_id(self, post: int) -> Post: ...

    @abstractmethod
    def search(self, pattern) -> List[Post]: ...


class CategoriesRepo(ABC):
    @abstractmethod
    def add(self, category: Category): ...

    @abstractmethod
    def remove(self, post: Category): ...

    @abstractmethod
    def update(self, post: Category): ...


class CommentsRepo(ABC):
    @abstractmethod
    def add(self, comment: Comment): ...

    @abstractmethod
    def remove(self, comment: Comment): ...

    @abstractmethod
    def update(self, comment: Comment): ...
