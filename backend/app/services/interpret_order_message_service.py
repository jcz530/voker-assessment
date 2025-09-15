from typing import Any, Dict

from models import Order
from schemas import InterpretedOrderResponse

from .llm_service import LLMService
from .order_storage import OrderStorageService


class InterpretOrderMessageService:
    def __init__(self, storage_service: OrderStorageService):
        self.storage_service = storage_service
        self.llm_service = LLMService(storage_service)

    def handle(self, message: str) -> Dict[str, Any]:
        # Get the parsed response from LLM
        response: InterpretedOrderResponse = self.llm_service.handle(message)

        # Handle order creation
        if response.order_items:
            self.storage_service.add_order(
                Order(
                    items=response.order_items,
                    number=len(self.storage_service.get_orders()) + 1,
                )
            )

        # Handle order cancellation
        if response.canceled_orders:
            for order_number in response.canceled_orders:
                self.storage_service.cancel_order(order_number)

        return response
