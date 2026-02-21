from app.delivery_service import DeliveryService

def test_delivery_success():

    service = DeliveryService()

    result = service.assign_delivery(1)

    assert result["delivery_status"] == "OUT_FOR_DELIVERY"
