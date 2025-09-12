from typing import List

from enums import ItemType
from pydantic import BaseModel


class Item(BaseModel):
    amount: int
    type: ItemType
