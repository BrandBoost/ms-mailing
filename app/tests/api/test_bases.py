# import pytest
# from httpx import AsyncClient
#
# from app.schemas.bases import RetrieveBases
#
#
# # TODO: implement tests for schemas validators
#
#
# @pytest.mark.asyncio
# async def test_retrieve_all_phones_bases(async_client: AsyncClient, mocker, access_token_with_id):
#     # Mock the phones.get_all_bases_for_user function
#     mock_get_all_bases_for_user = mocker.patch('app.services.bases.get_all_bases_for_user')
#     mock_get_all_bases_for_user.return_value = [
#         RetrieveBases(
#             base_name="Base 1",
#             numbers={"phones": ['+375445575448', '+375445575449'], "text": 'Test ads'},
#             emails={"emails": ['a@gmail.com', 'b@gmail.com'], "text": 'Test ads'},
#             company_id="1",
#             project_id='3',
#             watchers_id=[],
#             is_hide=False
#         ),
#         RetrieveBases(
#             base_name="Base 2",
#             numbers={"phones": ['+375445575441', '+375445575442'], "text": 'Test ads'},
#             company_id="1",
#             emails={"emails": ['c@gmail.com', 'd@gmail.com'], "text": 'Test ads'},
#             project_id='3',
#             watchers_id=[],
#             is_hide=False
#         )
#     ]
#
#     # Perform the request
#     response = await async_client.get("/api/v1/mailing/bases", headers=access_token_with_id)
#
#     # Assertions
#     assert response.status_code == 200
#     assert len(response.json()) == 2
#     assert response.json()[0]["base_name"] == "Base 1"
#     assert response.json()[1]["base_name"] == "Base 2"
#
#     # Ensure the mocked function was called
#     mock_get_all_bases_for_user.assert_called_once_with(user_id="1")
#
#
# @pytest.mark.asyncio
# async def test_retrieve_personal_phones_bases(async_client: AsyncClient, mocker, access_token_with_id):
#     # Mock the PhoneRepository().get_bases_by_company_id repository method
#     mock_get_bases_by_company_id = mocker.patch('app.repositories.BasesRepository.get_bases_by_company_id')
#     mock_get_bases_by_company_id.return_value = [
#         RetrieveBases(
#             base_name="Base 1",
#             numbers={"phones": ['+375445575448', '+375445575449'], "text": 'Test ads'},
#             emails={"emails": ['a@gmail.com', 'b@gmail.com'], "text": 'Test ads'},
#             project_id='3',
#             company_id="2",
#             watchers_id=[],
#             is_hide=False
#         ),
#     ]
#
#     # Perform the request
#     response = await async_client.get("/api/v1/mailing/bases/personal", headers=access_token_with_id)
#
#     # Assertions
#     assert response.status_code == 200
#     assert len(response.json()) == 1
#     assert response.json()[0]["base_name"] == "Base 1"
#
#     # Ensure the mocked method was called
#     mock_get_bases_by_company_id.assert_called_once_with(company_id='1')
#
#
# @pytest.mark.asyncio
# async def test_retrieve_shared_phones_bases(async_client: AsyncClient, mocker, access_token_with_id):
#     # Mock the PhoneRepository().get_shared_bases_by_user_id repository method
#     mock_get_shared_bases_by_user_id = mocker.patch('app.repositories.BasesRepository.get_shared_bases_by_user_id')
#     mock_get_shared_bases_by_user_id.return_value = [
#         RetrieveBases(
#             base_name="Base 3",
#             numbers={"phones": ['+375443575448', '+375425575449'], "text": 'Test ads'},
#             emails={"emails": ['a@gmail.com', 'b@gmail.com'], "text": 'Test ads'},
#             project_id='3',
#             company_id="2",
#             watchers_id=["1", "5"],
#             is_hide=False
#         ),
#         RetrieveBases(
#             base_name="Base 4",
#             numbers={"phones": ['+375445575400', '+375445575401'], "text": 'Test ads'},
#             emails={"emails": ['t@gmail.com', 'g@gmail.com'], "text": 'Test ads'},
#             project_id='3',
#             company_id="2",
#             watchers_id=["1", "7"],
#             is_hide=False
#         )
#     ]
#
#     # Perform the request
#     response = await async_client.get("/api/v1/mailing/bases/shared", headers=access_token_with_id)
#
#     # Assertions
#     assert response.status_code == 200
#     assert len(response.json()) == 2
#     assert response.json()[0]["base_name"] == "Base 3"
#     assert response.json()[1]["base_name"] == "Base 4"
#
#     # Ensure the mocked method was called
#     mock_get_shared_bases_by_user_id.assert_called_once_with(watcher_id='1')
#
#
# @pytest.mark.asyncio
# async def test_retrieve_phones_base(async_client: AsyncClient, mocker, access_token_with_id):
#     # Mock the PhoneRepository().get_by_id repository method
#     mock_get_by_id = mocker.patch('app.repositories.BasesRepository.get_by_id')
#     mock_get_by_id.return_value = {
#         "base_name": "Base 1",
#         "numbers": {"phones ": [], "text": 'test ads'},
#         "emails": {"emails": ['c@gmail.com', 'd@gmail.com'], "text": "test ads"},
#         "company_id": "1",
#         "project_id": "7",
#         "watchers_id": ["4", "5"],
#         "is_hide": False
#     }
#
#     # Perform the request
#     response = await async_client.get("/api/v1/mailing/bases/1", headers=access_token_with_id)
#
#     # Assertions
#     assert response.status_code == 200
#     assert response.json()["base_name"] == "Base 1"
#
#     # Ensure the mocked method was called
#     mock_get_by_id.assert_called_once_with(_id="1")
#
#
# @pytest.mark.asyncio
# async def test_retrieve_phones_base_not_found(async_client: AsyncClient, mocker, access_token_with_id):
#     # Mock the PhoneRepository().get_by_id repository method
#     mock_get_by_id = mocker.patch('app.repositories.BasesRepository.get_by_id')
#     mock_get_by_id.return_value = None
#
#     # Perform the request
#     response = await async_client.get("/api/v1/mailing/bases/1", headers=access_token_with_id)
#
#     # Assertions
#     assert response.status_code == 400
#     assert response.json()["detail"] == "Bad request."
#
#     # Ensure the mocked method was called
#     mock_get_by_id.assert_called_once_with(_id="1")
#
#
# @pytest.mark.asyncio
# async def test_retrieve_phones_base_no_permissions(async_client: AsyncClient, mocker, access_token_with_id):
#     # Mock the PhoneRepository().get_by_id repository method
#     mock_get_by_id = mocker.patch('app.repositories.BasesRepository.get_by_id')
#     mock_get_by_id.return_value = {
#         "_id": "1",
#         "base_name": "Base 1",
#         "numbers": {"phones ": [], "text": 'test ads'},
#         "emails": {"emails": ['c@gmail.com', 'd@gmail.com'], "text": "test ads"},
#         "project_id": "7",
#         "company_id": "3",
#         "watchers_id": ["4", "5"],
#         "is_hide": False
#     }
#
#     # Perform the request
#     response = await async_client.get("/api/v1/mailing/bases/1", headers=access_token_with_id)
#
#     # Assertions
#     assert response.status_code == 403
#     assert response.json()["detail"] == "You have no permissions to perform this action."
#
#     # Ensure the mocked method was called
#     mock_get_by_id.assert_called_once_with(_id="1")
#
#
# @pytest.mark.asyncio
# async def test_create_phones_base(async_client: AsyncClient, mocker, access_token_with_id):
#     # Mock the PhoneRepository().create repository method
#     mock_create = mocker.patch('app.repositories.BasesRepository.create')
#     mock_create.return_value = {
#         "base_name": "Base 1",
#         "numbers": {"phones ": [], "text": 'test ads'},
#         "emails": {"emails": ['c@gmail.com', 'd@gmail.com'], "text": "test ads"},
#         "project_id": "7",
#         "company_id": "1",
#         "watchers_id": [],
#         "is_hide": False
#     }
#
#     # Perform the request
#     payload = {
#         "base_name": "Base 1",
#         "numbers": {"phones ": [], "text": 'test ads'},
#         "emails": {"emails": ['c@gmail.com', 'd@gmail.com'], "text": "test ads"},
#         "project_id": "7",
#         "company_id": "1",
#         "watchers_id": [],
#         "is_hide": False
#     }
#     response = await async_client.post("/api/v1/mailing/bases", json=payload, headers=access_token_with_id)
#
#     # Assertions
#     assert response.status_code == 201
#     assert response.json()["base_name"] == "Base 1"
#
#     # Ensure the mocked method was called
#     mock_create.assert_called_once_with(instance=payload)
#
#
# @pytest.mark.asyncio
# async def test_create_phones_base_bad_request(async_client: AsyncClient, mocker, access_token_with_id):
#     # Mock the PhoneRepository().create repository method
#     mock_create = mocker.patch('app.repositories.BasesRepository.create')
#     mock_create.return_value = None
#
#     # Perform the request
#     payload = {}
#     response = await async_client.post("/api/v1/mailing/bases", json=payload, headers=access_token_with_id)
#
#     # Assertions
#     assert response.status_code == 422
#
#     # Ensure the mocked method was called
#     mock_create.assert_not_called()
#
#
# @pytest.mark.asyncio
# async def test_update_phones_base(async_client: AsyncClient, mocker, access_token_with_id):
#     # Mock the PhoneRepository().update_by_id and PhoneRepository().get_by_id repository methods
#     mock_update_by_id = mocker.patch('app.repositories.BasesRepository.update_by_id')
#     mock_get_by_id = mocker.patch('app.repositories.BasesRepository.get_by_id')
#     mock_get_by_id.return_value = {
#         "_id": "1",
#         "base_name": "Updated Base",
#         "numbers": {"phones ": [], "text": 'test ads'},
#         "emails": {"emails": ['c@gmail.com', 'd@gmail.com'], "text": "test ads"},
#         "project_id": "7",
#         "company_id": "1",
#         "watchers_id": [],
#         "is_hide": False
#     }
#
#     # Perform the request
#     payload = {
#         "base_name": "Updated Base",
#         "numbers": {"phones ": [], "text": 'test ads'},
#         "emails": {"emails": ['c@gmail.com', 'd@gmail.com'], "text": "test ads"},
#         "project_id": "7",
#         "company_id": "1",
#         "watchers_id": [],
#         "is_hide": False
#     }
#     response = await async_client.patch("/api/v1/mailing/bases/1", json=payload, headers=access_token_with_id)
#
#     # Assertions
#     assert response.status_code == 200
#     assert response.json() == {
#         "_id": "1",
#         "base_name": "Updated Base",
#         "numbers": {"phones ": [], "text": 'test ads'},
#         "emails": {"emails": ['c@gmail.com', 'd@gmail.com'], "text": "test ads"},
#         "project_id": "7",
#         "company_id": "1",
#         "watchers_id": [],
#         "is_hide": False
#     }
#
#     # Ensure the mocked methods were called
#     mock_update_by_id.assert_called_once_with(instance_id="1", instance=payload)
#     mock_get_by_id.assert_called_once_with(_id="1")
#
#
# @pytest.mark.asyncio
# async def test_update_phones_base_bad_request(async_client: AsyncClient, mocker, access_token_with_id):
#     # Mock the PhoneRepository().update_by_id and PhoneRepository().get_by_id repository methods
#     mock_update_by_id = mocker.patch('app.repositories.BasesRepository.update_by_id')
#     mock_get_by_id = mocker.patch('app.repositories.BasesRepository.get_by_id')
#
#     # Perform the request with an empty payload
#     payload = {}
#     response = await async_client.patch("/api/v1/mailing/bases/1", json=payload, headers=access_token_with_id)
#
#     # Assertions
#     assert response.status_code == 422
#
#     # Ensure the mocked methods were not called
#     mock_update_by_id.assert_not_called()
#     mock_get_by_id.assert_not_called()
#
#
# @pytest.mark.asyncio
# async def test_update_phones_base_no_permissions(async_client: AsyncClient, mocker, access_token_with_id):
#     # Mock the PhoneRepository().update_by_id and PhoneRepository().get_by_id repository methods
#     mock_update_by_id = mocker.patch('app.repositories.BasesRepository.update_by_id')
#     mock_get_by_id = mocker.patch('app.repositories.BasesRepository.get_by_id')
#     mock_get_by_id.return_value = {
#         "base_name": "Base",
#         "numbers": {"phones ": [], "text": 'test ads'},
#         "emails": {"emails": ['c@gmail.com', 'd@gmail.com'], "text": "test ads"},
#         "project_id": "7",
#         "company_id": "3",
#         "watchers_id": ["4", "5"],
#         "is_hide": False
#     }
#
#     # Perform the request
#     payload = {
#         "base_name": "Updated Base",
#         "numbers": {"phones ": [], "text": 'test ads'},
#         "emails": {"emails": ['c@gmail.com', 'd@gmail.com'], "text": "test ads"},
#         "project_id": "7",
#         "company_id": "3",
#         "watchers_id": ["4", "5"],
#         "is_hide": False
#     }
#     response = await async_client.patch("/api/v1/mailing/bases/1", json=payload, headers=access_token_with_id)
#
#     # Assertions
#     assert response.status_code == 403
#     assert response.json()["detail"] == "You have no permissions to perform this action."
#
#     # Ensure the mocked methods were not called
#     mock_update_by_id.assert_not_called()
#     mock_get_by_id.assert_not_called()
#
#
# @pytest.mark.asyncio
# async def test_delete_phones_base(async_client: AsyncClient, mocker, access_token_with_id):
#     # Mock the PhoneRepository().get_by_id and PhoneRepository().delete_by_id repository methods
#     mock_get_by_id = mocker.patch('app.repositories.BasesRepository.get_by_id')
#     mock_delete_by_id = mocker.patch('app.repositories.BasesRepository.delete_by_id')
#     mock_get_by_id.return_value = {
#         "base_name": "Base 1",
#         "numbers": {"phones ": [], "text": 'test ads'},
#         "emails": {"emails": ['c@gmail.com', 'd@gmail.com'], "text": "test ads"},
#         "project_id": "7",
#         "company_id": "1",
#         "watchers_id": [],
#         "is_hide": False
#     }
#
#     # Perform the request
#     response = await async_client.delete("/api/v1/mailing/bases/1", headers=access_token_with_id)
#
#     # Assertions
#     assert response.status_code == 200
#
#     # Ensure the mocked methods were called
#     mock_get_by_id.assert_called_once_with(_id="1")
#     mock_delete_by_id.assert_called_once_with(_id="1")
#
#
# @pytest.mark.asyncio
# async def test_delete_phones_base_bad_request(async_client: AsyncClient, mocker, access_token_with_id):
#     # Mock the PhoneRepository().get_by_id repository method
#     mock_get_by_id = mocker.patch('app.repositories.BasesRepository.get_by_id')
#     mock_get_by_id.return_value = None
#
#     # Perform the request
#     response = await async_client.delete("/api/v1/mailing/bases/1", headers=access_token_with_id)
#
#     # Assertions
#     assert response.status_code == 400
#     assert response.json()["detail"] == "Bad request."
#
#     # Ensure the mocked methods were not called
#     mock_get_by_id.assert_called_once_with(_id="1")
#
#
# @pytest.mark.asyncio
# async def test_delete_phones_base_no_permissions(async_client: AsyncClient, mocker, access_token_with_id):
#     # Mock the PhoneRepository().get_by_id repository method
#     mock_get_by_id = mocker.patch('app.repositories.BasesRepository.get_by_id')
#     mock_get_by_id.return_value = {
#         "base_name": "Base 1",
#         "numbers": {"phones ": [], "text": 'test ads'},
#         "emails": {"emails": ['c@gmail.com', 'd@gmail.com'], "text": "test ads"},
#         "project_id": "7",
#         "company_id": "5",
#         "watchers_id": ["user_3", "user_4"],
#         "is_hide": False
#     }
#
#     # Perform the request
#     response = await async_client.delete("/api/v1/mailing/bases/1", headers=access_token_with_id)
#
#     # Assertions
#     assert response.status_code == 403
#     assert response.json()["detail"] == "You have no permissions to perform this action."
#
#     # Ensure the mocked methods were not called
#     mock_get_by_id.assert_called_once_with(_id="1")
