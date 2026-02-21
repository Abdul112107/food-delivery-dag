import pytest
from app.order_service import OrderService

def test_create_order_success():

    service = OrderService()

    result = service.create_order(1, "Burger")

    assert result["status"] == "CREATED"


def test_create_order_fail():

    service = OrderService()

    with pytest.raises(ValueError):

        service.create_order(1, "")
