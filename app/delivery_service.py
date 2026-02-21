class DeliveryService:

    def assign_delivery(self, order_id):

        return {
            "order_id": order_id,
            "delivery_status": "OUT_FOR_DELIVERY"
        }