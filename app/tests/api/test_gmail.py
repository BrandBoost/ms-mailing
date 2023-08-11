import pytest
from _pytest.logging import LogCaptureFixture
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_send_ads_by_email(async_client: AsyncClient, mocker, caplog: LogCaptureFixture, access_token_with_id):
    # Define test data
    emails = ["test1@example.com", "test2@example.com"]
    text = "Test message"

    # Make the API request to trigger the send_ads_by_email function
    response = await async_client.post(
        "/api/v1/mailing/gmail/send_multi_email_advertising",
        json={"emails": emails, "text": text},
        headers=access_token_with_id
    )

    assert response.status_code == 200
