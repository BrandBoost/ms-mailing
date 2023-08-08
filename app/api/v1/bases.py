from typing import List

from fastapi import APIRouter, Request

from app.schemas.bases import CreateUpdateBases, RetrieveBases
from app.services import bases

api_router = APIRouter()


@api_router.get('/', status_code=200, response_model=List[RetrieveBases])
async def retrieve_all_phones_bases(request: Request):
    user_id = request.state.user_id
    return await bases.get_all_bases_for_user(user_id=user_id)


@api_router.get('/personal', status_code=200, response_model=List[RetrieveBases])
async def retrieve_personal_phones_bases(request: Request):
    user_id = request.state.user_id
    return await bases.get_bases_by_company_id(user_id=user_id)


@api_router.get('/shared', status_code=200, response_model=List[RetrieveBases])
async def retrieve_shared_phones_bases(request: Request):
    user_id = request.state.user_id
    return await bases.get_shared_bases_by_user_id(user_id=user_id)


@api_router.get('/{base_id}', status_code=200, response_model=RetrieveBases)
async def retrieve_phones_base(request: Request, phone_db_id: str):
    user_id = request.state.user_id
    return await bases.get_phones_by_id(user_id=user_id, base_id=phone_db_id)


@api_router.post('/', status_code=201, response_model=RetrieveBases)
async def create_phones_base(request: Request, base: CreateUpdateBases):
    user_id = request.state.user_id
    return await bases.create_phones_base(user_id=user_id, instance=base)


@api_router.patch('/{base_id}', status_code=200)
async def update_phones_base(request: Request, phone_db_id: str, base: CreateUpdateBases):
    user_id = request.state.user_id
    return await bases.update_phones_base(user_id=user_id, base_id=phone_db_id, instance=base)


@api_router.delete('/{base_id}', status_code=200)
async def delete_phones_base(request: Request, phone_db_id: str):
    user_id = request.state.user_id
    return await bases.delete_phones_base(user_id=user_id, _id=phone_db_id)
