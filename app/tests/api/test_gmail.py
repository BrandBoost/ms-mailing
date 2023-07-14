from unittest import mock

import pytest
from _pytest.logging import LogCaptureFixture
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_send_ads_by_email(async_client: AsyncClient, mocker, caplog: LogCaptureFixture):
    # Mock the send_mail function
    # mock_client = mock.Mock()
    # mock_messages_create = mock.Mock()
    # mock_client.messages.create = mock_messages_create

    # mock_send_mail = mocker.patch("app.services.gmail.send_mail")

    # Define test data
    emails = ["test1@example.com", "test2@example.com"]
    text = "Test message"

    # Make the API request to trigger the send_ads_by_email function
    response = await async_client.post(
        "/api/v1/mailing/gmail/send_multi_email_advertising",
        json={"emails": emails, "text": text},
    )

    assert response.status_code == 200

    # assert "Email successfully sent" in caplog.text
    # mock_send_mail.assert_called_once_with(emails, text)
