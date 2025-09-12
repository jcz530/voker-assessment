from services import InterpretOrderMessageService, OrderStorageService


def get_interpret_order_message_service() -> InterpretOrderMessageService:
    return InterpretOrderMessageService()


def get_order_storage_service() -> OrderStorageService:
    return OrderStorageService()
