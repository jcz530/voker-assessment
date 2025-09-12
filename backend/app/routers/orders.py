from typing import List

from dependencies import get_interpret_order_message_service, get_order_storage_service
from fastapi import APIRouter, Depends
from models import Order
from schemas import CreateOrderRequest
from services import InterpretOrderMessageService

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[Order])
async def indexOrders(storage=Depends(get_order_storage_service)):
    return storage.get_orders()


@router.post("/")
async def createOrders(
    request: CreateOrderRequest,
    service: InterpretOrderMessageService = Depends(get_interpret_order_message_service),
):
    return service.handle(request.message)
