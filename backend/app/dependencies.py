from functools import lru_cache

from fastapi import Depends
from services import InterpretOrderMessageService, OrderStorageService


@lru_cache()
def get_order_storage_service() -> OrderStorageService:
    return OrderStorageService()


def get_interpret_order_message_service(
    storage_service: OrderStorageService = Depends(get_order_storage_service),
) -> InterpretOrderMessageService:
    return InterpretOrderMessageService(storage_service)
