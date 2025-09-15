from typing import List

from models import Item
from pydantic import BaseModel


class Order(BaseModel):
    canceled_at: str | None = None
    items: List[Item]
    number: int
