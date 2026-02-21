import pytest
from app.payment_service import PaymentService

def test_payment_success():

    service = PaymentService()

    result = service.process_payment(1, 500)

    assert result["payment_status"] == "SUCCESS"


def test_payment_fail():

    service = PaymentService()

    with pytest.raises(ValueError):

        service.process_payment(1, -10)
