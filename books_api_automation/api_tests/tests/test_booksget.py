import allure
from utils.api_client import APIClient

@allure.feature("Books API")
@allure.story("Get all books")
def test_get_all_books(api_client):
    logger = APIClient().getLogger()
    with allure.step("Send GET request"):
        response = api_client.get("/books")

    with allure.step("Validate response"):
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response body: {response.json()}")
        assert response.status_code == 200

        allure.attach(
            str(response.json()),
            name="Books Response",
            attachment_type=allure.attachment_type.JSON
        )
        


@allure.feature("Books API")
@allure.story("Get single book")
def test_get_single_onebook(api_client):
    logger = APIClient().getLogger()

    with allure.step("Send GET request"):
        response = api_client.get("/books/1")

    with allure.step("Validate response"):
        logger.info(f"Response status code: {response.json()}")
        assert response.status_code == 200
        assert "name" in response.json()
        logger.info(f"Book details: {response.json()}")