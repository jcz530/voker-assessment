import json

from fastapi import HTTPException
from openai import OpenAI
from schemas import InterpretedOrderResponse
from services.order_storage import order_storage
from settings import settings


class LLMService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)

    def handle(self, message: str) -> InterpretedOrderResponse:
        try:
            response = self.client.responses.parse(
                model="gpt-4o-2024-08-06",
                input=[
                    {
                        "role": "system",
                        "content": self._get_system_prompt(),
                    },
                    {
                        "role": "user",
                        "content": f"""
                                    <customer_message>
                                        "{message}"
                                    </customer_message>
                                    """,
                    },
                ],
                text_format=InterpretedOrderResponse,
            )
            interpreted_order_response = response.output_parsed

            if interpreted_order_response.errors:
                raise Exception(f"{' '.join(interpreted_order_response.errors)}")

            return interpreted_order_response

        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"Something went wrong processing the order: {str(e)}",
            )

    def _get_system_prompt(self) -> str:
        pending_orders_json = json.dumps(
            [order.model_dump() for order in order_storage.get_pending_orders()],
            indent=2,
        )

        # Adding some validation to this prompt but in a more robust version
        # I would either move or add some validation on the model creation itself
        return f"""
                You are an order processing assistant for a restaurant. 
                Parse the following customer message and determine what actions they want to take.
                Available item types: burger, drink, fries.
                If the user tries to add more than 20 or any item, do not create an order and instead create an error message for the user to read.
                The user cannot add a negative amount of any item, if the user does, create an error message for the user to read.
                Only orders in "<pending_orders>" can be canceled.
                <pending_orders>
                {pending_orders_json}
                </pending_orders>
        """
