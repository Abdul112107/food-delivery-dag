from app.order_service import OrderService
from app.payment_service import PaymentService
from app.delivery_service import DeliveryService


def run_food_delivery_pipeline():

    order_service = OrderService()
    payment_service = PaymentService()
    delivery_service = DeliveryService()

    order = order_service.create_order(1001, "Pizza")

    payment = payment_service.process_payment(order["order_id"], 500)

    delivery = delivery_service.assign_delivery(order["order_id"])

    return {
        "order": order,
        "payment": payment,
        "delivery": delivery
    }
