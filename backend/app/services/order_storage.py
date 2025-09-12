import datetime
from typing import List

from models import Order

orders: List[Order] = []


class OrderStorageService:
    """Simple global storage for demo purposes instead of implementing a database with migrations and such."""

    def add_order(self, order: Order) -> None:
        """Add an order to the global storage"""
        orders.append(order)

    def get_orders(self) -> List[Order]:
        """Get all orders from storage"""
        return orders.copy()

    def get_pending_orders(self) -> List[Order]:
        """Get all pending (not canceled) orders from storage"""
        return [order for order in orders if order.canceled_at is None]

    def cancel_order(self, order_number: int) -> bool:
        """Cancel/remove an order by ID. Returns True if found and updated."""
        for order in self.get_pending_orders():
            if order.number == order_number:
                # Not using UTC to keep this demo simpler
                order.canceled_at = datetime.datetime.now().isoformat()
                return True
        return False


# Singleton instance
order_storage = OrderStorageService()
