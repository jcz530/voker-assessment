from typing import List

from models import Item
from pydantic import BaseModel, Field, field_validator


class CreateOrderRequest(BaseModel):
    message: str = Field(..., max_length=1000, min_length=1)

    @field_validator("message")
    def validate_message(cls, v):
        v = v.strip()
        if not v:
            raise ValueError("Message cannot be empty")
        return v


class InterpretedOrderResponse(BaseModel):
    canceled_orders: List[int] = []
    errors: List[str] = []
    order_items: List[Item] = []
