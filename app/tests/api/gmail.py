from unittest import mock

import pytest

from app.schemas.yandex import YandexApiOrganization, OrganizationSearchQuery


@mock.patch('app.services.yandex.get_all_organizations')
@pytest.mark.asyncio
async def test_retrieve_yandex_organizations(mock_send_yandex_request, async_client):
    search_data = {
        'cities': ["Moscow"],
        'categories': ["Automotive"],
        'email': True,
        'phones': True,
        'only_mobile_phones': False,
        'without_departments': False
    }
    organization_data = {
        'coordinates': [37.764661, 55.719081],
        'address': 'Russia, Moscow, 2nd Viazovskiy Proezd, 4A, Building 5',
        'name': '24-Hour Car Service',
        'categories': [
            {"class": "auto repair", "name": "Car service, auto center"},
            {"class": "tire fitting", "name": "Tire fitting"},
            {"class": "car wash", "name": "Car wash"}
        ],
        'phone': '+7 (495) 778-44-45',
        'description': 'Russia, Moscow, 2nd Viazovskiy Proezd, 4A, Building 5'
    }
    mock_send_yandex_request.return_value = [organization_data]
    response = await async_client.post("api/v1/parsers/yandex/get_organizations", json=search_data)
    assert response.status_code == 200
