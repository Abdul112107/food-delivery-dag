class PaymentService:

    def process_payment(self, order_id, amount):

        if amount <= 0:
            raise ValueError("Invalid payment amount")

        return {
            "order_id": order_id,
            "payment_status": "SUCCESS"
        }