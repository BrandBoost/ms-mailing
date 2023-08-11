from typing import List

from fastapi import HTTPException

from app.repositories import BasesRepository
from app.schemas.bases import CreateUpdateBases
from app.schemas.bases import RetrieveBases


async def get_phones_by_id(user_id: str, base_id: str) -> RetrieveBases:
    phone_base = await BasesRepository().get_by_id(_id=base_id)
    if not phone_base:
        raise HTTPException(status_code=400, detail='Bad request.')

    if user_id == phone_base.get('company_id') or user_id in phone_base.get('watchers_id'):
        return phone_base
    raise HTTPException(status_code=403, detail='You have no permissions to perform this action.')


async def get_all_bases_for_user(user_id: str) -> List[RetrieveBases]:
    personal_bases = await BasesRepository().get_bases_by_company_id(company_id=user_id)
    shared_bases = await BasesRepository().get_shared_bases_by_user_id(watcher_id=user_id)
    return personal_bases + shared_bases


async def get_bases_by_company_id(user_id: str) -> List[RetrieveBases]:
    return await BasesRepository().get_bases_by_company_id(company_id=user_id)


async def get_shared_bases_by_user_id(user_id: str) -> List[RetrieveBases]:
    return await BasesRepository().get_shared_bases_by_user_id(watcher_id=user_id)


async def update_phones_base(user_id: str, base_id: str, instance: CreateUpdateBases) -> RetrieveBases:
    if user_id == instance.company_id or user_id in instance.watchers_id:
        data = instance.dict(exclude_none=True)
        if not data:
            raise HTTPException(status_code=400, detail='Bad request.')

        await BasesRepository().update_by_id(instance_id=base_id, instance=data)
        return await BasesRepository().get_by_id(_id=base_id)
    else:
        raise HTTPException(status_code=403, detail='You have no permissions to perform this action.')


async def create_phones_base(user_id: str, instance: CreateUpdateBases) -> RetrieveBases:
    instance.company_id = user_id
    data = instance.dict(exclude_none=True)
    return await BasesRepository().create(instance=data)


async def delete_phones_base(user_id: str, _id: str) -> None:
    phone_base = await BasesRepository().get_by_id(_id=_id)
    if not phone_base:
        raise HTTPException(status_code=400, detail='Bad request.')

    if user_id == phone_base.get('company_id'):
        await BasesRepository().delete_by_id(_id=_id)
    else:
        raise HTTPException(status_code=403, detail='You have no permissions to perform this action.')
