class OrderService:

    def create_order(self, order_id, item):

        if not item:
            raise ValueError("Item cannot be empty")

        return {
            "order_id": order_id,
            "item": item,
            "status": "CREATED"
        }