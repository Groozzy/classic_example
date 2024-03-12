from datetime import datetime
from typing import Optional

from dataclasses import dataclass


@dataclass
class User:
    id: int
    email: str
    surname: Optional[str] = None
    name: Optional[str] = None


@dataclass
class Category:
    title: str


@dataclass
class Post:
    author: User
    category: Category
    title: str
    text: str
    publication_date: datetime


@dataclass
class Comment:
    author: User
    text: str
    publication_date: datetime
