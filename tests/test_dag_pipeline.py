from dag.food_delivery_dag import run_food_delivery_pipeline

def test_pipeline():

    result = run_food_delivery_pipeline()

    assert result["order"]["status"] == "CREATED"
    assert result["payment"]["payment_status"] == "SUCCESS"
    assert result["delivery"]["delivery_status"] == "OUT_FOR_DELIVERY"
