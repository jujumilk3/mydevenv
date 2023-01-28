from app.repository.tag_repository import TagRepository
from app.service.base_service import BaseService


class TagService(BaseService):
    def __init__(self, tag_repository: TagRepository):
        self.tag_repository = tag_repository
        super().__init__(tag_repository)

    async def get_by_name(self, name: str):
        return await self.tag_repository.select_by_name(name=name)

    async def get_by_names(self, names: list[str]):
        return await self.tag_repository.select_by_names(names=names)
