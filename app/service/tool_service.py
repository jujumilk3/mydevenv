from app.repository.tool_repository import ToolRepository, ToolToolRelationRepository, ToolTagRelationRepository
from app.service.base_service import BaseService


class ToolService(BaseService):
    def __init__(self, tool_repository: ToolRepository):
        self.tool_repository = tool_repository
        super().__init__(tool_repository)

    async def get_by_name(self, name: str):
        return await self.tool_repository.select_by_name(name=name)

    async def get_by_names(self, names: list[str]):
        return await self.tool_repository.select_by_names(names=names)


class ToolToolRelationService(BaseService):
    def __init__(self, tool_tool_relation_repository: ToolToolRelationRepository):
        self.tool_tool_relation_repository = tool_tool_relation_repository
        super().__init__(tool_tool_relation_repository)

    async def create_with_source_tool_id_target_tool_id(self, source_tool_id: int, target_tool_id: int):
        return await self.tool_tool_relation_repository.insert_with_source_tool_id_target_tool_id(source_tool_id=source_tool_id, target_tool_id=target_tool_id)


class ToolTagRelationService(BaseService):
    def __init__(self, tool_tag_relation_repository: ToolTagRelationRepository):
        self.tool_tag_relation_repository = tool_tag_relation_repository
        super().__init__(tool_tag_relation_repository)

    async def create_with_tool_id_tag_id(self, tool_id: int, tag_id: int):
        return await self.tool_tag_relation_repository.insert_with_tool_id_tag_id(tool_id=tool_id, tag_id=tag_id)

