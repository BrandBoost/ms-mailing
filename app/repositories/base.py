import typing as tp

from bson import ObjectId

from app.database import MongoManager


class BaseRepository(MongoManager):
    collection: str

    def __init__(self):
        super().__init__()

    async def get_by_id(self, _id: ObjectId) -> tp.Dict[tp.Any, tp.Any] | None:
        return await self.db[self.collection].find_one({"_id": _id})  # type: ignore

    async def get_all(self) -> tp.List[dict]:
        return await self.db[self.collection].find().to_list(length=None)

    async def create(self, instance: dict):
        result = await self.db[self.collection].insert_one(instance)
        return await self.db[self.collection].find_one({"_id": result.inserted_id})  # type: ignore

    async def update_by_id(self, instance_id: ObjectId, instance) -> None:
        await self.db[self.collection].update_one({'_id': instance_id}, {"$set": instance})

    async def delete_by_id(self, _id: tp.Union[str, ObjectId]) -> None:
        user_id = ObjectId(_id) if isinstance(_id, str) else _id
        await self.db[self.collection].delete_one({'_id': user_id})

    # bulk create; bulk update, bulk_delete
