import pytest
import random

from tests.utils.api_client import APIClient
@pytest.fixture(scope="session")
def api_client():
    return APIClient()

@pytest.fixture(scope="session")
def auth_token(api_client):
    random_email = f"sachin{random.randint(1000,9999)}@example.com"
    random_name = f"Sachin{random.randint(1000,9999)}"
    logger = APIClient().getLogger()
    payload = {
        "clientName": f"{random_name}",
        "clientEmail": f"{random_email}"
    }
    logger.info(f"Generating auth token with payload: {payload}")
    response = api_client.post("/api-clients/", payload)
    logger.info(f"Auth token response: {response.json()}")
    return response.json()["accessToken"]

@pytest.fixture
def headers(auth_token):
    logger = APIClient().getLogger()
    logger.info(f"Generating headers with auth token: {auth_token}")
    return {
        "Authorization": f"Bearer {auth_token}"
    }