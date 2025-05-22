from datetime import date
from dataclasses import dataclass
from typing import Optional

@dataclass
class Member:
    id: Optional[int]
    first_name: str
    last_name: str
    surname: str
    email: str
    joined_date: Optional[date]