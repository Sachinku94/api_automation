import pytest
import allure
from utils.data_loader import load_csv_data
from utils.api_client import APIClient

test_data = load_csv_data("data/orders.csv")


@allure.feature("Orders API")
@allure.story("Create order using multiple datasets")
@pytest.mark.parametrize("data", test_data)
def test_create_order_ddt(api_client, headers, data):
    logger = APIClient().getLogger()

    with allure.step(f"Request payload: {data}"):
        response = api_client.post("/orders", data, headers)
        logger.info(f"Request payload: {data},{headers}")

    with allure.step("Validate status code"):
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response body: {response.json()}")
        assert response.status_code == 201

    with allure.step("Validate response"):
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response body: {response.json()}")
        res = response.json()
        assert "orderId" in res

        allure.attach(
            str(data),
            name="Request Payload",
            attachment_type=allure.attachment_type.JSON
        )

        allure.attach(
            str(res),
            name="Response",
            attachment_type=allure.attachment_type.JSON
        )