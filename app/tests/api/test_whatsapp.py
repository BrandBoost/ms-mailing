from unittest import mock

import pytest
from httpx import AsyncClient
from twilio.rest import Client


@pytest.mark.asyncio
async def test_send_messages(async_client: AsyncClient, mocker):
    # Mock the Twilio client and its messages create method
    mock_client = mock.Mock(spec=Client)
    mock_messages_create = mock.Mock()
    mock_client.messages.create = mock_messages_create

    # Replace the original Twilio client with the mock
    mocker.patch('twilio.rest.Client', return_value=mock_client)

    # Define test data
    whatsapp_numbers = ["+375445575448", "+375445575449"]
    text = "Test message"

    # Make the API request to trigger the send_messages function
    response = await async_client.post(
        "api/v1/mailing/whatsapp/send_whatsapp_advertising",
        json={"phones": whatsapp_numbers, "text": text}
    )
    # Assert that the API request was successful
    assert response.status_code == 200
