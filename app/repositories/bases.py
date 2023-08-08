from app.repositories.base import BaseRepository


class BasesRepository(BaseRepository):
    def __init__(self):
        self.collection = 'mailing_projects_database'
        super().__init__()

    async def get_bases_by_company_id(self, company_id: str):
        return await self.db[self.collection].find({"company_id": company_id}).to_list(length=None)

    async def get_bases_by_project_id(self, company_id: str):
        return await self.db[self.collection].find({"project_id": company_id}).to_list(length=None)

    async def get_shared_bases_by_user_id(self, watcher_id: str):
        return await self.db[self.collection].find({"watcher_id": {"$in": [watcher_id]}}).to_list(length=None)
