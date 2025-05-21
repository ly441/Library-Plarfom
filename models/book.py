from datetime import date
from dataclasses import dataclass
from typing import Optional


@dataclass
class Book:
    id: Optional[int]
    title: str
    isbn: Optional[str]
    published_date: Optional[date]
    total_copies: int
    available_copies: int
    category_id: Optional[int] = None
