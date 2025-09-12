from typing import Any, Dict

from models.order import Order
from schemas.orders import InterpretedOrderResponse
from services.order_storage import order_storage

from .llm_service import LLMService


class InterpretOrderMessageService:
    def __init__(self):
        self.llm_service = LLMService()

    def handle(self, message: str) -> Dict[str, Any]:
        # Get the parsed response from LLM
        response: InterpretedOrderResponse = self.llm_service.handle(message)

        # Handle order creation
        if response.order_items:
            order_storage.add_order(
                Order(
                    items=response.order_items,
                    number=len(order_storage.get_orders()) + 1,
                )
            )

        # Handle order cancellation
        if response.canceled_orders:
            for order_number in response.canceled_orders:
                order_storage.cancel_order(order_number)

        return response
