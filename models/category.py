from dataclasses import dataclass
from typing import Optional


@dataclass
class Category:
    id: Optional[int]
    title: str
    description: Optional[str] = None
